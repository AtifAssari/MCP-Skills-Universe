---
title: slack history query
url: https://skills.sh/sixtysecondsapp/use60/slack-history-query
---

# slack history query

skills/sixtysecondsapp/use60/Slack History Query
Slack History Query
Installation
$ npx skills add https://github.com/sixtysecondsapp/use60 --skill 'Slack History Query'
SKILL.md
Available Context & Tools

@_platform-references/org-variables.md @_platform-references/capabilities.md

Slack History Query
Goal

Answer "when did I last…" and "show my meetings…" questions from Slack with a clean timeline view. Context matters — people ask these questions when preparing for calls or catch-ups.

Intent Patterns
Last Interaction with a Contact

Triggered when contact_name is extracted from the message.

Search contacts by name (partial match, case-insensitive)
Search recent meetings where title or summary mentions the contact name
Show contact profile header + last meeting details

Response format:

Section: *Full Name* — Title at Company (if contact found in CRM)
Section: *Last Meeting:* Meeting Title — Day, Mon DD
Section (italic): truncated meeting summary (max 300 chars)
Context: "N more meetings in the past week" (if applicable)
Divider + link to full contact profile

No interaction found: "I couldn't find any recent interactions with [name]. Check the name or try their full name."

Meeting Schedule Query

Triggered when message contains: "meetings this week", "meetings today", "meetings tomorrow", "upcoming meetings", "next week"

Fetch meetings for the relevant time window
Filter for upcoming (future) vs. this week (all)
Show list of up to 8 meetings with time and attendee count

Response format:

Header: "Upcoming Meetings (N)" or "This Week's Meetings (N)"
Bullet list: • *Meeting Title* — Tue, Jan 15 2:30 PM (N attendees)
Context: "N more. View calendar" link if >8 meetings

No meetings: "No upcoming meetings scheduled." or "No meetings found this week."

General Recent Activity

Triggered when no specific contact is named and not a schedule query.

Fetch last 5 meetings + last 5 activities from the past 7 days
Merge and sort by date descending
Show unified timeline

Response format:

Section: "Recent Activity (Past 7 Days):"
Bullet list (up to 8 items):
Meetings: :calendar: *Meeting Title* — Tue, Jan 15
Activities: :clipboard: Activity Type — Subject — Jan 15

No activity: "No recent activity found this week."

Data Sources
Meetings: execute_action("list_meetings", { owner: slack_user_id, days_back: 7 })
Contacts: execute_action("search_contacts", { query: contact_name })
Activities: execute_action("list_activities", { owner: slack_user_id, days_back: 7 })
Date Formatting
Meeting dates: new Date(start_time).toLocaleDateString('en-US', { weekday: 'long', month: 'short', day: 'numeric' })
Schedule view: include time — { weekday: 'short', month: 'short', day: 'numeric', hour: 'numeric', minute: '2-digit' }
Activity dates: short format — Mon Jan 15
Response Constraints
Maximum 8 items in any timeline/list view
Meeting summaries: truncate to 300 characters
Attendee count: show as "(N attendees)" not raw number
Sort all timeline items by date descending (most recent first)
For upcoming meetings filter: use start_time > now comparison
Always include link to /calendar for schedule queries
Error Cases
No meetings in period: Context-appropriate plain text ("No meetings found this week." vs "No upcoming meetings scheduled.")
Contact not in CRM: Show meeting history anyway if meetings mention the name, without the contact profile block
No activities or meetings: "No recent activity found this week."
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