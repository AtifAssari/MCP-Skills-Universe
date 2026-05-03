---
rating: ⭐⭐
title: runtime
url: https://skills.sh/assistant-ui/skills/runtime
---

# runtime

skills/assistant-ui/skills/runtime
runtime
Installation
$ npx skills add https://github.com/assistant-ui/skills --skill runtime
Summary

State management and thread/message access layer for assistant-ui chat applications.

Provides three runtime types: AssistantRuntime for overall state, ThreadRuntime for current conversation, and ThreadListRuntime for managing multiple threads
Access state via useAuiState selectors and perform operations through useAui() API (append messages, cancel runs, edit/reload messages, query capabilities)
Emit and listen to lifecycle events: thread.runStart, thread.runEnd, composer.send, and thread.modelContextUpdate
Hierarchical runtime structure supports per-message and per-content-part operations, with built-in capability detection for cancel, edit, reload, copy, speak, and attachments
SKILL.md
assistant-ui Runtime

Always consult assistant-ui.com/llms.txt for latest API.

References
./references/local-runtime.md -- useLocalRuntime deep dive
./references/external-store.md -- useExternalStoreRuntime deep dive
./references/thread-list.md -- Thread list management
./references/state-hooks.md -- State access hooks
./references/types.md -- Type definitions
Runtime Hierarchy
AssistantRuntime
├── ThreadListRuntime (thread management)
│   ├── ThreadListItemRuntime (per-thread item)
│   └── ...
└── ThreadRuntime (current thread)
    ├── ComposerRuntime (input state)
    └── MessageRuntime[] (per-message)
        └── MessagePartRuntime[] (per-content-part)

State Access (Modern API)
import { useAui, useAuiState, useAuiEvent } from "@assistant-ui/react";

function ChatControls() {
  const api = useAui();
  const messages = useAuiState(s => s.thread.messages);
  const isRunning = useAuiState(s => s.thread.isRunning);

  useAuiEvent("composer.send", (e) => {
    console.log("Sent in thread:", e.threadId);
  });

  return (
    <div>
      <button onClick={() => api.thread().append({
        role: "user",
        content: [{ type: "text", text: "Hello!" }],
      })}>
        Send
      </button>
      {isRunning && (
        <button onClick={() => api.thread().cancelRun()}>Cancel</button>
      )}
    </div>
  );
}

Thread Operations
const api = useAui();
const thread = api.thread();

// Append message
thread.append({ role: "user", content: [{ type: "text", text: "Hello" }] });

// Cancel generation
thread.cancelRun();

// Get current state
const state = thread.getState();  // { messages, isRunning, ... }

Message Operations
const message = api.thread().message(0);  // By index

message.edit({ role: "user", content: [{ type: "text", text: "Updated" }] });
message.reload();

Events
useAuiEvent("thread.runStart", () => {});
useAuiEvent("thread.runEnd", () => {});
useAuiEvent("composer.send", ({ threadId }) => {
  console.log("Sent in thread:", threadId);
});
useAuiEvent("thread.modelContextUpdate", () => {});

Capabilities
const caps = useAuiState(s => s.thread.capabilities);
// { cancel, edit, reload, copy, speak, attachments }

Quick Reference
// Get messages
const messages = useAuiState(s => s.thread.messages);

// Check running state
const isRunning = useAuiState(s => s.thread.isRunning);

// Append message
api.thread().append({ role: "user", content: [{ type: "text", text: "Hi" }] });

// Cancel generation
api.thread().cancelRun();

// Edit message
api.thread().message(index).edit({ ... });

// Reload message
api.thread().message(index).reload();

Common Gotchas

"Cannot read property of undefined"

Ensure hooks are called inside AssistantRuntimeProvider

State not updating

Use selectors with useAuiState to prevent unnecessary re-renders

Messages array empty

Check runtime is configured
Verify API response format
Weekly Installs
1.2K
Repository
assistant-ui/skills
GitHub Stars
14
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass