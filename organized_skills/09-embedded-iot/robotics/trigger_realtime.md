---
rating: ⭐⭐
title: trigger-realtime
url: https://skills.sh/triggerdotdev/skills/trigger-realtime
---

# trigger-realtime

skills/triggerdotdev/skills/trigger-realtime
trigger-realtime
Installation
$ npx skills add https://github.com/triggerdotdev/skills --skill trigger-realtime
Summary

Real-time task monitoring and streaming for Trigger.dev tasks across frontend and backend.

Subscribe to task runs with status updates, progress tracking, and output streaming via backend iterators or React hooks
Stream AI/LLM responses directly to React components using typed stream definitions that pipe OpenAI completions and other async iterables
Implement human-in-the-loop workflows with wait tokens that pause task execution until frontend approval or user input is received
Secure frontend access through scoped public tokens with fine-grained permissions (read-only, task-specific, time-limited) and trigger tokens for task initiation
SKILL.md
Trigger.dev Realtime

Subscribe to task runs and stream data in real-time from frontend and backend.

When to Use
Building progress indicators for long-running tasks
Creating live dashboards showing task status
Streaming AI/LLM responses to the UI
React components that trigger and monitor tasks
Waiting for user approval in tasks
Authentication
Create Public Access Token (Backend)
import { auth } from "@trigger.dev/sdk";

// Read-only token for specific runs
const publicToken = await auth.createPublicToken({
  scopes: {
    read: {
      runs: ["run_123"],
      tasks: ["my-task"],
    },
  },
  expirationTime: "1h",
});

// Pass this token to your frontend

Create Trigger Token (for frontend triggering)
const triggerToken = await auth.createTriggerPublicToken("my-task", {
  expirationTime: "30m",
});

Backend Subscriptions
import { runs, tasks } from "@trigger.dev/sdk";

// Trigger and subscribe
const handle = await tasks.trigger("my-task", { data: "value" });

for await (const run of runs.subscribeToRun(handle.id)) {
  console.log(`Status: ${run.status}`);
  console.log(`Progress: ${run.metadata?.progress}`);
  
  if (run.status === "COMPLETED") {
    console.log("Output:", run.output);
    break;
  }
}

// Subscribe to tagged runs
for await (const run of runs.subscribeToRunsWithTag("user-123")) {
  console.log(`Run ${run.id}: ${run.status}`);
}

// Subscribe to batch
for await (const run of runs.subscribeToBatch(batchId)) {
  console.log(`Batch run ${run.id}: ${run.status}`);
}

React Hooks
Installation
npm add @trigger.dev/react-hooks

Trigger Task from React
"use client";
import { useRealtimeTaskTrigger } from "@trigger.dev/react-hooks";
import type { myTask } from "../trigger/tasks";

function TaskTrigger({ accessToken }: { accessToken: string }) {
  const { submit, run, isLoading } = useRealtimeTaskTrigger<typeof myTask>(
    "my-task",
    { accessToken }
  );

  return (
    <div>
      <button 
        onClick={() => submit({ data: "value" })} 
        disabled={isLoading}
      >
        Start Task
      </button>
      
      {run && (
        <div>
          <p>Status: {run.status}</p>
          <p>Progress: {run.metadata?.progress}%</p>
          {run.output && <p>Result: {JSON.stringify(run.output)}</p>}
        </div>
      )}
    </div>
  );
}

Subscribe to Existing Run
"use client";
import { useRealtimeRun } from "@trigger.dev/react-hooks";
import type { myTask } from "../trigger/tasks";

function RunStatus({ runId, accessToken }: { runId: string; accessToken: string }) {
  const { run, error } = useRealtimeRun<typeof myTask>(runId, {
    accessToken,
    onComplete: (run) => {
      console.log("Completed:", run.output);
    },
  });

  if (error) return <div>Error: {error.message}</div>;
  if (!run) return <div>Loading...</div>;

  return (
    <div>
      <p>Status: {run.status}</p>
      <p>Progress: {run.metadata?.progress || 0}%</p>
    </div>
  );
}

Subscribe to Tagged Runs
"use client";
import { useRealtimeRunsWithTag } from "@trigger.dev/react-hooks";

function UserTasks({ userId, accessToken }: { userId: string; accessToken: string }) {
  const { runs } = useRealtimeRunsWithTag(`user-${userId}`, { accessToken });

  return (
    <ul>
      {runs.map((run) => (
        <li key={run.id}>{run.id}: {run.status}</li>
      ))}
    </ul>
  );
}

Realtime Streams (AI/LLM)
Define Stream (shared location)
// trigger/streams.ts
import { streams } from "@trigger.dev/sdk";

export const aiStream = streams.define<string>({
  id: "ai-output",
});

Pipe Stream in Task
import { task } from "@trigger.dev/sdk";
import { aiStream } from "./streams";

export const streamingTask = task({
  id: "streaming-task",
  run: async (payload: { prompt: string }) => {
    const completion = await openai.chat.completions.create({
      model: "gpt-4",
      messages: [{ role: "user", content: payload.prompt }],
      stream: true,
    });

    const { waitUntilComplete } = aiStream.pipe(completion);
    await waitUntilComplete();
  },
});

Read Stream in React
"use client";
import { useRealtimeStream } from "@trigger.dev/react-hooks";
import { aiStream } from "../trigger/streams";

function AIResponse({ runId, accessToken }: { runId: string; accessToken: string }) {
  const { parts, error } = useRealtimeStream(aiStream, runId, {
    accessToken,
    throttleInMs: 50,
  });

  if (error) return <div>Error: {error.message}</div>;
  if (!parts) return <div>Waiting for response...</div>;

  return <div>{parts.join("")}</div>;
}

Wait Tokens (Human-in-the-loop)
In Task
import { task, wait } from "@trigger.dev/sdk";

export const approvalTask = task({
  id: "approval-task",
  run: async (payload) => {
    // Process initial data
    const processed = await processData(payload);

    // Wait for human approval
    const approval = await wait.forToken<{ approved: boolean }>({
      token: `approval-${payload.id}`,
      timeoutInSeconds: 86400, // 24 hours
    });

    if (approval.approved) {
      return await finalizeData(processed);
    }
    
    throw new Error("Not approved");
  },
});

Complete Token from React
"use client";
import { useWaitToken } from "@trigger.dev/react-hooks";

function ApprovalButton({ tokenId, accessToken }: { tokenId: string; accessToken: string }) {
  const { complete } = useWaitToken(tokenId, { accessToken });

  return (
    <div>
      <button onClick={() => complete({ approved: true })}>
        Approve
      </button>
      <button onClick={() => complete({ approved: false })}>
        Reject
      </button>
    </div>
  );
}

Run Object Properties
Property	Description
id	Unique run identifier
status	QUEUED, EXECUTING, COMPLETED, FAILED, CANCELED
payload	Task input (typed)
output	Task result (typed, when completed)
metadata	Real-time updatable data
createdAt	Start timestamp
costInCents	Execution cost
Best Practices
Scope tokens narrowly — only grant necessary permissions
Set expiration times — don't use long-lived tokens
Use typed hooks — pass task types for proper inference
Handle errors — always check for errors in hooks
Throttle streams — use throttleInMs to control re-renders

See references/realtime.md for complete documentation.

Weekly Installs
1.2K
Repository
triggerdotdev/skills
GitHub Stars
25
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass