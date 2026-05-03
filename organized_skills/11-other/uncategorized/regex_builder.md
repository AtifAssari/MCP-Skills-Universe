---
rating: ⭐⭐
title: regex-builder
url: https://skills.sh/jmerta/codex-skills/regex-builder
---

# regex-builder

skills/jmerta/codex-skills/regex-builder
regex-builder
Installation
$ npx skills add https://github.com/jmerta/codex-skills --skill regex-builder
SKILL.md
Regex builder
Goal

Produce a correct, testable regex with rationale and runnable verification.

Inputs to confirm (ask if missing)
Target regex flavor/engine (PCRE, Python, JavaScript, .NET, RE2, etc.).
Example matches and non-matches (at least 3 each when possible).
Scope: single-line vs multi-line; file types/paths.
Output needs: capture groups, named groups, replacement template.
Workflow
Gather samples
Ask for sample text or identify files.
If files exist, locate with rg --files and preview with rg -n.
Choose tool
Prefer rg for quick match checks; use rg -P for PCRE features.
Use Python for detailed group inspection when needed.
Build incrementally
Start with a minimal literal anchor; expand piece by piece.
Add anchors/boundaries; handle whitespace and separators explicitly.
Validate
Show a command to test against samples.
Confirm no false positives by testing non-matches.
Deliver
Provide final regex, flags, and explanation.
Include a test command and expected match summary.
Note any tradeoffs/backtracking risks.
CLI snippets (use as needed)
Ripgrep check:
rg -n "<regex>" path\\to\\file
rg -n -P "<regex>" path\\to\\file
Python quick test (adjust quoting for the shell):
python -c "import re,sys;pat=re.compile(r'<regex>');data=sys.stdin.read();print([m.group(0) for m in pat.finditer(data)])" < path\\to\\file
Deliverables
Regex + flags and any capture group map.
Test command(s) and summary of matches/non-matches.
Short explanation of the approach and known limitations.
Weekly Installs
29
Repository
jmerta/codex-skills
GitHub Stars
126
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass