---
rating: ⭐⭐
title: cyrus-setup-endpoint
url: https://skills.sh/ceedaragents/cyrus/cyrus-setup-endpoint
---

# cyrus-setup-endpoint

skills/ceedaragents/cyrus/cyrus-setup-endpoint
cyrus-setup-endpoint
Installation
$ npx skills add https://github.com/ceedaragents/cyrus --skill cyrus-setup-endpoint
SKILL.md

CRITICAL: Never use Read, Edit, or Write tools on ~/.cyrus/.env or any file inside ~/.cyrus/. Use only Bash commands (grep, printf >>, etc.) to interact with env files — secrets must never be read into the conversation context.

Setup Endpoint

Configures a public URL so Linear (and other integrations) can send webhooks to your Cyrus instance.

Step 1: Check Existing Configuration
grep -E '^CYRUS_BASE_URL=' ~/.cyrus/.env 2>/dev/null


If CYRUS_BASE_URL is already set, inform the user:

Webhook endpoint already configured: <value> To reconfigure, remove CYRUS_BASE_URL from ~/.cyrus/.env and re-run this skill.

Skip to Step 4 (write port/webhooks if missing).

Step 2: Choose Endpoint Method

Ask the user:

How will you expose Cyrus to the internet for webhooks?

ngrok (recommended — every free account includes one static domain that persists across restarts)
Cloudflare Tunnel (permanent, requires Cloudflare account)
Own URL (you already have a public URL/domain)

Important: ngrok's free tier includes a permanent static domain — do NOT tell the user this is a paid feature or that URLs change on restart. Every free ngrok account gets one static domain at https://dashboard.ngrok.com/domains.

Step 3: Configure Endpoint
Option 1: ngrok
3a. Check if ngrok is installed
which ngrok


If not installed, provide install instructions:

macOS:

brew install ngrok


Linux:

curl -sSL https://ngrok-agent.s3.amazonaws.com/ngrok-v3-stable-linux-amd64.tgz | sudo tar xvz -C /usr/local/bin

3b. Guide ngrok domain setup

Instruct the user:

ngrok provides a free static domain so your URL doesn't change between restarts.

Sign up or log in at https://dashboard.ngrok.com
Go to https://dashboard.ngrok.com/domains
Copy your free static domain (e.g., your-name-here.ngrok-free.app)
Go to https://dashboard.ngrok.com/get-started/your-authtoken and copy your authtoken

Ask the user to provide:

Their ngrok domain
Their ngrok authtoken

CRITICAL: The authtoken is a secret. Use clipboard-to-file commands.

3c. Write ngrok configuration

Write the ngrok config so it can be started with ngrok start cyrus:

mkdir -p ~/.config/ngrok


Then write ~/.config/ngrok/ngrok.yml (merge with existing if present):

version: 3
agent:
  authtoken: <token>
endpoints:
  - name: cyrus
    url: <domain>
    upstream:
      url: 3456


For the authtoken, use a clipboard-to-file approach:

macOS:

# User copies authtoken, then runs:
NGROK_TOKEN=$(pbpaste) && cat > ~/.config/ngrok/ngrok.yml << EOF
version: 3
agent:
  authtoken: $NGROK_TOKEN
endpoints:
  - name: cyrus
    url: <domain>
    upstream:
      url: 3456
EOF


Universal fallback:

read -s -p "Paste your ngrok authtoken: " NGROK_TOKEN && cat > ~/.config/ngrok/ngrok.yml << EOF
version: 3
agent:
  authtoken: $NGROK_TOKEN
endpoints:
  - name: cyrus
    url: <domain>
    upstream:
      url: 3456
EOF
echo " ✓ Saved"

3d. Write CYRUS_BASE_URL
printf 'CYRUS_BASE_URL=https://%s\n' "<domain>" >> ~/.cyrus/.env


Where <domain> is the ngrok domain the user provided (e.g., your-name-here.ngrok-free.app).

Inform the user:

To start ngrok, run: ngrok start cyrus Run this in a separate terminal before starting Cyrus.

Option 2: Cloudflare Tunnel

Ask the user for:

Their Cloudflare Tunnel token
Their tunnel hostname (e.g., cyrus.yourdomain.com)

Token is a secret — use clipboard-to-env:

macOS:

printf 'CLOUDFLARE_TOKEN=%s\n' "$(pbpaste)" >> ~/.cyrus/.env


Universal fallback:

read -s -p "Paste your Cloudflare token: " val && printf 'CLOUDFLARE_TOKEN=%s\n' "$val" >> ~/.cyrus/.env && echo " ✓ Saved"


Then write the base URL (not a secret — agent can write directly):

printf 'CYRUS_BASE_URL=https://<hostname>\n' >> ~/.cyrus/.env

Option 3: Own URL

Ask the user for their URL. Validate it starts with https://.

printf 'CYRUS_BASE_URL=%s\n' "<url>" >> ~/.cyrus/.env

Step 4: Write Common Config

Ensure these are present in ~/.cyrus/.env (add only if missing):

grep -q '^CYRUS_SERVER_PORT=' ~/.cyrus/.env 2>/dev/null || printf 'CYRUS_SERVER_PORT=3456\n' >> ~/.cyrus/.env
grep -q '^LINEAR_DIRECT_WEBHOOKS=' ~/.cyrus/.env 2>/dev/null || printf 'LINEAR_DIRECT_WEBHOOKS=true\n' >> ~/.cyrus/.env
grep -q '^CYRUS_HOST_EXTERNAL=' ~/.cyrus/.env 2>/dev/null || printf 'CYRUS_HOST_EXTERNAL=true\n' >> ~/.cyrus/.env


LINEAR_DIRECT_WEBHOOKS=true enables direct Linear webhook signature verification. CYRUS_HOST_EXTERNAL=true enables direct Slack and GitHub webhook signature verification. Both are required for self-hosted setups where webhooks come directly from the services (not forwarded through CYHOST).

Completion

✓ Webhook endpoint configured: <CYRUS_BASE_URL> ✓ Server port: 3456 ✓ Direct webhooks: enabled

Weekly Installs
134
Repository
ceedaragents/cyrus
GitHub Stars
564
First Seen
Mar 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn