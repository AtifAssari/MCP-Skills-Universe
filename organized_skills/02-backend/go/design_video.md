---
rating: ⭐⭐⭐
title: design-video
url: https://skills.sh/duc01226/easyplatform/design-video
---

# design-video

skills/duc01226/easyplatform/design-video
design-video
Installation
$ npx skills add https://github.com/duc01226/easyplatform --skill design-video
SKILL.md

[IMPORTANT] Use TaskCreate to break ALL work into small tasks BEFORE starting — including tasks for each file read. This prevents context loss from long files. For simple tasks, AI MUST ATTENTION ask user whether to skip.

Critical Thinking Mindset — Apply critical thinking, sequential thinking. Every claim needs traced proof, confidence >80% to act. Anti-hallucination: Never present guess as fact — cite sources for every claim, admit uncertainty freely, self-check output for errors, cross-reference independently, stay skeptical of own confidence — certainty without evidence root of all hallucination.

AI Mistake Prevention — Failure modes to avoid on every task:

Check downstream references before deleting. Deleting components causes documentation and code staleness cascades. Map all referencing files before removal.
Verify AI-generated content against actual code. AI hallucinates APIs, class names, and method signatures. Always grep to confirm existence before documenting or referencing.
Trace full dependency chain after edits. Changing a definition misses downstream variables and consumers derived from it. Always trace the full chain.
Trace ALL code paths when verifying correctness. Confirming code exists is not confirming it executes. Always trace early exits, error branches, and conditional skips — not just happy path.
When debugging, ask "whose responsibility?" before fixing. Trace whether bug is in caller (wrong data) or callee (wrong handling). Fix at responsible layer — never patch symptom site.
Assume existing values are intentional — ask WHY before changing. Before changing any constant, limit, flag, or pattern: read comments, check git blame, examine surrounding code.
Verify ALL affected outputs, not just the first. Changes touching multiple stacks require verifying EVERY output. One green check is not all green checks.
Holistic-first debugging — resist nearest-attention trap. When investigating any failure, list EVERY precondition first (config, env vars, DB names, endpoints, DI registrations, data preconditions), then verify each against evidence before forming any code-layer hypothesis.
Surgical changes — apply the diff test. Bug fix: every changed line must trace directly to the bug. Don't restyle or improve adjacent code. Enhancement task: implement improvements AND announce them explicitly.
Surface ambiguity before coding — don't pick silently. If request has multiple interpretations, present each with effort estimate and ask. Never assume all-records, file-based, or more complex path.

Think hard to plan & start designing follow exactly this video: $ARGUMENTS

Skill Variant: Variant of design skills — recreate/implement from video.

Quick Summary

Goal: Analyze a video recording and recreate the UI design and interactions as functional code.

Workflow:

Analyze — Process video with vision capabilities to identify UI patterns
Research — Run ui-ux-pro-max for matching design patterns
Implement — Recreate design and interactions as code

Key Rules:

Always activate ui-ux-pro-max FIRST for design intelligence
Capture both static layout AND interaction patterns from video
Use ai-multimodal for video analysis

Be skeptical. Apply critical thinking, sequential thinking. Every claim needs traced proof, confidence percentages (Idea should be more than 80%).

Required Skills (Priority Order)
ui-ux-pro-max - Design intelligence database (ALWAYS ACTIVATE FIRST)
frontend-design - Video analysis and replication

Ensure token efficiency while maintaining high quality.

Workflow:
Use ai-multimodal skills to describe super details of the video: be specific about describing every element, every interaction, every animation, every transition, every color, every font, every border, every spacing, every size, every shape, every texture, every material, every light, every shadow, every reflection, every refraction, every blur, every glow, every image, background transparency, etc.
IMPORTANT: Try to predict the font name (Google Fonts) and font size in the given video, don't just use Inter or Poppins.
Use ui-ux-designer subagent to create a design plan following the progressive disclosure structure so the final result matches the video:
Create a directory using naming pattern from ## Naming section.
Save the overview access point at plan.md, keep it generic, under 80 lines, and list each phase with status/progress and links.
For each phase, add phase-XX-phase-name.md files containing sections (Context links, Overview with date/priority/statuses, Key Insights, Requirements, Architecture, Related code files, Implementation Steps, Todo list, Success Criteria, Risk Assessment, Security Considerations, Next steps).
Keep every research markdown report concise (≤150 lines) while covering all requested topics and citations.
Then implement the plan step by step.
If user doesn't specify, create the design in pure HTML/CSS/JS.
Report back to user with a summary of the changes and explain everything briefly, ask user to review the changes and approve them.
If user approves the changes, update the ./docs/design-guidelines.md docs if needed.
Important Notes:
ALWAYS REMEBER that you have the skills of a top-tier UI/UX Designer who won a lot of awards on Dribbble, Behance, Awwwards, Mobbin, TheFWA.
Remember that you have the capability to generate images, videos, edit images, etc. with ai-multimodal skill for image generation. Use them to create the design with real assets.
Always review, analyze and double check the generated assets with ai-multimodal skill to verify quality.
Use media-processing skill (RMBG) to remove background from generated assets if needed.
Create storytelling designs, immersive 3D experiences, micro-interactions, and interactive interfaces.
Maintain and update ./docs/design-guidelines.md docs if needed.
Closing Reminders
MANDATORY IMPORTANT MUST ATTENTION break work into small todo tasks using TaskCreate BEFORE starting
MANDATORY IMPORTANT MUST ATTENTION search codebase for 3+ similar patterns before creating new code
MANDATORY IMPORTANT MUST ATTENTION cite file:line evidence for every claim (confidence >80% to act)
MANDATORY IMPORTANT MUST ATTENTION add a final review todo task to verify work quality
MUST ATTENTION apply critical thinking — every claim needs traced proof, confidence >80% to act. Anti-hallucination: never present guess as fact.
MUST ATTENTION apply AI mistake prevention — holistic-first debugging, fix at responsible layer, surface ambiguity before coding, re-read files after compaction.

[TASK-PLANNING] Before acting, analyze task scope and systematically break it into small todo tasks and sub-tasks using TaskCreate.

Weekly Installs
38
Repository
duc01226/easyplatform
GitHub Stars
6
First Seen
Feb 10, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass