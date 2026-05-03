---
rating: ⭐⭐
title: primitives
url: https://skills.sh/assistant-ui/skills/primitives
---

# primitives

skills/assistant-ui/skills/primitives
primitives
Installation
$ npx skills add https://github.com/assistant-ui/skills --skill primitives
Summary

Unstyled, composable chat UI components following Radix UI patterns for assistant-ui.

Eight core primitives cover threads, messages, composer input, action bars, branch picking, and attachments with granular sub-parts for full customization
Use AuiIf for conditional rendering based on thread state, message role, branch count, and running status
Content parts support text, images, tool calls, and reasoning blocks with custom component mapping
Primitives require AssistantRuntimeProvider context and ship unstyled; apply your own Tailwind or CSS classes for styling
SKILL.md
assistant-ui Primitives

Always consult assistant-ui.com/llms.txt for latest API.

Composable, unstyled components following Radix UI patterns.

References
./references/thread.md -- ThreadPrimitive deep dive
./references/composer.md -- ComposerPrimitive deep dive
./references/message.md -- MessagePrimitive deep dive
./references/action-bar.md -- ActionBarPrimitive deep dive
Import
import {
  AuiIf,
  ThreadPrimitive,
  ComposerPrimitive,
  MessagePrimitive,
  ActionBarPrimitive,
  BranchPickerPrimitive,
  AttachmentPrimitive,
  ThreadListPrimitive,
  ThreadListItemPrimitive,
} from "@assistant-ui/react";

Primitive Parts
Primitive	Key Parts
ThreadPrimitive	.Root, .Viewport, .Messages, .Empty, .ScrollToBottom
ComposerPrimitive	.Root, .Input, .Send, .Cancel, .Attachments
MessagePrimitive	.Root, .Parts/.Content, .If, .Error
ActionBarPrimitive	.Copy, .Edit, .Reload, .Speak, .FeedbackPositive, .FeedbackNegative, .ExportMarkdown
BranchPickerPrimitive	.Previous, .Next, .Number, .Count
Custom Thread Example
function CustomThread() {
  return (
    <ThreadPrimitive.Root className="flex flex-col h-full">
      <ThreadPrimitive.Empty>
        <div className="flex-1 flex items-center justify-center">
          Start a conversation
        </div>
      </ThreadPrimitive.Empty>

      <ThreadPrimitive.Viewport className="flex-1 overflow-y-auto p-4">
        <ThreadPrimitive.Messages components={{
          UserMessage: CustomUserMessage,
          AssistantMessage: CustomAssistantMessage,
        }} />
      </ThreadPrimitive.Viewport>

      <ComposerPrimitive.Root className="border-t p-4 flex gap-2">
        <ComposerPrimitive.Input className="flex-1 rounded-lg border px-4 py-2" />
        <ComposerPrimitive.Send className="bg-blue-500 text-white px-4 py-2 rounded-lg">
          Send
        </ComposerPrimitive.Send>
      </ComposerPrimitive.Root>
    </ThreadPrimitive.Root>
  );
}

Conditional Rendering

Prefer AuiIf for new code. Primitive .If components still exist but are deprecated.

<AuiIf condition={({ message }) => message.role === "user"}>
  User only
</AuiIf>
<AuiIf condition={({ thread }) => thread.isRunning}>
  Generating...
</AuiIf>
<AuiIf condition={({ message }) => message.branchCount > 1}>
  Has edit history
</AuiIf>

<AuiIf condition={({ thread }) => thread.isRunning}>
  <ComposerPrimitive.Cancel>Stop</ComposerPrimitive.Cancel>
</AuiIf>

<AuiIf condition={({ thread }) => thread.isEmpty}>No messages</AuiIf>

Content Parts
<MessagePrimitive.Content components={{
  Text: ({ part }) => <p>{part.text}</p>,
  Image: ({ part }) => <img src={part.image} alt="" />,
  ToolCall: ({ part }) => <div>Tool: {part.toolName}</div>,
  Reasoning: ({ part }) => <details><summary>Thinking</summary>{part.text}</details>,
}} />

Branch Picker
<MessagePrimitive.If hasBranches>
  <BranchPickerPrimitive.Root className="flex items-center gap-1">
    <BranchPickerPrimitive.Previous>←</BranchPickerPrimitive.Previous>
    <span><BranchPickerPrimitive.Number /> / <BranchPickerPrimitive.Count /></span>
    <BranchPickerPrimitive.Next>→</BranchPickerPrimitive.Next>
  </BranchPickerPrimitive.Root>
</MessagePrimitive.If>

Common Gotchas

Primitives not rendering

Wrap in AssistantRuntimeProvider
Ensure parent primitive provides context

Styles not applying

Primitives are unstyled by default
Add className and style with your app's Tailwind/CSS system
Weekly Installs
1.3K
Repository
assistant-ui/skills
GitHub Stars
14
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn