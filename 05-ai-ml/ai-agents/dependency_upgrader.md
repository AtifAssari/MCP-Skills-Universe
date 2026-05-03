---
title: dependency-upgrader
url: https://skills.sh/jmerta/codex-skills/dependency-upgrader
---

# dependency-upgrader

skills/jmerta/codex-skills/dependency-upgrader
dependency-upgrader
Installation
$ npx skills add https://github.com/jmerta/codex-skills --skill dependency-upgrader
SKILL.md
Dependency upgrader
Goal

Safely upgrade dependencies with minimal, reviewable diffs and clear verification.

Inputs to ask for (if missing)
Which ecosystem: Gradle/Maven, Node/TypeScript, or both.
Scope: one dependency, a set (e.g., Spring Boot), or "everything".
Constraints: patch/minor only vs allow majors; time budget; CI requirements.
Motivation: CVE fix, feature need, or routine maintenance.
Can the agent use web search to confirm latest versions and read migration notes? (If not, rely on registry lookups.)
Workflow (checklist)
Detect the project type and package manager
Node: package.json + lock file (pnpm-lock.yaml, package-lock.json, yarn.lock, bun.lock).
Gradle: gradlew, build.gradle(.kts), settings.gradle(.kts), gradle/libs.versions.toml.
Maven: pom.xml.
If the required package manager or build tool is missing (npm/pnpm/yarn/bun, Gradle, Maven), tell the user and ask whether to install it or proceed with a manual edit-only upgrade.
Establish a baseline
Record current versions (dependency file + lock files).
Run the smallest reliable test/build command the repo uses (then expand if needed).
Plan the upgrade
Prefer the smallest bump that solves the problem.
Choose target versions using up-to-date sources:
Use web search (if available) to confirm latest stable versions and skim official release notes/migration guides.
Cross-check with the registry/source of truth (npm registry, Maven Central, Gradle Plugin Portal).
Group by risk:
low: patches/minors, leaf deps
medium: build tools/plugins
high: framework majors (Spring Boot), runtime bumps (Java/Node)
For majors: skim upstream migration notes and list expected breakpoints before editing.
Apply upgrades incrementally
Update one group at a time; keep diffs focused.
After each group: run tests/build and fix breakages immediately.
Use the playbooks in references/ for ecosystem-specific commands.
Validate and document
Run the repo's "CI equivalent" commands (tests + build).
Document:
what changed (versions)
why (CVE, compatibility, feature)
notable migrations or breaking changes
any follow-ups (deprecations, future majors)
Deliverable

Provide:

The list of version bumps (old -> new).
The commands run and their result (tests/build).
Any breaking changes and required code/config migrations.
Weekly Installs
23
Repository
jmerta/codex-skills
GitHub Stars
126
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass