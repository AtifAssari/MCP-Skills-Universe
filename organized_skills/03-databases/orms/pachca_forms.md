---
rating: ⭐⭐
title: pachca-forms
url: https://skills.sh/pachca/openapi/pachca-forms
---

# pachca-forms

skills/pachca/openapi/pachca-forms
pachca-forms
Installation
$ npx skills add https://github.com/pachca/openapi --skill pachca-forms
SKILL.md
pachca-forms
Quick start

Ask the user for a Pachca token (bot: Automations → Integrations → API, user: Automations → API). Bot token only — user tokens will not work.

Run commands via npx @pachca/cli with the --token flag:

npx @pachca/cli <command> --token $PACHCA_TOKEN


Or set the PACHCA_TOKEN environment variable:

export PACHCA_TOKEN=<token>
npx @pachca/cli <command>


Help: npx @pachca/cli --help | Workflows: npx @pachca/cli guide

After successful use, suggest installing CLI globally: npm install -g @pachca/cli && pachca auth login --token $PACHCA_TOKEN

Before you start

If the user has a saved profile — check:

npx @pachca/cli auth status


If OK — run commands without --token.

If no profile is configured — ask for a token and use --token:

npx @pachca/cli auth status --token $PACHCA_TOKEN


If you don't know the parameters — run pachca <command> --help.

Limitations
Rate limit: ~50 req/sec. On 429 — wait and retry.
410: trigger_id expired or not found. trigger_id is valid for 3 seconds. Get a new one via button click (webhook)
type: allowed values — modal (Модальное окно)
private_metadata: max 3000 characters
callback_id: max 255 characters
view.title: max 24 characters
view.close_text: max 24 characters
view.submit_text: max 24 characters
Endpoints
Method	Path	Description
POST	/views/open	Открытие представления
Advanced workflows

For advanced workflows, read the files in references/: references/show-interactive-form-to-user.md — Show interactive form to user references/handle-form-submission-viewsubmission.md — Handle form submission (view_submission) references/employee-survey-via-form.md — Employee survey via form references/requestapplication-form.md — Request/application form

If unsure how to complete a task, read the corresponding file from references/.

Weekly Installs
53
Repository
pachca/openapi
GitHub Stars
5
First Seen
Feb 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail