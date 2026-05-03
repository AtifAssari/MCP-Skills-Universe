---
title: mkdocs-site-bootstrap
url: https://skills.sh/daviddwlee84/agent-skills/mkdocs-site-bootstrap
---

# mkdocs-site-bootstrap

skills/daviddwlee84/agent-skills/mkdocs-site-bootstrap
mkdocs-site-bootstrap
Installation
$ npx skills add https://github.com/daviddwlee84/agent-skills --skill mkdocs-site-bootstrap
SKILL.md
mkdocs-site-bootstrap

Bootstrap and (optionally) deploy a MkDocs Material documentation site for a repository, then keep helping the user add pages over time.

This skill is consent-gated. It records the user's preferences in .skills/preferences.yaml and never repeats destructive actions without asking. If the user changes their mind, scripts/check-preferences.sh --reset mkdocs_site_bootstrap clears the recorded decision so the next invocation starts fresh.

When to trigger
User asks to "set up docs", "create a docs site", "add a documentation site", "publish docs to GitHub Pages"
User has loose markdown notes / a docs/ directory and wants it browsable
User wants the same docs stack as the daviddwlee84/agent-skills repo applied to a new project
User says they want an LLM-friendly docs site (llms.txt, copy-to-LLM)
When NOT to trigger
User just wants to write a single doc file → don't scaffold a whole site
User explicitly opted out (preferences.yaml says enabled: false) → defer unless the user is now reversing that decision
User wants to evaluate or benchmark a skill → use skill-creator
User wants to author a new agent skill → use skill-author
Workflow
1. Read preferences first

Before doing anything, check whether this repo already has a recorded decision:

bash skills/local/mkdocs-site-bootstrap/scripts/check-preferences.sh \
  --get mkdocs_site_bootstrap


Possible states:

State	Meaning	What to do
File doesn't exist or key missing	Never asked	Proceed to step 2 (interview)
enabled: true, pages_deployed: true	Site is live	Skip to step 6 (ongoing helpers)
enabled: true, pages_deployed: false	Bootstrapped but not deployed	Skip to step 5 (deploy)
enabled: false	User opted out	Confirm they want to reverse that, then --reset and re-run
2. Interview (only if no recorded decision)

Ask the user explicitly:

"Do you want a MkDocs Material documentation site for this project? (yes / no / I'll think about it)"
If yes: "Should it auto-deploy to GitHub Pages on push to main? (yes / no — I'll deploy manually)"

Record both answers immediately so an interrupted session doesn't lose them:

bash skills/local/mkdocs-site-bootstrap/scripts/check-preferences.sh \
  --set mkdocs_site_bootstrap.enabled=true \
  --set mkdocs_site_bootstrap.stack=mkdocs-material \
  --set mkdocs_site_bootstrap.auto_deploy=true


If the user said no, record enabled: false and stop. Don't pester on future invocations.

3. Detect existing docs (consent gate)

Before scaffolding, scan the target repo. Read references/existing-docs-handling.md for the full decision tree, but the short version:

If mkdocs.yml already exists → report "looks like an mkdocs site already exists at ; not overwriting" and stop.
If docs/ exists and is non-empty → list the files, ask the user one of: (a) skip — leave my docs alone, just create mkdocs.yml pointing at them; (b) wrap — create mkdocs.yml with my files included as-is in the nav; (c) manual — let me reorganize first, then re-run.
If neither exists → safe to scaffold from scratch.

Record the decision under mkdocs_site_bootstrap.existing_docs_decision.

4. Scaffold

Run init-docs-site.sh. It writes (or refuses to overwrite) mkdocs.yml, pyproject.toml (with [project.optional-dependencies] docs = […]), the docs/ skeleton, .github/workflows/docs.yml, and stub assets for copy-to-llm.

bash skills/local/mkdocs-site-bootstrap/scripts/init-docs-site.sh \
  --site-name "My Project" \
  --repo-slug owner/repo \
  --site-url https://owner.github.io/repo/


Use --dry-run first to preview. The script always preserves any existing files unless --force is passed.

After scaffolding, run a local strict build to catch obvious issues:

uv sync --extra docs
uv run mkdocs build --strict

5. Enable Pages and trigger first deploy (consent gate)

This calls the GitHub API (gh api -X POST .../pages -f build_type=workflow) and then triggers the workflow. Always confirm with the user first — say exactly which API call you're about to make and which repo it'll affect. Only proceed on explicit yes.

bash skills/local/mkdocs-site-bootstrap/scripts/enable-pages.sh \
  --repo owner/repo


Flags:

--dry-run — print the gh calls without running them
--no-trigger — enable Pages but don't run the workflow yet

After success, set pages_deployed=true and pages_enabled_at=$(date +%F) in preferences.

6. Ongoing: add docs pages

For each new doc the user wants, use the helper instead of hand-editing mkdocs.yml:

bash skills/local/mkdocs-site-bootstrap/scripts/add-docs-page.sh \
  --section workflows \
  --title "My new workflow" \
  --slug my-new-workflow


It creates docs/<section>/<slug>.md from the page template and inserts a nav entry into mkdocs.yml under the matching section heading. Idempotent — re-running with the same slug is a no-op.

Available scripts
scripts/check-preferences.sh — Read, set, or reset .skills/preferences.yaml. Always-safe to run.
Flags: --get KEY, --set KEY=VALUE (repeatable), --reset NAMESPACE, --list, --dry-run, --json.
scripts/init-docs-site.sh — Scaffold the site files.
Flags: --site-name, --repo-slug, --site-url, --existing skip|wrap, --no-workflow, --dry-run, --force.
scripts/enable-pages.sh — Enable Pages and trigger first deploy via gh api. Requires gh auth status to pass first.
Flags: --repo OWNER/REPO, --no-trigger, --dry-run.
scripts/add-docs-page.sh — Create a new page and insert it into mkdocs.yml's nav.
Flags: --section, --title, --slug, --template PATH, --dry-run, --force.
Reference files
references/preferences-schema.md — Schema for .skills/preferences.yaml and conventions for cross-skill use. Read this whenever you're touching a preferences key for the first time.
references/existing-docs-handling.md — Full decision tree for handling user's pre-existing docs/ content without surprises. Read this before step 3 of every fresh bootstrap.
references/docs-stack-recipe.md — Verbatim stack recipe (mkdocs.yml, pyproject.toml, workflow, linking rules). Useful when the user asks "what exactly is this stack?" or wants to apply pieces manually.
Bundled assets

Templates the scripts copy from. Edit them here, not in the user's repo.

assets/mkdocs.yml.template — Material theme + llmstxt + copy-to-llm plugins + pymdownx.snippets, parameterized with {{SITE_NAME}}, {{REPO_SLUG}}, {{SITE_URL}}.
assets/pyproject.toml.template — Minimal [project] block + the docs optional-deps group.
assets/docs-workflow.yml.template — .github/workflows/docs.yml with paths filter, uv setup, strict build, Pages deploy.
assets/docs-skeleton/ — index.md, getting-started.md, _snippets/ examples, assets/copy-to-llm/ JS+CSS files copied from this repo.
assets/page.md.template — Used by add-docs-page.sh.
Gotchas
MkDocs strict mode rejects relative .md links pointing outside docs/. Inside docs/ → relative is fine. Outside docs/ for .md files (e.g., linking to repo TODO.md) → use absolute GitHub URL. Outside docs/ for directories or non-.md (backlog/, pyproject.toml) → relative is downgraded to INFO and tolerated. Templates already do this right; don't "fix" the absolute URLs.
pymdownx.snippets requires _snippets/ in not_in_nav: or strict mode complains about pages-not-in-nav. Template handles it.
gh api -X POST .../pages is idempotent for build_type=workflow but errors on 404 Not Found if the repo isn't pushed to GitHub yet. Check gh repo view succeeds before running enable-pages.sh.
The Pages deploy workflow needs permissions: pages: write, id-token: write at the workflow level. Template has it; if you copy pieces into an existing workflow, don't lose this.
copy-to-llm plugin's repo_url is the SITE URL, not the GitHub URL. Counter-intuitive name.
Don't auto-migrate existing user docs. Always ask. Migrating someone's hand-curated docs/ into a new structure is a high-trust action that should be the user's explicit decision, not the agent's default.
.skills/preferences.yaml is per-repo, not global. Don't write it to ~/.skills/ or ~/.config/. Each repo has its own decisions.
Updating an existing site (not bootstrapping)

If mkdocs.yml already exists, this skill mostly defers — only add-docs-page.sh and check-preferences.sh are useful. Don't try to "upgrade" the user's mkdocs.yml without an explicit ask; their config may have customizations the templates don't know about.

Weekly Installs
9
Repository
daviddwlee84/ag…t-skills
First Seen
4 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn