---
rating: ⭐⭐
title: rivetkit-client-react
url: https://skills.sh/rivet-dev/skills/rivetkit-client-react
---

# rivetkit-client-react

skills/rivet-dev/skills/rivetkit-client-react
rivetkit-client-react
Installation
$ npx skills add https://github.com/rivet-dev/skills --skill rivetkit-client-react
Summary

React client for connecting to Rivet Actors with hooks and realtime state management.

Create typed hooks with createRivetKit() and connect to actor instances using useActor() with keys and optional parameters
Subscribe to actor events with useEvent() and monitor connection lifecycle through connStatus and error states
Use createClient() for stateless one-off calls, actor discovery methods (get, getOrCreate, create, getForId), and low-level HTTP/WebSocket access
Supports compound array keys for hierarchical actor addressing, automatic environment variable configuration, and explicit error handling via ActorError
SKILL.md
RivetKit React Client

Use this skill when building React apps that connect to Rivet Actors with @rivetkit/react.

First Steps
Install the React client (latest: 2.2.0)
npm install @rivetkit/react@2.2.0

Create hooks with createRivetKit() and connect with useActor().
Error Handling Policy
Prefer fail-fast behavior by default.
Avoid try/catch unless absolutely needed.
If a catch is used, handle the error explicitly, at minimum by logging it.
Getting Started

See the React quickstart guide for getting started.

Install
Minimal Client
import { createRivetKit } from "@rivetkit/react";
import type { registry } from "./index";

const { useActor } = createRivetKit<typeof registry>({
  endpoint: "https://my-namespace:pk_...@api.rivet.dev",
});

function Counter() {
  const { connection, connStatus } = useActor({ name: "counter", key: ["my-counter"] });

  if (connStatus !== "connected" || !connection) return <div>Connecting...</div>;
  return <button onClick={() => connection.increment(1)}>+</button>;
}

import { actor, setup } from "rivetkit";

export const counter = actor({
  state: { count: 0 },
  actions: {
    increment: (c, x: number) => {
      c.state.count += x;
      c.broadcast("newCount", c.state.count);
      return c.state.count;
    },
  },
});

export const registry = setup({
  use: { counter },
});

registry.start();

Stateless vs Stateful
import { createRivetKit } from "@rivetkit/react";

const { useActor } = createRivetKit();

function Counter() {
  const counter = useActor({ name: "counter", key: ["my-counter"] });

  const increment = async () => {
    await counter.connection?.increment(1);
  };

  return <button onClick={increment}>+</button>;
}

// Stateless: use createClient for one-off calls (SSR or utilities)
import { createClient } from "rivetkit/client";

const client = createClient();
await client.counter.getOrCreate(["my-counter"]).increment(1);

Getting Actors
import { createRivetKit } from "@rivetkit/react";
import { createClient } from "rivetkit/client";

const { useActor } = createRivetKit();

function ChatRoom() {
  const room = useActor({ name: "chatRoom", key: ["room-42"] });
  return <div>{room.connStatus}</div>;
}

// For get/getOrCreate/create/getForId, use createClient
const client = createClient();
const handle = client.chatRoom.getOrCreate(["room-42"]);
const existing = client.chatRoom.get(["room-42"]);
const created = await client.game.create(["game-1"], { input: { mode: "ranked" } });
const byId = client.chatRoom.getForId("actor-id");
const resolvedId = await handle.resolve();

Connection Parameters
import { createRivetKit } from "@rivetkit/react";

const { useActor } = createRivetKit();

function Chat() {
  const chat = useActor({
    name: "chatRoom",
    key: ["general"],
    params: { authToken: "jwt-token-here" },
  });

  return <div>{chat.connStatus}</div>;
}

Subscribing to Events
import { createRivetKit } from "@rivetkit/react";

const { useActor } = createRivetKit();

function Chat() {
  const chat = useActor({ name: "chatRoom", key: ["general"] });

  chat.useEvent("message", (msg) => {
    console.log("message:", msg);
  });

  return null;
}

Connection Lifecycle
import { createRivetKit } from "@rivetkit/react";

const { useActor } = createRivetKit();

function CounterStatus() {
  const actor = useActor({ name: "counter", key: ["my-counter"] });

  if (actor.connStatus === "connected") {
    console.log("connected");
  }

  if (actor.error) {
    console.error(actor.error);
  }

  return null;
}

Low-Level HTTP & WebSocket

Use the JavaScript client for raw HTTP and WebSocket access:

import { createClient } from "rivetkit/client";

const client = createClient();
const handle = client.chatRoom.getOrCreate(["general"]);

const response = await handle.fetch("history");
const history = await response.json();

const ws = await handle.webSocket("stream");
ws.addEventListener("message", (event) => {
  console.log("message:", event.data);
});
ws.send("hello");

Calling from Backend

Use the JavaScript client on your backend (Node.js/Bun). See the JavaScript client docs.

Error Handling
import { ActorError } from "rivetkit/client";
import { createRivetKit } from "@rivetkit/react";

const { useActor } = createRivetKit();

function Profile() {
  const actor = useActor({ name: "user", key: ["user-123"] });

  const updateUsername = async () => {
    try {
      await actor.connection?.updateUsername("ab");
    } catch (error) {
      if (error instanceof ActorError) {
        console.log(error.code, error.metadata);
      }
    }
  };

  return <button onClick={updateUsername}>Update</button>;
}

Concepts
Keys

Keys uniquely identify actor instances. Use compound keys (arrays) for hierarchical addressing:

import { createRivetKit } from "@rivetkit/react";
import type { registry } from "./index";

const { useActor } = createRivetKit<typeof registry>("http://localhost:6420");

function ChatRoom() {
  const room = useActor({ name: "chatRoom", key: ["org-acme", "general"] });
  return <div>{room.connStatus}</div>;
}

import { actor, setup } from "rivetkit";

export const chatRoom = actor({
  state: { messages: [] as string[] },
  actions: {
    getRoomInfo: (c) => ({ org: c.key[0], room: c.key[1] }),
  },
});

export const registry = setup({
  use: { chatRoom },
});

registry.start();


Don't build keys with string interpolation like "org:${userId}" when userId contains user data. Use arrays instead to prevent key injection attacks.

Environment Variables

createRivetKit() (and the underlying createClient() instance) automatically read:

RIVET_ENDPOINT
RIVET_NAMESPACE
RIVET_TOKEN
RIVET_RUNNER

Defaults to http://localhost:6420 when unset. RivetKit runs on port 6420 by default.

Endpoint Format

Endpoints support URL auth syntax:

https://namespace:token@api.rivet.dev


You can also pass the endpoint without auth and provide RIVET_NAMESPACE and RIVET_TOKEN separately. For serverless deployments, use your app's /api/rivet URL. See Endpoints for details.

API Reference

Package: @rivetkit/react

createRivetKit - Create hooks for React
useActor - Hook for actor instances
Need More Than the Client?

If you need more about Rivet Actors, registries, or server-side RivetKit, add the main skill:

npx skills add rivet-dev/skills


Then use the rivetkit skill for backend guidance.

Weekly Installs
4.8K
Repository
rivet-dev/skills
GitHub Stars
14
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail