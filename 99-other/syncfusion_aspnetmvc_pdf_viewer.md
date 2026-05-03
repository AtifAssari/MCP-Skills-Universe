---
title: syncfusion-aspnetmvc-pdf-viewer
url: https://skills.sh/syncfusion/pdf-viewer-sdk-skills/syncfusion-aspnetmvc-pdf-viewer
---

# syncfusion-aspnetmvc-pdf-viewer

skills/syncfusion/pdf-viewer-sdk-skills/syncfusion-aspnetmvc-pdf-viewer
syncfusion-aspnetmvc-pdf-viewer
Installation
$ npx skills add https://github.com/syncfusion/pdf-viewer-sdk-skills --skill syncfusion-aspnetmvc-pdf-viewer
SKILL.md
Syncfusion ASP.NET MVC Pdfviewer – UI Sample Generator
Generate Code for the User's Project (default)

Trigger keywords: "how to", "add pdfviewer", "code sample", "show me", "example", "snippet", "integrate", "component", "create sample", "ASP.NET MVC sample".

Purpose: Generate minimal, copy-pasteable Razor + HTML code (.cshtml) that the user can integrate directly into their ASP.NET MVC project.

Workflow: ⚠️ CRITICAL — Feature Support Policy (STRICT MODE):

FUNDAMENTAL RULE: Only generate code using APIs and properties that are EXPLICITLY listed in the reference files. ANY deviation is a VIOLATION.

MANDATORY CHECKS BEFORE GENERATING ANY CODE:

Search the reference files for the exact API/property name
Verify it appears in the Method Reference, Properties, or Events tables
If NOT found in ANY reference file, STOP immediately
Do NOT generate or suggest undocumented APIs under any circumstances

STRICT ENFORCEMENT - ZERO TOLERANCE:

NO custom properties - Only use properties from reference file tables
NO invented methods - Only use methods from reference file tables
NO workarounds with undefined APIs - Forbidden
NO assumptions about undocumented behavior - Forbidden
NO alternative implementations using guess-work - Forbidden
NO pretending support exists - Forbidden

MANDATORY RESPONSE FOR UNSUPPORTED FEATURES:

If a requested scenario/feature/API is NOT listed in any reference file, you MUST respond with:
"This feature is not supported in the current Syncfusion ASP.NET MVC PDF Viewer implementation."

Then list what IS supported from the appropriate reference file
Never suggest alternatives unless explicitly documented in reference files

REFERENCE FILE HIERARCHY:

Each reference file contains complete, authoritative documentation for its domain
The tables (Method Reference, Properties, Events) are the SOURCE OF TRUTH
Content outside these tables in reference files is explanatory only
Do NOT extend beyond what appears in the reference file tables

AUDIT YOUR GENERATION:

Before providing any code, verify EVERY API used appears in a reference file table
Document which reference file each API comes from
If you cannot cite a reference file table entry, DELETE that code

This is a CRITICAL REQUIREMENT. Violations compromise the skill's integrity and reliability.

Step 1 — Generate Code from Reference Files Only (REQUIRED)
Read the relevant references/*.md file(s) for the requested feature
Cross-reference EVERY API, property, and method against these tables
MANDATORY: Before generating ANY code, verify that reference files exist and are accessible
Read the appropriate reference file(s) for the requested feature:
Use read_file tool on relevant references/*.md files
Confirm file contains Methods/Properties/Events tables
Verify tables are complete and readable
If reference file is missing or cannot be read:
STOP code generation
Respond: "Reference file for this feature is not available. Please ensure all reference files are present in the references/ directory."
List the missing reference file name
This is a BLOCKER step: Cannot proceed without reference file validation
If an API/property does NOT appear in the reference file table, DO NOT USE IT
Do NOT invent, guess, or suggest any API, method, property, class, or namespace not explicitly present in the reference files
⚙️ SETTINGS CONFIGURATION BEST PRACTICES

When generating code with settings (toolbarSettings, annotationSettings, annotationSelectorSettings, arrowSettings, rectangleSettings, etc.), follow these guidelines to prevent unnecessary imports and over-engineering:

Rule 1: Simple Settings → Define as Razor inline code

Use this approach when:

Configuring only 1-3 properties
Settings are straightforward without custom types

Example (DO THIS):

@Html.EJS().PdfViewer("pdfviewer").AnnotationSelectorSettings(new Syncfusion.EJ2.PdfViewer.PdfViewerAnnotationSelectorSettings { ResizerBorderColor = "green", SelectionBorderColor = "blue", ResizerFillColor = "#4070ff", resizerSize = 8, SelectionBorderThickness = 1, SelectorLineDashArray = new int[] { 5, 6 }, ResizerLocation = "Corners|Edges", ResizerCursorType = "grab" }).Render()


Benefits:

✅ Simple and readable
✅ Less code clutter
✅ Type checking still works
Rule 2: Complex Settings → Define as Razor code blocks outside HTML

Use this approach when:

Configuring 4+ properties OR multiple related settings
Using enums or complex configurations
Need to reuse the same configuration across multiple components
Settings are complex enough to warrant separate definition

Example (DO THIS ONLY FOR COMPLEX CASES):

@{
    var annotationSelectorSettings = new {
        selectionBorderColor = "blue",
        resizerBorderColor = "red",
        resizerFillColor = "#4070ff",
        resizerSize = 8,
        selectionBorderThickness = 1,
        resizerShape = "Circle",
        selectorLineDashArray = new int[] { 5, 6 },
        resizerLocation = "Corners|Edges",
        resizerCursorType = "grab"
    };
}
@Html.EJS().PdfViewer("pdfviewer").AnnotationSelectorSettings(annotationSelectorSettings).Render()

Rule 3: NEVER Over-Engineer Simple Cases

❌ DO NOT DO THIS (Over-engineered):

@{
    var toolbarSettings = new Syncfusion.EJ2.PdfViewer.PdfViewerToolbarSettings  { ShowTooltip = true };
}
@Html.EJS().PdfViewer("pdfviewer").ToolbarSettings(@toolbarSettings).Render()


✅ DO THIS INSTEAD (Simple & Clean):

@Html.EJS().PdfViewer("pdfviewer").ToolbarSettings(new Syncfusion.EJ2.PdfViewer.PdfViewerToolbarSettings  { ShowTooltip = true }).Render()

Checklist Before Generating Code
 Count the settings properties: 1-3? → Use inline | 4+? → Use separate razor code block
 Is the component prop simple enough? Yes → Keep inline | No → Extract to separate razor code block
 Are Default values set for properties explicitly? Yes → Remove | No → Keep it
Code References

All templates and operation snippets live in references/*.md. Each file is a focused snippet or template the agent will combine when generating samples.

Flow: Always start with references/basic-sample.md, then merge matched features into its anchors (PROPS, EVENTS, UI_BUTTONS, HANDLERS). If no keyword matches, return only the basic sample.

Reference File Routing Guide
🎯 MVC Setup & Configuration
File	Purpose
references/basic-sample.md	Minimal PDF Viewer with documentPath, height, and width. Base template for all samples.
references/enable-properties.md	Enable/disable specific features (toolbar, annotations, forms, navigation, text selection, download, print).
references/general-properties.md	Configure core viewer properties and behavior (documentPath, width/height, locale, zoom/initialRenderPages), server/integration settings (serviceUrl, ajaxRequestSettings, serverActionSettings), resource loading (resourceUrl, customFonts), and performance/retry options.
Context Menu
File	Purpose
references/contextmenu.md	Context-aware context menu for text, annotations, and form fields; add custom items via addCustomMenu, handle clicks with customContextMenuSelect, dynamically show/hide items with customContextMenuBeforeOpen, and disable the menu using contextMenuOption. Configure default context menu using context menu settings.
Navigation Features
File	Purpose
references/navigation.md	Enable/disable page navigation (first/last/previous/next/go to page), thumbnail view and navigation, hyperlink support (internal and external links), table of contents navigation, programmatic navigation methods, and navigation-related events.
references/bookmark-navigation.md	Enable/disable and show/hide bookmark navigation. Programmatically retrieve bookmarks for a document
MVC Viewing and Interaction
File	Purpose
references/viewing-and-interaction.md	Understand interaction modes (Text Selection/Pan), page scrolling & viewing behavior, panning operations, feature modules for modular architecture, enabling/disabling specific viewing features, and MVC viewing capabilities.
references/magnification.md	Configure zoom levels & zoom percentages, zoom modes (fit to page/fit to width/fit to visible area/automatic), custom zoom control, programmatic zoom operations, zoom toolbar configuration, and mouse wheel zoom behavior.
Toolbar Configuration
File	Purpose
references/toolbar-customization.md	Customize the PDF viewer primary, form designer, annotation toolbars. Programmatically enable/disable toolbar, enable/disable and show/hide toolbar items. Lists the toolbar items available for toolbars. Enable/disable form designer, annotation or primary toolbars during initialization. Create a custom toolbar item
references/toolbar-reference.md	Use the toolbar API methods/properties to show/hide the primary/annotation/navigation/redaction toolbars.
references/toolbar-customization-scenarios.md	Common toolbar customization scenarios
Annotations and Markup
File	Purpose
references/annotation-overview.md	Information about ink/freehand, sticky notes/comments, handwritten/digital signatures annotations and programmatically adding them. Overall annotation types and common default annotation settings example
references/text-markup-annotations.md	Programmatically add text markup annotations (Highlight, underline, strikethrough, squiggly). Manipulate default settings for each textmarkup annotations
references/shape-annotations.md	Information on shape annotations (Line, Arrow, Rectangle, Circle, Polygon). Programmatically adding shape annotations and manipulating default shape settings for each shape annotations
references/measurement-annotations.md	Information on measurement annotations (Distance, Perimeter, Area, Radius, Volume). Programmatically adding measurement annotations and manipulating default settings for each measurement annotations
references/stamp-annotation.md	Information on stamp annotations and different types of stamps available. Programmatically adding stamp annotations
references/free-text-annotations.md	Information on free text annotation. Programmatically adding free text annotations
references/annotation-settings.md	Configure appearance (colors, opacity, borders, styles) and behavior (restrictions, locking, printing) for all annotation types. Apply settings globally or per annotation type. Customize annotation selector (resizer, selection border). Set author, subject, and custom data. Control annotation-related component properties (toolbar visibility, signature settings, export options, drawing constraints).
references/annotation-events.md	Handle annotation lifecycle events (add, delete, move, resize, select, property change).
references/annotation-operations.md	Programmatically manipulate annotations like selection, moving and resizing, deleting, locking and importing and exporting annotations
references/annotation-use-cases.md	Common scenarios on how annotations can be programmatically manipulated
references/shape-label-settings.md	Configure shape and measure annotation label appearance (fill color, font, font size, opacity) and default content (label text, notes).
references/redaction-annotation.md	Hide and permanently remove sensitive information in PDFs. Mark content by area or full page, configure overlay text and styling, apply redactions irreversibly, search text and auto-redact, and manage redaction annotations programmatically.
Forms Management
File	Purpose
references/form-fields-overview.md	Fill and design PDF forms, manage form fields (field types like textbox/password/checkbox/radio/dropdown/listbox/signature), create fields programmatically, use the form designer toolbar/UI interactions, configure field properties/customization, apply validation rules and constraints/settings, use form field API methods, and handle import/export form data including custom field data.
references/supported-form-fields.md	Supported form field types and programmatically add each
references/form-fields-props.md	Lists properties of form fields. Lists common properties and specific properties to each field. Manipulate form field settings
references/import-export-form-data.md	Programmatically import and export form field data
references/form-operations.md	Programmatically manipulate form fields including updating properties and values, moving and resizing, deleting, grouping, adding custom data & retrieving form field data
references/form-field-validation.md	Enable/disable form field validation. Programmatic flow of form field validation and examples
references/form-field-settings.md	Configure default properties for form fields (text, checkbox, radio, dropdown, signature).
references/form-field-events.md	Handle form field interaction events (focus, blur, value change, validation).
Text Operations
File	Purpose
references/text-search.md	Implement text search in PDFs: search functionality, search options (case-sensitive/whole word), highlight search results, find next/previous occurrences, programmatic text search methods, search completion events, and custom highlight colors. Configure text extraction options/settings and programmatically extract text from pages.
references/text-selection.md	Enable text selection and text extraction: selection modes/behavior, copy selected text, text selection events, programmatic selection and text collections/bounds.
Document Operations
File	Purpose
references/opening-pdfs.md	Load PDFs from URL/local paths/base64, open encrypted/password-protected PDFs, support programmatic document loading, handle document load events/lifecycle, and manage load failures/errors.
references/saving-and-downloading.md	Download PDFs, save PDFs with annotations/modifications, download with form data included, retrieve PDFs as base64, customize download events, and set custom download filenames.
references/printing-and-organizing.md	Print PDFs (including print options like page range/quality and silent printing), handle print events, organize pages (overview/rearrange/reorder/rotate/delete), copy/duplicate/extract pages to a new document, and use the page organizer toolbar with programmatic + mobile page organization.
⚙️ Advanced Features
File	Purpose	Route When User Asks About
references/api-methods.md	Programmatic control: load documents, manage forms, annotations, extract text, undo/redo, navigation APIs.	"load PDF programmatically", "API methods", "export form data", "extract text", "undo/redo", "programmatic control"
references/events.md	Complete list of all PDFViewer events (document load, download, annotations, forms, search, navigation).	"event list", "all events", "available events", "event reference", "event handlers"
Weekly Installs
10
Repository
syncfusion/pdf-…k-skills
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass