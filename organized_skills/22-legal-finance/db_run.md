---
rating: ⭐⭐⭐
title: db-run
url: https://skills.sh/arman-kudaibergenov/1c-ai-development-kit/db-run
---

# db-run

skills/arman-kudaibergenov/1c-ai-development-kit/db-run
db-run
Installation
$ npx skills add https://github.com/arman-kudaibergenov/1c-ai-development-kit --skill db-run
SKILL.md
/db-run — Запуск 1С:Предприятие

Запускает информационную базу в режиме 1С:Предприятие (пользовательский режим).

Usage
/db-run [database]
/db-run dev
/db-run dev /Execute process.epf
/db-run dev /C "параметр запуска"

Параметры подключения

Прочитай .v8-project.json из корня проекта. Возьми v8path (путь к платформе) и разреши базу:

Если пользователь указал параметры подключения (путь, сервер) — используй напрямую
Если указал базу по имени — ищи по id / alias / name в .v8-project.json
Если не указал — сопоставь текущую ветку Git с databases[].branches
Если ветка не совпала — используй default Если v8path не задан — автоопределение: Get-ChildItem "C:\Program Files\1cv8\*\bin\1cv8.exe" | Sort -Desc | Select -First 1 Если файла нет — предложи /db-list add. Если использованная база не зарегистрирована — после выполнения предложи добавить через /db-list add.
Команда
powershell.exe -NoProfile -File .claude/skills/db-run/scripts/db-run.ps1 <параметры>

Параметры скрипта
Параметр	Обязательный	Описание
-V8Path <путь>	нет	Каталог bin платформы (или полный путь к 1cv8.exe)
-InfoBasePath <путь>	*	Файловая база
-InfoBaseServer <сервер>	*	Сервер 1С (для серверной базы)
-InfoBaseRef <имя>	*	Имя базы на сервере
-UserName <имя>	нет	Имя пользователя
-Password <пароль>	нет	Пароль
-Execute <файл.epf>	нет	Запуск внешней обработки сразу после старта
-CParam <строка>	нет	Параметр запуска (/C)
-URL <ссылка>	нет	Навигационная ссылка (формат e1cib/...)

* — нужен либо -InfoBasePath, либо пара -InfoBaseServer + -InfoBaseRef

Важно

Скрипт запускает 1С в фоне (Start-Process без -Wait) — управление возвращается сразу.

Примеры
# Простой запуск
powershell.exe -NoProfile -File .claude/skills/db-run/scripts/db-run.ps1 -InfoBasePath "C:\Bases\MyDB" -UserName "Admin"

# Запуск с обработкой
powershell.exe -NoProfile -File .claude/skills/db-run/scripts/db-run.ps1 -InfoBasePath "C:\Bases\MyDB" -UserName "Admin" -Execute "C:\epf\МояОбработка.epf"

# Открыть по навигационной ссылке
powershell.exe -NoProfile -File .claude/skills/db-run/scripts/db-run.ps1 -InfoBasePath "C:\Bases\MyDB" -UserName "Admin" -URL "e1cib/data/Справочник.Номенклатура"

# Серверная база с параметром запуска
powershell.exe -NoProfile -File .claude/skills/db-run/scripts/db-run.ps1 -InfoBaseServer "srv01" -InfoBaseRef "MyDB" -UserName "Admin" -Password "secret" -CParam "ЗапуститьОбновление"

Weekly Installs
11
Repository
arman-kudaiberg…ment-kit
GitHub Stars
122
First Seen
Feb 26, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail