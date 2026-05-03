---
rating: ⭐⭐⭐
title: nomnoml
url: https://skills.sh/knoopx/pi/nomnoml
---

# nomnoml

skills/knoopx/pi/nomnoml
nomnoml
Installation
$ npx skills add https://github.com/knoopx/pi --skill nomnoml
SKILL.md
nomnoml

Convert plain-text descriptions into nomnoml markup and (optionally) render it via CLI.

Primary reference: https://nomnoml.com

Quick start
Minimal diagram
[User]->[AuthService]
[AuthService]->[DB]

Typical class box
[Order|
  +id: UUID;
  +total: Money;
  |
  +addItem(item);
  +checkout();
]

Syntax essentials
Nodes (boxes)
Basic: [A]
With compartments (title | attributes | methods): [A|x; y|do();]
Escape newlines with actual newlines (preferred) or \n when needed.
Relationships (common)
[A]->[B]        # association / dependency
[A]-->[B]       # dotted
[A]-:>[B]       # composition-like (varies by style)
[A]<-[B]        # reverse arrow
[A]-[B]         # line without arrow


If arrow semantics are ambiguous, prefer clear labels:

[API]->[DB]
[API] "reads/writes" -> [DB]

Cardinalities / labels
[Customer] 1->* [Order]
[Order] 1->* [OrderLine]

Grouping
[<frame> Payments|
  [API]
  [Worker]
]

[API]->[Worker]


Common containers:

<frame>: big box grouping
<package>: package-like grouping
<actor>: actor stick figure
Styling / directives

Add directives at the top using #:

#direction: right
#spacing: 40
#ranker: tight-tree

[Client]->[API]


Common directives:

#direction: right|down
#spacing: <number>
#padding: <number>
#ranker: network-simplex|tight-tree|longest-path
Workflow: generate a diagram from a description

Identify the diagram type:

Class/data model → boxes with compartments + inheritance/associations
Architecture/services → frames/packages + arrows + labeled edges
Flow/steps → simple boxes + arrows; keep it readable

Choose names:

Use stable nouns for nodes (AuthService, TokenStore, Frontend).
Keep node names short; put details in compartments or labels.

Produce nomnoml code:

Start with #direction: right for architecture diagrams.
Use frames/packages to group by bounded context.
Add labels for anything non-obvious.

Iterate:

If diagram is too dense, split into multiple diagrams (by subsystem).
Rendering (tool)

If a rendered asset is needed, use the nomnoml tools instead of CLI.

Option A: quick preview

Use the tool to render directly in chat:

nomnoml-display with inline source for a quick preview.
Option B: render to SVG

Use the tool to render and optionally write a file:

nomnoml-render with inline source and optional outputFile.
nomnoml-render-file with inputFile and optional outputFile.

If rendering isn’t required, still produce the .nomnoml source file so it can be rendered later.

Patterns
Architecture sketch (recommended default)
#direction: right

[<actor> User]->[WebApp]

[<frame> Backend|
  [API]
  [Worker]
]

[WebApp]->[API]
[Worker]->[DB]
[API]->[DB]

[DB]

Class diagram with inheritance
[<abstract> Animal|+name: string|+speak()]
[Dog|+breed: string|+speak()]
[Cat|+color: string|+speak()]

[Animal]<:-[Dog]
[Animal]<:-[Cat]

Entity relationship (simple)
#direction: down

[User|id; email]
[Session|id; userId; expiresAt]

[User] 1->* [Session]

When asked to “update an existing diagram”
Preserve existing node names unless there’s a clear rename.
Apply the smallest diff:
add one box/edge at a time
keep direction/ranker consistent
If you change meaning, update edge labels to stay explicit.
Weekly Installs
10
Repository
knoopx/pi
GitHub Stars
45
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass