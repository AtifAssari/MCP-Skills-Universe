---
title: document-update
url: https://skills.sh/jihunkim0/jk-skills/document-update
---

# document-update

skills/jihunkim0/jk-skills/document-update
document-update
Installation
$ npx skills add https://github.com/jihunkim0/jk-skills --skill document-update
SKILL.md
Document Update: Pre-PR Documentation Sync

Ensure every documentation file is accurate, up to date, and written in a friendly, succinctly, user-forward voice. Runs after a feature is completed, before a PR is opened or merged.

Autonomy Rules

You are mostly automated. The top-level rules below govern ALL steps — they are not repeated per-step.

Auto-update (never ask):

Factual corrections clearly supported by the diff
Adding items to tables/lists, updating paths/counts/versions
Fixing stale cross-references
CHANGELOG minor voice adjustments
Marking TODOS complete
Cross-doc factual inconsistencies (e.g., version mismatch)

Ask user first:

Narrative, philosophy, or security-related changes
Large rewrites or removals
New TODOS items to add
Cross-doc contradictions that are narrative (not factual)

NEVER do:

Overwrite, replace, or regenerate CHANGELOG entries — polish wording only, preserve all content
Use Write tool on CHANGELOG.md — always use Edit / Replace with exact matches
Step 1: Pre-flight & Diff Analysis
BASE_BRANCH=$(gh pr view --json baseRefName -q .baseRefName 2>/dev/null || gh repo view --json defaultBranchRef -q .defaultBranchRef.name 2>/dev/null || echo "main")

git diff $BASE_BRANCH...HEAD --stat
git log $BASE_BRANCH..HEAD --oneline
git diff $BASE_BRANCH...HEAD --name-only
find . -maxdepth 2 -name "*.md" -not -path "*/.git/*" -not -path "*/node_modules/*" | sort


Output: "Analyzing N files changed across M commits. Found K documentation files to review."

Step 2: Per-File Audit & Update

Read each doc file. Cross-reference against the diff. Apply auto-updates directly; queue risky changes for user confirmation.

File	Focus
README.md	Features, install/setup instructions, examples, usage descriptions still valid?
ARCHITECTURE.md	Component descriptions match code? Be conservative — only update clear contradictions.
AGENTS.md	Agent tools, behaviors, capabilities, configurations still accurate?
CONTRIBUTING.md	Walk through setup as a new contributor — would each command succeed?
Other .md files	Determine purpose/audience, check if diff contradicts anything.

For each file modified, output a one-line summary (e.g., "README.md: added feature X to capabilities list").

After auto-updates, present any risky/questionable changes to the user with your recommendation. Apply approved changes immediately.

Step 3: CHANGELOG Voice Polish

If CHANGELOG was modified in this branch:

Read the entire CHANGELOG.md first.
Review entries for voice:
Lead with what the user can now do — not implementation details
"You can now..." not "Refactored the..."
Rewrite entries that read like commit messages
Only modify wording. Never delete, reorder, or replace entries.
Step 4: Cross-Doc Consistency & Discoverability
README feature list matches what other docs describe?
ARCHITECTURE component list matches CONTRIBUTING project structure?
Discoverability: Is every doc file reachable from README.md? Every doc should be discoverable from the main entry point.
Step 5: TODOS Cleanup
Completed: Cross-reference diff against open TODO items. Move clearly completed items to "Completed" section.
Stale: If a TODO references significantly changed files, ask user whether to update, complete, or leave.
New: Check diff for TODO, FIXME, HACK comments. Ask user whether to capture in TODOS.md.
Step 6: Commit & Output

If no docs were modified (git status clean), output "All documentation is up to date." and exit.

Otherwise:

git add <modified doc files>
git commit -m "docs: sync documentation for recent changes"
git push


PR body update:

gh pr view --json body -q .body > /tmp/pr-body-$$.md
# Append/update a "## Documentation" section with doc diff preview
gh pr edit --body-file /tmp/pr-body-$$.md


Output a structured summary:

Documentation health:
  README.md       [Updated] (added feature X)
  CHANGELOG.md    [Voice polished] (adjusted wording)
  ARCHITECTURE.md [Current] (no changes needed)
  ...

Weekly Installs
8
Repository
jihunkim0/jk-skills
First Seen
Mar 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass