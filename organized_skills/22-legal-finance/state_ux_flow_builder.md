---
rating: ⭐⭐
title: state-ux-flow-builder
url: https://skills.sh/monkey1sai/openai-cli/state-ux-flow-builder
---

# state-ux-flow-builder

skills/monkey1sai/openai-cli/state-ux-flow-builder
state-ux-flow-builder
Installation
$ npx skills add https://github.com/monkey1sai/openai-cli --skill state-ux-flow-builder
SKILL.md
State & UX Flow Builder

Create consistent UX flows for all application states: loading, error, empty, and success.

Output Components

Every implementation includes: (1) Loading skeletons, (2) Error state with retry, (3) Empty state with action, (4) Success view, (5) Error boundary, (6) State management pattern (useState/XState/server).

Key Patterns

Data Fetching Flow: Check loading → Handle error → Show empty → Display data State Machine: XState for complex flows with multiple states and transitions Optimistic Updates: Instant UI feedback with rollback on error Progressive Loading: Show content incrementally as it loads

Best Practices

Always handle all states, prefer skeletons over spinners, provide retry mechanisms, use consistent error/empty UI, add ARIA live regions, implement error boundaries.

Weekly Installs
8
Repository
monkey1sai/openai-cli
GitHub Stars
2
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass