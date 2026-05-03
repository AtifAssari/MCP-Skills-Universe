---
title: bootstrap
url: https://skills.sh/vercel/vercel-plugin/bootstrap
---

# bootstrap

skills/vercel/vercel-plugin/bootstrap
bootstrap
Installation
$ npx skills add https://github.com/vercel/vercel-plugin --skill bootstrap
SKILL.md
Project Bootstrap Orchestrator

Execute bootstrap in strict order. Do not run migrations or development server until project linking and environment verification are complete.

Rules
Do not run db:push, db:migrate, db:seed, or dev until Vercel linking is complete and env keys are verified.
Prefer Vercel-managed provisioning (vercel integration ...) for shared resources.
Use provider CLIs only as fallback when Vercel integration flow is unavailable.
Never echo secret values in terminal output, logs, or summaries.
Preflight
Confirm Vercel CLI is installed and authenticated.
vercel --version
vercel whoami

Confirm repo linkage by checking .vercel/project.json.
If not linked, inspect available teams/projects before asking the user to choose:
vercel teams ls
vercel projects ls --scope <team>
vercel link --yes --scope <team> --project <project>

Find the env template in priority order: .env.example, .env.sample, .env.template.
Create local env file if missing:
cp .env.example .env.local

Resource Setup: Postgres
Preferred path (Vercel-managed Neon)
Read integration setup guidance:
vercel integration guide neon

Add Neon integration to the Vercel scope:
vercel integration add neon --scope <team>

Verify expected environment variable names exist in Vercel and pull locally:
vercel env ls
vercel env pull .env.local --yes

Fallback path 1 (Dashboard)
Provision Neon through the Vercel dashboard integration UI.
Re-run vercel env pull .env.local --yes.
Fallback path 2 (Neon CLI)

Use Neon CLI only when Vercel-managed provisioning is unavailable. After creating resources, add required env vars in Vercel and pull again.

AUTH_SECRET Generation

Generate a high-entropy secret without printing it, then store it in Vercel and refresh local env:

AUTH_SECRET="$(node -e "console.log(require('node:crypto').randomBytes(32).toString('base64url'))")"
printf "%s" "$AUTH_SECRET" | vercel env add AUTH_SECRET development preview production
unset AUTH_SECRET
vercel env pull .env.local --yes

Env Verification

Compare required keys from template file against .env.local keys (names only, never values):

template_file=""
for candidate in .env.example .env.sample .env.template; do
  if [ -f "$candidate" ]; then
    template_file="$candidate"
    break
  fi
done

comm -23 \
  <(grep -E '^[A-Za-z_][A-Za-z0-9_]*=' "$template_file" | cut -d '=' -f 1 | sort -u) \
  <(grep -E '^[A-Za-z_][A-Za-z0-9_]*=' .env.local | cut -d '=' -f 1 | sort -u)


Proceed only when missing key list is empty.

App Setup

After linkage + env verification:

npm run db:push
npm run db:seed
npm run dev


Use the repository package manager (npm, pnpm, bun, or yarn) and run only scripts that exist in package.json.

UI Baseline for Next.js + shadcn Projects

After linkage and env verification, establish the UI foundation before feature work:

Add a baseline primitive set: npx shadcn@latest add button card input label textarea select switch tabs dialog alert-dialog sheet dropdown-menu badge separator skeleton table
Apply the Geist font fix in layout.tsx and globals.css.
Confirm the app shell uses bg-background text-foreground.
Default to dark mode for product, admin, and AI apps unless the repo is clearly marketing-first.
Bootstrap Verification

Confirm each checkpoint:

vercel whoami succeeds.
.vercel/project.json exists and matches chosen project.
Postgres integration path completed (Vercel integration, dashboard, or provider CLI fallback).
vercel env pull .env.local --yes succeeds.
Required env key diff is empty.
Database command status is recorded (db:push, db:seed, db:migrate, db:generate as applicable).
dev command starts without immediate config/auth/env failure.

If verification fails, stop and report exact failing step plus remediation.

Summary Format

Return a final bootstrap summary in this format:

## Bootstrap Result
- **Linked Project**: <team>/<project>
- **Resource Path**: vercel-integration-neon | dashboard-neon | neon-cli
- **Env Keys**: <count> required, <count> present, <count> missing
- **Secrets**: AUTH_SECRET set in Vercel (value never shown)
- **Migration Status**: not-run | success | failed (<step>)
- **Dev Result**: not-run | started | failed

Bootstrap Next Steps
If env keys are still missing, add the missing keys in Vercel and re-run vercel env pull .env.local --yes.
If DB commands fail, fix connectivity/schema issues and re-run only the failed db step.
If dev fails, resolve runtime errors, then restart with your package manager's run dev.
next-forge Projects

If the project was scaffolded with npx next-forge init (detected by pnpm-workspace.yaml + packages/auth + packages/database + @repo/* imports):

Env files are per-app (apps/app/.env.local, apps/web/.env.local, apps/api/.env.local) plus packages/database/.env.
Run pnpm migrate (not db:push) — it runs prisma format + prisma generate + prisma db push.
Minimum env vars: DATABASE_URL, CLERK_SECRET_KEY, NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY, NEXT_PUBLIC_APP_URL, NEXT_PUBLIC_WEB_URL, NEXT_PUBLIC_API_URL.
Optional services (Stripe, Resend, PostHog, etc.) can be skipped initially — but remove their @repo/* imports from app env.ts files to avoid validation errors.
Deploy as 3 separate Vercel projects with root directories apps/app, apps/api, apps/web.

=> skill: next-forge — Full next-forge monorepo guide

Weekly Installs
211
Repository
vercel/vercel-plugin
GitHub Stars
156
First Seen
Mar 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass