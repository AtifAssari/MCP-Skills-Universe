---
title: react19-source-patterns
url: https://skills.sh/github/awesome-copilot/react19-source-patterns
---

# react19-source-patterns

skills/github/awesome-copilot/react19-source-patterns
react19-source-patterns
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill react19-source-patterns
SKILL.md
React 19 Source Migration Patterns

Reference for every source-file migration required for React 19.

Quick Reference Table
Pattern	Action	Reference
ReactDOM.render(...)	→ createRoot().render()	See references/api-migrations.md
ReactDOM.hydrate(...)	→ hydrateRoot(...)	See references/api-migrations.md
unmountComponentAtNode	→ root.unmount()	Inline fix
ReactDOM.findDOMNode	→ direct ref	Inline fix
forwardRef(...) wrapper	→ ref as direct prop	See references/api-migrations.md
Component.defaultProps = {}	→ ES6 default params	See references/api-migrations.md
useRef() no arg	→ useRef(null)	Inline fix add null
Legacy Context	→ createContext	→ api-migrations.md#legacy-context
String refs this.refs.x	→ createRef()	→ api-migrations.md#string-refs
import React from 'react' (unused)	Remove	Only if no React. usage in file
PropTypes Rule

Do not remove .propTypes assignments. The prop-types package still works as a standalone validator. React 19 only removes the built-in runtime checking from the React package the package itself remains valid.

Add this comment above any .propTypes block:

// NOTE: React 19 no longer runs propTypes validation at runtime.
// PropTypes kept for documentation and IDE tooling only.

Read the Reference

For full before/after code for each migration, read references/api-migrations.md. It contains the complete patterns including edge cases for forwardRef with useImperativeHandle, defaultProps null vs undefined behavior, and legacy context provider/consumer cross-file migrations.

Weekly Installs
540
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass