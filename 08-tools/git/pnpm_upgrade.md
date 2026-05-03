---
rating: ⭐⭐
title: pnpm-upgrade
url: https://skills.sh/openai/openai-agents-js/pnpm-upgrade
---

# pnpm-upgrade

skills/openai/openai-agents-js/pnpm-upgrade
pnpm-upgrade
Installation
$ npx skills add https://github.com/openai/openai-agents-js --skill pnpm-upgrade
SKILL.md
pnpm Upgrade

Use these steps to update pnpm and CI pins without blunt search/replace.

Steps (run from repo root)

Update pnpm locally

Try pnpm self-update; if pnpm is missing or self-update fails, run corepack prepare pnpm@latest --activate.
Capture the resulting version as PNPM_VERSION=$(pnpm -v).

Resolve pnpm package integrity

Query npm registry for the exact package integrity: curl -fsSL "https://registry.npmjs.org/pnpm/${PNPM_VERSION}" | jq -r .dist.integrity.
Store the result as PNPM_INTEGRITY.
Abort if the integrity is missing or does not start with sha512-.
Convert the base64 digest after sha512- to lowercase hex, for example:
printf '%s' "${PNPM_INTEGRITY#sha512-}" | base64 -d | xxd -p -c 256

Store the result as PNPM_SHA512_HEX.

Align package.json

Open package.json and set packageManager to pnpm@${PNPM_VERSION}+sha512.${PNPM_SHA512_HEX} (preserve trailing newline and formatting).

Find latest pnpm/action-setup tag

Query GitHub API: curl -fsSL https://api.github.com/repos/pnpm/action-setup/releases/latest | jq -r .tag_name.
Use GITHUB_TOKEN/GH_TOKEN if available for higher rate limits.
Store as ACTION_TAG (e.g., v4.2.0). Abort if missing.

Resolve the action tag to an immutable commit SHA

Run git ls-remote https://github.com/pnpm/action-setup "refs/tags/${ACTION_TAG}^{}" and capture the SHA as ACTION_SHA.
If the dereferenced tag is missing, fall back to git ls-remote https://github.com/pnpm/action-setup "refs/tags/${ACTION_TAG}".
Abort if ACTION_SHA is empty.

Update workflows carefully (no broad regex)

Files: everything under .github/workflows/ that uses pnpm/action-setup.
For each file, edit by hand:
Set uses: pnpm/action-setup@${ACTION_SHA}.
If a with: version: field exists, set it to ${PNPM_VERSION} (keep quoting style/indent).
Do not touch unrelated steps. Avoid multiline sed/perl one-liners.

Verify

Run pnpm -v and confirm it matches the version portion of packageManager.
Confirm packageManager keeps the exact +sha512.${PNPM_SHA512_HEX} suffix.
git diff to ensure only intended workflow/package.json changes.

Follow-up

If runtime code/build/test config was changed (not typical here), run $code-change-verification; otherwise, a light check is enough.
Commit with chore: upgrade pnpm toolchain and open a PR (automation may do this).
Notes
Tools needed: curl, jq, base64, xxd, node, pnpm/corepack. Install if missing.
Keep edits minimal and readable—prefer explicit file edits over global replacements.
GitHub Actions must stay pinned to commit SHAs, not tags. Use the latest release tag only to discover the commit SHA to pin.
If GitHub API is rate-limited, retry with a token or bail out rather than guessing the tag.
Weekly Installs
86
Repository
openai/openai-agents-js
GitHub Stars
2.9K
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn