---
title: markdoc-expert
url: https://skills.sh/x0y14/argent-skills/markdoc-expert
---

# markdoc-expert

skills/x0y14/argent-skills/markdoc-expert
markdoc-expert
Installation
$ npx skills add https://github.com/x0y14/argent-skills --skill markdoc-expert
SKILL.md
Markdoc Expert

Expert guide for building documentation sites and content experiences using Markdoc, the powerful Markdown-based authoring framework developed by Stripe.

When to Use
Creating documentation sites with Markdoc
Defining custom tags and nodes
Configuring schema validation and attributes
Working with variables and functions
Setting up React or HTML rendering
Integrating Markdoc with TypeScript
Building reusable content with partials
Customizing the transformation pipeline
Overview

Markdoc is a Markdown superset based on the CommonMark specification, designed to power Stripe's public documentation. It processes content in three stages:

Parse: Transform raw string into an Abstract Syntax Tree (AST)
Transform: Process AST with config object to create a renderable tree
Render: Generate final output (React, HTML, or custom format)
Installation and Setup
Basic Installation
npm install @markdoc/markdoc
# or
yarn add @markdoc/markdoc

With React
npm install @markdoc/markdoc react @types/react

TypeScript Configuration

Minimal tsconfig.json required:

{
  "compilerOptions": {
    "moduleResolution": "node",
    "target": "esnext",
    "esModuleInterop": true
  }
}

Basic Usage
import Markdoc from '@markdoc/markdoc';
import React from 'react';

const doc = `
# Welcome to Markdoc

{% callout type="note" %}
This is a custom callout tag.
{% /callout %}
`;

// Parse: string -> AST
const ast = Markdoc.parse(doc);

// Transform: AST -> Renderable tree
const content = Markdoc.transform(ast, config);

// Render: Renderable tree -> React elements
const rendered = Markdoc.renderers.react(content, React, { components });

Syntax Reference
Nodes (Markdown Elements)

Nodes are elements inherited from Markdown:

Node	Description	Attributes
document	Root document	frontmatter
heading	Headers (h1-h6)	level
paragraph	Text blocks	-
fence	Code blocks	content, language, process
image	Images	src, alt, title
link	Hyperlinks	href, title
list	Ordered/unordered lists	ordered
item	List items	-
blockquote	Quote blocks	-
strong	Bold text	-
em	Italic text	-
code	Inline code	-
hr	Horizontal rule	-
table	Tables	-
Tags (Custom Extensions)

Tags use {% %} syntax for custom functionality:

{% tagname attribute="value" %}
Content body
{% /tagname %}


Self-closing tags:

{% image src="/logo.svg" /%}

Annotations

Add attributes to nodes using annotations:

# Heading {% #custom-id .custom-class %}

![alt text](/image.png) {% width=500 %}

Variables

Reference variables with $ prefix:

Hello, {% $user.name %}!

{% if $flags.feature_enabled %}
New feature content here.
{% /if %}

Functions

Call functions in tags and attributes:

{% if equals($user.role, "admin") %}
Admin content
{% /if %}

{% if and($isLoggedIn, $hasPermission) %}
Protected content
{% /if %}

Debug: {% debug($variable) %}

Comments

Enable comments in tokenizer:

const tokenizer = new Markdoc.Tokenizer({ allowComments: true });

<!-- This is a comment -->

Built-in Tags
if/else - Conditional Rendering
{% if $user.loggedIn %}
Welcome back, {% $user.name %}!
{% else /%}
Please log in.
{% /if %}


Note: Markdoc treats only undefined, null, and false as falsy values (unlike JavaScript).

table - Rich Content Tables
{% table %}
* Heading 1
* Heading 2
---
* Row 1, Cell 1
* Row 1, Cell 2
---
* Row 2, Cell 1
* Row 2, Cell 2
{% /table %}

partial - Content Reuse
{% partial file="header.md" /%}

{% partial file="snippet.md" variables={sdk: "Ruby", version: 3} /%}

Built-in Functions
Function	Description	Example
equals	Strict equality check	equals($a, $b)
and	Logical AND	and($a, $b)
or	Logical OR	or($a, $b)
not	Logical NOT	not($value)
default	Fallback for undefined	default($value, "fallback")
debug	JSON serialize value	debug($variable)
Config Object

The config object controls transformation behavior:

import type { Config } from '@markdoc/markdoc';

const config: Config = {
  nodes: {
    // Custom node definitions
    heading: customHeadingSchema,
    fence: customFenceSchema,
  },
  tags: {
    // Custom tag definitions
    callout: calloutSchema,
    tabs: tabsSchema,
  },
  variables: {
    // Runtime variables
    user: { name: 'John', role: 'admin' },
    flags: { newFeature: true },
  },
  functions: {
    // Custom functions
    includes: includesFunction,
    uppercase: uppercaseFunction,
  },
  partials: {
    // Partial content mapping
    'header.md': headerAst,
  },
};

Creating Custom Tags
Tag Schema Definition
import type { Schema, Tag } from '@markdoc/markdoc';

export const callout: Schema = {
  render: 'Callout',
  children: ['paragraph', 'tag', 'list'],
  attributes: {
    type: {
      type: String,
      default: 'note',
      matches: ['note', 'warning', 'error', 'success'],
      description: 'The type of callout',
    },
    title: {
      type: String,
      required: false,
      description: 'Optional title for the callout',
    },
  },
  selfClosing: false,
  description: 'Display a callout/admonition block',
};

Schema Options Reference
Option	Type	Description
render	string	Component name to render
children	string[]	Allowed child node types
attributes	Record	Attribute definitions
slots	Record	Named slot definitions
selfClosing	boolean	Allow self-closing syntax
inline	boolean	Inline element
transform	function	Custom transform logic
validate	function	Custom validation logic
Attribute Options
interface SchemaAttribute {
  type?: ValidationType | ValidationType[];  // String, Number, Boolean, Array, Object
  render?: boolean | string;                  // How to render attribute
  default?: any;                              // Default value
  required?: boolean;                         // Is required
  matches?: RegExp | string[];                // Validation pattern
  validate?(value, config, name): ValidationError[];  // Custom validation
  errorLevel?: 'debug' | 'info' | 'warning' | 'error' | 'critical';
  description?: string;                       // Documentation
}

Complete Custom Tag Example
// tags/callout.ts
import type { Schema, Node, Config, RenderableTreeNodes } from '@markdoc/markdoc';
import { Tag } from '@markdoc/markdoc';

export const callout: Schema = {
  render: 'Callout',
  children: ['paragraph', 'tag', 'list', 'item'],
  attributes: {
    type: {
      type: String,
      default: 'note',
      matches: ['note', 'warning', 'error', 'success'],
      errorLevel: 'error',
    },
    title: {
      type: String,
      required: false,
    },
  },
  transform(node: Node, config: Config): RenderableTreeNodes {
    const attributes = node.transformAttributes(config);
    const children = node.transformChildren(config);

    return new Tag(
      this.render,
      {
        ...attributes,
        className: `callout callout-${attributes.type}`,
      },
      children
    );
  },
};

// React component
interface CalloutProps {
  type: 'note' | 'warning' | 'error' | 'success';
  title?: string;
  className?: string;
  children: React.ReactNode;
}

export function Callout({ type, title, className, children }: CalloutProps) {
  const icons = {
    note: 'info',
    warning: 'alert-triangle',
    error: 'x-circle',
    success: 'check-circle',
  };

  return (
    <div className={className}>
      <span className="callout-icon">{icons[type]}</span>
      {title && <div className="callout-title">{title}</div>}
      <div className="callout-content">{children}</div>
    </div>
  );
}

Creating Custom Nodes
Customizing Built-in Nodes
import type { Schema, Node, Config } from '@markdoc/markdoc';
import { Tag } from '@markdoc/markdoc';

// Custom heading with auto-generated IDs
export const heading: Schema = {
  children: ['inline'],
  attributes: {
    id: { type: String },
    level: { type: Number, required: true },
  },
  transform(node: Node, config: Config) {
    const attributes = node.transformAttributes(config);
    const children = node.transformChildren(config);

    // Generate ID from text content
    const id = attributes.id || generateSlug(children);

    return new Tag(
      `h${attributes.level}`,
      { id, className: 'heading' },
      children
    );
  },
};

function generateSlug(children: any[]): string {
  return children
    .filter((child) => typeof child === 'string')
    .join('')
    .toLowerCase()
    .replace(/\s+/g, '-')
    .replace(/[^\w-]/g, '');
}

Custom Fence (Code Block)
export const fence: Schema = {
  render: 'CodeBlock',
  attributes: {
    content: { type: String, render: false },
    language: { type: String },
    process: { type: Boolean, default: true },
    title: { type: String },
    highlight: { type: String },
  },
  transform(node: Node, config: Config) {
    const attributes = node.transformAttributes(config);

    // Parse highlight ranges (e.g., "1-3,5,7-9")
    const highlightLines = parseHighlight(attributes.highlight);

    return new Tag(this.render, {
      ...attributes,
      highlightLines,
    });
  },
};

Creating Custom Functions
import type { ConfigFunction } from '@markdoc/markdoc';

// Check if array includes value
export const includes: ConfigFunction = {
  parameters: {
    0: { type: Array, required: true },
    1: { required: true },
  },
  transform(parameters) {
    const [array, value] = Object.values(parameters);
    return Array.isArray(array) ? array.includes(value) : false;
  },
};

// Convert to uppercase
export const uppercase: ConfigFunction = {
  parameters: {
    0: { type: String, required: true },
  },
  transform(parameters) {
    const value = parameters[0];
    return typeof value === 'string' ? value.toUpperCase() : value;
  },
};

// Format date
export const formatDate: ConfigFunction = {
  parameters: {
    0: { type: String, required: true },
    1: { type: String, default: 'en-US' },
  },
  transform(parameters) {
    const [dateStr, locale] = Object.values(parameters);
    try {
      return new Date(dateStr).toLocaleDateString(locale);
    } catch {
      return dateStr;
    }
  },
};

// Register in config
const config = {
  functions: {
    includes,
    uppercase,
    formatDate,
  },
};

Rendering
React Rendering
import Markdoc from '@markdoc/markdoc';
import React from 'react';
import { Callout } from './components/Callout';
import { CodeBlock } from './components/CodeBlock';
import { Tabs, Tab } from './components/Tabs';

const components = {
  Callout,
  CodeBlock,
  Tabs,
  Tab,
};

function DocumentRenderer({ content }: { content: string }) {
  const ast = Markdoc.parse(content);
  const errors = Markdoc.validate(ast, config);

  if (errors.length > 0) {
    console.error('Validation errors:', errors);
  }

  const transformed = Markdoc.transform(ast, config);
  return Markdoc.renderers.react(transformed, React, { components });
}

HTML Rendering
import Markdoc from '@markdoc/markdoc';

function renderToHTML(content: string): string {
  const ast = Markdoc.parse(content);
  const transformed = Markdoc.transform(ast, config);
  return Markdoc.renderers.html(transformed);
}

Custom Renderer
function customRenderer(node: RenderableTreeNode): string {
  if (typeof node === 'string') {
    return escapeHtml(node);
  }

  if (node === null || typeof node !== 'object') {
    return String(node);
  }

  const { name, attributes, children } = node;
  const attrs = formatAttributes(attributes);
  const content = children.map(customRenderer).join('');

  if (selfClosingTags.has(name)) {
    return `<${name}${attrs} />`;
  }

  return `<${name}${attrs}>${content}</${name}>`;
}

Validation
Built-in Validation
import Markdoc from '@markdoc/markdoc';

const ast = Markdoc.parse(content);
const errors = Markdoc.validate(ast, config);

errors.forEach((error) => {
  console.log(`[${error.level}] ${error.message}`);
  if (error.location) {
    console.log(`  at line ${error.location.start.line}`);
  }
});

Custom Validation
export const restrictedTag: Schema = {
  render: 'RestrictedContent',
  attributes: {
    role: {
      type: String,
      required: true,
      matches: ['admin', 'editor', 'viewer'],
    },
  },
  validate(node: Node, config: Config) {
    const errors: ValidationError[] = [];
    const role = node.attributes.role;

    if (config.validation?.environment === 'production' && role === 'admin') {
      errors.push({
        id: 'restricted-role',
        level: 'error',
        message: 'Admin-only content not allowed in production',
        location: node.location,
      });
    }

    return errors;
  },
};

Advanced Patterns
Table of Contents Generation
interface TocEntry {
  id: string;
  title: string;
  level: number;
}

function extractToc(ast: Node): TocEntry[] {
  const toc: TocEntry[] = [];

  function walk(node: Node) {
    if (node.type === 'heading') {
      const text = extractText(node);
      const id = generateSlug(text);
      toc.push({
        id,
        title: text,
        level: node.attributes.level,
      });
    }

    if (node.children) {
      node.children.forEach(walk);
    }
  }

  walk(ast);
  return toc;
}

Frontmatter Processing
import Markdoc from '@markdoc/markdoc';
import yaml from 'js-yaml';

function parseWithFrontmatter(content: string) {
  const ast = Markdoc.parse(content);
  const frontmatter = ast.attributes.frontmatter
    ? yaml.load(ast.attributes.frontmatter)
    : {};

  return {
    ast,
    frontmatter,
    content: Markdoc.transform(ast, {
      ...config,
      variables: {
        ...config.variables,
        frontmatter,
      },
    }),
  };
}

Dynamic Imports with Partials
import Markdoc from '@markdoc/markdoc';
import fs from 'fs/promises';
import path from 'path';

async function loadPartials(dir: string): Promise<Record<string, Node>> {
  const partials: Record<string, Node> = {};
  const files = await fs.readdir(dir);

  for (const file of files) {
    if (file.endsWith('.md')) {
      const content = await fs.readFile(path.join(dir, file), 'utf-8');
      partials[file] = Markdoc.parse(content);
    }
  }

  return partials;
}

// Usage
const partials = await loadPartials('./partials');
const config = {
  partials,
  // ... other config
};

Slots for Complex Layouts
export const card: Schema = {
  render: 'Card',
  children: ['paragraph', 'tag', 'list'],
  slots: {
    header: {
      render: 'CardHeader',
      required: true,
    },
    footer: {
      render: 'CardFooter',
      required: false,
    },
  },
  attributes: {
    variant: {
      type: String,
      default: 'default',
    },
  },
};


Usage in Markdoc:

{% card variant="elevated" %}
{% slot "header" %}
# Card Title
{% /slot %}

Main content goes here.

{% slot "footer" %}
Footer content
{% /slot %}
{% /card %}

Next.js Integration
App Router Setup
// app/docs/[...slug]/page.tsx
import Markdoc from '@markdoc/markdoc';
import React from 'react';
import fs from 'fs/promises';
import path from 'path';
import { config, components } from '@/markdoc/config';

interface Props {
  params: { slug: string[] };
}

export default async function DocPage({ params }: Props) {
  const filePath = path.join(process.cwd(), 'content', ...params.slug) + '.md';
  const content = await fs.readFile(filePath, 'utf-8');

  const ast = Markdoc.parse(content);
  const transformed = Markdoc.transform(ast, config);

  return (
    <article className="prose">
      {Markdoc.renderers.react(transformed, React, { components })}
    </article>
  );
}

export async function generateStaticParams() {
  // Generate static paths from content directory
  const contentDir = path.join(process.cwd(), 'content');
  const files = await getMarkdownFiles(contentDir);

  return files.map((file) => ({
    slug: file.replace('.md', '').split('/'),
  }));
}

Markdoc Config File
// markdoc/config.ts
import type { Config } from '@markdoc/markdoc';
import { callout } from './tags/callout';
import { tabs, tab } from './tags/tabs';
import { codeBlock } from './tags/codeBlock';
import { heading } from './nodes/heading';
import { fence } from './nodes/fence';

export const config: Config = {
  nodes: {
    heading,
    fence,
  },
  tags: {
    callout,
    tabs,
    tab,
  },
  functions: {
    // Custom functions
  },
};

export { components } from './components';

Common Patterns
Error Boundaries for Rendering
import React, { Component, ErrorBoundary } from 'react';

interface Props {
  fallback: React.ReactNode;
  children: React.ReactNode;
}

class MarkdocErrorBoundary extends Component<Props, { hasError: boolean }> {
  state = { hasError: false };

  static getDerivedStateFromError() {
    return { hasError: true };
  }

  componentDidCatch(error: Error, errorInfo: React.ErrorInfo) {
    console.error('Markdoc rendering error:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return this.props.fallback;
    }
    return this.props.children;
  }
}

Live Preview Component
'use client';

import { useState, useMemo } from 'react';
import Markdoc from '@markdoc/markdoc';
import React from 'react';

export function MarkdocEditor({ initialContent = '' }) {
  const [content, setContent] = useState(initialContent);

  const rendered = useMemo(() => {
    try {
      const ast = Markdoc.parse(content);
      const errors = Markdoc.validate(ast, config);
      const transformed = Markdoc.transform(ast, config);

      return {
        content: Markdoc.renderers.react(transformed, React, { components }),
        errors,
      };
    } catch (error) {
      return {
        content: null,
        errors: [{ message: String(error), level: 'error' }],
      };
    }
  }, [content]);

  return (
    <div className="editor-container">
      <textarea
        value={content}
        onChange={(e) => setContent(e.target.value)}
        className="editor-input"
      />
      <div className="editor-preview">{rendered.content}</div>
      {rendered.errors.length > 0 && (
        <div className="editor-errors">
          {rendered.errors.map((err, i) => (
            <div key={i} className={`error-${err.level}`}>
              {err.message}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

Best Practices
Schema Design
Use descriptive names: Tag and attribute names should be self-documenting
Provide defaults: Always set sensible defaults for optional attributes
Validate early: Use the validate function to catch errors at parse time
Document thoroughly: Use the description field for all schemas and attributes
Performance
Cache parsed ASTs: Parsing is expensive, cache results when possible
Use static rendering: Pre-render at build time for static content
Lazy load components: Code-split large rendering components
Minimize transforms: Keep transform functions lightweight
Content Organization
Use partials for reuse: Extract common content into partials
Leverage frontmatter: Store metadata in frontmatter, not inline
Keep tags simple: Prefer composition over complex single tags
Use variables for configuration: Don't hardcode values in content
TypeScript Integration
Type your schemas: Use the Schema type from @markdoc/markdoc
Type component props: Match component props to tag attributes
Use strict mode: Enable strict TypeScript for better type safety
Export types: Export types for use in consuming applications
Debugging Tips
Inspect AST
const ast = Markdoc.parse(content);
console.log(JSON.stringify(ast, null, 2));

Debug Transform Output
const transformed = Markdoc.transform(ast, config);
console.log(JSON.stringify(transformed, null, 2));

Use Debug Function
{% debug($variable) %}

Validate Schema
const errors = Markdoc.validate(ast, config);
if (errors.length > 0) {
  console.table(errors);
}

References
Official Documentation: https://markdoc.dev/docs
GitHub Repository: https://github.com/markdoc/markdoc
Stripe Docs (built with Markdoc): https://stripe.com/docs
CommonMark Specification: https://commonmark.org
Next.js Integration: https://markdoc.dev/docs/nextjs
Weekly Installs
10
Repository
x0y14/argent-skills
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass