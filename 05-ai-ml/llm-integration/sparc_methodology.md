---
title: sparc-methodology
url: https://skills.sh/ruvnet/ruflo/sparc-methodology
---

# sparc-methodology

skills/ruvnet/ruflo/sparc-methodology
sparc-methodology
Installation
$ npx skills add https://github.com/ruvnet/ruflo --skill sparc-methodology
SKILL.md
Sparc Methodology Skill
Purpose

SPARC development workflow: Specification, Pseudocode, Architecture, Refinement, Completion. A structured approach for complex implementations that ensures thorough planning before coding.

When to Trigger
new feature implementation
complex implementations
architectural changes
system redesign
integration work
unclear requirements
When to Skip
simple bug fixes
documentation updates
configuration changes
well-defined small tasks
routine maintenance
Commands
Specification Phase

Define requirements, acceptance criteria, and constraints

npx @claude-flow/cli hooks route --task "specification: [requirements]"


Example:

npx @claude-flow/cli hooks route --task "specification: user authentication with OAuth2, MFA, and session management"

Pseudocode Phase

Write high-level pseudocode for the implementation

npx @claude-flow/cli hooks route --task "pseudocode: [feature]"


Example:

npx @claude-flow/cli hooks route --task "pseudocode: OAuth2 login flow with token refresh"

Architecture Phase

Design system structure, interfaces, and dependencies

npx @claude-flow/cli hooks route --task "architecture: [design]"


Example:

npx @claude-flow/cli hooks route --task "architecture: auth module with service layer, repository, and API endpoints"

Refinement Phase

Iterate on the design based on feedback

npx @claude-flow/cli hooks route --task "refinement: [feedback]"


Example:

npx @claude-flow/cli hooks route --task "refinement: add rate limiting and brute force protection"

Completion Phase

Finalize implementation with tests and documentation

npx @claude-flow/cli hooks route --task "completion: [final checks]"


Example:

npx @claude-flow/cli hooks route --task "completion: verify all tests pass, update API docs, security review"

SPARC Coordinator

Spawn SPARC coordinator agent

npx @claude-flow/cli agent spawn --type sparc-coord --name sparc-lead

Scripts
Script	Path	Description
sparc-init	.agents/scripts/sparc-init.sh	Initialize SPARC workflow for a new feature
sparc-review	.agents/scripts/sparc-review.sh	Run SPARC phase review checklist
References
Document	Path	Description
SPARC Overview	docs/sparc.md	Complete SPARC methodology guide
Phase Templates	docs/sparc-templates.md	Templates for each SPARC phase
Best Practices
Check memory for existing patterns before starting
Use hierarchical topology for coordination
Store successful patterns after completion
Document any new learnings
Weekly Installs
189
Repository
ruvnet/ruflo
GitHub Stars
35.8K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass