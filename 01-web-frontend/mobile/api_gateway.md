---
rating: ⭐⭐⭐
title: api-gateway
url: https://skills.sh/maton-ai/api-gateway-skill/api-gateway
---

# api-gateway

skills/maton-ai/api-gateway-skill/api-gateway
api-gateway
Installation
$ npx skills add https://github.com/maton-ai/api-gateway-skill --skill api-gateway
Summary

Unified API gateway for 100+ services with managed OAuth and native endpoint passthrough.

Supports 100+ integrations including Google Workspace, Microsoft 365, Slack, Notion, HubSpot, Salesforce, Stripe, and more with automatic OAuth token injection
Routes requests directly to native API endpoints via https://gateway.maton.ai/{app}/{native-api-path}, eliminating the need to learn custom abstractions
Manages OAuth connections through a separate control API with list, create, get, and delete operations; supports multiple connections per service with explicit connection selection
Requires MATON_API_KEY environment variable for authentication; each third-party service requires explicit user authorization through Maton's OAuth flow with scoped access control
SKILL.md
API Gateway

Managed OAuth proxy for third-party APIs, provided by Maton. The API gateway automatically injects the appropriate OAuth token for the target service.

Quick Start
# Native Slack API call
python <<'EOF'
import urllib.request, os, json
data = json.dumps({'channel': 'C0123456', 'text': 'Hello from gateway!'}).encode()
req = urllib.request.Request('https://api.maton.ai/slack/api/chat.postMessage', data=data, method='POST')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
req.add_header('Content-Type', 'application/json')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF

Base URL
https://api.maton.ai/{app}/{native-api-path}


Replace {app} with the service name and {native-api-path} with the actual API endpoint path.

IMPORTANT: The URL path MUST start with the connection's app name (eg. /google-mail/...). This prefix tells the gateway which app connection to use. For example, the native Gmail API path starts with gmail/v1/, so full paths look like /google-mail/gmail/v1/users/me/messages.

Authentication

All requests require the Maton API key in the Authorization header:

Authorization: Bearer $MATON_API_KEY


The API gateway automatically injects the appropriate OAuth token for the target service.

Environment Variable: You can set your API key as the MATON_API_KEY environment variable:

export MATON_API_KEY="YOUR_API_KEY"

Getting Your API Key
Sign in or create an account at maton.ai
Go to maton.ai/settings
Click the copy button on the right side of API Key section to copy it
Connection Management

Connection management uses a separate base URL: https://api.maton.ai

List Connections
python <<'EOF'
import urllib.request, os, json
req = urllib.request.Request('https://api.maton.ai/connections?app=slack&status=ACTIVE')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF


Query Parameters (optional):

app - Filter by service name (e.g., slack, hubspot, salesforce)
status - Filter by connection status (ACTIVE, PENDING, FAILED)

Response:

{
  "connections": [
    {
      "connection_id": "{connection_id}",
      "status": "ACTIVE",
      "creation_time": "2025-12-08T07:20:53.488460Z",
      "last_updated_time": "2026-01-31T20:03:32.593153Z",
      "url": "https://connect.maton.ai/?session_token=5e9...",
      "app": "slack",
      "method": "OAUTH2",
      "metadata": {}
    }
  ]
}

Create Connection
python <<'EOF'
import urllib.request, os, json
data = json.dumps({'app': 'slack'}).encode()
req = urllib.request.Request('https://api.maton.ai/connections', data=data, method='POST')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
req.add_header('Content-Type', 'application/json')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF


Request Body:

app (required) - Service name (e.g., slack, notion)
method (optional) - Connection method (API_KEY, BASIC, OAUTH1, OAUTH2, MCP)
Get Connection
python <<'EOF'
import urllib.request, os, json
req = urllib.request.Request('https://api.maton.ai/connections/{connection_id}')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF


Response:

{
  "connection": {
    "connection_id": "{connection_id}",
    "status": "ACTIVE",
    "creation_time": "2025-12-08T07:20:53.488460Z",
    "last_updated_time": "2026-01-31T20:03:32.593153Z",
    "url": "https://connect.maton.ai/?session_token=5e9...",
    "app": "slack",
    "metadata": {}
  }
}


Open the returned URL in a browser to complete OAuth.

Delete Connection
python <<'EOF'
import urllib.request, os, json
req = urllib.request.Request('https://api.maton.ai/connections/{connection_id}', method='DELETE')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF

Specifying Connection

If you have multiple connections for the same app, you can specify which connection to use by adding the Maton-Connection header with the connection ID:

python <<'EOF'
import urllib.request, os, json
data = json.dumps({'channel': 'C0123456', 'text': 'Hello!'}).encode()
req = urllib.request.Request('https://api.maton.ai/slack/api/chat.postMessage', data=data, method='POST')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
req.add_header('Content-Type', 'application/json')
req.add_header('Maton-Connection', '{connection_id}')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF


If you have multiple connections, always include this header to ensure requests go to the intended account.

Security & Permissions
Access is scoped to the specific third-party service connected through each Maton connection. Each connection grants access to one service's API only within the OAuth scopes the user authorized.
All operations that modify data require explicit user approval. Before executing any POST, PUT, PATCH, or DELETE call, confirm the target service, resource, and intended effect with the user. This includes sending messages, creating records, modifying content, deleting resources, and triggering workflows.
High-impact operations require extra caution. Actions such as bulk deletions, publishing content, sending emails/messages to external recipients, modifying billing or financial data, or changing permissions must be clearly described and confirmed before execution.
Always specify the connection. Use the Maton-Connection header to ensure requests go to the intended account, especially when the user has multiple connections for the same service.
Supported Services
Service	App Name	Base URL Proxied
ActiveCampaign	active-campaign	{account}.api-us1.com
Acuity Scheduling	acuity-scheduling	acuityscheduling.com
Airtable	airtable	api.airtable.com
Apify	apify	api.apify.com
Apollo	apollo	api.apollo.io
Asana	asana	app.asana.com
Attio	attio	api.attio.com
Basecamp	basecamp	3.basecampapi.com
Baserow	baserow	api.baserow.io
beehiiv	beehiiv	api.beehiiv.com
Box	box	api.box.com
Brevo	brevo	api.brevo.com
Brave Search	brave-search	api.search.brave.com
Buffer	buffer	api.buffer.com
Calendly	calendly	api.calendly.com
Cal.com	cal-com	api.cal.com
CallRail	callrail	api.callrail.com
Chargebee	chargebee	{subdomain}.chargebee.com
ClickFunnels	clickfunnels	{subdomain}.myclickfunnels.com
ClickSend	clicksend	rest.clicksend.com
ClickUp	clickup	api.clickup.com
Clio	clio	app.clio.com
Clockify	clockify	api.clockify.me
Coda	coda	coda.io
Confluence	confluence	api.atlassian.com
CompanyCam	companycam	api.companycam.com
Cognito Forms	cognito-forms	www.cognitoforms.com
Constant Contact	constant-contact	api.cc.email
Dropbox	dropbox	api.dropboxapi.com
Dropbox Business	dropbox-business	api.dropboxapi.com
ElevenLabs	elevenlabs	api.elevenlabs.io
Eventbrite	eventbrite	www.eventbriteapi.com
Exa	exa	api.exa.ai
Facebook Page	facebook-page	graph.facebook.com
fal.ai	fal-ai	queue.fal.run
Fathom	fathom	api.fathom.ai
Firecrawl	firecrawl	api.firecrawl.dev
Firebase	firebase	firebase.googleapis.com
Fireflies	fireflies	api.fireflies.ai
Front	front	api2.frontapp.com
GetResponse	getresponse	api.getresponse.com
Grafana	grafana	User's Grafana instance
GitHub	github	api.github.com
Gumroad	gumroad	api.gumroad.com
Granola MCP	granola	mcp.granola.ai
Google Ads	google-ads	googleads.googleapis.com
Google BigQuery	google-bigquery	bigquery.googleapis.com
Google Analytics Admin	google-analytics-admin	analyticsadmin.googleapis.com
Google Analytics Data	google-analytics-data	analyticsdata.googleapis.com
Google Calendar	google-calendar	www.googleapis.com
Google Classroom	google-classroom	classroom.googleapis.com
Google Contacts	google-contacts	people.googleapis.com
Google Docs	google-docs	docs.googleapis.com
Google Drive	google-drive	www.googleapis.com
Google Forms	google-forms	forms.googleapis.com
Gmail	google-mail	gmail.googleapis.com
Google Merchant	google-merchant	merchantapi.googleapis.com
Google Meet	google-meet	meet.googleapis.com
Google Play	google-play	androidpublisher.googleapis.com
Google Search Console	google-search-console	www.googleapis.com
Google Sheets	google-sheets	sheets.googleapis.com
Google Slides	google-slides	slides.googleapis.com
Google Tasks	google-tasks	tasks.googleapis.com
Google Workspace Admin	google-workspace-admin	admin.googleapis.com
GoHighLevel (PIT)	highlevel-pit	services.leadconnectorhq.com
HubSpot	hubspot	api.hubapi.com
Instantly	instantly	api.instantly.ai
Jira	jira	api.atlassian.com
Jobber	jobber	api.getjobber.com
JotForm	jotform	api.jotform.com
Kaggle	kaggle	api.kaggle.com
Keap	keap	api.infusionsoft.com
Kibana	kibana	User's Kibana instance
Kit	kit	api.kit.com
Klaviyo	klaviyo	a.klaviyo.com
Lemlist	lemlist	api.lemlist.com
Linear	linear	api.linear.app
LinkedIn	linkedin	api.linkedin.com
Mailchimp	mailchimp	{dc}.api.mailchimp.com
MailerLite	mailerlite	connect.mailerlite.com
Mailgun	mailgun	api.mailgun.net
Make	make	{zone}.make.com
ManyChat	manychat	api.manychat.com
Manus	manus	api.manus.ai
Memelord	memelord	www.memelord.com
Meta Ads	meta-ads	graph.facebook.com
Microsoft Excel	microsoft-excel	graph.microsoft.com
Microsoft Teams	microsoft-teams	graph.microsoft.com
Microsoft To Do	microsoft-to-do	graph.microsoft.com
Monday.com	monday	api.monday.com
Motion	motion	api.usemotion.com
Netlify	netlify	api.netlify.com
Notion	notion	api.notion.com
Notion MCP	notion	mcp.notion.com
OneNote	one-note	graph.microsoft.com
OneDrive	one-drive	graph.microsoft.com
Outlook	outlook	graph.microsoft.com
PDF.co	pdf-co	api.pdf.co
Pipedrive	pipedrive	api.pipedrive.com
Podio	podio	api.podio.com
PostHog	posthog	{subdomain}.posthog.com
QuickBooks	quickbooks	quickbooks.api.intuit.com
Quo	quo	api.openphone.com
Reducto	reducto	platform.reducto.ai
Resend	resend	api.resend.com
Salesforce	salesforce	{instance}.salesforce.com
Sentry	sentry	{subdomain}.sentry.io
SharePoint	sharepoint	graph.microsoft.com
SignNow	signnow	api.signnow.com
Slack	slack	slack.com
Snapchat	snapchat	adsapi.snapchat.com
Square	squareup	connect.squareup.com
Squarespace	squarespace	api.squarespace.com
Stripe	stripe	api.stripe.com
Sunsama MCP	sunsama	MCP server
Supabase	supabase	{project_ref}.supabase.co
Systeme.io	systeme	api.systeme.io
Tally	tally	api.tally.so
Tavily	tavily	api.tavily.com
Telegram	telegram	api.telegram.org
TickTick	ticktick	api.ticktick.com
Todoist	todoist	api.todoist.com
Toggl Track	toggl-track	api.track.toggl.com
Trello	trello	api.trello.com
Twilio	twilio	api.twilio.com
Twenty CRM	twenty	api.twenty.com
Typeform	typeform	api.typeform.com
Unbounce	unbounce	api.unbounce.com
Vercel	vercel	api.vercel.com
Vimeo	vimeo	api.vimeo.com
WATI	wati	{tenant}.wati.io
WhatsApp Business	whatsapp-business	graph.facebook.com
WooCommerce	woocommerce	{store-url}/wp-json/wc/v3
WordPress.com	wordpress	public-api.wordpress.com
Wrike	wrike	www.wrike.com
Xero	xero	api.xero.com
YouTube	youtube	www.googleapis.com
Zoom	zoom	api.zoom.us
Zoom Admin	zoom-admin	api.zoom.us
Zoho Bigin	zoho-bigin	www.zohoapis.com
Zoho Bookings	zoho-bookings	www.zohoapis.com
Zoho Books	zoho-books	www.zohoapis.com
Zoho Calendar	zoho-calendar	calendar.zoho.com
Zoho CRM	zoho-crm	www.zohoapis.com
Zoho Inventory	zoho-inventory	www.zohoapis.com
Zoho Mail	zoho-mail	mail.zoho.com
Zoho People	zoho-people	people.zoho.com
Zoho Projects	zoho-projects	projectsapi.zoho.com
Zoho Recruit	zoho-recruit	recruit.zoho.com

See references/ for detailed routing guides per provider:

ActiveCampaign - Contacts, deals, tags, lists, automations, campaigns
Acuity Scheduling - Appointments, calendars, clients, availability
Airtable - Records, bases, tables
Apify - Actors, runs, datasets, key-value stores, request queues, schedules
Apollo - People search, enrichment, contacts
Asana - Tasks, projects, workspaces, webhooks
Attio - People, companies, records, tasks
Basecamp - Projects, to-dos, messages, schedules, documents
Baserow - Database rows, fields, tables, batch operations
beehiiv - Publications, subscriptions, posts, custom fields
Box - Files, folders, collaborations, shared links
Brevo - Contacts, email campaigns, transactional emails, templates
Brave Search - Web search, image search, news search, video search
Buffer - Social media posts, channels, organizations, scheduling
Calendly - Event types, scheduled events, availability, webhooks
Cal.com - Event types, bookings, schedules, availability slots, webhooks
CallRail - Calls, trackers, companies, tags, analytics
Chargebee - Subscriptions, customers, invoices
ClickFunnels - Contacts, products, orders, courses, webhooks
ClickSend - SMS, MMS, voice messages, contacts, lists
ClickUp - Tasks, lists, folders, spaces, webhooks
Clio - Matters, contacts, activities, tasks, calendar entries, documents
Clockify - Time tracking, projects, clients, tasks, workspaces
Coda - Docs, pages, tables, rows, formulas, controls
Confluence - Pages, spaces, blogposts, comments, attachments
CompanyCam - Projects, photos, users, tags, groups, documents
Cognito Forms - Forms, entries, documents, files
Constant Contact - Contacts, email campaigns, lists, tags, custom fields, segments, bulk activities, reporting
Dropbox - Files, folders, search, metadata, revisions, tags
Dropbox Business - Team members, groups, team folders, devices, audit logs
ElevenLabs - Text-to-speech, voice cloning, sound effects, audio processing
Eventbrite - Events, venues, tickets, orders, attendees
Exa - Neural web search, content extraction, similar pages, AI answers, research tasks
fal.ai - AI model inference (image generation, video, audio, upscaling)
Facebook Page - Pages, posts, comments, insights, photos, videos, product catalogs
Fathom - Meeting recordings, transcripts, summaries, webhooks
Firecrawl - Web scraping, crawling, site mapping, web search
Firebase - Projects, web apps, Android apps, iOS apps, configurations
Fireflies - Meeting transcripts, summaries, AskFred AI, channels
Front - Conversations, messages, contacts, tags, inboxes, teammates
GetResponse - Campaigns, contacts, newsletters, autoresponders, tags, segments
Grafana - Dashboards, data sources, folders, annotations, alerts, teams
GitHub - Repositories, issues, pull requests, commits
Gumroad - Products, sales, subscribers, licenses, webhooks
Granola MCP - MCP-based interface for meeting notes, transcripts, queries
Google Ads - Campaigns, ad groups, GAQL queries
Google Analytics Admin - Reports, dimensions, metrics
Google Analytics Data - Reports, dimensions, metrics
Google BigQuery - Datasets, tables, jobs, SQL queries
Google Calendar - Events, calendars, free/busy
Google Classroom - Courses, coursework, students, teachers, announcements
Google Contacts - Contacts, contact groups, people search
Google Docs - Document creation, batch updates
Google Drive - Files, folders, permissions
Google Forms - Forms, questions, responses
Gmail - Messages, threads, labels
Google Meet - Spaces, conference records, participants
Google Merchant - Products, inventories, promotions, reports
Google Play - In-app products, subscriptions, reviews
Google Search Console - Search analytics, sitemaps
Google Sheets - Values, ranges, formatting
Google Slides - Presentations, slides, formatting
Google Tasks - Task lists, tasks, subtasks
Google Workspace Admin - Users, groups, org units, domains, roles
GoHighLevel PIT - Contacts, opportunities, calendars, conversations, locations, payments, custom fields
HubSpot - Contacts, companies, deals
Instantly - Campaigns, leads, accounts, email outreach
Jira - Issues, projects, JQL queries
Jobber - Clients, jobs, invoices, quotes (GraphQL)
JotForm - Forms, submissions, webhooks
Kaggle - Datasets, models, competitions, kernels
Keap - Contacts, companies, tags, tasks, opportunities, campaigns
Kibana - Saved objects, dashboards, data views, spaces, alerts, fleet
Kit - Subscribers, tags, forms, sequences, broadcasts
Klaviyo - Profiles, lists, campaigns, flows, events
Lemlist - Campaigns, leads, activities, schedules, unsubscribes
Linear - Issues, projects, teams, cycles (GraphQL)
LinkedIn - Profile, posts, shares, media uploads
Mailchimp - Audiences, campaigns, templates, automations
MailerLite - Subscribers, groups, campaigns, automations, forms
Mailgun - Email sending, domains, routes, templates, mailing lists, suppressions
Make - Scenarios, organizations, teams, connections, data stores, hooks
ManyChat - Subscribers, tags, flows, messaging
Manus - AI agent tasks, projects, files, webhooks
Memelord - AI meme generation, video memes, template editing
Meta Ads - Ad accounts, campaigns, ad sets, ads, creatives, insights
Microsoft Excel - Workbooks, worksheets, ranges, tables, charts
Microsoft Teams - Teams, channels, messages, members, chats
Microsoft To Do - Task lists, tasks, checklist items, linked resources
Monday.com - Boards, items, columns, groups (GraphQL)
Motion - Tasks, projects, workspaces, schedules
Netlify - Sites, deploys, builds, DNS, environment variables
Notion - Pages, databases, blocks
Notion MCP - MCP-based interface for pages, databases, comments, teams, users
OneNote - Notebooks, sections, section groups, pages via Microsoft Graph
OneDrive - Files, folders, drives, sharing
Outlook - Mail, calendar, contacts
PDF.co - PDF conversion, merge, split, edit, text extraction, barcodes
Pipedrive - Deals, persons, organizations, activities
Podio - Organizations, workspaces, apps, items, tasks, comments
PostHog - Product analytics, feature flags, session recordings, experiments, HogQL queries
QuickBooks - Customers, invoices, reports
Quo - Calls, messages, contacts, conversations, webhooks
Reducto - Document parsing, extraction, splitting, editing
Resend - Transactional emails, domains, audiences, contacts, broadcasts, webhooks
Salesforce - SOQL, sObjects, CRUD
SignNow - Documents, templates, invites, e-signatures
SendGrid - Email sending, contacts, templates, suppressions, statistics
Sentry - Issues, events, projects, teams, releases
SharePoint - Sites, lists, document libraries, files, folders, versions
Slack - Messages, channels, users
Snapchat - Ad accounts, campaigns, ad squads, ads, creatives, audiences
Square - Payments, customers, orders, catalog, inventory, invoices
Squarespace - Products, inventory, orders, profiles, transactions
Stripe - Customers, subscriptions, payments
Sunsama MCP - MCP-based interface for tasks, calendar, backlog, objectives, time tracking
Supabase - Database tables, auth users, storage buckets
Systeme.io - Contacts, tags, courses, communities, webhooks
Tally - Forms, submissions, workspaces, webhooks
Tavily - AI web search, content extraction, crawling, research tasks
Telegram - Messages, chats, bots, updates, polls
TickTick - Tasks, projects, task lists
Todoist - Tasks, projects, sections, labels, comments
Toggl Track - Time entries, projects, clients, tags, workspaces
Trello - Boards, lists, cards, checklists
Twilio - SMS, voice calls, phone numbers, messaging
Twenty CRM - Companies, people, opportunities, notes, tasks
Typeform - Forms, responses, insights
Unbounce - Landing pages, leads, accounts, sub-accounts, domains
Vercel - Projects, deployments, domains, environment variables
Vimeo - Videos, folders, albums, comments, likes
WATI - WhatsApp messages, contacts, templates, interactive messages
WhatsApp Business - Messages, templates, media
WooCommerce - Products, orders, customers, coupons
WordPress.com - Posts, pages, sites, users, settings
Wrike - Tasks, folders, projects, spaces, comments, timelogs, workflows
Xero - Contacts, invoices, reports
YouTube - Videos, playlists, channels, subscriptions
Zoom - Meetings, recordings, webinars, users
Zoom Admin - Users, meetings, webinars, recordings, account settings (admin scopes)
Zoho Bigin - Contacts, companies, pipelines, products
Zoho Bookings - Appointments, services, staff, workspaces
Zoho Books - Invoices, contacts, bills, expenses
Zoho Calendar - Calendars, events, attendees, reminders
Zoho CRM - Leads, contacts, accounts, deals, search
Zoho Inventory - Items, sales orders, invoices, purchase orders, bills
Zoho Mail - Messages, folders, labels, attachments
Zoho People - Employees, departments, designations, attendance, leave
Zoho Projects - Projects, tasks, milestones, tasklists, comments
Zoho Recruit - Candidates, job openings, interviews, applications
Examples
Slack - Post Message (Native API)
# Native Slack API: POST https://slack.com/api/chat.postMessage
python <<'EOF'
import urllib.request, os, json
data = json.dumps({'channel': 'C0123456', 'text': 'Hello!'}).encode()
req = urllib.request.Request('https://api.maton.ai/slack/api/chat.postMessage', data=data, method='POST')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
req.add_header('Content-Type', 'application/json; charset=utf-8')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF

HubSpot - Create Contact (Native API)
# Native HubSpot API: POST https://api.hubapi.com/crm/v3/objects/contacts
python <<'EOF'
import urllib.request, os, json
data = json.dumps({'properties': {'email': 'john@example.com', 'firstname': 'John', 'lastname': 'Doe'}}).encode()
req = urllib.request.Request('https://api.maton.ai/hubspot/crm/v3/objects/contacts', data=data, method='POST')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
req.add_header('Content-Type', 'application/json')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF

Google Sheets - Get Spreadsheet Values (Native API)
# Native Sheets API: GET https://sheets.googleapis.com/v4/spreadsheets/{id}/values/{range}
python <<'EOF'
import urllib.request, os, json
req = urllib.request.Request('https://api.maton.ai/google-sheets/v4/spreadsheets/{spreadsheet_id}/values/Sheet1!A1:B2')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF

Salesforce - SOQL Query (Native API)
# Native Salesforce API: GET https://{instance}.salesforce.com/services/data/v64.0/query?q=...
python <<'EOF'
import urllib.request, os, json
req = urllib.request.Request('https://api.maton.ai/salesforce/services/data/v64.0/query?q=SELECT+Id,Name+FROM+Contact+LIMIT+10')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF

Airtable - List Tables (Native API)
# Native Airtable API: GET https://api.airtable.com/v0/meta/bases/{id}/tables
python <<'EOF'
import urllib.request, os, json
req = urllib.request.Request('https://api.maton.ai/airtable/v0/meta/bases/{base_id}/tables')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF

Notion - Query Database (Native API)
# Native Notion API: POST https://api.notion.com/v1/data_sources/{id}/query
python <<'EOF'
import urllib.request, os, json
data = json.dumps({}).encode()
req = urllib.request.Request('https://api.maton.ai/notion/v1/data_sources/{data_source_id}/query', data=data, method='POST')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
req.add_header('Content-Type', 'application/json')
req.add_header('Notion-Version', '2025-09-03')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF

Stripe - List Customers (Native API)
# Native Stripe API: GET https://api.stripe.com/v1/customers
python <<'EOF'
import urllib.request, os, json
req = urllib.request.Request('https://api.maton.ai/stripe/v1/customers?limit=10')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF

Code Examples
JavaScript (Node.js)
const response = await fetch('https://api.maton.ai/slack/api/chat.postMessage', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${process.env.MATON_API_KEY}`
  },
  body: JSON.stringify({ channel: 'C0123456', text: 'Hello!' })
});

Python
import os
import requests

response = requests.post(
    'https://api.maton.ai/slack/api/chat.postMessage',
    headers={'Authorization': f'Bearer {os.environ["MATON_API_KEY"]}'},
    json={'channel': 'C0123456', 'text': 'Hello!'}
)

Error Handling
Status	Meaning
400	Missing connection for the requested app
401	Invalid or missing Maton API key
429	Rate limited (10 requests/second per account)
500	Internal Server Error
4xx/5xx	Passthrough error from the target API

Errors from the target API are passed through with their original status codes and response bodies.

Troubleshooting: API Key Issues
Check that the MATON_API_KEY environment variable is set:
echo $MATON_API_KEY

Verify the API key is valid by listing connections:
python <<'EOF'
import urllib.request, os, json
req = urllib.request.Request('https://api.maton.ai/connections')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF

Troubleshooting: Invalid App Name
Verify your URL path starts with the correct app name. The path must begin with /google-mail/. For example:
Correct: https://api.maton.ai/google-mail/gmail/v1/users/me/messages
Incorrect: https://api.maton.ai/gmail/v1/users/me/messages
Ensure you have an active connection for the app. List your connections to verify:
python <<'EOF'
import urllib.request, os, json
req = urllib.request.Request('https://api.maton.ai/connections?app=google-mail&status=ACTIVE')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF

Troubleshooting: Server Error

A 500 error may indicate an expired OAuth token. Try creating a new connection via the Connection Management section above and completing OAuth authorization. If the new connection is "ACTIVE", delete the old connection to ensure Maton uses the new one.

Rate Limits
10 requests per second per account
Target API rate limits also apply
Notes
When using curl with URLs containing brackets (fields[], sort[], records[]), use the -g flag to disable glob parsing
When piping curl output to jq, environment variables may not expand correctly in some shells, which can cause "Invalid API key" errors
Media upload URLs (LinkedIn, etc.): Some APIs return pre-signed upload URLs that point to a different host than Maton proxies (e.g., LinkedIn returns www.linkedin.com upload URLs, but Maton proxies api.linkedin.com). These upload URLs are pre-signed and do NOT require an Authorization header — upload the binary directly to the returned URL without going through the gateway. You MUST use Python urllib for these uploads because the URLs contain encoded characters (e.g., %253D) that get corrupted when passed through shell variables or curl. Always parse the JSON response with json.load() and use the URL directly in Python.
Tips

Use native API docs: Refer to each service's official API documentation for endpoint paths and parameters.

Headers are forwarded: Custom headers (except Host and Authorization) are forwarded to the target API.

Query params work: URL query parameters are passed through to the target API.

All HTTP methods supported: GET, POST, PUT, PATCH, DELETE are all supported.

QuickBooks special case: Use :realmId in the path and it will be replaced with the connected realm ID.

Optional
Github
API Reference
Maton Community
Maton Support
Weekly Installs
972
Repository
maton-ai/api-ga…ay-skill
GitHub Stars
22
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn