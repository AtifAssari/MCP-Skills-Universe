---
title: js-hoist-regexp
url: https://skills.sh/theorcdev/8bitcn-ui/js-hoist-regexp
---

# js-hoist-regexp

skills/theorcdev/8bitcn-ui/js-hoist-regexp
js-hoist-regexp
Installation
$ npx skills add https://github.com/theorcdev/8bitcn-ui --skill js-hoist-regexp
SKILL.md
Hoist RegExp Creation

Don't create RegExp inside render. Hoist to module scope or memoize with useMemo().

Incorrect (new RegExp every render):

function Highlighter({ text, query }: Props) {
  const regex = new RegExp(`(${query})`, 'gi')
  const parts = text.split(regex)
  return <>{parts.map((part, i) => ...)}</>
}


Correct (memoize or hoist):

const EMAIL_REGEX = /^[^\s@]+@[^\s@]+\.[^\s@]+$/

function Highlighter({ text, query }: Props) {
  const regex = useMemo(
    () => new RegExp(`(${escapeRegex(query)})`, 'gi'),
    [query]
  )
  const parts = text.split(regex)
  return <>{parts.map((part, i) => ...)}</>
}


Warning (global regex has mutable state):

Global regex (/g) has mutable lastIndex state:

const regex = /foo/g
regex.test('foo')  // true, lastIndex = 3
regex.test('foo')  // false, lastIndex = 0

Weekly Installs
22
Repository
theorcdev/8bitcn-ui
GitHub Stars
1.8K
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass