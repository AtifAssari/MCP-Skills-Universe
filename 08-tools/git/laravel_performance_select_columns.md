---
rating: ⭐⭐
title: laravel:performance-select-columns
url: https://skills.sh/jpcaparas/superpowers-laravel/laravel:performance-select-columns
---

# laravel:performance-select-columns

skills/jpcaparas/superpowers-laravel/laravel:performance-select-columns
laravel:performance-select-columns
Installation
$ npx skills add https://github.com/jpcaparas/superpowers-laravel --skill laravel:performance-select-columns
SKILL.md
Select Only Needed Columns

Reduce payloads by selecting exact fields:

User::select(['id', 'name'])->paginate();

Post::with(['author:id,name'])->select(['id','author_id','title'])->get();

Avoid *; keep DTOs/resources aligned with selected fields
Combine with eager loading to avoid N+1
Weekly Installs
66
Repository
jpcaparas/super…-laravel
GitHub Stars
131
First Seen
Jan 21, 2026