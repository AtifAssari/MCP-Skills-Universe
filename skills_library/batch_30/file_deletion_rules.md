---
title: file-deletion-rules
url: https://skills.sh/totto2727-dotfiles/agents/file-deletion-rules
---

# file-deletion-rules

skills/totto2727-dotfiles/agents/file-deletion-rules
file-deletion-rules
Installation
$ npx skills add https://github.com/totto2727-dotfiles/agents --skill file-deletion-rules
SKILL.md
File Deletion Rules
Rule (CRITICAL)

Skip if already deleted: If the target file does not exist in the working tree, do nothing. This rule applies only to files that currently exist.

NEVER use rm or unlink commands directly.

ALWAYS use git stash before deleting files to preserve them.

Apply without confirmation: When file deletion is needed, follow this rule without asking the user for confirmation. Execute the deletion process defined below.

Prohibited Commands

The following commands are strictly prohibited:

rm (any variant: rm -rf, rm -f, etc.)
unlink
Any direct file deletion without git stash
Deletion Process
For Modified Files (Tracked & Modified)

Save changes to git stash:

git stash push -m "[Deletion] <reason>" -- <files>


Remove file from git:

git rm <files>

For New Files (Untracked)

Stage the file:

git add <files>


Save to stash (file is automatically removed from working tree):

git stash push -m "[Deletion] <reason>" -- <files>

Stash Message Template

Use this format for stash messages:

[Deletion] <reason>
Files: <file1>, <file2>, ...

Examples
# Single file
git stash push -m "[Deletion] Remove deprecated API endpoints
Files: api/old-endpoint.js" -- api/old-endpoint.js

# Multiple files
git stash push -m "[Deletion] Clean up unused test fixtures
Files: test/fixtures/old.js, test/fixtures/deprecated.js" -- test/fixtures/old.js test/fixtures/deprecated.js

# Directory
git stash push -m "[Deletion] Remove legacy components
Files: src/components/legacy/" -- src/components/legacy/

Complete Examples
Good: Deleting Modified File
# Step 1: Save to stash
git stash push -m "[Deletion] Remove unused utility function
Files: utils/old-helper.js" -- utils/old-helper.js

# Step 2: Remove from git
git rm utils/old-helper.js

Good: Deleting Untracked File
# Step 1: Stage file
git add temp-file.js

# Step 2: Save to stash (removes from working tree)
git stash push -m "[Deletion] Remove temporary file
Files: temp-file.js" -- temp-file.js

Good: Deleting Multiple Files
# Save all files to stash
git stash push -m "[Deletion] Clean up deprecated modules
Files: module1.js, module2.js, module3.js" -- module1.js module2.js module3.js

# Remove from git
git rm module1.js module2.js module3.js

Bad: Direct Deletion
# DO NOT USE
rm file.js
rm -rf directory/
unlink file.js

Notes
Files saved to git stash can be recovered later if needed
Use descriptive reasons in stash messages for future reference
The stash preserves file contents even after deletion
List all files in the stash message for clarity
Related Skills
git-operations-rules - General git operation rules (unstage, undo, stash)
Weekly Installs
8
Repository
totto2727-dotfi…s/agents
First Seen
Feb 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketFail
SnykPass