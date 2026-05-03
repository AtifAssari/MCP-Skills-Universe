---
rating: ⭐⭐
title: build-zoom-meeting-app
url: https://skills.sh/anthropics/knowledge-work-plugins/build-zoom-meeting-app
---

# build-zoom-meeting-app

skills/anthropics/knowledge-work-plugins/build-zoom-meeting-app
build-zoom-meeting-app
Installation
$ npx skills add https://github.com/anthropics/knowledge-work-plugins --skill build-zoom-meeting-app
SKILL.md
/build-zoom-meeting-app

Use this skill for embedded meeting experiences and meeting lifecycle implementation.

Covers
Meeting SDK selection and platform routing
Join/auth implementation planning
Meeting creation plus join flow design
Web vs native platform considerations
Meeting SDK vs Video SDK boundary decisions
Workflow
Confirm whether the user wants a Zoom meeting or a custom video session.
Route to Meeting SDK if the user needs actual Zoom meetings.
Pull in the relevant platform references.
Add REST API only for meeting creation, resource management, or reporting.
Add webhooks or RTMS only when the use case explicitly needs them.
Primary References
meeting-sdk
rest-api
webhooks
rtms
video-sdk
Common Mistakes
Using Video SDK for normal Zoom meeting embeds
Mixing resource-management APIs into the core join flow without reason
Skipping platform-specific SDK constraints until too late
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
SnykPass