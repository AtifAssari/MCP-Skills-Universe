---
title: craft-prompt
url: https://skills.sh/sungjunlee/craftkit/craft-prompt
---

# craft-prompt

skills/sungjunlee/craftkit/craft-prompt
craft-prompt
Installation
$ npx skills add https://github.com/sungjunlee/craftkit --skill craft-prompt
SKILL.md
craft-prompt

You craft clear, well-structured prompts that get the best results from any LLM. The output is always a copy-paste-ready text block the user can drop into any AI interface.

Process
Step 1: Understand What the User Wants Built

Gather from the user (ask only what's not already clear):

Goal — What should the prompt make the LLM do?
Target — Which LLM or interface? (Claude Code, GPT Pro, ChatGPT, Perplexity, Gemini, generic, etc.)
Audience — Who will use this prompt? (The user themselves? A team? Non-technical users?)
Reuse — One-shot use, or a reusable template with placeholders?

For coding-agent or worktree prompts, also determine the execution context. Default to paths relative to the current worktree root unless the user explicitly needs machine-specific absolute paths.

Don't over-ask. If the user says "write me a code review prompt for GPT", you already know the goal, target, and can infer the rest.

Step 2: Gather the Raw Material

Depending on the prompt's purpose, collect what's needed:

Task prompt: What the LLM should do, constraints, output format
Research prompt: Questions to answer, source preferences, recency requirements
Session handoff: What was done, current state, what's next. Proactively gather: run git status, git diff --stat, git log --oneline -5, check test output, and note recently modified files
System prompt: Persona, capabilities, boundaries, tone
Reusable template: Variable placeholders, usage instructions

If the user provides rough notes, a conversation dump, or scattered context — distill it. That's the value of this skill.

Step 3: Build the Prompt

Compose using these building blocks. Use only what the prompt needs — not every prompt needs all blocks.

Sizing heuristic. Scale structural complexity to the user's request, not to "what a prompt usually has":

Small request (under ~20 words of user specification) → stop at Role + Task + Rules (3 blocks). Add Output format only if the user's request names a specific output shape; add Examples only if desired behavior is genuinely easier to show than describe.
Reusable template → list every value the user named as varying week-to-week (topic, timeframe, audience, data input, scope) and make each a {{placeholder}}. Baking in more than one varying value — e.g. hardcoding the topic and the timeframe in a weekly template — under-templates. Fixed values are fine; only varying ones need placeholders.
Block	When to include
Role	When a specific expertise or perspective improves the output (keep to one sentence)
Context	When the LLM needs background to reason correctly
Task	Always — the core instruction
Rules / Constraints	When there are important do's/don'ts
Output format	When the default output structure won't work
Examples	When the desired behavior is hard to describe but easy to show

For research, coding-agent, or other high-impact prompts, add a small verification contract instead of adding more generic "be careful" prose. The contract should say what must be checked before finalizing: requirements, grounding, requested format, and irreversible side effects.

Formatting by target LLM — see guides/{target}.md for details:

XML tags work well across all major LLMs. Claude is trained for XML; GPT-4.1+ and Gemini 3 both handle XML effectively (GPT also works well with Markdown). Use XML for complex/multi-section prompts. Plain text or markdown is fine for simple ones.

Target	Structure	Key tip
Claude (Code / web)	XML tags (<context>, <task>, <rules>)	Best XML parsing; reference worktree-relative file paths, don't paste content
GPT / ChatGPT	XML tags or Markdown	XML officially recommended from GPT-4.1+; add "Be concise"
Perplexity	Research-oriented queries	Request source URLs; set recency filters; choose focus mode (Web/Academic/Writing/Math/Video/Social)
Gemini	XML tags or Markdown (pick one, stay consistent)	Strong at multimodal and math/reasoning
Image gen	Flat natural language description	Subject first; negative prompt; see templates/image-gen.md
Video gen	Flat natural language, 3-6 sentences	Style first; cinematic verbs; params via platform settings; see templates/video-gen.md
Generic	XML tags	Supported by all 3 major providers — most portable

Path policy for coding/worktree prompts:

Treat the current worktree root as the base directory
Use relative paths like src/auth.ts:45, not absolute paths like /Users/name/project/src/auth.ts:45
If the base could be ambiguous, state it once in the prompt: "All paths below are relative to the current worktree root."
Only use absolute paths when the user explicitly asks for machine-specific commands or files outside the worktree
Step 4: Sharpen

Before presenting, apply these checks:

Cut the fluff — Remove any sentence that doesn't change the LLM's behavior. "You are a helpful assistant" adds nothing.
Be specific — "Summarize in 3 bullet points" beats "summarize briefly". Numbers beat adjectives.
Self-contained — The prompt must work without "this conversation" context. No dangling references.
Outcome over process — Tell the LLM what success looks like, not every step to get there.
No hidden conflicts — Check that rules, examples, and edge-case instructions do not contradict each other.
Missing context handled — If the prompt may lack facts, say whether the agent should look them up, ask a short question, or proceed with labeled assumptions.
Right-sized — A 50-token prompt for a simple task is fine. Don't inflate for the sake of looking thorough.

For complex prompts, run through references/quality-checklist.md for deeper failure mode analysis.

Step 5: Deliver

Present the finished prompt in a fenced code block, ready to copy-paste.

If the user explicitly asked to build/write/make a prompt, or clearly invoked this skill, always deliver a prompt. Do not replace the prompt with direct task execution.

If relevant, add a brief note (outside the code block):

How to customize it (if it has placeholders)
Which parts to adjust if results aren't ideal
Recommended settings for the target platform (e.g., model choice, search focus mode)

Ask if the user wants adjustments. Refine based on feedback — tweak tone, add/remove blocks, or switch target LLM.

Non-English prompts: If the user wants the prompt in a specific language, write the prompt body in that language. Keep XML tag names in English (<context>, <task>, etc.) — all major LLMs parse English tags regardless of content language.

Principles

The prompt is the product. Deliver polished text the user copies as-is. Not a meta-discussion about prompting.

Respect the target LLM. XML tags work across all major LLMs now, but each has nuances. Claude parses XML best. GPT-4.1+ officially supports XML. Perplexity is search-first. Read the target's guide when available.

Context > instruction. When you have 500 tokens to spend, put 400 into context and 100 into the task. A simple instruction with rich background always outperforms elaborate instructions with no context.

Cut in this order. When a prompt is too long: first cut verbose role definitions, then restated context, then hedging language. Never cut examples, success criteria, or format specs — these change LLM behavior the most.

Reusability when asked. If the user wants a template, use {{placeholder}} syntax with clear labels. If it's a one-shot, bake in the specifics.

Verification beats vague caution. For complex or high-impact prompts, tell the agent what to verify before finalizing instead of piling on broad "be thorough" instructions.

Know when to skip. Only skip prompt-building when the user did not ask for a prompt and direct execution is clearly better. If they explicitly asked for a prompt, deliver the prompt even if the underlying task is simple.

References (load on demand)
references/components-guide.md — Deep dive on each building block with examples and anti-patterns
references/prompt-patterns.md — 8 common patterns: research, code gen, review, writing, extraction, analysis, handoff, decision
references/quality-checklist.md — Quality checks with failure modes and fixes
Guides (platform-specific tips)
guides/claude-guide.md — Claude Code / Claude web / API
guides/gpt.md — GPT Pro / ChatGPT / API
guides/perplexity.md — Perplexity
guides/gemini.md — Gemini 3 / Imagen 4
guides/local-models.md — Local/open-source models (Llama, Qwen, Mistral, DeepSeek, Ollama, etc.)
Templates (special cases where a well-crafted template adds real value)
templates/session-handoff.md — AI session handoff (continuation, debug)
templates/image-gen.md — Image generation (photo, illustration, icon, per-platform notes)
templates/video-gen.md — Video generation (text-to-video, image-to-video, camera keywords, per-platform notes)
templates/system-prompt.md — Chatbot/agent system prompts (layered architecture)
Weekly Installs
8
Repository
sungjunlee/craftkit
First Seen
8 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass