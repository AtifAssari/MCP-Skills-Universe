---
rating: ⭐⭐
title: mql5-docs-research
url: https://skills.sh/tmaru-eng/strategy-bricks/mql5-docs-research
---

# mql5-docs-research

skills/tmaru-eng/strategy-bricks/mql5-docs-research
mql5-docs-research
Installation
$ npx skills add https://github.com/tmaru-eng/strategy-bricks --skill mql5-docs-research
SKILL.md
MQL5 Docs Research (JA/EN)

Provide doc-based guidance when users hit errors while creating or modifying MQL5 code. Use only the official docs in Japanese and English.

Scope and Sources
Allowed sources:
https://www.mql5.com/ja/docs
https://www.mql5.com/en/docs
Do not use forums, blogs, or third-party sites.
Inputs to Collect

Ask for any missing context before research:

Exact error text and error code (if any)
File path and line/column numbers
MQL5 file type (.mq5 or .mqh)
Related API/class names (e.g., CTrade, MqlRates)
MetaTrader 5 build/version (if available)
Workflow
Normalize the error or question into keywords:
Extract error code and symbols (function/class names)
Keep 2-5 keywords for searching
Search Japanese and English docs:
Use site search in the docs pages
If no direct hit, search broader sections by keyword
Open the most relevant doc pages and confirm:
Correct function signatures
Parameter types and constraints
Return values, error handling, and examples
Produce a response in Japanese with:
Summary of the cause
Doc links (JA first, EN second)
Specific guidance aligned with doc wording
Next checks (if ambiguity remains)
Output Format (Markdown)
Summary (1-3 sentences)
Relevant Docs
JA:
EN:
Key Notes (bullets)
Next Checks (bullets, optional)
Guardrails
If the error cannot be mapped to docs, state that clearly and propose a best-effort hypothesis.
Never invent API signatures or behavior not documented in the official docs.
Keep the response concise and actionable.
Weekly Installs
52
Repository
tmaru-eng/strat…y-bricks
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn