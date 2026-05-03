---
rating: ⭐⭐⭐
title: update-changelog
url: https://skills.sh/nweii/agent-stuff/update-changelog
---

# update-changelog

skills/nweii/agent-stuff/update-changelog
update-changelog
Installation
$ npx skills add https://github.com/nweii/agent-stuff --skill update-changelog
SKILL.md
Update Changelog

Update changelog files following Keep a Changelog conventions.

Usage
/update-changelog <version> <change_type> <message>
/update-changelog <skill_path> <version> <change_type> <message>

Parameters
<version>: Version number (e.g., "1.1.0")
<change_type>: One of: "added", "changed", "deprecated", "removed", "fixed", "security"
<message>: Description of the change
<skill_path> (optional): Path to skill folder for skill changelogs
Process
Check for existing changelog (CHANGELOG.md or changelog.md), create if missing
Find or create section for the specified version with today's date
Add the new entry under the appropriate change type heading
Format according to Keep a Changelog conventions
Write the updated changelog back to file
Format Conventions
Group changes by type (Added, Changed, Deprecated, Removed, Fixed, Security)
List changes as bullet points
Include date for version sections (YYYY-MM-DD)
Keep entries concise but descriptive
No emojis
Example Output
## [1.2.0] - 2025-01-24

### Added
- New markdown to BlockDoc conversion feature

### Fixed
- Bug in HTML renderer causing incorrect output

Skill & Plugin Changelogs

For skill-specific conventions (updating metadata.version in SKILL.md) or plugin changelog formats, see skill-plugin-conventions.md.

Weekly Installs
23
Repository
nweii/agent-stuff
GitHub Stars
2
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass