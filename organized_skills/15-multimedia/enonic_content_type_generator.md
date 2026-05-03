---
rating: ⭐⭐
title: enonic-content-type-generator
url: https://skills.sh/webmaxru/enonic-agent-skills/enonic-content-type-generator
---

# enonic-content-type-generator

skills/webmaxru/enonic-agent-skills/enonic-content-type-generator
enonic-content-type-generator
Installation
$ npx skills add https://github.com/webmaxru/enonic-agent-skills --skill enonic-content-type-generator
SKILL.md
Enonic XP Content Type Generator
Procedures

Step 1: Detect Enonic XP Project

Execute node scripts/find-enonic-targets.mjs [workspaceRoot] to locate Enonic XP project roots.
If the script returns an empty array, warn that no Enonic XP project markers were found and ask for the target directory.
Store the detected project root for use in subsequent steps.

Step 2: Gather Requirements

Identify the content type name from the request. The name must be lowercase-hyphenated (e.g., blog-post).
Identify the display name — a human-readable label (e.g., Blog Post).
Determine the super-type. Default to base:structured unless the request specifies a folder (base:folder) or another built-in type.
List all requested fields with their input types. Read references/content-type-reference.md to map natural-language field descriptions to the correct Enonic XP input type and configuration.
Identify any item sets (repeatable grouped fields), option sets (single-select or multi-select choices), or mixin references.
If the request mentions a mixin, determine whether to generate the mixin file or reference an existing one.
If the request mentions x-data, determine whether to generate the x-data file or reference an existing one.

Step 3: Generate the Content Type XML

Read assets/content-type.template.xml to obtain the starter template.
Replace DISPLAY_NAME with the display name from Step 2.
Replace DESCRIPTION with a short description or remove the element if none was provided.
Set the <super-type> element to the value determined in Step 2.
Populate the <form> element with the identified inputs, item sets, option sets, field sets, and mixin references.
For each input:
Set the name attribute using camelCase.
Set the type attribute to the exact Enonic XP input type name (case-sensitive).
Add <label>, <occurrences>, <help-text>, <default>, and <config> as required.
For ComboBox and RadioButton inputs, include all options inside <config>.
For ContentSelector, ImageSelector, and MediaSelector inputs, include <config> with allowContentType, allowPath, treeMode, and hideToggleIcon as specified.
For TextLine and TextArea, add <config> with max-length, show-counter, or regexp if validation constraints are requested.
For Long and Double, add <config> with min and max if range constraints are requested.
For DateTime, add <config> with <timezone>true</timezone> if timezone-aware storage is requested.
If examples are needed for reference, read references/examples.md.

Step 4: Write the File

Construct the target path: [projectRoot]/src/main/resources/site/content-types/[name]/[name].xml
Create the directory if it does not exist.
Write the generated XML to the file.
If a mixin was generated, write it to: [projectRoot]/src/main/resources/site/mixins/[name]/[name].xml
If x-data was generated, write it to: [projectRoot]/src/main/resources/site/x-data/[name]/[name].xml

Step 5: Validate Output

Verify the generated XML is well-formed.
Confirm every <input> has a valid type attribute by cross-referencing references/content-type-reference.md.
Confirm all name attributes are unique within their nesting level.
Confirm <occurrences> values are logically consistent (minimum <= maximum, or maximum = 0 for unlimited).
If the request asks about super-types, input types, or schema structure without requesting file generation, answer the question using references/content-type-reference.md without creating files.
Error Handling
If scripts/find-enonic-targets.mjs exits with a non-zero code, report the stderr message and ask for the project root path manually.
If the requested input type does not match any known Enonic XP input type, read references/content-type-reference.md and suggest the closest match. Do not invent input type names.
If XML validation fails, read references/troubleshooting.md to diagnose and correct the error, then regenerate the file.
If a mixin reference cannot be resolved, confirm the mixin file path exists before writing the content type.
Weekly Installs
80
Repository
webmaxru/enonic…t-skills
First Seen
Mar 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass