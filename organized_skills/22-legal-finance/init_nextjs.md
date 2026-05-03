---
rating: ⭐⭐
title: init-nextjs
url: https://skills.sh/zhangwanli09/skills/init-nextjs
---

# init-nextjs

skills/zhangwanli09/skills/init-nextjs
init-nextjs
Installation
$ npx skills add https://github.com/zhangwanli09/skills --skill init-nextjs
SKILL.md
Initialize a New Next.js App

Ask for the project name if not given, then run the phases in order. All @latest tags resolve to current stable at install time — no doc lookups.

1. Create
npx create-next-app@latest <name> --yes


All subsequent commands run inside the <name>/ directory.

2. Prettier
npm i -D prettier eslint-config-prettier

Write <name>/.prettierrc → {}
Read <name>/eslint.config.mjs. Add import eslintConfigPrettier from "eslint-config-prettier/flat"; near the other imports, then append eslintConfigPrettier as the last element of the eslintConfig array (after the ...compat.extends(...) spread).
3. Husky + lint-staged
npm i -D husky lint-staged
npx husky init

Overwrite <name>/.husky/pre-commit with: npx lint-staged
Add to <name>/package.json: "lint-staged": { "*": "prettier --ignore-unknown --write" }
4. Verify
npx prettier --write .
npm run lint


Fix any errors before declaring success. Tell the user the project path and that commits now auto-format.

Weekly Installs
9
Repository
zhangwanli09/skills
First Seen
Apr 8, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn