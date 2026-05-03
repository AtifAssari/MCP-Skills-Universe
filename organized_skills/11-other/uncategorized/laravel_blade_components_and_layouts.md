---
rating: ⭐⭐
title: laravel:blade-components-and-layouts
url: https://skills.sh/jpcaparas/superpowers-laravel/laravel:blade-components-and-layouts
---

# laravel:blade-components-and-layouts

skills/jpcaparas/superpowers-laravel/laravel:blade-components-and-layouts
laravel:blade-components-and-layouts
Installation
$ npx skills add https://github.com/jpcaparas/superpowers-laravel --skill laravel:blade-components-and-layouts
SKILL.md
Blade Components and Layouts

Encapsulate markup and behavior with components; prefer slots over includes.

Commands
sail artisan make:component Alert              # or: php artisan make:component Alert

// Use component
<x-alert type="warning" :message="$msg" class="mb-4" />

// Layouts + stacks
@extends('layouts.app')
@push('scripts')
    <script>/* page script */</script>
@endpush

Patterns
Keep components dumb: pass data in, emit markup out
Use merge() to honor passed classes/attributes in components
Prefer named slots for readability
Extract small, reusable atoms rather than giant organisms
Weekly Installs
86
Repository
jpcaparas/super…-laravel
GitHub Stars
131
First Seen
Jan 21, 2026