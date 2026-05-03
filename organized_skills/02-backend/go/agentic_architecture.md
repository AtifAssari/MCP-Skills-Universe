---
rating: ⭐⭐
title: agentic_architecture
url: https://skills.sh/cityfish91159/maihouses/agentic_architecture
---

# agentic_architecture

skills/cityfish91159/maihouses/agentic_architecture
agentic_architecture
Installation
$ npx skills add https://github.com/cityfish91159/maihouses --skill agentic_architecture
SKILL.md
Agentic Architecture Protocol
1. Think Before You Code

Before implementing any feature that spans multiple files:

Analyze Data Flow: Where does data come from? Where does it go?
Define Interfaces: creating types/*.ts is often the best first step.
Check Boundaries: Ensure API logic stays in api/, UI in components/, and business logic in services/ or hooks/.
2. Scalability & Performance Checks
Database:
Are we fetching 1000 items to filter 10? (Use DB filters instead).
Is RLS (Row Level Security) compatible with this query?
Frontend:
Are we causing unnecessary re-renders? (Use React.memo, useCallback appropriately).
Is this component becoming a "God Component"? (Break it down).
3. The "Three-Tier" Rule

For any non-trivial feature, verify you have these three layers:

Data Layer: Types + API/Service (e.g., user.types.ts, userService.ts)
State Layer: Hook or Store (e.g., useUser.ts)
View Layer: Components (e.g., UserProfile.tsx)
4. Architecture Checklist
 Have I defined the types first?
 Is the business logic separated from the UI?
 Did I consider how this scales to 10,000 users/items?
 Is the database schema validated (if changing DB)?
Weekly Installs
19
Repository
cityfish91159/maihouses
GitHub Stars
1
First Seen
Jan 25, 2026