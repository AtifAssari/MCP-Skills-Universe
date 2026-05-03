---
rating: ⭐⭐
title: rw-recipe-full-setup
url: https://skills.sh/runwayml/skills/rw-recipe-full-setup
---

# rw-recipe-full-setup

skills/runwayml/skills/rw-recipe-full-setup
rw-recipe-full-setup
Installation
$ npx skills add https://github.com/runwayml/skills --skill rw-recipe-full-setup
SKILL.md
Full Runway API Setup

PREREQUISITE: Run +rw-check-compatibility first to ensure the project has server-side capability.

This recipe guides a user through the complete process of integrating Runway's public API into their project. It chains together the compatibility check, API key setup, and API integration skills.

Workflow
Phase 1: Compatibility Check

Use +rw-check-compatibility to analyze the user's project.

Identify the project type (Node.js, Python, etc.)
Verify server-side capability
Check runtime version compatibility
Look for existing Runway SDK installation

If the project is INCOMPATIBLE, stop and explain the options:

Add a backend (Express, FastAPI, etc.)
Use a fullstack framework (Next.js, SvelteKit, Nuxt, Remix)
Add serverless functions (Vercel Functions, AWS Lambda)
Create a separate backend service

If NEEDS CHANGES, help the user make the required changes before proceeding.

If COMPATIBLE, proceed to Phase 2.

Phase 2: API Key Setup

Use +rw-setup-api-key to configure credentials.

Direct the user to https://dev.runwayml.com/ to create an account and API key
Install the appropriate SDK (@runwayml/sdk for Node.js, runwayml for Python)
Configure the RUNWAYML_API_SECRET environment variable
Update .gitignore to exclude .env
Remind about credit purchase requirement ($10 minimum)

Wait for the user to confirm they have their API key before proceeding.

Phase 3: Determine What to Integrate

Ask the user what they want to build. Based on their response, use the appropriate integration skill:

User wants...	Skill to use
Generate videos from text	+rw-integrate-video (text-to-video)
Animate images into video	+rw-integrate-video (image-to-video) + +rw-integrate-uploads if local files
Edit/transform existing videos	+rw-integrate-video (video-to-video) + +rw-integrate-uploads
Generate images from text	+rw-integrate-image
Generate images with references	+rw-integrate-image + +rw-integrate-uploads if local refs
Text-to-speech	+rw-integrate-audio
Sound effects	+rw-integrate-audio
Voice isolation/dubbing	+rw-integrate-audio + +rw-integrate-uploads
Real-time conversational avatar	+rw-integrate-characters + +rw-integrate-character-embed (React UI)
Avatar with domain knowledge	+rw-integrate-characters + +rw-integrate-documents + +rw-integrate-character-embed
Multiple capabilities	Integrate each one, sharing the same client instance
Phase 4: Write the Integration Code

Based on the user's framework and needs:

Create the API route/handler — server-side endpoint that calls Runway
Add upload handling if the user needs to accept files from their users
Add error handling — catch and handle task failures
Handle output storage — remind user that output URLs expire in 24-48 hours
Phase 5: Test and Verify

Help the user:

Run a test generation to verify everything works
Check for common issues (missing env var, insufficient credits, wrong model)
Confirm output is accessible
Decision Tree for Upload Requirements

When the user's workflow involves images or videos as input:

Does the input come from a public HTTPS URL?
├── YES → Pass the URL directly to the API
└── NO → Is it a local file or user-uploaded file?
    ├── YES → Use +rw-integrate-uploads to upload first, then pass runway:// URI
    └── NO → Is it small enough for a data URI? (< 5MB image, < 16MB video)
        ├── YES → Convert to base64 data URI
        └── NO → Use +rw-integrate-uploads

Important Reminders
Never expose the API key in client-side code. All API calls must happen server-side.
Output URLs expire. Always download and store generated content.
Credits are required. The API won't work without prepaid credits.
Rate limits exist. Rate limits exist. You should always check what is the rate limit before attempting concurrent generations.
Content moderation applies to both inputs and outputs. Safety-flagged inputs are non-refundable.
Be cost-conscious. Help users pick the right model for their budget. Credit cost can be found on https://docs.dev.runwayml.com/guides/pricing/
Weekly Installs
37
Repository
runwayml/skills
GitHub Stars
30
First Seen
4 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn