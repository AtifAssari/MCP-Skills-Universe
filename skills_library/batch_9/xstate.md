---
title: xstate
url: https://skills.sh/vercel-labs/json-render/xstate
---

# xstate

skills/vercel-labs/json-render/xstate
xstate
Installation
$ npx skills add https://github.com/vercel-labs/json-render --skill xstate
SKILL.md
@json-render/xstate

XState Store adapter for json-render's StateStore interface. Wire an @xstate/store atom as the state backend for json-render.

Installation
npm install @json-render/xstate @json-render/core @json-render/react @xstate/store


Requires @xstate/store v3+.

Usage
import { createAtom } from "@xstate/store";
import { xstateStoreStateStore } from "@json-render/xstate";
import { StateProvider } from "@json-render/react";

// 1. Create an atom
const uiAtom = createAtom({ count: 0 });

// 2. Create the json-render StateStore adapter
const store = xstateStoreStateStore({ atom: uiAtom });

// 3. Use it
<StateProvider store={store}>
  {/* json-render reads/writes go through @xstate/store */}
</StateProvider>

API
xstateStoreStateStore(options)

Creates a StateStore backed by an @xstate/store atom.

Option	Type	Required	Description
atom	Atom<StateModel>	Yes	An @xstate/store atom (from createAtom) holding the json-render state model
Weekly Installs
395
Repository
vercel-labs/json-render
GitHub Stars
14.6K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass