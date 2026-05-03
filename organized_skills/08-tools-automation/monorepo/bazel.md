---
rating: ⭐⭐⭐
title: bazel
url: https://skills.sh/checkmk/checkmk/bazel
---

# bazel

skills/checkmk/checkmk/bazel
bazel
Installation
$ npx skills add https://github.com/checkmk/checkmk --skill bazel
SKILL.md
Repo-specific flags
# Edition (affects which cmk targets are built/tested)
--cmk_edition=community|pro|ultimate|ultimatemt|cloud

# Configs defined in .bazelrc
--config=mypy      # type checking
--config=clippy    # Rust linting

# CI excludes these to avoid xunit parser issues (fine to include locally)
-//packages/livestatus/... -//packages/neb/... -//packages/unixcat/...

Weekly Installs
40
Repository
checkmk/checkmk
GitHub Stars
2.3K
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass