---
rating: ⭐⭐⭐
title: asciinema-streaming-backup
url: https://skills.sh/terrylica/cc-skills/asciinema-streaming-backup
---

# asciinema-streaming-backup

skills/terrylica/cc-skills/asciinema-streaming-backup
asciinema-streaming-backup
Installation
$ npx skills add https://github.com/terrylica/cc-skills --skill asciinema-streaming-backup
SKILL.md
asciinema-streaming-backup

Complete system for streaming asciinema recordings to GitHub with automatic brotli archival. Uses idle-detection for intelligent chunking, zstd for concatenatable streaming compression, and GitHub Actions for final brotli recompression.

Self-Evolving Skill: This skill improves through use. If instructions are wrong, parameters drifted, or a workaround was needed — fix this file immediately, don't defer. Only update for real, reproducible issues.

When to Use This Skill

Use this skill when:

Setting up real-time backup of asciinema recordings to GitHub
Configuring idle-detection chunking for recordings
Creating orphan branch infrastructure for recording storage
Integrating GitHub Actions for brotli recompression

Platform: macOS, Linux Isolation: Uses Git orphan branch (separate history, cannot pollute main)

Architecture Overview
┌─────────────────┐     zstd chunks      ┌─────────────────┐     Actions      ┌─────────────────┐
│  asciinema rec  │ ──────────────────▶  │  GitHub Orphan  │ ───────────────▶ │  brotli archive │
│  + idle-chunker │   (concatenatable)   │  gh-recordings  │                  │  (300x compress)│
└─────────────────┘                      └─────────────────┘                  └─────────────────┘
         │                                        │
         │ Idle ≥30s triggers chunk               │ Separate history
         ▼                                        │ Cannot PR to main
    ~/asciinema_recordings/                                 ▼
    └── repo-name/                          .github/workflows/
        └── chunks/*.zst                    └── recompress.yml

Requirements
Component	Required	Installation	Version
asciinema CLI	Yes	brew install asciinema	3.0+ (Rust)
zstd	Yes	brew install zstd	Any
brotli	Yes	brew install brotli	Any
git	Yes	Pre-installed	2.20+
gh CLI	Yes	brew install gh	Any
fswatch	Optional	brew install fswatch	For real-time
Workflow Phases
Phase 0: Preflight Validation

Verify all tools installed, offer self-correction if missing. Run the preflight check script, then AskUserQuestion to offer installation for missing tools.

See Setup Scripts for the complete preflight-check.sh script.

Self-Correction: If tools are missing, generate installation command and offer to run it.

Phase 1: GitHub Account Detection

Detect available GitHub accounts from 5 sources (SSH config, SSH keys, gh CLI, mise env, git config) and let user choose which to use.

See Account & Repository Detection for the detection script, scoring logic, and AskUserQuestion flow.

Phase 1.5: Current Repository Detection

Detect current git repository context (CURRENT_REPO_OWNER, CURRENT_REPO_NAME, DETECTED_FROM) to provide intelligent defaults for Phase 2.

See Account & Repository Detection for the detection script.

Phase 2: Core Configuration

Gather essential configuration: repository URL (with auto-detection from Phase 1.5), recording directory, and branch name.

See Configuration Reference for all AskUserQuestion sequences and URL normalization logic.

Phase 3: Advanced Configuration

Allow customization of compression and behavior parameters:

Parameter	Default	Range
Idle threshold	30s	5-300s
zstd level	3	1-22
Brotli level	9	1-11
Auto-push	Yes	Yes/No
Poll interval	5s	2s, 5s, 10s

See Configuration Reference for all AskUserQuestion sequences.

Phase 4: Orphan Branch Setup

Create or configure the orphan branch with GitHub Actions workflow. Checks for existing branch first and offers clone/reset/verify options.

Key actions:

Check if branch exists on remote via git ls-remote
If exists: AskUserQuestion for clone/reset/verify
If new: Create orphan branch, add workflow + directory structure, push

See Setup Scripts for the complete setup-orphan-branch.sh script. See GitHub Workflow for the full recompress.yml Actions workflow.

Phase 5: Local Environment Setup

Configure local directory and generate customized idle-chunker.sh with user parameters embedded from Phase 3.

Key actions:

Clone orphan branch to ~/asciinema_recordings/<repo>/
Generate idle-chunker.sh with embedded configuration
Display configuration summary and usage instructions

See Setup Scripts for local setup scripts. See Idle Chunker for the complete chunker implementation.

Phase 6: Autonomous Validation

Claude executes 8 tests autonomously, displaying formatted results. Only 2 tests require user action (recording test, chunker live test).

Test Category	Count	Autonomous?
Tool preflight	5	Yes
Compression round-trip	3	Yes
Repository validation	4	Yes
GitHub Actions trigger	1	Yes
Recording test	1	No (USER)
Chunker live test	1	No (USER)

See Autonomous Validation for the complete validation script, user-required test flows, and troubleshooting table.

Quick Start
First-Time Setup
/usr/bin/env bash << 'PREFLIGHT_EOF'
# 1. Check requirements
for tool in asciinema zstd brotli git gh; do
  command -v "$tool" &>/dev/null && echo "$tool: OK" || echo "$tool: MISSING"
done

# 2. Create orphan branch (replace with your repo)
REPO="git@github.com:YOUR/REPO.git"
./setup-orphan-branch.sh "$REPO"

# 3. Validate setup
./validate-setup.sh "$HOME/asciinema_recordings/REPO"
PREFLIGHT_EOF

Recording Session
/usr/bin/env bash << 'SKILL_SCRIPT_EOF'
# Terminal 1: Start recording
WORKSPACE=$(basename "$PWD")
asciinema rec $PWD/tmp/${WORKSPACE}_$(date +%Y-%m-%d_%H-%M).cast

# Terminal 2: Start idle-chunker
~/asciinema_recordings/REPO/idle-chunker.sh $PWD/tmp/${WORKSPACE}_*.cast
SKILL_SCRIPT_EOF

Key Design Decisions
Decision	Rationale
zstd for streaming	Supports frame concatenation (brotli doesn't)
brotli for archival	Best compression ratio (~300x for .cast files)
Orphan branch	Complete isolation, can't pollute main history
Idle-based chunking	Semantic breakpoints, not mid-output splits
Shallow clone	Minimal disk usage, can't accidentally access main
30s idle threshold	Balances chunk frequency vs semantic completeness
Troubleshooting

See Troubleshooting Guide for common issues and fixes.

Post-Change Checklist

After modifying this skill:

 Orphan branch creation scripts use heredoc wrapper
 All bash blocks compatible with zsh (no declare -A, no grep -P)
 GitHub Actions workflow validates brotli recompression
 Idle chunker handles both macOS and Linux stat syntax
 Detection flow outputs parseable key=value format
 References validate links to external documentation
Reference Documentation
Account & Repository Detection - GitHub account detection + repo context
Configuration Reference - AskUserQuestion sequences + task templates
Idle Chunker Script - Complete chunker implementation
GitHub Workflow - Full Actions workflow
Setup Scripts - All setup and validation scripts
Autonomous Validation - Validation script and user-required tests
Troubleshooting Guide - Common issues and fixes
asciinema 3.0 Docs
zstd Frame Format
Git Orphan Branches
Post-Execution Reflection

After this skill completes, reflect before closing the task:

Locate yourself. — Find this SKILL.md's canonical path before editing.
What failed? — Fix the instruction that caused it.
What worked better than expected? — Promote to recommended practice.
What drifted? — Fix any script, reference, or dependency that no longer matches reality.
Log it. — Evolution-log entry with trigger, fix, and evidence.

Do NOT defer. The next invocation inherits whatever you leave behind.

Weekly Installs
84
Repository
terrylica/cc-skills
GitHub Stars
39
First Seen
5 days ago
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn