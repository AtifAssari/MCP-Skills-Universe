---
title: pachca-users
url: https://skills.sh/pachca/openapi/pachca-users
---

# pachca-users

skills/pachca/openapi/pachca-users
pachca-users
Installation
$ npx skills add https://github.com/pachca/openapi --skill pachca-users
SKILL.md
pachca-users
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
Получить сотрудника по ID
Получи информацию о сотруднике:
pachca users get <ID>


Возвращает все поля, включая custom_properties, user_status, list_tags.

Массовое создание сотрудников с тегами

Создай тег (если нужен):

pachca group-tags create --name="Backend"


Для каждого сотрудника: создай аккаунт с тегами:

pachca users create --first-name="Иван" --last-name="Петров" --email="ivan@example.com" --list-tags='[{"name":"Backend"}]'


Теги назначаются через поле list_tags в теле запроса

Или обнови существующего:

pachca users update <ID> --list-tags='[{"name":"Backend"}]'


Создание доступно только администраторам и владельцам (не ботам). Нет отдельного эндпоинта "добавить юзера в тег".

Найти сотрудника по имени или email
Поиск по имени/email (частичное совпадение):
pachca users list --query=Иван


Пагинация cursor-based: limit и cursor из meta. Для точного email — перебери страницы.

Онбординг нового сотрудника

Создай аккаунт:

pachca users create --email="new@example.com" --first-name="Иван" --last-name="Петров"


Добавь в нужные каналы:

pachca members add <chat_id> --member-ids='[<user_id>]'


Отправь welcome-сообщение:

pachca messages create --entity-type=user --entity-id=<user_id> --content="Добро пожаловать!"


Шаг 1 требует токена администратора/владельца. Шаги 2-3 можно делать ботом.

Offboarding сотрудника

Заблокировать доступ:

pachca users update <ID> --suspended


Опционально: удалить аккаунт полностью:

pachca users delete <ID> --force


Приостановка (suspended) сохраняет данные, удаление — необратимо.

Получить всех сотрудников тега/департамента

Найди тег по названию, возьми id:

pachca group-tags list --names='["Backend"]'


Фильтр names — серверная фильтрация по названию тега

Получи всех участников тега:

pachca group-tags list-users <tag_id> --all

Управление статусом сотрудника

Получить текущий статус:

pachca users get-status <user_id>


Установить статус:

pachca users update-status <user_id> --emoji="🏖️" --title="В отпуске" --is-away


is_away: true — режим «Нет на месте». away_message — макс 1024 символа

Удалить статус:

pachca users remove-status <user_id> --force

Загрузить аватар сотрудника
Загрузи аватар сотруднику:
pachca users update-avatar <user_id> --file=<путь_к_файлу>


Требует прав администратора. Файл передается в формате multipart/form-data

Удалить аватар сотрудника
Удали аватар сотрудника:
pachca users remove-avatar <user_id> --force


Требует прав администратора

Limitations
Rate limit: ~50 req/sec. On 429 — wait and retry.
user.role: allowed values — admin (Администратор), user (Сотрудник), multi_guest (Мульти-гость)
status.away_message: max 1024 characters
limit: max 50
Pagination: cursor-based (limit + cursor)
Endpoints
Method	Path	Description
POST	/group_tags	Новый тег
GET	/group_tags	Список тегов сотрудников
GET	/group_tags/{id}	Информация о теге
PUT	/group_tags/{id}	Редактирование тега
DELETE	/group_tags/{id}	Удаление тега
GET	/group_tags/{id}/users	Список сотрудников тега
POST	/users	Создать сотрудника
GET	/users	Список сотрудников
GET	/users/{id}	Информация о сотруднике
PUT	/users/{id}	Редактирование сотрудника
DELETE	/users/{id}	Удаление сотрудника
PUT	/users/{user_id}/avatar	Загрузка аватара сотрудника
DELETE	/users/{user_id}/avatar	Удаление аватара сотрудника
GET	/users/{user_id}/status	Статус сотрудника
PUT	/users/{user_id}/status	Новый статус сотрудника
DELETE	/users/{user_id}/status	Удаление статуса сотрудника

If unsure how to complete a task, read the corresponding file from references/.

Weekly Installs
52
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