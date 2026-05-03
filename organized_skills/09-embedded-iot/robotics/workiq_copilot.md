---
rating: ⭐⭐
title: workiq-copilot
url: https://skills.sh/github/awesome-copilot/workiq-copilot
---

# workiq-copilot

skills/github/awesome-copilot/workiq-copilot
workiq-copilot
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill workiq-copilot
Summary

Query Microsoft 365 data with natural language to surface emails, meetings, documents, Teams messages, and people insights.

Supports five data sources: emails, meetings, documents, Teams channels, and people/projects with natural-language prompts
Install via Copilot CLI plugin (preferred) or standalone npm package; requires Microsoft 365 tenant admin consent on first use
Core workflow: clarify intent, craft precise prompts with timeframe/source, run workiq ask --question "...", and stream results
Includes MCP server mode (workiq mcp) for exposing WorkIQ tools to other agents and workflows
Best practices emphasize narrow, focused queries, privacy-respecting summaries, and mapping results to actionable follow-ups like blocking time or drafting messages
SKILL.md
WorkIQ Copilot Skill
Overview

WorkIQ (Public Preview) lets Copilot query Microsoft 365 data with natural language. It supports schedules, documents, Teams messages, email threads, follow-up tracking, stakeholder summaries, and more. Use this skill whenever a task needs live organizational intelligence beyond the local repository.

Supported Data & Sample Prompts
Emails – “Summarize emails from Sarah about the budget.”
Meetings – “What are my upcoming meetings this week?”
Documents – “Find recent documents about Q4 planning.”
Teams – “Summarize messages in the Engineering channel today.”
People/Projects – “Who is working on Project Alpha?”
Getting Access
Copilot CLI plugin (preferred)
copilot
/plugin marketplace add github/copilot-plugins
/plugin install workiq@copilot-plugins
Restart Copilot CLI.
Standalone CLI / MCP server
npm install -g @microsoft/workiq (or npx -y @microsoft/workiq mcp).
Run workiq mcp to expose MCP tools if needed.
Tenant consent
First use prompts for Microsoft 365 admin consent (EULA + permissions). Non-admins must contact tenant admin to approve per the Tenant Administrator Enablement Guide.
Pre-flight Checklist
Run Get-Command workiq to ensure the binary is available.
Accept the EULA once via workiq accept-eula.
Confirm the correct tenant (-t <tenant-id> if different from default common).
Be ready to complete device login in the browser when prompted.
Core Workflow
Clarify intent – agenda, action items, document lookup, people search, risk summary, etc.
Craft precise prompt – include timeframe, source, or topic (e.g., “Summarize Teams posts in #eng for today”).
Run command – workiq ask --question "<prompt>" (use -q for shorthand if desired).
Monitor execution – long answers may stream; wait for the response to finish before issuing additional requests.
Summarize & redact – highlight insights, note conflicts/tasks, avoid pasting raw links unless required.
Offer follow-ups – blocking time, drafting notes, deeper queries, etc.
Command Reference
Command	Purpose
workiq --help	Show global options.
workiq version	Display installed version.
workiq accept-eula	Accept license (first use).
workiq ask	Interactive mode.
workiq ask --question "..."	Ask a specific question (use -q shorthand if preferred).
workiq ask -t <tenant> -q "..."	Target a specific tenant.
workiq mcp	Start MCP stdio server (expose WorkIQ tools to other agents).
Prompt Patterns
Agenda: “What’s on my calendar tomorrow?”
Action items: “Summarize follow-ups from today’s customer sync.”
Documents: “List PowerPoints about Contoso FY26 roadmap.”
Communications: “What did my manager say about the deadline?”
Insights: “What blockers came up in the last three meetings?”
Planning: “Suggest focus blocks for Tuesday afternoon.”
Response Guidelines
Keep summaries concise (2–3 sentences) calling out load, priorities, blockers, and optional next steps.
Refer to meetings/documents generically unless the user specifically needs links.
Mention if WorkIQ can continue (e.g., “WorkIQ can show Thu–Sun if needed”).
Map WorkIQ’s suggested actions to clear offers (block time, send follow-up, request recording, run deeper query).
Best Practices
Prefer narrow prompts to reduce noise; run multiple queries if needed.
Combine outputs logically (agenda + conflicts + action items) before responding.
Respect privacy: do not expose attendee lists or confidential snippets unless explicitly requested.
Log which commands were run so future steps can reference them (“Asked WorkIQ for agenda + conflicts”).
Use MCP mode (workiq mcp) when another agent/workflow needs direct tool access.
Troubleshooting
Missing CLI – install via npm or ensure PATH is set; notify user if unavailable.
Consent/auth errors – re-run command after admin grants permissions or after completing device login.
Long/incomplete output – rerun with refined scope or ask for specific data slices (per day/project/person).
Command hanging – cancel the running command in your terminal (for example, with Ctrl+C) or restart the Copilot CLI session, then retry; ensure browser login completed.
Follow-up Actions to Offer
Block focus/overflow holds at suggested times.
Draft reschedule/decline messages referencing WorkIQ guidance.
Request recordings or summaries for overlapping sessions.
Capture action items into task trackers.
Run additional WorkIQ queries (by project, stakeholder, time range) for deeper analysis.
Weekly Installs
8.5K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass