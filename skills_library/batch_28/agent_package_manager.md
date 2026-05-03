---
title: agent-package-manager
url: https://skills.sh/webmaxru/agent-skills/agent-package-manager
---

# agent-package-manager

skills/webmaxru/agent-skills/agent-package-manager
agent-package-manager
Installation
$ npx skills add https://github.com/webmaxru/agent-skills --skill agent-package-manager
SKILL.md
Agent Package Manager
Procedures

Step 1: Assess the repository and the requested APM outcome

Inspect the repository root for apm.yml, apm.lock.yaml, .github/, .claude/, .cursor/, .opencode/, and apm_modules/.
Execute apm --version and apm config to confirm the installed CLI and current configuration.
If apm.yml exists, read references/manifest-and-lockfile.md before changing dependencies, scripts, or compilation settings.
If the request is about package installation, updates, pruning, or removal, read references/command-workflows.md before executing APM commands.
If no apm.yml exists and the user wants APM in the repository, initialize the project with apm init or apm init --yes.
If the repository already uses another agent configuration flow and the user did not ask to migrate it, limit the change to the requested APM scope instead of replacing the existing setup.

Step 2: Shape or repair the manifest deliberately

Read assets/apm.yml.template when the repository needs a fresh or repaired manifest structure.
Keep name and version present at the top level; treat them as required contract fields.
Add APM package dependencies under dependencies.apm and MCP servers under dependencies.mcp.
Prefer canonical dependency forms in apm.yml after installation. Default to the repository shorthand owner/repo/path for GitHub-hosted skills and packages, for example webmaxru/agent-skills/skills/webmcp, and preserve explicit path, ref, and alias only when they are needed.
Use pinned refs for shared team packages when reproducibility matters more than automatic drift.
Keep local path dependencies only for active local development. Replace them with remote references before recommending bundle distribution.
If the request includes scripts, define them under scripts and verify that each script can be previewed or executed through apm list, apm preview, or apm run.

Step 3: Manage dependencies with verification, not guesswork

Preview risky changes with apm install --dry-run, apm uninstall --dry-run, or apm prune --dry-run when the repository already has installed packages.
Install or update packages with apm install, apm install <package>, apm install --update, or apm deps update according to the requested scope.
After running apm install --update or apm deps update, verify the lockfile resolved_commit actually changed. If packages were served from a stale cache, follow the "Stale packages after update" workflow in references/troubleshooting.md.
When the request is to install a single skill from a repository, provide the package path down to that skill directory instead of a vague repo-only placeholder, for example apm install webmaxru/agent-skills/skills/webmcp.
Verify the resolved state with apm deps list, apm deps tree, or apm deps info <package> after dependency changes.
Treat apm.lock.yaml as the source of truth for resolved commits and deployed files. Recommend committing it for team and CI reproducibility.
If the repository needs MCP discovery or selection, use apm mcp list, apm mcp search <query>, and apm mcp show <server> before editing MCP entries by hand.
If installation output reports collisions or skipped files, read references/troubleshooting.md before retrying with forceful options.
If the repository consumes packages from itself (self-referencing dependency), remind the user that changes must be committed and pushed before APM can fetch them. Read references/troubleshooting.md for the "Self-referencing dependencies" section.

Step 4: Compile and validate only when it adds value

Read references/command-workflows.md before changing compilation strategy or target selection.
Use apm compile --validate to validate primitives when the goal is correctness rather than output generation.
Use apm compile --dry-run before large compilation changes or when checking placement decisions.
Explain that apm install already deploys prompts, agents, skills, hooks, and MCP integrations for supported tools; apm compile mainly exists to generate instruction files such as AGENTS.md or CLAUDE.md.
Use explicit targets when the repository serves more than one runtime or tool family.
Keep compilation.exclude aligned with build and dependency directories so compilation does not re-scan generated output.
If the project needs continuous regeneration during authoring, use apm compile --watch only after the one-shot validation path is clean.

Step 5: Operate scripts, runtimes, and distribution flows professionally

List project scripts with apm list before invoking them.
Preview prompt-driven scripts with apm preview <script> -p key=value before using apm run <script> -p key=value in an automation or debugging workflow.
Use apm runtime status, apm runtime list, and apm runtime setup <runtime> when the repository depends on an APM-managed runtime.
If the goal is CI fan-out, air-gapped delivery, or release traceability, read references/command-workflows.md and use apm pack only after a successful install has produced apm.lock.yaml and deployed files.
Use apm unpack only for additive extraction of a previously packed bundle. Do not present it as a replacement for dependency authoring.
Recommend apm-action or a prebuilt bundle when repeated installs create avoidable CI cost or network risk.
Error Handling
If apm is missing, install or update it first, then verify with apm --version before editing project files.
If apm install reports authentication failures, read references/troubleshooting.md and fix host authentication before retrying.
If apm install reports file collisions, inspect the diagnostic summary, retry with --verbose when needed, and use --force only when overwriting local files is clearly intended.
If apm compile is unnecessary for the user’s toolchain, avoid adding it as busywork; prefer the lighter install-only path.
If apm pack fails because apm.lock.yaml is missing or deployed files are absent, rerun apm install before retrying.
If the repository depends on local path packages, do not recommend apm pack until those dependencies are replaced with remote references.
Weekly Installs
83
Repository
webmaxru/agent-skills
GitHub Stars
27
First Seen
Mar 15, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn