---
title: cyrus-setup-claude-auth
url: https://skills.sh/ceedaragents/cyrus/cyrus-setup-claude-auth
---

# cyrus-setup-claude-auth

skills/ceedaragents/cyrus/cyrus-setup-claude-auth
cyrus-setup-claude-auth
Installation
$ npx skills add https://github.com/ceedaragents/cyrus --skill cyrus-setup-claude-auth
SKILL.md

CRITICAL: Never use Read, Edit, or Write tools on ~/.cyrus/.env or any file inside ~/.cyrus/. Use only Bash commands (grep, printf >>, etc.) to interact with env files — secrets must never be read into the conversation context.

Setup Claude Auth

Configures Claude Code credentials so Cyrus can run AI sessions.

Step 1: Check Existing Auth

Check if credentials are already configured:

grep -c -E '^(ANTHROPIC_API_KEY|CLAUDE_CODE_OAUTH_TOKEN)=' ~/.cyrus/.env 2>/dev/null || echo "0"


If the count is >= 1, inform the user:

Claude Code authentication is already configured. Skipping this step. To reconfigure, remove the existing key from ~/.cyrus/.env and re-run this skill.

Skip to completion.

Step 2: Choose Auth Method

Ask the user:

How would you like to authenticate Claude Code?

Current account (easiest) — use the credentials from your active claude CLI session
API Key — from console.anthropic.com
Separate OAuth token — run claude setup-token to generate a token for a specific account
Third-Party Provider — Vertex AI, AWS Bedrock, Azure, etc.
Step 3: Configure Credentials

CRITICAL: Secrets must NEVER appear in the conversation. Do not explore ~/.claude/ looking for credential files. Use only the methods below.

Detect the OS for the right clipboard command:

uname -s

Option 1: Current Account

Check if claude is authenticated on this machine:

claude auth status


If authenticated, instruct the user to run claude setup-token which will output a token.

To capture it safely, append a placeholder line to the env file, then open it in a GUI window so the user can paste the token:

grep -q '^CLAUDE_CODE_OAUTH_TOKEN=' ~/.cyrus/.env || echo 'CLAUDE_CODE_OAUTH_TOKEN=' >> ~/.cyrus/.env


Then open the file in a separate window — use whatever GUI editor is available:

# macOS: VS Code if available, otherwise TextEdit
code --new-window ~/.cyrus/.env 2>/dev/null || open -a TextEdit ~/.cyrus/.env

# Linux
code ~/.cyrus/.env 2>/dev/null || xdg-open ~/.cyrus/.env


Tell the user:

Run claude setup-token in a separate terminal
Copy the token it outputs
I've opened ~/.cyrus/.env — find the CLAUDE_CODE_OAUTH_TOKEN= line
Paste the token right after the = (no spaces, no newline)
Save and close the file
Option 2: API Key

Instruct the user to copy their API key from the Anthropic Console, then provide the appropriate command:

macOS:

printf 'ANTHROPIC_API_KEY=%s\n' "$(pbpaste)" >> ~/.cyrus/.env


Linux:

printf 'ANTHROPIC_API_KEY=%s\n' "$(xclip -selection clipboard -o)" >> ~/.cyrus/.env


Universal fallback:

read -s -p "Paste your Anthropic API key: " val && printf 'ANTHROPIC_API_KEY=%s\n' "$val" >> ~/.cyrus/.env && echo " ✓ Saved"

Option 3: Separate OAuth Token

This is for when the user wants to generate a token for a different account than the one currently logged in (e.g., running claude setup-token on another machine).

Append the placeholder, then open the file for the user to paste:

grep -q '^CLAUDE_CODE_OAUTH_TOKEN=' ~/.cyrus/.env || echo 'CLAUDE_CODE_OAUTH_TOKEN=' >> ~/.cyrus/.env

# macOS
code --new-window ~/.cyrus/.env 2>/dev/null || open -a TextEdit ~/.cyrus/.env
# Linux
code ~/.cyrus/.env 2>/dev/null || xdg-open ~/.cyrus/.env


Tell the user:

On the other machine, run claude setup-token
Copy the token it outputs
I've opened ~/.cyrus/.env — find CLAUDE_CODE_OAUTH_TOKEN= and paste the token after the =
Save and close
Option 4: Third-Party Provider

Inform the user:

For third-party providers, you'll need to set provider-specific environment variables. See Third-Party Integrations for details.

Common configurations:

AWS Bedrock:

CLAUDE_CODE_USE_BEDROCK=1
AWS_REGION=us-east-1


Google Vertex AI:

CLAUDE_CODE_USE_VERTEX=1
CLOUD_ML_REGION=us-east5
ANTHROPIC_VERTEX_PROJECT_ID=your-project-id


Guide the user to add the appropriate variables to ~/.cyrus/.env using the clipboard-to-env pattern.

Step 4: Verify

After the user runs the command, verify the key was written:

grep -c -E '^(ANTHROPIC_API_KEY|CLAUDE_CODE_OAUTH_TOKEN|CLAUDE_CODE_USE_BEDROCK|CLAUDE_CODE_USE_VERTEX)=' ~/.cyrus/.env


If the count is 0, the credential was not saved. Ask the user to try again.

Completion

✓ Claude Code authentication configured.

Weekly Installs
146
Repository
ceedaragents/cyrus
GitHub Stars
564
First Seen
Mar 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass