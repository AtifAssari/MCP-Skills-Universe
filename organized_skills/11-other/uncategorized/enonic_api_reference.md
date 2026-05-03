---
rating: ⭐⭐
title: enonic-api-reference
url: https://skills.sh/webmaxru/enonic-agent-skills/enonic-api-reference
---

# enonic-api-reference

skills/webmaxru/enonic-agent-skills/enonic-api-reference
enonic-api-reference
Installation
$ npx skills add https://github.com/webmaxru/enonic-agent-skills --skill enonic-api-reference
SKILL.md
Enonic XP Server-Side API Reference
Procedures

Step 1: Identify the Target Library

Determine which /lib/xp/* library the query relates to.

Map the library to the appropriate reference file:

Library	Reference File
lib-content	references/lib-content-reference.md
lib-node	references/lib-node-reference.md
lib-auth	references/lib-auth-reference.md
lib-portal	references/lib-portal-reference.md
lib-context, lib-event, lib-task	references/lib-context-reference.md
lib-io, lib-mail, lib-repo, lib-schema	references/lib-utilities-reference.md

If the query spans multiple libraries or asks for a usage pattern, read references/examples.md.

Step 2: Look Up the Function

Read the identified reference file.
Locate the specific function by name.
Extract the following details:
Signature: Function name and import path.
Parameters: Name, type, required/optional, default value, description.
Return type: Type and shape of the returned value.
Example: Code snippet demonstrating correct usage.

Step 3: Provide the Answer

Present the function signature with its import statement.
Include the parameter table with types and descriptions.
Include the return type and shape.
Add a usage example. If the reference file includes one, use it. Otherwise, compose a minimal working example consistent with the documented signature.
Note any version requirements (e.g., "Requires XP 7.8.0+").

Step 4: Handle Cross-Library Patterns

If the query involves combining multiple libraries (e.g., "create content as admin"), read references/examples.md for established patterns.
If a pattern is not documented, compose it by combining individual function signatures from the relevant reference files.

Step 5: Troubleshoot Common Issues

If the query describes an error or unexpected behavior, read references/troubleshooting.md.
Match the error message or symptom to a known issue.
Provide the documented fix and any version-compatibility notes.

Step 6: Generate Import Blocks

If the user needs a reusable import block, read assets/enonic-imports.template.ts.
Uncomment only the libraries required for the user's controller.
Error Handling
If a function is not found in any reference file, report that it may belong to a community library or a newer XP version not yet documented, and suggest checking https://developer.enonic.com/docs/xp/stable/api.
If the query relates to Guillotine/GraphQL, content type schemas, or Enonic CLI, indicate that this skill does not cover those topics.
If a version mismatch is suspected, consult the version compatibility table in references/troubleshooting.md.
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