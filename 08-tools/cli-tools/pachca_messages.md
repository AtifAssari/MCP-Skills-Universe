---
title: pachca-messages
url: https://skills.sh/pachca/openapi/pachca-messages
---

# pachca-messages

skills/pachca/openapi/pachca-messages
pachca-messages
Installation
$ npx skills add https://github.com/pachca/openapi --skill pachca-messages
SKILL.md
pachca-messages
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
Найти чат по имени и отправить сообщение

Найди чат по названию через поиск:

pachca search list-chats --query="название"


Если результатов несколько — выбери наиболее подходящий по name

Отправь сообщение в найденный чат:

pachca messages create --entity-id=<chat_id> --content="Текст сообщения"


entity_type по умолчанию "discussion", можно не указывать.

Отправить сообщение в канал или беседу (если chat_id известен)
Отправь сообщение в чат:
pachca messages create --entity-id=<chat_id> --content="Текст сообщения"


"entity_type": "discussion" используется по умолчанию, можно не указывать

Отправить личное сообщение пользователю

Определи user_id получателя:

pachca search list-users --query="имя"


Или возьми user_id из контекста (вебхук, предыдущий запрос)

Отправь личное сообщение:

pachca messages create --entity-type=user --entity-id=<user_id> --content="Привет!"


Создавать чат не требуется — он создаётся автоматически

Ответить в тред (комментарий к сообщению)

Получи или создай тред, возьми thread.id из ответа:

pachca thread add <ID>


Если тред уже существует, вернётся существующий

Отправь сообщение в тред:

pachca messages create --entity-type=thread --entity-id=<thread_id> --content="Ответ в тред"


skip_invite_mentions: true — не добавлять упомянутых пользователей в тред автоматически.

Отправить сообщение с кнопками

Сформируй массив buttons — массив строк, каждая строка — массив кнопок

Каждая кнопка: {"text": "Текст"} + либо url (ссылка), либо data (callback)

Отправь сообщение с кнопками:

pachca messages create --entity-id=<chat_id> --content="Выбери действие" --buttons='[[{"text":"Подробнее","url":"https://example.com"},{"text":"Отлично!","data":"awesome"}]]'


buttons — массив массивов (строки × кнопки). Максимум 100 кнопок, до 8 в строке. Кнопка с url открывает ссылку, с data — отправляет событие на вебхук.

Получить историю сообщений чата
Получи сообщения чата с пагинацией:
pachca messages list --chat-id=<chat_id>


limit (1-50), cursor, sort[id]=asc или desc (по умолчанию)

Для сообщений треда используй chat_id треда (thread.chat_id). Пагинация cursor-based, не page-based.

Получить вложения из сообщения

Получи сообщение — в files[] каждый объект содержит url, name, file_type, size:

pachca messages get <ID>


Скачай нужные файлы по files[].url

Ссылка прямая, авторизация не требуется

Вебхук о новом сообщении НЕ содержит вложений — поле files отсутствует. Всегда проверяй вложения через GET /messages/{id}.

Закрепить/открепить сообщение

Закрепить сообщение:

pachca messages pin <ID>


Открепить сообщение:

pachca messages unpin <ID> --force


В чате может быть несколько закреплённых сообщений.

Подписаться на тред сообщения

Получи или создай тред, возьми chat_id из ответа:

pachca thread add <ID>


Добавь бота в участники чата треда:

pachca members add <thread_chat_id> --member-ids='[<bot_user_id>]'


Теперь бот будет получать вебхук-события о новых сообщениях в этом треде

POST /messages/{id}/thread идемпотентен — безопасно вызывать повторно.

Отредактировать сообщение
Обнови сообщение:
pachca messages update <ID> --content="Обновлённый текст"


Редактировать можно только свои сообщения (или от имени бота).

Изменить вложения сообщения

Получи текущие вложения из files[]:

pachca messages get <ID>


Сохрани нужные объекты (key, name, file_type, size)

Если нужно добавить новый файл — загрузи его:

pachca common uploads


Обнови сообщение с новым массивом files:

pachca messages update <ID> --files='[...]'


files при редактировании — replace-all: присылаемый массив полностью заменяет текущие

files: [] удаляет все вложения. Если поле files не передавать — вложения не меняются.

Удалить сообщение
Удали сообщение:
pachca messages delete <ID> --force

Добавить реакцию на сообщение

Добавь реакцию:

pachca reactions add <ID> --code="👍"


Убрать реакцию:

pachca reactions remove <ID> --code="👍" --force


code — emoji-символ, не его текстовое название.

Проверить, кто прочитал сообщение

Получи массив user_id прочитавших:

pachca read-member list-readers <ID>


При необходимости сопоставь с именами сотрудников:

pachca users list

Разослать уведомление нескольким пользователям

Определи список user_id получателей:

pachca users list --all


Или получи user_id из тега — см. «Получить всех сотрудников тега/департамента»

Для каждого: отправь личное сообщение:

pachca messages create --entity-type=user --entity-id=<user_id> --content="Уведомление"


Для каждого получателя

Соблюдай rate limit: ~4 req/sec для сообщений. Добавляй паузы при большом списке.

Limitations
Rate limit: ~50 req/sec, messages ~4 req/sec per chat. On 429 — wait and retry.
message.entity_type: allowed values — discussion (Беседа или канал), thread (Тред), user (Пользователь)
message.display_avatar_url: max 255 characters
message.display_name: max 255 characters
limit: max — 50 (GET /messages), 50 (GET /messages/{id}/reactions), 300 (GET /messages/{id}/read_member_ids)
Pagination: cursor-based (limit + cursor)
Endpoints
Method	Path	Description
POST	/direct_url	Загрузка файла
POST	/messages	Новое сообщение
GET	/messages	Список сообщений чата
GET	/messages/{id}	Информация о сообщении
PUT	/messages/{id}	Редактирование сообщения
DELETE	/messages/{id}	Удаление сообщения
POST	/messages/{id}/pin	Закрепление сообщения
DELETE	/messages/{id}/pin	Открепление сообщения
POST	/messages/{id}/reactions	Добавление реакции
DELETE	/messages/{id}/reactions	Удаление реакции
GET	/messages/{id}/reactions	Список реакций
GET	/messages/{id}/read_member_ids	Список прочитавших сообщение
POST	/messages/{id}/thread	Новый тред
GET	/threads/{id}	Информация о треде
POST	/uploads	Получение подписи, ключа и других параметров
Advanced workflows

For advanced workflows, read the files in references/: references/reply-to-user-who-messaged-the-bot.md — Reply to user who messaged the bot references/send-message-with-files.md — Send message with files references/mention-user.md — Mention user

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
SocketPass
SnykFail