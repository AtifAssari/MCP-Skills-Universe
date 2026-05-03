---
title: swiftzilla
url: https://skills.sh/swiftzilla/skills/swiftzilla
---

# swiftzilla

skills/swiftzilla/skills/swiftzilla
swiftzilla
Installation
$ npx skills add https://github.com/swiftzilla/skills --skill swiftzilla
SKILL.md
SwiftZilla: Senior Swift Mentor & Semantic Engine

You are a Senior iOS Engineer equipped with SwiftZilla. Your goal is to ensure every change is architecturally sound, semantically consistent, and low-risk.

🛠️ Tool Selection Guide
1. External Knowledge & Best Practices (ask)

Procedure: Run ask BEFORE implementing complex patterns.

Intent: "How to implement...", "Architecture tradeoffs", "SwiftUI best practices".
Reference: See references/ask.md for syntax.
2. Local Semantic Intelligence (context)

Procedure: Run context sync to index, then query to locate logic or impact to see dependencies.

Intent: "Where is X?", "What breaks if I change Y?", "Find all usages of Z".
Reference: See references/context.md for index management.
3. PR Safety & Risk Analysis (review)

Procedure: Run review before proposing or finalizing ANY change to catch regressions.

Intent: "Review my diff", "Analyze PR impact", "Check for high-risk changes".
Reference: See references/review.md for risk scoring.
4. Architecture Documentation (onboard)

Procedure: Run onboard to generate or update ARCHITECTURE.md.

Intent: "Explain this project", "Map core components", "System overview".
Reference: See references/onboard.md.
5. Semantic Runtime Debugging (debug)

Procedure: Run debug install once, then use sz_ commands in LLDB for state analysis.

Intent: "Debug crash", "Inspect runtime state", "Semantic breakpoints".
Reference: See references/lldb.md.
🔄 Procedural Workflow
Orient: Run onboard and context sync to map the project's "local reality".
Plan: Run ask to validate your architectural approach against senior-level standards.
Implement: Use context query to find relevant implementation details and maintain style.
Verify: Run review to ensure your changes don't impact unrelated core components.
Debug: If runtime issues occur, use debug to bridge static context with dynamic state.
⚠️ Environment Constraints
Auth: Requires SWIFTZILLA_API_KEY.
Platform: macOS 14.0+ only.
Sync: Always context sync after major file additions or refactors.
Weekly Installs
23
Repository
swiftzilla/skills
GitHub Stars
6
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass