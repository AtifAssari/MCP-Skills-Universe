---
title: vitepress-tutorial
url: https://skills.sh/howell5/willhong-skills/vitepress-tutorial
---

# vitepress-tutorial

skills/howell5/willhong-skills/vitepress-tutorial
vitepress-tutorial
Installation
$ npx skills add https://github.com/howell5/willhong-skills --skill vitepress-tutorial
SKILL.md
VitePress Source Tutorial Generator

Generate VitePress documentation sites for source code learning and analysis.

Overview

This skill creates standalone VitePress tutorial sites that teach developers how a codebase works internally. Unlike user documentation that explains "how to use", these tutorials explain "how it's implemented".

Usage
/vitepress-tutorial [task-description]


Examples:

/vitepress-tutorial 帮我解析这个仓库的架构
/vitepress-tutorial explain the agent system in detail
Workflow
Phase 1: Project Analysis & Setup (REQUIRED FIRST)
Detect project type - Identify language, framework, monorepo structure
Ask user for preferences - Use AskUserQuestion tool to confirm:
Output directory path (suggest reasonable default based on project structure)
Tutorial focus areas (if not specified in the task)
Content language(s) - Which language(s) to generate content in (see Language Selection below)
Create project skeleton immediately - After user confirms:
Create directory structure
Write package.json with Mermaid plugin
Write .vitepress/config.ts
Write pnpm-workspace.yaml (if inside another workspace)
Run pnpm install
Phase 2: Deep Analysis
Explore source directory using Task tool with Explore agent
Identify key components, patterns, and architecture
Map dependencies and data flows
Build mental model of module interactions
Phase 3: Content Generation
Generate all documentation files based on analysis
Include Mermaid diagrams for architecture visualization
Reference actual source code with file:line annotations
Build and verify the site works
CRITICAL INSTRUCTIONS
Ask Before Writing

ALWAYS use AskUserQuestion to confirm output location AND content language before creating any files.

Use two questions in one AskUserQuestion call:

Question 1: "Where should I create the VitePress tutorial site?"
Options:
- "./docs" (project docs folder)
- "./tutorials/{project-name}" (dedicated tutorials folder)
- Custom path...

Question 2: "What language(s) should the tutorial content be written in? (Max 2)"
multiSelect: true
Options:
- "中文 (Chinese)" - Content in Chinese, code comments in English
- "English" - Content and code comments in English
- "日本語 (Japanese)" - Content in Japanese, code comments in English
- "한국어 (Korean)" - Content in Korean, code comments in English

Language Selection Rules
Max 2 languages - If user selects more than 2, ask them to narrow down. Mention they can run the skill again later to add more languages.
Single language - Generate content directly under docs/ with no locale prefix. Set lang in config accordingly.
Two languages - Use VitePress i18n with locale-based directory structure:
First selected language → root / (default locale)
Second selected language → /{locale-code}/ prefix
Configure locales in .vitepress/config.ts with proper labels and nav/sidebar for each locale
Add language switcher in navbar automatically
Language-to-locale mapping: zh-CN (Chinese), en-US (English), ja (Japanese), ko (Korean)
Content language only affects prose - Code snippets, file paths, and technical terms stay in English regardless of content language
Standalone Project Setup

When creating inside an existing pnpm workspace, ALWAYS create these files to make it independent:

pnpm-workspace.yaml (in tutorial root):

# Independent workspace - prevents inheriting parent config
packages: []


package.json (MUST include):

{
  "name": "{tutorial-name}",
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vitepress dev docs",
    "build": "vitepress build docs",
    "preview": "vitepress preview docs"
  },
  "devDependencies": {
    "mermaid": "^11.4.0",
    "vitepress": "^1.6.3",
    "vitepress-plugin-mermaid": "^2.0.17"
  },
  "pnpm": {
    "onlyBuiltDependencies": ["esbuild"]
  }
}

Config with Mermaid

docs/.vitepress/config.ts (MUST use withMermaid wrapper):

import { defineConfig } from 'vitepress'
import { withMermaid } from 'vitepress-plugin-mermaid'

export default withMermaid(defineConfig({
  // CRITICAL: Fix Mermaid's dayjs ESM compatibility issue
  vite: {
    optimizeDeps: {
      include: ['mermaid', 'dayjs']
    }
  },
  // ... rest of config
  mermaid: {
    theme: 'default'
  }
}))


Why vite.optimizeDeps? Mermaid depends on dayjs which is a CommonJS module. Without this config, Vite dev server will throw "does not provide an export named 'default'" error.

Install Dependencies

After creating project files, ALWAYS run:

cd {output-path} && pnpm install

Output Structure
Single Language
{output-path}/
├── package.json              # With mermaid plugin
├── pnpm-workspace.yaml       # If inside another workspace
├── README.md
└── docs/
    ├── .vitepress/
    │   └── config.ts         # With withMermaid wrapper
    ├── index.md              # Homepage
    ├── introduction/
    │   ├── overview.md       # Project overview
    │   └── architecture.md   # Architecture diagram
    └── {modules}/            # One directory per module
        ├── index.md
        └── {topics}.md

Two Languages (i18n)
{output-path}/
├── package.json
├── pnpm-workspace.yaml
├── README.md
└── docs/
    ├── .vitepress/
    │   └── config.ts         # With locales config + withMermaid
    ├── index.md              # Default locale homepage
    ├── introduction/         # Default locale content
    │   ├── overview.md
    │   └── architecture.md
    ├── {modules}/
    │   ├── index.md
    │   └── {topics}.md
    └── {locale}/             # e.g. "en" or "zh"
        ├── index.md          # Second locale homepage
        ├── introduction/
        │   ├── overview.md
        │   └── architecture.md
        └── {modules}/
            ├── index.md
            └── {topics}.md

Features
Mermaid Diagrams: Architecture, sequence, and flow diagrams (auto-installed)
Source References: Auto-generate Source: path/to/file.go:123 annotations
Code Highlighting: Go, TypeScript, Python with line highlighting
Multi-language Support: Choose up to 2 languages per run (Chinese, English, Japanese, Korean). Run again to add more languages later.
Standalone Deploy: Ready for Vercel, Netlify, or GitHub Pages
Content Guidelines
Always explore first - Read source files before writing tutorials
Reference actual code - Include real code snippets with file paths
Use Mermaid for architecture - Visual diagrams aid understanding
Keep chapters focused - One concept per file, ~200-400 lines
Link between chapters - Use VitePress prev/next navigation
Include API tables - Summarize endpoints, functions, types
Supporting Files
@config-template.md - VitePress configuration template
@project-structure.md - Project structure and file templates
@content-guidelines.md - Content writing guidelines
Weekly Installs
22
Repository
howell5/willhong-skills
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass