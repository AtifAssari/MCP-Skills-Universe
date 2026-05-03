---
title: hr-onboarding
url: https://skills.sh/nexu-io/open-design/hr-onboarding
---

# hr-onboarding

skills/nexu-io/open-design/hr-onboarding
hr-onboarding
Installation
$ npx skills add https://github.com/nexu-io/open-design --skill hr-onboarding
SKILL.md
HR Onboarding Skill

Produce a single-screen onboarding plan in HTML.

Workflow
Read the active DESIGN.md.
Identify the role + tenure expectations from the brief. Default to a 30/60/90-day shape if unspecified.
Layout:
Cover banner: name placeholder, role, start date, manager + buddy.
"Day 1" panel with the literal schedule (kickoff time, lunch, 1:1 slot).
First-week timeline (Mon → Fri, two activities per day).
30 / 60 / 90 day milestone cards with three concrete outcomes each.
Resource list: handbook, Slack channels, key dashboards, payroll setup.
"You're set when…" checklist — five outcomes with checkboxes.
Single inline <style>, semantic HTML.
Output contract
<artifact identifier="onboarding-plan" type="text/html" title="Onboarding Plan">
<!doctype html>...</artifact>

Weekly Installs
65
Repository
nexu-io/open-design
GitHub Stars
14.2K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass