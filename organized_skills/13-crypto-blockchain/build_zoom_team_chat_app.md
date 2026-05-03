---
rating: ⭐⭐⭐
title: build-zoom-team-chat-app
url: https://skills.sh/anthropics/knowledge-work-plugins/build-zoom-team-chat-app
---

# build-zoom-team-chat-app

skills/anthropics/knowledge-work-plugins/build-zoom-team-chat-app
build-zoom-team-chat-app
Installation
$ npx skills add https://github.com/anthropics/knowledge-work-plugins --skill build-zoom-team-chat-app
SKILL.md
/build-zoom-team-chat-app

Background reference for Zoom Team Chat integrations. Use this after the workflow is clear, especially when the Team Chat API versus Chatbot API distinction matters.

Read This First (Critical)

There are two different integration types and they are not interchangeable:

Team Chat API (user type)

Sends messages as a real authenticated user
Uses User OAuth (authorization_code)
Endpoint family: /v2/chat/users/...

Chatbot API (bot type)

Sends messages as your bot identity
Uses Client Credentials (client_credentials)
Endpoint family: /v2/im/chat/messages

If you choose the wrong type early, auth/scopes/endpoints all mismatch and implementation fails.

Official Documentation: https://developers.zoom.us/docs/team-chat/
Chatbot Documentation: https://developers.zoom.us/docs/team-chat/chatbot/extend/
API Reference: https://developers.zoom.us/docs/api/rest/reference/chatbot/

Quick Links

New to Team Chat? Follow this path:

Get Started - End-to-end fast path (user type vs bot type)
Choose Your API - Team Chat API vs Chatbot API
Environment Setup - Credentials, scopes, app configuration
OAuth Setup - Complete authentication flow
Send First Message - Working code to send messages

Reference:

Chatbot Message Cards - Complete card component reference
Webhook Events - All webhook event types
API Reference - Endpoints, methods, parameters
Sample Applications - 10+ official sample apps
Integrated Index - see the section below in this file

Having issues?

Authentication errors → OAuth Troubleshooting
Webhook not receiving events → Webhook Setup Guide
Messages not sending → Common Issues
Start with quick checks → 5-Minute Runbook

OAuth endpoint sanity check:

Authorize URL: https://zoom.us/oauth/authorize
Token URL: https://zoom.us/oauth/token
If /oauth/token returns 404/HTML, use https://zoom.us/oauth/token.

Building Interactive Bots?

Button Actions - Handle button clicks
Form Submissions - Process form data
Slash Commands - Create custom commands
Quick Decision: Which API?
Use Case	API to Use
Send notifications from scripts/CI/CD	Team Chat API
Automate messages as a user	Team Chat API
Build an interactive chatbot	Chatbot API
Respond to slash commands	Chatbot API
Create messages with buttons/forms	Chatbot API
Handle user interactions	Chatbot API
Team Chat API (User-Level)
Messages appear as sent by authenticated user
Requires User OAuth (authorization_code flow)
Endpoint: POST https://api.zoom.us/v2/chat/users/me/messages
Scopes: chat_message:write, chat_channel:read
Chatbot API (Bot-Level)
Messages appear as sent by your bot
Requires Client Credentials grant
Endpoint: POST https://api.zoom.us/v2/im/chat/messages
Scopes: imchat:bot (auto-added)
Rich cards: buttons, forms, dropdowns, images
Prerequisites
System Requirements
Zoom account
Account owner, admin, or Zoom for developers role enabled
To enable: User Management → Roles → Role Settings → Advanced features → Enable Zoom for developers
Create Zoom App
Go to Zoom App Marketplace
Click Develop → Build App
Select General App (OAuth)

⚠️ Do NOT use Server-to-Server OAuth - S2S apps don't have the Chatbot/Team Chat feature. Only General App (OAuth) supports chatbots.

Required Credentials

From Zoom Marketplace → Your App:

Credential	Location	Used By
Client ID	App Credentials → Development	Both APIs
Client Secret	App Credentials → Development	Both APIs
Account ID	App Credentials → Development	Chatbot API
Bot JID	Features → Chatbot → Bot Credentials	Chatbot API
Secret Token	Features → Team Chat Subscriptions	Chatbot API

See: Environment Setup Guide for complete configuration steps.

Quick Start: Team Chat API

Send a message as a user:

// 1. Get access token via OAuth
const accessToken = await getOAuthToken(); // See examples/oauth-setup.md

// 2. Send message to channel
const response = await fetch('https://api.zoom.us/v2/chat/users/me/messages', {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${accessToken}`,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    message: 'Hello from CI/CD pipeline!',
    to_channel: 'CHANNEL_ID'
  })
});

const data = await response.json();
// { "id": "msg_abc123", "date_time": "2024-01-15T10:30:00Z" }


Complete example: Send Message Guide

Quick Start: Chatbot API

Build an interactive chatbot:

// 1. Get chatbot token (client_credentials)
async function getChatbotToken() {
  const credentials = Buffer.from(
    `${CLIENT_ID}:${CLIENT_SECRET}`
  ).toString('base64');
  
  const response = await fetch('https://zoom.us/oauth/token', {
    method: 'POST',
    headers: {
      'Authorization': `Basic ${credentials}`,
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: 'grant_type=client_credentials'
  });
  
  return (await response.json()).access_token;
}

// 2. Send chatbot message with buttons
const response = await fetch('https://api.zoom.us/v2/im/chat/messages', {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${accessToken}`,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    robot_jid: process.env.ZOOM_BOT_JID,
    to_jid: payload.toJid,           // From webhook
    account_id: payload.accountId,   // From webhook
    content: {
      head: {
        text: 'Build Notification',
        sub_head: { text: 'CI/CD Pipeline' }
      },
      body: [
        { type: 'message', text: 'Deployment successful!' },
        {
          type: 'fields',
          items: [
            { key: 'Branch', value: 'main' },
            { key: 'Commit', value: 'abc123' }
          ]
        },
        {
          type: 'actions',
          items: [
            { text: 'View Logs', value: 'view_logs', style: 'Primary' },
            { text: 'Dismiss', value: 'dismiss', style: 'Default' }
          ]
        }
      ]
    }
  })
});


Complete example: Chatbot Setup Guide

Key Features
Team Chat API
Feature	Description
Send Messages	Post messages to channels or direct messages
List Channels	Get user's channels with metadata
Create Channels	Create public/private channels programmatically
Threaded Replies	Reply to specific messages in threads
Edit/Delete	Modify or remove messages
Chatbot API
Feature	Description
Rich Message Cards	Headers, images, fields, buttons, forms
Slash Commands	Custom /commands trigger webhooks
Button Actions	Interactive buttons with webhook callbacks
Form Submissions	Collect user input with forms
Dropdown Selects	Channel, member, date/time pickers
LLM Integration	Easy integration with Claude, GPT, etc.
Webhook Events (Chatbot API)
Event	Trigger	Use Case
bot_notification	User messages bot or uses slash command	Process commands, integrate LLM
bot_installed	Bot added to account	Initialize bot state
interactive_message_actions	Button clicked	Handle button actions
chat_message.submit	Form submitted	Process form data
app_deauthorized	Bot removed	Cleanup

See: Webhook Events Reference

Message Card Components

Build rich interactive messages with these components:

Component	Description
header	Title and subtitle
message	Plain text
fields	Key-value pairs
actions	Buttons (Primary, Danger, Default styles)
section	Colored sidebar grouping
attachments	Images with links
divider	Horizontal line
form_field	Text input
dropdown	Select menu
date_picker	Date selection

See: Message Cards Reference for complete component catalog

Architecture Patterns
Chatbot Lifecycle
User types /command → Webhook receives bot_notification
                            ↓
                     payload.cmd = "user's input"
                            ↓
                     Process command
                            ↓
                     Send response via sendChatbotMessage()

LLM Integration Pattern
case 'bot_notification': {
  const { toJid, cmd, accountId } = payload;
  
  // 1. Call your LLM
  const llmResponse = await callClaude(cmd);
  
  // 2. Send response back
  await sendChatbotMessage(toJid, accountId, {
    body: [{ type: 'message', text: llmResponse }]
  });
}


See: LLM Integration Guide

Sample Applications
Sample	Description	Link
Chatbot Quickstart	Official tutorial (recommended start)	GitHub
Claude Chatbot	AI chatbot with Anthropic Claude	GitHub
Unsplash Chatbot	Image search with database	GitHub
ERP Chatbot	Oracle ERP with scheduled alerts	GitHub
Task Manager	Full CRUD app	GitHub

See: Sample Applications Guide for analysis of all 10 samples

Common Operations
Send Message to Channel
// Team Chat API
await fetch('https://api.zoom.us/v2/chat/users/me/messages', {
  method: 'POST',
  headers: { 'Authorization': `Bearer ${token}` },
  body: JSON.stringify({
    message: 'Hello!',
    to_channel: 'CHANNEL_ID'
  })
});

Handle Button Click
// Webhook handler
case 'interactive_message_actions': {
  const { actionItem, toJid, accountId } = payload;
  
  if (actionItem.value === 'approve') {
    await sendChatbotMessage(toJid, accountId, {
      body: [{ type: 'message', text: '✅ Approved!' }]
    });
  }
}

Verify Webhook Signature
function verifyWebhook(req) {
  const message = `v0:${req.headers['x-zm-request-timestamp']}:${JSON.stringify(req.body)}`;
  const hash = crypto.createHmac('sha256', process.env.ZOOM_VERIFICATION_TOKEN)
    .update(message)
    .digest('hex');
  return req.headers['x-zm-signature'] === `v0=${hash}`;
}

Deployment
ngrok for Local Development
# Install ngrok
npm install -g ngrok

# Expose local server
ngrok http 4000

# Use HTTPS URL as Bot Endpoint URL in Zoom Marketplace
# Example: https://abc123.ngrok.io/webhook

Production Deployment

See: Deployment Guide for:

Nginx reverse proxy setup
Base path configuration
OAuth redirect URI setup
Limitations
Limit	Value
Message length	4,096 characters
File size	512 MB
Members per channel	10,000
Channels per user	500
Security Best Practices
Verify webhook signatures - Always validate using x-zm-signature header
Sanitize messages - Limit to 4096 chars, remove control characters
Validate JIDs - Check format: user@domain or channel@domain
Environment variables - Never hardcode credentials
Use HTTPS - Required for production webhooks

See: Security Best Practices

Complete Documentation Library
Core Concepts (Start Here!)
API Selection Guide - Choose Team Chat API vs Chatbot API
Environment Setup - Complete credentials guide
Authentication Flows - OAuth vs Client Credentials
Webhook Architecture - How webhooks work
Message Card Structure - Card component hierarchy
Complete Examples
OAuth Setup - Full OAuth implementation
Send Message - Team Chat API message sending
Chatbot Setup - Complete chatbot with webhooks
Button Actions - Handle interactive buttons
Form Submissions - Process form data
Slash Commands - Create custom commands
LLM Integration - Claude/GPT integration
Scheduled Alerts - Cron + incoming webhooks
Channel Management - Create/manage channels
References
API Reference - All endpoints and methods
Webhook Events - Complete event reference
Message Cards - All card components
Sample Applications - Analysis of 10 official samples
Error Codes - Error handling guide
Troubleshooting
OAuth Issues - Authentication failures
Webhook Issues - Webhook debugging
Common Issues - Quick diagnostics
Resources
Official Docs: https://developers.zoom.us/docs/team-chat/
API Reference: https://developers.zoom.us/docs/api/rest/reference/chatbot/
Dev Forum: https://devforum.zoom.us/
App Marketplace: https://marketplace.zoom.us/

Need help? Start with Integrated Index section below for complete navigation.

Integrated Index

This section was migrated from SKILL.md.

Complete navigation guide for the Zoom Team Chat skill.

Quick Start Paths
Start here: Get Started
Fast troubleshooting first: 5-Minute Runbook
Path 1: Team Chat API (User-Level Messaging)

For sending messages as a user account.

API Selection Guide - Confirm Team Chat API is right
Environment Setup - Get credentials
OAuth Setup Example - Implement authentication
Send Message Example - Send your first message
Path 2: Chatbot API (Interactive Bots)

For building interactive chatbots with rich messages.

API Selection Guide - Confirm Chatbot API is right
Environment Setup - Get credentials (including Bot JID)
Webhook Architecture - Understand webhook events
Chatbot Setup Example - Build your first bot
Message Cards Reference - Create rich messages
Core Concepts

Essential understanding for both APIs.

Document	Description
API Selection Guide	Choose Team Chat API vs Chatbot API
Environment Setup	Complete credentials and app configuration
Authentication Flows	OAuth vs Client Credentials
Webhook Architecture	How webhooks work (Chatbot API)
Message Card Structure	Card component hierarchy
Deployment Guide	Production deployment strategies
Security Best Practices	Secure your integration
Complete Examples

Working code for common scenarios.

Authentication
Example	Description
OAuth Setup	User OAuth flow implementation
Token Management	Refresh tokens, expiration handling
Basic Operations
Example	Description
Send Message	Team Chat API message sending
Chatbot Setup	Complete chatbot with webhooks
List Channels	Get user's channels
Create Channel	Create public/private channels
Interactive Features (Chatbot API)
Example	Description
Button Actions	Handle button clicks
Form Submissions	Process form data
Slash Commands	Create custom commands
Dropdown Selects	Channel/member pickers
Advanced Integration
Example	Description
LLM Integration	Integrate Claude/GPT
Scheduled Alerts	Cron + incoming webhooks
Database Integration	Store conversation state
Multi-Step Workflows	Complex user interactions
References
API Documentation
Reference	Description
API Reference	Pointers and common endpoints
Webhook Events	Event types and handling checklist
Message Cards	All card components
Error Codes	Error handling guide
Sample Applications
Reference	Description
Sample Applications	Sample app index/notes
Field Guides
Reference	Description
JID Formats	Understanding JID identifiers
Scopes Reference	Common scopes
Rate Limits	Throttling guidance
Troubleshooting
Guide	Description
Common Issues	Quick diagnostics and solutions
OAuth Issues	Authentication failures
Webhook Issues	Webhook debugging
Message Issues	Message sending problems
Deployment Issues	Production problems
Architecture Patterns
Chatbot Lifecycle
User Action → Webhook → Process → Response

LLM Integration Pattern
User Input → Chatbot receives → Call LLM → Send response

Approval Workflow Pattern
Request → Send card with buttons → User clicks → Update status → Notify

Common Use Cases
Notifications
CI/CD build notifications
Server monitoring alerts
Scheduled reports
System health checks
Workflows
Approval requests
Task assignment
Status updates
Form submissions
Integrations
LLM-powered assistants
Database queries
External API integration
File/image sharing
Automation
Scheduled messages
Auto-responses
Data collection
Report generation
Resource Links
Official Documentation
Team Chat Docs - Official overview
Chatbot Docs - Chatbot guide
API Reference - REST API docs
App Marketplace - Create and manage apps
Sample Code
Chatbot Quickstart - Official tutorial
Claude Chatbot - AI integration
Unsplash Chatbot - Image search bot
ERP Chatbot - Enterprise integration
Task Manager - Full CRUD app
Tools
App Card Builder - Visual card designer
ngrok - Local webhook testing
Postman - API testing
Community
Developer Forum - Ask questions
GitHub Discussions - Community support
Developer Support - Official support
Documentation Status
✅ Complete
Main skill.md entry point
API Selection Guide
Environment Setup
Webhook Architecture
Chatbot Setup Example (complete working code)
Message Cards Reference
Common Issues Troubleshooting
📝 Pending (High Priority)
OAuth Setup Example
Send Message Example
Button Actions Example
LLM Integration Example
Webhook Events Reference
API Reference
Sample Applications Analysis
📋 Planned (Lower Priority)
Form Submissions Example
Channel Management Examples
Database Integration Example
Error Codes Reference
Rate Limits Guide
Deployment troubleshooting
Getting Started Checklist
For Team Chat API
 Read API Selection Guide
 Complete Environment Setup
 Obtain Client ID, Client Secret
 Add required scopes
 Implement OAuth flow
 Send first message
For Chatbot API
 Read API Selection Guide
 Complete Environment Setup
 Obtain Client ID, Client Secret, Bot JID, Secret Token, Account ID
 Enable Team Chat in Features
 Configure Bot Endpoint URL and Slash Command
 Set up ngrok for local testing
 Implement webhook handler
 Send first chatbot message
Version History
v1.0 (2026-02-09) - Initial comprehensive documentation
Core concepts (API selection, environment setup, webhooks)
Complete chatbot setup example
Message cards reference
Common issues troubleshooting
Support

Use this SKILL.md as the navigation hub for Team Chat API selection, setup, examples, and troubleshooting.

Environment Variables
See references/environment-variables.md for standardized .env keys and where to find each value.
Weekly Installs
291
Repository
anthropics/know…-plugins
GitHub Stars
11.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn