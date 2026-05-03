---
rating: ⭐⭐⭐
title: security-secrets
url: https://skills.sh/igorwarzocha/opencode-workflows/security-secrets
---

# security-secrets

skills/igorwarzocha/opencode-workflows/security-secrets
security-secrets
Installation
$ npx skills add https://github.com/igorwarzocha/opencode-workflows --skill security-secrets
SKILL.md

High-signal regex patterns for detecting secrets in codebases.

High-Signal Regex Patterns
Secret Type	Pattern	Notes
AWS Access Key	AKIA[0-9A-Z]{16}	Always 20 chars, starts AKIA
AWS Secret	(?i)aws(.{0,20})?['"][0-9a-zA-Z/+]{40}['"]	40 chars base64-ish
Google API Key	AIza[0-9A-Za-z\-_]{35}	39 chars total
Google OAuth	[0-9]+-[0-9A-Za-z_]{32}\.apps\.googleusercontent\.com	Client ID
Google Service Account	"type":\s*"service_account"	In JSON files
GitHub Token	gh[pousr]_[A-Za-z0-9_]{36,}	ghp_/gho_/ghu_/ghs_/ghr_
GitHub PAT (fine-grained)	github_pat_[A-Za-z0-9_]{22,}	Newer format
GitLab Token	glpat-[A-Za-z0-9\-]{20,}	Personal access token
Stripe Secret	`sk_(live	test)_[0-9a-zA-Z]{24,}`
Stripe Restricted	`rk_(live	test)_[0-9a-zA-Z]{24,}`
Stripe Publishable	`pk_(live	test)_[0-9a-zA-Z]{24,}`
Slack Bot Token	xoxb-[A-Za-z0-9-]+	Bot token
Slack User Token	xoxp-[A-Za-z0-9-]+	User token
Slack Workflow Token	xwfp-[A-Za-z0-9-]+	Workflow token
Slack App Token	xapp-[A-Za-z0-9-]+	App-level token
Slack Webhook	https://hooks\.slack\.com/services/T[A-Z0-9]+/B[A-Z0-9]+/[a-zA-Z0-9]+	
Discord Token	[MN][A-Za-z\d]{23,}\.[\w-]{6}\.[\w-]{27}	Bot token
Discord Webhook	https://discord\.com/api/webhooks/[0-9]+/[A-Za-z0-9_-]+	
OpenAI Key	sk-[A-Za-z0-9]{48}	API key
Anthropic Key	sk-ant-[A-Za-z0-9\-]{32,}	API key
Twilio	SK[a-z0-9]{32}	API key SID
SendGrid	SG\.[a-zA-Z0-9]{22}\.[a-zA-Z0-9]{43}	API key
Mailgun	key-[0-9a-zA-Z]{32}	API key
Mailchimp	[a-f0-9]{32}-us[0-9]{1,2}	API key
Firebase	(?i)firebase[a-z0-9\-]+\.firebaseio\.com	Database URL
Supabase	eyJ[A-Za-z0-9_-]*\.[A-Za-z0-9_-]*\.[A-Za-z0-9_-]*	JWT (check context)
Heroku	[hH]eroku.*[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}	API key
NPM Token	npm_[A-Za-z0-9]{36}	Publish token
PyPI Token	pypi-[A-Za-z0-9_-]{50,}	Upload token
Private Key	`-----BEGIN (RSA	EC
Database URL	`(?i)(postgres	mysql
Password in URL	[a-zA-Z]{3,15}://[^/\\:@]+:[^/\\:@]+@.{1,100}	Basic auth
JWT Secret	`(?i)(jwt[_-]?secret	token[_-]?secret)['"]?\s*[:=]\s*['"][^'"]+['"]`
Generic Secret	`(?i)(password	passwd
CLI Scanning Commands
# Quick grep scan (fast, high signal)
rg -n "(AKIA[0-9A-Z]{16}|sk_(live|test)_|rk_(live|test)_|pk_(live|test)_|xox[baprs]-|xapp-|xwfp-|gh[pousr]_|github_pat_)" .
rg -n "BEGIN (RSA|EC|OPENSSH|DSA|PGP) PRIVATE KEY" .
rg -n "(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*['\"][^'\"]{8,}" .

# Dedicated scanners (thorough)
gitleaks detect --source . --redact --no-git
semgrep scan --config p/secrets --error
trufflehog filesystem . --only-verified


<priority_files>

Files to Prioritize
File Pattern	Risk Level	Why
.env*	CRITICAL	Often contains all secrets
*config*.js/ts/json	HIGH	App configuration
*secret*, *credential*	HIGH	Named suspiciously
docker-compose*.yml	HIGH	DB passwords, service creds
.github/workflows/*.yml	HIGH	CI/CD secrets
*test*, *spec*, *fixture*	MEDIUM	Test data with real creds
*.pem, *.key, *.p12	CRITICAL	Private keys

</priority_files>

Redaction Format

When reporting secrets, MUST always redact:

Original: AKIAIOSFODNN7EXAMPLE
Redacted: AKIA****...****MPLE

Original: sk_test_XXXXYYYYZZZZ11112222
Redacted: sk_****...****2222


Show first 4 + last 4 characters only. MUST instruct immediate rotation.

Weekly Installs
39
Repository
igorwarzocha/op…orkflows
GitHub Stars
111
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass