---
title: sf-connected-apps
url: https://skills.sh/jaganpro/sf-skills/sf-connected-apps
---

# sf-connected-apps

skills/jaganpro/sf-skills/sf-connected-apps
sf-connected-apps
Installation
$ npx skills add https://github.com/jaganpro/sf-skills --skill sf-connected-apps
SKILL.md
sf-connected-apps: Salesforce Connected Apps & External Client Apps

Use this skill when the user needs OAuth app configuration in Salesforce: Connected Apps, External Client Apps (ECAs), JWT bearer setup, PKCE decisions, scope design, or migration from older Connected App patterns to newer ECA patterns.

When This Skill Owns the Task

Use sf-connected-apps when the work involves:

.connectedApp-meta.xml or .eca-meta.xml files
OAuth flow selection and callback / scope setup
JWT bearer auth, device flow, client credentials, or auth-code decisions
Connected App vs External Client App architecture choices
consumer-key / secret / certificate handling strategy

Delegate elsewhere when the user is:

configuring Named Credentials or runtime callouts → sf-integration
analyzing access / permission policy assignments → sf-permissions
writing Apex token-handling code → sf-apex
deploying metadata to orgs → sf-deploy
First Decision: Connected App or External Client App
If the need is...	Prefer
simple single-org OAuth app	Connected App
new development with better secret handling	External Client App
multi-org / packaging / stronger operational controls	External Client App
straightforward legacy compatibility	Connected App

Default guidance:

choose ECA for new regulated, packageable, or automation-heavy solutions
choose Connected App when simplicity and legacy compatibility matter more
Spring ’26 note: creation of new Connected Apps is disabled by default in orgs. For new integrations, prefer External Client Apps unless Connected App compatibility is explicitly required.
Required Context to Gather First

Ask for or infer:

app type: Connected App or ECA
OAuth flow: auth code, PKCE, JWT bearer, device, client credentials
client type: confidential vs public
callback URLs / redirect surfaces
required scopes
distribution model: local org only vs packageable / multi-org
whether certificates or secret rotation are required
Recommended Workflow
1. Choose the app model

Decide whether a Connected App or ECA is the better long-term fit.

2. Choose the OAuth flow
Use case	Default flow
backend web app	Authorization Code
SPA / mobile / public client	Authorization Code + PKCE
server-to-server / CI/CD	JWT Bearer
device / CLI auth	Device Flow
service account style app	Client Credentials (typically ECA)
3. Start from the right template

Use the provided assets instead of building from scratch:

assets/connected-app-basic.xml
assets/connected-app-oauth.xml
assets/connected-app-jwt.xml
assets/external-client-app.xml
assets/eca-global-oauth.xml
assets/eca-oauth-settings.xml
assets/eca-policies.xml

If you need source-controlled ECA OAuth security metadata, retrieve it from an org first and treat the retrieved file as the schema source of truth:

sf project retrieve start --metadata ExtlClntAppOauthSecuritySettings:<AppName> --target-org <alias>
4. Apply security hardening

Favor:

least-privilege scopes
explicit callback URLs
PKCE for public clients
certificate-based auth where appropriate
rotation-ready secret / key handling
IP restrictions when realistic and maintainable
5. Validate deployment readiness

Before handoff, confirm:

metadata file naming is correct
scopes are justified
callback and auth model match the real client type
secrets are not embedded in source
High-Signal Security Rules

Avoid these anti-patterns:

Anti-pattern	Why it fails
wildcard / overly broad callback URLs	token interception risk
Full scope by default	unnecessary privilege
PKCE disabled for public clients	code interception risk
consumer secret committed to source	credential exposure
no rotation / cert strategy for automation	brittle long-term ops

Default fix direction:

narrow scopes
constrain callbacks
enable PKCE for public clients
keep secrets outside version control
use JWT certificates or controlled secret storage where appropriate
Metadata Notes That Matter
Connected App

Usually lives under:

force-app/main/default/connectedApps/
External Client App

Current source-supported ECA metadata uses multiple top-level source directories, not a single externalClientApps/ folder:

force-app/main/default/externalClientApps/ → ExternalClientApplication (.eca-meta.xml)
force-app/main/default/extlClntAppGlobalOauthSets/ → ExtlClntAppGlobalOauthSettings (.ecaGlblOauth-meta.xml)
force-app/main/default/extlClntAppOauthSettings/ → ExtlClntAppOauthSettings (.ecaOauth-meta.xml)
force-app/main/default/extlClntAppOauthSecuritySettings/ → ExtlClntAppOauthSecuritySettings (.ecaOauthSecurity-meta.xml)
force-app/main/default/extlClntAppOauthPolicies/ → ExtlClntAppOauthConfigurablePolicies (.ecaOauthPlcy-meta.xml)
force-app/main/default/extlClntAppPolicies/ → ExtlClntAppConfigurablePolicies (.ecaPlcy-meta.xml)

Important file-name gotchas:

the global OAuth suffix is .ecaGlblOauth, not .ecaGlobalOauth
the general policy suffix is .ecaPlcy, not .ecaPolicy
use .ecaOauthSecurity for ExtlClntAppOauthSecuritySettings
Output Format

When finishing, report in this order:

App type chosen
OAuth flow chosen
Files created or updated
Security decisions
Next deployment / testing step

Suggested shape:

App: <name>
Type: Connected App | External Client App
Flow: <oauth flow>
Files: <paths>
Security: <scopes, PKCE, certs, secrets, IP policy>
Next step: <deploy, retrieve consumer key, or test auth flow>

Cross-Skill Integration
Need	Delegate to	Reason
Named Credential / callout runtime config	sf-integration	runtime integration setup
deploy app metadata	sf-deploy	org validation and deployment
Apex token or refresh handling	sf-apex	implementation logic
permission review after deployment	sf-permissions	access governance
Reference Map
Start here
references/oauth-flows-reference.md
references/security-checklist.md
references/testing-validation-guide.md
Migration / examples
references/migration-guide.md
references/example-usage.md
assets/
Score Guide
Score	Meaning
80+	production-ready OAuth app config
54–79	workable but needs hardening review
< 54	block deployment until fixed
Weekly Installs
1.1K
Repository
jaganpro/sf-skills
GitHub Stars
404
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass