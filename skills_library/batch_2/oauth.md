---
title: oauth
url: https://skills.sh/vercel-labs/portless/oauth
---

# oauth

skills/vercel-labs/portless/oauth
oauth
Installation
$ npx skills add https://github.com/vercel-labs/portless --skill oauth
SKILL.md
OAuth with Portless

OAuth providers validate redirect URIs against domain rules. .localhost subdomains fail on most providers because they are not in the Public Suffix List or are explicitly blocked. Portless fixes this with --tld to serve apps on real, valid domains.

The Problem

When portless uses the default .localhost TLD, OAuth providers reject redirect URIs like http://myapp.localhost:1355/callback:

Provider	localhost	.localhost subdomains	Reason
Google	Allowed	Rejected	Not in their bundled PSL
Apple	Rejected	Rejected	No localhost at all
Microsoft	Allowed	Allowed	Permissive localhost handling
Facebook	Allowed	Varies	Must register each URI exactly
GitHub	Allowed	Allowed	Permissive

Google and Apple are the strictest. Microsoft and GitHub are more lenient with localhost.

The Fix

Use a valid TLD so the redirect URI passes provider validation:

portless proxy start --tld dev
portless myapp next dev
# -> https://myapp.dev


Any TLD in the Public Suffix List works: .dev, .app, .com, .io, etc.

Use a domain you own

Bare TLDs like .dev mean myapp.dev could collide with a real domain. Use a subdomain of a domain you control:

portless proxy start --tld dev
portless myapp.local.yourcompany next dev
# -> https://myapp.local.yourcompany.dev


This ensures no outbound traffic reaches something you don't own. For teams, set a wildcard DNS record (*.local.yourcompany.dev -> 127.0.0.1) so every developer gets resolution without /etc/hosts.

Provider Setup
Google
Go to Google Cloud Console > Credentials
Create or edit an OAuth 2.0 Client ID (Web application)
Add the portless domain to Authorized JavaScript origins: https://myapp.dev
Add the callback to Authorized redirect URIs: https://myapp.dev/api/auth/callback/google

Google validates domains against the Public Suffix List. The domain must end with a recognized TLD. .localhost subdomains fail this check; .dev, .app, .com, etc. all pass.

HTTPS is required for .dev and .app (HSTS-preloaded). Portless handles this automatically with --https.

Apple

Apple Sign In does not allow localhost or IP addresses at all.

Go to Apple Developer > Certificates, Identifiers & Profiles
Register a Services ID
Configure Sign In with Apple, adding the portless domain as a Return URL: https://myapp.dev/api/auth/callback/apple

The domain must be a real, publicly-resolvable domain name. Since portless maps the domain to 127.0.0.1 locally, the browser resolves it but Apple's server-side validation may require the domain to resolve publicly too. If Apple rejects the domain, add a public DNS A record pointing to 127.0.0.1 for your dev subdomain.

Microsoft (Entra / Azure AD)
Go to Azure Portal > App registrations
Create or edit an app registration
Under Authentication, add a Web redirect URI: https://myapp.dev/api/auth/callback/azure-ad

Microsoft allows http://localhost with any port for development. It also accepts .localhost subdomains in most cases. Using a custom TLD with portless is still recommended for consistency across providers.

Facebook (Meta)
Go to Meta for Developers > App Dashboard
Under Facebook Login > Settings, add the portless URL to Valid OAuth Redirect URIs: https://myapp.dev/api/auth/callback/facebook

Facebook requires each redirect URI to be registered exactly (no wildcards). Strict Mode (enabled by default) enforces exact matching.

GitHub
Go to GitHub Developer Settings > OAuth Apps
Set Authorization callback URL: https://myapp.dev/api/auth/callback/github

GitHub is permissive with localhost and subdomains. A custom TLD is not strictly required but keeps the setup consistent.

Auth Library Configuration
NextAuth / Auth.js

Set NEXTAUTH_URL to match the portless domain:

NEXTAUTH_URL=https://myapp.dev


NextAuth uses this to construct callback URLs. Without it, callbacks may use localhost and cause a mismatch.

Passport.js

Set the callbackURL in each strategy to use the portless domain:

new GoogleStrategy({
  clientID: process.env.GOOGLE_CLIENT_ID,
  clientSecret: process.env.GOOGLE_CLIENT_SECRET,
  callbackURL: process.env.BASE_URL + "/auth/google/callback",
});


Set BASE_URL=https://myapp.dev in your environment.

Generic / Manual

Read the PORTLESS_URL environment variable that portless injects into the child process:

const baseUrl = process.env.PORTLESS_URL || "http://localhost:3000";
const callbackUrl = `${baseUrl}/auth/callback`;

Troubleshooting
"redirect_uri_mismatch" or "invalid redirect URI"

The redirect URI sent during the OAuth flow doesn't match what's registered with the provider. Check:

The provider's registered redirect URI matches the portless domain exactly (protocol, host, path)
NEXTAUTH_URL or equivalent is set to the portless URL (not localhost)
The proxy is running with the correct TLD (portless list to verify)
Provider requires HTTPS

.dev and .app TLDs are HSTS-preloaded, so browsers force HTTPS. Start the proxy:

portless proxy start --tld dev


Portless defaults to HTTPS on port 443 (auto-elevates with sudo). Run portless trust to add the local CA to your system trust store and eliminate browser warnings.

Apple rejects the domain

Apple may require the domain to resolve publicly. Add a DNS A record for your dev subdomain pointing to 127.0.0.1:

myapp.local.yourcompany.dev  A  127.0.0.1


Or use a wildcard: *.local.yourcompany.dev A 127.0.0.1.

Callback goes to wrong URL after sign-in

The auth library is constructing the callback URL from localhost instead of the portless domain. Set the appropriate environment variable:

NextAuth: NEXTAUTH_URL=https://myapp.dev
Auth.js v5: AUTH_URL=https://myapp.dev
Manual: PORTLESS_URL is injected automatically; use it as the base URL
Example

See examples/google-oauth for a complete working example with Next.js + NextAuth + Google OAuth using --tld dev.

Weekly Installs
983
Repository
vercel-labs/portless
GitHub Stars
8.8K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn