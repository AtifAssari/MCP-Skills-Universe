---
title: recipe-create-feedback-form
url: https://skills.sh/googleworkspace/cli/recipe-create-feedback-form
---

# recipe-create-feedback-form

skills/googleworkspace/cli/recipe-create-feedback-form
recipe-create-feedback-form
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-create-feedback-form
Summary

Create a Google Form for feedback collection and distribute it via email.

Requires gws-forms and gws-gmail skills as dependencies
Two-step workflow: create a form with custom title and document name, then email the responder URI to recipients
Designed for feedback collection scenarios such as post-event surveys or attendee input gathering
SKILL.md
Create and Share a Google Form

PREREQUISITE: Load the following skills to execute this recipe: gws-forms, gws-gmail

Create a Google Form for feedback and share it via Gmail.

Steps
Create form: gws forms forms create --json '{"info": {"title": "Event Feedback", "documentTitle": "Event Feedback Form"}}'
Get the form URL from the response (responderUri field)
Email the form: gws gmail +send --to attendees@company.com --subject 'Please share your feedback' --body 'Fill out the form: FORM_URL'
Weekly Installs
11.0K
Repository
googleworkspace/cli
GitHub Stars
25.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass