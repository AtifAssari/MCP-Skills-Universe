---
title: setup-api-key
url: https://skills.sh/elevenlabs/skills/setup-api-key
---

# setup-api-key

skills/elevenlabs/skills/setup-api-key
setup-api-key
Installation
$ npx skills add https://github.com/elevenlabs/skills --skill setup-api-key
Summary

Interactive guide for obtaining and configuring an ElevenLabs API key.

Checks for existing ELEVENLABS_API_KEY in environment or .env file and validates it before prompting for setup
Walks users through account creation and key generation at elevenlabs.io, with clear copy-paste instructions
Validates the provided key via API call to https://api.elevenlabs.io/v1/user and saves it to .env on success
Requires internet access to elevenlabs.io and api.elevenlabs.io; retries validation once if the key fails initially
SKILL.md
ElevenLabs API Key Setup

Guide the user through obtaining and configuring an ElevenLabs API key.

Workflow
Step 0: Check for an existing API key first

Before asking the user for a key, check for an existing ELEVENLABS_API_KEY:

Check whether ELEVENLABS_API_KEY exists in the current environment.
If it's not in the environment, check .env for ELEVENLABS_API_KEY=<value>.
If an existing key is found, validate it:
GET https://api.elevenlabs.io/v1/user
Header: xi-api-key: <existing-api-key>

If existing key validation succeeds:
Tell the user ElevenLabs is already configured and working
Skip the setup flow
Ask whether they want to replace/rotate the key; if not, stop
If existing key validation fails:
Tell the user the existing key appears invalid or expired
Continue to Step 1
Step 1: Request the API key

Tell the user:

To set up ElevenLabs, open the API keys page: https://elevenlabs.io/app/settings/api-keys

(Need an account? Create one at https://elevenlabs.io/app/sign-up first)

If you don't have an API key yet:

Click "Create key"
Name it (or use the default)
Set permission for your key. If you provide a key with "User" permission set to "Read" this skill will automatically verify if your key works
Click "Create key" to confirm
Copy the key immediately - it's only shown once!

Paste your API key here when ready.

Then wait for the user's next message which should contain the API key.

Step 2: Validate and configure

Once the user provides the API key:

Validate the key by making a request:

GET https://api.elevenlabs.io/v1/user
Header: xi-api-key: <the-api-key>


If validation fails:

Tell the user the API key appears to be invalid
Ask them to try again
Remind them of the URL: https://elevenlabs.io/app/settings/api-keys
If it fails a second time, display an error and exit

If validation succeeds, save the API key in a .env file:

ELEVENLABS_API_KEY=<the-api-key>

If .env already has ELEVENLABS_API_KEY=..., replace that line
Otherwise add a new line for ELEVENLABS_API_KEY

Confirm success:

Done! Your key is stored as an environment variable in .env Keep the key safe! Don't share it with anyone!

Weekly Installs
2.2K
Repository
elevenlabs/skills
GitHub Stars
208
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail