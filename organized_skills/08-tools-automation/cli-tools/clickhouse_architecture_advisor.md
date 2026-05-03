---
rating: ⭐⭐⭐
title: clickhouse-architecture-advisor
url: https://skills.sh/clickhouse/agent-skills/clickhouse-architecture-advisor
---

# clickhouse-architecture-advisor

skills/clickhouse/agent-skills/clickhouse-architecture-advisor
clickhouse-architecture-advisor
Installation
$ npx skills add https://github.com/clickhouse/agent-skills --skill clickhouse-architecture-advisor
SKILL.md
ClickHouse Architecture Advisor

This skill adds workload-aware architecture decisioning on top of clickhouse-best-practices.

Official docs remain the source of truth. This skill must always prefer official ClickHouse documentation when available.

Required behavior

Before producing recommendations:

Identify the workload shape
observability
security / SIEM
product analytics
IoT / telemetry
market data / financial services
mixed OLAP with point-lookups
Read the relevant decision rule files in rules/
Use mappings/doc_links.yaml to attach official documentation
Classify every recommendation as:
official
derived
field
Never present field guidance as official guidance
If a recommendation is uncertain, say so explicitly
Provenance rules
official

Use this when the recommendation is directly backed by official docs.

derived

Use this when the recommendation is not stated verbatim in docs but follows logically from documented ClickHouse behavior.

field

Use this only for experience-based guidance that may be situational. When using field, include:

a disclaimer that the advice is heuristic
a relevant official doc if one partially applies
the reason the advice depends on workload context
Read these rule files by scenario
Real-time ingestion design
rules/decision-ingestion-strategy.md
rules/decision-real-time-preaggregation.md
Relevant best-practices insert rules
Time-series and retention design
rules/decision-partitioning-timeseries.md
Relevant best-practices schema partition rules
Enrichment and dimension lookups
rules/decision-join-enrichment.md
Relevant best-practices query join rules
Mutable state / late-arriving events
rules/decision-late-arriving-upserts.md
Relevant best-practices mutation avoidance rules
Output format

Structure responses like this:

## Workload Summary
- workload:
- latency target:
- data shape:
- primary query patterns:
- operational constraints:

## Key Decisions
- ...
- ...

## Recommendations

### <Recommendation title>

**What**
...

**Why**
...

**How**
...

**Category**
official | derived | field

**Confidence**
high | medium | heuristic

**Source**
- doc link(s)

**Validation**
- concrete SQL, metric, or smoke test

Architecture-specific guidance

Prefer decision frameworks over generic advice. Good responses should:

explain tradeoffs
identify the likely operating bottleneck
separate immediate actions from structural redesign
provide target architecture patterns, not just isolated settings
Full reference

See AGENTS.md for the compiled version and examples/ for sample outputs.

Weekly Installs
374
Repository
clickhouse/agent-skills
GitHub Stars
414
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass