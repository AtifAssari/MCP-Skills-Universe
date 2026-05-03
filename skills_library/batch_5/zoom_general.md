---
title: zoom-general
url: https://skills.sh/anthropics/knowledge-work-plugins/zoom-general
---

# zoom-general

skills/anthropics/knowledge-work-plugins/zoom-general
zoom-general
Installation
$ npx skills add https://github.com/anthropics/knowledge-work-plugins --skill zoom-general
SKILL.md
Zoom General (Cross-Product Skills)

Background reference for cross-product Zoom questions. Prefer the workflow skills first, then use this file for shared platform guidance and routing detail.

How zoom-general Routes a Complex Developer Query

Use zoom-general as the classifier and chaining layer:

detect product signals in the query
pick one primary skill
attach secondary skills for auth, events, or deployment edges
ask one short clarifier only when two routes match with similar confidence

Minimal implementation:

type SkillId =
  | 'zoom-general'
  | 'zoom-rest-api'
  | 'zoom-webhooks'
  | 'zoom-oauth'
  | 'zoom-meeting-sdk-web-component-view'
  | 'zoom-video-sdk'
  | 'zoom-mcp';

const hasAny = (q: string, words: string[]) => words.some((w) => q.includes(w));

function detectSignals(rawQuery: string) {
  const q = rawQuery.toLowerCase();
  return {
    meetingCustomUi: hasAny(q, ['zoom meeting', 'custom ui', 'component view', 'embed meeting']),
    customVideo: hasAny(q, ['video sdk', 'custom video session', 'peer-video-state-change']),
    restApi: hasAny(q, ['rest api', '/v2/', 'create meeting', 'list users', 's2s oauth']),
    webhooks: hasAny(q, ['webhook', 'x-zm-signature', 'event subscription', 'crc']),
    oauth: hasAny(q, ['oauth', 'pkce', 'token refresh', 'account_credentials']),
    mcp: hasAny(q, ['zoom mcp', 'agentic retrieval', 'tools/list', 'semantic meeting search']),
  };
}

function pickPrimarySkill(s: ReturnType<typeof detectSignals>): SkillId {
  if (s.meetingCustomUi) return 'zoom-meeting-sdk-web-component-view';
  if (s.mcp) return 'zoom-mcp';
  if (s.restApi) return 'zoom-rest-api';
  if (s.customVideo) return 'zoom-video-sdk';
  return 'zoom-general';
}

function buildChain(primary: SkillId, s: ReturnType<typeof detectSignals>): SkillId[] {
  const chain = [primary];
  if (s.oauth && !chain.includes('zoom-oauth')) chain.push('zoom-oauth');
  if (s.webhooks && !chain.includes('zoom-webhooks')) chain.push('zoom-webhooks');
  return chain;
}


Example:

Create a meeting, configure webhooks, and handle OAuth token refresh -> zoom-rest-api -> zoom-oauth -> zoom-webhooks
Build a custom video UI for a Zoom meeting on web -> zoom-meeting-sdk-web-component-view

For the full TypeScript implementation and handoff contract, use references/routing-implementation.md.

Choose Your Path
I want to...	Use this skill
Build a custom web UI around a real Zoom meeting	zoom-meeting-sdk-web-component-view
Build deterministic automation/configuration/reporting with explicit request control	zoom-rest-api
Receive event notifications (HTTP push)	zoom-webhooks
Receive event notifications (WebSocket, low-latency)	zoom-websockets
Embed Zoom meetings in my app	zoom-meeting-sdk
Build custom video experiences (Web, React Native, Flutter, Android, iOS, macOS, Unity, Linux)	zoom-video-sdk
Build an app that runs inside Zoom client	zoom-apps-sdk
Transcribe uploaded or stored media with AI Services Scribe	scribe
Access live audio/video/transcripts from meetings	zoom-rtms
Enable collaborative browsing for support	zoom-cobrowse-sdk
Build Contact Center apps and channel integrations	contact-center
Build Virtual Agent web/mobile chatbot experiences	virtual-agent
Build Zoom Phone integrations (Smart Embed, Phone API, webhooks, URI flows)	phone
Build Team Chat apps and integrations	zoom-team-chat
Build server-side integrations with Rivet (auth + webhooks + APIs)	rivet-sdk
Run browser/device/network preflight diagnostics before join	probe-sdk
Add pre-built UI components for Video SDK	zoom-ui-toolkit
Implement OAuth authentication (all grant types)	zoom-oauth
Build AI-driven tool workflows (AI Companion/agents) over Zoom data	zoom-mcp
Build AI-driven Whiteboard workflows over Zoom Whiteboard MCP	zoom-mcp/whiteboard
Build enterprise AI systems with stable API core + AI tool layer	zoom-rest-api + zoom-mcp
Planning Checkpoint: Rivet SDK (Optional)

When a user starts planning a server-side integration that combines auth + webhooks + API calls, ask this first:

Rivet SDK is a Node.js framework that bundles Zoom auth handling, webhook receivers, and typed API wrappers.
Do you want to use Rivet SDK for faster scaffolding, or do you prefer a direct OAuth + REST implementation without Rivet?

Routing after answer:

If user chooses Rivet: chain rivet-sdk + oauth + rest-api.
If user declines Rivet: chain oauth + rest-api (+ webhooks or product skill as needed).
SDK vs REST Routing Matrix (Hard Stop)
User intent	Correct path	Do not route to
Embed Zoom meeting in app UI	zoom-meeting-sdk	REST-only join_url flow
Build custom web UI for a real Zoom meeting	zoom-meeting-sdk-web-component-view	zoom-video-sdk
Build custom video UI/session app	zoom-video-sdk	Meeting SDK or REST meeting links
Get browser join links / manage meeting resources	zoom-rest-api	Meeting SDK join implementation

Routing guardrails:

If user asks for SDK embed/join behavior, stay in SDK path.
If the prompt says meeting plus custom UI/video/layout/embed, prefer zoom-meeting-sdk-web-component-view.
Only use zoom-video-sdk when the user is building a custom session product rather than a Zoom meeting.
Only use REST path for resource management, reporting, or link distribution unless user explicitly requests a mixed architecture.
For executable classification/chaining logic and error handling, see references/routing-implementation.md.
API vs MCP Routing Matrix (Hard Stop)
User intent	Correct path	Why
Deterministic backend automation, account/user configuration, reporting, scheduled jobs	zoom-rest-api	Explicit request/response control and repeatable behavior
AI agent chooses tools dynamically, cross-platform AI tool interoperability	zoom-mcp	MCP is optimized for dynamic tool discovery and agentic workflows
Enterprise AI architecture (stable core + adaptive AI layer)	zoom-rest-api + zoom-mcp	APIs run core system actions; MCP exposes curated AI tools/context

Routing guardrails:

Do not replace deterministic backend APIs with MCP-only routing.
Do not force raw REST-first routing when the task is AI-agent tool orchestration.
Prefer hybrid routing when the user needs both stable automation and AI-driven interactions.
MCP remote server works over Streamable HTTP/SSE; use this path when the target client/agent supports MCP transports (for example Claude or VS Code).
Do not design per-tenant custom MCP endpoint provisioning; Zoom MCP endpoints are shared at instance/cluster level.
Source: https://developers.zoom.us/docs/mcp/library/resources/apis-vs-mcp/
Ambiguity Resolution (Ask Before Routing)

When a prompt matches both API and MCP paths with similar confidence, ask one short clarifier before execution:

Do you want deterministic REST API automation, AI-agent MCP tooling, or a hybrid of both?

Then route as:

REST answer → zoom-rest-api
MCP answer → zoom-mcp
Hybrid answer → zoom-rest-api + zoom-mcp
MCP Availability and Topology Notes
Zoom-hosted MCP access is evolving; docs indicate a model where Zoom exposes product-scoped MCP servers (for example Meetings, Team Chat, Whiteboard).
Use zoom-mcp as the parent MCP entry point.
Route Whiteboard-specific MCP requests to zoom-mcp/whiteboard.
When a request is product-specific and MCP coverage exists, route to that MCP product surface first; otherwise use REST/SDK skills for deterministic implementation.
Webhooks vs WebSockets

Both receive event notifications, but differ in approach:

Aspect	webhooks	zoom-websockets
Connection	HTTP POST to your endpoint	Persistent WebSocket
Latency	Higher	Lower
Security	Requires public endpoint	No exposed endpoint
Setup	Simpler	More complex
Best for	Most use cases	Real-time, security-sensitive
Common Use Cases
Use Case	Description	Skills Needed
Meeting + Webhooks + OAuth Refresh	Create a meeting, process real-time updates, and refresh OAuth tokens safely in one design	zoom-rest-api + zoom-oauth + zoom-webhooks
Scribe Transcription Pipeline	Transcribe uploaded files or S3 archives with AI Services Scribe using fast mode or batch jobs	scribe + optional zoom-rest-api + optional zoom-webhooks
APIs vs MCP Routing	Decide whether to route to deterministic Zoom APIs, AI-driven MCP, or a hybrid design	zoom-rest-api and/or zoom-mcp
Custom Meeting UI (Web)	Build a custom video UI for a real Zoom meeting in a web app using Meeting SDK Component View	zoom-meeting-sdk-web-component-view + zoom-oauth
Meeting Automation	Schedule, update, delete meetings programmatically	zoom-rest-api
Meeting Bots	Build bots that join meetings for AI/transcription/recording	meeting-sdk/linux + zoom-rest-api + optional zoom-webhooks
High-Volume Meeting Platform	Design distributed meeting creation and event processing with retries, queues, and reconciliation	zoom-rest-api + zoom-webhooks + zoom-oauth
Recording & Transcription	Download recordings, get transcripts	zoom-webhooks + zoom-rest-api
Recording Download Pipeline	Auto-download recordings to your own storage (S3, GCS, etc.)	zoom-webhooks + zoom-rest-api
Real-Time Media Streams	Access live audio, video, transcripts via WebSocket	zoom-rtms + zoom-webhooks
In-Meeting Apps	Build apps that run inside Zoom meetings	zoom-apps-sdk + zoom-oauth
React Native Meeting Embed	Embed meetings into iOS/Android React Native apps	zoom-meeting-sdk-react-native + zoom-oauth
Native Meeting SDK Multi-Platform Delivery	Align Android, iOS, macOS, and Unreal Meeting SDK implementations under one auth/version strategy	zoom-meeting-sdk + platform skills
Native Video SDK Multi-Platform Delivery	Align Android, iOS, macOS, and Unity Video SDK implementations under one auth/version strategy	zoom-video-sdk + platform skills
Electron Meeting Embed	Embed meetings into desktop Electron apps	zoom-meeting-sdk-electron + zoom-oauth
Flutter Video Sessions	Build custom mobile video sessions in Flutter	zoom-video-sdk-flutter + zoom-oauth
React Native Video Sessions	Build custom mobile video sessions in React Native	zoom-video-sdk-react-native + zoom-oauth
Immersive Experiences	Custom video layouts with Layers API	zoom-apps-sdk
Collaborative Apps	Real-time shared state in meetings	zoom-apps-sdk
Contact Center App Lifecycle and Context Switching	Build Contact Center apps that handle engagement events and multi-engagement state	contact-center + zoom-apps-sdk
Virtual Agent Campaign Web and Mobile Wrapper	Deliver one campaign-driven bot flow across web and native mobile wrappers	virtual-agent + contact-center
Virtual Agent Knowledge Base Sync Pipeline	Sync external knowledge content into Zoom Virtual Agent using web sync or custom API connectors	virtual-agent + zoom-rest-api + zoom-oauth
Zoom Phone Smart Embed CRM Integration	Build CRM dialer and call logging flows using Smart Embed plus Phone APIs	phone + zoom-oauth + zoom-webhooks
Rivet Event-Driven API Orchestrator	Build a Node.js backend that combines webhooks and API actions through Rivet module clients	rivet-sdk + zoom-oauth + zoom-rest-api
Probe SDK Preflight Readiness Gate	Add browser/device/network diagnostics and readiness policy before Meeting SDK or Video SDK joins	probe-sdk + zoom-meeting-sdk or zoom-video-sdk
Complete Use-Case Index
APIs vs MCP Routing: choose API-only, MCP-only, or hybrid routing using official Zoom criteria.
AI Companion Integration: connect Zoom AI Companion capabilities into your app workflow.
AI Integration: add summarization, transcription, or assistant logic using Zoom data surfaces.
Backend Automation (S2S OAuth): run server-side jobs with account-level OAuth credentials.
Collaborative Apps: build shared in-meeting app state and interactions.
Contact Center Integration: connect Zoom Contact Center signals into external systems.
Contact Center App Lifecycle and Context Switching: implement event-driven engagement state and safe context switching in Contact Center apps.
Virtual Agent Campaign Web and Mobile Wrapper: deploy campaign-based Virtual Agent chat across website and Android/iOS WebView wrappers.
Virtual Agent Knowledge Base Sync Pipeline: automate knowledge-base ingestion with web sync strategy or custom API connector.
Zoom Phone Smart Embed CRM Integration: integrate Smart Embed events, Phone APIs, and CRM workflows with migration-safe data handling.
Rivet Event-Driven API Orchestrator: build a Node.js backend that combines webhook handling and API orchestration with Rivet.
Probe SDK Preflight Readiness Gate: run browser/device/network diagnostics before launching meeting or video session workflows.
Custom Video: decide between Video SDK and related components for custom session UX.
Custom Meeting UI (Web): use Meeting SDK Component View for a custom UI around a real Zoom meeting.
Scribe Transcription Pipeline: use AI Services Scribe for on-demand file transcription and batch archive processing.
Video SDK Bring Your Own Storage: configure Video SDK cloud recordings to write directly to your own S3 bucket.
Customer Support Cobrowsing: implement customer-agent collaborative browsing support flows.
Embed Meetings: embed Zoom meeting experience into your app.
Form Completion Assistant: build guided flows for form filling and completion assistance.
HD Video Resolution: enable and troubleshoot high-definition video requirements.
High-Volume Meeting Platform: build distributed meeting creation and event processing with concrete fallback patterns.
Immersive Experiences: use Zoom Apps Layers APIs for custom in-meeting visuals.
In-Meeting Apps: build Zoom Apps that run directly inside meeting and webinar contexts.
Marketplace Publishing: prepare and ship a Zoom app through Marketplace review.
Meeting Automation: create, update, and manage meetings programmatically.
Meeting Bots: build bots for meeting join, capture, and real-time analysis.
Native Meeting SDK Multi-Platform Delivery: standardize Android, iOS, macOS, and Unreal Meeting SDK delivery with shared auth and version controls.
Native Video SDK Multi-Platform Delivery: standardize Android, iOS, macOS, and Unity Video SDK delivery with shared auth and version controls.
Meeting Details with Events: combine REST retrieval with webhook event streams.
Minutes Calculation: compute usage and minute metrics across meetings/sessions.
Prebuilt Video UI: use UI Toolkit for faster Video SDK-based UI delivery.
QSS Monitoring: monitor Zoom quality statistics and performance indicators.
Raw Recording: capture raw streams for custom recording and processing pipelines.
Electron Meeting Embed: embed meetings in an Electron desktop application.
Flutter Video Sessions: build Video SDK sessions in Flutter mobile apps.
React Native Meeting Embed: embed Meeting SDK into React Native apps.
React Native Video Sessions: build custom video sessions in React Native.
Real-Time Media Streams: consume live media/transcript streams via RTMS.
Recording Download Pipeline: automate recording retrieval and storage pipelines.
Recording & Transcription: manage post-meeting recordings and transcript workflows.
Retrieve Meeting and Subscribe Events: join REST meeting fetch with event subscriptions.
SaaS App OAuth Integration: implement user-level OAuth in multi-tenant SaaS apps.
SDK Size Optimization: reduce bundle/runtime footprint for SDK-based apps.
SDK Wrappers and GUI: evaluate wrapper patterns and GUI frameworks around SDKs.
Team Chat LLM Bot: build a Team Chat bot with LLM-powered responses.
Testing and Development: local testing patterns, mocks, and safe development loops.
Token and Scope Troubleshooting: debug OAuth scope and token mismatch issues.
Transcription Bot (Linux): run Linux meeting bots for live transcription workloads.
Usage Reporting and Analytics: collect and analyze usage/reporting data.
User and Meeting Creation: provision users and schedule meetings in one flow.
Web SDK Embedding: embed meeting experiences in browser-based web apps.
Server-to-Server OAuth with Webhooks: combine account OAuth with event-driven backend processing.
Meeting Links vs Embedding: choose between join_url distribution and SDK embedding.
Enterprise App Deployment: deploy, govern, and operate Zoom integrations at enterprise scale.
Prerequisites
Zoom account (Pro, Business, or Enterprise)
App created in Zoom App Marketplace
OAuth credentials (Client ID and Secret)
References
Known Limitations & Quirks
Quick Start
Go to marketplace.zoom.us
Click Develop → Build App
Select app type (see references/app-types.md)
Configure OAuth and scopes
Copy credentials to your application
Detailed References
references/authentication.md - OAuth 2.0, S2S OAuth, JWT patterns
references/app-types.md - Decision guide for app types
references/scopes.md - OAuth scopes reference
references/marketplace.md - Marketplace portal navigation
references/query-routing-playbook.md - Route complex queries to the right specialized skills
references/interview-answer-routing.md - Short interview-ready answer pattern for zoom-general routing
references/routing-implementation.md - Concrete TypeScript query classification and skill handoff contract
references/automatic-skill-chaining-rest-webhooks.md - Executable process for REST + webhook chained workflows
references/meeting-webhooks-oauth-refresh-orchestration.md - Concrete design for meeting creation + webhook updates + OAuth token refresh
references/distributed-meeting-fallback-architecture.md - High-volume distributed architecture with retries, circuit breakers, and reconciliation fallbacks
references/community-repos.md - Curated official Zoom sample repositories by product
SDK Maintenance
references/sdk-upgrade-guide.md - Version policy, upgrade steps
references/sdk-upgrade-workflow.md - Changelog + RSS, version-by-version reusable upgrade workflow
references/sdk-logs-troubleshooting.md - Collecting SDK logs
Resources
Official docs: https://developers.zoom.us/
Marketplace: https://marketplace.zoom.us/
Developer forum: https://devforum.zoom.us/
Environment Variables
See references/environment-variables.md for standardized .env keys and where to find each value.
Operations
RUNBOOK.md - 5-minute preflight and debugging checklist.
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