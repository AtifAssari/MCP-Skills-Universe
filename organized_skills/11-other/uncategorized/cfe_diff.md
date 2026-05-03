---
rating: ⭐⭐⭐
title: cfe-diff
url: https://skills.sh/arman-kudaibergenov/1c-ai-development-kit/cfe-diff
---

# cfe-diff

skills/arman-kudaibergenov/1c-ai-development-kit/cfe-diff
cfe-diff
Installation
$ npx skills add https://github.com/arman-kudaibergenov/1c-ai-development-kit --skill cfe-diff
SKILL.md
/cfe-diff — Анализ расширения конфигурации

Анализирует расширение в двух режимах: обзор изменений (Mode A) или проверка переноса (Mode B).

Параметры
Параметр	Описание	По умолчанию
ExtensionPath	Путь к расширению (обязат.)	—
ConfigPath	Путь к конфигурации (обязат.)	—
Mode	A (обзор) / B (проверка переноса)	A
Команда
powershell.exe -NoProfile -File .claude/skills/cfe-diff/scripts/cfe-diff.ps1 -ExtensionPath src -ConfigPath C:\cfsrc\erp -Mode A

Mode A — обзор расширения

Для каждого объекта показывает:

[BORROWED] — заимствованный: перехватчики (&Перед, &После, &ИзменениеИКонтроль, &Вместо), собственные реквизиты/ТЧ/формы
[OWN] — собственный: количество реквизитов, ТЧ, форм

Пример вывода:

[BORROWED] Catalog.Валюты
           &ИзменениеИКонтроль("РеквизитыРедактируемыеВГрупповойОбработке") — line 4 in ...
           &Перед("ЗагрузитьКурсыВалют") — line 13 in ...
           ChildObjects: 1 own attrs, 1 own TS, 3 own forms
[OWN]      Catalog.Расш5_Справочник1

Mode B — проверка переноса

Для каждого &ИзменениеИКонтроль извлекает блоки #Вставка/#КонецВставки из расширения и ищет их в соответствующем модуле конфигурации.

Статусы:

[TRANSFERRED] — код найден в конфигурации
[NOT_TRANSFERRED] — код не найден
[NEEDS_REVIEW] — нет блоков #Вставка или модуль конфигурации не найден
Примеры
# Обзор — что изменено в расширении
... -ExtensionPath src -ConfigPath C:\cfsrc\erp -Mode A

# Проверка переноса — все ли #Вставка перенесены
... -ExtensionPath src -ConfigPath C:\cfsrc\erp -Mode B

Weekly Installs
9
Repository
arman-kudaiberg…ment-kit
GitHub Stars
122
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass