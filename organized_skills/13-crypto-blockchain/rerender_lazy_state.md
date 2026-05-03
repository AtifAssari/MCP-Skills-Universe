---
rating: ⭐⭐
title: rerender-lazy-state
url: https://skills.sh/theorcdev/8bitcn-ui/rerender-lazy-state
---

# rerender-lazy-state

skills/theorcdev/8bitcn-ui/rerender-lazy-state
rerender-lazy-state
Installation
$ npx skills add https://github.com/theorcdev/8bitcn-ui --skill rerender-lazy-state
SKILL.md
Use Lazy State Initialization

Pass a function to useState for expensive initial values. Without the function form, the initializer runs on every render even though the value is only used once.

Incorrect (runs on every render):

function FilteredList({ items }: { items: Item[] }) {
  // buildSearchIndex() runs on EVERY render, even after initialization
  const [searchIndex, setSearchIndex] = useState(buildSearchIndex(items))
  const [query, setQuery] = useState('')

  // When query changes, buildSearchIndex runs again unnecessarily
  return <SearchResults index={searchIndex} query={query} />
}

function UserProfile() {
  // JSON.parse runs on every render
  const [settings, setSettings] = useState(
    JSON.parse(localStorage.getItem('settings') || '{}')
  )

  return <SettingsForm settings={settings} onChange={setSettings} />
}


Correct (runs only once):

function FilteredList({ items }: { items: Item[] }) {
  // buildSearchIndex() runs ONLY on initial render
  const [searchIndex, setSearchIndex] = useState(() => buildSearchIndex(items))
  const [query, setQuery] = useState('')

  return <SearchResults index={searchIndex} query={query} />
}

function UserProfile() {
  // JSON.parse runs only on initial render
  const [settings, setSettings] = useState(() => {
    const stored = localStorage.getItem('settings')
    return stored ? JSON.parse(stored) : {}
  })

  return <SettingsForm settings={settings} onChange={setSettings} />
}


Use lazy initialization when computing initial values from localStorage/sessionStorage, building data structures (indexes, maps), reading from the DOM, or performing heavy transformations.

For simple primitives (useState(0)), direct references (useState(props.value)), or cheap literals (useState({})), the function form is unnecessary.

Weekly Installs
20
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