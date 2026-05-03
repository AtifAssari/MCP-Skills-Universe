---
rating: ⭐⭐
title: browserbase-cli
url: https://skills.sh/browserbase/skills/browserbase-cli
---

# browserbase-cli

skills/browserbase/skills/browserbase-cli
browserbase-cli
Installation
$ npx skills add https://github.com/browserbase/skills --skill browserbase-cli
SKILL.md
Browserbase CLI

Use the official bb CLI for Browserbase platform operations, Functions workflows, and Fetch API calls.

Setup check

Before using the CLI, verify it is installed:

which bb || npm install -g @browserbasehq/cli
bb --help


For authenticated commands, set the API key:

export BROWSERBASE_API_KEY="your_api_key"


If using bb functions dev or bb functions publish, also set:

export BROWSERBASE_PROJECT_ID="your_project_id"

When to use this skill

Use this skill when the user wants to:

run Browserbase commands through bb
scaffold, develop, publish, or invoke Browserbase Functions
inspect or manage Browserbase sessions, projects, contexts, or extensions
fetch a page through Browserbase without opening a browser session
search the web through Browserbase without opening a browser session
browse or scaffold starter templates with bb templates
When not to use this skill
For interactive browsing, page inspection, screenshots, clicking, typing, or login flows, prefer the browser skill.
For simple HTTP content retrieval where the user does not care about using the CLI specifically, the dedicated fetch skill is often a better fit.
Use bb browse ... only when the user explicitly wants the CLI wrapper or is already working in a bb-centric workflow.
Command selection
bb functions for local dev, packaging, publishing, and invocation
bb sessions, bb projects, bb contexts, bb extensions for Browserbase platform resources
bb fetch <url> for Fetch API requests
bb search "<query>" for Search API requests
bb templates to browse and scaffold starter templates
bb browse ... to forward to the standalone browse binary (requires @browserbasehq/browse-cli)
bb skills install to install Browserbase agent skills for Claude Code

For bb browse, the standalone browse CLI behavior is the source of truth: bb browse env local uses a clean isolated local browser by default, and bb browse env local --auto-connect opts into reusing an existing local Chrome session.

Common workflows
Functions
bb functions init my-function
cd my-function
bb functions dev index.ts
bb functions publish index.ts
bb functions invoke <function_id> --params '{"url":"https://example.com"}'


Use bb functions invoke --check-status <invocation_id> to poll an existing invocation instead of creating a new one.

Platform APIs
bb projects list
bb sessions create --proxies --advanced-stealth --region us-east-1
bb sessions create --solve-captchas --context-id ctx_abc --persist
bb sessions get <session_id>
bb sessions downloads get <session_id> --output session-artifacts.zip
bb contexts create --body '{"region":"us-west-2"}'
bb extensions upload ./my-extension.zip

Fetch API
bb fetch https://example.com
bb fetch https://example.com --allow-redirects --output page.html

Search API
bb search "browser automation"
bb search "web scraping" --num-results 5
bb search "AI agents" --output results.json

Templates
bb templates list
bb templates list --language python
bb templates clone form-filling --language typescript
bb templates clone amazon-product-scraping --language python ./my-scraper

Best practices
Prefer bb --help and subgroup --help before guessing flags.
Use dash-case flags exactly as shown in CLI help.
Use --output <file> on bb fetch and bb search to save results to a file.
Use environment variables for auth unless the user explicitly wants one-off overrides.
Pass structured request bodies with JSON strings in --body or --params.
Remember that bb functions ... uses --api-url, while platform API commands use --base-url.
If bb browse fails because browse is missing, either install @browserbasehq/browse-cli or switch to the browser skill.
Troubleshooting
Missing API key: set BROWSERBASE_API_KEY or pass --api-key
Missing project ID on bb functions dev or bb functions publish: set BROWSERBASE_PROJECT_ID or pass --project-id
Unknown flag: rerun the relevant command with --help and use the exact dash-case form
bb browse install error: run npm install -g @browserbasehq/browse-cli

For command-by-command reference and more examples, see REFERENCE.md.

Weekly Installs
789
Repository
browserbase/skills
GitHub Stars
1.5K
First Seen
Mar 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn