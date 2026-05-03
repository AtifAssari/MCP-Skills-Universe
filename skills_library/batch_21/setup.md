---
title: setup
url: https://skills.sh/spm1001/claude-suite/setup
---

# setup

skills/spm1001/claude-suite/setup
setup
Installation
$ npx skills add https://github.com/spm1001/claude-suite --skill setup
SKILL.md
Setup

Install Claude behavioral skills with one command.

When to Use
Fresh Claude Code installation
New machine setup
After cloning trousse for the first time
When /open or /close commands don't work
When NOT to Use
Skills are already installed and working
Just want to update existing skills (use git pull instead)
Installing a single skill (manually symlink it)
Quick Start
/setup           # Interactive — installs all behavioral skills, offers tool repos
/setup --verify  # Check existing setup

What Gets Installed

Behavioral skills (all installed together):

Session lifecycle: /open, /close
Utilities: diagram, screenshot, filing, github-cleanup, picture, server-checkup, skill-check, sprite, dbt

Optional tool repos (offered after core install):

todoist-gtd — GTD-flavored Todoist integration
garde-manger — Searchable memory across sessions
Workflow
Phase 1: Check Prerequisites
# Check for required tools
command -v gh &>/dev/null || echo "MISSING: GitHub CLI (brew install gh)"
command -v uv &>/dev/null || echo "MISSING: uv (brew install uv)"

# Create directories
mkdir -p ~/.claude/skills
mkdir -p ~/.claude/scripts
mkdir -p ~/.claude/hooks

Phase 2: Clone and Symlink
# Clone trousse if not present
if [ ! -d ~/Repos/trousse ]; then
    gh repo clone spm1001/trousse ~/Repos/trousse
fi

SUITE="$HOME/Repos/trousse"

# Symlink all skills
for skill in "$SUITE/skills/"*/; do
    name=$(basename "$skill")
    ln -sf "$skill" ~/.claude/skills/"$name"
done

Phase 3: Symlink Scripts and Hooks
# Scripts (if present)
if [ -d "$SUITE/scripts" ]; then
    for script in "$SUITE/scripts/"*.sh; do
        [ -f "$script" ] && ln -sf "$script" ~/.claude/scripts/
    done
fi

# Hooks (if present)
if [ -d "$SUITE/hooks" ]; then
    for hook in "$SUITE/hooks/"*.sh; do
        [ -f "$hook" ] && ln -sf "$hook" ~/.claude/hooks/
    done
fi

Phase 4: Offer Tool Repos

Use AskUserQuestion:

Core skills installed. Want to add tool integrations?

[ ] todoist-gtd — GTD task management with Todoist
[ ] garde-manger — Search past sessions


If todoist-gtd selected:

gh repo clone spm1001/todoist-gtd ~/Repos/todoist-gtd
ln -sf ~/Repos/todoist-gtd/skills/todoist-gtd ~/.claude/skills/todoist-gtd

# Run OAuth
todoist auth


If garde-manger selected:

gh repo clone spm1001/garde-manger ~/Repos/garde-manger
cd ~/Repos/garde-manger && uv sync
ln -sf ~/Repos/garde-manger/skill ~/.claude/skills/garde

# Initial scan
cd ~/Repos/garde-manger && uv run garde scan

Phase 5: Verify
# List installed skills
ls ~/.claude/skills/

# Test key skills
ls -la ~/.claude/skills/open


Tell user to restart Claude (/exit then claude) to load new skills.

Verification
Check	Command	Expected
Skills directory	ls ~/.claude/skills/	13+ skill symlinks
Session skills	ls -la ~/.claude/skills/open	Points to trousse
Updating
cd ~/Repos/trousse && git pull
# Symlinks automatically point to updated content

Anti-Patterns
Pattern	Problem	Fix
Running setup when skills exist	Overwrites custom symlinks	Use --verify first
Skipping OAuth for todoist-gtd	Skill fails silently	Complete auth flow
Not restarting Claude after install	Skills not loaded	/exit then claude
Weekly Installs
16
Repository
spm1001/claude-suite
GitHub Stars
1
First Seen
Jan 31, 2026
Security Audits
Gen Agent Trust HubFail
SocketFail
SnykWarn