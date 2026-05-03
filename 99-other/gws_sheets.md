---
rating: ⭐⭐⭐
title: gws-sheets
url: https://skills.sh/googleworkspace/cli/gws-sheets
---

# gws-sheets

skills/googleworkspace/cli/gws-sheets
gws-sheets
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-sheets
Summary

Read, write, and batch-update Google Sheets with direct API access.

Supports three helper commands: +read for retrieving values, +append for adding rows, and batchUpdate for applying multiple validated changes atomically
Access spreadsheets resource with methods to create, retrieve, and modify sheets, including grid data filtering and developer metadata operations
Requires Google Workspace authentication via the shared gws prerequisite; use gws schema to inspect method parameters before building requests
Batch operations validate all requests before applying; if any request fails, the entire batch is rejected with no partial changes
SKILL.md
sheets (v4)

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

gws sheets <resource> <method> [flags]

Helper Commands
Command	Description
+append	Append a row to a spreadsheet
+read	Read values from a spreadsheet
API Resources
spreadsheets
batchUpdate — Applies one or more updates to the spreadsheet. Each request is validated before being applied. If any request is not valid then the entire request will fail and nothing will be applied. Some requests have replies to give you some information about how they are applied. The replies will mirror the requests. For example, if you applied 4 updates and the 3rd one had a reply, then the response will have 2 empty replies, the actual reply, and another empty reply, in that order.
create — Creates a spreadsheet, returning the newly created spreadsheet.
get — Returns the spreadsheet at the given ID. The caller must specify the spreadsheet ID. By default, data within grids is not returned. You can include grid data in one of 2 ways: * Specify a field mask listing your desired fields using the fields URL parameter in HTTP * Set the includeGridData URL parameter to true.
getByDataFilter — Returns the spreadsheet at the given ID. The caller must specify the spreadsheet ID. For more information, see Read, write, and search metadata. This method differs from GetSpreadsheet in that it allows selecting which subsets of spreadsheet data to return by specifying a dataFilters parameter. Multiple DataFilters can be specified.
developerMetadata — Operations on the 'developerMetadata' resource
sheets — Operations on the 'sheets' resource
values — Operations on the 'values' resource
Discovering Commands

Before calling any API method, inspect it:

# Browse resources and methods
gws sheets --help

# Inspect a method's required params, types, and defaults
gws schema sheets.<resource>.<method>


Use gws schema output to build your --params and --json flags.

Weekly Installs
22.2K
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