---
rating: ⭐⭐
title: event follow-up analyzer
url: https://skills.sh/sixtysecondsapp/use60/event-follow-up-analyzer
---

# event follow-up analyzer

skills/sixtysecondsapp/use60/Event Follow-Up Analyzer
Event Follow-Up Analyzer
Installation
$ npx skills add https://github.com/sixtysecondsapp/use60 --skill 'Event Follow-Up Analyzer'
SKILL.md
Available Context & Tools

@_platform-references/org-variables.md @_platform-references/capabilities.md

Event Follow-Up Analyzer
Why Post-Event Follow-Up is Critical

Events are the highest-ROI lead generation channel in B2B sales -- but only if the follow-up is executed well. The data is stark:

48% of event leads go completely cold within 5 days without any follow-up (Bizzabo, 2023). Nearly half of the leads you paid thousands to acquire evaporate because nobody sends an email.
The first rep to follow up wins 78% of the time (InsideSales.com / XANT). Speed is the single strongest predictor of event lead conversion.
Personalized follow-ups convert 4.5x better than generic "great meeting you" emails (HubSpot event marketing study). Referencing a specific conversation or topic discussed at the event is the minimum bar.
Only 20% of event leads receive follow-up within 24 hours (Marketo). The other 80% either get delayed batch emails or nothing at all.
Events generate 3x the pipeline of cold outbound -- but only when follow-up happens within 48 hours (SiriusDecisions). After 48 hours, event leads perform barely better than cold leads.

The math is simple: if you spend $10K on an event and meet 50 prospects, each lead cost $200. Every lead that goes cold without follow-up is $200 burned. This skill ensures zero waste.

The Follow-Up Timeline: When Minutes Matter
The Golden Window: 0-24 Hours Post-Event

This is when the event is freshest in everyone's mind. Connections feel warm. Context is vivid. Brain research shows that episodic memory (remembering specific interactions) decays exponentially -- what someone remembers clearly on Day 1, they struggle to recall by Day 3.

Target: Top-priority leads get personalized follow-up within 24 hours of the event ending.

The Silver Window: 24-48 Hours Post-Event

Still warm, but cooling. Most competitors haven't followed up yet (only 20% follow up within 24h), so you still have a differentiation window. The prospect still remembers the event but is back in their normal workflow.

Target: All warm leads get follow-up by hour 48.

The Bronze Window: 48-72 Hours Post-Event

The event is becoming a memory. The prospect has had 2-3 normal workdays since. Your follow-up needs a stronger hook than "great meeting you at [event]" because the emotional warmth has faded.

Target: Remaining nurture leads get follow-up by hour 72.

The Dead Zone: 5+ Days Post-Event

After 5 days, event context is nearly gone. A follow-up referencing the event feels stale. At this point, you're essentially doing cold outreach with slightly better context. Still worth doing, but the conversion rate drops dramatically.

Target: If you haven't followed up by Day 5, shift to a standard outreach approach. Mention the event briefly but lead with value.

Lead Prioritization Framework

See references/engagement-signals.md for the complete engagement signal scoring framework with signal weights, CRM multipliers, tier assignment logic, and worked examples.

Not all event contacts are equal. Prioritize based on engagement signals, not just job titles.

The Engagement Signal Hierarchy

Signals are ranked by strength of buying intent. Higher-ranked signals indicate a more engaged, more interested lead.

Tier 1: Active Engagement Signals (HOT -- follow up within 24 hours)
Signal	Why It Matters	Weight
Asked a specific question about ${company_name}'s product/service	Shows active evaluation, not passive attendance	10
Requested a demo, meeting, or follow-up during the event	Explicit buying intent -- they asked YOU	10
Visited your booth and spent 5+ minutes in conversation	Invested time = invested interest	9
Exchanged contact details and asked you to reach out	Gave permission and expressed desire	9
Mentioned a specific problem ${company_name}'s product solves	Pain is present and top-of-mind	8
Referenced budget, timeline, or decision process	They're thinking about buying, not just browsing	8
Tier 2: Moderate Engagement Signals (WARM -- follow up within 48 hours)
Signal	Why It Matters	Weight
Attended your session/talk/workshop	Chose to spend time on your topic	6
Stopped by your booth and picked up materials	Low-effort engagement but still intentional	5
Connected with you on LinkedIn during/after the event	Social signal of interest	5
Mentioned they use a competitor's product	Potential switch opportunity	5
Expressed interest in a related topic (not directly ${company_name}'s product)	Adjacent interest, needs nurturing	4
Their company fits your ICP (industry, size, tech stack)	Good fit even without explicit engagement	4
Tier 3: Passive Signals (NURTURE -- follow up within 72 hours)
Signal	Why It Matters	Weight
Attended the same event (general)	Shared context, minimal engagement	2
Appeared on the attendee list but no interaction	May not have visited your booth	2
Works at a target account but didn't engage	Account-level interest, person-level unknown	3
Downloaded event materials or recordings after the fact	Post-event engagement, but not live	3
Scoring Methodology

Sum the weights of all applicable signals for each contact:

Total Score	Priority Level	Follow-Up Timing
15+	HOT	Within 24 hours, personalized email + phone call
8-14	WARM	Within 48 hours, personalized email
4-7	NURTURE	Within 72 hours, batch personalized email
1-3	LOW	Within 1 week, add to nurture sequence
Existing CRM Data Multipliers

Cross-reference event contacts against CRM data. Existing relationships amplify priority:

CRM Status	Multiplier	Rationale
Existing open deal	2.0x	Event interaction provides new touchpoint for an active opportunity
Previous customer (churned)	1.5x	Event re-engagement could signal win-back opportunity
Contact at target account	1.5x	New entry point into a strategic account
In CRM but no deal	1.2x	Existing awareness, event provides re-engagement hook
Not in CRM	1.0x	Net new lead, standard scoring
Organization Context Integration

Use the Organization Context to make follow-ups feel like they come from ${company_name}, not a generic sales tool:

Brand voice: Match the organization's communication style when drafting emails. A consultative brand sounds different from a direct, challenger-style brand.
Value propositions: Reference specific ${company_name} value propositions from the Organization Context in bridge statements and CTAs.
Case studies: When a prospect's industry or challenge maps to an available case study in the Organization Context, use it as the value-add resource in follow-ups.
Differentiators: Use competitive differentiators from the Organization Context to craft stronger hooks, especially for prospects who mentioned competitor products at the event.
Personalization Methodology: The "Event Bridge" Technique

Generic follow-ups fail. Personalized follow-ups succeed. The "Event Bridge" technique connects three elements:

[Specific Event Moment] --> [Their Business Context] --> [Your Value Proposition]

Step 1: Reference the Specific Interaction

Do NOT write: "Great meeting you at [Event]!" DO write: "I enjoyed our conversation about [specific topic] at [Event]."

The more specific the reference, the stronger the connection. Specificity proves you were paying attention and that this is not a mass email.

Good references:

A question they asked during a session
A problem they described at your booth
A specific comment they made about their current tools
A mutual connection you discovered
Something they said about their team, goals, or challenges

If you didn't interact directly:

Reference their session attendance: "I saw you attended the session on [topic]"
Reference shared context: "As someone in [their role/industry], the session on [topic] likely resonated"
Reference event content: "The keynote on [topic] highlighted challenges that [their company] is probably navigating"
Step 2: Bridge to Their Business Context

Connect the event interaction to their specific business situation. This requires CRM data or research.

Bridge examples:

"You mentioned your team is evaluating new [category] tools -- that aligns with what we've been seeing across [their industry]"
"Given [their company]'s growth to [employee count] employees, the scaling challenges discussed in the [session] must feel very real"
"With [their company]'s recent [funding round / product launch / expansion], the timing for ${company_name}'s [value prop from Organization Context] seems particularly relevant"
Step 3: Offer Concrete Value

End with a specific, low-friction next step. Not "let me know if you want to chat" -- that puts the burden on them.

Strong CTAs:

"I put together a [case study / benchmark report / comparison guide] that addresses exactly what we discussed. Would it be helpful if I sent it over?"
"We helped [similar company] solve the exact challenge you described. I'd love to walk you through the 15-minute version -- would [day/time] work?"
"Based on our conversation, I think [specific feature/approach] could save your team [quantified time/money]. Want me to put together a quick analysis?"
Multi-Channel Follow-Up Strategy
Channel Selection by Lead Priority and Context
Priority	Primary Channel	Secondary Channel	Timing
HOT	Personalized email	Phone call same day	Email within 24h, call within 4h of email
HOT	LinkedIn message (if connected at event)	Email + phone	LinkedIn within 12h, email within 24h
WARM	Personalized email	LinkedIn connection request	Email within 48h, LinkedIn within 24h of email
NURTURE	Batch personalized email	LinkedIn connection request	Email within 72h
LOW	Add to nurture sequence	--	Sequence starts within 1 week
Channel-Specific Best Practices
Email Follow-Up
Subject line: Reference the event and be specific. "[Event Name] follow-up: [specific topic you discussed]"
Length: 3-5 sentences max for the first email. Respect inbox fatigue post-event (everyone is catching up).
Timing: Tuesday-Thursday, 8-10 AM in the prospect's timezone. Avoid Monday (inbox overload) and Friday (low engagement).
One CTA only: Do not ask them to read a case study AND book a meeting AND connect on LinkedIn. Pick one.
LinkedIn Follow-Up
Connection request note: Reference the event. "Hi [Name], enjoyed our chat about [topic] at [Event]. Would love to stay connected."
After connection: Wait 24 hours, then send a message with value (not a pitch). Share a relevant article, insight, or resource.
Engage with their content: Before sending a message, like or comment on one of their recent posts. This puts your name in front of them organically.
Phone Follow-Up (HOT leads only)
Timing: 24-48 hours after the email, or same day for the hottest leads.
Opening: "Hi [Name], this is [Your Name] from ${company_name}. We spoke at [Event] about [topic]. I wanted to follow up on our conversation."
Duration: Keep it under 5 minutes unless they want to go deeper. The goal is to schedule a proper meeting, not have the meeting on the phone.
Voicemail: If no answer, leave a 30-second voicemail referencing the event interaction and follow up with an email referencing the voicemail.
Email Templates by Engagement Level

Consult references/followup-templates.md for the full template library with 3 variants per tier, LinkedIn connection request templates, speaker follow-up templates, booth visitor templates, and virtual event templates.

HOT Lead Template (Specific Interaction)
Subject: [Event Name] -- following up on [specific topic]

Hi [First Name],

I really enjoyed our conversation at [Event] about [specific topic/challenge they mentioned]. [One sentence showing you listened and remember the detail.]

[Bridge to value: how ${company_name}'s product/service addresses what they described. Reference relevant value propositions from the Organization Context.]

I put together [specific deliverable] based on what we discussed. [Would it be helpful to walk through it in a quick 15-minute call? / Would you like me to send it over?]

[Suggest two specific time slots, or offer to send a calendar link.]

Best,
[Your Name]
[Title] | [Company]

WARM Lead Template (Session Attendance or Brief Interaction)
Subject: After [Event Name] -- [relevant insight or resource]

Hi [First Name],

Great connecting at [Event]! [Reference to specific moment -- session they attended, brief chat, or shared experience.]

[One insight or takeaway from the event that's relevant to their role/company.] I think this is particularly relevant for [their company] given [specific business context from CRM or research].

I've attached [resource: guide, case study, benchmark data] that digs deeper into this topic. [If they find it useful, suggest a natural next step.]

Would a quick 15-minute chat next week be worth your time to discuss how ${company_name} is helping [similar companies] with this?

Best,
[Your Name]

NURTURE Lead Template (Minimal Interaction, Batch-Personalized)
Subject: [Event Name] recap + [relevant resource]

Hi [First Name],

I hope you enjoyed [Event Name] as much as I did. [Reference a keynote, popular session, or event theme that they likely attended.]

One thing that stood out was [insight related to their industry or role]. At ${company_name}, we've been working on [brief, relevant capability] to help [target persona] with exactly this challenge.

I thought you might find this [resource] interesting: [link to content piece, recording, or guide].

If [topic] is on your radar, I'd love to compare notes. Feel free to grab a time here: [calendar link].

Best,
[Your Name]

Batch vs. Individual Follow-Up Decision Framework

With a large event attendee list, you cannot personalize every email to the same depth. Use this framework to decide how to allocate effort.

The 20/30/50 Rule
Top 20% (HOT leads): Fully individualized follow-up. Write each email from scratch. Include specific references to your conversation. Call them.
Middle 30% (WARM leads): Semi-personalized. Use a template but customize the opening line, the bridge, and the CTA based on their role and company.
Bottom 50% (NURTURE leads): Batch-personalized. Use a single template with merge fields for name, company, and event-specific references. Add to a nurture sequence.
Batch Personalization Techniques

Even batch emails should feel personal. Use these merge strategies:

Merge Field	Source	Example
{first_name}	Contact record	"Hi Sarah"
{company}	Contact record	"for Acme Corp"
{role_type}	Title parsing	"as a VP of Sales" or "as a marketing leader"
{industry_challenge}	Industry lookup	"managing pipeline velocity in SaaS"
{event_session}	Session attendance data	"the session on AI in sales"
{similar_company}	ICP matching	"companies like [similar customer]"
When to Switch from Batch to Individual

Escalate a nurture lead to individual treatment when:

They reply to the batch email (any reply = human response required)
They click through and engage with content (3+ page views or download)
They connect on LinkedIn in response to your outreach
CRM data reveals they're at a target account with an active opportunity
A colleague reports a separate interaction with the same person/company
Data Gathering (via execute_action)
Fetch contact records: execute_action("get_contact", { id: contact_id }) for each attendee -- get CRM data, deal associations, activity history
Fetch related deals: execute_action("get_deal", { name: company_name }) for each attendee's company -- check for open opportunities
Fetch company status: execute_action("get_company_status", { company_name }) -- relationship health, recent activity
Fetch recent activities: Check for prior touchpoints with each contact in the last 90 days
Cross-reference attendee list: Match event attendees against CRM contacts to identify net-new vs. existing
Output Contract

Return a SkillResult with:

data.event_summary: Object with:

event_name: Name of the event
event_date: Date of the event
total_attendees: Total number of contacts analyzed
priority_breakdown: { hot: count, warm: count, nurture: count, low: count }
existing_crm_contacts: Count of attendees already in CRM
new_contacts: Count of net-new contacts
days_since_event: Number of days elapsed since the event (urgency indicator)
follow_up_urgency: "critical" (0-24h), "high" (24-48h), "moderate" (48-72h), "low" (72h+)

data.priority_leads: Array of lead objects, sorted by priority score descending:

contact_id: string (CRM ID if exists, null if new)
name: string
title: string
company: string
email: string
priority: "hot" | "warm" | "nurture" | "low"
score: number (raw engagement score)
engagement_signals: string[] (specific interactions observed)
crm_status: "existing_deal" | "existing_contact" | "target_account" | "new"
existing_deal: { name, stage, amount } | null
reason: string (1-sentence explanation of why they're prioritized at this level)
recommended_channel: "email" | "linkedin" | "phone" | "sequence"
recommended_timing: "today" | "tomorrow" | "this_week" | "next_week"

data.followup_recommendations: Array of action objects:

contact_id: string
contact_name: string
action_type: "personalized_email" | "phone_call" | "linkedin_message" | "linkedin_connect" | "add_to_sequence" | "schedule_meeting"
timing: "within_24h" | "within_48h" | "within_72h" | "within_1_week"
channel: "email" | "phone" | "linkedin"
personalization_hook: string (specific reference to use in outreach)
suggested_message: string (draft message text)
cta: string (specific call-to-action to include)

data.email_drafts: Array of draft email objects for all HOT and WARM leads:

contact_id: string
to: string (contact email)
subject: string
body: string (full email body with personalization)
priority: "hot" | "warm"
template_type: "individual" | "semi_personalized" | "batch"
personalization_elements: string[] (what was personalized and why)

data.batch_sequence: Object for nurture leads:

sequence_name: Suggested name for the nurture sequence
template: Email template with merge fields
contacts: Array of contact IDs to add
cadence: Suggested send timing (e.g., "Day 1, Day 4, Day 8")

references: Links to CRM records, event details, related deals

Quality Checklist

Before returning the analysis, verify:

 Every HOT lead has a fully personalized email draft. No templates, no merge fields -- written specifically for that person.
 Every email references the specific event. Generic follow-ups with no event context are unacceptable.
 Personalization hooks are specific. "Great meeting you" is not personalization. "Your question about integrating with Salesforce CPQ" is.
 Timing recommendations account for days since event. If the event was 3 days ago, "within 72 hours" is already past. Adjust to "today" or "ASAP."
 CRM cross-reference was performed. Every contact was checked against CRM. Existing deals and relationships are surfaced.
 Priority scoring is justified. Each lead's priority has a clear reason based on engagement signals, not just job title.
 Email drafts have one CTA only. No emails asking for multiple actions. One clear next step.
 Subject lines are specific. No generic "[Event] follow-up" subjects. Include a topic or hook.
 Phone follow-up is reserved for HOT leads only. Do not recommend calling WARM or NURTURE leads -- it is too aggressive for their engagement level.
 Batch sequence is provided for NURTURE leads. These leads should not be forgotten, but they also should not receive the same effort as HOT leads.
 Net-new contacts are flagged for CRM creation. If a contact from the event is not in CRM, recommend creating a record.
 Email tone aligns with ${company_name} brand voice from Organization Context.
 Value propositions and case studies from Organization Context are referenced in bridge statements where they naturally fit the prospect's industry or challenge.
Error Handling
No attendee list provided

Ask the user: "Can you share the attendee list or tell me who you met at the event?" If they describe interactions verbally, extract contacts from the description and create the analysis. If no list is available, offer to search CRM for contacts associated with the event or contacts at companies known to have attended.

Event was more than 7 days ago

Flag urgency: "This event was [X] days ago. Standard follow-up windows have passed. Adjusting strategy for late follow-up." Modify recommendations:

Do NOT reference the event as the primary hook (too stale)
Lead with value or a relevant insight instead
Mention the event briefly as context, not as the opening
Increase emphasis on content/resource sharing over meeting requests
Contact has no email address

For contacts without email:

Check CRM for the email
Check if the contact's company domain is known (suggest finding the email via company email pattern)
Recommend LinkedIn as the primary channel instead
Flag: "Email not found for [Name]. Recommend LinkedIn outreach or finding email via [company domain]."
Contact is already in an active deal

Do NOT send a generic event follow-up to someone with an active deal. Instead:

Flag the existing deal and its stage
Recommend using the event interaction as a touchpoint in the existing deal's context
Suggest a follow-up that references both the event and the deal: "Great seeing you at [Event]. Wanted to touch base on [deal topic] as well."
Very large attendee list (100+ contacts)

For large lists, do not analyze every contact individually. Instead:

Cross-reference against CRM to identify known contacts (prioritize these)
Filter by ICP criteria (title, company size, industry)
Analyze the top 30 in detail
Provide batch recommendations for the rest
Flag: "Analyzed [X] contacts in detail, with batch recommendations for the remaining [Y]."
Multiple events in a short period

If the user has attended multiple events recently, ensure follow-up references the correct event for each contact. Cross-reference to avoid sending duplicate follow-ups to someone met at multiple events.

Attendee was a speaker or panelist

Speakers and panelists require a different approach. They are high-status contacts who receive many follow-ups post-event. Differentiate by:

Referencing a specific point from their talk (not just "great session")
Asking a thoughtful follow-up question about their topic
Offering genuine value (not just pitching)
Being concise -- speakers get more post-event email than anyone
Event was virtual (webinar, online summit)

Virtual events generate different engagement signals. Adjust the hierarchy:

Session attendance duration replaces "booth visit time"
Chat messages and Q&A participation replace in-person conversation
Polls and interactive responses are engagement signals
Post-event recording views replace follow-up booth visits
Guidelines
Speed is everything. The single most important variable in event follow-up is speed. Prioritize getting follow-ups out fast over making them perfect.
Personalization beats polish. A slightly rough email that references a specific conversation converts better than a perfectly polished generic template.
One CTA per email. Decision fatigue is real, especially post-event when prospects are catching up on work.
Reference the event, don't rely on it. The event is context, not the value proposition. ${company_name}'s product/service value should stand on its own.
Track everything in CRM. Every follow-up sent should be logged. Every response should update the contact status. Do not let event leads fall into a tracking black hole.
Plan the follow-up sequence before the event ends. The best reps draft their follow-up emails during the event while context is freshest. This skill should enable that speed.
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