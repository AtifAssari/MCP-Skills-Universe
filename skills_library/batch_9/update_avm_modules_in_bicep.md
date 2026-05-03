---
title: update-avm-modules-in-bicep
url: https://skills.sh/github/awesome-copilot/update-avm-modules-in-bicep
---

# update-avm-modules-in-bicep

skills/github/awesome-copilot/update-avm-modules-in-bicep
update-avm-modules-in-bicep
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill update-avm-modules-in-bicep
Summary

Automated Azure Verified Module version updates for Bicep files with breaking change detection.

Scans Bicep files to extract AVM module references, queries MCR for latest versions, and applies updates automatically
Pauses for manual approval when breaking changes, security modifications, or parameter incompatibilities are detected
Validates all changes with bicep lint and bicep build to ensure compliance before finalizing
Outputs results in a structured table showing module names, version changes, status, and documentation links
SKILL.md
Update Azure Verified Modules in Bicep Files

Update Bicep file ${file} to use latest Azure Verified Module (AVM) versions. Limit progress updates to non-breaking changes. Don't output information other than the final output table and summary.

Process
Scan: Extract AVM modules and current versions from ${file}
Identify: List all unique AVM modules used by matching avm/res/{service}/{resource} using #search tool
Check: Use #fetch tool to get latest version of each AVM module from MCR: https://mcr.microsoft.com/v2/bicep/avm/res/{service}/{resource}/tags/list
Compare: Parse semantic versions to identify AVM modules needing update
Review: For breaking changes, use #fetch tool to get docs from: https://github.com/Azure/bicep-registry-modules/tree/main/avm/res/{service}/{resource}
Update: Apply version updates and parameter changes using #editFiles tool
Validate: Run bicep lint and bicep build using #runCommands tool to ensure compliance.
Output: Summarize changes in a table format with summary of updates below.
Tool Usage

Always use tools #search, #searchResults,#fetch, #editFiles, #runCommands, #todos if available. Avoid writing code to perform tasks.

Breaking Change Policy

⚠️ PAUSE for approval if updates involve:

Incompatible parameter changes
Security/compliance modifications
Behavioral changes
Output Format

Only display results in table with icons:

| Module | Current | Latest | Status | Action | Docs |
|--------|---------|--------|--------|--------|------|
| avm/res/compute/vm | 0.1.0 | 0.2.0 | 🔄 | Updated | [📖](link) |
| avm/res/storage/account | 0.3.0 | 0.3.0 | ✅ | Current | [📖](link) |

### Summary of Updates

Describe updates made, any manual reviews needed or issues encountered.

Icons
🔄 Updated
✅ Current
⚠️ Manual review required
❌ Failed
📖 Documentation
Requirements
Use MCR tags API only for version discovery
Parse JSON tags array and sort by semantic versioning
Maintain Bicep file validity and linting compliance
Weekly Installs
8.3K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn