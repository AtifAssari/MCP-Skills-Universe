---
title: pachca-security
url: https://skills.sh/pachca/openapi/pachca-security
---

# pachca-security

skills/pachca/openapi/pachca-security
pachca-security
Installation
$ npx skills add https://github.com/pachca/openapi --skill pachca-security
SKILL.md
pachca-security
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
Получить журнал аудита событий
Получи журнал аудита:
pachca security list --start-time=<ISO-8601> --end-time=<ISO-8601>


start_time и end_time обязательны (ISO-8601, UTC+0). Фильтры: event_key, actor_id, actor_type, entity_id, entity_type

Доступно только владельцу пространства.

Мониторинг подозрительных входов

Получи события неудачных 2FA за период:

pachca security list --start-time=<ISO-8601> --end-time=<ISO-8601> --event-key=user_2fa_fail --all


Если найдены аномалии — отправь уведомление администратору:

pachca messages create --entity-type=user --entity-id=<admin_id> --content="Обнаружены подозрительные входы"

Экспорт логов за период

Получи все события за период с пагинацией:

pachca security list --start-time=<ISO-8601> --end-time=<ISO-8601> --all


Собери все события в массив → сохрани в файл или отправь во внешнюю систему

Available event_key values
Category	Keys
Auth	user_login, user_logout, user_2fa_fail, user_2fa_success
Employees	user_created, user_deleted, user_role_changed, user_updated
Tags	tag_created, tag_deleted, user_added_to_tag, user_removed_from_tag
Chats	chat_created, chat_renamed, chat_permission_changed
Chat members	user_chat_join, user_chat_leave, tag_added_to_chat, tag_removed_from_chat
Messages	message_created, message_updated, message_deleted
Reactions and threads	reaction_created, reaction_deleted, thread_created
Tokens	access_token_created, access_token_updated, access_token_destroy
Encryption	kms_encrypt, kms_decrypt
Security	audit_events_accessed, dlp_violation_detected
Search (API)	search_users_api, search_chats_api, search_messages_api
Limitations
Rate limit: ~50 req/sec. On 429 — wait and retry.
limit: max 50
Pagination: cursor-based (limit + cursor)
start_time and end_time are required parameters (ISO-8601, UTC+0)
Endpoints
Method	Path	Description
GET	/audit_events	Журнал аудита событий

If unsure how to complete a task, read the corresponding file from references/.

Weekly Installs
49
Repository
pachca/openapi
GitHub Stars
5
First Seen
Feb 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn