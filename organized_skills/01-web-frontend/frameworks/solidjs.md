---
rating: ⭐⭐⭐
title: solidjs
url: https://skills.sh/suryavirkapur/skills/solidjs
---

# solidjs

skills/suryavirkapur/skills/solidjs
solidjs
Installation
$ npx skills add https://github.com/suryavirkapur/skills --skill solidjs
SKILL.md
SolidJS Development

SolidJS is a declarative JavaScript library for building user interfaces with fine-grained reactivity. Unlike virtual DOM frameworks, Solid compiles templates to real DOM nodes and updates them with fine-grained reactions.

Core Principles
Components run once — Component functions execute only during initialization, not on every update
Fine-grained reactivity — Only the specific DOM nodes that depend on changed data update
No virtual DOM — Direct DOM manipulation via compiled templates
Signals are functions — Access values by calling: count() not count
Reactivity Primitives
Signals — Basic State
import { createSignal } from "solid-js";

const [count, setCount] = createSignal(0);

// Read value (getter)
console.log(count()); // 0

// Update value (setter)
setCount(1);
setCount(prev => prev + 1); // Functional update


Options:

const [value, setValue] = createSignal(initialValue, {
  equals: false, // Always trigger updates, even if value unchanged
  name: "debugName" // For devtools
});

Effects — Side Effects
import { createEffect } from "solid-js";

createEffect(() => {
  console.log("Count changed:", count());
  // Runs after render, re-runs when dependencies change
});


Key behaviors:

Initial run: after render, before browser paint
Subsequent runs: when tracked dependencies change
Never runs during SSR or hydration
Use onCleanup for cleanup logic
Memos — Derived/Cached Values
import { createMemo } from "solid-js";

const doubled = createMemo(() => count() * 2);

// Access like signal
console.log(doubled()); // Cached, only recalculates when count changes


Use memos when:

Derived value is expensive to compute
Derived value is accessed multiple times
You want to prevent downstream updates when result unchanged
Resources — Async Data
import { createResource } from "solid-js";

const [user, { mutate, refetch }] = createResource(userId, fetchUser);

// In JSX
<Show when={!user.loading} fallback={<Loading />}>
  <div>{user()?.name}</div>
</Show>

// Resource properties
user.loading   // boolean
user.error     // error if failed
user.state     // "unresolved" | "pending" | "ready" | "refreshing" | "errored"
user.latest    // last successful value

Stores — Complex State

For nested objects/arrays with fine-grained updates:

import { createStore } from "solid-js/store";

const [state, setState] = createStore({
  user: { name: "John", age: 30 },
  todos: []
});

// Path syntax updates
setState("user", "name", "Jane");
setState("todos", todos => [...todos, newTodo]);
setState("todos", 0, "completed", true);

// Produce for immer-like updates
import { produce } from "solid-js/store";
setState(produce(s => {
  s.user.age++;
  s.todos.push(newTodo);
}));


Store utilities:

produce — Immer-like mutations
reconcile — Diff and patch data (for API responses)
unwrap — Get raw non-reactive object
Components
Basic Component
import { Component } from "solid-js";

const MyComponent: Component<{ name: string }> = (props) => {
  return <div>Hello, {props.name}</div>;
};

Props Handling
import { splitProps, mergeProps } from "solid-js";

// Default props
const merged = mergeProps({ size: "medium" }, props);

// Split props (for spreading)
const [local, others] = splitProps(props, ["class", "onClick"]);
return <button class={local.class} {...others} />;


Props rules:

Props are reactive getters — don't destructure at top level
Use props.value in JSX, not const { value } = props
Children Helper
import { children } from "solid-js";

const Wrapper: Component = (props) => {
  const resolved = children(() => props.children);
  
  createEffect(() => {
    console.log("Children:", resolved());
  });
  
  return <div>{resolved()}</div>;
};

Control Flow Components
Show — Conditional Rendering
import { Show } from "solid-js";

<Show when={user()} fallback={<Login />}>
  {(user) => <Profile user={user()} />}
</Show>

For — List Rendering (keyed by reference)
import { For } from "solid-js";

<For each={items()} fallback={<Empty />}>
  {(item, index) => (
    <div>{index()}: {item.name}</div>
  )}
</For>


Note: index is a signal, item is the value.

Index — List Rendering (keyed by index)
import { Index } from "solid-js";

<Index each={items()}>
  {(item, index) => (
    <input value={item().text} />
  )}
</Index>


Note: item is a signal, index is the value. Better for primitive arrays or inputs.

Switch/Match — Multiple Conditions
import { Switch, Match } from "solid-js";

<Switch fallback={<Default />}>
  <Match when={state() === "loading"}>
    <Loading />
  </Match>
  <Match when={state() === "error"}>
    <Error />
  </Match>
  <Match when={state() === "success"}>
    <Success />
  </Match>
</Switch>

Dynamic — Dynamic Component
import { Dynamic } from "solid-js/web";

<Dynamic component={selected()} someProp="value" />

Portal — Render Outside DOM Hierarchy
import { Portal } from "solid-js/web";

<Portal mount={document.body}>
  <Modal />
</Portal>

ErrorBoundary — Error Handling
import { ErrorBoundary } from "solid-js";

<ErrorBoundary fallback={(err, reset) => (
  <div>
    Error: {err.message}
    <button onClick={reset}>Retry</button>
  </div>
)}>
  <RiskyComponent />
</ErrorBoundary>

Suspense — Async Loading
import { Suspense } from "solid-js";

<Suspense fallback={<Loading />}>
  <AsyncComponent />
</Suspense>

Context API
import { createContext, useContext } from "solid-js";

// Create context
const CounterContext = createContext<{
  count: () => number;
  increment: () => void;
}>();

// Provider component
export function CounterProvider(props) {
  const [count, setCount] = createSignal(0);
  
  return (
    <CounterContext.Provider value={{
      count,
      increment: () => setCount(c => c + 1)
    }}>
      {props.children}
    </CounterContext.Provider>
  );
}

// Consumer hook
export function useCounter() {
  const ctx = useContext(CounterContext);
  if (!ctx) throw new Error("useCounter must be used within CounterProvider");
  return ctx;
}

Lifecycle
import { onMount, onCleanup } from "solid-js";

function MyComponent() {
  onMount(() => {
    console.log("Mounted");
    const handler = () => {};
    window.addEventListener("resize", handler);
    
    onCleanup(() => {
      window.removeEventListener("resize", handler);
    });
  });
  
  return <div>Content</div>;
}

Refs
let inputRef: HTMLInputElement;

<input ref={inputRef} />
<input ref={(el) => { /* el is the DOM element */ }} />

Event Handling
// Standard events (lowercase)
<button onClick={handleClick}>Click</button>
<button onClick={(e) => handleClick(e)}>Click</button>

// Delegated events (on:)
<input on:input={handleInput} />

// Native events (on:) - not delegated
<div on:scroll={handleScroll} />

Routing (Solid Router)

See references/routing.md for complete routing guide.

Quick setup:

import { Router, Route } from "@solidjs/router";

<Router>
  <Route path="/" component={Home} />
  <Route path="/users/:id" component={User} />
  <Route path="*404" component={NotFound} />
</Router>

SolidStart

See references/solidstart.md for full-stack development guide.

Quick setup:

npm create solid@latest my-app
cd my-app && npm install && npm run dev

Common Patterns
Conditional Classes
import { clsx } from "clsx"; // or classList

<div class={clsx("base", { active: isActive() })} />
<div classList={{ active: isActive(), disabled: isDisabled() }} />

Batch Updates
import { batch } from "solid-js";

batch(() => {
  setName("John");
  setAge(30);
  // Effects run once after batch completes
});

Untrack
import { untrack } from "solid-js";

createEffect(() => {
  console.log(count()); // tracked
  console.log(untrack(() => other())); // not tracked
});

TypeScript
import type { Component, ParentComponent, JSX } from "solid-js";

// Basic component
const Button: Component<{ label: string }> = (props) => (
  <button>{props.label}</button>
);

// With children
const Layout: ParentComponent<{ title: string }> = (props) => (
  <div>
    <h1>{props.title}</h1>
    {props.children}
  </div>
);

// Event handler types
const handleClick: JSX.EventHandler<HTMLButtonElement, MouseEvent> = (e) => {
  console.log(e.currentTarget);
};

Project Setup
# Create new project
npm create solid@latest my-app

# With template
npx degit solidjs/templates/ts my-app

# SolidStart
npm create solid@latest my-app -- --template solidstart


vite.config.ts:

import { defineConfig } from "vite";
import solid from "vite-plugin-solid";

export default defineConfig({
  plugins: [solid()]
});

Anti-Patterns to Avoid

Destructuring props — Breaks reactivity

// ❌ Bad
const { name } = props;

// ✅ Good
props.name


Accessing signals outside tracking scope

// ❌ Won't update
console.log(count());

// ✅ Will update
createEffect(() => console.log(count()));


Forgetting to call signal getters

// ❌ Passes the function
<div>{count}</div>

// ✅ Passes the value
<div>{count()}</div>


Using array index as key — Use <For> for reference-keyed, <Index> for index-keyed

Side effects during render — Use createEffect or onMount

Weekly Installs
264
Repository
suryavirkapur/skills
GitHub Stars
1
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass