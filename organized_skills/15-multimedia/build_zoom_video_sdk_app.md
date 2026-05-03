---
rating: ⭐⭐⭐
title: build-zoom-video-sdk-app
url: https://skills.sh/anthropics/knowledge-work-plugins/build-zoom-video-sdk-app
---

# build-zoom-video-sdk-app

skills/anthropics/knowledge-work-plugins/build-zoom-video-sdk-app
build-zoom-video-sdk-app
Installation
$ npx skills add https://github.com/anthropics/knowledge-work-plugins --skill build-zoom-video-sdk-app
SKILL.md
/build-zoom-video-sdk-app

Background reference for fully custom video-session products. Prefer plan-zoom-product first when the boundary between Meeting SDK and Video SDK is still unclear.

Build custom video experiences powered by Zoom's infrastructure.

Hard Routing Guardrail (Read First)
If the user asks for custom real-time video app behavior (topic/session join, custom rendering, attach/detach), route to Video SDK.
Do not switch to REST meeting endpoints for Video SDK join flows.
Video SDK does not use Meeting IDs, join_url, or Meeting SDK join payload fields (meetingNumber, passWord).
Meeting SDK vs Video SDK
Feature	Meeting SDK	Video SDK
UI	Default Zoom UI or Custom UI	Fully custom UI (you build it)
Experience	Zoom meetings	Video sessions
Branding	Limited customization	Full branding control
Features	Full Zoom features	Core video features
UI Options (Web)

Video SDK gives you full control over the UI:

Option	Description
UI Toolkit	Pre-built React components (low-code)
Custom UI	Build your own UI using the SDK APIs
Prerequisites
Zoom Video SDK credentials from Marketplace
SDK Key and Secret
Web development environment

Need help with OAuth or signatures? See the zoom-oauth skill for authentication flows.

Need pre-join diagnostics on web? Use probe-sdk before Video SDK join() to reduce first-minute failures.

Start troubleshooting fast: Use the 5-Minute Runbook before deep debugging.

Quick Start (Web)
NPM Usage (Bundler like Vite/Webpack)
import ZoomVideo from '@zoom/videosdk';

const client = ZoomVideo.createClient();
await client.init('en-US', 'Global', { patchJsMedia: true });
await client.join(topic, signature, userName, password);

// IMPORTANT: getMediaStream() ONLY works AFTER join()
const stream = client.getMediaStream();
await stream.startVideo();
await stream.startAudio();

CDN Usage (No Bundler)

WARNING: Ad blockers block source.zoom.us. Self-host the SDK to avoid issues.

# Download SDK locally
curl "https://source.zoom.us/videosdk/zoom-video-1.12.0.min.js" -o js/zoom-video-sdk.min.js

<script src="js/zoom-video-sdk.min.js"></script>

// CDN exports as WebVideoSDK, NOT ZoomVideo
// Must use .default property
const ZoomVideo = WebVideoSDK.default;
const client = ZoomVideo.createClient();

await client.init('en-US', 'Global', { patchJsMedia: true });
await client.join(topic, signature, userName, password);

// IMPORTANT: getMediaStream() ONLY works AFTER join()
const stream = client.getMediaStream();
await stream.startVideo();
await stream.startAudio();

ES Module with CDN (Race Condition Fix)

When using <script type="module"> with CDN, SDK may not be loaded yet:

// Wait for SDK to load before using
function waitForSDK(timeout = 10000) {
  return new Promise((resolve, reject) => {
    if (typeof WebVideoSDK !== 'undefined') {
      resolve();
      return;
    }
    const start = Date.now();
    const check = setInterval(() => {
      if (typeof WebVideoSDK !== 'undefined') {
        clearInterval(check);
        resolve();
      } else if (Date.now() - start > timeout) {
        clearInterval(check);
        reject(new Error('SDK failed to load'));
      }
    }, 100);
  });
}

// Usage
await waitForSDK();
const ZoomVideo = WebVideoSDK.default;
const client = ZoomVideo.createClient();

SDK Lifecycle (CRITICAL ORDER)

The SDK has a strict lifecycle. Violating it causes silent failures.

1. Create client:     client = ZoomVideo.createClient()
2. Initialize:        await client.init('en-US', 'Global', options)
3. Join session:      await client.join(topic, signature, userName, password)
4. Get stream:        stream = client.getMediaStream()  ← ONLY AFTER JOIN
5. Start media:       await stream.startVideo() / await stream.startAudio()


Common Mistake (Silent Failure):

// ❌ WRONG: Getting stream before joining
const client = ZoomVideo.createClient();
await client.init('en-US', 'Global');
const stream = client.getMediaStream();  // Returns undefined!
await client.join(...);

// ✅ CORRECT: Get stream after joining
const client = ZoomVideo.createClient();
await client.init('en-US', 'Global');
await client.join(...);
const stream = client.getMediaStream();  // Works!

Video Rendering (Event-Driven)

The SDK is event-driven. You must listen for events and render videos accordingly.

Use attachVideo() NOT renderVideo()
import { VideoQuality } from '@zoom/videosdk';

// Start your camera
await stream.startVideo();

// Attach video - returns element to append to DOM
const element = await stream.attachVideo(userId, VideoQuality.Video_360P);
container.appendChild(element);

// Detach when done
await stream.detachVideo(userId);

Required Events
// When other participant's video turns on/off
client.on('peer-video-state-change', async (payload) => {
  const { action, userId } = payload;
  if (action === 'Start') {
    const el = await stream.attachVideo(userId, VideoQuality.Video_360P);
    container.appendChild(el);
  } else {
    await stream.detachVideo(userId);
  }
});

// When participants join/leave
client.on('user-added', (payload) => { /* check bVideoOn */ });
client.on('user-removed', (payload) => { stream.detachVideo(payload.userId); });


See web/references/web.md for complete event handling patterns.

Key Concepts
Concept	Description
Session	Video session (not a meeting)
Topic	Session identifier (any string you choose)
Signature	JWT for authorization
MediaStream	Audio/video stream control
Session Creation Model

Important: Video SDK sessions are created just-in-time, not in advance.

Aspect	Video SDK	Meeting SDK
Pre-creation	NOT required	Create meeting via API first
Session start	First participant joins with topic	Join existing meeting ID
Topic	Any string (you define it)	Meeting ID from API
Scheduling	N/A - sessions are ad-hoc	Meetings can be scheduled
How Sessions Work
No pre-creation needed: Sessions don't exist until someone joins
Topic = Session ID: Any participants joining with the same topic string join the same session
First join creates it: The session is created when the first participant joins
No meeting ID: There's no numeric meeting ID like in Zoom Meetings
// Session is created on-the-fly when first user joins
// Any string can be the topic - it becomes the session identifier
await client.join('my-custom-session-123', signature, 'User Name');

// Other participants join the SAME session by using the SAME topic
await client.join('my-custom-session-123', signature, 'Another User');

Signature Endpoint Setup

The signature endpoint must be accessible from your frontend without CORS issues.

Option 1: Same-Origin Proxy (Recommended)

# Nginx config
location /api/ {
    proxy_pass http://YOUR_BACKEND_HOST:3005/api/;
    proxy_http_version 1.1;
    proxy_set_header Host $host;
}

// Frontend uses relative URL (same origin)
const response = await fetch('/api/signature', { ... });


Option 2: CORS Configuration

// Express.js backend
const cors = require('cors');
app.use(cors({
  origin: ['https://your-domain.com'],
  credentials: true
}));


WARNING: Mixed content (HTTPS page → HTTP API) will be blocked by browsers.

Use Cases
Use Case	Description
Video SDK BYOS (Bring Your Own Storage)	Save recordings directly to your S3 bucket
BYOS (Bring Your Own Storage)

Video SDK feature - Zoom saves cloud recordings directly to your Amazon S3 bucket. No downloading required.

Official docs: https://developers.zoom.us/docs/build/storage/

Prerequisites:

Video SDK account with Cloud Recording add-on (Universal Credit includes this)
AWS S3 bucket

Authentication options:

AWS Access Key - simpler setup
Cross Account Access - more secure (IAM role assumption)

S3 path structure:

Buckets/{bucketName}/cmr/byos/{YYYY}/{MM}/{DD}/{GUID}/cmr_byos/


Key benefits:

Zero download bandwidth costs
Direct storage during recording
Config-only setup (no webhook/download code needed)

Setup location: Developer Portal → Account Settings → General → Communications Content Storage Location

See ../general/use-cases/video-sdk-bring-your-own-storage.md for complete setup guide.

Detailed References
UI & Components
references/ui-toolkit.md - Pre-built UI components (Web)
references/triage-intake.md - What to ask first (turn vague reports into answers)
references/session-lifecycle.md - Correct API ordering + event-driven rendering
references/licensing-and-entitlements.md - License/admin prerequisites
references/token-contract-test-spec.md - Shared backend token contract and cross-platform smoke test
Platform Guides
references/authorization.md - Video SDK JWT generation
web/SKILL.md - Web Video SDK (JavaScript/TypeScript)
web/SKILL.md - Complete documentation navigation
web/examples/react-hooks.md - Official React hooks library
web/examples/framework-integrations.md - Next.js, Vue/Nuxt patterns
react-native/SKILL.md - React Native Video SDK (mobile wrapper, helper/event architecture)
react-native/SKILL.md - React Native documentation navigation
react-native/examples/session-join-pattern.md - Tokenized session join flow
flutter/SKILL.md - Flutter Video SDK (mobile wrapper, event-driven architecture)
flutter/SKILL.md - Flutter documentation navigation
flutter/examples/session-join-pattern.md - Tokenized session join flow
android/SKILL.md - Android Video SDK (native mobile custom UI, tokenized sessions)
ios/SKILL.md - iOS Video SDK (native mobile custom UI, delegate-driven lifecycle)
macos/SKILL.md - macOS Video SDK (desktop native apps, custom session windows)
unity/SKILL.md - Unity Video SDK wrapper (game-engine integration, scene-driven UX)
linux/SKILL.md - Linux Video SDK overview (C++ headless bots)
linux/linux.md - Linux C++ SDK (headless bots, raw media capture/injection)
linux/references/linux-reference.md - Linux API Reference
windows/SKILL.md - Windows C++ SDK (desktop applications, raw media capture/injection)
windows/references/windows-reference.md - Windows API Reference
references/troubleshooting.md - Common issues and solutions
references/forum-top-questions.md - Common forum question patterns (what to cover)
Sample Repositories
Official (by Zoom)
Type	Repository	Stars
Web	videosdk-web-sample	137
Web NPM	videosdk-web	56
Auth	videosdk-auth-endpoint-sample	23
UI Toolkit Web	videosdk-zoom-ui-toolkit-web	17
UI Toolkit React	videosdk-zoom-ui-toolkit-react-sample	17
Next.js	videosdk-nextjs-quickstart	16
Telehealth	VideoSDK-Web-Telehealth	11
Linux	videosdk-linux-raw-recording-sample	-

Full list: See general/references/community-repos.md

Resources
Official docs: https://developers.zoom.us/docs/video-sdk/
Developer forum: https://devforum.zoom.us/
Environment Variables
See references/environment-variables.md for standardized .env keys and where to find each value.
Linux Operations
linux/RUNBOOK.md - Linux platform preflight and debugging checklist.
Weekly Installs
290
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