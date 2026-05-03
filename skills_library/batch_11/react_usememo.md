---
title: react-usememo
url: https://skills.sh/b4r7x/agent-skills/react-usememo
---

# react-usememo

skills/b4r7x/agent-skills/react-usememo
react-usememo
Installation
$ npx skills add https://github.com/b4r7x/agent-skills --skill react-usememo
SKILL.md
React useMemo
Overview

useMemo caches a computed value between renders. It's an optimization — code should work correctly without it. The common denominator for all valid cases: cost of computation or reference stability.

When to Use
1. Expensive computations
// ❌ Filtering 10,000 products on every render
const filtered = products.filter(p =>
  p.name.toLowerCase().includes(query.toLowerCase())
);

// ✅ Recalculates only when products or query change
const filtered = useMemo(() =>
  products.filter(p =>
    p.name.toLowerCase().includes(query.toLowerCase())
  ), [products, query]
);

2. Stable reference for memo'd child

Object/array passed as props to a memo() component — without useMemo, a new reference is created every render, defeating memo.

3. Stable reference for useEffect dependency

Object/array used in useEffect deps array — without useMemo, the effect runs every render.

4. Context Provider value
const value = useMemo(() => ({ user, logout }), [user, logout]);
<AuthContext.Provider value={value}>


This is one of the few cases where useMemo is justified without profiling first — the mechanism is well-understood and predictable.

When NOT to Use
Scenario	Why skip
Simple operation (price * quantity)	useMemo overhead > computation cost
Primitives (string, number, boolean)	React compares by value, not reference
Dependencies change every render	Memoization never caches — just overhead
No measured performance problem	Premature optimization obscures code
First render	useMemo only helps on re-renders, never first render
Decision Heuristic
Slow render? → Measure with React DevTools Profiler
                    ↓
        Is THIS component the bottleneck?
           ↓ yes                ↓ no
   Is computation expensive    Look higher up
   or result is object/array
   passed to memo'd child?
           ↓ yes
        Add useMemo

React Compiler (2025+)

React Compiler auto-memoizes computed values at build time. If you're using it, don't add manual useMemo unless you hit a measured issue or work with uncompiled external libraries. Same rules as useCallback — see react-usecallback for details.

Key Rule

React docs say: check if you have a logic bug first — useMemo on buggy code just hides it. Measure first, optimize second.

References
useMemo — React docs — official API reference with when-to-use guidance
Understanding useMemo and useCallback — Josh Comeau's practical guide to memoization decisions
How to use memo and useCallback — Nadia Makarevich on reference stability
Weekly Installs
16
Repository
b4r7x/agent-skills
First Seen
Mar 11, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass