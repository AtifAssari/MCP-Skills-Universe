---
title: bash
url: https://skills.sh/dralgorhythm/claude-agentic-framework/bash
---

# bash

skills/dralgorhythm/claude-agentic-framework/bash
bash
Installation
$ npx skills add https://github.com/dralgorhythm/claude-agentic-framework --skill bash
SKILL.md
Bash Scripting
Script Template
#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

# Script description
# Usage: ./script.sh <arg1> <arg2>

readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

main() {
    local arg1="${1:-default}"

    # Script logic here
    echo "Running with: $arg1"
}

main "$@"

Safety Settings
set -e          # Exit on error
set -u          # Error on undefined variables
set -o pipefail # Catch pipe failures
set -x          # Debug: print commands

Variables
# Declaration
readonly CONST="immutable"
local var="function scoped"

# Default values
name="${1:-default}"      # Use default if unset
name="${1:?Error: missing}"  # Error if unset

# String operations
"${var^^}"    # Uppercase
"${var,,}"    # Lowercase
"${var#prefix}"  # Remove prefix
"${var%suffix}"  # Remove suffix

Conditionals
# File tests
[[ -f "$file" ]]  # Is file
[[ -d "$dir" ]]   # Is directory
[[ -r "$file" ]]  # Is readable
[[ -x "$file" ]]  # Is executable

# String tests
[[ -z "$var" ]]   # Is empty
[[ -n "$var" ]]   # Is not empty
[[ "$a" == "$b" ]] # Equals

# Numeric tests
(( num > 5 ))     # Greater than
(( num == 5 ))    # Equals

Functions
log() {
    local level="$1"
    local message="$2"
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] [$level] $message" >&2
}

die() {
    log "ERROR" "$1"
    exit 1
}

require_command() {
    command -v "$1" >/dev/null 2>&1 || die "Required command not found: $1"
}

Error Handling
# Trap for cleanup
cleanup() {
    rm -rf "$TMP_DIR"
}
trap cleanup EXIT

# Catch errors
if ! result=$(some_command 2>&1); then
    die "Command failed: $result"
fi

Loops
# For loop
for item in "${array[@]}"; do
    echo "$item"
done

# While read
while IFS= read -r line; do
    echo "$line"
done < file.txt

# Process substitution
while read -r line; do
    echo "$line"
done < <(command)

Best Practices
Quote all variables: "$var"
Use [[ instead of [
Use local in functions
Use readonly for constants
Always use set -euo pipefail
Use shellcheck for linting
Weekly Installs
35
Repository
dralgorhythm/cl…ramework
GitHub Stars
76
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass