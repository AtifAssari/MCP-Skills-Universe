---
title: hugo-sveltia-cms
url: https://skills.sh/baphomet480/claude-skills/hugo-sveltia-cms
---

# hugo-sveltia-cms

skills/baphomet480/claude-skills/hugo-sveltia-cms
hugo-sveltia-cms
Installation
$ npx skills add https://github.com/baphomet480/claude-skills --skill hugo-sveltia-cms
SKILL.md
Hugo + Sveltia CMS Skill

Two primary workflows:

Bootstrap: New Hugo site with Sveltia CMS + Basecoat UI, deployed to Cloudflare Pages
Convert: Migrate from TinaCMS, Decap/Netlify CMS, WordPress, Jekyll, Eleventy, or other platforms to Hugo + Sveltia CMS
Why This Stack
Hugo — Fastest SSG, single binary, Go templates
Sveltia CMS — Git-based headless CMS, drop-in Decap/Netlify CMS replacement with better UX and i18n. Beta, v1.0 early 2026. Same config.yml format as Decap
Basecoat — shadcn/ui components without React. Tailwind CSS utility classes (btn, card, input), minimal JS, dark mode, themeable
Cloudflare Pages — Primary deploy target. Free tier, fast CDN, Workers for OAuth
GitHub — Only supported Git backend
Critical Knowledge
YAML front matter only. Sveltia CMS has bugs with TOML (+++). Always use YAML (---) and set format: yaml on every collection.
Use hugo.yaml not hugo.toml for config consistency.
Admin files in static/admin/. Hugo copies static/ to build root.
Media paths. media_folder: "static/images/uploads" (repo) → public_folder: "/images/uploads" (URL). Hugo strips static/.
GitHub OAuth required. Deploy sveltia-cms-auth as a Cloudflare Worker. Netlify git-gateway NOT supported.
Always set extension: "md" and format: "yaml" on every folder collection.
Schema line at top of config.yml: # yaml-language-server: $schema=https://unpkg.com/@sveltia/cms/schema/sveltia-cms.json
Workflow: Bootstrap
Step 1: Gather Requirements

Ask:

Site purpose: Consulting/services, medical practice, blog, portfolio, docs?
Content types: What content will they manage?
Basecoat approach: Full Tailwind pipeline (recommended) or CDN-only prototype?
Custom domain: For CF Pages + OAuth setup
Step 2: Scaffold Hugo + Basecoat
hugo new site <site-name> --format yaml
cd <site-name>


Read references/hugo-sveltia-setup.md § Basecoat Integration for setup details.

Production (recommended): npm init -y && npm install -D tailwindcss @tailwindcss/cli basecoat-css, create assets/css/main.css with @import "tailwindcss"; @import "basecoat-css";, wire via Hugo's css.TailwindCSS pipe.

CDN (quick start): Add CDN links to baseof.html <head>.

Step 3: Create Admin Interface

Create static/admin/index.html and static/admin/config.yml using templates/. Build collections from the domain-specific patterns in the reference file.

Step 4: Build Layouts with Basecoat Components

Create Hugo partials wrapping Basecoat classes: partials/components/card.html, button.html, badge.html, alert.html, nav.html. These accept parameters via Hugo dict and emit styled HTML.

Step 5: Create Archetypes + Seed Content

One archetype per content type in archetypes/.

Step 6: Deploy to Cloudflare Pages
Register GitHub OAuth App → get Client ID + Secret
Deploy sveltia-cms-auth Cloudflare Worker
Connect repo to CF Pages, set HUGO_VERSION env var
Build command: hugo --minify, output: public
The bootstrap creates .github/workflows/deploy.yml automatically — set CLOUDFLARE_API_TOKEN, CLOUDFLARE_ACCOUNT_ID as GitHub Secrets and PAGES_PROJECT_NAME as a GitHub Variable
Step 7: Test Locally

Sveltia CMS detects localhost and uses File System Access API (Chromium) — no OAuth needed locally. Run hugo server, visit /admin/.

Workflow: Convert
From TinaCMS

TinaCMS uses GraphQL API + tina/config.ts schema + TinaCloud auth. Fundamentally different architecture.

Field type mapping:

TinaCMS type	Sveltia widget	Notes
string	string	
string + list: true	list	
datetime	datetime	
boolean	boolean	
image	image	
rich-text	markdown	Shortcode templates won't carry over
object	object	Map subfields recursively
reference	relation	Set collection, search_fields, value_field
number	number	Set value_type: int or float

Config mapping: tina/config.ts collections[].path → config.yml collections[].folder

Steps:

Read tina/config.{ts,js}, map each collection's fields using table above
Content files (Markdown + YAML front matter) stay as-is — Hugo reads them directly
Delete tina/ directory, remove tinacms from package.json, remove Tina build commands
Create static/admin/ with Sveltia CMS files
Map Tina media config (mediaRoot/publicFolder) → Sveltia media_folder/public_folder
Document shortcodes used in content (no CMS-side visual editing for these)
Deploy via CF Pages + GitHub OAuth

Key win: No more TinaCloud dependency, no GraphQL build step, no tina/__generated__/.

From Decap CMS / Netlify CMS

Drop-in replacement:

Replace script tag: <script src="https://unpkg.com/@sveltia/cms/dist/sveltia-cms.js"></script>
Existing config.yml works as-is
Replace git-gateway with GitHub OAuth + CF Worker
Test all collections
From WordPress
Export via wordpress-export-to-markdown or hugo import jekyll after Jekyll export
Clean front matter (strip wp_id, guid)
Map taxonomies → Hugo taxonomies
Download media → static/images/
Build collections matching cleaned structure
From Jekyll
hugo import jekyll <jekyll-root> <hugo-root> (built-in)
Review front matter, add Sveltia CMS per standard workflow
From Eleventy / Other SSGs
Copy Markdown + YAML front matter files into content/
Adjust for Hugo conventions (date format, draft boolean)
Rebuild templates in Hugo, add Sveltia CMS
Domain-Specific Collections

Read references/hugo-sveltia-setup.md § Domain Collection Patterns for ready-made configs:

Consulting / Services — Services, case studies, testimonials, team members
Medical Practice — Providers, locations, services/specialties, conditions, patient resources
Content / Blog — Posts, pages, authors, newsletter, categories

Mix and match. Each includes full field definitions.

File Checklist
 hugo.yaml
 package.json + assets/css/main.css (Basecoat/Tailwind, if npm path)
 static/admin/index.html + static/admin/config.yml
 archetypes/ — one per content type
 content/ — seed or converted content
 layouts/ — Basecoat-styled templates + component partials
 .github/workflows/deploy.yml — CI/CD for Cloudflare Pages
 .gitignore
Reference Files
references/hugo-sveltia-setup.md — Full config reference, domain collections, Basecoat setup, widgets, auth, CF Pages deploy, gotchas, i18n
templates/admin-index.html — Admin page template
templates/config.yml — Annotated CMS config starter
templates/deploy.yml — GitHub Actions workflow for Cloudflare Pages CI/CD
scripts/bootstrap-hugo-sveltia.sh — One-command scaffolding
scripts/convert-toml-to-yaml.py — Batch front matter conversion
Weekly Installs
14
Repository
baphomet480/cla…e-skills
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn