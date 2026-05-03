---
title: openwork-orchestrator-npm-publish
url: https://skills.sh/different-ai/openwork/openwork-orchestrator-npm-publish
---

# openwork-orchestrator-npm-publish

skills/different-ai/openwork/openwork-orchestrator-npm-publish
openwork-orchestrator-npm-publish
Installation
$ npx skills add https://github.com/different-ai/openwork --skill openwork-orchestrator-npm-publish
SKILL.md
Quick usage (already configured)
Ensure you are on the default branch and the tree is clean.
Bump versions via the shared release bump (this keeps openwork-orchestrator aligned with the app/desktop release).
pnpm bump:patch
# or: pnpm bump:minor
# or: pnpm bump:major
# or: pnpm bump:set -- X.Y.Z

Commit the bump.
Preferred: publish via the "Release App" GitHub Actions workflow by tagging vX.Y.Z.

Manual recovery path (sidecars + npm) below.

pnpm --filter openwork-orchestrator build:sidecars
gh release create openwork-orchestrator-vX.Y.Z packages/orchestrator/dist/sidecars/* \
  --repo different-ai/openwork \
  --title "openwork-orchestrator vX.Y.Z sidecars" \
  --notes "Sidecar binaries and manifest for openwork-orchestrator vX.Y.Z"

Build openwork-orchestrator binaries for all supported platforms.
pnpm --filter openwork-orchestrator build:bin:all

Publish openwork-orchestrator as a meta package + platform packages (optionalDependencies).
node packages/orchestrator/scripts/publish-npm.mjs

Verify the published version.
npm view openwork-orchestrator version

Scripted publish
./.opencode/skills/openwork-orchestrator-npm-publish/scripts/publish-openwork-orchestrator.sh

First-time setup (if not configured)

Authenticate with npm before publishing.

npm login


Alternatively, export an npm token in your environment (see .env.example).

Notes
openwork-orchestrator is published as:
openwork-orchestrator (wrapper + optionalDependencies)
openwork-orchestrator-darwin-arm64, openwork-orchestrator-darwin-x64, openwork-orchestrator-linux-arm64, openwork-orchestrator-linux-x64, openwork-orchestrator-windows-x64 (platform binaries)
openwork-orchestrator is versioned in lockstep with OpenWork app/desktop releases.
openwork-orchestrator downloads sidecars from openwork-orchestrator-vX.Y.Z release assets by default.
Weekly Installs
79
Repository
different-ai/openwork
GitHub Stars
14.6K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass