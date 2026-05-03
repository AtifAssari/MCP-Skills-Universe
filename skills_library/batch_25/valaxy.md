---
title: valaxy
url: https://skills.sh/yunyoujun/valaxy/valaxy
---

# valaxy

skills/yunyoujun/valaxy/valaxy
valaxy
Installation
$ npx skills add https://github.com/yunyoujun/valaxy --skill valaxy
SKILL.md
Valaxy

Next-generation static blog framework: Vue 3 + Vite + UnoCSS + file-based routing + markdown-it.

Quick Reference
pnpm create valaxy          # scaffold new site
pnpm i                      # MUST use pnpm
pnpm dev                    # dev server at localhost:4859
pnpm build                  # SSG build to dist/


Two config files:

site.config.ts — site metadata (title, author, social, search, comments) via defineSiteConfig()
valaxy.config.ts — framework config (theme, addons, markdown, vite) via defineValaxyConfig<ThemeConfig>()
Optional theme.config.ts — theme-specific via defineThemeConfig()

Posts go in pages/posts/*.md. Frontmatter controls title, date, tags, categories, cover, draft, encryption, layout, etc.

Key Patterns
Config Merging

Config sources merge via defu (user wins): Default → Theme → Addons → User.

File Resolution (Roots System)
roots = [clientRoot, themeRoot, ...addonRoots, userRoot]


User components/layouts/styles override theme which overrides core — by filename matching.

Routing

File-based via vue-router/vite. Files in pages/ become routes. Layout auto-assigned:

pages/posts/** → post layout
pages/tags/** → tags layout
pages/categories/** → categories layout

Override with layout: xxx in frontmatter.

Collections

Define in pages/collections/{name}/index.ts using defineCollection():

import { defineCollection } from 'valaxy'

export default defineCollection({
  key: 'hamster',
  title: 'Hamster Stories',
  items: [
    { title: 'Chapter 1', key: '1' },
  ],
})

i18n
CSS-based bilingual: ::: zh-CN / ::: en containers in markdown
File-based: locales/*.yml
Frontmatter: title: { en: 'Title', 'zh-CN': '标题' }
Tags: $locale:tag.notes syntax
Custom Styles

Create styles/index.ts (or .scss/.css) — auto-loaded. Override CSS vars for theming.

Custom Components

Place .vue files in components/ — auto-registered, overrides theme/core components by name.

Monorepo Development

When working on the Valaxy core framework itself:

pnpm i                     # install all workspace deps
pnpm run build             # build core: utils → valaxy → devtools
pnpm dev:lib               # watch core packages
pnpm demo                  # run demo site
pnpm docs:dev              # run docs site
pnpm test                  # unit tests (vitest)
pnpm e2e                   # E2E tests (playwright)
pnpm lint                  # eslint
pnpm typecheck             # type check

Repository URL Normalization

When displaying repository URLs from package.json, import and use normalizeRepositoryUrl() from @valaxyjs/utils to remove the git+ prefix.

References
Framework architecture, virtual modules, composables, components: Read references/architecture.md
Theme/addon development, post frontmatter, addon gallery: Read references/theme-addon-dev.md
Weekly Installs
22
Repository
yunyoujun/valaxy
GitHub Stars
1.1K
First Seen
Mar 2, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass