---
rating: ⭐⭐
title: configuring-tauri-csp
url: https://skills.sh/dchuk/claude-code-tauri-skills/configuring-tauri-csp
---

# configuring-tauri-csp

skills/dchuk/claude-code-tauri-skills/configuring-tauri-csp
configuring-tauri-csp
Installation
$ npx skills add https://github.com/dchuk/claude-code-tauri-skills --skill configuring-tauri-csp
SKILL.md
Tauri Content Security Policy (CSP) Configuration

This skill covers Content Security Policy configuration for Tauri v2 desktop applications.

Why CSP Matters in Tauri

CSP is a security mechanism that mitigates common web vulnerabilities in Tauri applications:

XSS Prevention: Restricts which scripts can execute, blocking injected malicious code
Resource Control: Limits where the WebView can load assets from (scripts, styles, images, fonts)
Trust Boundaries: Strengthens the isolation between frontend WebView and backend Rust code
Attack Surface Reduction: Prevents unauthorized network connections and resource loading

Tauri operates on a trust boundary model where frontend code has limited access to system resources through a well-defined IPC layer. CSP adds an additional layer of protection within the frontend trust zone.

How Tauri Implements CSP

Tauri uses a two-part protection strategy:

Local Scripts: Protected through cryptographic hashing at compile time
Styles and External Scripts: Verified using nonces

Tauri automatically appends nonces and hashes to bundled code during compilation. Developers only need to configure application-specific trusted sources.

Important: CSP protection only activates when explicitly configured in the Tauri configuration file.

Default CSP Behavior

By default, Tauri does not apply a CSP. You must explicitly configure it in tauri.conf.json under the security section:

{
  "security": {
    "csp": null
  }
}


When csp is null or omitted, no Content Security Policy is enforced.

Basic CSP Configuration
Minimal Secure Configuration
{
  "security": {
    "csp": {
      "default-src": "'self'"
    }
  }
}


This restricts all resources to the same origin only.

Recommended Configuration
{
  "security": {
    "csp": {
      "default-src": "'self' customprotocol: asset:",
      "connect-src": "ipc: http://ipc.localhost",
      "font-src": ["https://fonts.gstatic.com"],
      "img-src": "'self' asset: http://asset.localhost blob: data:",
      "style-src": "'unsafe-inline' 'self' https://fonts.googleapis.com"
    }
  }
}

Common CSP Directives for Tauri
default-src

Fallback policy for all resource types not explicitly defined.

"default-src": "'self' customprotocol: asset:"


Common values:

'self' - Same origin only
'none' - Block all resources
customprotocol: - Tauri custom protocol
asset: - Tauri asset protocol
script-src

Controls which scripts can execute.

"script-src": "'self'"


For WebAssembly or Rust-based frontends (Leptos, Yew, Dioxus):

"script-src": "'self' 'wasm-unsafe-eval'"


Warning: Never use 'unsafe-eval' unless absolutely required.

style-src

Controls stylesheet sources.

"style-src": "'self' 'unsafe-inline' https://fonts.googleapis.com"


Note: 'unsafe-inline' is often needed for CSS-in-JS libraries but reduces security.

connect-src

Controls allowed connection destinations for fetch, WebSocket, etc.

"connect-src": "ipc: http://ipc.localhost https://api.example.com"


Tauri-specific:

ipc: - Inter-process communication with Rust backend
http://ipc.localhost - Alternative IPC endpoint
img-src

Controls image loading sources.

"img-src": "'self' asset: http://asset.localhost blob: data:"


Common values:

blob: - Blob URLs (for dynamically created images)
data: - Data URLs (base64 encoded images)
asset: - Tauri asset protocol
font-src

Controls font loading sources.

"font-src": "'self' https://fonts.gstatic.com"

frame-src

Controls iframe sources.

"frame-src": "'none'"


Recommended to block all frames unless specifically needed.

object-src

Controls plugin content (Flash, Java, etc.).

"object-src": "'none'"


Always set to 'none' for modern applications.

Configuration Format Options
Object Format (Recommended)
{
  "security": {
    "csp": {
      "default-src": "'self'",
      "script-src": "'self' 'wasm-unsafe-eval'",
      "style-src": "'self' 'unsafe-inline'"
    }
  }
}

Array Format for Multiple Sources
{
  "security": {
    "csp": {
      "font-src": ["'self'", "https://fonts.gstatic.com", "https://fonts.googleapis.com"]
    }
  }
}

String Format
{
  "security": {
    "csp": "default-src 'self'; script-src 'self'"
  }
}

Framework-Specific Configurations
React/Vue/Svelte (Standard JS Frameworks)
{
  "security": {
    "csp": {
      "default-src": "'self'",
      "script-src": "'self'",
      "style-src": "'self' 'unsafe-inline'",
      "img-src": "'self' data: blob:",
      "font-src": "'self'",
      "connect-src": "ipc: http://ipc.localhost"
    }
  }
}

Leptos/Yew/Dioxus (Rust/WASM Frameworks)
{
  "security": {
    "csp": {
      "default-src": "'self'",
      "script-src": "'self' 'wasm-unsafe-eval'",
      "style-src": "'self' 'unsafe-inline'",
      "img-src": "'self' data: blob:",
      "font-src": "'self'",
      "connect-src": "ipc: http://ipc.localhost"
    }
  }
}

With External APIs
{
  "security": {
    "csp": {
      "default-src": "'self'",
      "script-src": "'self'",
      "connect-src": "ipc: http://ipc.localhost https://api.example.com wss://ws.example.com",
      "img-src": "'self' https://cdn.example.com"
    }
  }
}

Security Best Practices
1. Avoid Remote Scripts

Never load scripts from CDNs in production:

// AVOID - introduces attack vector
"script-src": "'self' https://cdn.jsdelivr.net"

// PREFERRED - bundle all dependencies
"script-src": "'self'"

2. Minimize unsafe-inline

Only use 'unsafe-inline' when required by your framework:

// More secure
"style-src": "'self'"

// Less secure but sometimes necessary
"style-src": "'self' 'unsafe-inline'"

3. Use Restrictive Defaults

Start restrictive and add permissions as needed:

{
  "security": {
    "csp": {
      "default-src": "'none'",
      "script-src": "'self'",
      "style-src": "'self'",
      "img-src": "'self'",
      "font-src": "'self'",
      "connect-src": "ipc: http://ipc.localhost"
    }
  }
}

4. Block Dangerous Features

Always block unused dangerous features:

{
  "security": {
    "csp": {
      "object-src": "'none'",
      "base-uri": "'self'",
      "form-action": "'self'"
    }
  }
}

Advanced Configuration
Disabling CSP Modifications

If you need full control over CSP (not recommended):

{
  "security": {
    "csp": {
      "default-src": "'self'"
    },
    "dangerousDisableAssetCspModification": true
  }
}


Warning: This disables Tauri's automatic nonce and hash injection.

Freeze Prototype

Additional XSS protection by freezing JavaScript prototypes:

{
  "security": {
    "csp": {
      "default-src": "'self'"
    },
    "freezePrototype": true
  }
}

Troubleshooting
Resources Blocked by CSP

Check browser DevTools console for CSP violation messages. They indicate which directive is blocking the resource.

Example error:

Refused to load the script 'https://example.com/script.js' because it violates the following Content Security Policy directive: "script-src 'self'"


Solution: Add the domain to the appropriate directive:

"script-src": "'self' https://example.com"

WebAssembly Not Loading

Add 'wasm-unsafe-eval' to script-src:

"script-src": "'self' 'wasm-unsafe-eval'"

Inline Styles Not Working

For CSS-in-JS libraries, add 'unsafe-inline' to style-src:

"style-src": "'self' 'unsafe-inline'"

IPC Not Working

Ensure connect-src includes Tauri IPC endpoints:

"connect-src": "ipc: http://ipc.localhost"

Complete Example Configuration
{
  "productName": "my-tauri-app",
  "version": "1.0.0",
  "security": {
    "csp": {
      "default-src": "'self' customprotocol: asset:",
      "script-src": "'self'",
      "style-src": "'self' 'unsafe-inline'",
      "img-src": "'self' asset: http://asset.localhost blob: data:",
      "font-src": "'self'",
      "connect-src": "ipc: http://ipc.localhost",
      "object-src": "'none'",
      "base-uri": "'self'",
      "form-action": "'self'",
      "frame-ancestors": "'none'"
    },
    "freezePrototype": true
  }
}

References
Tauri CSP Documentation
Tauri Security Overview
Tauri SecurityConfig Reference
Weekly Installs
57
Repository
dchuk/claude-co…i-skills
GitHub Stars
18
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass