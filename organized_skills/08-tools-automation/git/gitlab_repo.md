---
rating: ⭐⭐⭐
title: gitlab-repo
url: https://skills.sh/grandcamel/gitlab-assistant-skills/gitlab-repo
---

# gitlab-repo

skills/grandcamel/gitlab-assistant-skills/gitlab-repo
gitlab-repo
Installation
$ npx skills add https://github.com/grandcamel/gitlab-assistant-skills --skill gitlab-repo
SKILL.md
Repository Skill

Repository and project operations for GitLab using the glab CLI.

Quick Reference
Operation	Command	Risk
Clone repo	glab repo clone <repo>	-
Fork repo	glab repo fork <repo>	⚠️
View repo	glab repo view	-
Create repo	glab repo create	⚠️
Search repos	glab repo search <query>	-
Archive repo	glab repo archive	⚠️⚠️
Delete repo	glab repo delete	⚠️⚠️⚠️
List contributors	glab repo contributors	-

Risk Legend: - Safe | ⚠️ Caution | ⚠️⚠️ Warning | ⚠️⚠️⚠️ Danger

When to Use This Skill

ALWAYS use when:

User wants to clone, fork, or create repositories
User mentions "repo", "repository", "project", "clone", "fork"
User wants to manage project settings

NEVER use when:

User wants to work with specific repo content (use git directly)
User wants to manage deploy keys (use gitlab-deploy-key skill)
Available Commands
Clone Repository
glab repo clone <repo> [directory] [options]


Arguments:

<repo> - Repository path, URL, or project ID
[directory] - Optional local directory name

Options:

Flag	Description
-g, --group=<group>	Clone all repos in a group
-p, --preserve-namespace	Clone into subdirectory based on namespace
-a, --archived=<bool>	Include/exclude archived repos (with -g)
--paginate	Fetch all pages of projects (with -g)

Examples:

# Clone by path
glab repo clone gitlab-org/cli

# Clone by URL
glab repo clone https://gitlab.com/gitlab-org/cli

# Clone into specific directory
glab repo clone gitlab-org/cli my-glab

# Clone by project ID
glab repo clone 4356677

# Clone preserving namespace structure
glab repo clone gitlab-org/cli -p
# Creates: gitlab-org/cli/

# Clone all repos in a group
glab repo clone -g mygroup --paginate

# Clone only non-archived repos from group
glab repo clone -g mygroup --archived=false --paginate

Fork Repository
glab repo fork <repo> [options]


Options:

Flag	Description
-c, --clone	Clone the fork after creating
-n, --name=<name>	Name for the forked project
-p, --path=<path>	Path for the forked project
--remote	Add a remote for the fork

Examples:

# Fork a repository
glab repo fork owner/repo

# Fork and clone
glab repo fork owner/repo --clone

# Fork with custom name
glab repo fork owner/repo --name="my-fork"

# Fork and add remote
glab repo fork owner/repo --remote

View Repository
glab repo view [repo] [options]


Options:

Flag	Description
-w, --web	Open repository in browser
-b, --branch=<branch>	View specific branch

Examples:

# View current repository info
glab repo view

# View specific repo
glab repo view gitlab-org/cli

# Open in browser
glab repo view --web

# View specific branch
glab repo view --branch=develop

Create Repository
glab repo create [name] [options]


Options:

Flag	Description
-n, --name=<name>	Repository name
-d, --description=<desc>	Repository description
-g, --group=<group>	Create in specific group/namespace
--public	Make repository public
--private	Make repository private
--internal	Make repository internal
--readme	Initialize with README
-c, --clone	Clone after creation

Examples:

# Create repository interactively
glab repo create

# Create with name and description
glab repo create my-project -d "My awesome project"

# Create public repo in group
glab repo create my-project --group=myteam --public

# Create and clone
glab repo create my-project --clone --readme

Search Repositories
glab repo search <query> [options]


Options:

Flag	Description
-P, --per-page=<n>	Results per page
--all	Get all results

Examples:

# Search for repos
glab repo search "cli tools"

# Search with more results
glab repo search "gitlab" --per-page=50

Archive Repository
glab repo archive [repo] [options]


Archives a repository (makes it read-only).

Examples:

# Archive current repo
glab repo archive

# Archive specific repo
glab repo archive owner/repo

Delete Repository
glab repo delete [repo] [options]


Warning: This permanently deletes the repository and all its data!

Options:

Flag	Description
-y, --yes	Skip confirmation prompt

Examples:

# Delete repo (will prompt for confirmation)
glab repo delete owner/repo

# Delete without confirmation (dangerous!)
glab repo delete owner/repo --yes

List Contributors
glab repo contributors [repo] [options]


Options:

Flag	Description
-P, --per-page=<n>	Results per page
--order=<order>	Sort order: name, email, commits

Examples:

# List contributors for current repo
glab repo contributors

# List with sorting
glab repo contributors --order=commits

Transfer Repository
glab repo transfer <repo> <new-namespace>


Transfer a repository to another namespace.

Examples:

# Transfer to different group
glab repo transfer myrepo newgroup

Common Workflows
Workflow 1: Fork and Contribute
# 1. Fork the repository
glab repo fork upstream/project --clone

# 2. Add upstream remote
cd project
git remote add upstream https://gitlab.com/upstream/project.git

# 3. Create feature branch
git checkout -b feature/my-change

# 4. Make changes, commit, push
git add . && git commit -m "Add feature"
git push -u origin feature/my-change

# 5. Create MR to upstream
glab mr create --target-branch=main

Workflow 2: Batch Clone Team Repos
# Clone all non-archived repos from team group
glab repo clone -g myteam --archived=false --paginate -p

# This creates:
# myteam/
#   repo1/
#   repo2/
#   ...

Workflow 3: Create New Project
# 1. Create the repository
glab repo create awesome-project \
  -d "An awesome new project" \
  --group=myteam \
  --readme \
  --clone

# 2. Set up the project
cd awesome-project
# Add initial files...

# 3. View it in browser
glab repo view --web

Troubleshooting
Issue	Cause	Solution
Authentication failed	Invalid/expired token	Run glab auth login
Repo not found	Invalid path or no access	Check repo path and permissions
Clone failed	SSH keys not configured	Use HTTPS or configure SSH keys
Cannot fork	Already forked or no permission	Check existing forks
Cannot delete	Not owner or maintainer	Request owner to delete
Related Documentation
Safeguards
Quick Reference
Weekly Installs
89
Repository
grandcamel/gitl…t-skills
GitHub Stars
1
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass