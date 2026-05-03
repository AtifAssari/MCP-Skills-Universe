---
title: tpm-spec-trace-ids
url: https://skills.sh/ozten/skills/tpm-spec-trace-ids
---

# tpm-spec-trace-ids

skills/ozten/skills/tpm-spec-trace-ids
tpm-spec-trace-ids
Installation
$ npx skills add https://github.com/ozten/skills --skill tpm-spec-trace-ids
SKILL.md
PRD Vision Annotator

Annotate a narrative vision document with traceable Feature IDs and generate a Coverage Index.

Workflow
Add Goals section (if missing) — Extract or write 3-10 business objectives as G-01, G-02, etc.
Assign Feature IDs — Add [F-nnn] tags to major section headers
Generate Coverage Index — Create tracking file listing all features
Step 1: Goals Section

If the vision PRD lacks explicit goals, add them at the top:

## Goals

G-01: [Primary business objective]
G-02: [Secondary objective]
G-03: [Quality/compliance objective]


Extract goals from executive summary, introduction, or ask the user.

If the document contains goals already, add goal Ids and do not modify those pieces of prose.

Step 2: Feature ID Assignment

Add Feature IDs to major section headers. Do not modify prose.

Before:

## 14. RSVP Functionality

### 14.1 Process Flow


After:

## 14. RSVP Functionality [F-014]

### 14.1 Process Flow


Rules:

One Feature ID per major section (H2 level typically)
Subsections inherit parent ID unless substantial enough for their own
Number sequentially (F-001, F-002...) or match section numbers (§14 → F-014)
Skip sections explicitly out of scope
Step 3: Coverage Index

Generate a Coverage Index file using the template in assets/coverage-index-template.md.

List every Feature ID with initial status Planned.

Reference

See references/naming-conventions.md for ID format details.

Weekly Installs
9
Repository
ozten/skills
GitHub Stars
5
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass