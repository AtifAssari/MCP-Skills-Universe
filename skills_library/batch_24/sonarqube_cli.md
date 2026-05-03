---
title: sonarqube-cli
url: https://skills.sh/g-imhoff/skills/sonarqube-cli
---

# sonarqube-cli

skills/g-imhoff/skills/sonarqube-cli
sonarqube-cli
Installation
$ npx skills add https://github.com/g-imhoff/skills --skill sonarqube-cli
SKILL.md
SonarQube CLI Skill

This skill centers on scripts/scan_branch.py — a Python orchestrator that runs a full SonarQube analysis on a branch and reports the quality gate. For single-file checks, secrets scanning, and direct API calls, it wraps the sonar CLI (v0.9.0, Beta).

CRITICAL — Credential checks (run before ANY command)

Before running scripts/scan_branch.py or sonar-scanner, verify SONAR_HOST_URL and SONAR_TOKEN are set without reading their values:

[ -n "${SONAR_HOST_URL}" ] && echo "SONAR_HOST_URL set" || echo "SONAR_HOST_URL MISSING"
[ -n "${SONAR_TOKEN}" ]    && echo "SONAR_TOKEN set"    || echo "SONAR_TOKEN MISSING"


Before running sonar CLI commands, verify authentication:

sonar --version
sonar auth status


NEVER read, print, echo, or log the values of SONAR_TOKEN or SONAR_HOST_URL. If any check fails, stop and ask the user to set the variable or run sonar auth login.

Primary workflow — scripts/scan_branch.py

scripts/scan_branch.py is a self-contained Python script (stdlib only) that replicates the manual-sonarqube.yml GitHub Actions workflow as a local command. Use it whenever the user wants to analyze a branch end-to-end.

It performs:

git checkout of the requested ref
sonar-scanner invocation (single-project context by default for Community Edition)
Polls /api/ce/task until analysis completes
Calls /api/qualitygates/project_status for the gate result
Pass → prints success banner, exits 0
Fail → fetches /api/issues/search, prints a severity-sorted table, exits 1
Prerequisites
sonar-scanner and git on PATH (install scanner: https://docs.sonarsource.com/sonarqube/latest/analyzing-source-code/scanners/sonarscanner/)
SONAR_HOST_URL and SONAR_TOKEN exported (verified as above — never print values)
If the project has a sonar-project.properties file, run the script from that directory. Properties like sonar.projectKey, sonar.sources, etc. are read automatically; use -D extras only to override.
Branch analysis (--use-branch) requires SonarQube Developer Edition or higher
Usage
# Community Edition (default) — checks out the ref, scans against the main project context
python scripts/scan_branch.py --branch feature/my-branch --project-key my-project

# Project living in a subdirectory (matches the GitHub Actions workflow layout)
python scripts/scan_branch.py --branch develop --project-key my-project --project-dir ./yodea-app

# Developer Edition+ — true branch analysis via sonar.branch.name
python scripts/scan_branch.py --branch feature/my-branch --project-key my-project --use-branch

# Longer timeout + extra scanner properties (anything after the flags is passed through)
python scripts/scan_branch.py \
  --branch main \
  --project-key my-project \
  --timeout 900 \
  -Dsonar.sources=src \
  -Dsonar.exclusions=**/*.test.ts

Options
Option	Required	Description
--branch	Yes	Git ref to check out before scanning
--project-key	No*	SonarQube project key (falls back to SONAR_PROJECT_KEY)
--project-name	No	Display name (default: project key)
--project-dir	No	Passed as sonar.projectBaseDir
--timeout	No	Max seconds to wait for analysis (default: 600)
--poll-interval	No	Seconds between /api/ce/task polls (default: 5)
--use-branch	No	Send sonar.branch.name to the scanner (Developer Edition+)
trailing positional args	No	Forwarded verbatim to sonar-scanner (e.g. -Dsonar.sources=src)

* One of --project-key or SONAR_PROJECT_KEY is required.

Environment variables
Variable	Required	Description
SONAR_HOST_URL	Yes	SonarQube server URL
SONAR_TOKEN	Yes	User token, read by both sonar-scanner and the script
SONAR_PROJECT_KEY	No	Default project key, overridden by --project-key

Only user tokens work — project, global, and scoped-organization tokens will be rejected.

Output

Gate passed (exit 0):

============================================================
  QUALITY GATE PASSED - Everything looks good!
============================================================


Gate failed (exit 1):

============================================================
  QUALITY GATE FAILED (FAILED)
============================================================

Failed conditions:
  - new_violations 3 > 0

Issues found: 12

SEVERITY   TYPE            COMPONENT                                 MESSAGE
--------------------------------------------------------------------
BLOCKER    BUG             src/app.ts:42                             Null pointer dereference
CRITICAL   VULNERABILITY   src/auth.ts:15                            Hardcoded credentials
MAJOR      CODE_SMELL      src/utils.ts:88                           Function has 42 parameters

When to reach past the script

Drop to raw sonar-scanner only when the script is not a fit — e.g. custom analysis lifecycle, you already did the checkout, or you need to drive sonar-scanner from another orchestrator. The script's bare-metal equivalent is:

git checkout <branch>
sonar-scanner                                # Community Edition
sonar-scanner -Dsonar.branch.name=<branch>   # Developer Edition+

TASK_ID=$(grep ceTaskId .scannerwork/report-task.txt | cut -d= -f2)
sonar api get "/api/ce/task?id=$TASK_ID"
sonar api get "/api/qualitygates/project_status?projectKey=<key>&branch=<branch>"
sonar list issues -p <key> --branch <branch>

Extending the script

scripts/scan_branch.py is designed to be edited directly — it's one file, stdlib only, and each stage is a small function:

run_scanner() — builds and runs the sonar-scanner command
wait_for_analysis() — polls /api/ce/task
check_quality_gate() — reads /api/qualitygates/project_status
fetch_issues() — paginates /api/issues/search
format_issues() — renders the severity-sorted table

If the user asks for a new behavior (e.g. JSON output, a different gate metric, Slack notification on failure), modify the relevant function rather than adding a parallel script.

Secondary workflows — sonar CLI

These commands do not require scan_branch.py. Use them for targeted, local tasks. Full option tables and every flag live in references/commands.md — read that file whenever the user needs a flag that is not listed below.

Single-file check — sonar verify

Fastest way to scan one file for all issue classes:

sonar verify --file src/app.ts
sonar verify --file src/app.ts --branch main -p my-project

Secrets scan — sonar analyze secrets

Detects hardcoded credentials. Exits non-zero on a hit, so it plugs directly into CI:

sonar analyze secrets src/ .env.example
cat .env | sonar analyze secrets --stdin

Server-side deep analysis — sonar analyze sqaa (Cloud only)
sonar analyze sqaa --file src/app.ts --branch main

Listing issues and projects
sonar list issues -p my-project --severity CRITICAL --branch main
sonar list issues -p my-project --format toon           # AI-friendly output
sonar list projects -q partial-name

Raw API access — sonar api
sonar api get  "/api/qualitygates/project_status?projectKey=my-project"
sonar api post "/api/issues/do_transition" --data '{"issue":"<id>","transition":"accept"}'


Supports get, post, patch, put, delete. Add --verbose for request/response debugging.

API docs: Cloud · Server

Integrations
sonar integrate git                  # Pre-commit secrets hook
sonar integrate git --hook pre-push --global
sonar integrate claude -p my-project # Claude Code hooks + MCP server

Auth, config, self-update
sonar auth login / logout / status / purge
sonar config telemetry --enabled | --disabled
sonar self-update [--status | --force]


For every flag on every subcommand, see references/commands.md.

Decision guide
Need	Command
Full branch analysis + quality gate + issue report (Community Edition)	python scripts/scan_branch.py --branch <ref> --project-key <key>
Full branch analysis with true branch context (Developer Edition+)	python scripts/scan_branch.py --branch <ref> --project-key <key> --use-branch
Project lives in a subdirectory	add --project-dir ./<subdir> to the script call
Override scanner properties	append -Dsonar.key=value to the script call
Check a single file locally	sonar verify --file <path>
Find hardcoded secrets	sonar analyze secrets <paths…>
Deep server-side file analysis (Cloud)	sonar analyze sqaa --file <path>
List issues for a project	sonar list issues -p <key> [--severity …] [--branch …]
List/search projects	sonar list projects [-q …]
Arbitrary API call	sonar api <method> <endpoint> [--data …]
Prevent secret leaks in Git	sonar integrate git [--hook pre-push] [--global]
Protect Claude Code sessions	sonar integrate claude -p <key>
Run sonar-scanner manually	only when scan_branch.py doesn't fit — see the raw workflow above
Quick setup checklist
Install CLI: curl -o- https://raw.githubusercontent.com/SonarSource/sonarqube-cli/refs/heads/master/user-scripts/install.sh | bash
Install scanner: https://docs.sonarsource.com/sonarqube/latest/analyzing-source-code/scanners/sonarscanner/
sonar auth login and confirm with sonar auth status
Export credentials for the script:
export SONAR_HOST_URL="https://your-sonarqube.example.com"
export SONAR_TOKEN="squ_your_token_here"
# optional default for the script
export SONAR_PROJECT_KEY="my-project"

Verify variables are set (without printing):
[ -n "${SONAR_HOST_URL}" ] && [ -n "${SONAR_TOKEN}" ] && echo "OK" || echo "MISSING"

Run python scripts/scan_branch.py --branch <ref> from the project root (or the directory containing sonar-project.properties).
Weekly Installs
11
Repository
g-imhoff/skills
First Seen
10 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn