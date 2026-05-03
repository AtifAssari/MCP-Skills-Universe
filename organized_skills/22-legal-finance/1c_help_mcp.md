---
rating: ⭐⭐⭐
title: 1c-help-mcp
url: https://skills.sh/arman-kudaibergenov/1c-ai-development-kit/1c-help-mcp
---

# 1c-help-mcp

skills/arman-kudaibergenov/1c-ai-development-kit/1c-help-mcp
1c-help-mcp
Installation
$ npx skills add https://github.com/arman-kudaibergenov/1c-ai-development-kit --skill 1c-help-mcp
SKILL.md
/1c-help-mcp — Поиск по документации 1С

Семантический поиск по документации платформы 1С:Предприятие 8.3 через MCP.

MCP сервер
Сервер: PROJECT-codemetadata (CT104, YOUR_MCP_SERVER:7530) — инструмент helpsearch
Содержит 927 документов документации, 54178 документов кода
Когда использовать
Нужна сигнатура метода или функции платформы
Нужен синтаксис конструкции языка
Нужны примеры использования API
Поиск встроенных функций
Когда НЕ использовать
Функции БСП → используй ssl_search / /bsp-patterns
Шаблоны кода → используй templatesearch
Код проекта → используй codesearch / metadatasearch
Примеры запросов
helpsearch("СтрРазделить")           # Конкретный метод
helpsearch("работа с файлами")       # По функциональности
helpsearch("HTTP соединение")        # Платформенная фича
helpsearch("функции строки")         # Группа функций

Workflow
Поиск метода: helpsearch(query)
Получить шаблон: templatesearch(query) (если нужен пример)
Написать код
Проверить синтаксис через валидацию
Weekly Installs
12
Repository
arman-kudaiberg…ment-kit
GitHub Stars
122
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass