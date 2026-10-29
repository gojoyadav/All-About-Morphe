# Project Instructions (GEMINI.md)

This file contains foundational mandates for Antigravity / Gemini CLI when working in this workspace. These instructions take precedence over general defaults.

## Project Scope
- **Repository:** `All-About-Morphe` (https://github.com/gojoyadav/All-About-Morphe)
- **Objective:** The definitive, exhaustive knowledge base and technical whitepaper compendium for the Morphe Android Patching Ecosystem (covering all 21 MorpheApp repositories).
- **Format:** Pure GitHub-Flavored Markdown with architectural specifications, Mermaid sequence/class/flowchart diagrams, bytecode deep-dives, reverse-engineering analyses, and developer tutorials.

## Resource & Performance Mandates
- **No Local Builds:** NEVER run `./gradlew assembleDebug`, `flutter build apk`, or any command that performs a full APK/binary build locally. The host machine is limited to **4 GB RAM**.
- **Remote Verification:** Use GitHub Actions (CI/CD) for all build verifications and APK generation.

## Coding & Documentation Standards
- **Surgical Precision:** Adhere to surgical precision for all code and document modifications.
- **Deep Technical Rigor:** Never leave placeholders or shallow summaries. Include actual class names, bytecode instructions, package structures, Gradle plugin tasks, and reverse-engineering insights.
- **context-mode MCP:** Always use context-mode MCP tools (`ctx_execute`, `ctx_batch_execute`, `ctx_execute_file`, `ctx_search`) to query and inspect upstream repositories.

## Project Tracking & Documentation
- **Version.md Mandate:** Every project must contain a `Version.md` file. This file is the absolute source of truth for the project's evolution.
  - **Exhaustive Logging:** Track every changelog entry, library, method, and file version.
  - **CRITICAL: Strict Append Pattern:** 
    - **NEVER** use the replace tool or any method to edit, delete, or "update" existing lines in `Version.md`.
    - **ONLY** use `write_file` (with the full content) or append methods to add new entries at the bottom.
    - **NO STATUS UPDATES:** Do not update the "Status" line of a previous entry. If a status changes (e.g., from 90% to 100%), append a NEW entry with the new status.
    - **Immutable History:** Once information is written, it is permanent.
  - **Real-time Updates:** Log changes immediately after completion.
  - **Metadata:** Every entry must be logged with the current date and time.
- **Mandatory Pre-Work Protocol (Always Read First):**
  - **Sequential Prerequisite:** You will ALWAYS read `Version.md` and `GEMINI.md` of that repository before starting any work on that repo.
  - **Zero Exceptions:** ONLY after thoroughly reading both `Version.md` and `GEMINI.md` are you permitted to analyze, plan, execute commands, or modify files within that repository.
