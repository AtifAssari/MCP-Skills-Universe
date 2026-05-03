---
title: cfe-init
url: https://skills.sh/arman-kudaibergenov/1c-ai-development-kit/cfe-init
---

# cfe-init

skills/arman-kudaibergenov/1c-ai-development-kit/cfe-init
cfe-init
Installation
$ npx skills add https://github.com/arman-kudaibergenov/1c-ai-development-kit --skill cfe-init
SKILL.md
/cfe-init — Создание расширения конфигурации 1С

Создаёт scaffold расширения: Configuration.xml, Languages/Русский.xml, опционально Roles/.

Подготовка

Перед созданием расширения рекомендуется получить версию и режим совместимости базовой конфигурации:

/cf-info <ConfigPath> -Mode brief


Это даст CompatibilityMode (передать в -CompatibilityMode) и версию конфигурации (для -Version, например <ВерсияКонфигурации>.1).

Параметры
Параметр	Описание	По умолчанию
Name	Имя расширения (обязат.)	—
Synonym	Синоним	= Name
NamePrefix	Префикс собственных объектов	= Name + "_"
OutputDir	Каталог для создания	src
Purpose	Patch (исправление) / Customization (доработка) / AddOn (дополнение)	Customization
Version	Версия расширения	—
Vendor	Поставщик	—
CompatibilityMode	Режим совместимости	Version8_3_24
NoRole	Без основной роли	false
Команда
powershell.exe -NoProfile -File .claude/skills/cfe-init/scripts/cfe-init.ps1 -Name "МоёРасширение"

Что создаётся
<OutputDir>/
├── Configuration.xml         # Свойства расширения
├── Languages/
│   └── Русский.xml           # Язык (заимствованный)
└── Roles/                    # Если не -NoRole
    └── <Prefix>ОсновнаяРоль.xml

Примеры
# Расширение-исправление для ERP
... -Name Расш1 -Purpose Patch -CompatibilityMode Version8_3_17 -OutputDir src

# Расширение-доработка с версией
... -Name МоёРасширение -Version "1.0.0.1" -Vendor "Компания" -OutputDir src

# Без роли, с явным префиксом
... -Name ИсправлениеБага -NamePrefix "ИБ_" -Purpose Patch -NoRole -OutputDir src

Верификация
/cfe-validate <OutputDir>

Weekly Installs
8
Repository
arman-kudaiberg…ment-kit
GitHub Stars
122
First Seen
Feb 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass