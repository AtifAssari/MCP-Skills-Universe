---
title: capture
url: https://skills.sh/camacho/ai-skills/capture
---

# capture

skills/camacho/ai-skills/capture
capture
Installation
$ npx skills add https://github.com/camacho/ai-skills --skill capture
SKILL.md
Inputs
Free-text description of an idea, bug, or feature request
Steps

Parse the description to detect type:

Keywords	Type	Labels
error, crash, broken, fix, bug, fails, regression	Bug	triage, bug
add, want, should, new, feature, enhance, improve	Feature	triage, enhancement
Default	Feature	triage, enhancement

Create GitHub Issue:

gh issue create \
  --title "<concise title from description>" \
  --body "<full description>" \
  --label "triage" --label "<bug or enhancement>"


Return the issue number and URL.

Fallback

If gh is not available or GitHub access fails:

Try GitHub MCP tools (if available)
If neither works → append to ai-workspace/scratchpad.md:
## Captured [date]
**Type**: [bug/feature]
**Description**: [text]
_Failed to create GitHub Issue — saved here as fallback._

Inform the user that the capture was saved locally.
Edge Cases
No description provided → ask the user to describe the idea/bug
Offline / no GitHub access → scratchpad fallback (see above)
Weekly Installs
293
Repository
camacho/ai-skills
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass