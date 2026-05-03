---
title: git-hunk
url: https://skills.sh/wkentaro/git-hunk/git-hunk
---

# git-hunk

skills/wkentaro/git-hunk/git-hunk
git-hunk
Installation
$ npx skills add https://github.com/wkentaro/git-hunk --skill git-hunk
SKILL.md
/git-hunk - split changes into focused commits

Requires: uv tool install git-hunk (or pip install git-hunk)

Workflow
git-hunk list — see all hunks (file, id, +/- stats). No diffs.
git-hunk show [<id>...] when headers aren't clear enough (no args shows all).
Plan commits before staging. For each planned commit, list the hunk IDs (and -l line ranges for partial hunks). A single hunk may need to be split across commits. Ask the user if grouping is ambiguous.
Stage and commit each group:
git-hunk stage <id1> <id2> ...
git commit -m "<type>: <description>"

git-hunk list again to check nothing got left behind.
Partial hunks

Line selection (-l) works with stage, unstage, and discard (requires single id):

Include lines: git-hunk stage <id> -l 3,5-7
Exclude lines: git-hunk stage <id> -l ^3,^5-7
Fixing mistakes
git-hunk unstage <id1> <id2> ... — move staged hunks back to working tree.
git-hunk unstage <id> -l 3,5-7 — partially unstage specific lines.
git-hunk discard <id1> <id2> ... — permanently discard unstaged hunks (restore from HEAD).
git-hunk discard <id> -l 3,5-7 — partially discard specific lines.
Example git-hunk list output
unstaged:
labelme/app.py
  c43213b  @@ -78,6 +78,7 @@ _AI_CREATE_MODES  +1
  4da0d77  @@ -1364,6 +1365,19 @@ class MainWindow  +13
labelme/translate/de_DE.qm
  7a3befc  Binary file

Notes
IDs are content-based hashes, stable across partial staging, and support prefix matching
git-hunk list [<file>...] — filter hunks by file path
--staged / --unstaged to filter list and show (both search staged+unstaged by default)
--json exists but plain output is usually enough
One logical change per commit, conventional commit messages
Weekly Installs
44
Repository
wkentaro/git-hunk
GitHub Stars
3
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass