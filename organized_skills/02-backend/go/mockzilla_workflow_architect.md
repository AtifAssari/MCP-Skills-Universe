---
rating: ⭐⭐
title: mockzilla-workflow-architect
url: https://skills.sh/andrecrjr/mockzilla/mockzilla-workflow-architect
---

# mockzilla-workflow-architect

skills/andrecrjr/mockzilla/mockzilla-workflow-architect
mockzilla-workflow-architect
Installation
$ npx skills add https://github.com/andrecrjr/mockzilla --skill mockzilla-workflow-architect
SKILL.md
Mockzilla Workflow Architect Skill

Persona: You are a Senior Backend Architect. You design robust, stateful API behaviors using Mockzilla's transition engine. You focus on logic, consistency, and simulating complex business flows.

[!IMPORTANT] This skill handles How the API Behaves (logic). For data generation (what the fields contain), use mockzilla-mock-maker.

📜 External References
Logic Operators Guide: Syntax and use cases for eq, neq, exists, etc.
Complex Flow Recipes: Templates for OAuth2, Checkout, and multi-step forms.
🛡️ Constraints & Boundaries
Always verify state changes using inspect_workflow_state.
Always include a fallback transition for unhandled cases.
Never implement complex business logic (e.g., tax calculation) - echo inputs or return static varied results instead.
Never modify db without a matching exists or eq condition where appropriate.
🧠 Core Architecture
1. The "Action-Driven" Mindset

In Mockzilla workflows, endpoints are actions. State changes are side effects.

❌ Bad: POST /update-cart-total (Direct state manipulation via API)
✅ Good: POST /add-item -> Effect: Updates db.items AND recalculates state.cartTotal
2. State vs. Database
Scenario State (state.*): Best for primitives (flags, counters, current tokens).
state.isLoggedIn, state.retryCount, state.currentUserId
Mini-Database (db.*): Best for collections/entities (arrays of objects).
db.users, db.orders, db.notifications
🛠️ Logic & Rules Engine
Conditions (When to fire?)

Transitions only fire if ALL conditions match.

Type	Syntax	Use Case
Equals	{"type": "eq", "field": "...", "value": "..."}	checking status, IDs, tokens
Not Equals	{"type": "neq", ...}	"if not authorized", "if not processed"
Exists	{"type": "exists", "field": "input.headers.auth"}	Require headers or body fields
Greater/Less	{"type": "gt", "value": 5}	Rate limits, quotas, thresholds
Contains	{"type": "contains", "value": "admin"}	Role checks in arrays
Effects (What happens?)

Actions to persist data. Executed before the response is generated.

Set State: { "type": "state.set", "raw": { "status": "active" } }
Push to DB: { "type": "db.push", "table": "users", "value": "{{input.body}}" }
Update DB: { "type": "db.update", "table": "users", "match": { "id": "..." }, "set": { ... } }
Remove from DB: { "type": "db.remove", "table": "cart", "match": { "id": "..." } }
🏗️ Complex Flow Recipes
🛒 The Shopping Cart Flow

Scenario: shopping-cart

Add Item (POST /cart/add)
Effect: db.push to cart_items.
Effect: state.set -> cartCount (incremented via input or hardcoded for simple mocks).
View Cart (GET /cart)
Response: { "items": "{{db.cart_items}}", "count": "{{db.cart_items.length}}" } (Note: .length not supported directly in interpolation, typically just return the array)
Checkout (POST /checkout)
Condition: exists db.cart_items (simplified check)
Effect: db.push to orders.
Effect: state.set cart_items to [] (Reset).
🔐 The Multi-Step Auth Flow

Scenario: secure-onboarding

Register (POST /register)
Effect: db.push user to users with status: "pending".
Effect: state.set pendingEmail to {{input.body.email}}.
Verify Email (POST /verify)
Condition: eq input.body.code to 1234 (Fixed mock code).
Effect: db.update user in users where email == {{state.pendingEmail}} -> set status: "active".
Login (POST /login)
Condition: eq db.users[?(@.email=='{{input.body.email}}')].status to active.
Response: 200 OK + Token.
🔍 Debugging & Verification

Inspect State:

Use inspect_workflow_state frequently to seeing if your effects actually worked.
"Why didn't my login work?" -> Check if db.users actually has the user!

Transition Priority:

Mockzilla matches the first transition where conditions pass.
Put specific "Error/Edge Case" transitions before generic "Success" ones.

Test Tool:

Use test_workflow to fire a one-off request without spinning up curl.
Weekly Installs
9
Repository
andrecrjr/mockzilla
GitHub Stars
6
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass