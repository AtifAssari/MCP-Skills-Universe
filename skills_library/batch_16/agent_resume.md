---
title: agent-resume
url: https://skills.sh/ahpxex/resume-cli/agent-resume
---

# agent-resume

skills/ahpxex/resume-cli/agent-resume
agent-resume
Installation
$ npx skills add https://github.com/ahpxex/resume-cli --skill agent-resume
SKILL.md
Agent Resume
Overview

Guide the user from raw career information to a final PDF created with resumy. Collect background information first, collect the target job description second, tailor truthful resume copy third, then render the output with the CLI.

Workflow
Collect candidate background first. Ask for basics, experience, projects, education, skills, links, and any output preferences. If the user already has an existing resume, profile, notes, or portfolio, extract facts from that artifact instead of re-asking everything.
Collect the target JD second. Ask for the full job description text, or at least the role summary, required skills, domain, and responsibilities.
Tailor the resume copy. Read references/intake-and-tailoring.md when you need the intake checklist, JD analysis steps, or rewrite rules. Reframe the user's real experience to match the job's priorities without inventing facts.
Map the tailored content into CLI flags. Read references/resumy-cli.md when you are ready to build the command. Use resumy templates if you need to inspect themes. Prefer professional unless the user asks for another style.
Render and verify. Run resumy generate pdf .... Add --html-output when you want a debuggable HTML artifact. Follow the Playwright and browser fallback notes in references/resumy-cli.md if PDF export fails.
Deliver the result. Share the PDF path, summarize how the resume was tailored to the JD, and note any assumptions or missing facts that still need confirmation.
Interaction Pattern
Start with candidate background before asking for the JD if both are missing.
After background intake, explicitly ask for the target JD.
After you have both, decide whether the user would benefit from a short tailoring plan before rendering. For higher-stakes applications, show the plan first. For straightforward requests, go straight to drafting and rendering.
Keep follow-up questions focused. Prefer grouped prompts over long interrogations.
Preserve truthfulness. Never invent employers, dates, metrics, degrees, tools, or responsibilities.
Rendering Rules
Keep the most relevant experience and projects near the top.
Trim weak or redundant bullets instead of overfilling the page.
Use JD terminology only when it matches the user's real background.
Prefer concise, impact-oriented bullets over generic responsibility lists.
Use --section-order when the user's story benefits from emphasizing projects, education, or custom sections.
References
references/intake-and-tailoring.md: use for candidate intake, JD analysis, and resume-copy rewriting.
references/resumy-cli.md: use for command construction, theme selection, output flags, and PDF troubleshooting.
Weekly Installs
17
Repository
ahpxex/resume-cli
GitHub Stars
41
First Seen
Mar 14, 2026
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykPass