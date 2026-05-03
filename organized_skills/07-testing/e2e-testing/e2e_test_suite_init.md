---
rating: ⭐⭐
title: e2e-test-suite-init
url: https://skills.sh/agentmantis/test-skills/e2e-test-suite-init
---

# e2e-test-suite-init

skills/agentmantis/test-skills/e2e-test-suite-init
e2e-test-suite-init
Installation
$ npx skills add https://github.com/agentmantis/test-skills --skill e2e-test-suite-init
SKILL.md
Initialise E2E Test Suite

Scaffold the entire e2e/ directory structure with all configuration files, base classes, fixtures, and helpers needed to start writing Playwright E2E tests.

Pre-Flight Check
Check if e2e/ already exists. If so, abort and inform the user — do NOT overwrite an existing test suite.
Check if Playwright is installed. If @playwright/test is not in package.json, add it.
Workflow
Step 1 — Create the Directory Structure
e2e/
├── auth/
│   └── auth.setup.ts
├── fixtures/
│   └── base.ts
├── helpers/
│   └── env-config.ts
├── poms/
│   └── base.page.ts
├── test-data/
├── tests/
│   ├── handover/
│   ├── regression/
│   └── smoke/
├── .auth/                   # git-ignored, holds saved session state
├── .gitignore
├── .env.example
├── playwright.config.ts
└── tsconfig.json

Step 2 — Generate Configuration Files

Generate each file using the reference templates:

File	Template Reference
playwright.config.ts	references/playwright-config-template.md
poms/base.page.ts	references/base-page-template.md
fixtures/base.ts	references/fixtures-template.md
helpers/env-config.ts	references/env-config-template.md
auth/auth.setup.ts	See e2e-test-conventions skill, references/auth-setup.md
Step 3 — Generate Support Files

e2e/.gitignore:

.auth/
.env
.env.*
!.env.example
test-results/
playwright-report/
blob-report/


e2e/.env.example:

BASE_URL="https://your-app.example.com"
LOGIN_EMAIL="test-user@example.com"
LOGIN_PASSWORD="your-password"
AUTH_FILE="e2e/.auth/user.json"


e2e/tsconfig.json:

{
    "compilerOptions": {
        "target": "ES2022",
        "module": "commonjs",
        "moduleResolution": "node",
        "strict": true,
        "esModuleInterop": true,
        "skipLibCheck": true,
        "forceConsistentCasingInFileNames": true,
        "resolveJsonModule": true,
        "outDir": "./dist",
        "rootDir": "."
    },
    "include": ["**/*.ts"],
    "exclude": ["node_modules", "dist"]
}

Step 4 — Adapt to the Project

Ask the user (or infer from the existing codebase) about:

Login page URL — to customise auth.setup.ts
Post-login URL — the URL to wait for after login (e.g., /dashboard, /home)
Auth storage method — cookies/localStorage only, or IndexedDB (Firebase, Supabase, etc.)
Base URL — the application URL for the default environment
Step 5 — Print Next Steps

After generating all files, tell the user:

Install Playwright browsers: npx playwright install
Copy .env.example to .env.production and fill in values
Create a POM for the first page: /create-pom [page-name]
Create the first test: /create-regression-test [feature]
Rules
Never overwrite an existing e2e/ directory
All generated code must be TypeScript
Follow the e2e-test-conventions skill for all patterns
Use the two-layer env loading pattern (getEnvConfig(), getBaseUrl(), etc.)
Auth file path must come from AUTH_FILE env var via getAuthFilePath()
All five browsers must be configured in playwright.config.ts
All three suites (regression, handover, smoke) must be configured
Weekly Installs
18
Repository
agentmantis/test-skills
GitHub Stars
8
First Seen
7 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass