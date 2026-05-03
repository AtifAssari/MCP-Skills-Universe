---
title: bg-jobs
url: https://skills.sh/lirrensi/agent-cli-helpers/bg-jobs
---

# bg-jobs

skills/lirrensi/agent-cli-helpers/bg-jobs
bg-jobs
Installation
$ npx skills add https://github.com/lirrensi/agent-cli-helpers --skill bg-jobs
SKILL.md
Background Jobs Skill

Run and manage background jobs from the terminal, with friendly names, live runtime details, wait support, and persisted exit metadata.

Installation Check
bg --help


If not installed:

uv tool install agentcli-helpers

Usage

bg runs commands in your platform shell. bg run returns immediately after creating the handle; a detached worker finishes the launch in the background and jobs appear running unless failure is proven. A short best-effort PID probe updates the record a few seconds later when it can. On Windows it prefers PowerShell 7, then Windows PowerShell, then cmd.exe, launches jobs without a visible console window when PowerShell is available, and expects shell syntax that matches the shell you expect.

Run a Background Job
bg run "python long_script.py"
# Returns: sleepy-pytest (friendly name)

bg run "python --version"

List All Jobs
bg list
bg list --json


bg list shows live job details including name, UID, record state, process state, status, PID, start time, elapsed runtime, and command.

Check Job Status
bg status sleepy-pytest


bg status <ref> refreshes the job before printing JSON. Use either the friendly name or UID. Running jobs may include elapsed_seconds, memory_bytes, and cpu_percent. Finished jobs can also include finished_at and exit_code.

Wait for Completion
bg wait sleepy-pytest

Wait for Output
bg wait sleepy-pytest --match "needle"

Wait for All Jobs
bg wait-all

Read Job Output
bg read sleepy-pytest   # stdout only
bg logs sleepy-pytest   # stdout + stderr

Remove Job
bg rm sleepy-pytest

Prune Non-Running Jobs
bg prune


Deletes every job that is not currently running, including stale or broken records.

Restart Job
bg restart sleepy-pytest


bg restart <ref> kills the process if alive and starts a new one with the same command. Output appends to existing stdout/stderr files (like ctrl+c + run again). The job keeps the same UID and name.

Workflow Pattern
# Bash / zsh
JOB_NAME=$(bg run "python train_model.py")
bg status $JOB_NAME
bg read $JOB_NAME

# PowerShell
$jobName = bg run "python train_model.py"
bg status $jobName
bg read $jobName

Job Storage

Jobs keep runtime state in your OS temp directory under agentcli_bgjobs/:

index.json - Friendly-name and UID lookup index
records/<uid>/meta.json - Canonical job metadata (uid, name, cmd, pid, status, started_at, optional finished_at, optional exit_code, optional record_issue, and live runtime fields)
records/<uid>/meta.json - Canonical job metadata (uid, name, cmd, pid, status, started_at, optional finished_at, optional exit_code, optional record_issue, and lightweight event fields such as last_event_type, last_event_at, matched_pattern, and matched_stream)
records/<uid>/stdout.txt - Standard output
records/<uid>/stderr.txt - Standard error
records/<uid>/exit_code.txt - Persisted exit code

Terminal jobs are automatically pruned: keep them for at least 1 hour, cap history at 32 jobs, and evict the oldest terminal jobs first. Running jobs are never evicted automatically.

Windows note:

PowerShell syntax works by default when pwsh or powershell is available
Windows background jobs are started hidden, so there is no extra console window to close
Use explicit cmd.exe /d /c "..." if you need cmd-specific syntax
Status Values
running - Process is still active
launching - Internal-only launch state; user-facing status is shown as running until failure is proven
completed - Process finished
failed - Process exited with error
stale - Record is healthy but PID is gone and no exit code was found
missing / corrupt / orphaned - Record problem surfaced by bg list / bg status

Launch failures keep the handle and mark the record failed instead of deleting it.

bg list also shows a short update marker when a job has a notable event such as completion, failure, or matched output.

Examples
# Download large file
bg run "curl -O https://example.com/large_file.zip"

# Run tests in background
bg run "pytest tests/ -v"

# Start a server
bg run "python -m http.server 8000"

# Check one job as JSON
bg status sleepy-pytest

# Check all running jobs
bg list

# Wait for a job to finish
bg wait sleepy-pytest

# Wait for a log line to appear
bg wait sleepy-pytest --match "ready"

# Wait for all known jobs
bg wait-all

# Read merged logs
bg logs sleepy-pytest

# Restart a job
bg restart sleepy-pytest

# Native PowerShell command
bg run "Get-Process | Sort-Object CPU -Descending | Select-Object -First 5"

# Force cmd syntax when needed
bg run "cmd.exe /d /c dir"

Weekly Installs
9
Repository
lirrensi/agent-…-helpers
GitHub Stars
3
First Seen
Mar 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn