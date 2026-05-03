---
rating: ⭐⭐
title: hyva-cms-custom-field
url: https://skills.sh/hyva-themes/hyva-ai-tools/hyva-cms-custom-field
---

# hyva-cms-custom-field

skills/hyva-themes/hyva-ai-tools/hyva-cms-custom-field
hyva-cms-custom-field
Installation
$ npx skills add https://github.com/hyva-themes/hyva-ai-tools --skill hyva-cms-custom-field
SKILL.md
Hyvä CMS Custom Field Type Creator
Overview

This skill guides the creation of custom field types and field handlers for Hyvä CMS components. Custom field types extend the built-in field types (text, textarea, select, etc.) with specialized input controls for the CMS editor interface.

Two types of custom fields:

Basic Custom Field Type: Custom input control with direct data entry (e.g., date range, color picker, custom validation)
Field Handler: Enhanced UI with complex interactions (e.g., product selector with images, searchable dropdown, link configuration modal)

Command execution: For commands that need to run inside the development environment (e.g., bin/magento), use the hyva-exec-shell-cmd skill to detect the environment and determine the appropriate command wrapper.

Workflow
Step 1: Module Selection

If not already specified in the prompt, determine where to create the custom field type:

Option A: New Module

Use the hyva-create-module skill with:

dependencies: ["Hyva_CmsBase", "Hyva_CmsLiveviewEditor"]
composer_require: {"hyva-themes/commerce-module-cms": "^1.0"}

Option B: Existing Module

Verify the module has required dependencies:

Hyva_CmsBase and Hyva_CmsLiveviewEditor in etc/module.xml
hyva-themes/commerce-module-cms in composer.json

Add missing dependencies if needed.

Step 2: Field Type Details

Gather information about the custom field type:

Field type name (lowercase identifier, e.g., date_range, product_selector, color_picker)
Purpose (what data does it collect?)
UI pattern:
Basic field: Simple input with validation (date picker, pattern input, enhanced text field)
Inline handler: Enhanced control in field area (searchable dropdown, color picker)
Modal handler: Separate dialog for complex selection (product selector, link builder, media gallery)
Data structure (simple string, JSON object, array?)
Validation requirements (pattern, required, custom rules?)
Step 3: Implementation Pattern Selection

Based on the UI pattern identified in Step 2:

Pattern A: Basic Custom Field Type

For simple inputs with custom HTML5 validation or specialized input controls:

Single template file for the field
No separate handler modal
Example: Date range selector, custom pattern validation, slider input

Pattern B: Inline Field Handler

For enhanced controls that remain in the field area:

Single template file with Alpine.js component
No separate handler modal
Example: Searchable select dropdown, color picker with swatches

Pattern C: Modal-Based Field Handler

For complex selection interfaces requiring more space:

Field template (displays selection + trigger button)
Handler modal template (separate dialog with full UI)
Layout XML registration for the handler
Example: Product selector, link configuration, media gallery

See references/handler-patterns.md for detailed implementation patterns and code examples for each type.

Step 4: Generate Field Template

Create the field template at view/adminhtml/templates/field-types/[field-type-name].phtml.

Required template elements:

Field container with proper ID: field-container-{uid}_{fieldName}
Input element(s) with name: {uid}_{fieldName}
Validation messages container: validation-messages-{uid}_{fieldName}
updateWireField() or updateField() call on value change
Error state handling via $magewire->errors
IMPORTANT: Use null coalescing for field value: $block->getData('value') ?? '' (NOT type casting)

Use the appropriate template from assets/templates/:

basic-field.phtml.tpl - Basic custom field type
inline-handler.phtml.tpl - Inline enhanced control
modal-field.phtml.tpl - Modal handler field template

See references/template-requirements.md for detailed template requirements and patterns.

Step 5: Generate Handler Modal (if needed)

For modal-based handlers only, create the handler template at view/adminhtml/templates/handlers/[handler-name]-handler.phtml.

Handler modal structure:

<dialog> element with Alpine.js component and open:flex class (NOT static flex)
Listen for initialization event from field template
Implement selection UI (search, filters, grid, etc.)
Dispatch editor-change event on save

Use assets/templates/modal-handler.phtml.tpl as the starting point.

See references/handler-communication.md for event protocols and data exchange patterns.

Step 6: Register Field Type

Add registration to etc/adminhtml/di.xml:

<type name="Hyva\CmsLiveviewEditor\Model\CustomField">
    <arguments>
        <argument name="customTypes" xsi:type="array">
            <item name="[field_type_name]" xsi:type="string">
                [Vendor]_[Module]::field-types/[field-type-name].phtml
            </item>
        </argument>
    </arguments>
</type>

Step 7: Register Handler Modal (if needed)

For modal-based handlers only, create or update view/adminhtml/layout/liveview_editor.xml:

<?xml version="1.0"?>
<page xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:noNamespaceSchemaLocation="urn:magento:framework:View/Layout/etc/page_configuration.xsd">
    <body>
        <referenceContainer name="before.body.end">
            <block name="[handler_name]_handler"
                   template="[Vendor]_[Module]::handlers/[handler-name]-handler.phtml"/>
        </referenceContainer>
    </body>
</page>


Note: Inline handlers do NOT require layout XML registration.

Step 8: Usage Example

Provide an example of using the custom field type in components.json:

{
    "my_component": {
        "label": "My Component",
        "content": {
            "[field_name]": {
                "type": "custom_type",
                "custom_type": "[field_type_name]",
                "label": "Field Label",
                "attributes": {
                    "required": true,
                    "pattern": ".*"
                }
            }
        }
    }
}

Resources
references/template-requirements.md

Complete reference for custom field type template requirements:

Required markup patterns and element IDs
Field container structure
Validation message containers
Field value update methods (updateWireField vs updateField)
HTML5 validation attributes
Error state handling

Read this file when implementing the field template to ensure proper integration with the CMS editor.

references/handler-patterns.md

Implementation patterns for all three custom field types:

Basic custom field type (simple input)
Inline field handler (enhanced control)
Modal-based field handler (dialog selection)

Each pattern includes:

Complete code examples
When to use each pattern
Alpine.js component structure
Data flow and state management

Read this file when selecting the implementation pattern and writing the template code.

references/handler-communication.md

Event protocols and data exchange for field handlers:

Initialization event structure
Save event structure
Field value encoding/decoding
Error handling patterns
Common pitfalls and solutions

Read this file when implementing handler modals to understand the communication protocol.

references/built-in-handlers.md

Reference for Hyvä CMS built-in field handlers:

Product Handler (modal-based, image grid selection)
Link Handler (modal-based, multi-type link config)
Searchable Select (inline enhanced dropdown)

Each includes:

Location in Hyvä CMS module
Key features and patterns
Usage examples
Code to examine for patterns

Read this file when looking for implementation examples or patterns to copy.

assets/templates/basic-field.phtml.tpl

Template for basic custom field types with custom validation or input controls.

Placeholders:

{{FIELD_TYPE_NAME}} - Custom field type identifier
{{FIELD_INPUTS}} - Input element(s) HTML
{{VALIDATION_LOGIC}} - Custom validation JavaScript (optional)
assets/templates/inline-handler.phtml.tpl

Template for inline enhanced controls (searchable dropdown, color picker, etc.).

Placeholders:

{{HANDLER_NAME}} - Alpine.js component name
{{HANDLER_LOGIC}} - Alpine.js component implementation
{{HANDLER_UI}} - Enhanced control HTML
assets/templates/modal-field.phtml.tpl

Field template for modal-based handlers (trigger button + hidden input).

Placeholders:

{{EVENT_NAME}} - Custom event name to dispatch
{{BUTTON_LABEL}} - Button text
{{DISPLAY_VALUE}} - Current selection display
assets/templates/modal-handler.phtml.tpl

Handler modal template for modal-based selection interfaces.

Placeholders:

{{HANDLER_NAME}} - Alpine.js component name
{{MODAL_TITLE}} - Dialog header text
{{SELECTION_UI}} - Selection interface HTML
{{SAVE_LOGIC}} - Save button logic
Important Guidelines
Core Requirements
Template Requirements: All custom field types must follow required markup patterns (container ID, input name, validation messages)
Handler Registration: Modal handlers need layout XML registration; inline handlers do not
Validation: Apply HTML5 validation attributes via $filteredAttributes for automatic validation
Alpine Components: If using custom Alpine components, keep input fields outside the component and update via vanilla JS
Built-In Examples: Reference built-in handlers in Hyva_CmsLiveviewEditor::page/js/ for proven patterns
Accurate Patterns from Codebase

Based on built-in Hyvä CMS handler implementations:

Event Naming Convention: Use toggle-{type}-select pattern

✅ Correct: toggle-product-select, toggle-link-select, toggle-category-select
❌ Incorrect: toggle-product-handler, toggle-link-handler

Handler Function Naming: Use init{Type}Select() pattern

✅ Examples: initProductSelect(), initLinkSelect(), initCategorySelect()

Field Value Update Methods:

Use updateWireField (default): Products, Link, Category handlers
Triggers immediate server-side validation via Magewire
Keeps component state synchronized
Use updateField (specialized): Image handler, debounced inputs (color, range)
Updates preview without server round-trip
Defers validation until save

JSON Encoding Pattern: All complex data (arrays, objects) must be JSON-encoded

// Field template
value="<?= $escaper->escapeHtmlAttr(json_encode($fieldValue)) ?>"

// Handler initialization
const data = JSON.parse(fieldValue);

// @change handler
@change="updateWireField(..., JSON.parse($event.target.value))"


wire:ignore for Livewire Compatibility: Searchable select uses wire:ignore wrapper

<div wire:ignore>
    <div x-data="initSearchableSelect(...)">
        <!-- Alpine component -->
    </div>
</div>


Separate Handler Files: Even inline handlers may have separate function files

Field template: liveview/field-types/searchable_select.phtml
Handler function: page/js/searchable-select-handler.phtml

Icons View Model: Use for UI elements

/** @var Icons $icons */
$icons = $viewModels->require(Icons::class);
<?= /** @noEscape */ $icons->trashHtml('', 22, 22) ?>


FieldTypes View Model: Use for attribute filtering

/** @var FieldTypes $fieldTypes */
$fieldTypes = $viewModels->require(FieldTypes::class);
$filteredAttributes = $fieldTypes->getDefinedFieldAttributes($attributes);
// Or for specific attributes:
$filteredAttributes = $fieldTypes->getAttributesByKeys($attributes, ['required', 'data-required']);


CRITICAL: Layout XML referenceContainer: Handler modals MUST use before.body.end container

✅ Correct: <referenceContainer name="before.body.end">
❌ Incorrect: <referenceContainer name="content">
The before.body.end container ensures the handler modal is loaded at the end of the page body, which is required for proper Alpine.js initialization and modal functionality

CRITICAL: Field Value Type Handling: NEVER use type casting for field values, always use null coalescing operator

✅ Correct: $fieldValue = $block->getData('value') ?? '';
❌ Incorrect: $fieldValue = (string) $block->getData('value');
Type casting (string) will fail when value is null, causing PHP errors
Use ?? '' for string values, ?? [] for array values, or appropriate default for your data type
Reference: See built-in field types like category.phtml which use ?? [] pattern
CRITICAL: Dialog Modal Classes: Handler modals must use open:flex not static flex class
✅ Correct: <dialog class="... open:flex flex-col">
❌ Incorrect: <dialog class="... flex flex-col"> (modal always visible)
The open: prefix applies styles only when dialog is open (native HTML dialog state)
Reference: See built-in handlers like category-handler.phtml which use open:flex flex-col
CRITICAL: Complex Data Type Handling: For fields storing JSON/array data, handle BOTH array and string types
Field values may be returned as already-decoded arrays OR as JSON strings (depends on storage/context)
✅ Correct pattern:
$data = ['default' => 'structure'];
if ($fieldValue) {
    if (is_array($fieldValue)) {
        $data = $fieldValue;  // Already decoded
    } elseif (is_string($fieldValue)) {
        $decoded = json_decode($fieldValue, true);
        if (is_array($decoded)) {
            $data = $decoded;
        }
    }
}

// When outputting to hidden input, ALWAYS ensure it's a JSON string
$fieldValueJson = is_array($fieldValue) ? json_encode($fieldValue) : $fieldValue;

❌ Incorrect: json_decode($fieldValue) without type checking (fails if value is already an array)
❌ Incorrect: Using array directly in value attribute without JSON-encoding first
Weekly Installs
287
Repository
hyva-themes/hyv…ai-tools
GitHub Stars
65
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass