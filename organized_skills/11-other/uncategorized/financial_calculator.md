---
rating: ⭐⭐
title: financial-calculator
url: https://skills.sh/dkyazzentwatwa/chatgpt-skills/financial-calculator
---

# financial-calculator

skills/dkyazzentwatwa/chatgpt-skills/financial-calculator
financial-calculator
Installation
$ npx skills add https://github.com/dkyazzentwatwa/chatgpt-skills --skill financial-calculator
SKILL.md
Financial Calculator

Use deterministic calculations instead of ad hoc spreadsheet math when the user needs precise financial outputs.

Use This For
Loan and mortgage math
Investment growth and savings goals
NPV, IRR, and payback analysis
Retirement projections and withdrawal planning
Monte Carlo style risk scenarios
Workflow
Confirm units and assumptions first: rates, compounding, time horizon, taxes, and inflation.
Use scripts/financial_calc.py as the source of truth for the computation.
Return both the answer and the assumptions that materially drive it.
Guardrails
Treat outputs as calculations, not personalized financial advice.
Surface simplifying assumptions and scenario sensitivity.
Weekly Installs
317
Repository
dkyazzentwatwa/…t-skills
GitHub Stars
53
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass