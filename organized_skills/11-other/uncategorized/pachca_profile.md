---
rating: ⭐⭐
title: pachca-profile
url: https://skills.sh/pachca/openapi/pachca-profile
---

# pachca-profile

skills/pachca/openapi/pachca-profile
pachca-profile
Installation
$ npx skills add https://github.com/pachca/openapi --skill pachca-profile
SKILL.md
pachca-profile
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
Получить свой профиль
Получи информацию о текущем пользователе:
pachca profile get


Возвращает id, first_name, last_name, nickname, email, phone_number, department, title, role, suspended, invite_status, list_tags, custom_properties, user_status, bot, sso, created_at, last_activity_at, time_zone, image_url.

Проверить свой токен
Получи информацию о токене: скоупы, дату создания, срок жизни:
pachca profile get-info


Полезно для диагностики: какие скоупы доступны токену, когда он истекает.

Установить статус
Установи статус:
pachca profile update-status --emoji="🏖️" --title="В отпуске" --is-away --away-message="Я в отпуске до 10 марта" --expires-at="2025-03-10T23:59:59.000Z"


is_away: true — режим «Нет на месте». expires_at — автосброс (ISO-8601, UTC+0). away_message — макс 1024 символа

Сбросить статус
Удали статус:
pachca profile delete-status --force

Получить кастомные поля профиля

Получи список дополнительных полей для сотрудников:

pachca common custom-properties --entity-type=User


Добавь entity_type=User для фильтрации

Получи профиль — в custom_properties содержатся значения полей:

pachca profile get


Кастомные поля настраиваются администратором пространства.

Загрузить аватар профиля
Загрузи аватар из файла:
pachca profile update-avatar --file=<путь_к_файлу>


Файл изображения передается в формате multipart/form-data

Удалить аватар профиля
Удали аватар:
pachca profile delete-avatar --force

Limitations
Rate limit: ~50 req/sec. On 429 — wait and retry.
status.away_message: max 1024 characters
Pagination: cursor-based (limit + cursor)
Endpoints
Method	Path	Description
GET	/custom_properties	Список дополнительных полей
GET	/oauth/token/info	Информация о токене
GET	/profile	Информация о профиле
PUT	/profile/avatar	Загрузка аватара
DELETE	/profile/avatar	Удаление аватара
GET	/profile/status	Текущий статус
PUT	/profile/status	Новый статус
DELETE	/profile/status	Удаление статуса

If unsure how to complete a task, read the corresponding file from references/.

Weekly Installs
55
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