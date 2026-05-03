---
rating: ⭐⭐⭐⭐⭐
title: sf-diagram-mermaid
url: https://skills.sh/jaganpro/sf-skills/sf-diagram-mermaid
---

# sf-diagram-mermaid

skills/jaganpro/sf-skills/sf-diagram-mermaid
sf-diagram-mermaid
Installation
$ npx skills add https://github.com/jaganpro/sf-skills --skill sf-diagram-mermaid
SKILL.md
sf-diagram-mermaid: Salesforce Diagram Generation

Use this skill when the user needs text-based diagrams: Mermaid diagrams for architecture, OAuth, integration flows, ERDs, or Agentforce structure, plus ASCII fallback when plain-text compatibility matters.

When This Skill Owns the Task

Use sf-diagram-mermaid when the user wants:

Mermaid output
ASCII fallback diagrams
architecture, sequence, flowchart, or ERD views in markdown-friendly form
diagrams that can live directly in docs, READMEs, or issues

Delegate elsewhere when the user wants:

rendered PNG/SVG images or polished mockups → sf-diagram-nanobananapro
non-Salesforce systems only → use a more general diagramming skill
object discovery before an ERD → sf-metadata
Supported Diagram Families
Type	Preferred Mermaid form	Typical use
OAuth / auth flows	sequenceDiagram	Authorization Code, JWT, PKCE, Device Flow
ERD / data model	flowchart LR	object relationships and sharing context
integration sequence	sequenceDiagram	request/response or event choreography
system landscape	flowchart	high-level architecture
role / access hierarchy	flowchart	users, profiles, permissions
Agentforce behavior map	flowchart	agent → topic → action relationships
Required Context to Gather First

Ask for or infer:

diagram type
scope and entities / systems involved
output preference: Mermaid only, ASCII only, or both
whether styling should be minimal, documentation-first, or presentation-friendly
for ERDs: whether org metadata is available for grounding
Recommended Workflow
1. Pick the right diagram structure
use sequenceDiagram for time-ordered interactions
use flowchart LR for ERDs and capability maps
keep a single primary story per diagram when possible
2. Gather data

For ERDs and grounded diagrams:

use sf-metadata when real schema discovery is needed
optionally use the local metadata helper script for counts / relationship context when appropriate
3. Generate Mermaid first

Apply:

accurate labels
simple readable node text
consistent relationship notation
restrained styling that renders cleanly in markdown viewers
4. Add ASCII fallback when useful

Provide an ASCII version when the user wants terminal compatibility or plaintext documentation.

5. Explain the diagram briefly

Call out the key relationships, flow direction, and any assumptions.

High-Signal Rules
For sequence diagrams
use autonumber when step order matters
distinguish requests vs responses clearly
use notes sparingly for protocol detail
For ERDs
prefer flowchart LR
keep object cards simple
use clear relationship arrows
avoid field overload unless the user explicitly asks for field-level detail
color-code object types only when it improves readability
For ASCII output
keep width reasonable
align arrows and boxes consistently
optimize for readability over decoration
Output Format
## <Diagram Title>

### Mermaid Diagram
```mermaid
<diagram>
```

### ASCII Fallback
```text
<ascii>
```

### Notes
- <key point>
- <assumption or limitation>

Cross-Skill Integration
Need	Delegate to	Reason
real object / field definitions	sf-metadata	grounded ERD generation
rendered diagram / image output	sf-diagram-nanobananapro	visual polish beyond Mermaid
connected-app auth setup context	sf-connected-apps	accurate OAuth flows
Agentforce logic visualization	sf-ai-agentscript	source-of-truth behavior details
Flow behavior diagrams	sf-flow	actual Flow logic grounding
Reference Map
Start here
references/diagram-conventions.md
references/mermaid-reference.md
references/usage-examples.md
Styling / ERD specifics
references/mermaid-styling.md
references/color-palette.md
references/erd-conventions.md
Preview
references/preview-guide.md
scripts/mermaid_preview.py
scripts/query-org-metadata.py
Score Guide
Score	Meaning
72–80	production-ready diagram
60–71	clear and useful with minor polish left
48–59	functional but could be clearer
35–47	needs structural improvement
< 35	inaccurate or incomplete
Weekly Installs
1.1K
Repository
jaganpro/sf-skills
GitHub Stars
404
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass