---
title: angular-coding
url: https://skills.sh/khaihuynhvn/mcp-server_ai-interaction/angular-coding
---

# angular-coding

skills/khaihuynhvn/mcp-server_ai-interaction/angular-coding
angular-coding
Installation
$ npx skills add https://github.com/khaihuynhvn/mcp-server_ai-interaction --skill angular-coding
SKILL.md
Angular Coding Standards

Version-aware Angular development patterns.

Pre-Edit Analysis

Trước khi edit Angular code, read: → C:\Users\BLogic\.cursor\skills\project-scanner\SKILL.md

Quality gates cho high-risk edits (change signature, shared service, delete/rename).

Setup

Step 0: Scan Existing Patterns (Nếu project có code)

Trước khi tạo mới, scan project để follow convention đang dùng:

Glob: **/*.service.ts → Xem service pattern
Glob: **/*.component.ts → Xem component pattern  
Glob: **/*.model.ts → Xem model/interface pattern
Grep: FormGroup → Xem form pattern


Step 1: Detect Angular Version

Read package.json and find @angular/core version:

"@angular/core": "^17.0.0"  // → v17
"@angular/core": "~15.2.0"  // → v15


Step 2: Load Appropriate Patterns

Based on detected version, read the relevant files:

Version	Files to Read
v13-14	base.md + module-based.md
v15-16	base.md + standalone.md + signals.md (preview)
v17	base.md + standalone.md + signals.md + control-flow.md
v18-19+	base.md + standalone.md + signals.md + control-flow.md + advanced-v18-19.md
Quick Reference
Naming Conventions (All Versions)
Type	Convention	Example
Signal	Prefix $	$user, $state
Observable	Suffix $	isLoading$, data$
Private	Prefix _	_destroyed$, _load()
Core Principles
Priority	Principle	Guideline
🥇	Angular-native first	95% dùng Angular built-in (reactive forms, validators, pipes, directives). 5% custom code khi Angular không hỗ trợ
🥈	Performance	OnPush, signals, object mapping > array loop, minimal subscriptions
🥉	Readability	Simple code, dễ đọc, dễ sửa cho dev khác. OOP + SOLID
Decision Flow
Có vấn đề cần giải quyết?
    ↓
Angular có built-in? (FormControl, Pipe, Directive, Validator...)
    ├─ YES → Dùng Angular (95%)
    └─ NO  → Tạo custom với SOLID pattern (5%)

File Index
base.md - Common patterns all versions
module-based.md - NgModule patterns (v13-14)
standalone.md - Standalone components (v15+)
signals.md - Signals API (v16+)
control-flow.md - @if/@for/@defer (v17+)
advanced-v18-19.md - Signal inputs, linkedSignal (v18+)
Weekly Installs
20
Repository
khaihuynhvn/mcp…eraction
GitHub Stars
29
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass