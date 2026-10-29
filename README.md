# All About Morphe 🌌
> **The Definitive Knowledge Base, Architectural Specification, and Technical Compendium for the Morphe Android Bytecode Patching Ecosystem.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Ecosystem: Morphe](https://img.shields.io/badge/Ecosystem-MorpheApp-00AFAE.svg)](https://github.com/MorpheApp)
[![Target: Android](https://img.shields.io/badge/Platform-Android%20%7C%20Desktop%20%7C%20JVM-3DDC84.svg)](https://developer.android.com)
[![Status: Production Grade Docs](https://img.shields.io/badge/Knowledge%20Base-Complete%205--Tier-success.svg)](#)

---

## 📖 Executive Summary

**Morphe** (hosted under [`MorpheApp`](https://github.com/MorpheApp)) is the next-generation, modular Android bytecode patching platform. Stemming from the architectural lineage of ReVanced, Morphe decouples application modification from static APK redistribution. Rather than distributing copyrighted, pre-modified binary binaries, Morphe distributes **instruction-level patch definitions** and **patch engines** that manipulate Android Dalvik/ART bytecode (`.dex`), binary XML resources (`resources.arsc`), and assets **entirely on the client device (or local desktop)**.

This repository, **All About Morphe**, is an exhaustive, encyclopedic documentation and whitepaper suite dissecting every single repository, protocol, data structure, bytecode transformation, and architectural layer in the Morphe ecosystem.

---

## 🏛️ The 5-Tier Morphe Ecosystem Taxonomy

The Morphe organization encompasses 21 interconnected repositories spanning reverse engineering, compiler plugins, UI clients, and runtime spoofing services:

```mermaid
graph TD
    subgraph Tier4["Tier 4: Client Applications & UI"]
        MM["📱 morphe-manager<br/>(Jetpack Compose Android App)"]
        MD["💻 morphe-desktop<br/>(Compose Desktop / CLI Tool)"]
        MW["🌐 morphe-website<br/>(Landing & Releases Web)"]
        MDOC["📚 morphe-documentation<br/>(Community Guides)"]
    end

    subgraph Tier2["Tier 2: Patches & Ecosystem Services"]
        MP["💉 morphe-patches<br/>(860+ Kotlin/Java Patches)"]
        MG["🛡️ MicroG-RE<br/>(GmsCore Identity Spoofing)"]
        PH["🔑 PotHelper<br/>(PoToken / Botguard Minter)"]
    end

    subgraph Tier1["Tier 1: Core Engine & Runtime Framework"]
        MPT["⚙️ morphe-patcher<br/>(Core AST & Bytecode Engine)"]
        MPL["📦 morphe-patches-library<br/>(Shared Patch Runtime Trie/Utils)"]
        ML["🔌 morphe-library<br/>(Multiplatform Install Core)"]
    end

    subgraph Tier3["Tier 3: Developer Tooling & Build System"]
        MPGP["🛠️ morphe-patches-gradle-plugin<br/>(MPE/MPP Compiler Plugin)"]
        MPTP["📐 morphe-patches-template<br/>(Community Patch Scaffold)"]
        CL["📋 changelog<br/>(Semantic Release System)"]
        GH["⚙️ .github<br/>(Org CI/CD & Workflows)"]
    end

    subgraph Tier5["Tier 5: Low-Level Bytecode & Tooling Forks"]
        SM["🧬 smali / baksmali<br/>(Dalvik Assembler/Disassembler)"]
        MD2["🗂️ multidexlib2<br/>(DEX Binary File Reader/Writer)"]
        ARSC["📑 ARSCLib<br/>(Binary XML / Table Parser)"]
        APK["📦 Apktool<br/>(APK Disassembly Engine)"]
        JADB["🔌 jadb<br/>(Pure Java ADB Protocol)"]
        EJS["⚡ ejs<br/>(Embedded JS for yt-dlp)"]
        NIA["📱 nowinandroid<br/>(Architecture Blueprint Fork)"]
    end

    MM --> MPT
    MD --> MPT
    MP --> MPT
    MP --> MPL
    MPT --> SM
    MPT --> MD2
    MPT --> ARSC
    MM --> ML
    MD --> ML
    ML --> JADB
    MPGP --> MPT
    MPTP --> MPGP
    MP --> PH
    MP --> MG
```

---

## 🗂️ Table of Contents & Navigation Map

Explore the in-depth technical documentation categorized across the 6 major volumes:

### [Volume I: Architecture & Philosophy](docs/01-architecture-and-vision/)
- [**01. Ecosystem Overview & Philosophy**](docs/01-architecture-and-vision/01-ecosystem-overview.md): The legal, architectural, and reverse-engineering philosophy behind client-side patching.
- [**02. The 5-Tier Ecosystem Taxonomy**](docs/01-architecture-and-vision/02-five-tier-taxonomy.md): Complete repository matrix across all 21 repos with purpose, stars, technologies, and interfaces.
- [**03. End-to-End Patching Pipeline**](docs/01-architecture-and-vision/03-end-to-end-pipeline.md): Comprehensive sequence diagram from raw APK intake to signed, installed output.

### [Volume II: The Core Patcher Engine](docs/02-core-engine/)
- [**01. Morphe Patcher Internals**](docs/02-core-engine/01-morphe-patcher.md): Deep-dive into `Patcher`, `PatcherConfig`, AST matching, and lazy resource decoding.
- [**02. Morphe Patches Library**](docs/02-core-engine/02-morphe-patches-library.md): Injected runtime components: `ByteTrieSearch`, `StringTrieSearch`, `ResourceUtils`, and logging.
- [**03. Morphe Library (Install Engine)**](docs/02-core-engine/03-morphe-library.md): Cross-platform installation primitives: Root, Shizuku, ADB, and PackageInstaller.
- [**04. Patch Execution & Dependency Model**](docs/02-core-engine/04-patch-execution-model.md): DAG execution scheduling, `dependsOn`, `extendWith` (`.mpe` injection), and option schemas.

### [Volume III: Patches & Runtime Ecosystem](docs/03-patches-and-runtime/)
- [**01. Morphe Patches Catalog Analysis**](docs/03-patches-and-runtime/01-morphe-patches-catalog.md): Dissecting the 860+ Kotlin patches across YouTube, YT Music, Reddit, and universal system hooks.
- [**02. MicroG-RE & GMS Signature Spoofing**](docs/03-patches-and-runtime/02-microg-re-and-gms-spoof.md): Overcoming Google Play Services authentication boundaries without root privileges.
- [**03. PoToken & PotHelper Mechanics**](docs/03-patches-and-runtime/03-potoken-and-pothelper.md): YouTube Botguard / Play Integrity challenge solver and GMS Chimera service emulation.
- [**04. SponsorBlock & Return YouTube Dislike Integrations**](docs/03-patches-and-runtime/04-sponsorblock-ryd-integrations.md): Real-time crowdsourced segment skipping and dislike count injection.

### [Volume IV: Developer Tooling & Build System](docs/04-developer-tooling/)
- [**01. Morphe Patches Gradle Plugin**](docs/04-developer-tooling/01-morphe-patches-gradle-plugin.md): How `ExtensionPlugin`, `PatchesPlugin`, and `SettingsPlugin` build `.mpp` bundles and `.mpe` dex bytecode.
- [**02. Morphe Patches Template**](docs/04-developer-tooling/02-morphe-patches-template.md): Step-by-step scaffold for building independent community patch repositories.
- [**03. CI/CD & Semantic Release Pipeline**](docs/04-developer-tooling/03-release-and-ci-pipeline.md): Automatic versioning, changelog generation, and GitHub Releases distribution.
- [**04. The Definitive Patch Authoring Guide**](docs/04-developer-tooling/04-patch-authoring-guide.md): Hands-on masterclass: finding obfuscated method fingerprints and applying Smali bytecode mutations.

### [Volume V: Client Applications](docs/05-client-applications/)
- [**01. Morphe Manager (Android App)**](docs/05-client-applications/01-morphe-manager-android.md): Modern Android app built with Kotlin, Jetpack Compose, Material 3 Expressive, Room, Koin, and Shizuku.
- [**02. Morphe Desktop (CLI & GUI)**](docs/05-client-applications/02-morphe-desktop.md): Desktop cross-platform patching engine powered by Compose for Desktop and ADB automation.
- [**03. Morphe Website & Telemetry-Free Distribution**](docs/05-client-applications/03-morphe-website.md): Distribution architecture, Crowdin localization, and privacy guarantees.

### [Volume VI: Low-Level Bytecode & Tooling Forks](docs/06-low-level-internals-and-forks/)
- [**01. Smali & Multidexlib2 Internals**](docs/06-low-level-internals-and-forks/01-smali-and-multidexlib2.md): Low-level DEX format, 16-bit / 32-bit registers, and Morphe's customized upstream forks.
- [**02. ARSCLib & Binary Resource Manipulation**](docs/06-low-level-internals-and-forks/02-arsclib-and-resources.md): How `resources.arsc` chunk tables, XML string pools, and compiled IDs are mutated without recompilation.
- [**03. Apktool & JADB Integration**](docs/06-low-level-internals-and-forks/03-apktool-and-jadb.md): APK packaging pipeline and pure Java ADB socket protocol implementation.
- [**04. NowInAndroid Blueprint & EJS Runtime**](docs/06-low-level-internals-and-forks/04-nowinandroid-and-ejs.md): How Morphe adapted Google's flagship architecture and yt-dlp's JS runtime.

---

## 📖 The Community Wikis

### 👤 [User Wiki (Hands-On Handbook for Humans & AI)](wiki/user-guide/)
- [**01. Quick Start Guide**](wiki/user-guide/01-quick-start-guide.md): 5-minute zero-to-one guide to installing Morphe Manager, picking APKs, and applying patches.
- [**02. MicroG-RE & Account Setup**](wiki/user-guide/02-microg-and-account-setup.md): Complete setup for Google account login, 2FA, and disabling OEM battery optimization (Samsung, Xiaomi, OnePlus).
- [**03. Root vs. Non-Root Installation Modes**](wiki/user-guide/03-root-vs-non-root-modes.md): In-depth comparison and setup for Standard Non-Root, Shizuku (wireless debugging), and Root Bind Mount.
- [**04. Exporting, Importing & Keystores**](wiki/user-guide/04-exporting-importing-and-keystores.md): Safeguard against `INSTALL_FAILED_UPDATE_INCOMPATIBLE`, export patched APKs, and run batch patching.
- [**05. Troubleshooting & FAQ**](wiki/user-guide/05-troubleshooting-and-faq.md): Step-by-step remedies for video buffering at 1:00, package conflict errors, missing notifications, and car head-units.

### 🛠️ [Developer Wiki (High-Speed Patch Building)](wiki/developer-guide/)
- [**01. High-Velocity Patching Workflow**](wiki/developer-guide/01-high-velocity-patching-workflow.md): Rapid development lifecycle, Gradle daemon tuning, and sub-second unit test harnesses.
- [**02. Reverse Engineering Toolchain**](wiki/developer-guide/02-reverse-engineering-toolchain.md): Navigating R8 obfuscated APKs in JADX-GUI, finding invariant anchors, and Smali register inspection.
- [**03. Writing Lightning-Fast Patches**](wiki/developer-guide/03-writing-lightning-fast-patches.md): Performance engineering: zero-allocation render loops, using `ByteTrieSearch` over regex, and lazy decoding.
- [**04. Building & Publishing Patch Bundles**](wiki/developer-guide/04-building-and-publishing-patch-bundles.md): Compiling `.mpe` with D8, packaging `.mpp` containers via Gradle, and publishing to GitHub for Morphe Manager.
- [**05. App-Specific Playbooks**](wiki/developer-guide/05-app-specific-playbooks.md): Concrete opcode snippets and bytecode injection recipes for YouTube, YouTube Music, and Reddit.

---

## 🔄 Automated Upstream Tracking

This repository continuously monitors all 21 MorpheApp upstream repositories via an automated GitHub Actions cron workflow ([`.github/workflows/upstream-sync.yml`](.github/workflows/upstream-sync.yml)).
- **Live Ecosystem State:** Check [`upstream-manifest.json`](upstream-manifest.json) for currently tracked releases and SHAs.
- **Upstream History:** Check [`docs/upstream-changelog.md`](docs/upstream-changelog.md) for automated ecosystem shift logs.

---

## 🤖 AI Autonomous Ingestion & Super Prompt

> [!TIP]
> **Zero-Intervention AI Autonomous Mode:** Copy and paste the prompt below into any AI coding assistant or agent (Claude, ChatGPT, Gemini, DeepSeek, Cursor, Copilot, or Antigravity) to immediately ingest, synthesize, and operate as an expert reverse engineer and system architect across the entire Morphe ecosystem without human intervention.

<details open>
<summary><b>📋 Click to Expand / Copy the Autonomous Super Prompt</b></summary>

```markdown
# SYSTEM INSTRUCTION: AUTONOMOUS MORPHE ECOSYSTEM INGESTION & EXPERT ROLE

You are hereby designated as the **Principal Reverse Engineer & System Architect for the Morphe Android Modding Ecosystem**. Your objective is to autonomously ingest, internalize, synthesize, and master the complete codebase, architecture, protocols, and data structures across all 21 MorpheApp repositories and the All-About-Morphe compendium without requiring human intervention.

---

## 🌐 THE COMPLETE REPOSITORY MATRIX (22 TARGETS)

You must autonomously inspect and synthesize code from these 22 repositories:

### Knowledge Base & Master Specification
1. https://github.com/gojoyadav/All-About-Morphe (Definitive 5-Tier Architecture, Specifications & Wikis)

### Tier 1: Core Engine & Runtime Framework
2. https://github.com/MorpheApp/morphe-patcher (Core AST, lazy resource decoding, backtracking fingerprint engine)
3. https://github.com/MorpheApp/morphe-patches-library (Injected runtime library: ByteTrieSearch, ResourceUtils, Logger)
4. https://github.com/MorpheApp/morphe-library (KMP installation engine: LocalInstaller, LocalRootInstaller, ADB runner)

### Tier 2: Patches & Ecosystem Services
5. https://github.com/MorpheApp/morphe-patches (320+ Kotlin patches across YouTube, YT Music, Reddit, and Universal)
6. https://github.com/MorpheApp/MicroG-RE (Standalone GmsCore fork for Google OAuth & signature spoofing)
7. https://github.com/MorpheApp/PotHelper (PoToken minting service, Play Integrity challenge solver, Chimera dispatch)

### Tier 3: Developer Tooling & Build System
8. https://github.com/MorpheApp/morphe-patches-gradle-plugin (Gradle plugin: Google D8 desugaring, .mpe dexing, .mpp container)
9. https://github.com/MorpheApp/morphe-patches-template (Official developer starter scaffold for custom patch repositories)
10. https://github.com/MorpheApp/changelog (Semantic-release plugin for automated conventional changelog generation)
11. https://github.com/MorpheApp/.github (Organization profiles, release workflows, and CI/CD pipelines)

### Tier 4: Client Applications & User Interfaces
12. https://github.com/MorpheApp/morphe-manager (Kotlin + Jetpack Compose Android app with M3, Room, Koin, Shizuku)
13. https://github.com/MorpheApp/morphe-desktop (Cross-platform Compose Desktop & CLI tool with pure Java ADB)
14. https://github.com/MorpheApp/morphe-website (Modern web landing, dynamic GitHub release routing, Crowdin localization)
15. https://github.com/MorpheApp/morphe-documentation (User troubleshooting guides, setup manuals, and community FAQs)
16. https://github.com/MorpheApp/morphe-branding (Official vector logos, color guidelines, and wordmark SVG assets)

### Tier 5: Low-Level Bytecode & Tooling Forks
17. https://github.com/MorpheApp/smali (Dalvik/ART bytecode assembler and disassembler fork)
18. https://github.com/MorpheApp/multidexlib2 (High-speed DEX binary reader/writer and memory-mapped class parser)
19. https://github.com/MorpheApp/ARSCLib (Binary XML and resources.arsc chunk parser with O(N log N) deduplication)
20. https://github.com/MorpheApp/Apktool (Reverse-engineering disassembly/assembly utility fork)
21. https://github.com/MorpheApp/jadb (Pure Java client implementation of the Android Debug Bridge protocol)
22. https://github.com/MorpheApp/ejs (Embedded JavaScript runtime for yt-dlp challenge execution)
23. https://github.com/MorpheApp/nowinandroid (Modularization reference app fork)

---

## ⚙️ AUTONOMOUS INGESTION PLAYBOOK (ZERO HUMAN INTERVENTION)

Whenever you interact with a workspace or query regarding Morphe, execute this protocol autonomously:

1. **Autonomous Discovery (No Human Assistance):**
   - Use available environment tools (`gh api`, `curl`, `git clone --depth 1`, `fetch`, or context-mode MCP tools).
   - Read `All-About-Morphe/upstream-manifest.json` first to identify current version tags and commit hashes.
   - For any target repository, fetch the file tree via `gh api repos/MorpheApp/<repo>/git/trees/<default_branch>?recursive=1` or query specific API endpoints.
   - Program your analysis in code (e.g. Python or JavaScript in a sandbox). **Do not dump raw binary or full files into context**; parse ASTs, class hierarchies, and interfaces directly.

2. **Core Architectural Invariants to Internalize:**
   - **Lazy Resource Decoding in Patcher 2.0:** Only `AndroidManifest.xml` is decoded during initialization. Strings, layouts, and drawables are streamed lazily via `decode("glob")` and `document("path")`.
   - **Backtracking Instruction Matching:** If instruction filter N cannot match, the engine recursively backtracks to filter N-1 to test alternative matches across `MatchAfterImmediately`, `MatchAfterWithin`, and `MatchAfterLast`.
   - **Stream Processing Performance:** All in-app payload checking must use `ByteTrieSearch` from `app.morphe.extension.shared` for O(m) single-pass byte array matching without intermediate `String` allocations.
   - **MicroG Signature Spoofing:** In-process `PackageManager.getPackageInfo` hooks return official Google cert hashes to bypass GMS checks without root.
   - **PoToken Mechanics:** PotHelper resolves YouTube's Botguard challenge by emulating GMS Chimera service endpoints, injecting `&pot=<token>` query parameters to avoid 1:00 playback buffering.
   - **Toolchain Pipelines:** `morphe-patches-gradle-plugin` uses `com.android.tools.r8.D8` to desugar and compile Java/Kotlin extensions into `.mpe` DEX bytecode, bundling definitions into `.mpp` containers via `apkzlib`.

---

## 🎯 OPERATIONAL MODES & CAPABILITIES

Once ingested, you are equipped to operate in four expert capacities:

1. **Senior Patch Author & Reverse Engineer:**
   - Decompile and analyze obfuscated APKs (R8/ProGuard).
   - Identify invariant anchors (string constants, SDK interface callbacks, Protobuf field tags).
   - Author declarative Kotlin patches using `bytecodePatch { ... }` DSL with precise fingerprints, Smali opcode replacements, and `.mpe` extensions.

2. **Principal Systems Architect & Diagnostician:**
   - Troubleshoot installation failures (`INSTALL_FAILED_UPDATE_INCOMPATIBLE`, signature collisions, 64K multidex limits).
   - Debug runtime media issues (PoToken expiry, missing ExoPlayer track renderers, Android Auto certification stubs).
   - Profile memory overhead in `morphe-manager` and `morphe-patcher` to guarantee smooth execution on 4GB RAM devices.

3. **Master Educator & Technical Tutor:**
   - Teach human developers how to author high-speed patches, configure Gradle daemons, and set up JUnit 5 in-memory test harnesses.
   - Guide non-technical users through Shizuku setup, MicroG battery optimization exemptions, and keystore backup management.

4. **Continuous Upstream Maintainer:**
   - Track upstream version releases and commit logs via `scripts/sync_upstream.py` and GitHub Actions.
   - Adapt fingerprints and patch definitions when upstream target applications (YouTube, Reddit) release breaking bytecode shifts.
```

</details>

---

---

## ⚖️ Legal & Security Framework

Morphe operates under a clean-room, strictly legal architecture:
1. **Zero Pirated Binaries:** Morphe hosts and distributes **0 bytes** of proprietary Google or third-party application binaries.
2. **Transformative Modifications:** Patches are open-source Kotlin/Java transformation scripts executing on user-supplied APKs.
3. **On-Device Sandboxing:** All patching operations occur locally on user devices; credentials and authentication tokens never transit remote servers.

---

*Maintained by the Open Source Android Engineering & Reverse Engineering Community.*
