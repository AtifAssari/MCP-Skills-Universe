---
title: loogle-search
url: https://skills.sh/parcadei/continuous-claude-v3/loogle-search
---

# loogle-search

skills/parcadei/continuous-claude-v3/loogle-search
loogle-search
Installation
$ npx skills add https://github.com/parcadei/continuous-claude-v3 --skill loogle-search
SKILL.md
Loogle Search - Mathlib Type Signature Search

Search Mathlib for lemmas by type signature pattern.

When to Use
Finding a lemma when you know the type shape but not the name
Discovering what's available for a type (e.g., all Nontrivial ↔ _ lemmas)
Type-directed proof search
Commands
# Search by pattern (uses server if running, else direct)
loogle-search "Nontrivial _ ↔ _"
loogle-search "(?a → ?b) → List ?a → List ?b"
loogle-search "IsCyclic, center"

# JSON output
loogle-search "List.map" --json

# Start server for fast queries (keeps index in memory)
loogle-server &

Query Syntax
Pattern	Meaning
_	Any single type
?a, ?b	Type variables (same variable = same type)
Foo, Bar	Must mention both Foo and Bar
Foo.bar	Exact name match
Examples
# Find lemmas relating Nontrivial and cardinality
loogle-search "Nontrivial _ ↔ _ < Fintype.card _"

# Find map-like functions
loogle-search "(?a → ?b) → List ?a → List ?b"
# → List.map, List.pmap, ...

# Find everything about cyclic groups and center
loogle-search "IsCyclic, center"
# → commutative_of_cyclic_center_quotient, ...

# Find Fintype.card lemmas
loogle-search "Fintype.card"

Performance
With server running: ~100-200ms per query
Cold start (no server): ~10s per query (loads 343MB index)
Setup

Loogle must be built first:

cd ~/tools/loogle && lake build
lake build LoogleMathlibCache  # or use --write-index

Integration with Proofs

When stuck in a Lean proof:

Identify what type shape you need
Query Loogle to find the lemma name
Apply the lemma in your proof
-- Goal: Nontrivial G from 1 < Fintype.card G
-- Query: loogle-search "Nontrivial _ ↔ 1 < Fintype.card _"
-- Found: Fintype.one_lt_card_iff_nontrivial
exact Fintype.one_lt_card_iff_nontrivial.mpr h

Weekly Installs
296
Repository
parcadei/contin…laude-v3
GitHub Stars
3.8K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn