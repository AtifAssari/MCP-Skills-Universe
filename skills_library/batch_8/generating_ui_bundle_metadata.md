---
title: generating-ui-bundle-metadata
url: https://skills.sh/forcedotcom/afv-library/generating-ui-bundle-metadata
---

# generating-ui-bundle-metadata

skills/forcedotcom/afv-library/generating-ui-bundle-metadata
generating-ui-bundle-metadata
Installation
$ npx skills add https://github.com/forcedotcom/afv-library --skill generating-ui-bundle-metadata
SKILL.md
UI Bundle Metadata
Scaffolding a New UI Bundle

Use sf template generate ui-bundle to create new apps — not create-react-app, Vite, or other generic scaffolds.

Always pass --template reactbasic to scaffold a React-based bundle.

UI bundle name (-n): Alphanumerical only — no spaces, hyphens, underscores, or special characters.

Example:

sf template generate ui-bundle -n CoffeeBoutique --template reactbasic


After generation:

Replace all default boilerplate — "React App", "Vite + React", default <title>, placeholder text
Populate the home page with real content (landing section, banners, hero, navigation)
Update navigation and placeholders (see the building-ui-bundle-frontend skill)

Always install dependencies before running any scripts in the UI bundle directory.

UIBundle Bundle

A UIBundle bundle lives under uiBundles/<AppName>/ and must contain:

<AppName>.uibundle-meta.xml — filename must exactly match the folder name
A build output directory (default: dist/) with at least one file
Meta XML

Required fields: masterLabel, version (max 20 chars), isActive (boolean). Optional: description (max 255 chars).

ui-bundle.json

Optional file. Allowed top-level keys: outputDir, routing, headers.

Constraints:

Valid UTF-8 JSON, max 100 KB
Root must be a non-empty object (never {}, arrays, or primitives)

Path safety (applies to outputDir and routing.fallback): Reject backslashes, leading / or \, .. segments, null/control characters, globs (*, ?, **), and %. All resolved paths must stay within the bundle.

outputDir

Non-empty string referencing a subdirectory (not . or ./). Directory must exist and contain at least one file.

routing

If present, must be a non-empty object. Allowed keys: rewrites, redirects, fallback, trailingSlash, fileBasedRouting.

trailingSlash: "always", "never", or "auto"
fileBasedRouting: boolean
fallback: non-empty string satisfying path safety; target file must exist
rewrites: non-empty array of { route?, rewrite } objects — e.g., { "route": "/app/:path*", "rewrite": "/index.html" }
redirects: non-empty array of { route?, redirect, statusCode? } objects — statusCode must be 301, 302, 307, or 308
headers

Non-empty array of { source, headers: [{ key, value }] } objects.

Example:

{
  "routing": {
    "rewrites": [{ "route": "/app/:path*", "rewrite": "/index.html" }],
    "trailingSlash": "never"
  },
  "headers": [
    {
      "source": "/assets/**",
      "headers": [{ "key": "Cache-Control", "value": "public, max-age=31536000, immutable" }]
    }
  ]
}


Never suggest: {} as root, empty "routing": {}, empty arrays, [{}], "outputDir": ".", "outputDir": "./".

CSP Trusted Sites

Salesforce enforces Content Security Policy headers. Any external domain not registered as a CSP Trusted Site will be blocked (images won't load, API calls fail, fonts missing).

When to Create

Whenever the app references a new external domain: CDN images, external fonts, third-party APIs, map tiles, iframes, external stylesheets.

Steps
Identify external domains — extract the origin (scheme + host) from each external URL in the code
Check existing registrations — look in force-app/main/default/cspTrustedSites/
Map resource type to CSP directive:
Resource Type	Directive Field
Images	isApplicableToImgSrc
API calls (fetch, XHR)	isApplicableToConnectSrc
Fonts	isApplicableToFontSrc
Stylesheets	isApplicableToStyleSrc
Video / audio	isApplicableToMediaSrc
Iframes	isApplicableToFrameSrc

Always also set isApplicableToConnectSrc to true for preflight/redirect handling.

Create the metadata file — follow implementation/csp-metadata-format.md for the .cspTrustedSite-meta.xml format. Place in force-app/main/default/cspTrustedSites/.
Weekly Installs
430
Repository
forcedotcom/afv-library
GitHub Stars
242
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass