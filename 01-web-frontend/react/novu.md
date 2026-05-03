---
title: novu
url: https://skills.sh/novuhq/skills/novu
---

# novu

skills/novuhq/skills/novu
novu
Installation
$ npx skills add https://github.com/novuhq/skills --skill novu
SKILL.md
Novu

Novu is a notification infrastructure platform for sending notifications across email, SMS, push, chat, and in-app channels. Workflows can be created via the Novu dashboard UI or in code using @novu/framework.

Sub-Skills
Skill	Use When...
trigger-notification	Sending notifications, triggering workflows, single or bulk sends
manage-subscribers	Creating, updating, listing, or deleting subscribers; managing topics and groups
inbox-integration	Adding the in-app notification inbox, bell icon, or notification feed to a web app and react native app
manage-preferences	Setting up subscriber notification preferences, workflow defaults, or the Preferences UI
Quick Routing
"Send a welcome email" → trigger-notification/
"Create subscriber groups" → manage-subscribers/
"Add a bell icon to my app" → inbox-integration/
"Let users opt out of emails" → manage-preferences/
Common Combinations
Full notification system: trigger-notification/ + manage-subscribers/
In-app notifications: trigger-notification/ + inbox-integration/
Complete stack: all four skills
SDK Overview
Package	Side	Purpose
@novu/api	Server	Trigger notifications, manage subscribers/topics/workflows via REST
@novu/react	Client	React Inbox component, Notifications, Preferences, Bell
@novu/nextjs	Client	Next.js-optimized Inbox integration
@novu/react-native	Client	React native hooks based Inbox integration
@novu/js	Client	Vanilla JS client for non-React apps

Important distinctions:

@novu/api is for triggering workflow to send notifications and managing resources (subscribers, topics, contexts)
@novu/react / @novu/js are for client-side Inbox integrations and preferences
Common Setup
npm i @novu/api

import { Novu } from "@novu/api";

const novu = new Novu({
 secretKey: process.env.NOVU_SECRET_KEY,
});

await novu.trigger({
  workflowId: "workflowId",
  to: "subscriberId",
  payload: {
    "comment_id": "string",
    "post": {
      "text": "string",
    },
  },
})

Resources
Novu Documentation
Novu Dashboard
GitHub
Weekly Installs
35
Repository
novuhq/skills
First Seen
Mar 13, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn