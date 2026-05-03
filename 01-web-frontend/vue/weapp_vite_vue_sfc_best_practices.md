---
rating: ⭐⭐
title: weapp-vite-vue-sfc-best-practices
url: https://skills.sh/weapp-vite/weapp-vite/weapp-vite-vue-sfc-best-practices
---

# weapp-vite-vue-sfc-best-practices

skills/weapp-vite/weapp-vite/weapp-vite-vue-sfc-best-practices
weapp-vite-vue-sfc-best-practices
Installation
$ npx skills add https://github.com/weapp-vite/weapp-vite --skill weapp-vite-vue-sfc-best-practices
SKILL.md
weapp-vite-vue-sfc-best-practices
目的

Implement Vue SFC for mini-programs with a two-layer model: compile-time rules (weapp-vite) and runtime behavior (wevu). Favor predictable compile output and explicit mini-program semantics.

触发信号
User asks how to write/refactor mini-program .vue files.
User asks about JSON macro usage (definePageJson, defineComponentJson, defineAppJson) or <json> migration.
User hits directive compatibility issues (v-model assignment rules, v-bind="object" behavior).
User reports SFC compile or runtime mismatch after template/script changes.
User asks how to declare usingComponents correctly in SFC.
适用边界

Use this skill when the center of gravity is SFC authoring and compile compatibility.

Do not use this as the primary skill when:

The issue is mostly project-level build/CI/subpackage strategy. Use weapp-vite-best-practices.
The issue is mostly runtime lifecycle/store/event architecture. Use wevu-best-practices.
The task is phased migration from native mini-program. Use native-to-weapp-vite-wevu-migration.
快速开始
Confirm SFC type first: App, Page, or Component.
Pick one JSON macro family that matches the SFC role.
Validate template directives against mini-program compatibility constraints.
Verify runtime API imports and hook timing.
If the project installs weapp-vite, prefer packaged docs under node_modules/weapp-vite/dist/docs/ for current-version examples.
执行流程
Classify the failure stage
Compile-time: macro syntax, template transform, usingComponents declaration.
Runtime: hook timing, event payload, reactive update expectations.
Tooling/type: Volar config, vueCompilerOptions.lib, type resolution.
Enforce SFC boundaries
Keep <template>/<script>/<style> responsibilities explicit.
Manage mini-program JSON via Script Setup JSON macros first.
Use <json> only for legacy compatibility or explicit migration constraints.
Do not register mini-program components via script-side ESM registration patterns.
Apply script rules
Prefer <script setup lang="ts">.
Import runtime APIs from wevu in business logic.
Register hooks synchronously in setup() and avoid post-await registration.
Apply macro and template rules
Use only one JSON macro per SFC role (defineAppJson / definePageJson / defineComponentJson).
Treat definePageMeta as a separate page-meta macro; it may coexist with definePageJson in page SFCs.
App -> defineAppJson; Page -> definePageJson; Component -> defineComponentJson.
Keep macro calls top-level with a single object argument.
For v-model, only use assignable left values: x, x.y, x[i].
Avoid unsupported forms such as v-model modifiers/arguments and full-object v-bind expansion assumptions.
Verify narrowly
Run targeted checks that match the touched SFC files.
Escalate to broader runs only when cross-page behavior is affected.
约束
Do not treat mini-program component registration like web Vue component registration.
Do not register hooks after await in setup().
Do not assume web Vue template features are fully available in mini-program compilation.
Do not mix multiple JSON macro families in one SFC.
Do not mix SFC syntax fixes with unrelated runtime architecture refactors.
Do not ignore project root AGENTS.md guidance in scaffolded templates.
输出要求

When applying this skill, return:

Stage-based diagnosis (compile/runtime/tooling).
Concrete SFC-level edit list.
Compatibility notes for directives/macros used.
Minimal verification commands.
完成检查
SFC config path is clear and macro-first (avoid new <json> usage by default).
usingComponents strategy is deterministic and path-safe.
Template usage avoids unsupported directive forms.
Runtime API imports come from wevu.
Hook timing and page/component context are valid.
SFC guidance remains aligned with current template-level AI instructions and packaged docs.
参考资料
references/macro-config-checklist.md
references/template-compat-matrix.md
references/troubleshooting-playbook.md
Weekly Installs
43
Repository
weapp-vite/weapp-vite
GitHub Stars
317
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass