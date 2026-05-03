---
rating: ⭐⭐
title: status-page-generator
url: https://skills.sh/kostja94/marketing-skills/status-page-generator
---

# status-page-generator

skills/kostja94/marketing-skills/status-page-generator
status-page-generator
Installation
$ npx skills add https://github.com/kostja94/marketing-skills --skill status-page-generator
SKILL.md
Pages: Status Page

Guides status page design for communicating service health, uptime, and incidents. Typically at status.* subdomain. Reduces support during outages, builds trust.

When invoking: On first use, if helpful, open with 1–2 sentences on what this skill covers and why it matters, then provide the main output. On subsequent use or when the user asks to skip, go directly to the main output.

Initial Assessment

Check for project context first: If .claude/project-context.md or .cursor/project-context.md exists, read it for product and service components.

Identify:

Service components: API, dashboard, billing, etc.
Monitoring: What tools feed status (PagerDuty, Datadog, etc.)
Audience: Customers, developers, internal
Hosting: Self-hosted vs. third-party (Statuspage, Better Uptime, etc.)
Status Page Structure
Section	Purpose
Overall status	Operational, Degraded, Outage, Maintenance
Components	Per service: status, uptime %
Incidents	Active and past; timeline, updates
Subscribe	Email, SMS, RSS for notifications
Uptime history	90-day or custom range (optional)
Best Practices
Communication
Clear status: Operational, Degraded, Partial Outage, Major Outage
Incident updates: Timely, honest, actionable
Post-mortem: Link to post-incident review when public
Maintenance: Schedule ahead, notify subscribers
Design
Scannable: Status at a glance; green/yellow/red
Mobile: Critical for on-the-go checks
Accessible: Color + text; don't rely on color alone
No login required: Public status, no auth
Technical
Independent hosting: Status page should stay up when main product is down
Subdomain: status.yourdomain.com
Integrations: Slack, PagerDuty, etc. for incident creation
Historical data: Uptime %, incident count
Output Format
Structure (components, incident format)
Status definitions and colors
Incident template (title, updates, resolution)
Subscribe options
Hosting recommendation (self vs. third-party)
Related Skills
docs-page-generator: Link status from docs footer
api-page-generator: Link status for developer trust
footer-generator: Status link in footer
404-page-generator: Status page as utility; similar UX principles
Weekly Installs
512
Repository
kostja94/market…g-skills
GitHub Stars
413
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass