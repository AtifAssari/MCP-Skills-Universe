---
title: dev-status
url: https://skills.sh/andreaserradev-gbj/dev-workflow/dev-status
---

# dev-status

skills/andreaserradev-gbj/dev-workflow/dev-status
dev-status
Installation
$ npx skills add https://github.com/andreaserradev-gbj/dev-workflow --skill dev-status
SKILL.md
Dev Status Report

Scan all features in the .dev/ folder, generate a status report, and offer to archive completed or stale features.

Agents

This skill uses a specialized agent for status scanning:

feature-batch-scanner (blue) — Scans a batch of feature folders and extracts status for each

Agent definition is in agents/ within this skill's directory.

Step 0: Discover Project Root

Run the discovery script:

bash "$DISCOVER" root


Where $DISCOVER is the absolute path to scripts/discover.sh within this skill's directory.

Path safety — shell state does not persist between tool calls, so you must provide full script paths on each call:

Use $HOME instead of the literal home directory (e.g., bash "$HOME/code/…/discover.sh", not bash "/Users/name/…/discover.sh"). This prevents username hallucination.
Copy values from tool output. When reusing a value returned by a previous command (like $PROJECT_ROOT), copy it verbatim from that command's output. Never retype a path from memory.
Verify on first call: if a script call fails with "No such file", the path is wrong — STOP and re-derive from the skill-loading context.
Never ignore a non-zero exit. If any script in this skill fails, stop and report the error before continuing.

Store the output as $PROJECT_ROOT. If the command fails, inform the user and stop.

Step 1: Discover Features

Run the discovery script to find features:

bash "$DISCOVER" features "$PROJECT_ROOT"

If the script exits non-zero (no .dev/ directory): inform the user "No .dev/ directory found. Use /dev-plan to start a new feature."
If output is empty: inform the user "No features found in .dev/. Use /dev-plan to start a new feature."
Otherwise: store the list of feature folder paths for the next step.

Also check for archived features using the discovery script:

bash "$DISCOVER" archived "$PROJECT_ROOT"


Store any archived paths for the report.

Security rule: only use exact folder paths returned by discovery commands. Never build archive/move paths from raw user input.

Step 2: Calculate Batches

Distribute feature folders across agents (maximum 5 agents):

If N ≤ 5 features: Launch N agents, 1 folder each
If N > 5 features: Launch 5 agents, distribute folders round-robin

Batch distribution algorithm (for N > 5):

Agent 1: folders[0], folders[5], folders[10], ...
Agent 2: folders[1], folders[6], folders[11], ...
Agent 3: folders[2], folders[7], folders[12], ...
Agent 4: folders[3], folders[8], folders[13], ...
Agent 5: folders[4], folders[9], folders[14], ...

Step 3: Launch Parallel Agents

Launch all feature-batch-scanner agents in parallel using the Task tool.

For each agent, provide a prompt like:

"Scan these feature folders and return status for each:
- $PROJECT_ROOT/.dev/feature-a
- $PROJECT_ROOT/.dev/feature-b
- $PROJECT_ROOT/.dev/feature-c

For each folder, determine: Status (Active/Complete/Stale/No PRD), Progress (phases and steps), Last Checkpoint date, and Next Action."


Use subagent_type=dev-workflow:feature-batch-scanner and model=haiku for each agent.

IMPORTANT: Launch all agents in a single message with multiple Task tool calls to run them in parallel.

Step 4: Aggregate Results

After all agents return:

Parse each agent's batch results
Combine into a unified list of all features
Sort by status: Active first, then Stale, then Complete, then No PRD
Calculate summary counts
Step 5: Present Report

Display the status report to the user:

## Dev Status Report

**Generated**: [ISO 8601 timestamp]
**Features Scanned**: [N]

### Summary

| Status | Count |
|--------|-------|
| Active | [X] |
| Complete | [Y] |
| Stale | [Z] |
| No PRD | [W] |

### All Features

| Feature | Status | Progress | Last Activity | Next Action |
|---------|--------|----------|---------------|-------------|
| [name] | [status] | [X/Y phases] | [date/ago] | [summary] |
...


If there are archived features, add a section:

### Archived Features

[N] features in `.dev-archive/`:
- [feature-name-1]
- [feature-name-2]

Step 6: Archive Offer

If there are any Complete or Stale features, ask the user:

"Would you like to archive any completed or stale features? This moves them to .dev-archive/ to keep .dev/ clean."

Present options:

Archive all complete features
Archive all stale features
Archive specific features (list them)
Skip archiving

If user chooses to archive:

Create .dev-archive/ if it doesn't exist:

mkdir -p "$PROJECT_ROOT/.dev-archive"


For each selected feature, set $FEATURE_PATH to the matching path from Step 1's discovered list. Validate with the validation script:

bash "$VALIDATE" feature-path "$FEATURE_PATH" "$PROJECT_ROOT"


Where $VALIDATE is the absolute path to scripts/validate.sh within this skill's directory. Apply the path safety rules from Step 0 ($HOME, copy from output). On failure, STOP immediately — do not archive or continue with an unvalidated path.

Then move:

mv -- "$FEATURE_PATH" "$PROJECT_ROOT/.dev-archive/"


$FEATURE_PATH must be one of the discovered .dev/* directories selected by the user. Never construct it from raw user input.

Confirm what was archived.

If user skips: Proceed to Step 7.

Step 7: Save Report

Remove any previous status reports before writing the new one:

bash "$DISCOVER" status-reports "$PROJECT_ROOT"


Delete each file path returned (if any). If the command fails, skip cleanup and continue.

Write the status report to $PROJECT_ROOT/.dev/status-report-YYYY-MM-DD.md:

# Dev Status Report

**Generated**: [ISO 8601 timestamp]
**Project**: [project name from git or folder]
**Features Scanned**: [N]

## Summary

| Status | Count |
|--------|-------|
| Active | [X] |
| Complete | [Y] |
| Stale | [Z] |
| No PRD | [W] |

## Features

| Feature | Status | Progress | Last Activity |
|---------|--------|----------|---------------|
| [name] | [status] | [X/Y phases] | [date] |
...

## Archive Candidates

### Complete (ready to archive)
- [feature-name]
...

### Stale (no activity > 30 days)
- [feature-name]
...

---

*Report generated by `/dev-status`*


Confirm: "Status report saved to .dev/status-report-YYYY-MM-DD.md"

Privacy Rules

NEVER include in output or saved reports:

Absolute paths containing usernames (e.g., /Users/username/...)
Secrets, API keys, tokens, or credentials
Personal information

ALWAYS use instead:

Relative paths from project root (e.g., .dev/feature-name/)
Feature names without full paths in tables
Weekly Installs
14
Repository
andreaserradev-…workflow
GitHub Stars
2
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass