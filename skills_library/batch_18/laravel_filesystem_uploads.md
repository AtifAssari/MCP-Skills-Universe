---
title: laravel:filesystem-uploads
url: https://skills.sh/jpcaparas/superpowers-laravel/laravel:filesystem-uploads
---

# laravel:filesystem-uploads

skills/jpcaparas/superpowers-laravel/laravel:filesystem-uploads
laravel:filesystem-uploads
Installation
$ npx skills add https://github.com/jpcaparas/superpowers-laravel --skill laravel:filesystem-uploads
SKILL.md
Filesystem Uploads and URLs

Use the Storage facade consistently; abstract away the backend (local, S3, etc.).

Commands
$path = Storage::disk('public')->putFile('avatars', $request->file('avatar'));

// Temporary URLs (S3, etc.)
$url = Storage::disk('s3')->temporaryUrl($path, now()->addMinutes(10));

// Streams
return Storage::disk('backups')->download('db.sql.gz');

Patterns
Keep user uploads under a dedicated disk with explicit visibility
Avoid assuming local paths; always go through Storage
For public assets, run storage:link and serve via web server / CDN
Validate mime/types and size limits at upload boundaries
Weekly Installs
55
Repository
jpcaparas/super…-laravel
GitHub Stars
131
First Seen
Jan 21, 2026