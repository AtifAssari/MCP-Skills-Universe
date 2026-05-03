---
rating: ⭐⭐⭐
title: gitea
url: https://skills.sh/halfwhey/extea/gitea
---

# gitea

skills/halfwhey/extea/gitea
gitea
Installation
$ npx skills add https://github.com/halfwhey/extea --skill gitea
SKILL.md
Gitea

Interact with a Gitea instance using extea — a drop-in replacement for tea that adds project board (kanban) management.

Authentication
Use --login <name> (or -l <name>) for all commands to select a login profile.
Board password is stored in ~/.config/tea/config.yml alongside the login. Can also be set via GITEA_PASSWORD env var.
For git push/pull over HTTP, embed the token in the URL: http://user:TOKEN@<host>/owner/repo.git
Run extea login add to create a login (API token + optional board password).
Repos
extea repos list -l <login>
extea repos create --name <name> --description "<desc>" -l <login>
extea repos delete --name <name> --owner <owner> --force -l <login>


Do NOT use --init when creating a repo you plan to push an existing local repo into.

Issues
extea issues list -l <login> -r owner/repo
extea issues list -l <login> -r owner/repo --state all    # open + closed
extea issues create -l <login> -r owner/repo \
  --title "<title>" --description "<desc>" \
  --labels "<label1>,<label2>" --milestone "<milestone title>" --assignees "<user>"
extea issues close   -l <login> -r owner/repo <number>
extea issues reopen  -l <login> -r owner/repo <number>

Pull Requests
extea pulls list -l <login> -r owner/repo
extea pulls list -l <login> -r owner/repo --state all     # open + merged + closed
extea pulls create -l <login> -r owner/repo \
  --title "<title>" --description "<desc>" \
  --head <branch> --base main \
  --labels "<labels>" --milestone "<ms>"
extea pulls close -l <login> -r owner/repo <number>

Merging PRs

extea pulls merge can silently fail if the PR was already merged. Prefer the API:

extea api -l <login> -X POST "/repos/owner/repo/pulls/<number>/merge" \
  -f Do=merge \
  -f MergeMessageField="<commit message>"
# Do= options: merge | rebase | squash | manually-merged

Labels
extea labels list   -l <login> -r owner/repo
extea labels create -l <login> -r owner/repo --name "<name>" --color "#hexcolor" --description "<desc>"
extea labels delete -l <login> -r owner/repo <id>

Milestones
extea milestones list   -l <login> -r owner/repo
extea milestones list   -l <login> -r owner/repo --state all
extea milestones create -l <login> -r owner/repo --title "<title>" --description "<desc>" --deadline "<YYYY-MM-DD>"
extea milestones close  -l <login> -r owner/repo "<title>"   # close by title string

Releases
extea releases list   -l <login> -r owner/repo
extea releases create -l <login> -r owner/repo --tag <tag> --title "<title>" --note "<body>"


Tag must exist in the repo before creating the release:

git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0
extea releases create -l <login> -r owner/repo --tag v1.0.0 --title "v1.0.0" --note "..."

Comments
extea comment -l <login> -r owner/repo <issue-or-pr-number> "<comment text>"


PRs and issues share the same number sequence — commenting on a PR number works the same way.

Notifications
extea notifications -l <login> -r owner/repo


Always pass -r owner/repo — extea notifications requires a repo context even when run from a git directory.

API (raw endpoint access)

Use this for anything not covered by named commands (PR merges, wiki, etc.):

extea api -l <login> <endpoint>                            # GET
extea api -l <login> -X POST <endpoint> -f key=value       # POST with form fields
extea api -l <login> -X PATCH <endpoint> -f key=value      # PATCH
extea api -l <login> -X DELETE <endpoint>                  # DELETE


Pipe JSON output to python3 -c "import sys,json; d=json.load(sys.stdin); print(...)" for field extraction.

Project Boards

Board commands use web session auth (password stored in config or GITEA_PASSWORD env var) because Gitea has no REST API for project boards.

Projects (projects, project, p)
# List projects
extea projects ls -l <login> -r owner/repo
extea projects ls --state all -l <login> -r owner/repo    # open + closed

# View kanban board (shows all columns and their issues)
extea projects view <id> -l <login> -r owner/repo

# Create (templates: kanban, triage, none)
extea projects create -t "<title>" --template kanban -l <login> -r owner/repo

# Edit title
extea projects edit <id> -t "<new title>" -l <login> -r owner/repo

# Close / reopen / delete
extea projects close  <id> -l <login> -r owner/repo
extea projects open   <id> -l <login> -r owner/repo
extea projects delete <id> -l <login> -r owner/repo

# Assign issues to a project (can pass multiple -i flags)
extea projects assign <project-id> -i <issue-num> -i <issue-num> -l <login> -r owner/repo

# Remove issues from a project
extea projects unassign -i <issue-num> -l <login> -r owner/repo

# Move issues between columns
extea projects move <project-id> --column <col-id> -i <issue-num> -l <login> -r owner/repo

Columns (columns, column, col)
# List columns in a project
extea columns ls -p <project-id> -l <login> -r owner/repo

# Create a column (--color is optional)
extea columns create -p <project-id> -t "<title>" --color "#hexcolor" -l <login> -r owner/repo

# Edit a column title
extea columns edit -p <project-id> -c <col-id> -t "<new title>" -l <login> -r owner/repo

# Delete a column (issues move to default column)
extea columns delete -p <project-id> -c <col-id> -l <login> -r owner/repo

# Set default column (new issues land here)
extea columns default -p <project-id> -c <col-id> -l <login> -r owner/repo

# Reorder columns (pass all column IDs in desired order)
extea columns move -p <project-id> --order <id1>,<id2>,<id3> -l <login> -r owner/repo

JSON Output

Add --output json / -o json to projects list, projects view, or columns list for machine-readable output. Useful for extracting IDs:

extea projects ls -l <login> -r owner/repo -o json | python3 -c "import sys,json; [print(p['id'], p['title']) for p in json.load(sys.stdin)]"
extea columns ls -p <id> -l <login> -r owner/repo -o json | python3 -c "import sys,json; [print(c['id'], c['title']) for c in json.load(sys.stdin)]"

Wiki

The wiki is a separate git repo at http://<host>/owner/repo.wiki.git.

The wiki repo does not exist until the first page is created. Initialize it via the API before attempting to clone:

# Initialize wiki with a Home page (required before git clone works)
extea api -l <login> -X POST "/repos/owner/repo/wiki/new" \
  -f title="Home" \
  -f content_base64="$(echo '# Home page content' | base64)" \
  -f message="init: create wiki home page"

# Create additional pages
extea api -l <login> -X POST "/repos/owner/repo/wiki/new" \
  -f title="Page Title" \
  -f content_base64="$(printf '%s' "$CONTENT" | base64)" \
  -f message="docs: add page"

# List all wiki pages
extea api -l <login> "/repos/owner/repo/wiki/pages"


Always work with the wiki in /tmp to avoid polluting the current working directory.

# Clone wiki (only works after at least one page has been created)
if [ ! -d /tmp/repo-wiki ]; then
  git clone "http://user:${TOKEN}@<host>/owner/repo.wiki.git" /tmp/repo-wiki
fi

cd /tmp/repo-wiki
git config user.name "yourname"
git config user.email "you@host"   # Must match the Gitea account's registered email or history links won't be clickable
                                    # Check with: extea api -l <login> "/users/<username>" | python3 -c "import sys,json; print(json.load(sys.stdin)['email'])"

# Pages are markdown files: Home.md, Page-Name.md (hyphens for spaces)
# Edit files, then:
git add -A && git commit -m "Update wiki"
git push

Typical Workflow
# 1. Create repo and push code
extea repos create --name myrepo --description "..." -l mylogin
cd /tmp/myrepo && git init && git remote add origin "http://user:TOKEN@host/user/myrepo.git"
git push -u origin main

# 2. Set up labels and milestones
extea labels create -l mylogin -r user/myrepo --name "bug" --color "#d73a4a"
extea milestones create -l mylogin -r user/myrepo --title "v1.0" --deadline "2026-06-01"

# 3. File issues
extea issues create -l mylogin -r user/myrepo --title "Fix the thing" --labels "bug" --milestone "v1.0"

# 4. Branch, commit, PR
git checkout -b fix/the-thing && git commit -m "fix: the thing" && git push origin fix/the-thing
extea pulls create -l mylogin -r user/myrepo --title "fix: the thing" --head fix/the-thing --base main

# 5. Comment, merge
extea comment -l mylogin -r user/myrepo 1 "LGTM"
extea api -l mylogin -X POST "/repos/user/myrepo/pulls/1/merge" -f Do=merge -f MergeMessageField="fix: the thing"

# 6. Project board
extea projects create -t "Sprint 1" --template kanban -l mylogin -r user/myrepo
PROJECT_ID=$(extea projects ls -l mylogin -r user/myrepo -o json | python3 -c "import sys,json; print(json.load(sys.stdin)[0]['id'])")
extea projects assign $PROJECT_ID -i 1 -l mylogin -r user/myrepo
# Get column IDs, then move issues
extea columns ls -p $PROJECT_ID -l mylogin -r user/myrepo -o json
extea projects move $PROJECT_ID --column <col-id> -i 1 -l mylogin -r user/myrepo

# 7. Release
git tag -a v1.0.0 -m "Release v1.0.0" && git push origin v1.0.0
extea releases create -l mylogin -r user/myrepo --tag v1.0.0 --title "v1.0.0" --note "..."

# 8. Wiki
extea api -l mylogin -X POST "/repos/user/myrepo/wiki/new" \
  -f title="Home" -f content_base64="$(echo '# Docs' | base64)" -f message="init wiki"
git clone "http://user:TOKEN@host/user/myrepo.wiki.git" /tmp/myrepo-wiki

PR Reviews with Inline Line Comments

extea pulls review is interactive-only. Use curl with the API for scriptable inline comments:

# Get the head commit SHA first
HEAD_SHA=$(extea api -l <login> "/repos/owner/repo/pulls/<number>" \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['head']['sha'])")

# Post a review with inline comments
curl -s -X POST "http://<host>/api/v1/repos/owner/repo/pulls/<number>/reviews" \
  -H "Authorization: token $TOKEN" \
  -H "Content-Type: application/json" \
  -d "{
    \"commit_id\": \"$HEAD_SHA\",
    \"event\": \"COMMENT\",
    \"body\": \"Overall review comment\",
    \"comments\": [
      { \"path\": \"main.py\", \"new_position\": 4,  \"body\": \"Comment on new file line 4\" },
      { \"path\": \"main.py\", \"old_position\": 3, \"body\": \"Comment on a deleted line\" }
    ]
  }"

new_position — line number in the new version of the file (1-indexed)
old_position — line number in the old version (for commenting on deleted lines)
event options: COMMENT | APPROVE | REQUEST_CHANGES (can't use REQUEST_CHANGES on your own PR)
extea api -f doesn't support nested JSON arrays — always use curl for review creation
The original_position field in the response is always 0 (Gitea bug); check diff_hunk in the response to confirm anchoring worked

Fetch a review's inline comments:

extea api -l <login> "/repos/owner/repo/pulls/<number>/reviews/<review-id>/comments"


Other review actions:

extea pulls approve -l <login> -r owner/repo <number>           # approve
extea pulls reject  -l <login> -r owner/repo <number>           # request changes (not your own PR)
extea api -l <login> "/repos/owner/repo/pulls/<number>/reviews" # list all reviews

Images
Issue / PR attachments

Upload a file and embed the returned URL in markdown:

# Upload attachment to an issue
curl -s -X POST "http://<host>/api/v1/repos/owner/repo/issues/<number>/assets" \
  -H "Authorization: token $TOKEN" \
  -F "attachment=@/path/to/image.jpg" \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['browser_download_url'])"
# Returns: http://<host>/attachments/<uuid>

# Embed in a comment
extea comment -l <login> -r owner/repo <number> "![alt](http://<host>/attachments/<uuid>)"

Wiki images

Commit image files directly into the wiki git repo alongside the .md files. Reference them with relative paths in markdown — Gitea resolves them automatically.

cd /tmp/repo-wiki
cp /path/to/image.jpg ./image.jpg
echo '![caption](image.jpg)' >> Page.md
git add image.jpg Page.md
git commit -m "docs: add image"
git push


Images are served at:

http://<host>/owner/repo/wiki/raw/branch/master/<filename>


They live as flat files in the wiki repo — same level as .md files — and are not listed as wiki pages. Link to the page that contains them from somewhere discoverable (e.g. Home.md).

Linking to Commits and File Lines

These are markdown links you embed in issue/PR bodies and comments — not CLI commands.

Commit reference — paste a short or full SHA; Gitea auto-links it:

cdc9af8
owner/repo@cdc9af8    ← cross-repo form


File + line (branch ref) — drifts as the file changes:

http://<host>/owner/repo/src/branch/main/file.py#L10
http://<host>/owner/repo/src/branch/main/file.py#L10-L15   ← line range


File + line (commit permalink) — stable forever, won't drift after refactors:

http://<host>/owner/repo/src/commit/<sha>/file.py#L10
http://<host>/owner/repo/src/commit/<sha>/file.py#L10-L15


Commit diff page:

http://<host>/owner/repo/commit/<sha>


Prefer the commit permalink form (/src/commit/<sha>/) in bug reports — branch-based links become wrong after file moves or refactors.

Notes
extea auto-detects the repo from the git remote in $PWD, but always pass -l <login> and -r owner/repo explicitly to avoid ambiguity.
Board commands require a password (stored in config via extea login add, or GITEA_PASSWORD env var). Standard tea commands use API tokens only.
PRs and issues share the same number sequence in a repo — a PR opened as #6 can be commented on with extea comment ... 6.
extea milestones close takes the milestone title as a string, not an ID.
extea pulls merge may silently fail on already-merged PRs — always use the API form for reliability.
Weekly Installs
48
Repository
halfwhey/extea
First Seen
Apr 4, 2026
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykFail