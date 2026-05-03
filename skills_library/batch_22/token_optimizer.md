---
title: token-optimizer
url: https://skills.sh/alexismunoz1/token-optimizer/token-optimizer
---

# token-optimizer

skills/alexismunoz1/token-optimizer/token-optimizer
token-optimizer
Installation
$ npx skills add https://github.com/alexismunoz1/token-optimizer --skill token-optimizer
SKILL.md
Token Optimizer

A comprehensive toolkit to reduce token consumption and lower AI costs — for both Claude Code users (file organization, CLAUDE.md, context hygiene) and API developers (prompt caching, Batch API, effort tuning, prompt architecture). Recommendations are backed by real experiment data and current Anthropic pricing.

Which sections apply to you:

Using Claude Code? → Sections 1-5 and the Quick Wins Checklist.
Calling the Anthropic API directly? → Also read references/api-optimization-guide.md. That's where the biggest savings live (prompt caching = 90% off, Batch API = 50% off, stackable).
Installation
npx skills add amunozdev/token-optimizer


Or manually:

cp -r token-optimizer ~/.claude/skills/

Core Features
1. File Organization Optimization

The single highest-impact optimization. Small, focused files reduce token consumption by 18.2% and noise by 92% on focused tasks (the majority of daily development work).

Core rules:

Maximum 150 lines per file — split by responsibility if longer
Single responsibility — one concern per file
Descriptive names in kebab-case — the filename tells the AI exactly what's inside

Real example: Fixing an email validation bug required reading 814 lines in a monolithic file (49,466 tokens) vs only 67 lines in a modular setup (40,447 tokens) — 18.2% savings, 92% less noise.

For naming conventions, avoid/prefer tables, and project structure templates, see references/file-organization-guide.md

2. CLAUDE.md Optimization

A well-structured CLAUDE.md can reduce token consumption by 50-70%. Most projects have bloated CLAUDE.md files that load unnecessary context on every interaction.

Key principles:

Keep it under 500 lines — essentials only
Be specific — "PostgreSQL with Prisma" not just "database"
Include project structure and commands — save the AI from guessing
Use triggers, not full docs — reference skills/files for details, don't inline everything

For a ready-to-use optimized template, see references/claude-md-template.md

3. Context Management

Token waste often comes from accumulated irrelevant context, not from individual operations.

Essential commands:

Command	When to Use	Effect
/clear	Switching tasks, after major corrections	Resets context completely
/compact	Long conversation (>50 exchanges)	Compresses history, keeps essentials
/context	Diagnosing high token use	Shows what's consuming tokens

Lazy loading: Don't front-load all information. One project achieved 54% reduction in initial tokens (7,584 → 3,434) by keeping only triggers in CLAUDE.md and loading details on demand.

For advanced strategies, subagent patterns, and MCP management, see references/context-management-guide.md

4. Strategic Model Selection

Choosing the right model per task type is one of the easiest cost savings to implement.

Task Type	Model	Why
80% of daily tasks	Sonnet	Best cost/performance ratio
Complex architecture	Opus	Deeper reasoning needed
Simple/quick tasks	Haiku	Up to 18x cheaper than Opus

Default to Sonnet. Escalate to Opus only for genuinely complex problems. Use Haiku for simple tasks, tests, and searches.

5. MCP & Subagent Optimization

MCP Management:

Keep maximum 10 active MCPs at a time (max 80 total tools)
Disable MCPs not needed for the current task
Each unused MCP still costs tokens in tool descriptions

Subagents for verbose tasks: Use the Task tool for operations that generate large output (test runs, builds, searches). The verbose output stays in the subagent's context — only the summary returns to your main conversation.

6. Prompt Architecture (Claude Code and API)

How you write prompts has a direct, measurable impact on tokens — in both directions.

Be direct, put the ask first, say it once. Repetition doesn't increase compliance, it just bills.
Constrain output explicitly. "Under 50 words", "max 3 bullets", "JSON with keys X, Y, Z, no explanation." Open-ended prompts produce open-ended (expensive) responses.
Use XML tags (<instructions>, <context>, <output_format>) to reduce ambiguity.
Include only relevant context. Don't paste 500 lines when one function is enough.
7. API-Only Optimizations

If you're calling the Anthropic API directly (SDK, custom agents, production apps), these are the highest-impact levers — most are absent when using Claude Code because the harness handles them for you.

Technique	Savings	Notes
Prompt caching	90% on cached reads	Cache writes cost 1.25x, reads 0.1x. Pays for itself on 2nd call.
Batch API	50% on all tokens	<24h latency. Stacks with caching → up to 95% total.
effort: low	Large reduction	Skip deep reasoning for classification/extraction.
budget_tokens cap	Proportional	8K-16K is plenty for most tasks. Don't use 100K to format a date.
Prefill assistant turn	Removes preamble	{"role": "assistant", "content": "{"} skips "Sure! Here's…".
Token-efficient tools	~14% output avg	Default in Claude 4. Add token-efficient-tools-2025-02-19 header for 3.7.
Dynamic tool loading	Scales with tool count	Every tool schema ships in every request. Only include what the task needs.
Token counting endpoint	Debugging	Get exact cost before running inference.

Critical cache gotchas:

Images break the cache. Adding or removing an image anywhere in the prompt invalidates it. If your flow sometimes sends images, treat it as a separate request pattern.
Anything before the cache breakpoint must be stable. Timestamps, session IDs, or the user message placed before the breakpoint defeat caching entirely — you pay the 1.25x write surcharge every time with zero reads.
Concurrency pitfall. Cache entries become available only after the first response starts streaming. Fire-and-forget 10 parallel requests → 9 cache misses. Fire one, wait for stream to start, then fan out.
Mind the minimum token threshold per breakpoint (2,048 for Sonnet 4.6; 4,096 for Opus 4.6 and Haiku 4.5). Below it, nothing caches and no error is raised. Verify cache_creation_input_tokens in the response.

Full details, pricing math, TTL tradeoffs, and a setup checklist: references/api-optimization-guide.md

Quick Wins Checklist

Apply these in order of impact:

Run /context first → establishes your baseline before any changes
Split large files (>150 lines) into focused modules → saves 18%+ tokens
Optimize your CLAUDE.md → can reduce consumption 50-70%
Use /clear between tasks → eliminates irrelevant context
Use /compact in long conversations → compresses history
Use subagents for verbose tasks → test output, build logs, and search results stay in subagent context instead of polluting your main conversation
Use the right model → default to Sonnet for daily work, Haiku for simple tasks (18x cheaper than Opus), Opus only for genuinely complex architecture decisions
Limit active MCPs to ≤10 → each unused MCP still costs tokens every turn because its tool descriptions are sent in every request
Track cost with /cost → use it to see spend per session; configure the statusline to display it continuously
API users: enable prompt caching → cache_control on system prompt and tools = 90% off on repeated input; see references/api-optimization-guide.md
Expected Savings

Results from our controlled experiment with an 814-line TypeScript e-commerce app:

Optimization	Impact
Modular files (focused tasks)	-18.2% tokens
Noise reduction (lines processed)	-92%
Optimized CLAUDE.md	-50-70% consumption
Lazy loading context	-54% initial tokens
Haiku vs Opus (simple tasks)	-94% cost

Key insight: Focused tasks (bug fixes, specific changes — ~80% of daily work) benefit enormously from modular code. Cross-cutting tasks show minimal difference at small scale (+1-5%) but modular wins decisively at 5,000+ lines.

Note on scale: These results are from a controlled experiment with an 814-line codebase. At larger scales (5,000+ lines), the savings from modular architecture are even more significant because monolithic files start hitting context window limits while modular files maintain constant size (35-146 lines each).

For the complete experiment methodology and raw data, see references/metrics-report.md

Diagnostic Workflow

When activated, follow this process:

Measure first: Always start by asking the user to run /context. Without a baseline number, you can't prove any optimization worked. This step is not optional.
Read the user's code: Before recommending anything, look at their actual files and project structure. Scan for files >150 lines, check their CLAUDE.md size, and count active MCPs. Recommendations grounded in their real codebase are far more useful than generic advice.
Identify: Determine the biggest source of waste (large files, bloated CLAUDE.md, accumulated context, too many MCPs)
Recommend: Suggest the highest-impact optimization from the Quick Wins Checklist
Verify: After changes, have the user re-run /context to measure improvement

Important guidelines:

Always diagnose first — don't dump all optimizations
Measure before and after — every optimization should be verified with /context
Focus on the user's specific problem — identify the most impactful change first
Be transparent about trade-offs — modular files save 18%+ on focused tasks but show minimal difference on cross-cutting tasks at small scale
Usage Examples
"My Claude Code sessions are getting expensive"
Run /context to see current token consumption breakdown
Audit CLAUDE.md size — if over 500 lines, trim to essentials
Check for files >150 lines — identify candidates for splitting
Count active MCPs — disable unused ones
Review model usage — switch routine tasks to Sonnet/Haiku
"Organize my codebase for AI"
Scan the project for files exceeding 150 lines
Identify generic filenames (utils.ts, helpers.ts, index.ts with logic)
Propose file splits by responsibility with new descriptive names
Suggest a project structure following the organization guide
"My context window keeps filling up"
Run /context to identify what's consuming tokens
Check if CLAUDE.md has inline documentation that should be referenced instead
Recommend /clear between tasks and /compact for long sessions
Suggest moving verbose content to referenced files (lazy loading)
Troubleshooting
Problem	Cause	Solution
No improvement after optimizations	No baseline measurement taken	Run /context before AND after each change
Don't know how many tokens I'm using	Token consumption not visible by default	Use /context to see the full breakdown
/compact doesn't reduce enough	Compresses but keeps essentials	Use /clear if prior context is irrelevant
Cross-cutting tasks slower after splitting	Multiple reads needed (1-5% more tokens)	Expected and marginal — focused tasks (80% of work) still save 18%+
API: cache seems not to work, writes every call	Content before breakpoint changes every request (timestamp, session ID, user msg) OR below minimum tokens OR image added/removed	Check cache_creation_input_tokens — move volatile content after the breakpoint and meet per-model minimums
API: parallel requests all miss cache	Cache entry only exists after first response streams	Fire first request, wait for stream to start, then fan out the rest
API: thinking tokens making requests expensive	Default budget_tokens can be tens of thousands	Cap budget_tokens at 8K-16K, or set effort: low, or disable thinking for formatting/lookup tasks
Reference Materials
references/file-organization-guide.md — Naming conventions, project structure templates, and implementation checklist
references/context-management-guide.md — Lazy loading, subagents, MCP management, and model selection strategies
references/metrics-report.md — Complete experiment data and methodology with raw numbers
references/claude-md-template.md — Ready-to-use optimized CLAUDE.md template
references/api-optimization-guide.md — Prompt caching, Batch API, effort/thinking budget, prefill, token-efficient tools, and monitoring for direct API users
Weekly Installs
67
Repository
alexismunoz1/to…ptimizer
GitHub Stars
4
First Seen
Feb 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass