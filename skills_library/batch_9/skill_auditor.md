---
title: skill-auditor
url: https://skills.sh/haha0815/claude-meta-skills/skill-auditor
---

# skill-auditor

skills/haha0815/claude-meta-skills/skill-auditor
skill-auditor
Installation
$ npx skills add https://github.com/haha0815/claude-meta-skills --skill skill-auditor
SKILL.md
Claude Skill Auditor & Central Repository Manager
Overview

Two responsibilities:

Audit — Analyze SKILL.md bundles: extract metadata, detect overlap, produce cleanup plans with merge proposals.
Central Repo — Manage a central skills repository ($HOME/.claude-skills-repo), symlink skills into projects, migrate scattered skills, and keep everything in sync.

Two-turn protocol (audit mode): On the first message describing an audit task, confirm understanding and request the skill bundle. Do not analyze until the bundle is provided.

MANDATORY: Every operation ends with skillshare sync to distribute changes across all AI tool targets.

When to Use
Audit Triggers
User pastes multiple SKILL.md files and asks for analysis
User wants to find duplicate or overlapping skills
User wants a consolidation or cleanup plan for their skill library
User asks which skills to merge, archive, or delete
Central Repository Triggers
User wants to set up a central skills repository
User wants to share skills across multiple projects
User wants to migrate project-level skills into a central location
User wants to sync new skills to existing projects
User asks to audit which projects use which skills
User wants to verify symlink health across projects
Part 1: Skill Audit
Parsing Rules

Split input into skills using the strongest available delimiter:

=== SKILL: <name> === (preferred)
# SKILL: <name> or ## SKILL: <name>
If boundaries are ambiguous → create an UNSURE_BOUNDARY note; never guess

For each skill extract:

skill_name — from delimiter; if missing, use Unnamed Skill NN and flag as uncertain
short_description — 1–2 sentences
main_category — from taxonomy below
notable_allowed_tools / hooks / side_effects — tool whitelists, file writes, APIs, memory writes, external sends; if not specified → mark as "Not specified" and flag as governance risk
Output Order
A) Per-Skill Extraction

Compact structured list (Markdown bullets or JSON) with all fields above plus uncertainty_notes.

B) Consolidation Table

| skill_name | main_category | similar_skills | overlap_level | recommended_action | rationale |

overlap_level: low / medium / high (see rubric below) recommended_action: keep / merge / disable / archive / delete

C) Merge Candidates (high overlap only)

For each group:

Proposed consolidated skill name
1–2 sentence description
Core instructions as bullets
What to deprecate and why
Migration notes (content from old skills that must be preserved)
D) Prioritized Cleanup Checklist (10–15 items)
Quick wins first: duplicates, obvious merges, dead skills
Rewrites: vague descriptions, missing tool constraints
Governance: naming conventions, category taxonomy, templates
Overlap Scoring Rubric
Level	Criteria
High	Same purpose, similar steps, same tools/hook patterns — mostly duplicate
Medium	Same domain but different workflows or constraints
Low	Loosely related; minimal shared intent

Overlap indicators: same trigger/goal verbs · same inputs/outputs · same tools or side effects · similar examples or templates

Part 2: Central Skills Repository
Environment
SKILLS_REPO="${CLAUDE_SKILLS_REPO:-$HOME/.claude-skills-repo}"


Use $CLAUDE_SKILLS_REPO env var if set, otherwise default to $HOME/.claude-skills-repo. This allows team members to use different paths.

Step 1: Initialize Central Repository

Run when the central repo doesn't exist yet:

SKILLS_REPO="${CLAUDE_SKILLS_REPO:-$HOME/.claude-skills-repo}"

if [ ! -d "$SKILLS_REPO" ]; then
    mkdir -p "$SKILLS_REPO"
    cd "$SKILLS_REPO"
    git init
    cat > README.md << 'HEREDOC'
# Central Claude Skills Repository

Single source of truth for reusable Claude skills.
Each subdirectory contains a skill with its SKILL.md and supporting files.

## Structure
- `<skill-name>/SKILL.md` — one directory per skill
- Projects symlink to skills they need from here
- Changes here propagate instantly to all linked projects
- Use `$CLAUDE_SKILLS_REPO` env var to override the default path
HEREDOC
    git add -A && git commit -m "Initialize central skills repository"
    echo "Central repo created at $SKILLS_REPO"
else
    echo "Central repo already exists at $SKILLS_REPO"
fi

Step 2: Scan & Migrate Existing Skills

First, scan for all project-level skills:

SKILLS_REPO="${CLAUDE_SKILLS_REPO:-$HOME/.claude-skills-repo}"

echo "=== Scanning for project-level skills ==="
find ~/ -path "*/.claude/skills/*/SKILL.md" \
    -not -path "*/.claude-skills-repo/*" \
    -not -path "*/node_modules/*" \
    2>/dev/null | while read skillfile; do
    skill_dir=$(dirname "$skillfile")
    skill_name=$(basename "$skill_dir")
    project_dir=$(echo "$skill_dir" | sed 's|/.claude/skills/.*||')

    # Check if it's already a symlink
    if [ -L "$skill_dir" ]; then
        target=$(readlink "$skill_dir")
        echo "  LINKED: $skill_name ($project_dir) -> $target"
    else
        echo "  LOCAL:  $skill_name ($project_dir)"
    fi
done


To migrate a specific skill:

migrate_skill() {
    local SKILL_NAME="$1"
    local SOURCE_PROJECT="$2"
    local SKILLS_REPO="${CLAUDE_SKILLS_REPO:-$HOME/.claude-skills-repo}"
    local SOURCE="$SOURCE_PROJECT/.claude/skills/$SKILL_NAME"

    if [ ! -d "$SOURCE" ]; then
        echo "ERROR: $SOURCE does not exist"
        return 1
    fi

    if [ -L "$SOURCE" ]; then
        echo "SKIP: $SKILL_NAME is already a symlink"
        return 0
    fi

    if [ -d "$SKILLS_REPO/$SKILL_NAME" ]; then
        echo "WARNING: $SKILL_NAME already exists in central repo"
        echo "  Central: $(head -5 "$SKILLS_REPO/$SKILL_NAME/SKILL.md")"
        echo "  Local:   $(head -5 "$SOURCE/SKILL.md")"
        echo "  Skipping — resolve manually (diff the two versions)"
        return 1
    fi

    # Copy to central repo
    cp -r "$SOURCE" "$SKILLS_REPO/$SKILL_NAME"
    # Remove original and create symlink
    rm -rf "$SOURCE"
    ln -s "$SKILLS_REPO/$SKILL_NAME" "$SOURCE"

    echo "MIGRATED: $SKILL_NAME -> $SKILLS_REPO/$SKILL_NAME"
    ls -la "$SOURCE"
}

Step 3: Link Skills to a Project
link_skills() {
    local PROJECT_DIR="$1"
    local MODE="${2:-all}"  # "all" or skill name
    local SKILLS_REPO="${CLAUDE_SKILLS_REPO:-$HOME/.claude-skills-repo}"

    mkdir -p "$PROJECT_DIR/.claude/skills"

    if [ "$MODE" = "all" ]; then
        # Link ALL skills
        for skill_dir in "$SKILLS_REPO"/*/; do
            local skill_name=$(basename "$skill_dir")
            [ -f "$skill_dir/SKILL.md" ] || continue
            [ "$skill_name" = ".git" ] && continue
            if [ -L "$PROJECT_DIR/.claude/skills/$skill_name" ]; then
                echo "  SKIP: $skill_name (already linked)"
                continue
            fi
            ln -s "$SKILLS_REPO/$skill_name" "$PROJECT_DIR/.claude/skills/$skill_name"
            echo "  LINKED: $skill_name"
        done
    else
        # Link single skill
        if [ ! -d "$SKILLS_REPO/$MODE" ]; then
            echo "ERROR: Skill '$MODE' not found in central repo"
            return 1
        fi
        ln -s "$SKILLS_REPO/$MODE" "$PROJECT_DIR/.claude/skills/$MODE"
        echo "  LINKED: $MODE"
    fi
}


Link by tag (requires .tags file in skill directory):

link_by_tag() {
    local PROJECT_DIR="$1"
    local TAG="$2"
    local SKILLS_REPO="${CLAUDE_SKILLS_REPO:-$HOME/.claude-skills-repo}"

    mkdir -p "$PROJECT_DIR/.claude/skills"

    for skill_dir in "$SKILLS_REPO"/*/; do
        [ -f "$skill_dir/.tags" ] || continue
        if grep -q "$TAG" "$skill_dir/.tags"; then
            local skill_name=$(basename "$skill_dir")
            [ -L "$PROJECT_DIR/.claude/skills/$skill_name" ] && continue
            ln -s "$skill_dir" "$PROJECT_DIR/.claude/skills/$skill_name"
            echo "  LINKED (tag=$TAG): $skill_name"
        fi
    done
}

Step 4: Verify Setup
verify_project() {
    local PROJECT_DIR="${1:-$(pwd)}"
    local SKILLS_REPO="${CLAUDE_SKILLS_REPO:-$HOME/.claude-skills-repo}"
    local ok=0 broken=0 local_count=0

    echo "=== Symlinked Skills ($PROJECT_DIR) ==="
    for entry in "$PROJECT_DIR/.claude/skills"/*/; do
        local name=$(basename "${entry%/}")
        if [ -L "${entry%/}" ]; then
            local target=$(readlink "${entry%/}")
            if [ -f "$target/SKILL.md" ]; then
                echo "  OK: $name -> $target"
                ((ok++))
            else
                echo "  BROKEN: $name -> $target (SKILL.md missing!)"
                ((broken++))
            fi
        elif [ -d "$entry" ]; then
            echo "  LOCAL: $name (not symlinked)"
            ((local_count++))
        fi
    done

    echo ""
    echo "=== Available in Central Repo (not linked) ==="
    for skill_dir in "$SKILLS_REPO"/*/; do
        local skill_name=$(basename "$skill_dir")
        [ -f "$skill_dir/SKILL.md" ] || continue
        [ "$skill_name" = ".git" ] && continue
        if [ ! -L "$PROJECT_DIR/.claude/skills/$skill_name" ] && \
           [ ! -d "$PROJECT_DIR/.claude/skills/$skill_name" ]; then
            local desc=$(sed -n '/^description:/s/^description: *//p' "$skill_dir/SKILL.md" 2>/dev/null | head -1)
            echo "  AVAILABLE: $skill_name — $desc"
        fi
    done

    echo ""
    echo "Summary: $ok linked, $broken broken, $local_count local-only"

    if [ "$broken" -gt 0 ]; then
        echo ""
        echo "Fix broken symlinks:"
        echo "  find \"$PROJECT_DIR/.claude/skills/\" -type l ! -exec test -e {} \\; -print"
    fi
}

Step 5: Sync New Skills to Projects

After adding new skills to the central repo, detect what's new:

sync_new_skills() {
    local PROJECT_DIR="${1:-$(pwd)}"
    local SKILLS_REPO="${CLAUDE_SKILLS_REPO:-$HOME/.claude-skills-repo}"
    local new_count=0

    echo "=== New skills available for $PROJECT_DIR ==="
    for skill_dir in "$SKILLS_REPO"/*/; do
        local skill_name=$(basename "$skill_dir")
        [ -f "$skill_dir/SKILL.md" ] || continue
        [ "$skill_name" = ".git" ] && continue
        if [ ! -L "$PROJECT_DIR/.claude/skills/$skill_name" ] && \
           [ ! -d "$PROJECT_DIR/.claude/skills/$skill_name" ]; then
            local desc=$(sed -n '/^description:/s/^description: *//p' "$skill_dir/SKILL.md" 2>/dev/null | head -1)
            echo "  NEW: $skill_name"
            [ -n "$desc" ] && echo "       $desc"
            ((new_count++))
        fi
    done

    if [ "$new_count" -eq 0 ]; then
        echo "  All central repo skills are already linked."
    else
        echo ""
        echo "$new_count new skill(s) available. Link with:"
        echo "  ln -s \"\$SKILLS_REPO/<name>\" \"$PROJECT_DIR/.claude/skills/<name>\""
    fi
}

Step 6: Git Integration
commit_central_repo() {
    local SKILLS_REPO="${CLAUDE_SKILLS_REPO:-$HOME/.claude-skills-repo}"
    cd "$SKILLS_REPO"
    git add -A
    if ! git diff --cached --quiet; then
        git commit -m "Update skills: $(date +%Y-%m-%d)"
        echo "Central repo committed."
    else
        echo "Central repo: no changes to commit."
    fi
}


In project repos, symlinks are committed as-is — collaborators need the same $CLAUDE_SKILLS_REPO path or the env var set.

Step 7: Cross-Project Audit

List all projects using a specific skill:

audit_skill_usage() {
    local SKILL_NAME="$1"
    local SKILLS_REPO="${CLAUDE_SKILLS_REPO:-$HOME/.claude-skills-repo}"

    echo "=== Projects using '$SKILL_NAME' ==="
    find ~/ -lname "*/.claude-skills-repo/$SKILL_NAME" 2>/dev/null | while read link; do
        local project=$(echo "$link" | sed 's|/.claude/skills/.*||')
        echo "  $project"
    done
}

Part 3: Troubleshooting
Broken Symlink
# Find all broken symlinks
find .claude/skills/ -type l ! -exec test -e {} \; -print

# Fix: remove and recreate
rm .claude/skills/broken-skill
ln -s "$HOME/.claude-skills-repo/broken-skill" .claude/skills/broken-skill

Skill Not Loading
Verify SKILL.md exists: cat .claude/skills/<name>/SKILL.md
Check symlink resolves: ls -L .claude/skills/<name>/SKILL.md
Ensure frontmatter is valid YAML between --- markers
Category Taxonomy
Content Transformation (translate, rewrite, summarize)
Research & Enrichment (web research, expansion, citations)
Document & File Ops (PDF/DOCX/XLSX generation/editing)
Web & Automation (scraping, scheduled tasks, monitoring)
Dev & Integration (APIs, pipelines, codegen, CI/CD)
Creative / Media (image/video prompts, branding)
Governance / Meta (auditing, linting, policy enforcement)
Skill Management (repo setup, symlinks, sync, migration) ← NEW
Integrity Rules
Never invent tool permissions or side effects
If a skill omits tools → "Not specified" + governance risk flag
If a delimiter is missing → label uncertain + propose fix
Every recommendation must be justified:
"Merge" → include concrete consolidated skill spec
"Disable/Archive/Delete" → cite specific reason (duplicate, obsolete, too vague, risky, unused assumptions)
Never rm -rf symlinked skills — this deletes the source. Use skillshare uninstall or manual rm on the symlink only.
Optional: Governance Template

If the skill set is messy, propose a standardized SKILL.md template:

---
name: skill-name
version: 1.0.0
owner: <team/person>
category: <from taxonomy>
description: Use when...
---

# Skill Name

## Triggers
## Inputs / Outputs
## Allowed Tools & Side Effects
## Safety Constraints
## Examples
## Acceptance Criteria

Common Mistakes
Analyzing before receiving the bundle (violates two-turn handshake)
Inventing tool permissions when a skill doesn't mention them
Recommending "merge" without providing the actual merged spec
Using a category set that grows unbounded — keep to the 8 categories above unless a clear gap exists
Running rm -rf on a symlink target instead of removing the symlink
Forgetting to run sync after making changes
MANDATORY: Final Sync

Every operation performed by this skill MUST end with a skillshare sync command.

After any audit, migration, linking, verification, or repo change:

echo ""
echo "=== Running final skillshare sync ==="
skillshare sync
echo "=== Sync complete ==="


This ensures all changes are distributed across all configured AI tool targets (Claude, Cursor, Windsurf, etc.). Never skip this step.

Notes on sync:

Personal global skills (~/.claude/skills/) load for ALL projects automatically — no symlinks needed
Project skills (.claude/skills/) only load for that project — use symlinks to share
skillshare sync handles distributing from source of truth to all targets
If skillshare is not installed, warn the user and provide fallback manual sync guidance
Weekly Installs
10
Repository
haha0815/claude…a-skills
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubWarn
SocketFail
SnykPass