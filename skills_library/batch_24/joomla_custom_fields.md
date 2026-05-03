---
title: joomla-custom-fields
url: https://skills.sh/nicolasflores9/skills/joomla-custom-fields
---

# joomla-custom-fields

skills/nicolasflores9/skills/joomla-custom-fields
joomla-custom-fields
Installation
$ npx skills add https://github.com/nicolasflores9/skills --skill joomla-custom-fields
SKILL.md
Custom Fields in Joomla 5/6

Master custom fields in Joomla. Custom Fields allow you to add additional attributes to articles, users, contacts, and categories without extending the core. They offer 16 different types with native access control and validation.

Quick Start

Load custom fields in your code:

// Register and load the helper
JLoader::register('FieldsHelper', JPATH_ADMINISTRATOR . '/components/com_fields/helpers/fields.php');

// Get fields from an article
$fields = FieldsHelper::getFields('com_content.article', $article, true);

// Render each field
foreach ($fields as $field) {
    echo $field->label . ': ' . $field->value;
}

The 16 Field Types

Text Fields: Text (single line), Textarea (multiline), Editor (full WYSIWYG)

Selection Fields: List (simple list), Checkboxes (multiple), Radio (single option), User (user selector), User Groups (group selector)

Media Fields: Media (file selector), List of images (gallery), Color (color picker)

Specialized Fields: Calendar (date/time), Integer (whole numbers), URL (validated URLs), SQL (dynamic queries), Repeatable (multiple instances)

Each type offers specific parameters. Common parameters include: Label, Required, Filter (NOHTML, RAW, SAFEHTML), Default value, Access (access level).

FieldsHelper API

Access fields programmatically using FieldsHelper. This helper centralizes all custom field logic.

FieldsHelper::getFields() returns an array of fields for an element:

// Signature: getFields($context, $item, $asArray = true)
$fields = FieldsHelper::getFields('com_content.article', $article, true);

// Common contexts
// com_content.article - Articles
// com_content.categories - Categories
// com_users.user - Users
// com_contact.contact - Contacts


Field object properties: $field->id, $field->name (technical), $field->label, $field->type, $field->value (rendered HTML), $field->rawvalue (raw value).

FieldsHelper::render() renders a field's HTML:

foreach ($this->item->jcfields as $field) {
    echo FieldsHelper::render($field->context, 'field.render', array('field' => $field));
}

Creating Fields from Admin

Navigate to Content -> Fields (or Users -> Fields, Contacts -> Fields).

Click "New"
Fill in: Title (visible name), Name (technical), Type (select type)
In Field Group, assign to a group if desired (organizes into tabs)
In Category, limit to specific categories (optional)
Define type-specific parameters (max characters, options, etc.)
Configure validation: Filter and custom rules
Set Access for permission control
Publish the field (state = Published)

Field Groups are created in Content -> Field Groups. They group fields into tabs to improve UX. Without an assigned group, fields appear in the "Fields" tab.

Databases

Main table structure:

#__fields stores definitions:

id - Unique identifier
context - Context (com_content.article, etc.)
name - Technical name (snake_case)
label - Visible label
type - Field type
params - JSON configuration
access - Access level
state - 1=published

#__fields_values stores values:

id - Unique identifier
field_id - Reference to #__fields
item_id - Element ID (article, user, etc.)
value - Stored value (JSON for multiple values)

Typical query with JDatabase:

$db = Factory::getContainer()->get(DatabaseInterface::class);
$query = $db->getQuery(true)
    ->select(['fv.*', 'f.name', 'f.label', 'f.type'])
    ->from($db->quoteName('#__fields_values', 'fv'))
    ->innerJoin($db->quoteName('#__fields', 'f') . ' ON fv.field_id = f.id')
    ->where($db->quoteName('vf.item_id') . ' = ' . (int)$itemId)
    ->where($db->quoteName('f.context') . ' = ' . $db->quote('com_content.article'));
$db->setQuery($query);
$results = $db->loadObjectList();

Rendering in Templates

Access rendered fields via $this->item->jcfields. This array contains all already-loaded fields.

Method 1: Basic rendering with FieldsHelper

<?php foreach ($this->item->jcfields as $field) : ?>
    <div class="field field-<?php echo htmlspecialchars($field->type); ?>">
        <label><?php echo htmlspecialchars($field->label); ?></label>
        <div class="field-value">
            <?php echo $field->value; ?>
        </div>
    </div>
<?php endforeach; ?>


Method 2: Direct access by name

<?php
// Create index by name
foreach($this->item->jcfields as $jcfield) {
    $this->item->jcFields[$jcfield->name] = $jcfield;
}

// Access directly
echo $this->item->jcFields['mi_campo']->value;
?>


Create overrides at: templates/yourtemplate/html/layouts/com_content/fields/render.php

In the override, customize the generated HTML. Each rendered field passes through this layout.

Usage in Modules

In the module helper, load article fields:

<?php
class ModYourModuleHelper {
    public static function getArticleWithFields($articleId) {
        $model = Factory::getApplication()->bootComponent('com_content')
            ->getMVCFactory()
            ->createModel('Article', 'Administrator');
        $article = $model->getItem($articleId);

        JLoader::register('FieldsHelper', JPATH_ADMINISTRATOR . '/components/com_fields/helpers/fields.php');
        $article->jcfields = FieldsHelper::getFields('com_content.article', $article, true);

        return $article;
    }
}
?>


In the module view, render:

<?php foreach ($this->article->jcfields as $field) : ?>
    <div class="field-<?php echo $field->name; ?>">
        <strong><?php echo $field->label; ?></strong>:
        <?php echo $field->value; ?>
    </div>
<?php endforeach; ?>

Integration in Custom Components

Implement the onContentPrepareForm event in a plugin to inject fields into your component:

<?php
use Joomla\CMS\Form\Form;
use Joomla\CMS\Factory;

class PlgSystemYourComponent extends CMSPlugin {
    public function onContentPrepareForm($form, $data) {
        if (!($form instanceof Form)) {
            return true;
        }

        $context = isset($data->context) ? $data->context :
                   Factory::getApplication()->input->getCmd('option') . '.' .
                   Factory::getApplication()->input->getCmd('view');

        // Check your component's context
        if (strpos($context, 'com_mycomponent.myelement') === 0) {
            JLoader::register('FieldsHelper', JPATH_ADMINISTRATOR . '/components/com_fields/helpers/fields.php');
            FieldsHelper::getFields('com_mycomponent.myelement', $data, false);
        }

        return true;
    }
}
?>

Validation and Filters

Define validation in the field configuration using the validate parameter:

validate="required" - Required field
validate="integer" - Integers only
validate="integer:1,100" - Numeric range
validate="email" - Email format
validate="url" - Valid URL
validate="color" - Valid color


Apply filters using Filter:

NOHTML - No HTML tags
RAW - Unprocessed value
SAFEHTML - Safe HTML (filters scripts)
STRING - Simple string
WORD - Words only
ALNUM - Alphanumeric

System Events

Joomla fires events in the field lifecycle:

onContentPrepareForm - Before displaying the form (injects fields)

onContentPrepareData - After loading data (prepares for rendering)

onContentValidateForm - Server-side validation

onContentAfterSave - After saving (processes values)

These events allow you to intercept the flow and apply custom logic. Implement them in a system plugin.

Direct Database Access

For advanced queries, access #__fields and #__fields_values directly:

// Get all fields from an article
$db = Factory::getContainer()->get(DatabaseInterface::class);
$query = $db->getQuery(true)
    ->select('*')
    ->from($db->quoteName('#__fields_values'))
    ->where($db->quoteName('item_id') . ' = ' . (int)$articleId);
$db->setQuery($query);
$values = $db->loadObjectList('field_id');

// Save a field value
$obj = new stdClass();
$obj->field_id = 5;
$obj->item_id = 123;
$obj->value = 'My value';
$db->insertObject('#__fields_values', $obj);

Supported Contexts

Valid contexts for getFields() are:

com_content.article - Articles
com_content.categories - Content categories
com_users.user - User profiles
com_contact.contact - Contacts


Each context has its own field definitions. Verify the context before loading fields.

Fields in Frontend Editors

In frontend forms (user registration, article submission), the system automatically loads fields if:

The field is published (state = 1)
The category matches (if limited)
The user has access (access level)

Fields appear automatically in the form. To render manually, use the same FieldsHelper.

Best Practices

Naming: Use snake_case for technical names (my_field, not myField)

Organization: Group related fields into Field Groups to improve editor UX

Permissions: Set Access appropriately (Registered, Special, etc.)

Validation: Always define server-side validation in the component

Performance: Cache getFields() results if called multiple times

Documentation: Document which fields your component requires

Testing: Test in both frontend and backend that fields display correctly

Troubleshooting

Fields not appearing: Verify that state = published, category matches, and access level is visible

Values not saving: Check that onContentPrepareData is injecting values into the object

Rendering errors: Validate that jcfields contains correct objects, not null

Slow performance: Reduce the number of loaded fields, implement caching

Permissions denied: Verify user access level vs field access

See references/ for complete module and component examples.

Weekly Installs
11
Repository
nicolasflores9/skills
GitHub Stars
1
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass