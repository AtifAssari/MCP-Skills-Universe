---
rating: ⭐⭐
title: browser-extension-dev
url: https://skills.sh/phrazzld/claude-config/browser-extension-dev
---

# browser-extension-dev

skills/phrazzld/claude-config/browser-extension-dev
browser-extension-dev
Installation
$ npx skills add https://github.com/phrazzld/claude-config --skill browser-extension-dev
SKILL.md
Browser Extension Development

Manifest V3, minimal permissions, cross-browser first.

Manifest V3

Required for new extensions:

{
  "manifest_version": 3,
  "name": "My Extension",
  "version": "1.0.0",
  "permissions": ["storage"],
  "host_permissions": ["https://api.example.com/*"],
  "background": {
    "service_worker": "background.js"
  },
  "content_scripts": [{
    "matches": ["https://*.example.com/*"],
    "js": ["content.js"]
  }],
  "content_security_policy": {
    "extension_pages": "script-src 'self'; object-src 'none'"
  }
}

Minimal Permissions

Request only what you need. Justify each permission:

Permission	Use Case
storage	Save user preferences
activeTab	Access current tab on user action
scripting	Inject scripts programmatically
https://specific.com/*	Access specific API

Never: <all_urls> without documented justification.

Use optional permissions for non-core features:

chrome.permissions.request({
  origins: ['https://optional.com/*']
}, (granted) => {
  if (granted) enableFeature();
});

Message Passing

Always validate messages at boundaries:

// background.js
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  // Validate sender
  if (!sender.tab) return;

  // Validate message structure
  if (message.type !== 'FETCH_DATA') return;
  if (typeof message.url !== 'string') return;

  // Process safely
  fetchData(message.url).then(sendResponse);
  return true; // async response
});


Never trust data from content scripts without validation.

Cross-Browser Support
// Use webextension-polyfill for API normalization
import browser from 'webextension-polyfill';

// Feature detection
if (browser.storage?.sync) {
  await browser.storage.sync.set({ key: value });
} else {
  await browser.storage.local.set({ key: value });
}


Test on Chrome, Firefox, Safari, Edge.

Updates
Semantic versioning (MAJOR.MINOR.PATCH)
Changelog accessible in-extension
Gradual rollout for major changes
Highlight permission changes to users
Maintain backward compatibility
Preserve user data across versions
Anti-Patterns
<all_urls> permission hoarding
eval() or remote code execution
Trusting content script data without validation
Manifest V2 for new development
Chrome-only without cross-browser testing
Silent permission scope creep
Weekly Installs
30
Repository
phrazzld/claude-config
GitHub Stars
8
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass