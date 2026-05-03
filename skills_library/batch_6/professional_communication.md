---
title: professional-communication
url: https://skills.sh/softaworks/agent-toolkit/professional-communication
---

# professional-communication

skills/softaworks/agent-toolkit/professional-communication
professional-communication
Installation
$ npx skills add https://github.com/softaworks/agent-toolkit --skill professional-communication
Summary

Frameworks and best practices for clear, professional communication across emails, team chat, meetings, and technical audiences.

Covers four core areas: the What-Why-How structure for organizing messages, email templates with subject line formulas, team messaging etiquette including the "no hello" principle, and strategies for translating technical concepts to non-technical audiences
Includes audience calibration guidance, jargon-to-plain-language translation examples, and clarity principles like active voice and eliminating filler words
Provides meeting communication templates for agendas, action items, and post-meeting summaries with time-boxing tips
Includes a pre-send communication checklist covering purpose clarity, audience fit, scannable formatting, and tone appropriateness
SKILL.md
Professional Communication
Overview

This skill provides frameworks and guidance for effective professional communication in software development contexts. Whether you're writing an email to stakeholders, crafting a team chat message, or preparing meeting agendas, these principles help you communicate clearly and build professional credibility.

Core principle: Effective communication isn't about proving how much you know - it's about ensuring your message is received and understood.

When to Use This Skill

Use this skill when:

Writing emails to teammates, managers, or stakeholders
Crafting team chat messages or async communications
Preparing meeting agendas or summaries
Translating technical concepts for non-technical audiences
Structuring status updates or reports
Improving clarity of written communication

Keywords: email, chat, teams, slack, discord, message, writing, communication, meeting, agenda, status update, report

Core Frameworks
The What-Why-How Structure

Use this universal framework to organize any professional message:

Component	Purpose	Example
What	State the topic/request clearly	"We need to delay the release by one week"
Why	Explain the reasoning	"Critical bug found in payment processing"
How	Outline next steps/action items	"QA will retest by Thursday; I'll update stakeholders Friday"

Apply to: Emails, status updates, meeting talking points, technical explanations

Three Golden Rules for Written Communication
Start with a clear subject/purpose - Recipients should immediately grasp what your message is about
Use bullets, headlines, and scannable formatting - Nobody wants a wall of text
Key messages first - Busy people appreciate efficiency; state your main point upfront
Audience Calibration

Before communicating, ask yourself:

Who are you writing to? (Technical peers, managers, stakeholders, customers)
What level of detail do they need? (High-level overview vs implementation details)
What's the value for them? (How does this affect their work/decisions?)
Email Best Practices
Subject Line Formula
Instead of	Try
"Project updates"	"Project X: Status Update and Next Steps"
"Question"	"Quick question: API rate limiting approach"
"FYI"	"FYI: Deployment scheduled for Tuesday 3pm"
Email Structure Template
**Subject:** [Project/Topic]: [Specific Purpose]

Hi [Name],

[1-2 sentences stating the key point or request upfront]

**Context/Background:**
- [Bullet point 1]
- [Bullet point 2]

**What I need from you:**
- [Specific action or decision needed]
- [Timeline if applicable]

[Optional: Brief next steps or follow-up plan]

Best,
[Your name]

Common Email Types
Type	Key Elements
Status Update	Progress summary, blockers, next steps, timeline
Request	Clear ask, context, deadline, why it matters
Escalation	Issue summary, impact, attempted solutions, needed decision
FYI/Announcement	What changed, who's affected, any required action

For templates: See references/email-templates.md

Team Messaging Etiquette

Note: Examples use Slack terminology, but these principles apply equally to Microsoft Teams, Discord, or any team messaging platform.

When to Use Chat vs Email
Use Chat	Use Email
Quick questions with short answers	Detailed documentation needing records
Real-time coordination	Formal communications to stakeholders
Informal team discussions	Messages requiring careful review
Time-sensitive updates	Complex explanations with multiple parts
Team Messaging Best Practices
Use threads - Keep main channels scannable; follow-ups go in threads
@mention thoughtfully - Don't notify people unnecessarily
Channel organization - Right channel for right topic
Be direct - "Can you review my PR?" beats "Hey, are you busy?"
Async-friendly - Write messages that don't require immediate response
The "No Hello" Principle

Instead of:

You: Hi
You: Are you there?
You: Can I ask you something?
[waiting...]


Try:

You: Hi Sarah - quick question about the deployment script.
     Getting a permission error on line 42. Have you seen this before?
     Here's the error: [paste error]

Technical vs Non-Technical Communication
When to Be Technical vs Accessible
Audience	Approach
Engineering peers	Technical details, code examples, architecture specifics
Technical managers	Balance of detail and high-level impact
Non-technical stakeholders	Business impact, analogies, outcomes over implementation
Customers	Plain language, what it means for them, avoid jargon
Three Strategies for Simplification
Start with the big picture before details - People process "why" before "how"
Simplify without losing accuracy - Use analogies; replace jargon with plain language
Know when to switch - Read the room; adjust based on questions and engagement
Jargon Translation Examples
Technical	Plain Language
"Microservices architecture"	"Our system is split into smaller, independent pieces that can scale separately"
"Asynchronous message processing"	"Tasks are queued and processed in the background"
"CI/CD pipeline"	"Automated process that tests and deploys our code"
"Database migration"	"Updating how our data is organized and stored"

For more examples: See references/jargon-simplification.md

Writing Clarity Principles
Active Voice Over Passive Voice

Active voice is clearer, more direct, and conveys authority:

Passive (avoid)	Active (prefer)
"A bug was identified by the team"	"The team identified a bug"
"The feature will be implemented"	"We will implement the feature"
"Errors were found during testing"	"Testing revealed errors"
Eliminate Filler Words
Instead of	Use
"At this point in time"	"Now"
"In the event that"	"If"
"Due to the fact that"	"Because"
"In order to"	"To"
"I just wanted to check if"	"Can you"
The "So What?" Test

After writing, ask: "So what? Why does this matter to the reader?"

If you can't answer clearly, restructure your message to lead with the value/impact.

Meeting Communication
Before: Agenda Best Practices

Every meeting invite should include:

Clear objective - What will be accomplished?
Agenda items - Topics to cover with time estimates
Preparation required - What should attendees bring/review?
Expected outcome - Decision needed? Information sharing? Brainstorm?
During: Facilitation Tips
Time-box discussions - "Let's spend 5 minutes on this, then move on"
Capture action items live - Who does what by when
Parking lot - Note off-topic items for later
After: Summary Format
**Meeting: [Topic] - [Date]**

**Attendees:** [Names]

**Key Decisions:**
- [Decision 1]
- [Decision 2]

**Action Items:**
- [ ] [Person]: [Task] - Due [Date]
- [ ] [Person]: [Task] - Due [Date]

**Next Steps:**
- [Follow-up meeting if needed]
- [Documents to share]


For structures by meeting type: See references/meeting-structures.md

Quick Reference: Communication Checklist

Before sending any professional communication:

 Clear purpose - Can the recipient understand intent in 5 seconds?
 Right audience - Is this the appropriate person/channel?
 Key message first - Is the main point upfront?
 Scannable - Are there bullets, headers, short paragraphs?
 Action clear - Does the recipient know what (if anything) they need to do?
 Jargon check - Will the audience understand all terminology?
 Tone appropriate - Is it professional but not cold?
 Proofread - Any typos or unclear phrasing?
Additional Tools
references/email-templates.md - Ready-to-use email templates by type
references/meeting-structures.md - Structures for standups, retros, reviews
references/jargon-simplification.md - Technical-to-plain-language translations
Companion Skills
feedback-mastery - For difficult conversations and feedback delivery
/draft-email - Generate emails using these frameworks

Last Updated: 2025-12-22

Version History
v1.0.0 (2025-12-26): Initial release
Weekly Installs
3.6K
Repository
softaworks/agent-toolkit
GitHub Stars
1.7K
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass