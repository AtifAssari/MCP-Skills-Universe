---
rating: ⭐⭐⭐
title: frontend-iconify
url: https://skills.sh/petbrains/mvp-builder/frontend-iconify
---

# frontend-iconify

skills/petbrains/mvp-builder/frontend-iconify
frontend-iconify
Installation
$ npx skills add https://github.com/petbrains/mvp-builder --skill frontend-iconify
SKILL.md
Iconify

200,000+ open-source icons through single API. Search by concept, use any icon set.

When to Use
Find icon by concept ("dashboard", "settings")
Need icons from specific set (Lucide, Heroicons)
Download SVGs for project
Dynamic icon component
Process

SEARCH → SELECT → INTEGRATE

Search: curl "https://api.iconify.design/search?query=dashboard"
Select from results
Use via component or download SVG
API Quick Reference
# Search icons
curl "https://api.iconify.design/search?query=home&limit=10"

# Get SVG directly
curl "https://api.iconify.design/lucide/home.svg"

# With custom color (URL-encode #)
curl "https://api.iconify.design/lucide/home.svg?color=%236366f1"

Recommended Sets
Set	Prefix	Style	Best For
Lucide	lucide	Outline 24px	Default, shadcn
Heroicons	heroicons	Outline+Solid	Tailwind
Phosphor	ph	6 weights	Weight variants
Tabler	tabler	Outline 24px	Large variety
Simple Icons	simple-icons	Logos	Brand logos
Integration Methods
React Component (Recommended)
npm install @iconify/react

import { Icon } from '@iconify/react';

<Icon icon="lucide:home" width={24} />
<Icon icon="lucide:settings" className="w-5 h-5 text-primary" />

Download SVG
curl -o ./public/icons/home.svg "https://api.iconify.design/lucide/home.svg"

Batch Download
ICONS="home settings user search menu"
for icon in $ICONS; do
  curl -o "./public/icons/$icon.svg" "https://api.iconify.design/lucide/$icon.svg"
done

Common Icon Names
Navigation:  home, menu, x, chevron-right, arrow-right, search
Actions:     plus, minus, check, edit, trash-2, copy, download
Objects:     file, folder, image, calendar, mail, link
Users:       user, users, bell, lock, key, shield
Media:       play, pause, volume-2, camera, mic
Data:        bar-chart, trending-up, database, server
Status:      check-circle, x-circle, alert-triangle, info

Quick Pattern
// Icon utility wrapper
function AppIcon({ name, ...props }) {
  return <Icon icon={`lucide:${name}`} {...props} />;
}

// Usage
<AppIcon name="home" className="w-5 h-5" />

Style Matching
Project Style	Recommended
Modern/Clean	Lucide, Feather
Enterprise	Heroicons, Material
Playful	Phosphor (fill)
Brand logos	Simple Icons

Browser: https://icon-sets.iconify.design

Weekly Installs
8
Repository
petbrains/mvp-builder
GitHub Stars
10
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass