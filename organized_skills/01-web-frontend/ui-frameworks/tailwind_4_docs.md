---
rating: ⭐⭐
title: tailwind-4-docs
url: https://skills.sh/lombiq/tailwind-agent-skills/tailwind-4-docs
---

# tailwind-4-docs

skills/lombiq/tailwind-agent-skills/tailwind-4-docs
tailwind-4-docs
Installation
$ npx skills add https://github.com/lombiq/tailwind-agent-skills --skill tailwind-4-docs
SKILL.md
Tailwind 4 Docs
Overview

Use this skill to navigate a locally synced Tailwind CSS v4 documentation snapshot and answer development, configuration, migration, implementation, refactor, and review questions with official guidance.

The docs snapshot is not bundled with this skill because the upstream repository is source-available but not open-source. Users must initialize the snapshot themselves and are responsible for complying with the upstream license.

Quick start
Check whether the docs snapshot is initialized (references/docs/ and references/docs-index.tsx exist).
If the snapshot is missing or older than one week, stop and ask to run the initialization step in "Initialization" before continuing. Do not answer the user's question until the snapshot is initialized.
Identify the topic (utility, variant, config, migration, compatibility, implementation, refactor, review).
Find the matching doc in references/docs-index.tsx.
Load only the relevant file from references/docs/.
For implementation, refactor, or review tasks, also load references/engineering-playbook.md.
Apply guidance and call out any breaking changes or constraints.
Initialization (required once per install)

Run the sync script to download the Tailwind docs locally. This requires network access, git, and Python 3:

python skills/tailwind-4-docs/scripts/sync_tailwind_docs.py --accept-docs-license


This pulls content from tailwindlabs/tailwindcss.com. That repo is source-available and explicitly not open-source, so the user must accept its license before downloading and keep the snapshot local.

If you cannot run tools or have no internet access, ask the user to run the exact command above in a terminal, then continue once references/docs/ and references/docs-index.tsx exist.

If the snapshot is missing or older than one week, you must ask for permission to run the command or ask the user to run it. Do not proceed with Tailwind guidance until the snapshot is initialized or refreshed.

If initialization is blocked (no internet or no write access), use references/gotchas.md as a limited fallback and ask the user to consult the official docs. For implementation, refactor, or review tasks, references/engineering-playbook.md can also serve as a limited fallback.

References map
references/docs/ is generated locally and contains the Tailwind v4 MDX docs snapshot.
references/docs-index.tsx is generated locally and contains the category and slug map used by the docs sidebar.
references/docs-source.txt captures the upstream repo, commit, and snapshot date (or reports that initialization is pending).
references/engineering-playbook.md is the agent-oriented implementation, refactor, and review guide.
references/gotchas.md provides a quick scan of common v4 migration pitfalls.
MDX handling
Treat export const title and export const description as metadata.
Read JSX callouts like <TipInfo> or <TipBad> as guidance text.
Common entry points
Migration: references/docs/upgrade-guide.mdx, references/docs/compatibility.mdx.
Implementation/refactor/review: references/engineering-playbook.md.
Gotchas overview: references/gotchas.md.
Configuration and directives: references/docs/functions-and-directives.mdx, references/docs/adding-custom-styles.mdx, references/docs/theme.mdx.
Variants and responsive patterns: references/docs/hover-focus-and-other-states.mdx, references/docs/responsive-design.mdx.
Core behavior: references/docs/preflight.mdx, references/docs/detecting-classes-in-source-files.mdx.
Migration checklist

When upgrading from v3 to v4, always confirm the following in the docs:

Browser support and compatibility expectations.
Tooling changes: @tailwindcss/postcss, @tailwindcss/cli, @tailwindcss/vite.
Import syntax: @import "tailwindcss" replaces @tailwind directives.
Utility renames/removals, prefix format, and important modifier placement.
Changes to variants, transforms, and arbitrary value syntax.
Update workflow

Run scripts/sync_tailwind_docs.py to refresh the snapshot. Use --local-repo if you already have a local clone of tailwindlabs/tailwindcss.com to speed up syncs. Always pass --accept-docs-license.

Weekly Installs
492
Repository
lombiq/tailwind…t-skills
GitHub Stars
27
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn