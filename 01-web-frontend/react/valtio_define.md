---
rating: ⭐⭐
title: valtio-define
url: https://skills.sh/hairyf/skills/valtio-define
---

# valtio-define

skills/hairyf/skills/valtio-define
valtio-define
Installation
$ npx skills add https://github.com/hairyf/skills --skill valtio-define
Summary

Valtio-based reactive state management with Pinia-like API for React.

Core API includes defineStore for creating stores with state, actions, and getters, plus useStore hook for React component access
Advanced features cover subscriptions, patch operations, inline reactive JSX components via Signal, and conversion to useState-like hooks
Plugin system enables store extensions, including built-in persistent storage plugin for state hydration
Full TypeScript support with comprehensive type definitions
SKILL.md

Based on valtio-define v1.0.1. A Valtio-based state management library with Pinia-like API for React applications.

Overview

valtio-define provides a factory function for creating reactive stores with state, actions, and getters. Built on top of Valtio, it offers a familiar API similar to Pinia with full TypeScript support.

Core References
Topic	Description	Reference
defineStore	Core API for creating reactive stores	core-define-store
useStore	React hook for accessing store state	core-use-store
Types	TypeScript types and interfaces	core-types
Advanced Features
Topic	Description	Reference
Subscriptions	Subscribe to state changes	advanced-subscribe
Patch	Update state with patch operations	advanced-patch
Signal	JSX component for inline reactive values	advanced-signal
Store to State	Convert store to useState-like hooks	advanced-store-to-state
Features
Topic	Description	Reference
Plugin System	Extend stores with plugins	feature-plugin-system
Persistent Plugin	Persist state to storage	feature-persistent-plugin
Quick Start
import { defineStore, useStore } from 'valtio-define'

const store = defineStore({
  state: () => ({ count: 0 }),
  actions: {
    increment() { this.count++ },
  },
  getters: {
    doubled() { return this.count * 2 },
  },
})

function Counter() {
  const state = useStore(store)
  return (
    <div>
      <div>Count: {state.count}</div>
      <div>Doubled: {state.doubled}</div>
      <button onClick={store.increment}>Increment</button>
    </div>
  )
}

Weekly Installs
583
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