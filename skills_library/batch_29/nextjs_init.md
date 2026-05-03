---
title: nextjs-init
url: https://skills.sh/kazdenc/builder-skills/nextjs-init
---

# nextjs-init

skills/kazdenc/builder-skills/nextjs-init
nextjs-init
Installation
$ npx skills add https://github.com/kazdenc/builder-skills --skill nextjs-init
SKILL.md
Next.js Project Scaffold

Create a production-ready Next.js project with App Router, TypeScript, and Tailwind CSS. If the user provides a target, use it as the project name. Otherwise, ask.

Step 1: Run create-next-app

Execute this command, replacing <project-name> with the target:

npx create-next-app@latest <project-name> \
  --typescript \
  --tailwind \
  --eslint \
  --app \
  --src-dir \
  --import-alias "@/*" \
  --use-pnpm


If the user prefers npm or yarn, swap --use-pnpm accordingly. Default to pnpm.

Step 2: Set Up Directory Structure

Create these directories inside src/:

src/
  app/                  # Routes and layouts (created by create-next-app)
    (auth)/             # Auth route group
    (dashboard)/        # Main app route group
    api/                # API routes
    layout.tsx          # Root layout
    page.tsx            # Landing page
  components/
    ui/                 # Reusable primitives (Button, Input, Card)
    forms/              # Form components
    layout/             # Header, Footer, Sidebar, Nav
  lib/
    utils.ts            # Shared utility functions
    constants.ts        # App-wide constants
  types/
    index.ts            # Shared TypeScript types
  hooks/                # Custom React hooks
  styles/
    globals.css         # Already created by create-next-app

mkdir -p src/{components/{ui,forms,layout},lib,types,hooks,app/{\\(auth\\),\\(dashboard\\),api}}

Step 3: Configure TypeScript

Verify tsconfig.json has these settings. Patch if missing:

{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "forceConsistentCasingInFileNames": true,
    "paths": {
      "@/*": ["./src/*"]
    }
  }
}

Setting	Why
strict: true	Catches type errors early. Non-negotiable.
noUncheckedIndexedAccess	Forces handling of undefined from array/object access
forceConsistentCasingInFileNames	Prevents deploy failures on case-sensitive Linux servers
Step 4: Configure ESLint

Extend .eslintrc.json:

{
  "extends": [
    "next/core-web-vitals",
    "next/typescript"
  ],
  "rules": {
    "prefer-const": "error",
    "no-unused-vars": "off",
    "@typescript-eslint/no-unused-vars": ["error", { "argsIgnorePattern": "^_" }]
  }
}

Step 5: Add Prettier
pnpm add -D prettier prettier-plugin-tailwindcss


Create .prettierrc:

{
  "semi": false,
  "singleQuote": true,
  "tabWidth": 2,
  "trailingComma": "all",
  "plugins": ["prettier-plugin-tailwindcss"]
}


Create .prettierignore:

node_modules
.next
dist
pnpm-lock.yaml

Step 6: Environment Setup

Create .env.local with a template:

# App
NEXT_PUBLIC_APP_URL=http://localhost:3000

# Database (fill in after setting up Supabase or other DB)
# DATABASE_URL=

# Auth (fill in after setting up auth provider)
# NEXTAUTH_SECRET=
# NEXTAUTH_URL=http://localhost:3000


Create .env.example with the same keys but no values. Ensure .env.local is in .gitignore (create-next-app does this by default).

Step 7: Starter Root Layout

Replace src/app/layout.tsx with:

import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import '@/styles/globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'App Name',
  description: 'App description',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={inter.className}>{children}</body>
    </html>
  )
}

Step 8: Add Utility Helpers

Create src/lib/utils.ts:

import { type ClassValue, clsx } from 'clsx'
import { twMerge } from 'tailwind-merge'

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}


Install the dependencies:

pnpm add clsx tailwind-merge

Step 9: Verify

Run these checks before handing off:

pnpm build        # Must compile without errors
pnpm lint         # Must pass with zero warnings

Post-Scaffold Checklist
Task	Status
create-next-app ran with correct flags	
Directory structure created	
TypeScript strict mode enabled	
ESLint configured	
Prettier + Tailwind plugin installed	
.env.local template created	
.env.example created (no secrets)	
Root layout uses Inter font + metadata	
cn() utility installed	
pnpm build passes	
pnpm lint passes	
Weekly Installs
9
Repository
kazdenc/builder-skills
GitHub Stars
35
First Seen
Mar 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass