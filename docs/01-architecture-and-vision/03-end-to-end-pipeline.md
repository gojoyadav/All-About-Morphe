# Volume I: Chapter 3 — End-to-End Patching Pipeline

The Morphe patching pipeline is the orchestrated sequence of operations that transforms an unmodified stock Android APK into a fully patched, feature-enhanced, and signed APK.

---

## 🔁 Complete Lifecycle Sequence Diagram

```mermaid
sequenceDiagram
    autonumber
    actor User as End User
    participant Manager as Morphe Manager (Android / Desktop)
    participant Engine as Morphe Patcher (JVM Engine)
    participant Decoders as ARSCLib & Smali/Dex
    participant Patches as Morphe Patches Bundle (.mpp)
    participant Signer as Android ZipSigner / ApkSigner
    participant OS as Android OS (PackageInstaller / Shizuku / Root)

    User->>Manager: 1. Select Target App (e.g., YouTube v19.xx)
    Manager->>Manager: 2. Verify APK Architecture & Version Compatibility
    User->>Manager: 3. Select Patches (MicroG, AdBlock, SponsorBlock, etc.)
    Manager->>Engine: 4. Instantiate Patcher(PatcherConfig(apkFile))
    
    rect rgb(240, 248, 255)
        note right of Engine: Disassembly & AST Construction Phase
        Engine->>Engine: 5. Unpack APK ZIP container to memory/temp storage
        Engine->>Decoders: 6. Parse AndroidManifest.xml (lazy decode)
        Engine->>Decoders: 7. Open and index classes*.dex via multidexlib2
    end

    rect rgb(255, 245, 238)
        note right of Engine: Patch Resolution & Execution Phase
        Engine->>Patches: 8. Build DAG (Directed Acyclic Graph) of selected patches
        Engine->>Patches: 9. Topological sort on dependencies (dependsOn)
        loop For each Patch in sorted DAG
            Engine->>Patches: 10. Check compatibleWith(packageMetadata)
            alt Patch has precompiled DEX extension (.mpe)
                Patches->>Engine: 11. Merge extension DEX classes into target DEX pool
            end
            Engine->>Decoders: 12. Run Fingerprint searches (Backtracking opcode filter)
            Decoders-->>Engine: 13. Return target Method/Class reference
            Engine->>Engine: 14. Execute AST bytecode mutations (smali instruction insertion/replacement)
            opt If patch modifies resources
                Engine->>Decoders: 15. Decode targeted XML/ARSC table on demand
                Engine->>Engine: 16. Mutate binary XML attributes or string values
            end
        end
    end

    rect rgb(245, 255, 245)
        note right of Engine: Compilation & Assembly Phase
        Engine->>Decoders: 17. Recompile modified resources.arsc table
        Engine->>Decoders: 18. Re-serialize modified DEX classes into classes*.dex
        Engine->>Manager: 19. Emit modified ZIP entries
        Manager->>Manager: 20. Align ZIP entries (4-byte alignment via zipalign)
        Manager->>Signer: 21. Sign APK with custom keystore (v1, v2, and v3 signatures)
    end

    rect rgb(255, 250, 240)
        note right of Manager: Deployment & Installation Phase
        alt Root mode enabled
            Manager->>OS: 22a. Direct Mount APK into /data/app via libsu
        else Shizuku enabled
            Manager->>OS: 22b. Install via Shizuku PackageInstaller API
        else Standard Non-Root
            Manager->>OS: 22c. Prompt user via system PackageInstaller session
        end
        OS-->>User: 23. Installation Complete & App Launchable
    end
```

---

## 🔍 Detailed Phase Breakdown

### Phase 1: Ingestion & Verification
1. **APK Extraction:** The user selects either an APK file downloaded from an APK mirror or the currently installed base APK extracted from `/data/app/*`.
2. **Compatibility Evaluation:** The `PackageMetadata` extractor reads `packageName`, `versionCode`, and `versionName` directly from the APK's binary manifest. It evaluates these values against the patch's declared `Compatibility` rules.

### Phase 2: In-Memory Indexing & Lazy Resource Decoding
1. In Morphe Patcher 2.0, resources are **not eagerly decoded**. Prior engines extracted every PNG, layout, and string pool, consuming hundreds of megabytes of RAM.
2. Only `AndroidManifest.xml` is decoded during initialization to obtain package identifiers and component declarations.
3. All DEX files (`classes.dex`, `classes2.dex`, `...`, `classesN.dex`) are indexed using `multidexlib2` into mutable class definition wrappers (`MutableClassDef`).

### Phase 3: DAG Dependency Resolution
1. Patches declare dependencies via `dependsOn(otherPatch)`.
2. A Directed Acyclic Graph (DAG) is constructed.
3. The engine performs a **topological sort** (Kahn's algorithm / DFS post-order). If cycles are detected, patching is aborted immediately with an explanatory error.

### Phase 4: Fingerprint Matching & AST Bytecode Mutation
1. For each patch, the engine evaluates its `MethodFingerprint` or `ClassFingerprint`.
2. Rather than hardcoded offsets, fingerprints match:
   - Specific opcode sequences (e.g., `sget-object`, `check-cast`, `invoke-virtual`).
   - String literals (e.g., `"player_response"`, `"ad_break"`).
   - Parameter and return type signatures.
3. **Backtracking Filter Matching:** If instruction 3 of a 5-instruction filter fails, Morphe backtracks to find the next valid instance of instruction 1 and retries.
4. Once located, bytecode mutations are applied:
   - Hook injection: Inserting `invoke-static {p0}, Lapp/morphe/extension/...;->hookMethod(...)V`.
   - Register manipulation: Replacing registers or branching instructions (`goto`, `return-void`).

### Phase 5: Merging Patch Extensions (`.mpe`)
1. Patches often need rich custom Java/Kotlin logic (such as an embedded HTTP client for SponsorBlock, or a custom UI dialog for settings).
2. Writing this in raw smali assembly would be error-prone and unmaintainable.
3. Instead, extensions are written in pure Java/Kotlin, compiled by Gradle into standalone DEX bytecode (`.mpe`), and merged directly into the target APK's DEX pool by Morphe Patcher.

### Phase 6: Binary Resource & ARSC Table Encoding
1. Modifications to string resources, themes, colors, and layout XML files are written back to `resources.arsc` using `ARSCLib`.
2. ARSCLib avoids full recompilation by directly modifying binary chunk tables, string pools, and entry maps.

### Phase 7: ZipAligning, Signing & Delivery
1. The modified DEX and ARSC files are repacked into a zip archive.
2. **4-Byte Alignment (ZipAlign):** Uncompressed data is 4-byte aligned to allow `mmap` optimization by Android's ART runtime.
3. **Cryptographic Signing:** The APK is signed with a generated custom keystore using Android's APK Signature Scheme v2/v3.
4. **Installation:** Delivered to the OS via Android's `PackageInstaller.Session`, Shizuku IPC, or root bind-mount.
