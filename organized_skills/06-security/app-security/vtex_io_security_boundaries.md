---
rating: ⭐⭐
title: vtex-io-security-boundaries
url: https://skills.sh/vtex/skills/vtex-io-security-boundaries
---

# vtex-io-security-boundaries

skills/vtex/skills/vtex-io-security-boundaries
vtex-io-security-boundaries
Installation
$ npx skills add https://github.com/vtex/skills --skill vtex-io-security-boundaries
SKILL.md
Security Boundaries & Exposure Review
When this skill applies

Use this skill when the main question is whether a VTEX IO route, integration, or service boundary is safe.

Reviewing public versus private route exposure
Validating external input at service boundaries
Handling tokens, account context, or sensitive payloads
Avoiding cross-account, cross-workspace, or cross-user leakage
Hardening integrations that expose or consume sensitive data

Do not use this skill for:

policy declaration syntax in manifest.json
service runtime sizing
logging and observability strategy
frontend browser security concerns
deciding which VTEX auth token should call an endpoint
Decision rules
Use this skill to decide what data and input may safely cross the app boundary, not which policies or tokens authorize the call.
Treat every public route as an explicit trust boundary.
In service.json, changing a route from public: false to public: true is a boundary change and should trigger explicit security review.
Use public: true for routes that must be callable from outside VTEX IO, such as partner webhooks or externally consumed integration endpoints. Treat them as internet-exposed boundaries.
Use public: false for routes that are meant only for VTEX internal flows or other IO apps, but do not treat them as implicitly safe. They still require validation and scoped assumptions.
A route with public: true in service.json is reachable from outside the app as long as the account domain is accessible. Do not rely on obscure paths or internal-looking URLs as a security measure.
Validate external input as early as possible, before it reaches domain logic or downstream integrations.
For webhook-style routes, validate both structure and authenticity, for example through required fields plus a shared secret or signature header, before calling downstream clients.
Do not assume a request is safe because it originated from another VTEX service or internal-looking route path.
Keep account, workspace, and user context explicit when a service reads or writes scoped data.
When data or behavior must be restricted to a specific workspace, check ctx.vtex.workspace explicitly and reject calls from other workspaces.
Never expose more data than the caller needs. Shape responses intentionally instead of returning raw downstream payloads.
Keep secrets, tokens, and security-sensitive headers out of logs and route responses.
Do not use console.log or console.error in production routes or services. Use ctx.vtex.logger for application logging with structured objects, and only use a dedicated external logging client when the app intentionally forwards logs to a partner-owned system.
Avoid exposing debug or diagnostic routes that return internal configuration, secrets, or full downstream payloads. If such routes are strictly necessary, keep them non-public and limited to minimal, non-sensitive information.
Use this skill to decide what may cross the boundary, and use vtex-io-auth-and-policies to decide how that boundary is authorized and protected.
Related skills
vtex-io-auth-and-policies - Use when the main decision is how route or resource access will be authorized
vtex-io-auth-tokens-and-context - Use when the main decision is which runtime identity should call VTEX endpoints
Hard constraints
Constraint: Public routes must validate untrusted input at the boundary

Any route exposed beyond a tightly controlled internal boundary MUST validate incoming data before calling domain logic or downstream clients.

Why this matters

Unvalidated input at public boundaries creates the fastest path to abuse, bad writes, and accidental downstream failures.

Detection

If a public route forwards body fields, params, or headers directly into business logic or client calls without validation, STOP and add validation first.

Correct

export async function webhook(ctx: Context) {
  const body = ctx.request.body

  if (!body?.eventId || !body?.type) {
    ctx.status = 400
    ctx.body = { message: 'Invalid payload' }
    return
  }

  await ctx.clients.partnerApi.handleWebhook(body)
  ctx.status = 202
}


Wrong

export async function webhook(ctx: Context) {
  await ctx.clients.partnerApi.handleWebhook(ctx.request.body)
  ctx.status = 202
}

Constraint: Sensitive data must not cross route boundaries by accident

Routes and integrations MUST not leak tokens, internal headers, raw downstream payloads, or data that belongs to another account, workspace, or user context.

Why this matters

Boundary leaks are hard to detect once deployed and can expose information far beyond the intended caller scope.

Detection

If a route returns raw downstream responses, logs secrets, or mixes contexts without explicit filtering, STOP and narrow the output before proceeding.

Correct

ctx.body = {
  orderId: order.id,
  status: order.status,
}


Wrong

ctx.body = order

Constraint: Trust boundaries must stay explicit when services call each other

When one service calls another, the receiving boundary MUST still be treated as a real security boundary with explicit validation and scoped assumptions.

Why this matters

Internal service-to-service traffic can still carry malformed or overbroad data. Assuming “internal means trusted” leads to fragile security posture and cross-context leakage.

Detection

If a service accepts data from another service without validating format, scope, or account/workspace context, STOP and make those checks explicit.

Correct

if (ctx.vtex.account !== expectedAccount) {
  ctx.status = 403
  return
}


Wrong

await processPartnerPayload(ctx.request.body)

Preferred pattern

Security review should start at the boundary:

Who can call this route or trigger this integration?
What data enters the system?
What must be validated immediately?
What data leaves the system?
Could account, workspace, or user context leak across the boundary?

Use minimal request and response shapes, explicit validation, and scoped context checks to keep boundaries safe.

Common failure modes
Treating public routes like trusted internal handlers.
Returning raw downstream payloads that expose more data than necessary.
Logging secrets or security-sensitive headers.
Using console.log in handlers instead of ctx.vtex.logger, making logs less structured and increasing the risk of leaking sensitive data.
Mixing account or workspace context without explicit checks.
Assuming service-to-service traffic is inherently safe.
Review checklist
 Is the trust boundary clear?
 Are external inputs validated before reaching domain or integration logic?
 Is the response shape intentionally minimal?
 Are sensitive values kept out of logs and responses?
 Could account, workspace, or user context leak across this boundary?
Reference
Service - Route exposure and service behavior
Policies - Authorization-related declaration context
Weekly Installs
157
Repository
vtex/skills
GitHub Stars
25
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass