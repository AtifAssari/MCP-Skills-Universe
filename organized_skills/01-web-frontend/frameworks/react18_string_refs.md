---
rating: ⭐⭐⭐
title: react18-string-refs
url: https://skills.sh/github/awesome-copilot/react18-string-refs
---

# react18-string-refs

skills/github/awesome-copilot/react18-string-refs
react18-string-refs
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill react18-string-refs
SKILL.md
React 18 String Refs Migration

String refs (ref="myInput" + this.refs.myInput) were deprecated in React 16.3, warn in React 18.3.1, and are removed in React 19.

Quick Pattern Map
Pattern	Reference
Single ref on a DOM element	→ patterns.md#single-ref
Multiple refs in one component	→ patterns.md#multiple-refs
Refs in a list / dynamic refs	→ patterns.md#list-refs
Callback refs (alternative approach)	→ patterns.md#callback-refs
Ref passed to a child component	→ patterns.md#forwarded-refs
Scan Command
# Find all string ref assignments in JSX
grep -rn 'ref="' src/ --include="*.js" --include="*.jsx" | grep -v "\.test\."

# Find all this.refs accessors
grep -rn "this\.refs\." src/ --include="*.js" --include="*.jsx" | grep -v "\.test\."


Both should be migrated together - find the ref="name" and the this.refs.name accesses for each component as a pair.

The Migration Rule

Every string ref migrates to React.createRef():

Add refName = React.createRef(); as a class field (or in constructor)
Replace ref="refName" → ref={this.refName} in JSX
Replace this.refs.refName → this.refName.current everywhere

Read references/patterns.md for the full before/after for each case.

Weekly Installs
520
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