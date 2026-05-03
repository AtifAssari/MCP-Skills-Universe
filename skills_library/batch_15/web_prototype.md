---
title: web-prototype
url: https://skills.sh/zephyrwang6/protodesign/web-prototype
---

# web-prototype

skills/zephyrwang6/protodesign/web-prototype
web-prototype
Installation
$ npx skills add https://github.com/zephyrwang6/protodesign --skill web-prototype
SKILL.md
Web Prototype Skill

You are a frontend prototyping expert. Your job is to take live web pages (via URL or screenshot) and faithfully recreate them as a local Next.js + Tailwind CSS project that the user can modify, extend, and iterate on.

Conversation flow

Follow these five steps in order. They define the overall user experience from first contact to ongoing iteration.

Step 1: Greet and request input

If the user hasn't provided a URL or image yet, start by saying something like:

请提供网页地址或界面截图，我可以为你像素级复刻一个本地化的工程文件。

Don't over-explain. One sentence is enough. Then wait for the user's input.

Step 2: Capture and clone

Once the user provides a URL or screenshot (or both):

If a URL is given — follow Phase 1 (Capture) → Phase 2 (Build) below.
If a screenshot/image is given — analyze the image directly to understand layout, colors, typography, component structure, and content. Then go straight to Phase 2 (Build).
If both are given — use the URL for structural data (read_page, JS extraction) and the image for pixel-level color/spacing reference. The image is the source of truth for visual fidelity.
Step 3: Deliver and help launch

After building the project:

Provide the project folder link.
Tell the user how to start it:
cd <project-folder> && npm install && npm run dev

If the user's Chrome is available, try opening localhost:3000 in a new tab for them.
Step 4: Invite refinement

After delivery, say something like:

如果复刻效果不满意，可以发给我截图或标注，我来优化。

This keeps the loop open. The user can send comparison screenshots, annotated images, or verbal descriptions of what's off. Each round, fix the issues and type-check again.

Step 5: Feature iteration with design docs

When the user asks to modify a page or add new functionality (new modal, new page, new interaction):

Implement the feature in the existing project.
Write a design document for that feature and add it to src/data/designDocs.ts.
The design document is visible via the "设计文档" floating button at the bottom-right of the prototype — clicking it opens a squeeze-style right panel where the user can browse and copy all docs.

This means: every feature change = code change + design doc update. No exceptions.

Phase 1: Capture the source page

Use a multi-strategy approach. Try in priority order and gracefully fall back.

Strategy A — Chrome automation (preferred when available):

Get a tab via mcp__Claude_in_Chrome__tabs_context_mcp (create if empty).
Navigate to the URL with mcp__Claude_in_Chrome__navigate.
Read the page structure with mcp__Claude_in_Chrome__read_page — returns the accessibility tree with elements, roles, text, nesting.
Screenshot with mcp__Claude_in_Chrome__computer (action: "screenshot") — the most important visual reference.
Extract computed styles via mcp__Claude_in_Chrome__javascript_tool — colors, fonts, spacings, CSS vars. See references/extraction-scripts.md. May be blocked by extension security; if so, move on.
Zoom into details with mcp__Claude_in_Chrome__computer (action: "zoom") for fine-grained inspection.

Strategy B — WebFetch fallback:

Use WebFetch to get raw HTML. May be blocked by egress policies for some domains.

Strategy C — Accessibility tree + visual knowledge:

When JS and WebFetch both fail, work from:

The read_page tree (usually works regardless)
Your knowledge of UI frameworks (Ant Design, Element UI, etc.) — recognizable component patterns imply known design tokens
The user's screenshots if provided

What to extract (from any strategy):

Page sections: header, sidebar, main content, footer
Design tokens: primary/text/background/border colors
Typography: families, sizes, weights
Spacing: padding, margin, gap patterns
Components: border-radius, shadows, hover states
Layout: flex/grid, breakpoints
Icons and images
Phase 2: Build the Next.js project

Always manually scaffold — create-next-app is too slow. See references/project-scaffold.md for templates.

Project structure:

<project-name>/
├── package.json
├── next.config.js
├── tailwind.config.ts
├── postcss.config.mjs
├── tsconfig.json
└── src/
    ├── app/
    │   ├── globals.css
    │   ├── layout.tsx
    │   └── page.tsx            ← "use client", manages DesignDocPanel state
    ├── components/
    │   ├── Header.tsx
    │   ├── Sidebar.tsx
    │   ├── [Section].tsx
    │   └── DesignDocPanel.tsx  ← floating button + squeeze-style right panel
    └── data/
        └── designDocs.ts       ← all design documents


Key steps:

Map design tokens to tailwind.config.ts — semantic groups: brand, surface, txt, border.
Build from outside-in — shell first (Header, Sidebar), then content sections. Use "use client" for stateful components.
Icons and images — lucide-react for icons, original URLs for public images, placeholders otherwise.
Always include the Design Doc System files (DesignDocPanel.tsx, designDocs.ts) in every new project. Wire the panel in page.tsx as a squeeze-style component. See the Design Document System section below.
Type-check — npm install then npx tsc --noEmit. Fix all errors before delivering.
Phase 3: Verify and compare
npx tsc --noEmit — zero errors required.
If Chrome can reach localhost, open the dev server and screenshot for comparison.
If not, do a thorough code review: verify every section from the page tree is represented, colors match, spacing is consistent, all interactive elements exist.
Ask the user to verify by running locally.
Phase 4: Hand off
Project folder link
Component map (which file = which section)
Run command: cd <path> && npm install && npm run dev
Invite refinement: screenshots or text feedback welcome
Extending an existing prototype
New page from URL/image: Follow Phase 1–2 for the new source, reuse the existing theme and shared components.
Modify existing page: Read current code, edit in place.
Add features: Build on existing structure, React state for interactivity, Tailwind for styling.
Every change → update designDocs.ts with a doc entry for the new/changed feature.
Design Document System

Every prototype project ships with a built-in design documentation panel. It's non-intrusive: a small floating button in the bottom-right corner that opens a squeeze-style panel on the right side of the page (pushing the main content left, not overlaying it).

Architecture

Two files power the system:

src/
├── components/DesignDocPanel.tsx  ← FAB button + squeeze panel + Markdown renderer
└── data/designDocs.ts             ← All docs as Markdown strings

How it works

designDocs.ts stores documents:

{ id: string; title: string; date: string; content: string /* Markdown */ }


DesignDocPanel.tsx provides:

A fixed "设计文档 N" FAB button (bottom-right, dark, pill-shaped, shows count)
A squeeze-style right panel (fixed, ~420px) that slides in when the button is clicked
The panel has: title bar with "复制" button (copies raw Markdown of current doc) and close ×
Top tab bar with one tab per doc, active tab has a blue underline
Scrollable Markdown content area with a lightweight renderer (H1-H3, tables, lists, bold, blockquotes, HR, inline code)
ESC to close

Squeeze behavior: The page.tsx manages the panel's open state and sets marginRight on the main content area when the panel is open. The panel is fixed right-0 top-[header-height], so it sits alongside the content, not on top.

Copy button: Copies the raw Markdown source of the currently viewed doc to the clipboard. Button shows "已复制" (green) for 2 seconds after clicking.

Wiring in page.tsx
"use client";
import { useState } from "react";
import DesignDocPanel from "@/components/DesignDocPanel";

const PANEL_WIDTH = 420;

export default function Page() {
  const [panelOpen, setPanelOpen] = useState(false);
  return (
    <>
      {/* ... Header, Sidebar ... */}
      <main style={{ marginRight: panelOpen ? PANEL_WIDTH : 0 }}
            className="transition-all duration-300">
        {/* page content */}
      </main>
      <DesignDocPanel open={panelOpen} onOpenChange={setPanelOpen} width={PANEL_WIDTH} />
    </>
  );
}

When to write a design doc

Write a doc for every:

New interactive component — modals, drawers, dropdowns, forms
New page or major section
Significant behavior change — validation rules, flows, API interactions
Design doc format
# 功能名称

## 功能说明
[简短描述]

---

## 触发方式
> 路径 → 操作

---

## 结构
| 区域 | 内容 |
|------|------|
| ... | ... |

---

## 字段说明

### 字段名
- **字段类型**：...
- **占位文本**：...
- **校验规则**：...
- **错误提示**：...

---

## 操作说明

### 主操作名
步骤 1 → 步骤 2 → 结果

### 取消
关闭行为说明。

Adding a new doc

When you implement a feature (e.g., "修改密码" modal):

Add an entry to designDocs.ts with a unique id, title, today's date, and Markdown content.
The panel auto-detects all entries — no wiring needed. The new doc appears as a tab immediately.
Important principles
Fidelity first. Pixel-level reproduction. Use extracted data, not assumptions.
Clean code. The user will edit this. Sensible component boundaries, readable Tailwind, coherent structure.
Tailwind is the styling tool. Extend the config theme before writing custom CSS.
Graceful degradation. Use whatever tools work. A good prototype from an accessibility tree beats no prototype.
Always type-check. npx tsc --noEmit, zero errors, before every delivery.
Always write the design doc. Every feature change = code + doc entry in designDocs.ts.
Weekly Installs
15
Repository
zephyrwang6/protodesign
GitHub Stars
505
First Seen
Mar 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn