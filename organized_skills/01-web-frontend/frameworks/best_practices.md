---
rating: ⭐⭐⭐
title: best-practices
url: https://skills.sh/addyosmani/web-quality-skills/best-practices
---

# best-practices

skills/addyosmani/web-quality-skills/best-practices
best-practices
Installation
$ npx skills add https://github.com/addyosmani/web-quality-skills --skill best-practices
Summary

Modern web development standards covering security, compatibility, and code quality patterns.

Enforces HTTPS, Content Security Policy, and security headers to prevent XSS, clickjacking, and mixed-content vulnerabilities
Addresses browser compatibility through proper doctype, charset, viewport configuration, and feature detection instead of user-agent sniffing
Covers deprecated APIs (document.write, synchronous XHR, Application Cache) with modern replacements (dynamic script loading, fetch, Service Workers)
Includes code quality checks: valid HTML, semantic markup, error handling, memory cleanup, and passive event listeners for performance
Provides an audit checklist and tools (npm audit, SecurityHeaders.com, W3C Validator, Lighthouse) for systematic best-practices validation
SKILL.md
Best practices

Modern web development standards based on Lighthouse best practices audits. Covers security, browser compatibility, and code quality patterns.

Security
HTTPS everywhere

Enforce HTTPS:

<!-- ❌ Mixed content -->
<img src="http://example.com/image.jpg">
<script src="http://cdn.example.com/script.js"></script>

<!-- ✅ HTTPS only -->
<img src="https://example.com/image.jpg">
<script src="https://cdn.example.com/script.js"></script>

<!-- ✅ Protocol-relative (will use page's protocol) -->
<img src="//example.com/image.jpg">


HSTS Header:

Strict-Transport-Security: max-age=31536000; includeSubDomains; preload

Content Security Policy (CSP)
<!-- Basic CSP via meta tag -->
<meta http-equiv="Content-Security-Policy" 
      content="default-src 'self'; 
               script-src 'self' https://trusted-cdn.com; 
               style-src 'self' 'unsafe-inline';
               img-src 'self' data: https:;
               connect-src 'self' https://api.example.com;">

<!-- Better: HTTP header -->


CSP Header (recommended):

Content-Security-Policy: 
  default-src 'self';
  script-src 'self' 'nonce-abc123' https://trusted.com;
  style-src 'self' 'nonce-abc123';
  img-src 'self' data: https:;
  connect-src 'self' https://api.example.com;
  frame-ancestors 'self';
  base-uri 'self';
  form-action 'self';


Using nonces for inline scripts:

<script nonce="abc123">
  // This inline script is allowed
</script>

Security headers
# Prevent clickjacking
X-Frame-Options: DENY

# Prevent MIME type sniffing
X-Content-Type-Options: nosniff

# Enable XSS filter (legacy browsers)
X-XSS-Protection: 1; mode=block

# Control referrer information
Referrer-Policy: strict-origin-when-cross-origin

# Permissions policy (formerly Feature-Policy)
Permissions-Policy: geolocation=(), microphone=(), camera=()

No vulnerable libraries
# Check for vulnerabilities
npm audit
yarn audit

# Auto-fix when possible
npm audit fix

# Check specific package
npm ls lodash


Keep dependencies updated:

// package.json
{
  "scripts": {
    "audit": "npm audit --audit-level=moderate",
    "update": "npm update && npm audit fix"
  }
}


Known vulnerable patterns to avoid:

// ❌ Prototype pollution vulnerable patterns
Object.assign(target, userInput);
_.merge(target, userInput);

// ✅ Safer alternatives
const safeData = JSON.parse(JSON.stringify(userInput));

Input sanitization
// ❌ XSS vulnerable
element.innerHTML = userInput;
document.write(userInput);

// ✅ Safe text content
element.textContent = userInput;

// ✅ If HTML needed, sanitize
import DOMPurify from 'dompurify';
element.innerHTML = DOMPurify.sanitize(userInput);

Secure cookies
// ❌ Insecure cookie
document.cookie = "session=abc123";

// ✅ Secure cookie (server-side)
Set-Cookie: session=abc123; Secure; HttpOnly; SameSite=Strict; Path=/

Browser compatibility
Doctype declaration
<!-- ❌ Missing or invalid doctype -->
<HTML>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN">

<!-- ✅ HTML5 doctype -->
<!DOCTYPE html>
<html lang="en">

Character encoding
<!-- ❌ Missing or late charset -->
<html>
<head>
  <title>Page</title>
  <meta charset="UTF-8">
</head>

<!-- ✅ Charset as first element in head -->
<html>
<head>
  <meta charset="UTF-8">
  <title>Page</title>
</head>

Viewport meta tag
<!-- ❌ Missing viewport -->
<head>
  <title>Page</title>
</head>

<!-- ✅ Responsive viewport -->
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Page</title>
</head>

Feature detection
// ❌ Browser detection (brittle)
if (navigator.userAgent.includes('Chrome')) {
  // Chrome-specific code
}

// ✅ Feature detection
if ('IntersectionObserver' in window) {
  // Use IntersectionObserver
} else {
  // Fallback
}

// ✅ Using @supports in CSS
@supports (display: grid) {
  .container {
    display: grid;
  }
}

@supports not (display: grid) {
  .container {
    display: flex;
  }
}

Polyfills (when needed)
<!-- Load polyfills conditionally -->
<script>
  if (!('fetch' in window)) {
    document.write('<script src="/polyfills/fetch.js"><\/script>');
  }
</script>

<!-- Or use polyfill.io -->
<script src="https://polyfill.io/v3/polyfill.min.js?features=fetch,IntersectionObserver"></script>

Deprecated APIs
Avoid these
// ❌ document.write (blocks parsing)
document.write('<script src="..."></script>');

// ✅ Dynamic script loading
const script = document.createElement('script');
script.src = '...';
document.head.appendChild(script);

// ❌ Synchronous XHR (blocks main thread)
const xhr = new XMLHttpRequest();
xhr.open('GET', url, false); // false = synchronous

// ✅ Async fetch
const response = await fetch(url);

// ❌ Application Cache (deprecated)
<html manifest="cache.manifest">

// ✅ Service Workers
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js');
}

Event listener passive
// ❌ Non-passive touch/wheel (may block scrolling)
element.addEventListener('touchstart', handler);
element.addEventListener('wheel', handler);

// ✅ Passive listeners (allows smooth scrolling)
element.addEventListener('touchstart', handler, { passive: true });
element.addEventListener('wheel', handler, { passive: true });

// ✅ If you need preventDefault, be explicit
element.addEventListener('touchstart', handler, { passive: false });

Console & errors
No console errors
// ❌ Errors in production
console.log('Debug info'); // Remove in production
throw new Error('Unhandled'); // Catch all errors

// ✅ Proper error handling
try {
  riskyOperation();
} catch (error) {
  // Log to error tracking service
  errorTracker.captureException(error);
  // Show user-friendly message
  showErrorMessage('Something went wrong. Please try again.');
}

Error boundaries (React)
class ErrorBoundary extends React.Component {
  state = { hasError: false };
  
  static getDerivedStateFromError(error) {
    return { hasError: true };
  }
  
  componentDidCatch(error, info) {
    errorTracker.captureException(error, { extra: info });
  }
  
  render() {
    if (this.state.hasError) {
      return <FallbackUI />;
    }
    return this.props.children;
  }
}

// Usage
<ErrorBoundary>
  <App />
</ErrorBoundary>

Global error handler
// Catch unhandled errors
window.addEventListener('error', (event) => {
  errorTracker.captureException(event.error);
});

// Catch unhandled promise rejections
window.addEventListener('unhandledrejection', (event) => {
  errorTracker.captureException(event.reason);
});

Source maps
Production configuration
// ❌ Source maps exposed in production
// webpack.config.js
module.exports = {
  devtool: 'source-map', // Exposes source code
};

// ✅ Hidden source maps (uploaded to error tracker)
module.exports = {
  devtool: 'hidden-source-map',
};

// ✅ Or no source maps in production
module.exports = {
  devtool: process.env.NODE_ENV === 'production' ? false : 'source-map',
};

Performance best practices
Avoid blocking patterns
// ❌ Blocking script
<script src="heavy-library.js"></script>

// ✅ Deferred script
<script defer src="heavy-library.js"></script>

// ❌ Blocking CSS import
@import url('other-styles.css');

// ✅ Link tags (parallel loading)
<link rel="stylesheet" href="styles.css">
<link rel="stylesheet" href="other-styles.css">

Efficient event handlers
// ❌ Handler on every element
items.forEach(item => {
  item.addEventListener('click', handleClick);
});

// ✅ Event delegation
container.addEventListener('click', (e) => {
  if (e.target.matches('.item')) {
    handleClick(e);
  }
});

Memory management
// ❌ Memory leak (never removed)
const handler = () => { /* ... */ };
window.addEventListener('resize', handler);

// ✅ Cleanup when done
const handler = () => { /* ... */ };
window.addEventListener('resize', handler);

// Later, when component unmounts:
window.removeEventListener('resize', handler);

// ✅ Using AbortController
const controller = new AbortController();
window.addEventListener('resize', handler, { signal: controller.signal });

// Cleanup:
controller.abort();

Code quality
Valid HTML
<!-- ❌ Invalid HTML -->
<div id="header">
<div id="header"> <!-- Duplicate ID -->

<ul>
  <div>Item</div> <!-- Invalid child -->
</ul>

<a href="/"><button>Click</button></a> <!-- Invalid nesting -->

<!-- ✅ Valid HTML -->
<header id="site-header">
</header>

<ul>
  <li>Item</li>
</ul>

<a href="/" class="button">Click</a>

Semantic HTML
<!-- ❌ Non-semantic -->
<div class="header">
  <div class="nav">
    <div class="nav-item">Home</div>
  </div>
</div>
<div class="main">
  <div class="article">
    <div class="title">Headline</div>
  </div>
</div>

<!-- ✅ Semantic HTML5 -->
<header>
  <nav>
    <a href="/">Home</a>
  </nav>
</header>
<main>
  <article>
    <h1>Headline</h1>
  </article>
</main>

Image aspect ratios
<!-- ❌ Distorted images -->
<img src="photo.jpg" width="300" height="100">
<!-- If actual ratio is 4:3, this squishes the image -->

<!-- ✅ Preserve aspect ratio -->
<img src="photo.jpg" width="300" height="225">
<!-- Actual 4:3 dimensions -->

<!-- ✅ CSS object-fit for flexibility -->
<img src="photo.jpg" style="width: 300px; height: 200px; object-fit: cover;">

Permissions & privacy
Request permissions properly
// ❌ Request on page load (bad UX, often denied)
navigator.geolocation.getCurrentPosition(success, error);

// ✅ Request in context, after user action
findNearbyButton.addEventListener('click', async () => {
  // Explain why you need it
  if (await showPermissionExplanation()) {
    navigator.geolocation.getCurrentPosition(success, error);
  }
});

Permissions policy
<!-- Restrict powerful features -->
<meta http-equiv="Permissions-Policy" 
      content="geolocation=(), camera=(), microphone=()">

<!-- Or allow for specific origins -->
<meta http-equiv="Permissions-Policy" 
      content="geolocation=(self 'https://maps.example.com')">

Audit checklist
Security (critical)
 HTTPS enabled, no mixed content
 No vulnerable dependencies (npm audit)
 CSP headers configured
 Security headers present
 No exposed source maps
Compatibility
 Valid HTML5 doctype
 Charset declared first in head
 Viewport meta tag present
 No deprecated APIs used
 Passive event listeners for scroll/touch
Code quality
 No console errors
 Valid HTML (no duplicate IDs)
 Semantic HTML elements used
 Proper error handling
 Memory cleanup in components
UX
 No intrusive interstitials
 Permission requests in context
 Clear error messages
 Appropriate image aspect ratios
Tools
Tool	Purpose
npm audit	Dependency vulnerabilities
SecurityHeaders.com	Header analysis
W3C Validator	HTML validation
Lighthouse	Best practices audit
Observatory	Security scan
References
MDN Web Security
OWASP Top 10
Web Quality Audit
Weekly Installs
5.3K
Repository
addyosmani/web-…y-skills
GitHub Stars
1.8K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass