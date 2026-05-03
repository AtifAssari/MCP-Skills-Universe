---
title: n8n-workflows-master
url: https://skills.sh/skezu/skills/n8n-workflows-master
---

# n8n-workflows-master

skills/skezu/skills/n8n-workflows-master
n8n-workflows-master
Installation
$ npx skills add https://github.com/skezu/skills --skill n8n-workflows-master
SKILL.md
n8n Automation Workflows Skill

This skill allows you to act as a workflow engineer, QA specialist, and security architect to build high-quality n8n automations.

Core Capabilities
1. Build Captain (Orchestrator)

Use this role to build full n8n workflows from a plain-language spec. It produces valid, import-ready JSON, READMEs, and sample payloads.

Reference: n8n_Build_Captain.md

2. QA & Compliance

Use this role to validate JSON importability, node conventions, error handling, and adherence to n8n best practices. It returns targeted JSON patches and test plans.

Reference: n8n_QA_Compliance.md

3. Security Architect

Use this role to identify risks in workflow design (auth, PII, DoS, SSRF, etc.) and suggest hardening measures.

Reference: n8n_Security_Architect.md

Usage

When the user asks for a new n8n workflow:

Read references/n8n_Build_Captain.md to understand the creation standards.
Generate the workflow JSON and README based on the user's requirements.
(Optional but recommended) Self-correct using the principles in references/n8n_QA_Compliance.md and references/n8n_Security_Architect.md.
Assets
Sample Workflow: assets/samples/n8n-sample.json - A canonical reference export for n8n workflows.
Weekly Installs
12
Repository
skezu/skills
First Seen
Feb 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass