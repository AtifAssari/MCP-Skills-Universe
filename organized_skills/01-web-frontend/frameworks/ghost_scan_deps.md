---
rating: ⭐⭐⭐
title: ghost-scan-deps
url: https://skills.sh/ghostsecurity/skills/ghost-scan-deps
---

# ghost-scan-deps

skills/ghostsecurity/skills/ghost-scan-deps
ghost-scan-deps
Installation
$ npx skills add https://github.com/ghostsecurity/skills --skill ghost-scan-deps
Summary

Scans dependency lockfiles for known vulnerabilities and generates severity-ranked findings with remediation guidance.

Discovers and scans all common lockfile formats (package-lock.json, yarn.lock, go.sum, Gemfile.lock, and others) across your repository
Identifies CVEs in dependencies and assigns severity levels to help prioritize remediation
Analyzes exploitability of each vulnerability candidate to distinguish high-risk from low-risk findings
Generates a structured scan report with actionable remediation guidance for each discovered vulnerability
SKILL.md
Ghost Security SCA Scanner — Orchestrator

You are the top-level orchestrator for Software Composition Analysis (SCA) scanning. Your ONLY job is to call the Task tool to spawn subagents to do the actual work. Each step below gives you the exact Task tool parameters to use. Do not do the work yourself.

Defaults
repo_path: the current working directory
scan_dir: ~/.ghost/repos/<repo_id>/scans/<short_sha>/deps
short_sha: git rev-parse --short HEAD (falls back to YYYYMMDD for non-git dirs)

$ARGUMENTS

Any values provided above override the defaults.

Execution
Setup — compute paths and create output directories
Initialize Wraith — install the wraith binary
Discover Lockfiles — find all dependency lockfiles in the repo
Scan for Vulnerabilities — run wraith against each lockfile
Analyze Candidates — assess exploitability of each candidate
Summarize Results — generate the final scan report
Step 0: Setup

Run this Bash command to compute the repo-specific output directory, create it, and locate the skill files:

repo_name=$(basename "$(pwd)") && remote_url=$(git remote get-url origin 2>/dev/null || pwd) && short_hash=$(printf '%s' "$remote_url" | git hash-object --stdin | cut -c1-8) && repo_id="${repo_name}-${short_hash}" && short_sha=$(git rev-parse --short HEAD 2>/dev/null || date +%Y%m%d) && ghost_repo_dir="$HOME/.ghost/repos/${repo_id}" && scan_dir="${ghost_repo_dir}/scans/${short_sha}/deps" && cache_dir="${ghost_repo_dir}/cache" && mkdir -p "$scan_dir/findings" && skill_dir=$(find . -path '*skills/scan-deps/SKILL.md' 2>/dev/null | head -1 | xargs dirname) && echo "scan_dir=$scan_dir cache_dir=$cache_dir skill_dir=$skill_dir"


Store scan_dir (the absolute path under ~/.ghost/repos/), cache_dir (the repo-level cache directory), and skill_dir (the absolute path to the skill directory containing agents/, scripts/, etc.).

After this step, your only remaining tool is Task. Do not use Bash, Read, Grep, Glob, or any other tool for Steps 1–5.

Step 1: Initialize Wraith

Call the Task tool to initialize the wraith binary:

{
  "description": "Initialize wraith binary",
  "subagent_type": "general-purpose",
  "prompt": "You are the init agent. Read and follow the instructions in <skill_dir>/agents/init/agent.md.\n\n## Inputs\n- skill_dir: <skill_dir>"
}


The init agent installs wraith to ~/.ghost/bin/wraith (or wraith.exe on Windows).

Step 2: Discover Lockfiles

Call the Task tool to discover lockfiles in the repository:

{
  "description": "Discover lockfiles",
  "subagent_type": "general-purpose",
  "prompt": "You are the discover agent. Read and follow the instructions in <skill_dir>/agents/discover/agent.md.\n\n## Inputs\n- repo_path: <repo_path>\n- scan_dir: <scan_dir>"
}


The discover agent finds all lockfiles (go.mod, package-lock.json, etc.) and writes <scan_dir>/lockfiles.json.

If lockfile count is 0: Skip to Step 5 (Summarize) with no lockfiles found.

Step 3: Scan for Vulnerabilities

Call the Task tool to run the wraith scanner:

{
  "description": "Scan for vulnerabilities",
  "subagent_type": "general-purpose",
  "prompt": "You are the scan agent. Read and follow the instructions in <skill_dir>/agents/scan/agent.md.\n\n## Inputs\n- repo_path: <repo_path>\n- scan_dir: <scan_dir>"
}


The scan agent executes wraith for each lockfile and writes <scan_dir>/candidates.json.

If candidate count is 0: Skip to Step 5 (Summarize) with no vulnerabilities found.

Step 4: Analyze Candidates

Call the Task tool to analyze the vulnerability candidates:

{
  "description": "Analyze vulnerability candidates",
  "subagent_type": "general-purpose",
  "prompt": "You are the analysis agent. Read and follow the instructions in <skill_dir>/agents/analyze/agent.md.\n\n## Inputs\n- repo_path: <repo_path>\n- scan_dir: <scan_dir>\n- skill_dir: <skill_dir>\n- cache_dir: <cache_dir>"
}


The analysis agent spawns parallel analyzers for each candidate to assess exploitability and writes finding files to <scan_dir>/findings/.

Step 5: Summarize Results

Call the Task tool to summarize the findings:

{
  "description": "Summarize scan results",
  "subagent_type": "general-purpose",
  "prompt": "You are the summarize agent. Read and follow the instructions in <skill_dir>/agents/summarize/agent.md.\n\n## Inputs\n- repo_path: <repo_path>\n- scan_dir: <scan_dir>\n- skill_dir: <skill_dir>\n- cache_dir: <cache_dir>"
}


After executing all the tasks, report the scan results to the user.

Error Handling

If any Task call fails, retry it once. If it fails again, stop and report the failure.

Weekly Installs
1.4K
Repository
ghostsecurity/skills
GitHub Stars
400
First Seen
1 day ago
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn