---
rating: ⭐⭐
title: pachca-search
url: https://skills.sh/pachca/openapi/pachca-search
---

# pachca-search

skills/pachca/openapi/pachca-search
pachca-search
Installation
$ npx skills add https://github.com/pachca/openapi --skill pachca-search
SKILL.md
pachca-search
Quick start

Ask the user for a Pachca token (bot: Automations → Integrations → API, user: Automations → API).

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

Workflows
Найти сообщение по тексту
Полнотекстовый поиск по сообщениям:
pachca search list-messages --query="текст"


limit (до 200), cursor. Фильтры: chat_ids[], user_ids[], active, created_from/created_to

Поиск по всем доступным чатам. root_chat_id в ответе — корневой чат для тредов.

Найти чат по названию
Полнотекстовый поиск по чатам:
pachca search list-chats --query="название"


limit (до 100), cursor. Фильтры: active, chat_subtype, personal, created_from/created_to

Найти сотрудника по имени
Полнотекстовый поиск по сотрудникам:
pachca search list-users --query="имя"


sort=alphabetical для алфавитного порядка, sort=by_score (по умолчанию). Фильтры: company_roles[], created_from/created_to

Поиск по имени, email, должности и другим полям. Поддерживает сортировку по релевантности.

Limitations
Rate limit: ~50 req/sec. On 429 — wait and retry.
limit: max — 100 (GET /search/chats), 200 (GET /search/messages), 200 (GET /search/users)
Pagination: cursor-based (limit + cursor)
Endpoints
Method	Path	Description
GET	/search/chats	Поиск чатов
GET	/search/messages	Поиск сообщений
GET	/search/users	Поиск сотрудников

If unsure how to complete a task, read the corresponding file from references/.

Weekly Installs
50
Repository
pachca/openapi
GitHub Stars
5
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail