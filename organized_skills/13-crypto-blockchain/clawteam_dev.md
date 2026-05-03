---
rating: ⭐⭐
title: clawteam-dev
url: https://skills.sh/hkuds/clawteam/clawteam-dev
---

# clawteam-dev

skills/hkuds/clawteam/clawteam-dev
clawteam-dev
Installation
$ npx skills add https://github.com/hkuds/clawteam --skill clawteam-dev
SKILL.md
ClawTeam Local Development

This skill is for developing and validating ClawTeam inside the ClawTeam repository. Use it when the task is about changing ClawTeam itself, testing local behavior, or verifying multi-agent workflows against the current checkout.

Development Bootstrap

Standardize the local development environment with the bootstrap script:

bash scripts/bootstrap_clawteam_dev.sh


This script lives in scripts/bootstrap_clawteam_dev.sh inside this skill folder.

This script does all of the following:

Creates a fixed uv environment at ~/.clawteam-venv
Installs the current repository into that environment with dev dependencies
Writes ~/.local/bin/clawteam to point at the fixed environment
Adds a clawteam() shell function block to ~/.bashrc

After it finishes:

source ~/.bashrc
clawteam --version


Use this bootstrap whenever you want the same clawteam command across different Python environments on the machine.

Project Skill Wiring

To wire another local project so its ./.agents and ./.claude directories use this repository's local ClawTeam skills directly:

bash scripts/link_local_clawteam_skills.sh /path/to/project


This script lives in scripts/link_local_clawteam_skills.sh inside this skill folder.

This creates these symlinks inside the target project:

./.agents/skills/clawteam
./.claude/skills/clawteam

Run the same script again any time you want to refresh or recreate those links.

Typical Uses
Run targeted local validation after code changes
Reproduce a spawn / board / task / inbox / harness bug
Smoke-test the real CLI in tmux or subprocess mode
Review ClawTeam workflows end-to-end from the current repository checkout
Fast Validation

Prefer the smallest validation that proves the change.

ruff check clawteam/ tests/
pytest tests/<target_file>.py -q


Use broader runs only when the change crosses modules:

pytest tests/test_cli_commands.py -q
pytest tests/test_spawn_backends.py -q
pytest tests/test_harness.py tests/test_event_bus.py -q

Prerequisites
clawteam command available
tmux available
A supported CLI agent such as claude or codex if you are spawning real workers
Current directory is the ClawTeam git repo when testing worktree isolation or local source changes
Local Smoke Test

Use this when you need a real multi-agent workflow check instead of unit tests.

clawteam team spawn-team dev-smoke -d "Local ClawTeam smoke test" -n leader
clawteam task create dev-smoke "Smoke test worker" -o worker1 -p high
clawteam spawn --team dev-smoke --agent-name worker1 --task "Report your status to leader and mark the task completed when done."
clawteam board show dev-smoke
clawteam task wait dev-smoke --timeout 300 --poll-interval 5


If you are validating harness behavior specifically:

clawteam harness conduct dev-harness \
  --goal "Create a small implementation plan and execute it with one worker" \
  --cli codex \
  --agents 1

Cleanup

Use the real ClawTeam commands instead of ad-hoc directory assumptions whenever possible:

clawteam team cleanup dev-smoke
clawteam team cleanup dev-harness


If a crashed tmux session or worktree is left behind, clean it up explicitly after inspecting it.

Development Rules
Prefer clawteam commands over editing state files directly.
Prefer targeted tests over broad end-to-end runs unless the change crosses spawn/runtime/workflow boundaries.
Use board, task wait, and team status to observe behavior before assuming a bug is in the spawn layer.
When testing agent coordination, keep the team small first: one leader and one or two workers.
Only escalate to harness or full swarm tests when the lower-level task/spawn/inbox path already works.
Weekly Installs
34
Repository
hkuds/clawteam
GitHub Stars
5.0K
First Seen
5 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass