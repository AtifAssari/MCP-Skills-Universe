---
title: mdx-sanitizer
url: https://skills.sh/erichowens/some_claude_skills/mdx-sanitizer
---

# mdx-sanitizer

skills/erichowens/some_claude_skills/mdx-sanitizer
mdx-sanitizer
Installation
$ npx skills add https://github.com/erichowens/some_claude_skills --skill mdx-sanitizer
SKILL.md
MDX Sanitizer

Comprehensive MDX content sanitizer that prevents JSX parsing errors caused by angle brackets, generics, and other conflicting patterns.

The Problem

MDX 2.x treats unescaped < and { as JSX syntax. This causes build failures when content contains:

TypeScript generics: Promise&lt;T&gt;, Array&lt;string&gt;, Map&lt;K, V&gt;
Comparisons: &lt;100ms, &lt;=, &gt;=
Arrows: --&gt;, &lt;--, -&gt;
Invalid tags: &lt;link&gt; in prose, &lt;tag&gt; placeholders
Empty brackets: &lt;&gt;
Solution Architecture

This skill implements a three-layer defense:

1. Sync-Time Sanitization (Proactive)

Content is sanitized when syncing from .claude/skills/ to website/docs/:

syncSkillDocs.ts - Main skill files
syncSkillSubpages.ts - Reference files
doc-generator.ts - Generated docs
2. Pre-Commit Validation (Reactive)

The git pre-commit hook validates files before commit using validate-brackets.js.

3. Build-Time Validation (Final Check)

npm run validate:all runs as part of prebuild to catch any issues.

Usage
Check for Issues (Dry Run)
cd website
npm run sanitize:mdx
# or with verbose output
npm run sanitize:mdx -- --verbose

Fix All Issues
cd website
npm run sanitize:mdx -- --fix
# or shorthand
npm run fix:mdx

Programmatic API
import { sanitizeForMdx, validateMdxSafety, isMdxSafe } from './lib/mdx-sanitizer';

// Sanitize content
const result = sanitizeForMdx(content, { useHtmlEntities: true });
if (result.modified) {
  console.log(`Fixed ${result.issues.length} issues`);
  fs.writeFileSync(path, result.content);
}

// Validate without modifying
const issues = validateMdxSafety(content, 'path/to/file.md');

// Quick check
if (!isMdxSafe(content)) {
  // Handle issues
}

Escaping Strategies

The sanitizer uses HTML entities for maximum compatibility:

Pattern	Original	Escaped
Less-than	<	&lt;
Greater-than	>	&gt;
Generics	&lt;T&gt;	&amp;lt;T&amp;gt;
Comparison	&lt;=	&amp;lt;=

Content inside code blocks (``` or `) is automatically protected and never escaped.

Files Modified
website/scripts/lib/mdx-sanitizer.ts - Core sanitizer module
website/scripts/sanitize-mdx.ts - CLI wrapper
website/scripts/syncSkillDocs.ts - Integration
website/scripts/syncSkillSubpages.ts - Integration
website/scripts/lib/doc-generator.ts - Integration
website/package.json - npm scripts
Patterns Detected
Less-than before digit: &lt;100, &lt;0.5ms
Comparison operators: &lt;=, &gt;=
Empty brackets: &lt;&gt;
Arrows: &lt;--, --&gt;
Generic types: Promise&lt;T&gt;, Array&lt;string&gt;
Space after less-than: &lt; value
Invalid pseudo-tags: &lt;link&gt;, &lt;tag&gt; (not valid HTML)
Troubleshooting
Build Still Fails After Running Sanitizer
Clear Docusaurus cache: npm run clear
Re-run sanitizer: npm run sanitize:mdx -- --fix
Rebuild: npm run build
False Positives

If valid JSX components are being escaped:

Ensure they use PascalCase (e.g., &lt;MyComponent&gt;)
Check they're valid HTML5 elements
Manual Escaping

For edge cases, manually escape in source:

Use backticks for inline code: `&lt;T&gt;`
Use fenced code blocks for multi-line
Use HTML entities: &lt; and &gt;
Sources
MDX Troubleshooting
TypeDoc MDX Issues
Weekly Installs
96
Repository
erichowens/some…e_skills
GitHub Stars
98
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass