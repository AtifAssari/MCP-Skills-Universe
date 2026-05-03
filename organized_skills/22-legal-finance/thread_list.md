---
rating: ⭐⭐
title: thread-list
url: https://skills.sh/assistant-ui/skills/thread-list
---

# thread-list

skills/assistant-ui/skills/thread-list
thread-list
Installation
$ npx skills add https://github.com/assistant-ui/skills --skill thread-list
Summary

Multi-thread chat management with built-in and custom UI components for assistant-ui.

Requires useChatRuntime with AssistantCloud for thread persistence; local in-memory adapter available for development without cloud
Provides ThreadListPrimitive components for custom UI layouts, plus pre-built ThreadList component for quick integration
Thread operations include switching threads, creating new threads, renaming, archiving, and deleting via the useAui hook API
Built on assistant-ui's runtime system; consult assistant-ui.com/llms.txt for latest API compatibility
SKILL.md
assistant-ui Thread List

Always consult assistant-ui.com/llms.txt for latest API.

Manage multiple chat threads with built-in or custom UI.

References
./references/management.md -- Thread CRUD operations
./references/custom-ui.md -- Custom thread list UI
Quick Start

Thread list is available with useChatRuntime + cloud:

import { AssistantCloud } from "assistant-cloud";
import { useChatRuntime, AssistantChatTransport } from "@assistant-ui/react-ai-sdk";
import { AssistantRuntimeProvider } from "@assistant-ui/react";
import { ThreadList } from "@/components/assistant-ui/thread-list";
import { Thread } from "@/components/assistant-ui/thread";

const cloud = new AssistantCloud({
  baseUrl: process.env.NEXT_PUBLIC_ASSISTANT_BASE_URL,
  authToken: async () => getAuthToken(),
});

function Chat() {
  const runtime = useChatRuntime({
    transport: new AssistantChatTransport({ api: "/api/chat" }),
    cloud,
  });

  return (
    <AssistantRuntimeProvider runtime={runtime}>
      <div className="flex h-screen">
        <ThreadList className="w-64 border-r" />
        <Thread className="flex-1" />
      </div>
    </AssistantRuntimeProvider>
  );
}

Thread Operations
import { useAui, useAuiState } from "@assistant-ui/react";

const api = useAui();
const { threadIds, mainThreadId } = useAuiState((s) => ({
  threadIds: s.threads.threadIds,
  mainThreadId: s.threads.mainThreadId,
}));

// Switch to thread
api.threads().switchToThread(threadId);

// Create new thread
api.threads().switchToNewThread();

// Thread item operations
const item = api.threads().item({ id: threadId });
await item.rename("New Title");
await item.archive();
await item.delete();

Custom Thread List
import { ThreadListPrimitive, ThreadListItemPrimitive } from "@assistant-ui/react";

function CustomThreadList() {
  return (
    <ThreadListPrimitive.Root className="w-64">
      <ThreadListPrimitive.New className="w-full p-2 bg-blue-500 text-white">
        + New Chat
      </ThreadListPrimitive.New>

      <ThreadListPrimitive.Items>
        <ThreadListItemPrimitive.Root className="flex p-2 hover:bg-gray-100">
          <ThreadListItemPrimitive.Trigger className="flex-1">
            <ThreadListItemPrimitive.Title />
          </ThreadListItemPrimitive.Trigger>
          <ThreadListItemPrimitive.Archive>Archive</ThreadListItemPrimitive.Archive>
          <ThreadListItemPrimitive.Delete>Delete</ThreadListItemPrimitive.Delete>
        </ThreadListItemPrimitive.Root>
      </ThreadListPrimitive.Items>
    </ThreadListPrimitive.Root>
  );
}

Without Cloud (Local)
import {
  unstable_useRemoteThreadListRuntime as useRemoteThreadListRuntime,
  unstable_InMemoryThreadListAdapter as InMemoryThreadListAdapter,
} from "@assistant-ui/react";

const runtime = useRemoteThreadListRuntime({
  adapter: new InMemoryThreadListAdapter(),
  runtimeHook: () => useLocalRuntime({ model: myModel }),
});

Common Gotchas

ThreadList not showing

Pass cloud to runtime
Check authentication

Threads not persisting

Verify cloud connection
Check network requests
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