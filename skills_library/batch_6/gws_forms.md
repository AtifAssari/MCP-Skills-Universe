---
title: gws-forms
url: https://skills.sh/googleworkspace/cli/gws-forms
---

# gws-forms

skills/googleworkspace/cli/gws-forms
gws-forms
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-forms
Summary

Read and write Google Forms through direct API resource commands.

Supports five core operations: create forms, retrieve form data, batch update form structure, manage publish settings, and handle responses and watches
Requires Google Workspace authentication via the shared gws prerequisite; review ../gws-shared/SKILL.md for auth setup and security rules
Use gws schema to inspect method signatures, required parameters, and data types before constructing API calls with --params and --json flags
Form creation requires a two-step process: first call forms.create with title only, then use forms.batchUpdate to add items and configure settings
SKILL.md
forms (v1)

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

gws forms <resource> <method> [flags]

API Resources
forms
batchUpdate — Change the form with a batch of updates.
create — Create a new form using the title given in the provided form message in the request. Important: Only the form.info.title and form.info.document_title fields are copied to the new form. All other fields including the form description, items and settings are disallowed. To create a new form and add items, you must first call forms.create to create an empty form with a title and (optional) document title, and then call forms.update to add the items.
get — Get a form.
setPublishSettings — Updates the publish settings of a form. Legacy forms aren't supported because they don't have the publish_settings field.
responses — Operations on the 'responses' resource
watches — Operations on the 'watches' resource
Discovering Commands

Before calling any API method, inspect it:

# Browse resources and methods
gws forms --help

# Inspect a method's required params, types, and defaults
gws schema forms.<resource>.<method>


Use gws schema output to build your --params and --json flags.

Weekly Installs
14.5K
Repository
googleworkspace/cli
GitHub Stars
25.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn