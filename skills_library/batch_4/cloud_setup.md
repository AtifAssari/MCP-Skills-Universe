---
title: cloud-setup
url: https://skills.sh/elastic/agent-skills/cloud-setup
---

# cloud-setup

skills/elastic/agent-skills/cloud-setup
cloud-setup
Installation
$ npx skills add https://github.com/elastic/agent-skills --skill cloud-setup
SKILL.md
Cloud Environment Setup

Configure Elastic Cloud authentication and preferences. All other cloud/* skills depend on this setup.

Workflow
Setup Progress:
- [ ] Step 1: Verify API key
- [ ] Step 2: Set defaults
- [ ] Step 3: Validate connection

Step 1: Verify API key

Check whether EC_API_KEY is already set:

echo "${EC_API_KEY:?Not set}"


If not set, instruct the user to set it. Never ask the user to paste an API key into the chat — secrets must not appear in conversation history.

If the user indicates they do not have an Elastic Cloud account yet, propose starting a free trial at Elastic Cloud free trial. The trial provides 14 days of full access to Elastic Cloud Serverless with no credit card required. Once the user has registered and logged in, proceed with API key generation below.

Direct the user to:

Generate a key at Elastic Cloud API keys. Only Organization owners can create and manage Cloud API keys.
When creating this key, include Project Admin privileges or higher (Org Owner) so it can create and manage serverless projects.
Create a .env file in the project root (recommended — works in sandboxed agent shells):
EC_API_KEY=your-api-key


All cloud/* scripts auto-load .env from the working directory — no manual sourcing needed.

Alternatively, export directly in the terminal:

export EC_API_KEY="your-api-key"


Terminal exports might not be visible to sandboxed agents running in a separate shell session. Prefer the .env file when working with an agent.

Remind the user that storing secrets in local files is acceptable for development, but for production or shared environments, use a centralized secrets manager (for example, HashiCorp Vault, AWS Secrets Manager, 1Password CLI) to avoid secrets sprawl.

Step 2: Set defaults

Export the base URL and default region:

export EC_BASE_URL="https://api.elastic-cloud.com"
export EC_REGION="gcp-us-central1"


Ask the user if they want a different region. To list available regions:

curl -s -H "Authorization: ApiKey ${EC_API_KEY}" \
  "${EC_BASE_URL}/api/v1/serverless/regions" | python3 -m json.tool

Step 3: Validate connection

Confirm the API key works by calling the regions endpoint:

curl -sf -H "Authorization: ApiKey ${EC_API_KEY}" \
  "${EC_BASE_URL}/api/v1/serverless/regions" > /dev/null && echo "Authenticated." || echo "Authentication failed."


If validation fails, check:

The API key is valid and not expired
Network connectivity to api.elastic-cloud.com
Examples
First-time setup
User: set up my cloud environment
Agent: Check if EC_API_KEY is set in your terminal. If not, generate a key at
       https://cloud.elastic.co/account/keys and run:
       export EC_API_KEY="your-key"
       Then confirm and I'll validate the connection.

Setup with custom region
User: set up cloud with eu region
Agent: [runs setup, sets EC_REGION to user's preferred EU region]

Guidelines
Never receive, echo, or log API keys, passwords, or any credentials in the chat. Instruct the user to manage secrets in their terminal or using files directly.
Always validate the connection after setting the key.
Default region is gcp-us-central1 — only change if the user requests a different region.
This skill is a prerequisite. Other cloud skills should refer here when EC_API_KEY is missing.
Environment variables
Variable	Required	Description
EC_API_KEY	Yes	Elastic Cloud API key
EC_BASE_URL	No	Cloud API base URL (default: https://api.elastic-cloud.com)
EC_REGION	No	Default region (default: gcp-us-central1)
Troubleshooting
Problem	Fix
401 Unauthorized	API key is invalid or expired — generate a new one
connection refused	Check network access to api.elastic-cloud.com
Weekly Installs
390
Repository
elastic/agent-skills
GitHub Stars
451
First Seen
Mar 13, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass