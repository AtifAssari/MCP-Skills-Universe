---
title: button-skill
url: https://skills.sh/ashwinikarnik/rds-skills/button-skill
---

# button-skill

skills/ashwinikarnik/rds-skills/button-skill
button-skill
Installation
$ npx skills add https://github.com/ashwinikarnik/rds-skills --skill button-skill
SKILL.md
Button Skill
When To Use

Use this skill when implementing base-theme button patterns in a Vue project using @rds-vue-ui/* packages (not local component copies).

Inputs
Framework: Vue 3
Package manager: yarn (or npm/pnpm equivalent)
Private registry (required): https://npm.edpl.us
Storybook docs URL: https://rds-vue-ui.edpl.us/?path=/docs/components-button-buttons--docs
Base theme only (ignore alternate themes).
Dependencies (Registry Packages)
@rds-vue-ui/rds-theme-base
sass-embedded (if SCSS preprocessing is required by dependent packages)
Registry Configuration (Required)
Add/update project .npmrc:
@rds-vue-ui:registry=https://npm.edpl.us/
Validate package resolution:
npm view @rds-vue-ui/rds-theme-base version --registry=https://npm.edpl.us/
Workflow
Configure .npmrc with @rds-vue-ui scoped registry.
Install packages from private registry:
yarn add @rds-vue-ui/rds-theme-base
yarn add -D sass-embedded (if build fails on SCSS preprocessing).
Import base theme once in app entry:
import '@rds-vue-ui/rds-theme-base/dist/css/rds-theme-base.css';
Implement button usage based on Storybook Components/Button/Buttons docs:
Use documented classes (btn, size variants, solid/outline variants, disabled, block).
Do not create local replacement button components to mimic RDS behavior.
Create/update practical demo examples and route links.
Run QA checklist and resolve all open items.
Outputs
README.md
spec/component-spec.md
examples/*
checklists/qa.md
Verification Checklist
 .npmrc contains @rds-vue-ui:registry=https://npm.edpl.us/.
 @rds-vue-ui/rds-theme-base resolves from private registry.
 Base theme CSS imported exactly once in app entry.
 Examples use documented button patterns from Storybook.
 No local replacement button component was introduced.
 Build completes successfully.
Constraints
Base theme only.
No non-base screenshots, variants, or token references.
Prefer registry package usage over local component implementations.
If details are unknown, mark them as TBD and capture source needed to confirm.
Failure Handling
Registry/auth failure:
Verify .npmrc scope is set to @rds-vue-ui:registry=https://npm.edpl.us/.
Retry npm view @rds-vue-ui/rds-theme-base version --registry=https://npm.edpl.us/.
If still blocked, confirm VPN/SSO/token requirements for private registry access.
SCSS preprocessor failure:
Install sass-embedded and rebuild.
Weekly Installs
10
Repository
ashwinikarnik/rds-skills
First Seen
Mar 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass