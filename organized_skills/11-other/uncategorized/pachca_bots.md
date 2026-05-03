---
rating: ⭐⭐
title: pachca-bots
url: https://skills.sh/pachca/openapi/pachca-bots
---

# pachca-bots

skills/pachca/openapi/pachca-bots
pachca-bots
Installation
$ npx skills add https://github.com/pachca/openapi --skill pachca-bots
SKILL.md
pachca-bots
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
Настроить бота с исходящим вебхуком

Создай бота в интерфейсе Пачки: Автоматизации → Интеграции → Webhook

Получи access_token бота во вкладке «API» настроек бота

Укажи Webhook URL для получения событий

Бот создаётся через UI, не через API. Единственный эндпоинт для ботов — PUT /bots/{id} (обновление webhook URL). API используется для отправки сообщений от имени бота.

Обновить Webhook URL бота
Обнови webhook URL бота:
pachca bots update <bot_id> --webhook='{"outgoing_url":"https://example.com/webhook"}'


id бота (его user_id) можно узнать во вкладке «API» настроек бота

Обновлять настройки может только тот, кому разрешено редактирование бота.

Периодический дайджест/отчёт

По расписанию (cron/scheduler): собери данные из своей системы

Сформируй текст сообщения с нужными метриками или сводкой

Отправь сообщение в канал:

pachca messages create --entity-id=<chat_id> --content="Дайджест за сегодня: ..."


Нет встроенного планировщика — используй cron, celery, sidekiq и т.п. на своей стороне.

Limitations
Rate limit: ~50 req/sec. On 429 — wait and retry.
limit: max 50
Pagination: cursor-based (limit + cursor)
Endpoints
Method	Path	Description
PUT	/bots/{id}	Редактирование бота
POST	/messages/{id}/link_previews	Unfurl (разворачивание ссылок)
GET	/webhooks/events	История событий
DELETE	/webhooks/events/{id}	Удаление события
Advanced workflows

For advanced workflows, read the files in references/: references/handle-incoming-webhook-event.md — Handle incoming webhook event references/link-unfurling.md — Link unfurling references/handle-button-click-callback.md — Handle button click (callback) references/monitoring-and-alerts.md — Monitoring and alerts references/process-events-via-history-polling.md — Process events via history (polling)

references/webhook-events.md — Webhook event types

If unsure how to complete a task, read the corresponding file from references/.

Weekly Installs
57
Repository
pachca/openapi
GitHub Stars
5
First Seen
Feb 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykFail