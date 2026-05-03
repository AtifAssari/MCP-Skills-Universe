---
rating: ⭐⭐⭐
title: expo-architect
url: https://skills.sh/shipshitdev/library/expo-architect
---

# expo-architect

skills/shipshitdev/library/expo-architect
expo-architect
Installation
$ npx skills add https://github.com/shipshitdev/library --skill expo-architect
SKILL.md
Expo Architect

Create production-ready Expo React Native apps with:

Framework: Expo SDK 54 + React Native 0.83 + TypeScript
Navigation: Expo Router (file-based routing)
Auth: Clerk authentication (optional)
UI: NativeWind (Tailwind for RN) or StyleSheet
Quality: Biome linting + TypeScript strict mode
Package Manager: bun
What Makes This Different

Generates working mobile apps, not empty scaffolds:

Complete navigation structure with working screens
Optional Clerk authentication flow
Real UI components with proper styling
API client integration ready
Runs immediately with bun start
Workflow Summary
PRD Brief Intake - Extract app type, screens, features, auth needs
Auth Setup (if requested) - Clerk provider, sign-in/sign-up screens
Screen Generation - Tab or stack-based navigation
Component Generation - UI components, entity components, layouts
Quality Setup - Biome, TypeScript strict, path aliases
Verification - Run quality gate, report results
Usage
# Create app with PRD-style prompt
python3 scripts/init-expo.py \
  --root ~/www/myapp \
  --name "My App" \
  --brief "A fitness tracker where users can log workouts"

# With specific options
python3 scripts/init-expo.py \
  --root ~/www/myapp \
  --name "My App" \
  --tabs "Home,Workouts,Profile" \
  --auth

Generated Structure
myapp/
├── app/
│   ├── _layout.tsx          # Root layout
│   ├── (tabs)/              # Tab navigator
│   │   ├── _layout.tsx
│   │   ├── index.tsx
│   │   └── ...
│   └── (auth)/              # Auth screens (if enabled)
├── components/
│   ├── ui/                  # Base UI components
│   ├── [entity]/            # Feature components
│   └── layout/              # Layout components
├── lib/
│   ├── api.ts               # API client
│   └── auth.ts              # Auth utilities
├── providers/               # Context providers
├── types/                   # TypeScript types
├── app.json                 # Expo config
├── package.json
├── tsconfig.json
└── biome.json

Development Commands
bun start          # Start Expo dev server
bun run ios        # iOS simulator
bun run android    # Android emulator
bun run lint       # Check code style
bun run typecheck  # Type checking

Environment Variables
EXPO_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_test_...
EXPO_PUBLIC_API_URL=http://localhost:3001


For detailed patterns, code templates, and complete examples: references/full-guide.md

Weekly Installs
216
Repository
shipshitdev/library
GitHub Stars
21
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass