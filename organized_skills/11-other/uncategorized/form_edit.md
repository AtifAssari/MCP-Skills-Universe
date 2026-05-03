---
rating: ⭐⭐
title: form-edit
url: https://skills.sh/arman-kudaibergenov/1c-ai-development-kit/form-edit
---

# form-edit

skills/arman-kudaibergenov/1c-ai-development-kit/form-edit
form-edit
Installation
$ npx skills add https://github.com/arman-kudaibergenov/1c-ai-development-kit --skill form-edit
SKILL.md
/form-edit — Редактирование формы

Добавляет элементы, реквизиты и/или команды в существующий Form.xml. Автоматически выделяет ID из правильного пула, генерирует companion-элементы (ContextMenu, ExtendedTooltip, и др.) и обработчики событий.

Использование
/form-edit <FormPath> <JsonPath>

Параметры
Параметр	Обязательный	Описание
FormPath	да	Путь к существующему Form.xml
JsonPath	да	Путь к JSON с описанием добавлений
Команда
powershell.exe -NoProfile -File .claude/skills/form-edit/scripts/form-edit.ps1 -FormPath "<путь>" -JsonPath "<путь>"

JSON формат
{
  "into": "ГруппаШапка",
  "after": "Контрагент",
  "elements": [
    { "input": "Склад", "path": "Объект.Склад", "on": ["OnChange"] }
  ],
  "attributes": [
    { "name": "СуммаИтого", "type": "decimal(15,2)" }
  ],
  "commands": [
    { "name": "Рассчитать", "action": "РассчитатьОбработка" }
  ]
}

Позиционирование элементов
Ключ	По умолчанию	Описание
into	корневой ChildItems	Имя группы/таблицы/страницы, куда вставлять
after	в конец	Имя элемента, после которого вставлять
Типы элементов

Те же DSL-ключи, что в /form-compile:

Ключ	XML тег	Companions
input	InputField	ContextMenu, ExtendedTooltip
check	CheckBoxField	ContextMenu, ExtendedTooltip
label	LabelDecoration	ContextMenu, ExtendedTooltip
labelField	LabelField	ContextMenu, ExtendedTooltip
group	UsualGroup	ExtendedTooltip
table	Table	ContextMenu, AutoCommandBar, Search*, ViewStatus*
pages	Pages	ExtendedTooltip
page	Page	ExtendedTooltip
button	Button	ExtendedTooltip

Группы и таблицы поддерживают children/columns для вложенных элементов.

Кнопки: command и stdCommand
"command": "ИмяКоманды" → Form.Command.ИмяКоманды
"stdCommand": "Close" → Form.StandardCommand.Close
"stdCommand": "Товары.Add" → Form.Item.Товары.StandardCommand.Add (стандартная команда элемента)
Допустимые события (on)

Компилятор предупреждает об ошибках в именах событий. Основные:

input: OnChange, StartChoice, ChoiceProcessing, Clearing, AutoComplete, TextEditEnd
check: OnChange
table: OnStartEdit, OnEditEnd, OnChange, Selection, BeforeAddRow, BeforeDeleteRow, OnActivateRow
label/picture: Click, URLProcessing
pages: OnCurrentPageChange
button: Click
Система типов (для attributes)

string, string(100), decimal(15,2), boolean, date, dateTime, CatalogRef.XXX, DocumentObject.XXX, ValueTable, DynamicList, Type1 | Type2 (составной).

Вывод
=== form-edit: Форма ===

Added elements (into ГруппаШапка, after Контрагент):
  + [Input] Склад -> Объект.Склад {OnChange}

Added attributes:
  + СуммаИтого: decimal(15,2) (id=12)

---
Total: 1 element(s) (+2 companions), 1 attribute(s)
Run /form-validate to verify.

Когда использовать
После /form-compile: добавить элементы, которые не были в исходном JSON
Модификация существующих форм: добавить поле, реквизит или команду в форму из конфигурации
Пакетное добавление: один JSON может содержать элементы + реквизиты + команды
Workflow
/form-info — посмотреть текущую структуру формы
Создать JSON с описанием добавлений
/form-edit — добавить в форму
/form-validate — проверить корректность
/form-info — убедиться что добавилось правильно
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