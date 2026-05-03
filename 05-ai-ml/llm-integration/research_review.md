---
title: research-review
url: https://skills.sh/wanshuiyin/auto-claude-code-research-in-sleep/research-review
---

# research-review

skills/wanshuiyin/auto-claude-code-research-in-sleep/research-review
research-review
Installation
$ npx skills add https://github.com/wanshuiyin/auto-claude-code-research-in-sleep --skill research-review
SKILL.md
Research Review via Codex MCP (xhigh reasoning)

Get a multi-round critical review of research work from an external LLM with maximum reasoning depth.

Constants
REVIEWER_MODEL = gpt-5.4 — Model used via Codex MCP. Must be an OpenAI model (e.g., gpt-5.4, o3, gpt-4o)
REVIEWER_BACKEND = codex — Default: Codex MCP (xhigh). Override with — reviewer: oracle-pro for GPT-5.4 Pro via Oracle MCP. See shared-references/reviewer-routing.md.
Context: $ARGUMENTS
Prerequisites
Codex MCP Server configured in Claude Code:
claude mcp add codex -s user -- codex mcp-server

This gives Claude Code access to mcp__codex__codex and mcp__codex__codex-reply tools
Workflow
Step 1: Gather Research Context

Before calling the external reviewer, compile a comprehensive briefing:

Read project narrative documents (e.g., STORY.md, README.md, paper drafts)
Read any memory/notes files for key findings and experiment history
Identify: core claims, methodology, key results, known weaknesses
Step 2: Initial Review (Round 1)

Send a detailed prompt with xhigh reasoning:

mcp__codex__codex:
  config: {"model_reasoning_effort": "xhigh"}
  prompt: |
    [Full research context + specific questions]
    Please act as a senior ML reviewer (NeurIPS/ICML level). Identify:
    1. Logical gaps or unjustified claims
    2. Missing experiments that would strengthen the story
    3. Narrative weaknesses
    4. Whether the contribution is sufficient for a top venue
    Please be brutally honest.

Step 3: Iterative Dialogue (Rounds 2-N)

Use mcp__codex__codex-reply with the returned threadId to continue the conversation:

For each round:

Respond to criticisms with evidence/counterarguments
Ask targeted follow-ups on the most actionable points
Request specific deliverables: experiment designs, paper outlines, claims matrices

Key follow-up patterns:

"If we reframe X as Y, does that change your assessment?"
"What's the minimum experiment to satisfy concern Z?"
"Please design the minimal additional experiment package (highest acceptance lift per GPU week)"
"Please write a mock NeurIPS/ICML review with scores"
"Give me a results-to-claims matrix for possible experimental outcomes"
Step 4: Convergence

Stop iterating when:

Both sides agree on the core claims and their evidence requirements
A concrete experiment plan is established
The narrative structure is settled
Step 5: Document Everything

Save the full interaction and conclusions to a review document in the project root:

Round-by-round summary of criticisms and responses
Final consensus on claims, narrative, and experiments
Claims matrix (what claims are allowed under each possible outcome)
Prioritized TODO list with estimated compute costs
Paper outline if discussed

Update project memory/notes with key review conclusions.

Key Rules
ALWAYS use config: {"model_reasoning_effort": "xhigh"} for reviews
Send comprehensive context in Round 1 — the external model cannot read your files
Be honest about weaknesses — hiding them leads to worse feedback
Push back on criticisms you disagree with, but accept valid ones
Focus on ACTIONABLE feedback — "what experiment would fix this?"
Document the threadId for potential future resumption
The review document should be self-contained (readable without the conversation)
Prompt Templates
For initial review:

"I'm going to present a complete ML research project for your critical review. Please act as a senior ML reviewer (NeurIPS/ICML level)..."

For experiment design:

"Please design the minimal additional experiment package that gives the highest acceptance lift per GPU week. Our compute: [describe]. Be very specific about configurations."

For paper structure:

"Please turn this into a concrete paper outline with section-by-section claims and figure plan."

For claims matrix:

"Please give me a results-to-claims matrix: what claim is allowed under each possible outcome of experiments X and Y?"

For mock review:

"Please write a mock NeurIPS review with: Summary, Strengths, Weaknesses, Questions for Authors, Score, Confidence, and What Would Move Toward Accept."

Review Tracing

After each mcp__codex__codex or mcp__codex__codex-reply reviewer call, save the trace following shared-references/review-tracing.md. Use tools/save_trace.sh or write files directly to .aris/traces/<skill>/<date>_run<NN>/. Respect the --- trace: parameter (default: full).

Weekly Installs
99
Repository
wanshuiyin/auto…in-sleep
GitHub Stars
7.9K
First Seen
Mar 12, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass