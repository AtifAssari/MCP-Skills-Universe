---
title: prime
url: https://skills.sh/slamb2k/mad-skills/prime
---

# prime

skills/slamb2k/mad-skills/prime
prime
Installation
$ npx skills add https://github.com/slamb2k/mad-skills --skill prime
SKILL.md
Prime - Project Context Loader

When this skill is invoked, IMMEDIATELY output the banner below before doing anything else. Pick ONE tagline at random — vary your choice each time. CRITICAL: Reproduce the banner EXACTLY character-for-character. The first line of the art has 4 leading spaces — you MUST preserve them.

{tagline}

⠀   ██╗██████╗ ██████╗ ██╗███╗   ███╗███████╗
   ██╔╝██╔══██╗██╔══██╗██║████╗ ████║██╔════╝
  ██╔╝ ██████╔╝██████╔╝██║██╔████╔██║█████╗
 ██╔╝  ██╔═══╝ ██╔══██╗██║██║╚██╔╝██║██╔══╝
██╔╝   ██║     ██║  ██║██║██║ ╚═╝ ██║███████╗
╚═╝    ╚═╝     ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚══════╝


Taglines:

🔋 Loading the arsenal...
📚 Knowledge is power!
📖 Absorbing the sacred texts...
📡 Context loading... please stand by!
💣 Priming the knowledge cannon!
🤓 Time to do my homework!
📜 Downloading the lore...
🧠 Brain cells: ACTIVATING
Output Formatting

After the banner, display parsed input:

┌─ Input ────────────────────────────────────────
│  {Field}:  {value}
│  Flags:    {parsed flags or "none"}
└────────────────────────────────────────────────


Pre-flight results:

── Pre-flight ───────────────────────────────────
  ✅ {dep}           {version or "found"}
  ⚠️ {dep}           not found → {fallback detail}
  ❌ {dep}           missing → stopping
──────────────────────────────────────────────────


Stage/phase headers: ━━ {N} · {Name} ━━━━━━━━━━━━━━━━━━━━━━━━━

Status icons: ✅ done · ❌ failed · ⚠️ degraded · ⏳ working · ⏭️ skipped

Load project context to inform agent decisions. Raw file contents stay in a subagent — the primary thread only sees a structured PRIME_REPORT.

Step 1: Parse Arguments

Extract domain hints from the request (comma-separated). These are directory names or topic keywords to focus the context scan on. If no domain specified, load core context only (CLAUDE.md, README, specs/).

Step 2: Load Context via Subagent

Launch a general-purpose subagent to read files and build the report:

Task(
  subagent_type: "general-purpose",
  description: "Load and summarise project context",
  prompt: <see below>
)

Subagent Prompt
Load project context and return a structured summary. Raw file contents must
NOT appear in the report — summarise only.

Limit PRIME_REPORT to 30 lines maximum.

## Core Files (always load)

1. CLAUDE.md — Project conventions, architecture, instructions
2. README.md — Project overview, setup, usage
3. specs/ — Project specifications and roadmap (scan directory if present)
4. docs/ — Documentation directory (scan if present)

If a file is missing, record as NOT FOUND and continue.

## Domain Files

{For each requested domain hint, use Glob to find relevant files:}
- Search for directories matching the hint name (e.g., "auth" → src/auth/, lib/auth/)
- Search for files matching *{hint}*.md, *{hint}*.yaml, *{hint}*.json
- Read the most relevant matches (max 5 files per domain)

For each file:
- If it exists: read and summarise (2-3 lines max per domain)
- If it doesn't exist: record as NOT FOUND and continue

## Output Format

PRIME_REPORT:
- core_files_loaded: {count}/{total}
- missing_files: {list or "none"}
- domains_loaded: {list}
- per_domain_summary:
  - {domain}: {2-3 line summary}
- branch: {current branch from git branch --show-current}
- ready_for: {inferred from loaded context}

Step 3: Present Summary

Parse PRIME_REPORT and present a clean summary to the user:

┌─ Prime · Report ───────────────────────────────
│
│  ✅ Context loaded
│
│  📚 Core:   {count}/{total} files loaded
│  🌐 Branch: {branch}
│
│  📝 Domains
│     {domain}: {2-3 line summary}
│     {domain}: {2-3 line summary}
│
│  ⚠️ Missing: {list or "none"}
│
│  🎯 Ready to assist with: {ready_for}
│
└─────────────────────────────────────────────────


If CLAUDE.md was missing, warn the user and note that only domain context was loaded.

Weekly Installs
16
Repository
slamb2k/mad-skills
GitHub Stars
2
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass