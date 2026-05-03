---
title: ghl ai agents
url: https://skills.sh/justin322322/ghl-skills/ghl-ai-agents
---

# ghl ai agents

skills/justin322322/ghl-skills/GHL AI Agents
GHL AI Agents
Installation
$ npx skills add https://github.com/justin322322/ghl-skills --skill 'GHL AI Agents'
SKILL.md
GHL AI Agents
Overview

GoHighLevel offers AI-powered automation through Voice AI (phone calls), Conversation AI (chat/SMS/social), Workflow AI (automation building), and Review AI (review management). Together, these function as a 24/7 digital employee.

AI Employee Types
Type	Channel	Capabilities
Voice AI	Phone calls (inbound)	Answer calls, qualify leads, book appointments, collect info
Conversation AI	SMS, Facebook, Instagram, Chat Widget, Live Chat	Respond to messages, answer FAQs, book appointments
Workflow AI	Workflow builder	Generate workflow steps using natural language prompts
Review AI	Review platforms	Automate review requests and responses
Content AI	Email, SMS, Funnels	Generate marketing copy, subject lines, content
Voice AI Setup
Prerequisites
Agency Pro plan or higher
LC Phone number (not Twilio) with A2P verification (US)
AI Employee feature enabled at the agency level
Step-by-Step Configuration

Navigate to Settings → AI Agents

Create a new agent:

Agent Name: Descriptive name (e.g., "Front Desk AI")
Business Name: Your business name for context
Voice: Select from available voices; preview before choosing
Language/Accent: Match your target audience
Greeting: Set the initial message (e.g., "Hello, you've reached [Business]. How can I help?")

Assign Phone Number:

Go to Phone & Availability tab
Assign an LC Phone number
Configure call routing:
AI answers all calls directly, OR
AI as backup (waits for human first, picks up if no answer)

Configure Agent Goals:

Basic Mode: Simple objective selection
Advanced Mode: Detailed prompt with specific instructions

Connect Calendar:

Sync calendars for real-time appointment booking
Select which calendar the AI should use for bookings
Voice AI Prompt Engineering
Basic Guidelines
You are a friendly, professional receptionist for [Business Name].
Your primary goals are:
1. Greet the caller warmly
2. Identify their reason for calling
3. Book an appointment if appropriate
4. Collect their name, email, and phone number
5. If you can't help, offer to transfer to a team member

Important rules:
- Never make up information you don't know
- Always confirm details before booking
- Keep responses concise and natural
- If asked about pricing, say "[specific response]"
- For emergencies, direct them to [number/action]

Advanced Prompt Template
## Identity
You are [Name], the virtual assistant for [Business Name].
Personality: [Professional / Friendly / Casual]
Tone: [Warm and helpful / Direct and efficient]

## Goals (in priority order)
1. [Primary goal — e.g., Book a consultation]
2. [Secondary goal — e.g., Collect contact info]
3. [Tertiary goal — e.g., Answer FAQs]

## Knowledge
- Services offered: [list]
- Business hours: [hours]
- Location: [address]
- Pricing: [how to handle pricing questions]

## Handling Specific Scenarios
- If caller asks about [topic]: [specific response]
- If caller is upset: [de-escalation approach]
- If caller asks to speak to a human: [transfer/callback protocol]
- If outside business hours: [after-hours message]

## Restrictions
- DO NOT: [list things the AI should never do]
- ALWAYS: [list things the AI must do]

Conversation AI Setup
Supported Channels
SMS / MMS
Facebook Messenger
Instagram DMs
Website Chat Widget
Live Chat
Google Business Messages
Configuration Steps
Navigate to Settings → Conversation AI
Enable channels where the bot should operate
Set mode:
Autopilot: Fully automated responses
Suggestive: AI suggests responses for human approval
Configure response settings:
Wait time before responding
Maximum messages per conversation
Handoff rules (when to transfer to human)
Training the Knowledge Base

The Conversation AI learns from your provided content to answer questions accurately.

Training Sources:

Source	How
Website URL	Paste your site URL; AI crawls and learns the content
Google Docs	Link docs with FAQs, service descriptions, policies
Manual Q&A	Add specific question-answer pairs directly
File Upload	Upload PDFs, documents with business information

Best Practices:

Start with FAQs — Add the 20 most common questions and ideal answers
Be specific — Vague training data produces vague responses
Update regularly — Add new Q&As as you discover gaps
Test thoroughly — Ask the bot questions from different angles
Review conversations — Check chat logs for incorrect or missed responses
Appointment Booking via Chat
Enable Appointment Booking in Conversation AI settings
Select the target calendar
The AI will:
Suggest available time slots
Confirm the booking details
Create the appointment in the calendar
Send confirmation to the lead
Content AI

Use built-in AI for content generation across GHL:

Feature	Where	What It Does
Email Copy	Email Builder	Generate subject lines, body copy, CTAs
SMS Copy	SMS Action	Draft text messages
Funnel Copy	Page Builder	Write headlines, descriptions, bullet points
Social Posts	Social Planner	Generate social media content
Workflow Prompts	Workflow Builder	Create workflow steps from natural language
AI Best Practices
General
Set clear boundaries — Define exactly what the AI can and cannot do
Start conservative — Begin with limited scope, expand as you gain confidence
Monitor regularly — Review AI conversations daily during the first week
Have a human fallback — Always provide a way to reach a real person
Test edge cases — Ask unusual or adversarial questions to find weak spots
Prompt Engineering Tips
Be literal — The AI follows instructions exactly; be explicit
Use examples — Show desired input/output pairs
Define the persona — Give the AI a name, role, and personality
Set guardrails — Clearly state topics to avoid or redirect
Iterate — Refine prompts based on real conversation analysis
Performance Optimization
Track booking rate — Measure how many conversations result in appointments
Monitor CSAT — Collect satisfaction feedback after AI interactions
Analyze drop-offs — Identify where conversations end without conversion
A/B test prompts — Try different approaches and measure results
Key Resources
Official Guide: GoHighLevel AI Employee Setup
Voice AI Docs: Voice AI Configuration
Prompt Guidelines: Available in the AI Agent Advanced Mode settings
Weekly Installs
–
Repository
justin322322/ghl-skills
GitHub Stars
5
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn