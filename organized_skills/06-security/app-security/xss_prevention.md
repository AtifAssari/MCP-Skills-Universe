---
rating: ⭐⭐
title: xss-prevention
url: https://skills.sh/aj-geddes/useful-ai-prompts/xss-prevention
---

# xss-prevention

skills/aj-geddes/useful-ai-prompts/xss-prevention
xss-prevention
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill xss-prevention
SKILL.md
XSS Prevention
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Implement comprehensive Cross-Site Scripting (XSS) prevention using input sanitization, output encoding, CSP headers, and secure coding practices.

When to Use
User-generated content display
Rich text editors
Comment systems
Search functionality
Dynamic HTML generation
Template rendering
Quick Start

Minimal working example:

// xss-prevention.js
const createDOMPurify = require("dompurify");
const { JSDOM } = require("jsdom");
const he = require("he");

const window = new JSDOM("").window;
const DOMPurify = createDOMPurify(window);

class XSSPrevention {
  /**
   * HTML Entity Encoding - Safest for text content
   */
  static encodeHTML(str) {
    return he.encode(str, {
      useNamedReferences: true,
      encodeEverything: false,
    });
  }

  /**
   * Sanitize HTML - For rich content
   */
  static sanitizeHTML(dirty) {
    const config = {
      ALLOWED_TAGS: [
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Node.js XSS Prevention	Node.js XSS Prevention
Python XSS Prevention	Python XSS Prevention
React XSS Prevention	React XSS Prevention
Content Security Policy	Content Security Policy
Best Practices
✅ DO
Encode output by default
Use templating engines
Implement CSP headers
Sanitize rich content
Validate URLs
Use HTTPOnly cookies
Regular security testing
Use secure frameworks
❌ DON'T
Trust user input
Use innerHTML directly
Skip output encoding
Allow inline scripts
Use eval()
Mix contexts (HTML/JS)
Weekly Installs
271
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass