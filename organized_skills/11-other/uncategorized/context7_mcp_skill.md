---
rating: ⭐⭐
title: context7-mcp-skill
url: https://skills.sh/holon-run/uxc/context7-mcp-skill
---

# context7-mcp-skill

skills/holon-run/uxc/context7-mcp-skill
context7-mcp-skill
Installation
$ npx skills add https://github.com/holon-run/uxc --skill context7-mcp-skill
SKILL.md
Context7 Skill

Use this skill to query library documentation and code examples.

Prerequisites
uxc skill is installed (see uxc skill for installation)
Network access to https://mcp.context7.com/mcp
Core Workflow

Use fixed link command by default:

command -v context7-mcp-cli
If missing, create it: uxc link context7-mcp-cli mcp.context7.com/mcp
context7-mcp-cli -h
If command conflict is detected and cannot be safely reused, stop and ask skill maintainers to pick a different fixed command name.

Resolve a library name to get library ID:

context7-mcp-cli resolve-library-id libraryName=react query='useState hook'

Query documentation:

context7-mcp-cli query-docs libraryId=/reactjs/react.dev query='how to use useState'
Available Tools
resolve-library-id: Resolve a package/library name to Context7 library ID
query-docs: Query documentation and code examples for a specific library
Usage Examples
Find React documentation
# First resolve the library
context7-mcp-cli resolve-library-id libraryName=react query='React useState hook'

Query specific documentation
context7-mcp-cli query-docs '{"libraryId":"/reactjs/react.dev","query":"how to use useEffect"}'

Query Node.js documentation
context7-mcp-cli resolve-library-id libraryName=node query='file system'

Notes
Requires library name first, then use the returned libraryId for queries
Context7 provides version-specific, up-to-date documentation
Supports npm packages, Python libraries, and more
context7-mcp-cli <operation> ... is equivalent to uxc mcp.context7.com/mcp <operation> ....
If link setup is temporarily unavailable, use direct uxc mcp.context7.com/mcp ... calls as fallback.
Reference Files
Workflow details: references/usage-patterns.md
Weekly Installs
26
Repository
holon-run/uxc
GitHub Stars
106
First Seen
Mar 9, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn