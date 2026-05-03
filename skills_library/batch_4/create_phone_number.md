---
title: create-phone-number
url: https://skills.sh/vapiai/skills/create-phone-number
---

# create-phone-number

skills/vapiai/skills/create-phone-number
create-phone-number
Installation
$ npx skills add https://github.com/vapiai/skills --skill create-phone-number
SKILL.md
Vapi Phone Number Setup

Import phone numbers from Twilio, Vonage, or Telnyx, or use Vapi's built-in numbers to connect voice assistants to real phone calls.

Setup: Ensure VAPI_API_KEY is set. See the setup-api-key skill if needed.

Quick Start — Buy a Vapi Number

Vapi provides free phone numbers for testing with daily call limits.

curl -X POST https://api.vapi.ai/phone-number \
  -H "Authorization: Bearer $VAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "provider": "vapi",
    "assistantId": "your-assistant-id",
    "name": "Main Support Line"
  }'

Import from Twilio
curl -X POST https://api.vapi.ai/phone-number \
  -H "Authorization: Bearer $VAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "provider": "twilio",
    "number": "+11234567890",
    "twilioAccountSid": "your-twilio-account-sid",
    "twilioAuthToken": "your-twilio-auth-token",
    "assistantId": "your-assistant-id",
    "name": "Twilio Support Line"
  }'

Import from Vonage
curl -X POST https://api.vapi.ai/phone-number \
  -H "Authorization: Bearer $VAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "provider": "vonage",
    "number": "+11234567890",
    "credentialId": "your-vonage-credential-id",
    "assistantId": "your-assistant-id",
    "name": "Vonage Support Line"
  }'

Import from Telnyx
curl -X POST https://api.vapi.ai/phone-number \
  -H "Authorization: Bearer $VAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "provider": "telnyx",
    "number": "+11234567890",
    "credentialId": "your-telnyx-credential-id",
    "assistantId": "your-assistant-id",
    "name": "Telnyx Support Line"
  }'

Assign an Assistant

Every phone number can be linked to an assistant or squad for inbound calls:

curl -X PATCH https://api.vapi.ai/phone-number/{id} \
  -H "Authorization: Bearer $VAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "assistantId": "your-assistant-id"
  }'


Or assign a squad:

curl -X PATCH https://api.vapi.ai/phone-number/{id} \
  -H "Authorization: Bearer $VAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "squadId": "your-squad-id"
  }'

Phone Number Hooks

Configure automated actions when calls come in:

{
  "hooks": [
    {
      "on": "call.ringing",
      "do": [
        {
          "type": "say",
          "exact": "Please hold while we connect you."
        }
      ]
    }
  ]
}

Managing Phone Numbers
# List all phone numbers
curl https://api.vapi.ai/phone-number \
  -H "Authorization: Bearer $VAPI_API_KEY"

# Get a phone number
curl https://api.vapi.ai/phone-number/{id} \
  -H "Authorization: Bearer $VAPI_API_KEY"

# Update a phone number
curl -X PATCH https://api.vapi.ai/phone-number/{id} \
  -H "Authorization: Bearer $VAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"name": "Updated Name"}'

# Delete a phone number
curl -X DELETE https://api.vapi.ai/phone-number/{id} \
  -H "Authorization: Bearer $VAPI_API_KEY"

Inbound Call Flow
Caller dials your Vapi phone number
Vapi routes the call to the assigned assistant or squad
The assistant speaks its firstMessage
The conversation proceeds with the configured model, voice, and tools
Outbound Call Flow
Create a call via POST /call with phoneNumberId and customer.number
Vapi dials the customer from your phone number
When answered, the assistant begins the conversation
Free Number Limitations
Cannot make international calls
Daily call limits apply
For production use, import your own Twilio/Vonage/Telnyx numbers
References
Vapi Phone Numbers Docs
Free Telephony
Phone Number Hooks
Additional Resources

This skills repository includes a Vapi documentation MCP server (vapi-docs) that gives your AI agent access to the full Vapi knowledge base. Use the searchDocs tool to look up anything beyond what this skill covers — advanced configuration, troubleshooting, SDK details, and more.

Auto-configured: If you cloned or installed these skills, the MCP server is already configured via .mcp.json (Claude Code), .cursor/mcp.json (Cursor), or .vscode/mcp.json (VS Code Copilot).

Manual setup: If your agent doesn't auto-detect the config, run:

claude mcp add vapi-docs -- npx -y mcp-remote https://docs.vapi.ai/_mcp/server


See the README for full setup instructions across all supported agents.

Weekly Installs
463
Repository
vapiai/skills
GitHub Stars
39
First Seen
Today
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass