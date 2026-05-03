---
rating: ⭐⭐
title: copilot-review-invite
url: https://skills.sh/ma233/copilot-review/copilot-review-invite
---

# copilot-review-invite

skills/ma233/copilot-review/copilot-review-invite
copilot-review-invite
Installation
$ npx skills add https://github.com/ma233/copilot-review --skill copilot-review-invite
SKILL.md
Copilot Review Invite

Use the bundled script. Do not rebuild the gh calls manually.

Resolve the script from this skill directory.

SKILL_ROOT="<absolute-path-to-this-skill>"
SCRIPT="$SKILL_ROOT/scripts/invite_copilot_reviewer.sh"
"$SCRIPT" [--branch <name>] [--repo <owner/repo>]


This skill is for action, not display.

Rules:

Run scripts/invite_copilot_reviewer.sh.
Report that Copilot was invited, including the PR number when available.
Do not claim review comments exist yet unless the user separately asked to fetch them.
Do not describe unsupported colon forms such as $copilot-review:invite.
Keep the reply short and action-oriented.
Weekly Installs
9
Repository
ma233/copilot-review
First Seen
4 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass