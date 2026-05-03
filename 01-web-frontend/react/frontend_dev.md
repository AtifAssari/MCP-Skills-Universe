---
title: frontend-dev
url: https://skills.sh/srbhr/resume-matcher/frontend-dev
---

# frontend-dev

skills/srbhr/resume-matcher/frontend-dev
frontend-dev
Installation
$ npx skills add https://github.com/srbhr/resume-matcher --skill frontend-dev
SKILL.md
Frontend Development

Use when creating or modifying Next.js pages, React components, Tailwind CSS styles, API integration, hooks, or i18n.

Before Writing Code
Read docs/agent/architecture/frontend-workflow.md for user flow
Read docs/agent/design/style-guide.md for Swiss International Style (REQUIRED)
Read docs/agent/coding-standards.md for conventions
Check existing components in apps/frontend/components/
Non-Negotiable Rules
Swiss International Style - ALL UI changes must follow it
rounded-none everywhere - no rounded corners, ever
Hard shadows - shadow-[4px_4px_0px_0px_#000000], never soft shadows
Run npm run lint before committing
Run npm run format before committing
Enter key handling on all textareas
Swiss International Style Quick Reference
Element	Value
Canvas bg	#F0F0E8 / bg-[#F0F0E8]
Ink text	#000000
Hyper Blue	#1D4ED8 / text-blue-700
Signal Green	#15803D / text-green-700
Alert Red	#DC2626 / text-red-600
Headers	font-serif
Body	font-sans
Labels	font-mono text-sm uppercase tracking-wider
Borders	rounded-none border-2 border-black
Shadows	shadow-[4px_4px_0px_0px_#000000]
Hover	hover:translate-y-[1px] hover:translate-x-[1px] hover:shadow-none
Anti-Patterns (NEVER)
rounded-* (except rounded-none)
Gradients or blur shadows
Colors outside the palette
Pastel or soft colors
Decorative icons without function
Patterns
New Component
'use client';

interface MyComponentProps {
  title: string;
  onAction: () => void;
}

export function MyComponent({ title, onAction }: MyComponentProps) {
  return (
    <div className="bg-white border-2 border-black shadow-[4px_4px_0px_0px_#000000] p-6">
      <h3 className="font-serif text-xl mb-4">{title}</h3>
      <button
        onClick={onAction}
        className="rounded-none border-2 border-black px-4 py-2 bg-blue-700 text-white shadow-[2px_2px_0px_0px_#000000] hover:translate-y-[1px] hover:translate-x-[1px] hover:shadow-none transition-all"
      >
        Action
      </button>
    </div>
  );
}

Textarea (Enter key fix)
const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
  if (e.key === 'Enter') e.stopPropagation();
};

<textarea onKeyDown={handleKeyDown} className="w-full rounded-none border-2 border-black p-3 font-sans" />

Bundle Optimization
// Direct icon import (NOT barrel import)
import FileText from 'lucide-react/dist/esm/icons/file-text';

// Dynamic import for heavy components
import dynamic from 'next/dynamic';
const PDFViewer = dynamic(() => import('./PDFViewer'), { ssr: false });

API Integration
// Use Promise.all for independent fetches
const [resumes, jobs] = await Promise.all([
  api.get('/api/v1/resumes'),
  api.get('/api/v1/jobs'),
]);

Checklist
 npm run lint passes
 npm run format run
 rounded-none on all elements
 Hard shadows, Swiss palette only
 Correct typography (serif headers, mono labels, sans body)
 Textareas have Enter key handler
 Icons imported directly, heavy components use next/dynamic
 Independent fetches use Promise.all()
Weekly Installs
65
Repository
srbhr/resume-matcher
GitHub Stars
26.5K
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass