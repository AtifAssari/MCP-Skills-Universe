---
title: slack block kit
url: https://skills.sh/sixtysecondsapp/use60/slack-block-kit
---

# slack block kit

skills/sixtysecondsapp/use60/Slack Block Kit
Slack Block Kit
Installation
$ npx skills add https://github.com/sixtysecondsapp/use60 --skill 'Slack Block Kit'
SKILL.md
Available Context

@_platform-references/org-variables.md

Slack Block Kit for Sales Workflows

Build rich, interactive Slack messages using our typed Block Kit abstraction layer. Every sales notification, coaching digest, deal alert, and approval request flows through this system.

Architecture
Adapter/Skill → build{Type}Message(data) → SlackMessage { blocks, text }
                         ↓
              send-slack-message edge function
                         ↓
              Slack Web API (chat.postMessage)
                         ↓
              slack-interactive (button clicks)


Key file: supabase/functions/_shared/slackBlocks.ts (3000+ lines, 33+ builders) Delivery: supabase/functions/send-slack-message/index.ts Interactions: supabase/functions/slack-interactive/

Primitive Block Builders

All builders auto-truncate to Slack limits. See references/block-types-and-limits.md for full constraints.

Function	Purpose	Auto-truncation
header(text)	Title/alert	150 chars
section(text)	Markdown content	2800 chars
sectionWithFields(fields)	Key-value grid (2-col)	10 fields max
sectionWithButton(text, btn, actionId, value, style?)	Section + accessory button	
sectionWithImage(text, url, alt)	Section + image	
context(elements)	Metadata/footer	10 elements, 1900 chars
actions(buttons)	Action buttons	5 max (recommend 3)
divider()	Horizontal rule	
Message Builders (33+ types)

Each builder takes a typed Data interface and returns SlackMessage { blocks, text }.

Core Sales Messages
Builder	Interface	Use Case
buildMeetingPrepMessage	MeetingPrepData	Pre-meeting briefing with attendees, deal, talking points, risks
buildMeetingDebriefMessage	MeetingDebriefData	Post-call summary with sentiment, talk time, action items
buildDailyDigestMessage	DailyDigestData	Morning standup with meetings, tasks, insights
buildCoachingMicroFeedbackMessage	CoachingMicroFeedbackData	Per-meeting coaching: scores, insights, recommendations
buildWeeklyCoachingDigestMessage	WeeklyCoachingDigestData	Weekly coaching: trends, patterns, challenge
Deal Lifecycle
Builder	Interface	Use Case
buildDealRoomMessage	DealRoomData	Deal room creation
buildDealStageChangeMessage	DealStageChangeData	Pipeline movement
buildDealActivityMessage	DealActivityData	Activity logged
buildDealWonMessage	DealWonData	Win celebration
buildDealLostMessage	DealLostData	Loss notification + lessons
buildWinProbabilityChangeMessage	WinProbabilityChangeData	AI health shift
buildDealSnapshotMessage	DealSnapshotData	Deal health card
buildDealMomentumMessage	DealMomentumData	Velocity/momentum trends
HITL (Human-in-the-Loop)
Builder	Interface	Use Case
buildHITLApprovalMessage	HITLApprovalData	Approve/reject/edit for email drafts, follow-ups, proposals
buildHITLConfirmationMessage	HITLConfirmationData	Checkbox confirmation
buildHITLEditRequestMessage	HITLEditRequestData	Suggest edits
buildHITLActionedConfirmation	HITLActionedConfirmation	Action completed
Intelligence & Alerts
Builder	Interface	Use Case
buildMorningBriefMessage	MorningBriefData	Morning briefing
buildStaleDealAlertMessage	StaleDealAlertData	Stale deal warning
buildEmailReplyAlertMessage	EmailReplyAlertData	Email response alert
buildAccountSignalAlert	AccountSignalAlertData	Account signal
buildAccountIntelligenceDigest	AccountDigestData	Weekly account digest
Delivery via send-slack-message

The send-slack-message edge function accepts message_type + data and routes to the appropriate builder:

// From an orchestrator adapter:
await fetch(`${supabaseUrl}/functions/v1/send-slack-message`, {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${serviceKey}`,
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    org_id: state.event.org_id,
    user_id: state.event.user_id,
    message_type: 'coaching_digest',  // routes to builder
    data: { /* matches WeeklyCoachingDigestData */ },
  }),
});


Supported message_type values: meeting_briefing, coaching_digest, campaign_report

For message types not yet wired, call the builder directly and pass blocks to the function.

Design Principles

See references/sales-message-patterns.md for complete pattern library and references/visual-techniques.md for score displays and progress bars.

Lead with impact — Most important number or insight first
Max 3 buttons — 1 primary (green), 1-2 secondary (gray)
Fields for KPIs — Use sectionWithFields for metric grids
Context at bottom — Timestamps, attribution, metadata
Always set fallback text — Screen readers and notifications use text
Truncate before building — Use safeMrkdwn(), safeHeaderText() helpers
Dividers sparingly — Only between distinct content groups
Under 10 blocks for routine messages, up to 20 for weekly digests
Quality Check

Before delivering any Slack message:

 Top-level text field populated (accessibility + notifications)
 Header under 150 chars
 Section text under 3000 chars
 Max 3 buttons per actions block, 1 primary
 No value + url on the same button (URL buttons for external links)
 action_id follows convention: {domain}_{action}_{entityId}
 Emoji used for quick visual scanning, not as sole indicators
 Renders well on mobile (fields stack vertically)
Weekly Installs
–
Repository
sixtysecondsapp/use60
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass