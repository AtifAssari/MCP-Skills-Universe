---
rating: ⭐⭐
title: vue3-naiveui-fsd
url: https://skills.sh/shohzod-abdusamatov-7777777/agent-skills/vue3-naiveui-fsd
---

# vue3-naiveui-fsd

skills/shohzod-abdusamatov-7777777/agent-skills/vue3-naiveui-fsd
vue3-naiveui-fsd
Installation
$ npx skills add https://github.com/shohzod-abdusamatov-7777777/agent-skills --skill vue3-naiveui-fsd
SKILL.md
Vue 3 + Naive UI + FSD Senior Development Skill

Expert-level skill for building production-ready Vue 3 applications with Naive UI, Feature-Sliced Design architecture, TypeScript, and industry best practices.

Tech Stack
Vue 3 with Composition API (<script setup>)
Naive UI v2.43+ component library
Feature-Sliced Design (FSD) architecture
TypeScript with strict mode
Pinia for state management
Vue Router 4 for routing
Tailwind CSS v4 for utility styles
Axios for HTTP requests
Day.js for date handling
Lucide Vue Next for icons
Vue I18n for internationalization
References

Detailed documentation is organized in the references/ folder:

File	Description
fsd-architecture.md	FSD directory structure and layer rules
api-layer.md	Axios setup, interceptors, service pattern
types.md	TypeScript patterns, I-prefix convention
stores.md	Pinia global stores (auth, operation)
composables.md	usePagination, useValidationRules, useTheme
forms.md	Form composable pattern (useXxxForm)
pages.md	Page component with table, CRUD
shared-ui.md	BaseTable, BaseModal, buttons
utilities.md	Formatters, helpers
router.md	Router config, guards, loading bar
Quick Start Patterns
Component Structure
<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { NCard, NButton } from 'naive-ui'
import type { IUser } from '@/entities/user'

const props = defineProps<{ userId: number }>()
const emit = defineEmits<{ success: [] }>()

const loading = ref(false)
// ... logic
</script>

<template>
  <NCard>
    <!-- content -->
  </NCard>
</template>

FSD Layer Import Rules
app     → pages, features, entities, shared
pages   → features, entities, shared
features → entities, shared
entities → shared only
shared  → nothing (self-contained)

Type Naming Convention
IUser         // Base entity
IUserList     // List item (simplified)
IUserDetail   // Full detail
IUserForm     // Form data
IUserListParams // Query params

Code Quality Checklist
 TypeScript strict mode passes
 Types use I prefix convention
 FSD layer boundaries respected
 API services in shared/api/
 Form logic in composables (useXxxForm)
 Pagination uses usePagination
 Validation uses useValidationRules
 i18n for all user-facing text
 Loading/error states handled
Weekly Installs
30
Repository
shohzod-abdusam…t-skills
GitHub Stars
1
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass