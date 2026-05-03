---
title: linux-script-developer
url: https://skills.sh/mkabumattar/skills/linux-script-developer
---

# linux-script-developer

skills/mkabumattar/skills/linux-script-developer
linux-script-developer
Installation
$ npx skills add https://github.com/mkabumattar/skills --skill linux-script-developer
SKILL.md
Linux Script Developer

Production-ready Bash. Strict mode + input validation + cross-platform.

When to use
The user asks for any .sh script, installer, automation, or CLI wrapper.
The user wants to harden, refactor, or review an existing Bash script.
A task chain ends in "and put it in a shell script".
Required structure

Every script you write starts from this skeleton. Do not omit set -euo pipefail or the main "$@" invocation.

#!/usr/bin/env bash
set -euo pipefail

readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly SCRIPT_NAME="$(basename "$0")"

# Colors only when stdout is a TTY (avoids garbage in pipes/CI logs)
if [ -t 1 ]; then
    RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; BLUE='\033[0;34m'; NC='\033[0m'
else
    RED=''; GREEN=''; YELLOW=''; BLUE=''; NC=''
fi

usage() {
    cat <<EOF
Usage: $SCRIPT_NAME [OPTIONS] <args>
EOF
    exit "${1:-0}"
}

main() {
    [ "$#" -ge 1 ] || { echo -e "${RED}Error: missing args${NC}" >&2; usage 1; }
    # logic here
}

main "$@"

Workflow
Pick a starting template from assets/templates/ — copy and edit, do not rewrite from scratch:
script.template.sh — basic single-purpose script.
cli-tool.template.sh — multi-subcommand CLI (init / build / deploy style).
file-processor.template.sh — batch operations over files.
Apply the patterns in references/patterns.md for any non-obvious case (traps, getopts, template processing, while-read loops). Read it on demand — don't preload it.
Validate the result. Run bash scripts/validate-script.sh <your-script.sh> — it grep-scans the script and checks shebang, strict mode, header comment, usage/main patterns, quoted positional args, no eval, no hardcoded user-home paths, TTY-guarded ANSI codes, GNU-only flags, and stderr redirection. Aim for ≥ 90%.
Cross-check against the gotchas in references/anti-patterns.md before finishing — especially unquoted vars, hardcoded paths, and missing input validation.
For cross-platform scripts (running on macOS or Windows), load references/cross-platform.md and apply the relevant rules (sed -i'', readlink -f replacements, grep -E not -P).
Generate AWS-style reference docs for the script using the template in references/documentation.md. Always do this — either inline as a markdown block or as a sibling <script>.md.
Available resources
assets/templates/{script,cli-tool,file-processor}.template.sh — starting points.
assets/examples/scaffold-example.sh — full reference implementation.
scripts/validate-script.sh — score a script against the checklist (run after writing).
references/patterns.md — load when implementing error handling, parsing, traps, templates, loops.
references/anti-patterns.md — load when reviewing or rewriting an existing script.
references/cross-platform.md — load when targeting macOS or Windows alongside Linux.
references/documentation.md — load when generating script reference docs.
Top gotchas (always inline — do not skip)
Quote everything. cat $file breaks on spaces; always cat "$file".
set -euo pipefail is the minimum. -e exits on error, -u on undefined vars, pipefail propagates pipe failures.
#!/usr/bin/env bash, never #!/bin/bash. macOS ships an old Bash at /bin/bash; Alpine uses /bin/sh.
Validate args before using them. Fail loudly with a clear message and usage, not a cryptic unbound variable.
Use [ -t 1 ] before emitting ANSI codes so output is clean when piped or in CI logs.
Use ${SCRIPT_DIR} / relative paths, never hardcode /home/user/....
Trap cleanup on EXIT/ERR when creating temp files: trap 'rm -f "$TMP"' EXIT.
macOS sed -i requires an empty string: sed -i'' -e 's/a/b/' file works on both macOS and Linux.
What you DO
Start every script from assets/templates/.
Use set -euo pipefail from the first line of logic.
Quote every variable expansion: "$var", "$@", "${arr[@]}".
Validate every input — count, type, file existence — before using it.
Emit colored messages only when [ -t 1 ].
Use functions for any logic block over ~5 lines; keep main() thin.
Use ${SCRIPT_DIR} and relative paths; never hardcode absolute paths outside the user's project.
Trap cleanup on EXIT / ERR when you create temp files or background processes.
Run scripts/validate-script.sh on the result; iterate until ≥ 90%.
Generate AWS-style reference documentation alongside the script (see references/documentation.md).
Test cross-platform tooling differences (see references/cross-platform.md) when the script will run anywhere besides the author's machine.
What you do NOT do
Skip set -e, leave bare except/no error handling, or use eval/bash -c "$user_input".
Use unquoted variables, hardcoded absolute paths, or cd without a guard.
Use GNU-only flags (grep -P, date -d, readlink -f, mktemp --suffix) without a portable fallback.
Write monolithic scripts with logic outside functions, or skip the usage function.
Emit ANSI color codes unconditionally — they pollute logs and pipes.
Weekly Installs
9
Repository
mkabumattar/skills
First Seen
4 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass