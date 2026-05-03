---
title: pachca-chats
url: https://skills.sh/pachca/openapi/pachca-chats
---

# pachca-chats

skills/pachca/openapi/pachca-chats
pachca-chats
Installation
$ npx skills add https://github.com/pachca/openapi --skill pachca-chats
SKILL.md
pachca-chats
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
Создать канал и пригласить участников

Создай канал с участниками:

pachca chats create --name="Новый канал" --channel --member-ids='[1,2,3]'


"channel": true для канала, false (по умолчанию) для беседы. Участников можно передать сразу: member_ids и/или group_tag_ids

Или добавь участников позже:

pachca members add <chat_id> --member-ids='[1,2,3]'


channel — boolean, не строка. member_ids и group_tag_ids — опциональны при создании.

Переименовать или обновить чат
Обнови чат:
pachca chats update <ID> --name="Новое название"


Доступные поля: name, public

Для изменения состава участников используй POST/DELETE /chats/{id}/members.

Создать проектную беседу из шаблона

Создай беседу с участниками из тега:

pachca chats create --name="Проект Alpha" --group-tag-ids='[42]' --member-ids='[186,187]'


Отправь приветственное сообщение:

pachca messages create --entity-id=<chat_id> --content="Добро пожаловать в проект!"


group_tag_ids при создании добавляет всех участников тега сразу.

Найти активные чаты за период
Получи чаты с активностью после указанной даты:
pachca chats list --last-message-at-after=<дата> --all


Для диапазона добавь --last-message-at-before. Дата в ISO-8601 UTC+0

Найти и заархивировать неактивные чаты

Получи чаты без активности с нужной даты:

pachca chats list --last-message-at-before=<порог> --all


Для каждого чата: архивируй:

pachca chats archive <ID>


Проверяй "channel": false — архивация каналов может быть нежелательной

Limitations
Rate limit: ~50 req/sec. On 429 — wait and retry.
role: allowed values — admin (Админ), editor (Редактор (доступно только для каналов)), member (Участник или подписчик)
limit: max 50
Pagination: cursor-based (limit + cursor)
Endpoints
Method	Path	Description
POST	/chats	Новый чат
GET	/chats	Список чатов
POST	/chats/exports	Экспорт сообщений
GET	/chats/exports/{id}	Скачать архив экспорта
GET	/chats/{id}	Информация о чате
PUT	/chats/{id}	Обновление чата
PUT	/chats/{id}/archive	Архивация чата
POST	/chats/{id}/group_tags	Добавление тегов
DELETE	/chats/{id}/group_tags/{tag_id}	Исключение тега
DELETE	/chats/{id}/leave	Выход из беседы или канала
GET	/chats/{id}/members	Список участников чата
POST	/chats/{id}/members	Добавление пользователей
DELETE	/chats/{id}/members/{user_id}	Исключение пользователя
PUT	/chats/{id}/members/{user_id}	Редактирование роли
PUT	/chats/{id}/unarchive	Разархивация чата
Advanced workflows

For advanced workflows, read the files in references/: references/archive-and-manage-chat.md — Archive and manage chat references/export-chat-history.md — Export chat history

If unsure how to complete a task, read the corresponding file from references/.

Weekly Installs
54
Repository
pachca/openapi
GitHub Stars
5
First Seen
Feb 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass