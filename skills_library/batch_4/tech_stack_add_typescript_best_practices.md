---
title: tech-stack:add-typescript-best-practices
url: https://skills.sh/neolabhq/context-engineering-kit/tech-stack:add-typescript-best-practices
---

# tech-stack:add-typescript-best-practices

skills/neolabhq/context-engineering-kit/tech-stack:add-typescript-best-practices
tech-stack:add-typescript-best-practices
Installation
$ npx skills add https://github.com/neolabhq/context-engineering-kit --skill tech-stack:add-typescript-best-practices
SKILL.md
Setup TypeScript Best Practices

Create or update CLAUDE.md in with following content, write it strictly as it is, do not summaraise or introduce and new additional information:

## Code Style Rules

### General Principles

- **TypeScript**: All code must be strictly typed, leverage TypeScript's type safety features

### Code style rules

- Interfaces over types - use interfaces for object types
- Use enum for constant values, prefer them over string literals
- Export all types by default
- Use type guards instead of type assertions

### Best Practices

#### Library-First Approach

- Common areas where libraries should be preferred:
  - Date/time manipulation → date-fns, dayjs
  - Form validation → joi, yup, zod
  - HTTP requests → axios, got
  - State management → Redux, MobX, Zustand
  - Utility functions → lodash, ramda

#### Code Quality

- Use destructuring of objects where possible:
  - Instead of `const name = user.name` use `const { name } = user`
  - Instead of `const result = await getUser(userId)` use `const { data: user } = await getUser(userId)`
  - Instead of `const parseData = (data) => data.name` use `const parseData = ({ name }) => name`
- Use `ms` package for time related configuration and environment variables, instead of multiplying numbers by 1000

Weekly Installs
440
Repository
neolabhq/contex…ring-kit
GitHub Stars
942
First Seen
Feb 19, 2026