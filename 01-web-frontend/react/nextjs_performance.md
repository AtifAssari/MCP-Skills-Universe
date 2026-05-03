---
title: nextjs-performance
url: https://skills.sh/srbhr/resume-matcher/nextjs-performance
---

# nextjs-performance

skills/srbhr/resume-matcher/nextjs-performance
nextjs-performance
Installation
$ npx skills add https://github.com/srbhr/resume-matcher --skill nextjs-performance
SKILL.md
Next.js Performance
Before Writing Code
Read docs/agent/architecture/nextjs-critical-fixes.md for full patterns
Check existing components in apps/frontend/components/
Critical Rules
Waterfalls
Use Promise.all() for independent fetches
Wrap slow data in <Suspense> boundaries
Defer await into branches where needed
// WRONG
const resumes = await fetchResumes();
const jobs = await fetchJobs();

// RIGHT
const [resumes, jobs] = await Promise.all([fetchResumes(), fetchJobs()]);

Bundle Size
NO barrel imports: import X from 'lucide-react' is WRONG
YES direct imports: import X from 'lucide-react/dist/esm/icons/x'
Use next/dynamic for heavy components (editors, charts, PDF)
Defer analytics with ssr: false
import dynamic from 'next/dynamic';
const HeavyEditor = dynamic(() => import('./HeavyEditor'), { ssr: false });

Server Actions
ALWAYS check auth INSIDE the action, not just middleware
Verify resource ownership before mutations
Production Build
Run npm run build && npm run start, NOT npm run dev
Docker must use standalone output
Pre-PR Checklist
[ ] No sequential awaits for independent data
[ ] Icons imported directly (not barrel)
[ ] Heavy components use next/dynamic
[ ] Server Actions have auth inside
[ ] Suspense around slow fetches

Weekly Installs
63
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