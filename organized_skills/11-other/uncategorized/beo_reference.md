---
rating: ⭐⭐
title: beo-reference
url: https://skills.sh/minhtri2710/skills/beo-reference
---

# beo-reference

skills/minhtri2710/skills/beo-reference
beo-reference
Installation
$ npx skills add https://github.com/minhtri2710/skills --skill beo-reference
SKILL.md
beo-reference

Canonical shared reference corpus for beo skills.

This skill is lookup-only. It exists so other beo skills can cite beo-reference → references/<file> and load exactly the protocol document they need.

Atomic purpose

Expose one authoritative reference, read-only.

When to use
another beo skill needs one specific shared protocol, rule, convention, contract, or CLI reference
authoritative guidance is required without any behavioral work or state changes
Inputs

Required

one explicit reference request identifying the needed document
Outputs

Allowed reads only

the targeted reference document from references/<file>

Must not write

STATE.json
HANDOFF.json
feature artifacts
implementation code
Boundary rules
beo-reference is read-only and not a routing destination.
beo-reference must not make decisions, write state, edit artifacts, or execute feature work.
Callers must load only the needed reference file, not the full corpus.
beo-reference must not function as an operational skill.
Reference index
CLI references
references/br-cli-reference.md — canonical br command usage
references/bv-cli-reference.md — canonical bv command usage
Status and state
references/status-mapping.md — canonical bead states and transitions
references/state-and-handoff-protocol.md — STATE.json and HANDOFF.json schema and resume rules
Artifacts
references/artifact-conventions.md — artifact paths, ownership, and naming
references/bead-description-templates.md — standard bead description formats
Workflow protocols
references/pipeline-contracts.md — routing table, allowed transitions, cross-skill invariants
references/approval-gates.md — approval timing and label ownership
references/dependency-and-scheduling.md — dependency reconciliation and scheduling cascade
references/failure-recovery.md — failure classes and recovery rules
references/shared-hard-gates.md — shared onboarding, session-boundary, and interaction rules
references/worker-template.md — standard worker prompt template
Knowledge and communication
references/knowledge-store.md — knowledge-store rules and integration
references/learnings-read-protocol.md — reading learnings and critical patterns safely
references/communication-standard.md — communication rules for beo outputs
references/agent-mail-coordination.md — coordinator / worker messaging protocol
Red flags
routing to beo-reference
loading the entire corpus instead of one needed file
treating reference docs as permission to change pipeline ownership
Weekly Installs
24
Repository
minhtri2710/skills
GitHub Stars
1
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass