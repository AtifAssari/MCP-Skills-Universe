---
title: react-19
url: https://skills.sh/prowler-cloud/prowler/react-19
---

# react-19

skills/prowler-cloud/prowler/react-19
react-19
Installation
$ npx skills add https://github.com/prowler-cloud/prowler --skill react-19
SKILL.md
No Manual Memoization (REQUIRED)
// ✅ React Compiler handles optimization automatically
function Component({ items }) {
  const filtered = items.filter(x => x.active);
  const sorted = filtered.sort((a, b) => a.name.localeCompare(b.name));

  const handleClick = (id) => {
    console.log(id);
  };

  return <List items={sorted} onClick={handleClick} />;
}

// ❌ NEVER: Manual memoization
const filtered = useMemo(() => items.filter(x => x.active), [items]);
const handleClick = useCallback((id) => console.log(id), []);

Imports (REQUIRED)
// ✅ ALWAYS: Named imports
import { useState, useEffect, useRef } from "react";

// ❌ NEVER
import React from "react";
import * as React from "react";

Server Components First
// ✅ Server Component (default) - no directive
export default async function Page() {
  const data = await fetchData();
  return <ClientComponent data={data} />;
}

// ✅ Client Component - only when needed
"use client";
export function Interactive() {
  const [state, setState] = useState(false);
  return <button onClick={() => setState(!state)}>Toggle</button>;
}

When to use "use client"
useState, useEffect, useRef, useContext
Event handlers (onClick, onChange)
Browser APIs (window, localStorage)
use() Hook
import { use } from "react";

// Read promises (suspends until resolved)
function Comments({ promise }) {
  const comments = use(promise);
  return comments.map(c => <div key={c.id}>{c.text}</div>);
}

// Conditional context (not possible with useContext!)
function Theme({ showTheme }) {
  if (showTheme) {
    const theme = use(ThemeContext);
    return <div style={{ color: theme.primary }}>Themed</div>;
  }
  return <div>Plain</div>;
}

Actions & useActionState
"use server";
async function submitForm(formData: FormData) {
  await saveToDatabase(formData);
  revalidatePath("/");
}

// With pending state
import { useActionState } from "react";

function Form() {
  const [state, action, isPending] = useActionState(submitForm, null);
  return (
    <form action={action}>
      <button disabled={isPending}>
        {isPending ? "Saving..." : "Save"}
      </button>
    </form>
  );
}

ref as Prop (No forwardRef)
// ✅ React 19: ref is just a prop
function Input({ ref, ...props }) {
  return <input ref={ref} {...props} />;
}

// ❌ Old way (unnecessary now)
const Input = forwardRef((props, ref) => <input ref={ref} {...props} />);

Weekly Installs
346
Repository
prowler-cloud/prowler
GitHub Stars
13.7K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass