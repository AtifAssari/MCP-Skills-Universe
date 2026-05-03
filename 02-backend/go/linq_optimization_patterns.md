---
title: linq-optimization-patterns
url: https://skills.sh/thapaliyabikendra/ai-artifacts/linq-optimization-patterns
---

# linq-optimization-patterns

skills/thapaliyabikendra/ai-artifacts/linq-optimization-patterns
linq-optimization-patterns
Installation
$ npx skills add https://github.com/thapaliyabikendra/ai-artifacts --skill linq-optimization-patterns
SKILL.md
LINQ Optimization Patterns

Optimize LINQ queries and prevent performance anti-patterns in EF Core/ABP applications.

Summary

This skill covers efficient data access patterns for Entity Framework Core in ABP Framework applications. Focus areas: N+1 prevention, pagination, projections, and batch loading.

When to use: Reviewing queries, fixing slow endpoints, implementing list APIs.

Concepts
Concept	Description	Details
Eager Loading	Load related entities in single query via JOIN	[patterns/eager-loading.md]
Projection	Transform to DTO at database level	[patterns/projection.md]
Batch Loading	Load related data for multiple parents in one query	[patterns/batch-loading.md]
Pagination	Efficient paging with count optimization	[patterns/pagination.md]
Anti-Patterns
Anti-Pattern	Severity	Detect	Impact	Details
N+1 Query	🔴 HIGH	foreach.*await.*Repo	N+1 DB calls	[anti-patterns/n-plus-one.md]
Count After Pagination	🔴 HIGH	Count.*after.*ToList	Double query	[anti-patterns/count-after-pagination.md]
Full Table Load	🔴 HIGH	GetListAsync() then filter	Memory explosion	[anti-patterns/full-table-load.md]
In-Memory Join	🔴 HIGH	Multiple ToListAsync	Cartesian in memory	[anti-patterns/in-memory-join.md]
Decision Tree
Need related data for display?
├─ Single entity ──────────► Include()        → [patterns/eager-loading.md]
├─ List of entities ───────► Batch load       → [patterns/batch-loading.md]
└─ Only specific fields ───► Projection       → [patterns/projection.md]

Need paginated list with count?
└─ Always count FIRST ─────► CountAsync()     → [patterns/pagination.md]

Loading data then filtering?
├─ Filter in query ────────► WhereIf()        → ✅ Correct
└─ Filter after ToList ────► ❌ Anti-pattern  → [anti-patterns/full-table-load.md]

Quick Detection

Run these to find issues in your codebase:

# N+1: Query inside loop
grep -rn "foreach.*await.*Repository\|for.*await.*GetAsync" src/

# Count after pagination
grep -rn "\.Count().*ToList\|ToList.*\.Count()" src/

# Full table load
grep -rn "GetListAsync()" src/ | grep -v "Where\|Any\|First"

# In-memory filtering
grep -rn "ToListAsync().*\.Where\|GetListAsync.*\.Where" src/

Rules
ID	Rule	Related
R001	Execute CountAsync() before Skip/Take	[anti-patterns/count-after-pagination.md]
R002	Apply Where clauses before ToListAsync()	[anti-patterns/full-table-load.md]
R003	Load related entities via Include or batch, not in loops	[anti-patterns/n-plus-one.md]
R004	Use Select() projection for DTO returns	[patterns/projection.md]
R005	Use AsNoTracking() for read-only queries	[patterns/projection.md]
R006	Use AsSplitQuery() for multiple collection includes	[patterns/eager-loading.md]
Checklist

Review checklist for LINQ queries:

 No foreach/for with await repository calls inside
 CountAsync() executed before Skip/Take
 No GetListAsync() followed by .Where() in memory
 No FirstOrDefault inside Select projections
 Related data loaded via Include or batch query
 Select() projection used for DTO returns
 AsNoTracking() used for read-only queries
 Multiple collection includes use AsSplitQuery()
Integration Points

This skill is used by:

abp-code-reviewer: Query performance validation
abp-developer: Efficient data access implementation
debugger: Performance issue diagnosis
Related Skills
efcore-patterns - Entity configuration, migrations
abp-framework-patterns - Repository patterns
dotnet-async-patterns - Async/await correctness
Weekly Installs
19
Repository
thapaliyabikend…rtifacts
GitHub Stars
21
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass