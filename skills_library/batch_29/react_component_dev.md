---
title: react-component-dev
url: https://skills.sh/corvo007/miosub/react-component-dev
---

# react-component-dev

skills/corvo007/miosub/react-component-dev
react-component-dev
Installation
$ npx skills add https://github.com/corvo007/miosub --skill react-component-dev
SKILL.md
React Component Development Guidelines
Purpose

Establish consistency and best practices for React components in Gemini-Subtitle-Pro using React 19, TypeScript 5.8, and TailwindCSS 4.

When to Use This Skill

Automatically activates when working on:

Creating or modifying React components
Building pages, modals, dialogs, forms
Styling with TailwindCSS
Working with React hooks
Implementing state management
Performance optimization
Quick Start
New Component Checklist
 Location: Place in src/components/[feature]/
 TypeScript: Define proper props interface
 Styling: Use TailwindCSS with clsx and tw-merge
 Path Aliases: Use @components/*, @hooks/*, etc.
 State: Use appropriate state pattern (local, context, etc.)
 i18n: Use useTranslation for all user-facing text
Component Architecture
File Organization
src/components/
├── common/              # Shared components (Button, Modal, etc.)
├── layout/              # Layout components (Header, Sidebar, etc.)
├── subtitle/            # Subtitle-related components
├── settings/            # Settings components
├── workspace/           # Workspace components
└── [feature]/           # Feature-specific components

Naming Conventions
Components: PascalCase - SubtitleEditor.tsx
Hooks: camelCase with use prefix - useSubtitleParser.ts
Utils: camelCase - formatTimestamp.ts
Core Principles
1. Always Use Path Aliases
// ❌ NEVER: Relative paths
import { Button } from '../../components/common/Button';

// ✅ ALWAYS: Path aliases
import { Button } from '@components/common/Button';
import { useWorkspace } from '@hooks/useWorkspace';
import { SubtitleEntry } from '@types/subtitle';

2. Define Props Interface
// ✅ ALWAYS: Clear prop types
interface SubtitleEditorProps {
  entries: SubtitleEntry[];
  onUpdate: (index: number, entry: SubtitleEntry) => void;
  isReadOnly?: boolean;
}

export function SubtitleEditor({ entries, onUpdate, isReadOnly = false }: SubtitleEditorProps) {
  // ...
}

3. Use TailwindCSS with clsx
import { clsx } from 'clsx';
import { twMerge } from 'tailwind-merge';

// ✅ Conditional classes
<div className={twMerge(clsx(
  'rounded-lg p-4',
  isActive && 'bg-blue-500 text-white',
  isDisabled && 'opacity-50 cursor-not-allowed'
))}>

4. Use i18n for All Text
import { useTranslation } from 'react-i18next';

export function SettingsPanel() {
  const { t } = useTranslation();

  return (
    <h1>{t('settings.title')}</h1>
  );
}

Resource Files

For detailed guidelines, see the resources directory:

component-patterns.md - Component design patterns
styling-guide.md - TailwindCSS styling patterns
hooks-patterns.md - Custom hooks patterns
performance.md - Performance optimization
Weekly Installs
14
Repository
corvo007/miosub
GitHub Stars
421
First Seen
Feb 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass