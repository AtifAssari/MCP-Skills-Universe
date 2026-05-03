---
rating: ⭐⭐⭐
title: deploy
url: https://skills.sh/pedrohcgs/claude-code-my-workflow/deploy
---

# deploy

skills/pedrohcgs/claude-code-my-workflow/deploy
deploy
Installation
$ npx skills add https://github.com/pedrohcgs/claude-code-my-workflow --skill deploy
SKILL.md
Deploy Slides to GitHub Pages

Render Quarto slides and sync all files to docs/ for GitHub Pages deployment.

Steps

Run the sync script:

If $ARGUMENTS is provided (e.g., "Lecture4"): ./scripts/sync_to_docs.sh $ARGUMENTS
If no argument: ./scripts/sync_to_docs.sh (syncs all lectures)

Verify deployment:

Check that HTML files exist in docs/slides/
Check that _files/ directories were copied (RevealJS assets)
Check that docs/Figures/ was synced from Figures/

Verify interactive charts (if applicable):

Grep rendered HTML for interactive widget count
Confirm count matches expected

Verify TikZ SVGs (if applicable):

Check that all referenced SVG files exist in docs/Figures/LectureN/

Open in browser for visual verification:

open docs/slides/LectureX_Name.html # macOS
# xdg-open docs/slides/LectureX_Name.html # Linux
Confirm slides render, images display, navigation works

Report results to the user

What the sync script does:
Renders all .qmd files in Quarto/ (skips *_backup* files)
Copies HTML and _files/ directories to docs/slides/
Copies Beamer PDFs from Slides/ to docs/slides/
Syncs Figures/ to docs/Figures/ using rsync
Weekly Installs
15
Repository
pedrohcgs/claud…workflow
GitHub Stars
1.0K
First Seen
Feb 19, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass