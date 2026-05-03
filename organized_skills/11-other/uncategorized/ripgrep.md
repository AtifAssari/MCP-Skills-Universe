---
rating: ⭐⭐
title: ripgrep
url: https://skills.sh/jpcaparas/skills/ripgrep
---

# ripgrep

skills/jpcaparas/skills/ripgrep
ripgrep
Installation
$ npx skills add https://github.com/jpcaparas/skills --skill ripgrep
SKILL.md
ripgrep

Prefer rg over grep for text search, and prefer rg --files over find | grep when the real task is path discovery.

Verified locally against ripgrep 15.1.0 on April 10, 2026. The skill is repo-agnostic, but the examples assume a Unix-like shell and an rg binary in PATH.

Decision Tree

What kind of search do you need?

Search file contents for text, symbols, regexes, or literals

Start with rg
Read references/commands.md

Find filenames or paths without reading file contents

Start with rg --files [path]
Then filter that list with a second rg if needed
Read references/patterns.md

Search only specific languages, globs, hidden files, ignored files, compressed data, or multiline blocks

Read references/commands.md
If results seem wrong or missing, read references/gotchas.md

Make ripgrep behavior repeatable with config files, aliases, or custom file types

Read references/configuration.md

Feed results into automation, scripts, editors, or other tools

Prefer --json, -0, -l, --count-matches, or --sort path as appropriate
Read references/patterns.md

The user wants full-file reading, structured JSON queries, or filesystem metadata

Do not force rg into a role it is bad at
Read the file directly, or use jq, find, or fd
Default Operating Rules
Use rg first for text search. Only fall back to grep when rg is unavailable or exact POSIX grep behavior is the real requirement.
Use -F for user-provided literals unless the user clearly asked for regex semantics.
Narrow the search early with an explicit path plus -t or -g instead of searching the entire tree and cleaning up later.
Use rg --files for path discovery, then pipe into another rg for filename filtering instead of composing find ... | grep ....
Escalate ignore overrides gradually: normal search, then --hidden, then -u or --no-ignore, then -uu or -uuu only if the missing-result hypothesis justifies it.
Use --debug when results are missing and you need to know what ripgrep skipped.
Use --json or -n --color never --no-heading for machine consumption. Prefer --sort path when deterministic output matters more than maximum speed.
Quick Reference
Need	Command	Notes
Literal text search	rg -n -F 'needle' path/	Best default for user-provided strings with punctuation
Regex search	rg -n 'foo\\s+bar' path/	Use single quotes so the shell does not interfere
Filenames only	rg --files path/	Respects ignore files by default
Filter filenames	`rg --files	rg '(^
Match specific languages	rg -n -t py 'pattern' src/	-t includes, -T excludes
Match specific globs	rg -n -g '*.tsx' 'pattern' src/	Later globs override earlier ones
Search hidden or ignored content	rg --hidden 'pattern' then rg -u 'pattern'	Escalate only as needed
Files with matches	rg -l 'pattern' path/	Use before opening files
Count individual matches	rg --count-matches 'pattern' path/	-c counts matching lines, not matches
Machine-readable output	rg --json 'pattern' path/	Best for tools and scripts
Lookaround or backreferences	rg -P '...' path/	Requires PCRE2 support in the build
Multiline blocks	rg -U '(?s)start.*end' file	Multiline is slower and more memory-hungry
Diagnose skipped files	rg --debug 'pattern' path/	Shows ignore and skip reasons
Reading Guide
Task	Read
Correct command, flag, or output mode	references/commands.md
Config files, aliases, custom types, and environment setup	references/configuration.md
Agent search workflows, filename discovery, shell pipelines, and deterministic output	references/patterns.md
Missing results, quoting issues, multiline surprises, JSON limits, and other traps	references/gotchas.md
Verified Behaviors
rg --files respects ignore rules by default and excluded an ignored logs/app.log in local probes.
.rgignore overrode .ignore, and --no-ignore restored access to the same ignored file.
--hidden surfaced hidden content without turning off ignore handling.
The order of -g flags changed the result set exactly as upstream documents: later globs overrode earlier ones.
RIPGREP_CONFIG_PATH successfully loaded --smart-case and a custom web type from a config file.
--json emitted begin, match, end, and summary messages in JSON Lines format.
-U '(?s)...' matched across lines, and -P lookaround worked on this machine because the local build includes PCRE2.
Gotchas
rg is not a byte-for-byte drop-in replacement for POSIX grep; it is the default search tool when speed, recursion, ignore handling, or Unicode-aware regex matter.
Missing results are usually an ignore, hidden-file, glob-order, or quoting problem before they are a ripgrep bug. Run --debug before switching tools.
--replace changes printed output only. It never edits files.
--json is for search results, not every output mode. It does not combine with --files, -l, or -c.
-P and -U are powerful but costlier than the default engine and normal line-oriented search. Use them deliberately.
Helper Scripts
scripts/probe_ripgrep.py builds a temporary corpus and verifies real rg behavior such as ignore precedence, JSON output, multiline matching, and PCRE2 support.
scripts/validate.py checks structure, frontmatter, references, required files, and Python syntax.
scripts/test_skill.py runs validation, checks eval coverage, verifies cross-references, and executes the ripgrep probe suite.
Weekly Installs
26
Repository
jpcaparas/skills
GitHub Stars
13
First Seen
4 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass