---
rating: ⭐⭐⭐
title: form-add
url: https://skills.sh/arman-kudaibergenov/1c-ai-development-kit/form-add
---

# form-add

skills/arman-kudaibergenov/1c-ai-development-kit/form-add
form-add
Installation
$ npx skills add https://github.com/arman-kudaibergenov/1c-ai-development-kit --skill form-add
SKILL.md
/form-add — Добавление формы к объекту конфигурации

Создаёт управляемую форму (metadata XML + Form.xml + Module.bsl) и регистрирует её в корневом XML объекта конфигурации (Document, Catalog, InformationRegister и др.).

Usage
/form-add <ObjectPath> <FormName> [Purpose] [Synonym] [--set-default]

Параметр	Обязательный	По умолчанию	Описание
ObjectPath	да	—	Путь к XML-файлу объекта (Documents/Док.xml)
FormName	да	—	Имя формы (ФормаДокумента)
Purpose	нет	Object	Назначение: Object, List, Choice, Record
Synonym	нет	= FormName	Синоним формы
--set-default	нет	авто	Установить как форму по умолчанию
Команда
powershell.exe -NoProfile -File .claude/skills/form-add/scripts/form-add.ps1 -ObjectPath "<ObjectPath>" -FormName "<FormName>" [-Purpose "<Purpose>"] [-Synonym "<Synonym>"] [-SetDefault]

Purpose — назначение формы
Purpose	Допустимые типы объектов	Основной реквизит	DefaultForm-свойство
Object	Document, Catalog, DataProcessor, Report, ExternalDataProcessor, ExternalReport, ChartOf*, ExchangePlan, BusinessProcess, Task	Объект (тип: *Object.Имя)	DefaultObjectForm (DefaultForm для DataProcessor/Report/ExternalDataProcessor/ExternalReport)
List	Все кроме DataProcessor	Список (DynamicList)	DefaultListForm
Choice	Document, Catalog, ChartOf*, ExchangePlan, BusinessProcess, Task	Список (DynamicList)	DefaultChoiceForm
Record	InformationRegister	Запись (InformationRegisterRecordManager)	DefaultRecordForm
Что создаётся
<ObjectDir>/Forms/
├── <FormName>.xml                    # Метаданные формы (UUID)
└── <FormName>/
    └── Ext/
        ├── Form.xml                  # Описание формы (logform namespace)
        └── Form/
            └── Module.bsl           # BSL-модуль с 5 регионами + ПриСозданииНаСервере

Что модифицируется
<ObjectPath> — добавляется <Form> в ChildObjects (перед <Template> или <TabularSection>), обновляется Default*Form (автоматически если пустое, или явно при --set-default)
Поддерживаемые типы объектов

Document, Catalog, DataProcessor, Report, ExternalDataProcessor, ExternalReport, InformationRegister, ChartOfAccounts, ChartOfCharacteristicTypes, ExchangePlan, BusinessProcess, Task

Примеры
# Форма документа
/form-add Documents/АвансовыйОтчет.xml ФормаДокумента --purpose Object

# Форма списка каталога
/form-add Catalogs/Контрагенты.xml ФормаСписка --purpose List

# Форма записи регистра сведений
/form-add InformationRegisters/КурсыВалют.xml ФормаЗаписи --purpose Record

# Форма выбора с синонимом
/form-add Catalogs/Номенклатура.xml ФормаВыбора --purpose Choice --synonym "Выбор номенклатуры"

# Установить как форму по умолчанию
/form-add Documents/Заказ.xml ФормаДокументаНовая --purpose Object --set-default

Workflow
/form-add — создать каркас формы
/form-compile или /form-edit — наполнить Form.xml элементами
/form-validate — проверить корректность
/form-info — проанализировать результат
Weekly Installs
11
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