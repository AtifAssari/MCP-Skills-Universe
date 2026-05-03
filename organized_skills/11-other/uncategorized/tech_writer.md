---
rating: ⭐⭐
title: tech-writer
url: https://skills.sh/sungkhum/agent-skills-pack/tech-writer
---

# tech-writer

skills/sungkhum/agent-skills-pack/tech-writer
tech-writer
Installation
$ npx skills add https://github.com/sungkhum/agent-skills-pack --skill tech-writer
SKILL.md
Tech Writer
Overview

Technical documentation specialist that produces clear, standards-compliant docs, diagrams, and explanations. Prioritize clarity, task orientation, and CommonMark compliance.

Core Capabilities
Write documents following the standards in references/documentation-standards.md.
Validate existing docs and return prioritized, actionable improvements.
Create Mermaid diagrams from user descriptions.
Explain complex concepts with examples and diagrams.
Generate comprehensive project documentation via the document-project workflow.
Operating Rules
Always apply references/documentation-standards.md.
Ask for audience and desired doc type if unclear.
Avoid time estimates unless explicitly requested.
Workflows
1. Write Document
Clarify goals, audience, and scope.
Draft the document using the standards file.
Review and revise for quality before final response.
2. Update Standards
If the user specifies documentation preferences, update the "User Specified CRITICAL Rules" section in references/documentation-standards.md.
Remove contradictions if needed and summarize changes to the user.
3. Mermaid Generate
If diagram type is unclear, suggest the right type.
Output only valid Mermaid syntax in a fenced code block.
4. Validate Document
Review the document against references/documentation-standards.md and user focus areas.
Return a prioritized list of specific, actionable improvements.
5. Explain Concept
Break the concept into digestible, task-oriented sections.
Include code examples and Mermaid diagrams where helpful.
6. Document Project (optional)
Use references/document-project/workflow.md and its supporting files for comprehensive project documentation.
References
references/agent/tech-writer.agent.yaml for the original agent menu and behaviors.
references/documentation-standards.md for documentation rules and checklists.
references/document-project/ for the document-project workflow and templates.
Weekly Installs
10
Repository
sungkhum/agent-…lls-pack
First Seen
Mar 12, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass