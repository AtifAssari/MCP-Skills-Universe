---
rating: ⭐⭐
title: saas-agent-toolkit
url: https://skills.sh/hexbee/hello-skills/saas-agent-toolkit
---

# saas-agent-toolkit

skills/hexbee/hello-skills/saas-agent-toolkit
saas-agent-toolkit
Installation
$ npx skills add https://github.com/hexbee/hello-skills --skill saas-agent-toolkit
SKILL.md
SaaS Agent Toolkit
Overview

Use this skill when a user asks how to make a SaaS product "agent-usable" rather than only human-usable.

This skill reframes product capabilities into a stable execution model:

Connectors layer: auth and event plumbing
Tools layer: six reusable tool shapes
Policy layer: permissions, approvals, and reliability guardrails
Workflow
Scope target SaaS domain and entities.
Define the 3-layer architecture.
Map capabilities into the six tool shapes.
Add guardrails (auth, allowlists, idempotency, audit).
Produce a concrete rollout plan and KPI set.
Step 1: Scope Domain

Capture:

Product/system (for example Zendesk, Salesforce, Jira, Notion)
Core entities (ticket, contact, issue, page, deal, order)
High-risk actions (payment, delete, external publish, permission change)
Success outcome (speed, quality, cost, reliability)
Step 2: Build 3-Layer Architecture

Design these layers explicitly:

Connectors: OAuth/API key, webhook ingestion, identity mapping, optional SCIM.
Tools: Search, Summarize, Draft, Update, Notify, Approve.
Policy & Guardrails: RBAC, budgets, rate limits, PII controls, logging, retries.

Design principle: Prefer predictable, auditable, rollback-safe operations over "smart but opaque" behavior.

Step 3: Define Tool Contracts

Use six stable tool contracts:

Search: locate entities and relationships.
Summarize: produce structured, citation-backed takeaways.
Draft: generate submit-ready drafts without auto-sending.
Update: write bounded, idempotent changes back to systems.
Notify: close loops with owners/watchers/approvers.
Approve: enforce human gating for high-risk operations.

Read references/tool-contracts.md for function templates and I/O expectations.

Step 4: Add Mandatory Guardrails

Apply all of the following:

Explicit error taxonomy (401, 403, 404, empty, conflict, timeout)
Idempotency key for mutating actions
Field allowlist for Update (no unrestricted patch)
Citation requirement for Summarize
Dry-run and draft-only defaults for user-facing output
Approval gates for high-risk categories
Full audit trail: who requested, who approved, what changed, when, result

Read references/approval-and-audit.md for standard approval and audit schema.

Step 5: Produce Deliverables

Return output in this structure:

Domain scope and entities
3-layer architecture
Tool contract table (six tools)
Guardrail design
Example end-to-end workflow
Rollout plan (0-30, 31-90, 90+ days)
KPI table
Top unresolved risk

KPI minimums:

task completion rate
first-call success
API success rate
p95 latency
integration lead time
unit outcome cost
Example Workflow Patterns

Use references/workflow-patterns.md for ready-to-adapt flows:

customer support triage and response
sales follow-up automation
incident assistant with approval-gated external updates
Weekly Installs
21
Repository
hexbee/hello-skills
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass