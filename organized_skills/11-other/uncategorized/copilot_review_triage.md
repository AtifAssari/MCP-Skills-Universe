---
rating: ⭐⭐
title: copilot-review-triage
url: https://skills.sh/ma233/copilot-review/copilot-review-triage
---

# copilot-review-triage

skills/ma233/copilot-review/copilot-review-triage
copilot-review-triage
Installation
$ npx skills add https://github.com/ma233/copilot-review --skill copilot-review-triage
SKILL.md
Copilot Review Triage

Use the bundled script. Do not rebuild the gh calls manually.

Resolve scripts from this skill directory. Use templates/triage_prompt.md.

SKILL_ROOT="<absolute-path-to-this-skill>"
SCRIPT="$SKILL_ROOT/scripts/get_latest_copilot_review.sh"
"$SCRIPT" [--branch <name>] [--repo <owner/repo>]

TRIAGE_TEMPLATE="$SKILL_ROOT/templates/triage_prompt.md"


This skill is for action, not display.

Rules:

Run scripts/get_latest_copilot_review.sh.
Use templates/triage_prompt.md.
Classify each comment as apply, verify, or ignore.
Implement apply items if the user asked for improvements.
Reply with a short summary of applied, verified, and ignored items.
Do not dump raw JSON unless the user explicitly asks for it.
Paraphrase comments briefly instead of quoting them.
Merge duplicate comments into one decision.
Reject comments that are stale, incorrect, or too weak to justify a code change.
Do not describe unsupported colon forms such as $copilot-review:triage.
Weekly Installs
9
Repository
ma233/copilot-review
First Seen
4 days ago
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn