---
rating: ⭐⭐
title: valtio
url: https://skills.sh/hairyf/skills/valtio
---

# valtio

skills/hairyf/skills/valtio
valtio
Installation
$ npx skills add https://github.com/hairyf/skills --skill valtio
Summary

Minimal proxy-based state management for React and vanilla JavaScript with fine-grained reactivity.

Core API includes proxy() for creating reactive state objects, useSnapshot() for render-optimized React hooks, and subscribe() for listening to changes anywhere in your app
Utilities cover observable Map and Set proxies, property-level subscriptions, Redux DevTools integration, and unproxied references for special objects
Supports React 18+, Suspense, and computed properties via getters and setters
Best practices guide covers organizing actions, persisting state to storage, and composing multiple state objects
SKILL.md

Valtio makes proxy-state simple for React and vanilla JavaScript. It provides a minimal, flexible, and unopinionated API that turns objects into self-aware proxies, enabling fine-grained subscription and reactivity. Valtio shines at render optimization in React and is compatible with Suspense and React 18+.

The skill is based on Valtio v2.3.0, generated at 2026-01-29.

Core References
Topic	Description	Reference
Proxy	Create reactive state objects that track changes	core-proxy
useSnapshot	React hook for render-optimized state access	core-use-snapshot
Snapshot	Create immutable snapshots for comparison and Suspense	core-snapshot
Subscribe	Subscribe to state changes from anywhere	core-subscribe
Utils
Topic	Description	Reference
proxyMap	Observable Map-like proxy for Map data structures	utils-proxy-map
proxySet	Observable Set-like proxy for Set data structures	utils-proxy-set
subscribeKey	Subscribe to changes of a specific property	utils-subscribe-key
DevTools	Redux DevTools Extension integration	utils-devtools
Ref	Create unproxied references for special objects	utils-ref
Guides
Topic	Description	Reference
Component State	Isolate component state using useRef	guides-component-state
Computed Properties	Create computed properties with getters and setters	guides-computed-properties
Async	Work with promises and React Suspense	guides-async
Best Practices
Topic	Description	Reference
Actions	Organize actions for mutating state	best-practices-actions
Persistence	Persist state to localStorage or other storage	best-practices-persistence
State Composition	Split and compose states for organization	best-practices-state-composition
Weekly Installs
603
Repository
hairyf/skills
GitHub Stars
15
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass