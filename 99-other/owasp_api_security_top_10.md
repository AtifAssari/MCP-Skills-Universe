---
rating: ⭐⭐
title: owasp-api-security-top-10
url: https://skills.sh/yariv1025/skills/owasp-api-security-top-10
---

# owasp-api-security-top-10

skills/yariv1025/skills/owasp-api-security-top-10
owasp-api-security-top-10
Installation
$ npx skills add https://github.com/yariv1025/skills --skill owasp-api-security-top-10
SKILL.md
OWASP API Security Top 10

This skill encodes the OWASP API Security Top 10 for secure API design, code review, and vulnerability prevention. References are loaded per risk (progressive disclosure).

Based on OWASP API Security Top 10:2023.

When to Read Which Reference
Risk	Read
API1 Broken Object Level Authorization	references/api1-broken-object-level-authorization.md
API2 Broken Authentication	references/api2-broken-authentication.md
API3 Broken Object Property Level Authorization	references/api3-broken-object-property-authorization.md
API4 Unrestricted Resource Consumption	references/api4-unrestricted-resource-consumption.md
API5 Broken Function Level Authorization	references/api5-broken-function-level-authorization.md
API6 Unrestricted Access to Sensitive Business Flows	references/api6-sensitive-business-flows.md
API7 Server Side Request Forgery (SSRF)	references/api7-ssrf.md
API8 Security Misconfiguration	references/api8-security-misconfiguration.md
API9 Improper Inventory Management	references/api9-improper-inventory-management.md
API10 Unsafe Consumption of APIs	references/api10-unsafe-consumption-of-apis.md
Quick Patterns
Enforce object-level and function-level authorization on every API request; never trust client-supplied IDs without server-side checks.
Validate and sanitize all inputs; treat third-party API responses as untrusted.
Apply rate limiting, quotas, and cost controls to prevent abuse and DoS.
Maintain an API inventory; retire or protect deprecated and debug endpoints.
Quick Reference / Examples
Task	Approach
Object-level auth (IDOR)	Verify user owns/can access the resource by ID server-side. See API1.
Function-level auth	Check user role before admin/sensitive operations. See API5.
Rate limiting	Apply per-user/IP limits, quotas, and timeouts. See API4.
SSRF prevention	Validate/allowlist URLs; block internal ranges. See API7.
Third-party APIs	Validate responses, use TLS, set timeouts. See API10.

Safe - object-level authorization check:

@app.get("/api/orders/{order_id}")
def get_order(order_id: int, current_user: User):
    order = Order.query.get(order_id)
    if order.user_id != current_user.id:
        raise HTTPException(403, "Access denied")
    return order


Unsafe - missing authorization (IDOR vulnerability):

@app.get("/api/orders/{order_id}")
def get_order(order_id: int):
    return Order.query.get(order_id)  # Any user can access any order!


Rate limiting example (FastAPI):

from slowapi import Limiter
limiter = Limiter(key_func=get_remote_address)

@app.get("/api/search")
@limiter.limit("10/minute")
def search(query: str):
    return perform_search(query)

Workflow
Object-level authorization (IDOR) → Read references/api1-broken-object-level-authorization.md.
Authentication and tokens → Read references/api2-broken-authentication.md.
Rate limiting / DoS → Read references/api4-unrestricted-resource-consumption.md.
Admin vs user endpoints → Read references/api5-broken-function-level-authorization.md.
User-supplied URLs in API → Read references/api7-ssrf.md.
Third-party API consumption → Read references/api10-unsafe-consumption-of-apis.md.

Load reference files only when relevant to the task.

Weekly Installs
14
Repository
yariv1025/skills
GitHub Stars
1
First Seen
Feb 15, 2026
Security Audits
Gen Agent Trust HubPass
SocketFail
SnykPass