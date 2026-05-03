---
title: eve-auth-and-secrets
url: https://skills.sh/incept5/eve-skillpacks/eve-auth-and-secrets
---

# eve-auth-and-secrets

skills/incept5/eve-skillpacks/eve-auth-and-secrets
eve-auth-and-secrets
Installation
$ npx skills add https://github.com/incept5/eve-skillpacks --skill eve-auth-and-secrets
SKILL.md
Eve Auth and Secrets

Use this workflow to log in to Eve and manage secrets for your app.

When to Use
Setting up a new project profile
Authentication failures
Adding or rotating secrets
Secret interpolation errors during deploys
Setting up identity providers or org invites
Adding SSO login to an Eve-deployed app
Setting up access groups and scoped data-plane authorization
Configuring group-aware RLS for environment databases
Authentication
eve auth login
eve auth login --ttl 30                # custom token TTL (1-90 days)
eve auth status

Challenge-Response Flow

Eve uses challenge-response authentication. The default provider is github_ssh:

Client sends SSH public key fingerprint
Server returns a challenge (random bytes)
Client signs the challenge with the private key
Server verifies the signature and issues a JWT
Token Types
Type	Issued Via	Use Case
User Token	eve auth login	Interactive CLI sessions
Job Token	Worker auto-issued	Agent execution within jobs
Minted Token	eve auth mint	Bot/service accounts

JWT payloads include sub (user ID), org_id, scope, and exp. Verify tokens via the JWKS endpoint: GET /auth/jwks.

Role and org membership changes take effect immediately -- the server resolves permissions from live DB memberships, not stale JWT claims. When a request includes a project_id but no org_id, the permission guard derives the org context from the project's owning org.

Permissions

Check what the current token can do:

eve auth permissions


Register additional identities for multi-provider access:

curl -X POST "$EVE_API_URL/auth/identities" -H "Authorization: Bearer $TOKEN" \
  -d '{"provider": "nostr", "external_id": "<pubkey>"}'

Identity Providers

Eve supports pluggable identity providers. The auth guard tries Bearer JWT first, then provider-specific request auth.

Provider	Auth Method	Use Case
github_ssh	SSH challenge-response	Default CLI login
nostr	NIP-98 request auth + challenge-response	Nostr-native users
Nostr Authentication

Two paths:

Challenge-response: Like SSH but signs with Nostr key. Use eve auth login --provider nostr.
NIP-98 request auth: Every API request signed with a Kind 27235 event. Stateless, no stored token.
Org Invites

Invite external users via the CLI or API:

# Invite with SSH key registration (registers key so the user can log in immediately)
eve admin invite --email user@example.com --ssh-key ~/.ssh/id_ed25519.pub --org org_xxx

# Invite with GitHub identity
eve admin invite --email user@example.com --github ghuser --org org_xxx

# Invite with web-based auth (Supabase)
eve admin invite --email user@example.com --web --org org_xxx

# API: invite targeting a Nostr pubkey
curl -X POST "$EVE_API_URL/auth/invites" -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"org_id": "org_xxx", "role": "member", "provider_hint": "nostr", "identity_hint": "<pubkey>"}'


If no auth method is specified (--github, --ssh-key, or --web), the CLI warns that the user will not be able to log in. The user can self-register later via eve auth request-access --org "Org Name" --ssh-key ~/.ssh/id_ed25519.pub --wait.

When the identity authenticates, Eve auto-provisions their account and org membership.

For app-driven onboarding, use the org-scoped invite API instead of the legacy admin invite flow:

# Create an org-scoped Supabase invite with a return URL for the app
curl -X POST "$EVE_API_URL/orgs/org_xxx/invites" \
  -H "Authorization: Bearer $USER_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "role": "member",
    "redirect_to": "https://app.example.com/invite/complete",
    "app_context": { "project_id": "proj_123" }
  }'

# Search existing org members for an assignee picker
curl "$EVE_API_URL/orgs/org_xxx/members/search?q=ali" \
  -H "Authorization: Bearer $USER_TOKEN"


Use a user token with orgs:invite to create or list these invites and orgs:members:read for member lookup. Invite emails should land on GoTrue's /verify path, not the OAuth callback directly. If the invite is auto-applied during the SSO exchange, Eve returns invite_redirect_to so the SSO callback can land the user back in the target app even when the email provider strips nested redirect params. Current invite onboarding establishes the SSO session first, then sends the user through /set-password before redirecting to the app.

Token Minting (Admin)

Mint tokens for bot/service users without SSH login:

# Mint token for a bot user (creates user + membership if needed)
eve auth mint --email app-bot@example.com --org org_xxx

# With custom TTL (1-90 days, default: server configured)
eve auth mint --email app-bot@example.com --org org_xxx --ttl 90

# Scope to project with admin role
eve auth mint --email app-bot@example.com --project proj_xxx --role admin


Print the current access token (useful for scripts):

eve auth token

Self-Service Access Requests

Users without an invite can request access:

eve auth request-access --org "My Company" --email you@example.com
eve auth request-access --org "My Company" --ssh-key ~/.ssh/id_ed25519.pub
eve auth request-access --status <request_id>


Admins approve or reject via:

eve admin access-requests list
eve admin access-requests approve <request_id>
eve admin access-requests reject <request_id> --reason "..."


List responses use the canonical { "data": [...] } envelope.

Approval is atomic (single DB transaction) and idempotent -- re-approving a completed request returns the existing record. If the fingerprint is already registered, Eve reuses that identity owner. If a legacy partial org matches the requested slug and name, Eve reuses it during approval. Failed attempts never leave partial state.

Credential Check

Verify local AI tool credentials:

eve auth creds                # Show Claude + Codex cred status
eve auth creds --claude       # Only Claude
eve auth creds --codex        # Only Codex


Output includes token type (setup-token or oauth), preview, and expiry. Use this to confirm token health before syncing.

OAuth Token Sync

Sync local Claude/Codex OAuth tokens into Eve secrets so agents can use them. Scope precedence: project > org > user.

eve auth sync                       # Sync to user-level (default)
eve auth sync --org org_xxx         # Sync to org-level (shared across org projects)
eve auth sync --project proj_xxx    # Sync to project-level (scoped to one project)
eve auth sync --dry-run             # Preview without syncing


This sets CLAUDE_CODE_OAUTH_TOKEN / CLAUDE_OAUTH_REFRESH_TOKEN (Claude) and CODEX_AUTH_JSON_B64 (Codex/Code) at the requested scope.

Claude Token Types
Token Prefix	Type	Lifetime	Recommendation
sk-ant-oat01-*	setup-token (long-lived)	Long-lived	Preferred for jobs and automation
Other sk-ant-*	oauth (short-lived)	~15 hours	Use for interactive dev; regenerate with claude setup-token

eve auth sync warns when syncing a short-lived OAuth token. Run eve auth creds to inspect token type before syncing.

Automatic Codex/Code Token Write-Back

After each harness invocation, the worker checks if the Codex/Code CLI refreshed auth.json during the session. If the token changed, it is automatically written back to the originating secret scope (user/org/project) so the next job starts with a fresh token. This is transparent and non-fatal -- a write-back failure logs a warning but does not affect the job result.

For Codex/Code credentials, the sync picks the freshest token across ~/.codex/auth.json and ~/.code/auth.json by comparing tokens.expires_at.

Access Groups + Scoped Access

Groups are first-class authorization primitives that segment data-plane access (org filesystem, org docs, environment databases). Create groups, add members, and bind roles with scoped constraints:

# Create a group
eve access groups create --org org_xxx --slug eng-team --name "Engineering"

# Add members
eve access groups members add eng-team --org org_xxx --user user_abc
eve access groups members add eng-team --org org_xxx --service-principal sp_xxx

# Bind a role with scoped access
eve access bind --org org_xxx --group grp_xxx --role data-reader \
  --scope-json '{"orgfs":{"allow_prefixes":["/shared/"]},"envdb":{"schemas":["public"]}}'

# Check effective access
eve access memberships --org org_xxx --user user_abc

Scope Types
Resource	Scope Fields	Example
Org Filesystem	orgfs.allow_prefixes, orgfs.read_only_prefixes	"/shared/", "/reports/"
Org Documents	orgdocs.allow_prefixes, orgdocs.read_only_prefixes	"/pm/features/"
Environment DB	envdb.schemas, envdb.tables	"public", "analytics_*"
Group-Aware RLS

Scaffold RLS helper functions for group-based row-level security in environment databases:

eve db rls init --with-groups


This creates SQL helpers (app.current_user_id(), app.current_group_ids(), app.has_group()) that read session context set by Eve's runtime. Use them in RLS policies:

CREATE POLICY notes_group_read ON notes FOR SELECT
  USING (group_id = ANY(app.current_group_ids()));

Membership Introspection

Inspect a principal's full effective access -- base org/project roles, group memberships, resolved bindings, and merged scopes:

eve access memberships --org org_xxx --user user_abc
eve access memberships --org org_xxx --service-principal sp_xxx


The response includes effective_scopes (merged across all bindings), effective_permissions, and each binding's matched_via (direct or group).

Resource-Specific Access Checks

Check and explain access against a specific data-plane resource:

eve access can orgfs:read /shared/reports --org org_xxx
eve access explain orgfs:write /shared/reports --org org_xxx --user user_abc


The response includes scope_required, scope_matched, and per-grant scope_reason explaining why a binding did or did not match the requested resource path.

Policy-as-Code (v2)

Declare groups, roles, and scoped bindings in .eve/access.yaml. Use version: 2:

version: 2
access:
  groups:
    eng-team:
      name: Engineering Team
      description: Scoped access for engineering collaborators
      members:
        - type: user
          id: user_abc
  roles:
    app_editor:
      scope: org
      permissions:
        - orgdocs:read
        - orgdocs:write
        - orgfs:read
        - envdb:read
  bindings:
    - subject: { type: group, id: eng-team }
      roles: [app_editor]
      scope:
        orgdocs: { allow_prefixes: ["/groups/app/**"] }
        orgfs: { allow_prefixes: ["/groups/app/**"] }
        envdb: { schemas: ["app"] }


Validate, plan, and sync:

eve access validate --file .eve/access.yaml
eve access plan --file .eve/access.yaml --org org_xxx
eve access sync --file .eve/access.yaml --org org_xxx


Sync is declarative: it creates, updates, and prunes groups, members, roles, and bindings to match the YAML. Invalid scope configurations fail fast before any mutations are applied. Binding subjects can be user, service_principal, or group.

Key Rotation

Rotate the JWT signing key:

Set EVE_AUTH_JWT_SECRET_NEW alongside the existing secret
Server starts signing with the new key but accepts both during the grace period
After grace period (EVE_AUTH_KEY_ROTATION_GRACE_HOURS), remove the old secret
Emergency rotation: set only the new key (immediately invalidates all existing tokens)
App SSO Integration

Add Eve SSO login to any Eve-deployed app using two shared packages: @eve-horizon/auth (backend) and @eve-horizon/auth-react (frontend). The platform auto-injects EVE_SSO_URL, EVE_ORG_ID, and EVE_API_URL into deployed services.

Backend (@eve-horizon/auth)

Install: npm install @eve-horizon/auth

Use the unified middleware by default for new apps:

Export	Behavior
eveAuth()	Non-blocking middleware. Verifies user or agent tokens and attaches normalized identity at req.eveIdentity.
eveIdentityGuard()	Returns 401 if req.eveIdentity is not set. Place on protected routes.
eveAuthConfig()	Handler returning { sso_url, eve_api_url, ... } from auto-injected env vars. Frontend fetches this to discover SSO.
eveAuthMe()	/auth/me handler for the React SDK and custom clients.

Keep the legacy split middleware only for apps that explicitly want user-only or agent-only handling:

Export	Behavior
eveUserAuth()	User-only non-blocking middleware. Attaches req.eveUser: { id, email, orgId, role }.
eveAuthGuard()	Returns 401 if req.eveUser is not set.
eveAuthMiddleware()	Blocking middleware for agent/job tokens. Attaches req.agent with full EveTokenClaims. Returns 401 on failure.
verifyEveToken(token)	JWKS-based local verification (15-min cache). Returns EveTokenClaims.
verifyEveTokenRemote(token)	HTTP verification via /auth/token/verify. Always current.

Express setup (~3 lines):

import { eveAuth, eveIdentityGuard, eveAuthConfig, eveAuthMe } from '@eve-horizon/auth';

app.use(eveAuth());
app.get('/auth/config', eveAuthConfig());
app.get('/auth/me', eveAuthMe());               // Full response for React SDK
app.use('/api', eveIdentityGuard());


req.eveIdentity normalizes both token types:

User token: id, email, orgId, role, permissions, isAgent: false
Agent/job token: jobId, agentSlug, stable email as {agent_slug}@eve.agent, permissions, isAgent: true

Use agentSlug or the stable agent email for RLS, audit logs, and app-level routing. Do not key agent identity off {job_id}@eve.agent; that older pattern was per-job and unstable.

NestJS setup: apply eveAuth() globally in main.ts, then use a thin guard wrapper:

// main.ts
import { eveAuth } from '@eve-horizon/auth';
app.use(eveAuth());

// auth.guard.ts -- thin NestJS adapter
@Injectable()
export class EveGuard implements CanActivate {
  canActivate(ctx: ExecutionContext): boolean {
    const req = ctx.switchToHttp().getRequest();
    if (!req.eveIdentity) throw new UnauthorizedException();
    return true;
  }
}

// auth-config.controller.ts
@Controller()
export class AuthConfigController {
  private handler = eveAuthConfig();

  @Get('auth/config')
  getConfig(@Req() req, @Res() res) { this.handler(req, res); }
}


Verification strategies: eveAuth() and eveUserAuth() default to 'local' (JWKS, cached 15 min). Use strategy: 'remote' for immediate membership freshness at ~50ms latency per request.

Custom role mapping: If your app needs roles beyond Eve's owner/admin/member, bridge after eveAuth():

app.use((req, _res, next) => {
  if (req.eveIdentity && !req.eveIdentity.isAgent) {
    req.user = {
      ...req.eveIdentity,
      appRole: req.eveIdentity.role === 'member' ? 'viewer' : 'admin',
    };
  }
  next();
});

Frontend (@eve-horizon/auth-react)

Install: npm install @eve-horizon/auth-react

Export	Purpose
EveAuthProvider	Context provider. Bootstraps session: checks sessionStorage, probes SSO /session, caches tokens.
useEveAuth()	Hook: { user, loading, error, config, loginWithSso, loginWithToken, logout }
EveLoginGate	Renders children when authenticated, login form otherwise.
EveLoginForm	Built-in SSO + token-paste login UI.
createEveClient(baseUrl?)	Fetch wrapper with automatic Bearer injection.

Simple setup -- EveLoginGate handles the loading/login/authenticated states:

import { EveAuthProvider, EveLoginGate } from '@eve-horizon/auth-react';

<EveAuthProvider apiUrl="/api">
  <EveLoginGate>
    <ProtectedApp />
  </EveLoginGate>
</EveAuthProvider>


Custom auth gate -- use useEveAuth() for full control over loading, login, and error states:

import { EveAuthProvider, useEveAuth } from '@eve-horizon/auth-react';

function AuthGate() {
  const { user, loading, loginWithToken, loginWithSso, logout } = useEveAuth();
  if (loading) return <Spinner />;
  if (!user) return <LoginPage onSso={loginWithSso} onToken={loginWithToken} />;
  return <App user={user} onLogout={logout} />;
}

export default () => (
  <EveAuthProvider apiUrl="/api">
    <AuthGate />
  </EveAuthProvider>
);


API calls with auth: Use createEveClient() for automatic Bearer token injection:

import { createEveClient } from '@eve-horizon/auth-react';
const client = createEveClient('/api');
const res = await client.fetch('/data');

Migration from Custom Auth

The SDK replaces ~700-800 lines of hand-rolled auth with ~50 lines. Delete custom JWKS/token verification, Bearer extraction middleware, SSO URL discovery, session probe logic, token storage helpers, and login form. Keep app-specific role mapping and local password auth.

For the full migration checklist, types reference, token lifecycle, and advanced patterns (SSE auth, token paste mode, token staleness), see references/app-sso-integration.md.

BYOK Model (LLM API Keys)

Eve does not proxy inference traffic. All model access is BYOK (Bring Your Own Keys): harnesses and apps bring their own API keys via secrets and call providers directly.

Store LLM provider keys as project secrets:

eve secrets set ANTHROPIC_API_KEY "sk-ant-xxx" --project proj_xxx
eve secrets set OPENAI_API_KEY "sk-xxx" --project proj_xxx
eve secrets set OPENAI_BASE_URL "https://my-vllm.runpod.ai/v1" --project proj_xxx


Harnesses resolve these automatically. For self-hosted models (vLLM, LM Studio via Tailscale), set the base URL and API key as secrets -- Eve provides connectivity via private endpoints (see eve-deploy-debugging), not a managed inference layer.

Per-Org OAuth Credentials (BYOA)

Each org brings its own OAuth app credentials for Google Drive, Slack, and other integrations. No cluster-level shared secrets.

# View setup instructions (redirect URIs, required scopes)
eve integrations setup-info google-drive
eve integrations setup-info slack

# Register OAuth app credentials
eve integrations configure google-drive \
  --client-id "xxx.apps.googleusercontent.com" \
  --client-secret "GOCSPX-xxx" \
  --label "Acme Corp Google Drive"

eve integrations configure slack \
  --client-id "12345.67890" \
  --client-secret "abc123" \
  --signing-secret "def456" \
  --app-id "A0123ABC" \
  --label "Acme Corp Slack Bot"

# View current config (secrets redacted)
eve integrations config google-drive

# Then connect as before (uses per-org credentials)
eve integrations connect google-drive
eve integrations connect slack


Benefits: isolated credentials per org, custom consent screen branding, independent rate limits, no shared-secret blast radius.

Project Role Resolution

Role and org membership changes take effect immediately -- the server resolves permissions from live DB memberships, not stale JWT claims. When a request includes a project_id but no org_id, the permission guard derives the org context from the project's owning org.

The Auth SDK (@eve-horizon/auth) exposes this via eveUserAuth() middleware. Use strategy: 'remote' for immediate membership freshness when needed.

Project Secrets
# Set a secret
eve secrets set API_KEY "your-api-key" --project proj_xxx

# List keys (no values)
eve secrets list --project proj_xxx

# Delete a secret
eve secrets delete API_KEY --project proj_xxx

# Import from file
eve secrets import .env --project proj_xxx

Secret Interpolation

Reference secrets in .eve/manifest.yaml using ${secret.KEY}:

services:
  api:
    environment:
      API_KEY: ${secret.API_KEY}

Manifest Validation

Validate that all required secrets are set before deploying:

eve manifest validate --validate-secrets    # check secret references
eve manifest validate --strict              # fail on missing secrets

Local Secrets File

For local development, create .eve/dev-secrets.yaml (gitignored):

secrets:
  default:
    API_KEY: local-dev-key
    DB_PASSWORD: local-password
  staging:
    DB_PASSWORD: staging-password

Worker Injection

At job execution time, resolved secrets are injected as environment variables into the worker container. File-type secrets are written to disk and referenced via EVE_SECRETS_FILE. The file is removed after the agent process reads it.

Git Auth

The worker uses secrets for repository access:

HTTPS: github_token secret → Authorization: Bearer header
SSH: ssh_key secret → written to ~/.ssh/ and used via GIT_SSH_COMMAND
Troubleshooting
Problem	Fix
Not authenticated	Run eve auth login
Token expired	Re-run eve auth login (tokens auto-refresh if within 5 min of expiry)
Bootstrap already completed	Use eve auth login (existing user) or eve admin invite (new users). On non-prod stacks, eve auth bootstrap auto-attempts server recovery. For wrong-email recovery: eve auth bootstrap --email correct@example.com
Secret missing	Confirm with eve secrets list and set the key
Interpolation error	Verify ${secret.KEY} spelling; run eve manifest validate --validate-secrets
Git clone failed	Check github_token or ssh_key secret is set
Service can't reach API	Verify EVE_API_URL is injected (check eve env show)
Scoped access denied	Run eve access explain <permission> <resource> --org <org> to see scope match details. Check that the binding's scope constraints include the target path/schema
Wrong role shown	Role is resolved from live DB memberships. Run eve auth permissions to see effective role. If multi-org, check eve auth status for per-org membership listing
Short-lived Claude token in jobs	Run eve auth creds to check token type. If oauth (not setup-token), regenerate with claude setup-token then re-sync with eve auth sync
Codex token expired between jobs	Automatic write-back should refresh it. If not, re-run eve auth sync. Check that ~/.codex/auth.json or ~/.code/auth.json has a fresh token
App SSO not working	Verify EVE_SSO_URL is injected (eve env show). For local dev, set EVE_SSO_URL, EVE_ORG_ID, and EVE_API_URL manually
Stale org membership in app tokens	Default 1-day TTL. Use strategy: 'remote' in eveUserAuth() for immediate membership checks
Incident Response (Secret Leak)

If a secret may be compromised:

Contain: Rotate the secret immediately via eve secrets set
Invalidate: Redeploy affected environments
Audit: Check eve job list for recent jobs that used the secret
Recover: Generate new credentials at the source (GitHub, AWS, etc.)
Document: Record the incident and update rotation procedures
Weekly Installs
250
Repository
incept5/eve-skillpacks
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail