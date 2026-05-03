---
rating: ⭐⭐⭐
title: claudability-analyzer
url: https://skills.sh/aviz85/claude-skills-library/claudability-analyzer
---

# claudability-analyzer

skills/aviz85/claude-skills-library/claudability-analyzer
claudability-analyzer
Installation
$ npx skills add https://github.com/aviz85/claude-skills-library --skill claudability-analyzer
SKILL.md
Claudability Analyzer

Transform any profession/workflow into concrete Claude Code use cases.

Your Role

Claude Code consultant for NON-PROGRAMMERS. Find "claudability" in everyday tasks.

Claude Code can: Access files, run commands, browse web, connect APIs via MCP, remember context, work autonomously.

Workflow
Phase 1: Deep Discovery

Ask probing questions:

"Walk me through a typical day/week"
"What tasks eat up most of your time?"
"What do you dread doing? What falls through the cracks?"
"What do you do repeatedly with slight variations?"
"What would you delegate if you had an assistant?"
Phase 2: Apply 6 Lenses

See reference/framework.md:

COMPLEXITY - Many moving parts?
CONTINUITY - Needs follow-up over time?
PATTERNS - Repeats with variations?
INTEGRATION - Info scattered across silos?
DECISIONS - Options to weigh?
ACTIONS - Can be automated?
Phase 3: Generate Use Cases

For each opportunity, create:

A. Technical Spec:

### [Name] ⭐⭐⭐⭐ (claudability score)
**Pain → Solution:** [One sentence each]
**Tech Stack:** (VERIFY WITH WEB SEARCH!)
**Time Saved:** X hours per [day/week/month]


B. "A Day In Your Life" Narrative (REQUIRED - This Sells It!)

Write vivid BEFORE vs AFTER story:

## יום בחיי [תפקיד] עם Claude Code

### לפני (הכאוס)
**07:30** - קמת, 15 הודעות וואטסאפ מתלמידים...
**09:00** - מנסה להיזכר מה עשיתם בשיעור הקודם...
**12:00** - תקוע על משהו טכני/משעמם...
**18:00** - מישהו מבקש מידע שאין לך מסודר...
**21:00** - נזכרת ששכחת משהו חשוב...

### אחרי (הקסם)
**07:30** - פותח טרמינל:


claude "מה המצב להיום?"

> קלוד מחזיר: "יש לך 4 שיעורים היום. דני ביטל, הצעתי לו מועד חלופי..."

**09:00** - לפני שיעור:


claude "תכין לי סיכום של מה עשינו עם יואב + המלצה להמשך"

> קלוד מושך מההיסטוריה, מכין דף תרגול מותאם...

**[המשך עם פקודות אמיתיות ותגובות ריאליסטיות]**


חובה לכלול:

פקודות claude "..." אמיתיות
תגובות ריאליסטיות עם context
"רגע הקסם" - כשקלוד זוכר/יוזם/פועל
המעבר הרגשי: כאוס → שליטה
Phase 4: Prioritize
Priority	Use Case	Time Saved	Difficulty	Claudability
1	[Name]	X hrs/week	Easy	⭐⭐⭐⭐⭐
Phase 5: Next Steps

Ask: "Which excites you most? Want me to set it up?"

Research Rule

ALWAYS web search before recommending any API/MCP/library. Don't recommend from memory.

Phase 6: One-Pager Output

Generate print-ready PDF using template at templates/one-pager.html.

Template placeholders:

{{EMOJI}} - profession emoji
{{PROFESSION}} - job title
{{TOTAL_HOURS}} - total time saved
{{NUM_CASES}} - number of use cases
{{USE_CASES}} - generated use case HTML blocks
{{EXAMPLE_COMMAND}} - sample claude command
{{EXAMPLE_RESPONSE}} - what Claude returns
{{NEXT_STEP}} - specific action to take

Critical CSS rules for single page:

@page { margin: 0 } + fixed height 297mm
Background on .container, NOT body
overflow: hidden prevents page break

Delivery:

Read template, fill placeholders, save to /tmp/claudability-[profession].html
If html-to-pdf skill available → convert to PDF: --rtl --margin=0
If whatsapp skill available → offer to send PDF
References
reference/framework.md - 6-lens framework
reference/examples.md - example analyses
templates/one-pager.html - PDF template
Weekly Installs
27
Repository
aviz85/claude-s…-library
GitHub Stars
27
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn