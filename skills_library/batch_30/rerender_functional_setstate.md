---
title: rerender-functional-setstate
url: https://skills.sh/theorcdev/8bitcn-ui/rerender-functional-setstate
---

# rerender-functional-setstate

skills/theorcdev/8bitcn-ui/rerender-functional-setstate
rerender-functional-setstate
Installation
$ npx skills add https://github.com/theorcdev/8bitcn-ui --skill rerender-functional-setstate
SKILL.md
Use Functional setState Updates

When updating state based on the current state value, use the functional update form of setState instead of directly referencing the state variable. This prevents stale closures, eliminates unnecessary dependencies, and creates stable callback references.

Incorrect (requires state as dependency):

function TodoList() {
  const [items, setItems] = useState(initialItems)

  // Callback must depend on items, recreated on every items change
  const addItems = useCallback((newItems: Item[]) => {
    setItems([...items, ...newItems])
  }, [items])  // items dependency causes recreations

  // Risk of stale closure if dependency is forgotten
  const removeItem = useCallback((id: string) => {
    setItems(items.filter(item => item.id !== id))
  }, [])  // Missing items dependency - will use stale items!

  return <ItemsEditor items={items} onAdd={addItems} onRemove={removeItem} />
}


The first callback is recreated every time items changes, which can cause child components to re-render unnecessarily. The second callback has a stale closure bug—it will always reference the initial items value.

Correct (stable callbacks, no stale closures):

function TodoList() {
  const [items, setItems] = useState(initialItems)

  // Stable callback, never recreated
  const addItems = useCallback((newItems: Item[]) => {
    setItems(curr => [...curr, ...newItems])
  }, [])  // No dependencies needed

  // Always uses latest state, no stale closure risk
  const removeItem = useCallback((id: string) => {
    setItems(curr => curr.filter(item => item.id !== id))
  }, [])  // Safe and stable

  return <ItemsEditor items={items} onAdd={addItems} onRemove={removeItem} />
}


Benefits:

Stable callback references - Callbacks don't need to be recreated when state changes
No stale closures - Always operates on the latest state value
Fewer dependencies - Simplifies dependency arrays and reduces memory leaks
Prevents bugs - Eliminates the most common source of React closure bugs

When to use functional updates:

Any setState that depends on the current state value
Inside useCallback/useMemo when state is needed
Event handlers that reference state
Async operations that update state

When direct updates are fine:

Setting state to a static value: setCount(0)
Setting state from props/arguments only: setName(newName)
State doesn't depend on previous value

Note: If your project has React Compiler enabled, the compiler can automatically optimize some cases, but functional updates are still recommended for correctness and to prevent stale closure bugs.

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