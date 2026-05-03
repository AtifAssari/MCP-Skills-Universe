---
rating: ⭐⭐⭐
title: worker-image-investigation
url: https://skills.sh/jwmossmoz/agent-skills/worker-image-investigation
---

# worker-image-investigation

skills/jwmossmoz/agent-skills/worker-image-investigation
worker-image-investigation
Installation
$ npx skills add https://github.com/jwmossmoz/agent-skills --skill worker-image-investigation
SKILL.md
Contains Shell Commands

This skill contains shell command directives (!`command`) that may execute system commands. Review carefully before installing.

Worker Image Investigation

Investigate Taskcluster task failures by comparing worker images, extracting SBOM info, and debugging Azure VMs.

Use this local skills checkout path for commands in this file:

SKILLS_ROOT=/Users/jwmoss/github_moz/agent-skills/skills
WII="$SKILLS_ROOT/worker-image-investigation/scripts/investigate.py"

Prerequisites
taskcluster CLI: brew install taskcluster
az CLI (for VM debugging): brew install azure-cli && az login
uv for running scripts
Usage
# Investigate a failing task - get worker pool, image version, status
uv run "$WII" investigate <TASK_ID>
uv run "$WII" investigate https://firefox-ci-tc.services.mozilla.com/tasks/<TASK_ID>

# Compare two tasks (e.g., passing vs failing on same revision)
uv run "$WII" compare <PASSING_TASK_ID> <FAILING_TASK_ID>

# List running workers in a pool (for Azure VM access)
uv run "$WII" workers gecko-t/win11-64-24h2

# Get SBOM/image info for a worker pool
uv run "$WII" sbom gecko-t/win11-64-24h2

# Get Windows build and GenericWorker version from Azure VM
uv run "$WII" vm-info <VM_NAME> <RESOURCE_GROUP>

Investigation Workflow
1. Initial Task Analysis
# Get task info including worker pool and image version
uv run "$WII" investigate <FAILING_TASK_ID>


Output includes: taskId, taskLabel, workerPool, workerId, imageVersion, status.

2. Resolve Treeherder Job ID

treeherder-cli --similar-history takes a Treeherder job ID, not a Taskcluster task ID. Resolve it from the task ID:

REPO=autoland  # or try, mozilla-central, etc.
curl -s "https://treeherder.mozilla.org/api/project/${REPO}/jobs/?task_id=<TASK_ID>&count=5" \
  | jq '.results[0] | {id, job_type_name, result, platform}'


Save the id field as JOB_ID.

3. Check Similar Job History for a Pass/Fail Cliff

Run --similar-history with a large count on the branch where failures are observed. A sudden flip from passing to all-failing indicates a regression — possibly an image update.

treeherder-cli --similar-history <JOB_ID> --similar-count 200 --repo autoland --json \
  | jq '[.[] | {result, job_type_name, push_timestamp}]'


Look for a timestamp where results flip from success to testfailed/busted. Correlate that date against when the image was rolled out.

4. Cross-Branch Comparison

If autoland shows all failures, check mozilla-central (which may be on an older image) to confirm whether the job type still passes elsewhere:

job_type="<job_type_name from step 2>"
enc=$(jq -nr --arg v "$job_type" '$v|@uri')

for repo in autoland mozilla-central mozilla-beta; do
  curl -s "https://treeherder.mozilla.org/api/project/${repo}/jobs/?job_type_name=${enc}&result=success&count=50" \
    | jq -r --arg repo "$repo" '
        if (.results|length)==0 then "\($repo)\tNO_PASSING_RUNS"
        else (.results|last) as $r | "\($repo)\t\($r.last_modified)\t\($r.id)"
        end'
done


If mozilla-central shows recent passes but autoland does not, the failure is branch/image-specific.

5. Compare Tasks to Confirm Image Version Difference

Grab a passing task ID from step 4 (e.g., from a mozilla-central run) and compare:

uv run "$WII" compare <PASSING_TASK_ID> <FAILING_TASK_ID>


Look for differences in imageVersion (e.g., 1.0.8 vs 1.0.9). A version bump that aligns with the pass/fail cliff confirms the image caused the regression.

6. Debug Running Worker (Azure)
# Find running workers
uv run "$WII" workers gecko-t/win11-64-24h2

# Get VM details - extract VM name from workerId (e.g., vm-xyz...)
uv run "$WII" vm-info vm-xyz RG-TASKCLUSTER-WORKER-MANAGER-PRODUCTION

7. Direct Azure VM Commands

For deeper investigation, use Azure CLI directly:

# Get Windows build number
az vm run-command invoke --resource-group RG-TASKCLUSTER-WORKER-MANAGER-PRODUCTION \
  --name <VM_NAME> --command-id RunPowerShellScript \
  --scripts "(Get-ItemProperty 'HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion').CurrentBuild"

# Get GenericWorker version
az vm run-command invoke --resource-group RG-TASKCLUSTER-WORKER-MANAGER-PRODUCTION \
  --name <VM_NAME> --command-id RunPowerShellScript \
  --scripts "Get-Content C:\\generic-worker\\generic-worker-info.json"

# Get recent Windows updates
az vm run-command invoke --resource-group RG-TASKCLUSTER-WORKER-MANAGER-PRODUCTION \
  --name <VM_NAME> --command-id RunPowerShellScript \
  --scripts "Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 10"

# Check for file system filters (AppLocker, etc.)
az vm run-command invoke --resource-group RG-TASKCLUSTER-WORKER-MANAGER-PRODUCTION \
  --name <VM_NAME> --command-id RunPowerShellScript \
  --scripts "fltMC"

Creating Debug VMs

Spin up a throwaway Azure VM from the same image a worker pool uses.

Constraints
VM name ≤ 15 characters — Windows NetBIOS limit. Generate short names (e.g., dbg-1a2b3c).
Confirm vmSize from worker manager — Never guess. Use the /taskcluster skill to look up the worker pool configuration and extract the vmSize from launchConfigs. Never hardcode or assume a VM size.
Use a simple password — These VMs are throwaway. Use Password1!.
Workflow
Use the /taskcluster skill to get the worker pool config for the target pool (e.g., gecko-t/win11-64-24h2). Extract the vmSize and image reference from config.launchConfigs.
Create the VM (name must be ≤ 15 chars):
az vm create \
  --resource-group jmoss-win11 \
  --name "dbg-abc123" \
  --image "<image-id-from-step-1>" \
  --size "<vmSize-from-step-1>" \
  --admin-username azureuser \
  --admin-password "Password1!" \
  --location eastus

Run commands on the VM:
az vm run-command invoke \
  --resource-group jmoss-win11 \
  --name "dbg-abc123" \
  --command-id RunPowerShellScript \
  --scripts "<POWERSHELL_COMMAND>"

Delete when done:
az vm delete --resource-group jmoss-win11 \
  --name "dbg-abc123" --yes


See references/azure-commands.md for the full command reference.

Common Resource Groups
Production: RG-TASKCLUSTER-WORKER-MANAGER-PRODUCTION
Staging: RG-TASKCLUSTER-WORKER-MANAGER-STAGING
Common Worker Pools
Pool	Description
gecko-t/win11-64-24h2	Windows 11 24H2 64-bit production
gecko-t/win11-64-24h2-alpha	Windows 11 24H2 64-bit alpha (os-integration)
gecko-t/win11-32-24h2	Windows 11 24H2 32-bit
Azure Resource Groups to Review
RG-TASKCLUSTER-WORKER-MANAGER-PRODUCTION contains all taskcluster azure windows 10 windows 11 windows server machines.
Stage Taskcluster

For CI tasks on fxci-config PRs:

uv run "$WII" --root-url https://stage.taskcluster.nonprod.cloudops.mozgcp.net \
  investigate <TASK_ID>

Output Format

All commands return JSON for easy parsing with jq:

uv run "$WII" investigate <TASK_ID> | jq '.imageVersion'
uv run "$WII" workers gecko-t/win11-64-24h2 | jq '.workers[0].workerId'

SBOM Encoding Note

Some Windows worker SBOM markdown artifacts are UTF-16LE encoded. If text looks garbled, decode before parsing:

curl -sL <SBOM_URL> | iconv -f UTF-16LE -t UTF-8

Related Skills
taskcluster: Query task status, logs, artifacts
treeherder: Find tasks by revision and job type
os-integrations: Run mach try commands for testing
References
Worker image configs: fxci-config/worker-images/
SBOM files: Check Azure Shared Image Gallery
ronin_puppet: Worker configuration management
Weekly Installs
16
Repository
jwmossmoz/agent-skills
GitHub Stars
3
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykWarn