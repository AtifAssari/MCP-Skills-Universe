---
rating: ⭐⭐⭐
title: bash-scripting
url: https://skills.sh/sickn33/antigravity-awesome-skills/bash-scripting
---

# bash-scripting

skills/sickn33/antigravity-awesome-skills/bash-scripting
bash-scripting
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill bash-scripting
SKILL.md
Bash Scripting Workflow
Overview

Specialized workflow for creating robust, production-ready bash scripts with defensive programming patterns, comprehensive error handling, and automated testing.

When to Use This Workflow

Use this workflow when:

Creating automation scripts
Writing system administration tools
Building deployment scripts
Developing backup solutions
Creating CI/CD scripts
Workflow Phases
Phase 1: Script Design
Skills to Invoke
bash-pro - Professional scripting
bash-defensive-patterns - Defensive patterns
Actions
Define script purpose
Identify inputs/outputs
Plan error handling
Design logging strategy
Document requirements
Copy-Paste Prompts
Use @bash-pro to design production-ready bash script

Phase 2: Script Structure
Skills to Invoke
bash-pro - Script structure
bash-defensive-patterns - Safety patterns
Actions
Add shebang and strict mode
Create usage function
Implement argument parsing
Set up logging
Add cleanup handlers
Copy-Paste Prompts
Use @bash-defensive-patterns to implement strict mode and error handling

Phase 3: Core Implementation
Skills to Invoke
bash-linux - Linux commands
linux-shell-scripting - Shell scripting
Actions
Implement main functions
Add input validation
Create helper functions
Handle edge cases
Add progress indicators
Copy-Paste Prompts
Use @bash-linux to implement system commands

Phase 4: Error Handling
Skills to Invoke
bash-defensive-patterns - Error handling
error-handling-patterns - Error patterns
Actions
Add trap handlers
Implement retry logic
Create error messages
Set up exit codes
Add rollback capability
Copy-Paste Prompts
Use @bash-defensive-patterns to add comprehensive error handling

Phase 5: Logging
Skills to Invoke
bash-pro - Logging patterns
Actions
Create logging function
Add log levels
Implement timestamps
Configure log rotation
Add debug mode
Copy-Paste Prompts
Use @bash-pro to implement structured logging

Phase 6: Testing
Skills to Invoke
bats-testing-patterns - Bats testing
shellcheck-configuration - ShellCheck
Actions
Write Bats tests
Run ShellCheck
Test edge cases
Verify error handling
Test with different inputs
Copy-Paste Prompts
Use @bats-testing-patterns to write script tests

Use @shellcheck-configuration to lint bash script

Phase 7: Documentation
Skills to Invoke
documentation-templates - Documentation
Actions
Add script header
Document functions
Create usage examples
List dependencies
Add troubleshooting section
Copy-Paste Prompts
Use @documentation-templates to document bash script

Script Template
#!/usr/bin/env bash
set -euo pipefail

readonly SCRIPT_NAME=$(basename "$0")
readonly SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"; }
error() { log "ERROR: $*" >&2; exit 1; }

usage() { cat <<EOF
Usage: $SCRIPT_NAME [OPTIONS]
Options:
    -h, --help      Show help
    -v, --verbose   Verbose output
EOF
}

main() {
    log "Script started"
    # Implementation
    log "Script completed"
}

main "$@"

Quality Gates
 ShellCheck passes
 Bats tests pass
 Error handling works
 Logging functional
 Documentation complete
Related Workflow Bundles
os-scripting - OS scripting
linux-troubleshooting - Linux troubleshooting
cloud-devops - DevOps automation
Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
569
Repository
sickn33/antigra…e-skills
GitHub Stars
36.1K
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass