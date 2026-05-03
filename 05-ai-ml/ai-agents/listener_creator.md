---
title: listener-creator
url: https://skills.sh/anthropics/claude-agent-sdk-demos/listener-creator
---

# listener-creator

skills/anthropics/claude-agent-sdk-demos/listener-creator
listener-creator
Installation
$ npx skills add https://github.com/anthropics/claude-agent-sdk-demos --skill listener-creator
SKILL.md
Listener Creator

Creates TypeScript listener files that monitor email events and execute custom logic when conditions are met.

When to Use This Skill

Use this skill when the user wants to:

Get notifications about specific emails ("notify me when boss sends urgent emails")
Automatically handle certain emails ("auto-archive newsletters")
Monitor for patterns ("watch for package tracking emails")
Set up scheduled actions ("daily email summary at 9am")
Create custom email workflows
How Listeners Work

Listeners are TypeScript files in agent/custom_scripts/listeners/ that:

Export a config object defining the event type and metadata
Export a handler function that filters and processes events
Use ListenerContext methods to perform actions (notify, archive, star, etc.)

The system automatically loads enabled listeners and executes them when matching events occur.

Creating a Listener
1. Understand the User's Intent

Parse the user's request to identify:

Event type: What triggers this listener? (email_received, email_sent, email_starred, email_archived, email_labeled, scheduled_time)
Filter conditions: What specific emails/events to match? (sender, subject keywords, time-based)
Actions: What should happen? (notify, archive, star, mark as read, add label)
Priority: How urgent is this? (high/normal/low)
2. Choose an Event Type
// Available event types:
- "email_received"  // Most common - new email arrives
- "email_sent"      // User sends an email
- "email_starred"   // Email is starred
- "email_archived"  // Email is archived
- "email_labeled"   // Label added to email
- "scheduled_time"  // Time-based (cron) - requires scheduler setup

3. Write the Listener File

Create a file in agent/custom_scripts/listeners/ with this structure:

import type { ListenerConfig, Email, ListenerContext } from "../types";

export const config: ListenerConfig = {
  id: "unique_listener_id",           // kebab-case, descriptive
  name: "Human Readable Name",         // For UI display
  description: "What this does",       // Optional but helpful
  enabled: true,                       // Start enabled
  event: "email_received"              // Event type
};

export async function handler(email: Email, context: ListenerContext): Promise<void> {
  // 1. Basic filter (identity/sender only)
  if (!email.from.includes("example@email.com")) return;

  // 2. Use AI for intelligent classification (PREFERRED over keyword matching)
  const analysis = await context.callAgent<{ isUrgent: boolean; reason: string }>({
    prompt: `Is this email urgent?\nSubject: ${email.subject}\nBody: ${email.body.substring(0, 500)}`,
    schema: {
      type: "object",
      properties: {
        isUrgent: { type: "boolean" },
        reason: { type: "string" }
      },
      required: ["isUrgent", "reason"]
    },
    model: "haiku"
  });

  if (!analysis.isUrgent) return;

  // 3. Perform actions via context methods
  await context.notify(`Urgent email: ${email.subject}\n${analysis.reason}`, {
    priority: "high"
  });

  await context.starEmail(email.messageId);
}

4. File Naming Convention

Use kebab-case matching the listener's purpose:

boss-urgent-watcher.ts
auto-archive-newsletters.ts
package-tracking.ts
daily-summary.ts
5. Available Context Methods

The ListenerContext provides these methods:

// Notifications
await context.notify(message, { priority: "high" | "normal" | "low" });

// Email actions
await context.archiveEmail(emailId);
await context.starEmail(emailId);
await context.unstarEmail(emailId);
await context.markAsRead(emailId);
await context.markAsUnread(emailId);
await context.addLabel(emailId, "label-name");
await context.removeLabel(emailId, "label-name");

// AI-powered analysis
const result = await context.callAgent<ResultType>({
  prompt: "Your prompt with email content",
  schema: {
    type: "object",
    properties: { field: { type: "string" } },
    required: ["field"]
  },
  model: "haiku" // or "sonnet" or "opus"
});

Recommended Approach: AI-Powered Classification

Default to using context.callAgent() for intelligent decision-making instead of hard-coded keyword lists. This provides better accuracy and adaptability.

// PREFERRED: AI-based urgency detection
const analysis = await context.callAgent<{ isUrgent: boolean; reason: string }>({
  prompt: `Analyze if this email is urgent:
Subject: ${email.subject}
Body: ${email.body.substring(0, 500)}

Is this email urgent or time-sensitive? Consider context, not just keywords.`,

  schema: {
    type: "object",
    properties: {
      isUrgent: { type: "boolean" },
      reason: { type: "string" }
    },
    required: ["isUrgent", "reason"]
  },
  model: "haiku" // Fast and cost-effective
});

if (analysis.isUrgent) {
  await context.notify(`Urgent: ${email.subject}\n${analysis.reason}`);
}

// AVOID: Hard-coded keyword lists (brittle and prone to false positives)
// const isUrgent = subject.includes("urgent") || subject.includes("asap");

Examples and Templates

Reference the template files for common patterns:

ai-classifier.ts: ⭐ AI-powered email classification (RECOMMENDED)
urgent-watcher.ts: AI-based urgent email detection
auto-archive.ts: Automatically archives newsletters
package-tracker.ts: Package tracking with status extraction
Best Practices
Prefer AI Classification: Use context.callAgent() instead of hard-coded keyword lists for intelligent decision-making
Filter Early: Return early if email doesn't match basic criteria (like sender)
Clear IDs: Use descriptive, unique listener IDs
Error Handling: Wrap context method calls in try-catch when appropriate
Performance: Use "haiku" model for fast AI classification (< 1 second typical)
Notify Wisely: Only notify when truly important
Avoid Hard-Coded Lists: Let AI determine urgency, importance, or categories instead of keyword matching
Type Imports

Always import types from the correct location:

import type { ListenerConfig, Email, ListenerContext } from "../types";

// For scheduled listeners:
import type { ListenerConfig, ListenerContext } from "../types";

// For labeled event:
import type { ListenerConfig, Email, ListenerContext } from "../types";

Common Patterns
AI-Powered (PREFERRED)

Basic filter (sender/type) → Call AI agent for intelligent classification → Act on AI result → Notify if important

This is the recommended approach for most listeners as it:

Avoids brittle keyword matching
Adapts to nuanced language and context
Makes better decisions about urgency and categorization
Reduces false positives
Simple Notification (Use sparingly)

Basic filter (sender only) → Notify → Optional star/label

Only use this when: The trigger is purely identity-based (e.g., "notify me about ALL emails from X")

Auto-Archive

Basic filter → Archive → Mark as read → Optional notify

Scheduled

Run at specific time → Query emails → Analyze → Send summary

Creating the File

When the user requests a listener:

Ask clarifying questions if the intent is unclear:

Who is the sender? What keywords?
What action should happen?
How urgent is this?

Choose the right event type (usually email_received)

Write the TypeScript file in agent/custom_scripts/listeners/

Use Write tool to create the file with:

Proper imports
Descriptive config
Handler with early filtering
Appropriate context method calls

Return listener reference in markdown format using [listener:filename.ts] notation (e.g., [listener:boss-urgent-watcher.ts]) for easy parsing and linking in the UI

Confirm with user that the listener matches their intent

Output Format Example

When presenting a created listener to the user, use this format:

Created listener: [listener:boss-urgent-watcher.ts]

This listener will:
- Monitor emails from boss@company.com
- Use AI to detect urgent emails (not just keywords)
- Send high-priority notifications for truly urgent emails
- Star emails that require immediate action

When to Use AI vs Simple Filtering

Use AI (context.callAgent()) when:

Detecting urgency, importance, or sentiment
Classifying email content or intent
Extracting structured data from email bodies
Making nuanced decisions based on context
Any logic that involves "understanding" the email content

Use simple filtering when:

Checking exact sender/recipient
Basic pattern matching on email fields (e.g., "from specific domain")
Identity-based triggers (e.g., "all emails from X person")

Default to AI unless the filter is purely identity-based.

Scheduled Listeners

For time-based actions (daily summaries, weekly reports):

export const config: ListenerConfig = {
  id: "daily_summary",
  name: "Daily Email Summary",
  enabled: true,
  event: "scheduled_time"
  // Note: Cron schedule configured separately in scheduler
};

export async function handler(
  data: { timestamp: Date },
  context: ListenerContext
): Promise<void> {
  // Your scheduled logic here
  await context.notify("Good morning! Your daily summary...");
}


Note: Scheduled listeners require cron scheduler configuration outside the listener file.

Reference

Full specification: See project root LISTENERS_SPEC.md for complete details on:

All event types
Complete type definitions
ListenersManager implementation
Advanced examples
Error handling patterns
Weekly Installs
69
Repository
anthropics/clau…dk-demos
GitHub Stars
2.3K
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn