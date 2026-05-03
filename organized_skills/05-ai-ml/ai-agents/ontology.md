---
rating: ⭐⭐⭐
title: ontology
url: https://skills.sh/sundial-org/awesome-openclaw-skills/ontology
---

# ontology

skills/sundial-org/awesome-openclaw-skills/ontology
ontology
Installation
$ npx skills add https://github.com/sundial-org/awesome-openclaw-skills --skill ontology
Summary

Typed knowledge graph for structured agent memory, entity management, and cross-skill state sharing.

Supports 15+ core entity types (Person, Project, Task, Event, Document, etc.) with typed properties, relations, and constraint validation
Enables graph queries, traversals, and dependency tracking; model multi-step plans as sequences of validated graph transformations
Stores data as append-only JSONL by default; schema-driven validation prevents invalid mutations and enforces cardinality, enums, and acyclic constraints
Skills declare read/write contracts and preconditions/postconditions; integrates with causal inference logging and cross-skill communication patterns
SKILL.md
Ontology

A typed vocabulary + constraint system for representing knowledge as a verifiable graph.

Core Concept

Everything is an entity with a type, properties, and relations to other entities. Every mutation is validated against type constraints before committing.

Entity: { id, type, properties, relations, created, updated }
Relation: { from_id, relation_type, to_id, properties }

When to Use
Trigger	Action
"Remember that..."	Create/update entity
"What do I know about X?"	Query graph
"Link X to Y"	Create relation
"Show all tasks for project Z"	Graph traversal
"What depends on X?"	Dependency query
Planning multi-step work	Model as graph transformations
Skill needs shared state	Read/write ontology objects
Core Types
# Agents & People
Person: { name, email?, phone?, notes? }
Organization: { name, type?, members[] }

# Work
Project: { name, status, goals[], owner? }
Task: { title, status, due?, priority?, assignee?, blockers[] }
Goal: { description, target_date?, metrics[] }

# Time & Place
Event: { title, start, end?, location?, attendees[], recurrence? }
Location: { name, address?, coordinates? }

# Information
Document: { title, path?, url?, summary? }
Message: { content, sender, recipients[], thread? }
Thread: { subject, participants[], messages[] }
Note: { content, tags[], refs[] }

# Resources
Account: { service, username, credential_ref? }
Device: { name, type, identifiers[] }
Credential: { service, secret_ref }  # Never store secrets directly

# Meta
Action: { type, target, timestamp, outcome? }
Policy: { scope, rule, enforcement }

Storage

Default: memory/ontology/graph.jsonl

{"op":"create","entity":{"id":"p_001","type":"Person","properties":{"name":"Alice"}}}
{"op":"create","entity":{"id":"proj_001","type":"Project","properties":{"name":"Website Redesign","status":"active"}}}
{"op":"relate","from":"proj_001","rel":"has_owner","to":"p_001"}


Query via scripts or direct file ops. For complex graphs, migrate to SQLite.

Workflows
Create Entity
python3 scripts/ontology.py create --type Person --props '{"name":"Alice","email":"alice@example.com"}'

Query
python3 scripts/ontology.py query --type Task --where '{"status":"open"}'
python3 scripts/ontology.py get --id task_001
python3 scripts/ontology.py related --id proj_001 --rel has_task

Link Entities
python3 scripts/ontology.py relate --from proj_001 --rel has_task --to task_001

Validate
python3 scripts/ontology.py validate  # Check all constraints

Constraints

Define in memory/ontology/schema.yaml:

types:
  Task:
    required: [title, status]
    status_enum: [open, in_progress, blocked, done]
  
  Event:
    required: [title, start]
    validate: "end >= start if end exists"

  Credential:
    required: [service, secret_ref]
    forbidden_properties: [password, secret, token]  # Force indirection

relations:
  has_owner:
    from_types: [Project, Task]
    to_types: [Person]
    cardinality: many_to_one
  
  blocks:
    from_types: [Task]
    to_types: [Task]
    acyclic: true  # No circular dependencies

Skill Contract

Skills that use ontology should declare:

# In SKILL.md frontmatter or header
ontology:
  reads: [Task, Project, Person]
  writes: [Task, Action]
  preconditions:
    - "Task.assignee must exist"
  postconditions:
    - "Created Task has status=open"

Planning as Graph Transformation

Model multi-step plans as a sequence of graph operations:

Plan: "Schedule team meeting and create follow-up tasks"

1. CREATE Event { title: "Team Sync", attendees: [p_001, p_002] }
2. RELATE Event -> has_project -> proj_001
3. CREATE Task { title: "Prepare agenda", assignee: p_001 }
4. RELATE Task -> for_event -> event_001
5. CREATE Task { title: "Send summary", assignee: p_001, blockers: [task_001] }


Each step is validated before execution. Rollback on constraint violation.

Integration Patterns
With Causal Inference

Log ontology mutations as causal actions:

# When creating/updating entities, also log to causal action log
action = {
    "action": "create_entity",
    "domain": "ontology", 
    "context": {"type": "Task", "project": "proj_001"},
    "outcome": "created"
}

Cross-Skill Communication
# Email skill creates commitment
commitment = ontology.create("Commitment", {
    "source_message": msg_id,
    "description": "Send report by Friday",
    "due": "2026-01-31"
})

# Task skill picks it up
tasks = ontology.query("Commitment", {"status": "pending"})
for c in tasks:
    ontology.create("Task", {
        "title": c.description,
        "due": c.due,
        "source": c.id
    })

Quick Start
# Initialize ontology storage
mkdir -p memory/ontology
touch memory/ontology/graph.jsonl

# Create schema (optional but recommended)
cat > memory/ontology/schema.yaml << 'EOF'
types:
  Task:
    required: [title, status]
  Project:
    required: [name]
  Person:
    required: [name]
EOF

# Start using
python3 scripts/ontology.py create --type Person --props '{"name":"Alice"}'
python3 scripts/ontology.py list --type Person

References
references/schema.md — Full type definitions and constraint patterns
references/queries.md — Query language and traversal examples
Weekly Installs
2.9K
Repository
sundial-org/awe…w-skills
GitHub Stars
589
First Seen
Mar 2, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass