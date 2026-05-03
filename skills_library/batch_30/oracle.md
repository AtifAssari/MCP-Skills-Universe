---
title: oracle
url: https://skills.sh/charys117/skills/oracle
---

# oracle

skills/charys117/skills/oracle
oracle
Installation
$ npx skills add https://github.com/charys117/skills --skill oracle
SKILL.md
Oracle

Create a bundle you can hand to an external expert assistant (ChatGPT Pro, Claude, etc.) with real repository context.

This skill produces two artifacts:

prompt.md — paste this into the expert assistant as your message
context.zip — upload this to the expert assistant (contains selected repo files + MANIFEST.md)

Both artifacts are written to:

<repo_root>/.agents/oracle/<slug>/

Workflow
Pick the expert “role” (what mindset you want)
debugging → senior engineer debugging with limited context
code-review → staff engineer reviewing for correctness & maintainability
architecture → principal engineer reviewing system design
security → security engineer doing threat modeling
performance → performance engineer identifying bottlenecks
data-sql → database engineer reviewing correctness & performance
ui-ux → expert UI/UX designer reviewing interaction & visuals
general → general expert second opinion
Select a conservative file set Include the smallest set that allows a grounded answer:
README / docs / ADRs relevant to the task
The feature folder(s) under discussion
Direct dependencies (callers/callees), config, types, error handling
Repro artifacts: failing test output, logs, stack traces (redact secrets)

Do not include secrets: .env, API keys, credentials, private keys, prod configs.

Generate the bundle (script) Resolve scripts/oracle.py from this skill directory, and set the target repository with --repo-root (use your current project root):
python3 scripts/oracle.py \
  --repo-root "$PWD" \
  --task "What you want the expert to do" \
  --template debugging \
  --constraint "Key constraint" \
  --verify "Command(s) to validate locally" \
  --entry "path/to/folder::Main feature folder" \
  --entry "path/to/file.ts::Key code path"


The script writes:

<repo_root>/.agents/oracle/<slug>/prompt.md
<repo_root>/.agents/oracle/<slug>/context.zip
Hand off to the expert assistant
Upload context.zip
Paste the contents of prompt.md as the message
After you get advice: verify locally (tests, logs, benchmarks)
Script flags (quick reference)
--template {general|debugging|code-review|architecture|security|performance|data-sql|ui-ux}
--role "Custom role string" (overrides the template default)
--entry "PATH::REASON" (repeatable; PATH may be a file or directory)
--entries-from <file> (one PATH::REASON per line)
--exclude <glob> (repeatable)
--max-file-bytes <int> (skip very large files; default 2,000,000)
--estimate-tokens (best-effort token estimate)
--dry-run (don’t write files; print what would be included)
Output contract for the expert assistant

The generated prompt asks the expert assistant to:

Read MANIFEST.md first
Use only evidence supported by the uploaded files
Cite file paths for concrete claims
Avoid questions; proceed with explicit assumptions
Keep output structured and actionable (Answer → Key Points → Next Steps → Risks)
Weekly Installs
8
Repository
charys117/skills
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass