---
rating: ⭐⭐⭐
title: vercel-plugin-eval
url: https://skills.sh/vercel/vercel-plugin/vercel-plugin-eval
---

# vercel-plugin-eval

skills/vercel/vercel-plugin/vercel-plugin-eval
vercel-plugin-eval
Installation
$ npx skills add https://github.com/vercel/vercel-plugin --skill vercel-plugin-eval
SKILL.md
Plugin Eval

Launch real Claude Code sessions with the plugin installed, monitor debug logs in real-time, and verify every hook fires correctly with proper dedup.

DO NOT (Hard Rules)
DO NOT use claude --print or -p — hooks don't fire, no files created
DO NOT use --dangerously-skip-permissions
DO NOT create projects in /tmp/ — always use ~/dev/vercel-plugin-testing/
DO NOT manually wire hooks or create settings.local.json — use npx add-plugin
DO NOT set CLAUDE_PLUGIN_ROOT manually
DO NOT use bash -c in WezTerm — use /bin/zsh -ic
DO NOT use full path to claude — use the x alias
DO NOT write eval scripts — do everything as Bash tool calls in the conversation

Copy the exact commands below. Do not improvise.

Quick Start

Always append a timestamp to directory names so reruns don't overwrite old projects:

# 1. Create test dir & install plugin (with timestamp)
TS=$(date +%Y%m%d-%H%M)
SLUG="my-eval-$TS"
mkdir -p ~/dev/vercel-plugin-testing/$SLUG
cd ~/dev/vercel-plugin-testing/$SLUG
npx add-plugin https://github.com/vercel/vercel-plugin -s project -y

# 2. Launch session via WezTerm
wezterm cli spawn --cwd /Users/johnlindquist/dev/vercel-plugin-testing/$SLUG -- /bin/zsh -ic \
  "unset CLAUDECODE; VERCEL_PLUGIN_LOG_LEVEL=debug x '<PROMPT>' --settings .claude/settings.json; exec zsh"

# 3. Find debug log (wait ~25s for session start)
find ~/.claude/debug -name "*.txt" -mmin -2 -exec grep -l "$SLUG" {} +

What to Monitor
Hook firing (all 8 registered hooks)
LOG=~/.claude/debug/<session-id>.txt

# SessionStart (3 hooks)
grep "SessionStart.*success" "$LOG"

# PreToolUse skill injection
grep -c "executePreToolHooks" "$LOG"        # total calls
grep -c "provided additionalContext" "$LOG"  # injections

# UserPromptSubmit
grep "UserPromptSubmit.*success" "$LOG"

# PostToolUse validate + shadcn font-fix
grep "posttooluse-validate.*provided" "$LOG"
grep "PostToolUse:Bash.*success" "$LOG"

# SessionEnd cleanup
grep "SessionEnd" "$LOG"

Dedup correctness (the key metric)
TMPDIR=$(node -e "import {tmpdir} from 'os'; console.log(tmpdir())" --input-type=module)
CLAIMDIR="$TMPDIR/vercel-plugin-<session-id>-seen-skills.d"

# Claim files = one per skill, atomic O_EXCL
ls "$CLAIMDIR"

# Compare: injections should equal claims
inject_meta=$(grep -c "skillInjection:" "$LOG")
claims=$(ls "$CLAIMDIR" 2>/dev/null | wc -l | tr -d ' ')
echo "Injections: $((inject_meta / 3)) | Claims: $claims"


skillInjection: appears 3x per actual injection in the debug log (initial check, parsed, success). Divide by 3.

PostToolUse validate quality

Look for real catches — API key bypass, outdated models, wrong patterns:

grep "VALIDATION" "$LOG" | head -10

Scenario Design

Describe products and features, never name specific technologies. Let the plugin infer which skills to inject. Always end prompts with: "Link the project to my vercel-labs team so we can deploy it later. Skip any planning and just build it. Get the dev server running."

Coverage targets by scenario type
Scenario Type	Skills Exercised
AI chat app	ai-sdk, ai-gateway, nextjs, ai-elements
Durable workflow	workflow, ai-sdk, vercel-queues
Monorepo	turborepo, turbopack, nextjs
Edge auth + routing	routing-middleware, auth, sign-in-with-vercel
Chat bot (multi-platform)	chat-sdk, ai-sdk, vercel-storage
Feature flags + CRM	vercel-flags, vercel-queues, ai-sdk
Email pipeline	email, satori, ai-sdk, vercel-storage
Marketplace/payments	payments, marketplace, cms
Kitchen sink	micro, ncc, all niche skills
Hard-to-trigger skills (8 of 44)

These need explicit technology references in the prompt because agents don't naturally reach for them:

ai-elements — say "use the AI Elements component registry"
v0-dev — say "generate components with v0"
vercel-firewall — say "use Vercel Firewall for rate limiting"
marketplace — say "publish to the Vercel Marketplace"
geist — say "install the geist font package"
json-render — name files components/chat-*.tsx
Coverage Report

Write results to .notes/COVERAGE.md with:

Session index — slug, session ID, unique skills, dedup status
Hook coverage matrix — which hooks fired in which sessions
Skill injection table — which of the 44 skills triggered
Dedup stats — injections vs claims per session
Issues found — bugs, pattern gaps, validation findings
Cleanup
rm -rf ~/dev/vercel-plugin-testing

Weekly Installs
202
Repository
vercel/vercel-plugin
GitHub Stars
156
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn