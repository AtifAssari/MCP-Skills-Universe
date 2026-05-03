---
rating: ⭐⭐⭐
title: zoom-cobrowse-sdk
url: https://skills.sh/anthropics/knowledge-work-plugins/zoom-cobrowse-sdk
---

# zoom-cobrowse-sdk

skills/anthropics/knowledge-work-plugins/zoom-cobrowse-sdk
zoom-cobrowse-sdk
Installation
$ npx skills add https://github.com/anthropics/knowledge-work-plugins --skill zoom-cobrowse-sdk
SKILL.md
Zoom Cobrowse SDK - Web Development

Background reference for collaborative browsing on the web with Zoom Cobrowse SDK. Use this after the support workflow is clear and you need implementation detail.

Official Documentation: https://developers.zoom.us/docs/cobrowse-sdk/
API Reference: https://marketplacefront.zoom.us/sdk/cobrowse/
Quickstart Repository: https://github.com/zoom/CobrowseSDK-Quickstart
Auth Endpoint Sample: https://github.com/zoom/cobrowsesdk-auth-endpoint-sample

Quick Links

New to Cobrowse SDK? Follow this path:

Get Started Guide - Complete setup from credentials to first session
Session Lifecycle - Understanding customer and agent flows
JWT Authentication - Token generation and security
Customer Integration - Integrate SDK into your website
Agent Integration - Set up agent portal (iframe or npm)

Core Concepts:

Two Roles Pattern - Customer vs Agent architecture
Session Lifecycle - PIN generation, connection, reconnection
JWT Authentication - SDK Key vs API Key, role_type, claims
Distribution Methods - CDN vs npm (BYOP)

Features:

Annotation Tools - Drawing, highlighting, pointer tools
Privacy Masking - Hide sensitive fields from agents
Remote Assist - Agent can scroll customer's page
Multi-Tab Persistence - Session continues across tabs
BYOP Mode - Bring Your Own PIN with npm integration

Troubleshooting:

Common Issues - Quick diagnostics and solutions
Error Codes - Complete error reference
CORS and CSP - Cross-origin and security policy configuration
Browser Compatibility - Supported browsers and limitations
5-Minute Runbook - Fast preflight checks before deep debugging

Reference:

API Reference - Complete SDK methods and events
Settings Reference - All initialization settings
Integrated Index - see the section below in this file
SDK Overview

The Zoom Cobrowse SDK is a JavaScript library that provides:

Real-Time Co-Browsing: Agent sees customer's browser activity live
PIN-Based Sessions: Secure 6-digit PIN for customer-to-agent connection
Annotation Tools: Drawing, highlighting, vanishing pen, rectangle, color picker
Privacy Masking: CSS selector-based masking of sensitive form fields
Remote Assist: Agent can scroll customer's page (with consent)
Multi-Tab Persistence: Session continues when customer opens new tabs
Auto-Reconnection: Session recovers from page refresh (2-minute window)
Session Events: Real-time events for session state changes
HTTPS Required: Secure connections (HTTP only works on loopback/local development hosts)
No Plugins: Pure JavaScript, no browser extensions needed
Two Roles Architecture

Cobrowse has two distinct roles, each with different integration patterns:

Role	role_type	Integration	JWT Required	Purpose
Customer	1	Website integration (CDN or npm)	Yes	User who shares their browser session
Agent	2	Iframe (CDN) or npm (BYOP only)	Yes	Support staff who views/assists customer

Key Insight: Customer and agent use different integration methods but the same JWT authentication pattern.

Read This First (Critical)

For customer/agent demos, treat the PIN from customer SDK event pincode_updated as the only user-facing PIN.

Show one clearly labeled value in UI (for example, Support PIN).
Use that same PIN for agent join.
Do not expose provisional/debug PINs from backend pre-start records to users.

If these rules are ignored, agent desk often fails with Pincode is not found / code 30308.

Typical Production Flow (Most Common)

This is the flow most teams implement first, and what users usually expect in demos:

Customer starts session first (role_type=1)
Backend creates/records session
Backend returns customer JWT
Customer SDK starts and receives a PIN
Agent joins second (role_type=2)
Agent enters customer PIN
Backend validates PIN and session state
Backend returns agent JWT
Agent opens Zoom-hosted desk iframe (or custom npm agent UI in BYOP)

If a demo only has one generic "session" user, it is incomplete for real cobrowse operations.

Prerequisites
Platform Requirements

Supported Browsers:

Chrome 80+ ✓
Firefox 78+ ✓
Safari 14+ ✓
Edge 80+ ✓
Internet Explorer ✗ (not supported)

Network Requirements:

HTTPS required (HTTP works on loopback/local development hosts only)
Allow cross-origin requests to *.zoom.us
CSP headers must allow Zoom domains (see CORS and CSP guide)

Third-Party Cookies:

Must enable third-party cookies for refresh reconnection
Privacy mode may limit certain features
Zoom Account Requirements
Zoom Workplace Account with SDK Universal Credit
Video SDK App created in Zoom Marketplace
Cobrowse SDK Credentials from the app's Cobrowse tab

Note: Cobrowse SDK is a feature of Video SDK (not a separate product).

Credentials Overview

You'll receive 4 credentials from Zoom Marketplace → Video SDK App → Cobrowse tab:

Credential	Type	Used For	Exposure Safe?
SDK Key	Public	CDN URL, JWT app_key claim	✓ Yes (client-side)
SDK Secret	Private	Sign JWTs	✗ No (server-side only)
API Key	Private	REST API calls (optional)	✗ No (server-side only)
API Secret	Private	REST API calls (optional)	✗ No (server-side only)

Critical: SDK Key is public (embedded in CDN URL), but SDK Secret must never be exposed client-side.

Quick Start
Step 1: Get SDK Credentials
Go to Zoom Marketplace
Open your Video SDK App (or create one)
Navigate to the Cobrowse tab
Copy your credentials:
SDK Key
SDK Secret
API Key (optional)
API Secret (optional)
Step 2: Set Up Token Server

Deploy a server-side endpoint to generate JWTs. Use the official sample:

git clone https://github.com/zoom/cobrowsesdk-auth-endpoint-sample.git
cd cobrowsesdk-auth-endpoint-sample
npm install

# Create .env file
cat > .env << EOF
ZOOM_SDK_KEY=your_sdk_key_here
ZOOM_SDK_SECRET=your_sdk_secret_here
PORT=4000
EOF

npm start


Token endpoint:

// POST https://YOUR_TOKEN_SERVICE_BASE_URL
{
  "role": 1,           // 1 = customer, 2 = agent
  "userId": "user123",
  "userName": "John Doe"
}

// Response
{
  "token": "eyJhbGciOiJIUzI1NiIs..."
}

Step 3: Customer Side Integration (CDN)
<!DOCTYPE html>
<html>
<head>
  <title>Customer - Cobrowse Demo</title>
  <script type="module">
    const ZOOM_SDK_KEY = 'YOUR_SDK_KEY';
    
    // Load SDK from CDN
    (function(r, a, b, f, c, d) {
      r[f] = r[f] || { init: function() { r.ZoomCobrowseSDKInitArgs = arguments }};
      var fragment = a.createDocumentFragment();
      function loadJs(url) {
        c = a.createElement(b);
        d = a.getElementsByTagName(b)[0];
        c["async"] = false;
        c.src = url;
        fragment.appendChild(c);
      }
      loadJs(`https://us01-zcb.zoom.us/static/resource/sdk/${ZOOM_SDK_KEY}/js/2.13.2`);
      d.parentNode.insertBefore(fragment, d);
    })(window, document, "script", "ZoomCobrowseSDK");
  </script>
</head>
<body>
  <h1>Customer Support</h1>
  <button id="cobrowse-btn" disabled>Loading...</button>
  
  <!-- Sensitive fields - will be masked from agent -->
  <label>SSN: <input type="text" class="pii-mask" placeholder="XXX-XX-XXXX"></label>
  <label>Credit Card: <input type="text" class="pii-mask" placeholder="XXXX-XXXX-XXXX-XXXX"></label>
  
  <script type="module">
    let sessionRef = null;
    
    const settings = {
      allowAgentAnnotation: true,
      allowCustomerAnnotation: true,
      piiMask: {
        maskCssSelectors: ".pii-mask",
        maskType: "custom_input"
      }
    };
    
    ZoomCobrowseSDK.init(settings, function({ success, session, error }) {
      if (success) {
        sessionRef = session;
        
        // Listen for PIN code
        session.on("pincode_updated", (payload) => {
          console.log("PIN Code:", payload.pincode);
          // IMPORTANT: this is the PIN agent should use
          alert(`Share this PIN with agent: ${payload.pincode}`);
        });
        
        // Listen for session events
        session.on("session_started", () => console.log("Session started"));
        session.on("agent_joined", () => console.log("Agent joined"));
        session.on("agent_left", () => console.log("Agent left"));
        session.on("session_ended", () => console.log("Session ended"));
        
        document.getElementById("cobrowse-btn").disabled = false;
        document.getElementById("cobrowse-btn").innerText = "Start Cobrowse Session";
      } else {
        console.error("SDK init failed:", error);
      }
    });
    
    document.getElementById("cobrowse-btn").addEventListener("click", async () => {
      // Fetch JWT from your server
      const response = await fetch("https://YOUR_TOKEN_SERVICE_BASE_URL", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          role: 1,
          userId: "customer_" + Date.now(),
          userName: "Customer"
        })
      });
      const { token } = await response.json();
      
      // Start cobrowse session
      sessionRef.start({ sdkToken: token });
    });
  </script>
</body>
</html>

Step 4: Agent Side Integration (Iframe)
<!DOCTYPE html>
<html>
<head>
  <title>Agent Portal</title>
</head>
<body>
  <h1>Agent Portal</h1>
  <iframe 
    id="agent-iframe"
    width="1024" 
    height="768"
    allow="autoplay *; camera *; microphone *; display-capture *; geolocation *;"
  ></iframe>
  
  <script>
    async function connectAgent() {
      // Fetch JWT from your server
      const response = await fetch("https://YOUR_TOKEN_SERVICE_BASE_URL", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          role: 2,
          userId: "agent_" + Date.now(),
          userName: "Support Agent"
        })
      });
      const { token } = await response.json();
      
      // Load Zoom agent portal
      const iframe = document.getElementById("agent-iframe");
      iframe.src = `https://us01-zcb.zoom.us/sdkapi/zcb/frame-templates/desk?access_token=${token}`;
    }
    
    connectAgent();
  </script>
</body>
</html>

Step 5: Test the Integration
Open two separate browsers (or incognito + normal)
Customer browser: Open customer page, click "Start Cobrowse Session"
Customer browser: Note the 6-digit PIN displayed
Agent browser: Open agent page, enter the PIN code
Both browsers: Session connects, agent can see customer's page
Test features: Annotations, data masking, remote assist
Key Features
1. Annotation Tools

Both customer and agent can draw on the shared screen:

const settings = {
  allowAgentAnnotation: true,      // Agent can draw
  allowCustomerAnnotation: true    // Customer can draw
};


Available tools:

Pen (persistent)
Vanishing pen (disappears after 4 seconds)
Rectangle
Color picker
Eraser
Undo/Redo
2. Privacy Masking

Hide sensitive fields from agents using CSS selectors:

const settings = {
  piiMask: {
    maskType: "custom_input",           // Mask specific fields
    maskCssSelectors: ".pii-mask, #ssn", // CSS selectors
    maskHTMLAttributes: "data-sensitive=true" // HTML attributes
  }
};


Supported masking:

Text nodes ✓
Form inputs ✓
Select elements ✓
Images ✗ (not supported)
Links ✗ (not supported)
3. Remote Assist

Agent can scroll the customer's page:

const settings = {
  remoteAssist: {
    enable: true,
    enableCustomerConsent: true,        // Customer must approve
    remoteAssistTypes: ['scroll_page'], // Only scroll supported
    requireStopConfirmation: false      // Confirmation when stopping
  }
};

4. Multi-Tab Session Persistence

Session continues when customer opens new tabs:

const settings = {
  multiTabSessionPersistence: {
    enable: true,
    stateCookieKey: '$$ZCB_SESSION$$'  // Cookie key (base64 encoded)
  }
};

Session Lifecycle
Customer Flow
Load SDK → CDN script loads ZoomCobrowseSDK
Initialize → ZoomCobrowseSDK.init(settings, callback)
Fetch JWT → Request token from your server (role_type=1)
Start Session → session.start({ sdkToken })
PIN Generated → pincode_updated event fires
Share PIN → Customer gives 6-digit PIN to agent
Agent Joins → agent_joined event fires
Session Active → Real-time synchronization begins
End Session → session.end() or agent leaves
Agent Flow
Fetch JWT → Request token from your server (role_type=2)
Load Iframe → Point to Zoom agent portal with token
Enter PIN → Agent inputs customer's 6-digit PIN
Connect → session_joined event fires
View Session → Agent sees customer's browser
Use Tools → Annotations, remote assist, zoom
Leave Session → Click "Leave Cobrowse" button
Session Recovery (Auto-Reconnect)

When customer refreshes the page:

ZoomCobrowseSDK.init(settings, function({ success, session, error }) {
  if (success) {
    const sessionInfo = session.getSessionInfo();
    
    // Check if session is recoverable
    if (sessionInfo.sessionStatus === 'session_recoverable') {
      session.join();  // Auto-rejoin previous session
    } else {
      // Start new session
      session.start({ sdkToken });
    }
  }
});


Recovery window: 2 minutes. After 2 minutes, session ends.

Critical Gotchas and Best Practices
⚠️ CRITICAL: SDK Secret Must Stay Server-Side

Problem: Developers often accidentally embed SDK Secret in frontend code.

Solution:

✓ SDK Key → Safe to expose (embedded in CDN URL)
✗ SDK Secret → Never expose (use for JWT signing server-side)
// ❌ WRONG - Secret exposed in frontend
const jwt = signJWT(payload, 'YOUR_SDK_SECRET');  // Security risk!

// ✅ CORRECT - Secret stays on server
const response = await fetch('/api/token', {
  method: 'POST',
  body: JSON.stringify({ role: 1, userId, userName })
});
const { token } = await response.json();

SDK Key vs API Key (Different Purposes!)
Credential	Used For	JWT Claim
SDK Key	CDN URL, JWT app_key	app_key: "SDK_KEY"
API Key	REST API calls (optional)	Not used in JWT

Common mistake: Using API Key instead of SDK Key in JWT app_key claim.

Session Limits
Limit	Value	What Happens
Customers per session	1	Error 1012: SESSION_CUSTOMER_COUNT_LIMIT
Agents per session	5	Error 1013: SESSION_AGENT_COUNT_LIMIT
Active sessions per browser	1	Error 1004: SESSION_COUNT_LIMIT
PIN code length	10 chars max	Error 1008: SESSION_PIN_INVALID_FORMAT
Session Timeout Behavior
Event	Timeout	What Happens
Agent waiting for customer	3 minutes	Session ends automatically
Page refresh reconnection	2 minutes	Session ends if not reconnected
Reconnection attempts	2 times max	Session ends after 2 failed attempts
HTTPS Requirement

Problem: SDK doesn't load on HTTP sites.

Solution:

Production: Use HTTPS ✓
Development: Use a loopback host for local HTTP testing ✓
Development: Use a local HTTPS endpoint with a trusted/self-signed cert if required ✓
Third-Party Cookies Required

Problem: Refresh reconnection doesn't work.

Solution: Enable third-party cookies in browser settings.

Affected scenarios:

Browser privacy mode
Safari with "Prevent cross-site tracking" enabled
Chrome with "Block third-party cookies" enabled
Distribution Method Confusion
Method	Use Case	Agent Integration	BYOP Required
CDN	Most use cases	Zoom-hosted iframe	No (auto PIN)
npm	Custom agent UI, full control	Custom npm integration	Yes (required)

Key Insight: If you want npm integration, you must use BYOP (Bring Your Own PIN) mode.

Cross-Origin Iframe Handling

Problem: Cobrowse doesn't work in cross-origin iframes.

Solution: Inject SDK snippet into cross-origin iframes:

<script>
const ZOOM_SDK_KEY = "YOUR_SDK_KEY_HERE";

(function(r,a,b,f,c,d){r[f]=r[f]||{init:function(){r.ZoomCobrowseSDKInitArgs=arguments}};
var fragment=a.createDocumentFragment();function loadJs(url) {c=a.createElement(b);d=a.getElementsByTagName(b)[0];c.async=false;c.src=url;fragment.appendChild(c);};
loadJs('https://us01-zcb.zoom.us/static/resource/sdk/${ZOOM_SDK_KEY}/js');d.parentNode.insertBefore(fragment,d);})(window,document,'script','ZoomCobrowseSDK');
</script>


Same-origin iframes: No extra setup needed.

Known Limitations
Synchronization Limits

Not synchronized:

HTML5 Canvas elements
WebGL content
Audio and Video elements
Shadow DOM
PDF rendered with Canvas
Web Components

Partially synchronized:

Drop-down boxes (only selected result)
Date pickers (only selected result)
Color pickers (only selected result)
Rendering Limits
High-resolution images may be compressed
Different screen sizes may cause CSS media query differences
Cross-origin images may not render (CORS restrictions)
Cross-origin fonts may not render (CORS restrictions)
Masking Limits

Supported:

Text nodes ✓
Form inputs ✓
Select elements ✓

Not supported:

<img> elements ✗
Links ✗
Complete Documentation Library

This skill includes comprehensive guides organized by category:

Core Concepts
Two Roles Pattern - Customer vs Agent architecture
Session Lifecycle - Complete flow from start to end
JWT Authentication - Token structure and signing
Distribution Methods - CDN vs npm (BYOP)
Examples
Customer Integration - Complete customer-side setup
Agent Integration - Iframe and npm agent setups
Annotations - Drawing tools configuration
Privacy Masking - Field masking patterns
Remote Assist - Agent page control
Multi-Tab Persistence - Cross-tab sessions
BYOP Custom PIN - Custom PIN codes
References
API Reference - Complete SDK methods and events
Settings Reference - All initialization settings
Error Codes - Complete error reference
Session Events - All event types
Troubleshooting
Common Issues - Quick diagnostics
Error Codes - Error code reference
CORS and CSP - Cross-origin configuration
Browser Compatibility - Browser support
Resources
Official Docs: https://developers.zoom.us/docs/cobrowse-sdk/
API Reference: https://marketplacefront.zoom.us/sdk/cobrowse/
Quickstart Repo: https://github.com/zoom/CobrowseSDK-Quickstart
Auth Endpoint Sample: https://github.com/zoom/cobrowsesdk-auth-endpoint-sample
Dev Forum: https://devforum.zoom.us/
Developer Blog: https://developers.zoom.us/blog/?category=zoom-cobrowse-sdk

Need help? Start with Integrated Index section below for complete navigation.

Integrated Index

This section was migrated from SKILL.md.

Complete navigation guide for all Cobrowse SDK documentation.

Getting Started (Start Here!)

If you're new to Zoom Cobrowse SDK, follow this learning path:

SKILL.md - Main overview and quick start
5-Minute Runbook - Preflight checks for common failures
Get Started Guide - Step-by-step setup from credentials to first session
Session Lifecycle - Understand the complete customer and agent flow
Customer Integration - Integrate SDK into your website
Agent Integration - Set up agent portal
Core Concepts

Foundational concepts you need to understand:

Two Roles Pattern - Customer (role_type=1) vs Agent (role_type=2) architecture
Session Lifecycle - Complete flow: init → start → PIN → connect → end
JWT Authentication - Token structure, signing, SDK Key vs API Key
Distribution Methods - CDN vs npm (BYOP mode)
Examples and Patterns

Complete working examples for common scenarios:

Session Management
Customer Integration - Complete customer-side implementation (CDN and npm)
Agent Integration - Iframe and npm agent setup patterns
Session Events - Handle all session lifecycle events
Auto-Reconnection - Page refresh and session recovery
Features
Annotation Tools - Enable drawing, highlighting, vanishing pen
Privacy Masking - Mask sensitive fields with CSS selectors
Remote Assist - Agent can scroll customer's page
Multi-Tab Persistence - Session continues across browser tabs
BYOP Custom PIN - Bring Your Own PIN with npm integration
References

Complete API and configuration references:

SDK Reference

API Reference - All SDK methods and interfaces

ZoomCobrowseSDK.init()
session.start()
session.join()
session.end()
session.on()
session.getSessionInfo()

Settings Reference - All initialization settings

allowAgentAnnotation
allowCustomerAnnotation
piiMask
remoteAssist
multiTabSessionPersistence

Session Events Reference - All event types

pincode_updated
session_started
session_ended
agent_joined
agent_left
session_error
session_reconnecting
remote_assist_started
remote_assist_stopped
Error Reference
Error Codes - Complete error code reference
1001-1017: Session errors
2001: Token errors
9999: Service errors
Official Documentation
Get Started - Official get started documentation (crawled)
Features - Official features documentation (crawled)
Authorization - Official JWT authorization docs (crawled)
API Documentation - Crawled API reference docs
Troubleshooting

Quick diagnostics and common issue resolution:

Common Issues - Quick fixes for frequent problems

SDK not loading
Token generation fails
Agent can't connect
Fields not masked
Session doesn't reconnect after refresh

Error Codes - Error code lookup and solutions

Session start/join failures (1001, 1011, 1016)
Session limit errors (1002, 1004, 1012, 1013, 1015)
PIN code errors (1006, 1008, 1009, 1010)
Token errors (2001)

CORS and CSP - Cross-origin and Content Security Policy setup

Access-Control-Allow-Origin headers
Content-Security-Policy headers
Cross-origin iframe handling
Same-origin iframe handling

Browser Compatibility - Browser requirements and limitations

Supported browsers (Chrome 80+, Firefox 78+, Safari 14+, Edge 80+)
Internet Explorer not supported
Privacy mode limitations
Third-party cookie requirements
By Use Case

Find documentation by what you're trying to do:

I want to...

Set up cobrowse for the first time:

Get Started Guide
JWT Authentication
Customer Integration
Agent Integration

Add annotation tools:

Annotation Tools Example
[Settings Reference - allowAgentAnnotation](references/settings-reference.md#allowa gentannotation)
Settings Reference - allowCustomerAnnotation

Hide sensitive data from agents:

Privacy Masking Example
Settings Reference - piiMask

Let agents control customer's page:

Remote Assist Example
Settings Reference - remoteAssist

Use custom PIN codes:

BYOP Custom PIN Example
JWT Authentication - enable_byop

Handle page refreshes:

Auto-Reconnection Example
Session Lifecycle - Recovery

Integrate with npm (not CDN):

BYOP Custom PIN Example
Distribution Methods

Debug session connection issues:

Common Issues
Error Codes
Session Events - session_error

Configure CORS and CSP headers:

CORS and CSP Guide
Browser Compatibility
By Error Code

Quick lookup for error code solutions:

Session Errors
1001 (SESSION_START_FAILED) → Error Codes
1002 (SESSION_CONNECTING_IN_PROGRESS) → Error Codes
1004 (SESSION_COUNT_LIMIT) → Error Codes
1011 (SESSION_JOIN_FAILED) → Error Codes
1012 (SESSION_CUSTOMER_COUNT_LIMIT) → Error Codes
1013 (SESSION_AGENT_COUNT_LIMIT) → Error Codes
1015 (SESSION_DUPLICATE_USER) → Error Codes
1016 (NETWORK_ERROR) → Error Codes
1017 (SESSION_CANCELING_IN_PROGRESS) → Error Codes
PIN Errors
1006 (SESSION_JOIN_PIN_NOT_FOUND) → Error Codes
1008 (SESSION_PIN_INVALID_FORMAT) → Error Codes
1009 (SESSION_START_PIN_REQUIRED) → Error Codes
1010 (SESSION_START_PIN_CONFLICT) → Error Codes
Auth Errors
2001 (TOKEN_INVALID) → Error Codes
Service Errors
9999 (UNDEFINED) → Error Codes
Official Resources

External documentation and samples:

Official Docs: https://developers.zoom.us/docs/cobrowse-sdk/
API Reference: https://marketplacefront.zoom.us/sdk/cobrowse/
Quickstart Repo: https://github.com/zoom/CobrowseSDK-Quickstart
Auth Endpoint Sample: https://github.com/zoom/cobrowsesdk-auth-endpoint-sample
Dev Forum: https://devforum.zoom.us/
Developer Blog: https://developers.zoom.us/blog/?category=zoom-cobrowse-sdk
Documentation Structure
cobrowse-sdk/
├── SKILL.md                    # Main skill entry point
├── SKILL.md                    # This file - complete navigation
├── get-started.md              # Step-by-step setup guide
│
├── concepts/                   # Core concepts
│   ├── two-roles-pattern.md
│   ├── session-lifecycle.md
│   ├── jwt-authentication.md
│   └── distribution-methods.md
│
├── examples/                   # Working examples
│   ├── customer-integration.md
│   ├── agent-integration.md
│   ├── annotations.md
│   ├── privacy-masking.md
│   ├── remote-assist.md
│   ├── multi-tab-persistence.md
│   ├── byop-custom-pin.md
│   ├── session-events.md
│   └── auto-reconnection.md
│
├── references/                 # API and config references
│   ├── api-reference.md        # SDK methods
│   ├── settings-reference.md   # Init settings
│   ├── session-events.md       # Event types
│   ├── error-codes.md          # Error reference
│   ├── get-started.md          # Official docs (crawled)
│   ├── features.md             # Official docs (crawled)
│   ├── authorization.md        # Official docs (crawled)
│   └── api.md                  # API docs (crawled)
│
└── troubleshooting/            # Problem resolution
    ├── common-issues.md
    ├── error-codes.md
    ├── cors-csp.md
    └── browser-compatibility.md

Search Tips

Find by keyword:

"annotation" → Annotation Tools
"mask" or "privacy" → Privacy Masking
"PIN" or "custom PIN" → BYOP Custom PIN
"JWT" or "token" → JWT Authentication
"error" → Error Codes
"CORS" or "CSP" → CORS and CSP
"iframe" → Agent Integration
"npm" → Distribution Methods, BYOP
"refresh" or "reconnect" → Auto-Reconnection
"agent" → Agent Integration, Two Roles Pattern
"customer" → Customer Integration, Two Roles Pattern

Not finding what you need? Check the Official Documentation or ask on the Dev Forum.

Environment Variables
See references/environment-variables.md for standardized .env keys and where to find each value.
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
SnykWarn