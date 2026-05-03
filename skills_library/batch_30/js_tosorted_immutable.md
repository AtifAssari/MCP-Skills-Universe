---
title: js-tosorted-immutable
url: https://skills.sh/theorcdev/8bitcn-ui/js-tosorted-immutable
---

# js-tosorted-immutable

skills/theorcdev/8bitcn-ui/js-tosorted-immutable
js-tosorted-immutable
Installation
$ npx skills add https://github.com/theorcdev/8bitcn-ui --skill js-tosorted-immutable
SKILL.md
Use toSorted() Instead of sort() for Immutability

.sort() mutates the array in place, which can cause bugs with React Use .toSorted() to create a new sorted array without state and props. mutation.

Incorrect (mutates original array):

function UserList({ users }: { users: User[] }) {
  // Mutates the users prop array!
  const sorted = useMemo(
    () => users.sort((a, b) => a.name.localeCompare(b.name)),
    [users]
  )
  return <div>{sorted.map(renderUser)}</div>
}


Correct (creates new array):

function UserList({ users }: { users: User[] }) {
  // Creates new sorted array, original unchanged
  const sorted = useMemo(
    () => users.toSorted((a, b) => a.name.localeCompare(b.name)),
    [users]
  )
  return <div>{sorted.map(renderUser)}</div>
}


Why this matters in React:

Props/state mutations break React's immutability model - React expects props and state to be treated as read-only
Causes stale closure bugs - Mutating arrays inside closures (callbacks, effects) can lead to unexpected behavior

Browser support (fallback for older browsers):

.toSorted() is available in all modern browsers (Chrome 110+, Safari 16+, Firefox 115+, Node.js 20+). For older environments, use spread operator:

// Fallback for older browsers
const sorted = [...items].sort((a, b) => a.value - b.value)


Other immutable array methods:

.toSorted() - immutable sort
.toReversed() - immutable reverse
.toSpliced() - immutable splice
.with() - immutable element replacement
Weekly Installs
21
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