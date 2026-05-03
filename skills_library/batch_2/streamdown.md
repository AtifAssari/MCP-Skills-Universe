---
title: streamdown
url: https://skills.sh/vercel/streamdown/streamdown
---

# streamdown

skills/vercel/streamdown/streamdown
streamdown
Installation
$ npx skills add https://github.com/vercel/streamdown --skill streamdown
Summary

Streaming-optimized React Markdown renderer with syntax highlighting, diagrams, math, and AI chat integration.

Supports four optional plugins: code syntax highlighting via Shiki (200+ languages), Mermaid diagrams, LaTeX math rendering, and CJK text support
Two rendering modes: streaming (with animated caret cursor for AI chat) and static (for blogs and documentation)
Built-in security features including link safety modals, HTML tag filtering, URL sanitization, and configurable element allowlists
Requires Tailwind CSS configuration via @source directive (v4) or content scanning (v3); integrates seamlessly with Vercel AI SDK and other streaming frameworks
Customizable via props for themes, components, controls, and styling through CSS variables and data attributes
SKILL.md
Streamdown

Streaming-optimized React Markdown renderer. Drop-in replacement for react-markdown with built-in streaming support, security, and interactive controls.

Quick Setup
1. Install
npm install streamdown


Optional plugins (install only what's needed):

npm install @streamdown/code @streamdown/mermaid @streamdown/math @streamdown/cjk

2. Configure Tailwind CSS (Required)

This is the most commonly missed step. Streamdown uses Tailwind for styling and the dist files must be scanned.

Tailwind v4 — add to globals.css:

@source "../node_modules/streamdown/dist/*.js";


Add plugin @source lines only for packages you have installed (omitting uninstalled plugins avoids Tailwind errors). See plugin pages for exact paths:

Code: @source "../node_modules/@streamdown/code/dist/*.js";
CJK: @source "../node_modules/@streamdown/cjk/dist/*.js";
Math: @source "../node_modules/@streamdown/math/dist/*.js";
Mermaid: @source "../node_modules/@streamdown/mermaid/dist/*.js";

Tailwind v3 — add to tailwind.config.js:

module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./node_modules/streamdown/dist/*.js",
  ],
};

3. Basic Usage
import { Streamdown } from 'streamdown';

<Streamdown>{markdown}</Streamdown>

4. With AI Streaming (Vercel AI SDK)
'use client';
import { useChat } from '@ai-sdk/react';
import { Streamdown } from 'streamdown';
import { code } from '@streamdown/code';

export default function Chat() {
  const { messages, input, handleInputChange, handleSubmit, isLoading } = useChat();

  return (
    <>
      {messages.map((msg, i) => (
        <Streamdown
          key={msg.id}
          plugins={{ code }}
          caret="block"
          isAnimating={isLoading && i === messages.length - 1 && msg.role === 'assistant'}
        >
          {msg.content}
        </Streamdown>
      ))}
      <form onSubmit={handleSubmit}>
        <input value={input} onChange={handleInputChange} disabled={isLoading} />
      </form>
    </>
  );
}

5. Static Mode (Blogs, Docs)
<Streamdown mode="static" plugins={{ code }}>
  {content}
</Streamdown>

Key Props
Prop	Type	Default	Purpose
children	string	—	Markdown content
mode	"streaming" | "static"	"streaming"	Rendering mode
plugins	{ code?, mermaid?, math?, cjk? }	—	Feature plugins
isAnimating	boolean	false	Streaming indicator
caret	"block" | "circle"	—	Cursor style
components	Components	—	Custom element overrides
controls	boolean | object	true	Interactive buttons
linkSafety	LinkSafetyConfig	{ enabled: true }	Link confirmation modal
shikiTheme	[light, dark]	['github-light', 'github-dark']	Code themes
className	string	—	Container class
allowedElements	string[]	all	Tag names to allow
disallowedElements	string[]	[]	Tag names to disallow
allowElement	AllowElement	—	Custom element filter
unwrapDisallowed	boolean	false	Keep children of disallowed elements
skipHtml	boolean	false	Ignore raw HTML
urlTransform	UrlTransform	defaultUrlTransform	Transform/sanitize URLs

For full API reference, see references/api.md.

Plugin Quick Reference
Plugin	Package	Purpose
Code	@streamdown/code	Syntax highlighting (Shiki, 200+ languages)
Mermaid	@streamdown/mermaid	Diagrams (flowcharts, sequence, etc.)
Math	@streamdown/math	LaTeX via KaTeX (requires CSS import)
CJK	@streamdown/cjk	Chinese/Japanese/Korean text support

Math requires CSS:

import 'katex/dist/katex.min.css';


For plugin configuration details, see references/plugins.md.

References

Use these for deeper implementation details:

references/api.md — Complete props, types, and interfaces
references/plugins.md — Plugin setup, configuration, and customization
references/styling.md — CSS variables, data attributes, custom components, theme examples
references/security.md — Hardening, link safety, custom HTML tags, production config
references/features.md — Carets, remend, static mode, controls, GFM, memoization, troubleshooting
Example Configurations

Copy and adapt from assets/examples/:

basic-streaming.tsx — Minimal AI chat with Vercel AI SDK
with-caret.tsx — Streaming with block caret cursor
full-featured.tsx — All plugins, carets, link safety, controls
static-mode.tsx — Blog/docs rendering
custom-security.tsx — Strict security for AI content
Common Gotchas
Tailwind styles missing — Add @source directive or content entry for node_modules/streamdown/dist/*.js
Math not rendering — Import katex/dist/katex.min.css
Caret not showing — Both caret prop AND isAnimating={true} are required
Copy buttons during streaming — Disabled automatically when isAnimating={true}
Link safety modal appearing — Enabled by default; disable with linkSafety={{ enabled: false }}
Shiki warning in Next.js — Install shiki explicitly, add to transpilePackages
allowedTags not working — Only works with default rehype plugins
Math uses $$ not $ — Single dollar is disabled by default to avoid currency conflicts
Weekly Installs
1.4K
Repository
vercel/streamdown
GitHub Stars
5.1K
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn