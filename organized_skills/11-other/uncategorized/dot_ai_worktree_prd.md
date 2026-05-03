---
rating: ⭐⭐⭐
title: dot-ai-worktree-prd
url: https://skills.sh/vfarcic/dot-ai/dot-ai-worktree-prd
---

# dot-ai-worktree-prd

skills/vfarcic/dot-ai/dot-ai-worktree-prd
dot-ai-worktree-prd
Installation
$ npx skills add https://github.com/vfarcic/dot-ai --skill dot-ai-worktree-prd
SKILL.md
Create Git Worktree for PRD

Create a git worktree with a descriptive branch name based on the PRD title. This ensures feature branches have human-readable names that describe what the work is about.

Workflow
Step 1: Identify the PRD

Try to infer the PRD number from the current conversation. Look for PRD references like "PRD 353", "PRD #353", or "prd-353".

If not found in context, ask the user: "Which PRD should I create a worktree for? (e.g., 353)"

Step 2: Get the PRD Title

If the PRD content is already in the conversation context, extract the title from there.

Otherwise, read the PRD file. PRD files are in the prds/ directory with naming pattern [number]-[slug].md:

ls prds/ | grep "^[PRD_NUMBER]-"


The title is on the first line in format: # PRD #[number]: [Title]

Step 3: Generate Descriptive Branch Name

Convert the PRD title to a branch-friendly name:

Start with prd-[number]-
Extract the title after the colon (e.g., "Update to Kimi K2.5 Model Support")
Convert to lowercase
Replace spaces with hyphens
Remove special characters except hyphens and dots
Keep it concise (truncate if very long)

Examples:

"PRD #353: Update to Kimi K2.5 Model Support" → prd-353-kimi-k2.5-support
"PRD #290: Skills Distribution System" → prd-290-skills-distribution
"PRD #264: GitOps Tool ArgoCD Integration" → prd-264-gitops-argocd-integration
Step 4: Create the Worktree

Run the following commands directly. Replace [branch-name] with the name generated in Step 3.

Get the repo name and compute the worktree path:
repo_name=$(basename "$(git rev-parse --show-toplevel)")
worktree_path="../${repo_name}-[branch-name]"

Validate — check that the branch, worktree path, and worktree registration don't already exist:
git show-ref --verify --quiet "refs/heads/[branch-name]" && echo "ERROR: Branch already exists"
test -d "${worktree_path}" && echo "ERROR: Worktree path already exists"
git worktree list | grep -q "[branch-name]" && echo "ERROR: Worktree already registered"


If any check fails, inform the user and ask how to proceed.

Create the worktree branching from main:
git worktree add "${worktree_path}" -b [branch-name] main

Report the result to the user:
Worktree path: ${worktree_path}
Branch: [branch-name]
Next step: cd ${worktree_path}
Guidelines
Descriptive names: Branch names should describe the feature, not just the PRD number
Consistent format: Always prefix worktree directory with the repository name
Base on main: Always branch from main for new feature work
Clean names: Keep branch names concise but descriptive
Weekly Installs
25
Repository
vfarcic/dot-ai
GitHub Stars
308
First Seen
Feb 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass