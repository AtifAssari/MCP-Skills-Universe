---
title: ghost-repo-context
url: https://skills.sh/ghostsecurity/skills/ghost-repo-context
---

# ghost-repo-context

skills/ghostsecurity/skills/ghost-repo-context
ghost-repo-context
Installation
$ npx skills add https://github.com/ghostsecurity/skills --skill ghost-repo-context
Summary

Scans repository structure, detects projects, maps dependencies, and generates a comprehensive codebase overview document.

Automatically detects project types, languages, frameworks, and dependency files across the repository
Generates a structured repo.md file documenting project architecture, components, and organization for security analysis or codebase understanding
Caches results in a configurable directory to avoid redundant scans on subsequent runs
Works entirely with local files; no external API calls or subagent delegation
SKILL.md
Repository Context Builder

You gather repository context by detecting projects, summarizing their architecture, and writing the results to repo.md. Do all work yourself — do not spawn subagents or delegate.

Inputs

Parse these from $ARGUMENTS (key=value pairs):

repo_path: path to the repository root
cache_dir: path to the cache directory (defaults to ~/.ghost/repos/<repo_id>/cache)

$ARGUMENTS

If cache_dir is not provided, compute it:

repo_name=$(basename "$(pwd)") && remote_url=$(git remote get-url origin 2>/dev/null || pwd) && short_hash=$(printf '%s' "$remote_url" | git hash-object --stdin | cut -c1-8) && repo_id="${repo_name}-${short_hash}" && cache_dir="$HOME/.ghost/repos/${repo_id}/cache" && echo "cache_dir=$cache_dir"

Tool Restrictions

Do NOT use WebFetch or WebSearch. All work must use only local files in the repository.

Setup

Discover this skill's own directory so you can reference agent files:

skill_dir=$(find . -path '*/skills/repo-context/SKILL.md' 2>/dev/null | head -1 | xargs dirname)
echo "skill_dir=$skill_dir"

Check Cache First

Check if <cache_dir>/repo.md already exists. If it does, skip everything and return:

Repository context is at: <cache_dir>/repo.md


If it does not exist, run mkdir -p <cache_dir> and continue.

Workflow

Detect Projects — Read <skill_dir>/detector.md and follow its instructions against <repo_path>. Save the full detection output (project details needed for step 2). If detection finds no projects, write a minimal repo.md noting "No projects detected" and skip to step 4.

Summarize Each Project — Read <skill_dir>/summarizer.md. For EACH project detected in step 1, follow the summarizer instructions using that project's details (id, type, base_path, languages, frameworks, dependency_files, extensions, evidence). Collect the summary for each project. If summarization fails for a project, note it as "summary unavailable" and continue with remaining projects.

Write repo.md — Combine detection and summary results into <cache_dir>/repo.md using the format in <skill_dir>/template-repo.md. For each project include:

Detection: ID, Type, Base Path, Languages, Frameworks, Dependency Files, Extensions, Evidence
Summary: Architectural summary, Sensitive Data Types, Business Criticality, Component Map, Evidence

Validate — Read <cache_dir>/repo.md back and verify it contains the expected sections from <skill_dir>/template-repo.md (e.g., project entries with Detection and Summary fields). If the file is missing or malformed, retry the write once before reporting an error.

Output — Return: Repository context is at: <cache_dir>/repo.md

Weekly Installs
1.2K
Repository
ghostsecurity/skills
GitHub Stars
400
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass