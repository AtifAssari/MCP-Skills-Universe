---
title: laravel:api-resources-and-pagination
url: https://skills.sh/jpcaparas/superpowers-laravel/laravel:api-resources-and-pagination
---

# laravel:api-resources-and-pagination

skills/jpcaparas/superpowers-laravel/laravel:api-resources-and-pagination
laravel:api-resources-and-pagination
Installation
$ npx skills add https://github.com/jpcaparas/superpowers-laravel --skill laravel:api-resources-and-pagination
SKILL.md
API Resources and Pagination

Represent models via Resources; keep transport concerns out of Eloquent.

Commands
# Resource
sail artisan make:resource PostResource    # or: php artisan make:resource PostResource

# Controller usage
return PostResource::collection(
    Post::with('author')->latest()->paginate(20)
);

# Resource class
public function toArray($request)
{
    return [
        'id' => $this->id,
        'title' => $this->title,
        'author' => new UserResource($this->whenLoaded('author')),
        'published_at' => optional($this->published_at)->toAtomString(),
    ];
}

Patterns
Prefer Resource::collection($query->paginate()) over manual arrays
Use when() / mergeWhen() for conditional fields
Keep pagination cursors/links intact for clients
Version resources when contracts change; avoid breaking fields silently
Weekly Installs
64
Repository
jpcaparas/super…-laravel
GitHub Stars
131
First Seen
Jan 21, 2026