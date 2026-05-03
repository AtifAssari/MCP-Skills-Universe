---
title: codex
url: https://skills.sh/abpai/skills/codex
---

# codex

skills/abpai/skills/codex
codex
Installation
$ npx skills add https://github.com/abpai/skills --skill codex
SKILL.md
Codex Skill Guide
Workflow
Confirm task mode:
New run: use codex exec.
Continue prior run: use codex exec ... resume --last with stdin prompt.
Set defaults unless user overrides:
Model: gpt-5.4.
Reasoning effort: ask user to choose xhigh, high, medium, or low.
Sandbox: read-only unless edits/network are required.
Build command with required flags:
Always include --skip-git-repo-check.
Add 2>/dev/null by default to suppress thinking tokens on stderr.
Show stderr only if user asks or debugging is needed.
Run command, summarize outcome, and ask what to do next.
After completion, remind user they can continue with codex resume.
Quick Reference
Use case	Sandbox mode	Key flags
Read-only review or analysis	read-only	--sandbox read-only 2>/dev/null
Apply local edits	workspace-write	--sandbox workspace-write --full-auto 2>/dev/null
Permit network or broad access	danger-full-access	--sandbox danger-full-access --full-auto 2>/dev/null
Resume recent session	Inherited from original	echo "prompt" | codex exec --skip-git-repo-check resume --last 2>/dev/null
Run from another directory	Match task needs	-C <DIR> plus other flags 2>/dev/null
Command Patterns
New run
codex exec --skip-git-repo-check \
  --model gpt-5.4 \
  --config model_reasoning_effort="high" \
  --sandbox read-only \
  "your prompt here" 2>/dev/null

Resume latest session

Use stdin and keep flags between exec and resume.

echo "your prompt here" | codex exec --skip-git-repo-check resume --last 2>/dev/null


When resuming, do not add configuration flags unless the user explicitly asks for changes (for example, different model or reasoning effort).

Model Options
Model	Best for	Context window	Key features
gpt-5.4 ⭐	Default for most coding tasks in Codex	N/A in this skill	OpenAI's recommended default for general-purpose coding
gpt-5.4-pro	Harder problems that benefit from more compute	N/A in this skill	More compute for deeper reasoning on difficult tasks
gpt-5-mini	Faster/cost-effective option for lighter tasks	N/A in this skill	Smaller GPT-5 model for lower-cost coding and chat tasks
gpt-5.3-codex	Legacy specialized alternative	N/A in this skill	Prior Codex-tuned model; generally superseded by GPT-5.4

gpt-5.4 is the default for software engineering tasks.

Reasoning Effort
xhigh - Ultra-complex tasks (deep problem analysis, complex reasoning, deep understanding of the problem)
high - Complex tasks (refactoring, architecture, security analysis, performance optimization)
medium - Standard tasks (refactoring, code organization, feature additions, bug fixes)
low - Simple tasks (quick fixes, simple changes, code formatting, documentation)
Following Up
After every run, ask for next steps or clarifications.
When proposing another run, restate model, reasoning effort, and sandbox mode.
For continuation, use stdin with resume --last.
Error Handling
If codex --version or codex exec exits non-zero, report failure and ask before retrying.
Ask permission before high-impact flags unless already granted: --full-auto, --sandbox danger-full-access, --skip-git-repo-check.
If output includes warnings or partial results, summarize and ask how to proceed.
CLI Version

Use a current Codex CLI version that supports gpt-5.4. Check with:

codex --version


Use /model inside Codex to switch models, or set defaults in ~/.codex/config.toml.

Update Check

On first use in a session, silently check for a newer version:

Fetch https://raw.githubusercontent.com/abpai/skills/main/versions.json.
Compare the version for codex against this file's metadata.version.
If the remote version is newer, pause before the main task and ask:

codex update available (local {X.Y} → remote {A.B}). Would you like me to update it for you first? I can run npx skills update codex for you.

If the user says yes, run the update before continuing.
If the user says no, continue with the current local version.
If the fetch fails or web access is unavailable, skip silently.
Weekly Installs
9
Repository
abpai/skills
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn