---
title: claude-code-plugin-release
url: https://skills.sh/thedotmack/claude-mem/claude-code-plugin-release
---

# claude-code-plugin-release

skills/thedotmack/claude-mem/claude-code-plugin-release
claude-code-plugin-release
Installation
$ npx skills add https://github.com/thedotmack/claude-mem --skill claude-code-plugin-release
SKILL.md
Version Bump & Release Workflow

IMPORTANT: Plan and write detailed release notes before starting.

CRITICAL: Commit EVERYTHING (including build artifacts). At the end of this workflow, NOTHING should be left uncommitted or unpushed. Run git status at the end to verify.

Preparation

Analyze: Determine if the change is PATCH (bug fixes), MINOR (features), or MAJOR (breaking).

Environment: Identify repository owner/name from git remote -v.

Paths — every file that carries the version string:

package.json — the npm/npx-published version (npx claude-mem@X.Y.Z resolves from this)
plugin/package.json — bundled plugin runtime deps
.claude-plugin/marketplace.json — version inside plugins[0].version
.claude-plugin/plugin.json — top-level Claude-plugin manifest
plugin/.claude-plugin/plugin.json — bundled Claude-plugin manifest
.codex-plugin/plugin.json — Codex-plugin manifest
openclaw/openclaw.plugin.json — OpenClaw plugin manifest

Verify coverage before editing: git grep -l "\"version\": \"<OLD>\"" should list all seven. If a new manifest has been added since this doc was last updated, update this list.

Workflow
Update: Increment the version string in every path above. Do NOT touch CHANGELOG.md — it's regenerated.
Verify: git grep -n "\"version\": \"<NEW>\"" — confirm all seven files match. git grep -n "\"version\": \"<OLD>\"" — should return zero hits.
Build: npm run build to regenerate artifacts.
Commit: git add -A && git commit -m "chore: bump version to X.Y.Z".
Tag: git tag -a vX.Y.Z -m "Version X.Y.Z".
Push: git push origin main && git push origin vX.Y.Z.
Publish to npm (this is what makes npx claude-mem@X.Y.Z work):
npm publish

The prepublishOnly script re-runs npm run build automatically. Confirm publish succeeded:
npm view claude-mem@X.Y.Z version   # should print X.Y.Z

Alternative: npm run release:patch / release:minor / release:major invokes np and handles tag+push+publish in one shot — use ONLY if you skipped steps 4–6, otherwise np will error on the existing tag.
GitHub release: gh release create vX.Y.Z --title "vX.Y.Z" --notes "RELEASE_NOTES".
Changelog: Regenerate via the project's changelog script:
npm run changelog:generate

(Runs node scripts/generate-changelog.js, which pulls releases from the GitHub API and rewrites CHANGELOG.md.)
Sync changelog: Commit and push the updated CHANGELOG.md.
Notify: npm run discord:notify vX.Y.Z if applicable.
Finalize: git status — working tree must be clean.
Checklist
 All seven config files have matching versions
 git grep for old version returns zero hits
 npm run build succeeded
 Git tag created and pushed
 npm publish succeeded and npm view claude-mem@X.Y.Z version confirms it (so npx claude-mem@X.Y.Z resolves)
 GitHub release created with notes
 CHANGELOG.md updated and pushed
 git status shows clean tree
Weekly Installs
840
Repository
thedotmack/claude-mem
GitHub Stars
70.8K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn