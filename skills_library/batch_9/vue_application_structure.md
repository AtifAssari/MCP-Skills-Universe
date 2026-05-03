---
title: vue-application-structure
url: https://skills.sh/aj-geddes/useful-ai-prompts/vue-application-structure
---

# vue-application-structure

skills/aj-geddes/useful-ai-prompts/vue-application-structure
vue-application-structure
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill vue-application-structure
SKILL.md
Vue Application Structure
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Build well-organized Vue 3 applications using Composition API, proper file organization, and TypeScript for type safety and maintainability.

When to Use
Large-scale Vue applications
Component library development
Reusable composable hooks
Complex state management
Performance optimization
Quick Start

Minimal working example:

// useCounter.ts (Composable)
import { ref, computed } from 'vue';

export function useCounter(initialValue = 0) {
  const count = ref(initialValue);

  const doubled = computed(() => count.value * 2);
  const increment = () => count.value++;
  const decrement = () => count.value--;
  const reset = () => count.value = initialValue;

  return {
    count,
    doubled,
    increment,
    decrement,
    reset
  };
}

// Counter.vue
<template>
  <div class="counter">
    <p>Count: {{ count }}</p>
    <p>Doubled: {{ doubled }}</p>
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Vue 3 Composition API Component	Vue 3 Composition API Component
Async Data Fetching Composable	Async Data Fetching Composable
Component Organization Structure	Component Organization Structure
Form Handling Composable	Form Handling Composable
Pinia Store (State Management)	Pinia Store (State Management)
Best Practices
✅ DO
Follow established patterns and conventions
Write clean, maintainable code
Add appropriate documentation
Test thoroughly before deploying
❌ DON'T
Skip testing or validation
Ignore error handling
Hard-code configuration values
Weekly Installs
271
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass