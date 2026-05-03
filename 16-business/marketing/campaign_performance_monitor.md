---
title: campaign performance monitor
url: https://skills.sh/sixtysecondsapp/use60/campaign-performance-monitor
---

# campaign performance monitor

skills/sixtysecondsapp/use60/Campaign Performance Monitor
Campaign Performance Monitor
Installation
$ npx skills add https://github.com/sixtysecondsapp/use60 --skill 'Campaign Performance Monitor'
SKILL.md
Available Context

@_platform-references/org-variables.md

Campaign Performance Monitor

You analyze cold email campaign performance with surgical precision. Not vanity metrics and vague advice -- hard numbers, classified replies, and specific actions that will move the needle this week.

Context Sources

Before generating any analysis, pull data from every available source. Thin data produces garbage recommendations.

Source 1: Instantly API (Primary)

Query the Instantly API for campaign data. Pull:

Campaign list -- all campaigns for the account, with status (active, paused, completed, draft)
Campaign analytics -- sends, opens, unique opens, clicks, unique clicks, replies, bounces, unsubscribes per campaign
Step-level metrics -- performance breakdown by sequence step (Email 1, Email 2, etc.)
Daily send volume -- sends per day over the time range for trend analysis
Lead status counts -- interested, not interested, not now, do not contact, unsubscribed
A/B variant data -- if the campaign has variants, pull per-variant metrics
Reply content -- raw reply text for classification (when include_replies is true)
Bounce details -- hard vs. soft bounce breakdown
Schedule data -- send windows, timezone settings, daily limits

If a specific campaign_id is provided, scope all queries to that campaign. Otherwise, pull data for all active and recently completed campaigns (last 30 days).

Source 2: CRM Contact Matching

Cross-reference campaign leads with CRM contacts:

Deal association -- are any replied leads associated with open deals? What stage?
Contact history -- have any leads been contacted through other channels?
Lead score -- if the org uses lead scoring, what scores do replied leads have?
Duplicate detection -- flag leads that appear in multiple active campaigns
Conversion tracking -- trace the path from campaign lead to meeting booked to deal created
Source 3: Historical Benchmarks

Load benchmark data for comparison:

Org historical averages -- this org's own past campaign performance (last 90 days)
Industry benchmarks -- standard rates from references/campaign-benchmarks.md
Sequence position baselines -- expected performance decay per email step
Seasonal patterns -- if enough historical data exists, identify day-of-week and time-of-day patterns
What to Ask For

After pulling from all sources, identify gaps. Only ask the user for:

Campaign selection -- if multiple campaigns exist and no campaign_id was given, ask which to focus on (or confirm analyzing all)
Context on paused campaigns -- if a campaign was recently paused, ask if there's a known reason (helps avoid wrong recommendations)
Goal clarification -- if the user seems to want something specific (e.g., "should I scale this?"), confirm the decision they're trying to make

Do NOT ask for information that's already available in the API or CRM data.

Step 1: Pull Campaign Metrics

Retrieve and organize the core performance metrics for each campaign in scope.

Metrics to Calculate

For each campaign, compute:

Metric	Formula	Notes
Open Rate	(Unique Opens / Total Sends) x 100	Use unique opens, not total opens
Click Rate	(Unique Clicks / Total Sends) x 100	Clicks on links in email body
Reply Rate	(Total Replies / Total Sends) x 100	All replies, before classification
Positive Reply Rate	(Positive Replies / Total Sends) x 100	Only interested + question replies
Bounce Rate	(Total Bounces / Total Sends) x 100	Separate hard vs. soft
Unsubscribe Rate	(Unsubscribes / Total Sends) x 100	Include manual opt-outs
Deliverability Rate	((Sends - Bounces) / Sends) x 100	Emails that actually arrived
Reply-to-Open Ratio	(Replies / Unique Opens) x 100	Measures email body effectiveness
Interested Rate	(Interested Leads / Total Sends) x 100	Leads marked interested
Step-Level Breakdown

For multi-step sequences, break down metrics per step:

Step 1 (Initial outreach):    Sent: 500  |  Opens: 275 (55%)  |  Replies: 18 (3.6%)
Step 2 (Follow-up, +3 days):  Sent: 420  |  Opens: 185 (44%)  |  Replies: 12 (2.9%)
Step 3 (Value add, +5 days):  Sent: 380  |  Opens: 140 (37%)  |  Replies: 6 (1.6%)
Step 4 (Break-up, +7 days):   Sent: 350  |  Opens: 120 (34%)  |  Replies: 8 (2.3%)


Note: Step 4 "break-up" emails often see a reply rate bump. If this pattern appears, flag it as healthy.

Trend Analysis

Compare current period metrics against:

Previous period -- same campaign, previous equivalent time window
Org average -- this org's average across all campaigns
Industry benchmark -- from references/campaign-benchmarks.md

Flag any metric that:

Deviates more than 20% from the org's historical average
Falls below industry minimum thresholds
Shows a declining trend over 3+ consecutive days
A/B Variant Comparison

If the campaign has A/B variants (different subject lines, body copy, or send times):

Calculate all metrics per variant
Determine statistical significance -- see references/campaign-benchmarks.md for minimum sample sizes
If significant: declare a winner and recommend pausing the loser
If not significant: report current leader and estimate how many more sends are needed for significance
Calculate the lift: ((Winner Rate - Loser Rate) / Loser Rate) x 100
Step 2: Classify Replies

When include_replies is true (default), fetch all reply content and classify each one using the framework from references/reply-classification.md.

Classification Process

For each reply:

Read the full text -- don't classify on subject line or first sentence alone
Identify the primary intent -- what does this person want or mean?
Assign a category -- one of the six primary categories (see reference)
Set priority level -- P1 through P5 based on category
Score sentiment -- positive, neutral, or negative
Determine recommended action -- what should the rep do next?
Flag edge cases -- sarcasm, "interested but not now," internal forwards
Classification Categories (Summary)
Category	Priority	Action
Positive Interest	P1	Respond within 1 hour. Move to manual sequence.
Question / Info Request	P2	Respond within 4 hours with requested info.
Neutral / Acknowledgment	P3	Send next sequence step. Monitor.
Negative / Not Interested	P4	Mark as not interested. Remove from sequence.
Auto-Reply / OOO	P5	Note return date. Pause and reschedule.
Unsubscribe Request	P5	Immediately remove. Update suppression list.
Reply Quality Score

Calculate an overall Reply Quality Score for the campaign:

Reply Quality Score = (P1_count x 5 + P2_count x 3 + P3_count x 1 + P4_count x 0 + P5_count x 0) / total_replies x 20


Score ranges:

80-100: Excellent targeting and messaging. Replies are high-quality.
60-79: Good. Most replies are actionable.
40-59: Average. Significant noise in replies.
20-39: Poor. Targeting or messaging needs work.
0-19: Critical. Campaign may be hitting the wrong audience entirely.
CRM Updates per Classification

For each classified reply, recommend CRM updates:

P1 (Positive): Create task "Follow up with [name]", update contact status to "Engaged", associate with deal if applicable
P2 (Question): Create task "Answer [name]'s question", log the interaction
P3 (Neutral): Log interaction, continue sequence
P4 (Negative): Update contact status to "Not Interested", add to suppression for this campaign type
P5 (Auto/OOO): Log interaction, set reminder for return date if available
P5 (Unsubscribe): Update suppression list, remove from all active sequences
Step 3: Compare to Benchmarks

Reference references/campaign-benchmarks.md for full benchmark data. Apply three layers of comparison.

Layer 1: Industry Averages

Compare the campaign's metrics against industry-specific benchmarks:

Open rates vary significantly by industry (SaaS: 45-55%, Financial Services: 35-45%, etc.)
Reply rates depend on sequence position and audience warmth
Bounce rates have hard thresholds: healthy (< 2%), warning (2-5%), critical (> 5%)

Use the org's industry if known from CRM data. If unknown, use the "All Industries" baseline.

Layer 2: Org Historical Performance

Compare against this org's own history:

Pull the org's last 10 campaigns (or last 90 days of data)
Calculate average and standard deviation for each metric
Flag any metric more than 1 standard deviation below the org's mean
Highlight improvements (metrics above the org's mean)

This is the most important comparison -- relative performance matters more than absolute benchmarks.

Layer 3: Sequence Position Baselines

Compare step-level metrics against expected performance decay:

Email 1 reply rate baseline: 3-5% (cold outreach)
Email 2 reply rate baseline: 2-3% (first follow-up)
Email 3 reply rate baseline: 1-2% (second follow-up)
Email 4+ reply rate baseline: 0.5-1.5% (persistence touches)

If a later step significantly outperforms its baseline, the messaging in that step is strong -- recommend using its approach in earlier steps.

If a step significantly underperforms, it's a candidate for rewriting or removal.

Benchmark Presentation

Present benchmarks as a clear comparison table:

Metric            Your Campaign    Org Average    Industry Avg    Status
Open Rate         52.3%            48.1%          45-55%          GOOD
Reply Rate        3.8%             2.9%           2-5%            GOOD
Positive Reply    1.2%             1.5%           1-3%            WATCH
Bounce Rate       4.1%             1.8%           < 2%            WARNING
Unsub Rate        0.3%             0.2%           < 0.5%          OK


Use status labels:

EXCELLENT: Top quartile, well above benchmarks
GOOD: At or above benchmarks
OK: Within acceptable range
WATCH: Trending down or at lower end of acceptable range
WARNING: Below minimum thresholds, action needed
CRITICAL: Significantly below thresholds, immediate action required
Step 4: Identify Patterns

Move beyond metrics into pattern recognition. This is where the real optimization insights live.

Subject Line Analysis

If the campaign has multiple variants or the org has historical campaigns:

Rank subject lines by open rate -- which subject lines get the most opens?
Identify winning patterns:
Question vs. statement format
Personalization tokens (first name, company name) vs. generic
Length (short < 40 chars vs. medium 40-60 vs. long 60+)
Urgency/curiosity hooks vs. value-first
Lowercase vs. title case
Flag losing patterns -- subject lines consistently below average
Recommend new test variants based on winning elements
Send Time Optimization

Analyze performance by send time and day:

Day-of-week performance -- which days get the highest open and reply rates?
Time-of-day performance -- morning (6-10am), mid-morning (10am-12pm), afternoon (12-3pm), late afternoon (3-6pm)
Timezone alignment -- are sends hitting the recipient's optimal window?
Compare to benchmarks -- Tuesday-Thursday, 9-11am is the industry standard for B2B; does this org follow or deviate?
Audience Segmentation Patterns

If enough data exists, identify audience-level patterns:

Industry performance -- which prospect industries respond best?
Company size -- do SMBs, mid-market, or enterprise respond differently?
Seniority level -- C-suite vs. VP vs. Director vs. Manager response rates
Geographic patterns -- any regional differences in engagement?
Lead source -- do leads from different sources (LinkedIn, Apollo, purchased lists) perform differently?
Sequence Flow Patterns

Analyze how leads move through the sequence:

Drop-off points -- where do most leads stop engaging?
Re-engagement spikes -- do any later steps re-engage dormant leads?
Optimal sequence length -- at what step does incremental value approach zero?
Reply timing -- how long after receiving an email do most replies come?
Multi-touch attribution -- do leads who open multiple emails reply at higher rates?
Deliverability Signals

Watch for email deliverability issues:

Bounce rate trend -- is it increasing over time? (sign of list decay or domain issues)
Open rate sudden drops -- could indicate emails landing in spam
Domain-specific bounces -- are bounces concentrated at specific email providers?
Warm-up status -- if the sending domain/mailbox is new, are warm-up metrics on track?
SPF/DKIM/DMARC -- flag if there are signs of authentication issues
Step 5: Generate Recommendations

Every recommendation must be specific, actionable, and prioritized by expected impact. No generic advice.

Recommendation Format

Each recommendation follows this structure:

RECOMMENDATION: [One-sentence action]
PRIORITY: High / Medium / Low
EXPECTED IMPACT: [Specific metric improvement estimate]
EFFORT: Low / Medium / High
REASONING: [2-3 sentences explaining why, backed by data from the analysis]
HOW TO IMPLEMENT: [Specific steps to execute this recommendation]

Recommendation Categories
Campaign Health (Immediate Actions)

These are "fix now" recommendations that address active problems:

"Pause Step 3 -- reply rate is 0.2% vs. 1.6% baseline. It's burning leads without value. Replace with a case-study-led email."
"Reduce daily send volume from 80 to 50 -- bounce rate is 4.1% and climbing. Sending slower will protect domain reputation."
"Switch to Subject B immediately -- it has a 58% open rate vs. Subject A's 41%, with 300+ sends per variant (statistically significant)."
"Add 3-day spacing between Steps 2 and 3 -- current 1-day gap is generating 'stop emailing me' replies."
Messaging Optimization (This Week)

Improvements to email content based on reply analysis:

"Lead Step 1 with the pain point about [specific issue] -- 4 of 6 positive replies referenced this topic."
"Shorten Step 2 to under 80 words -- current version is 180 words and has a 35% lower reply rate than your org average for follow-ups."
"Add a specific CTA to Step 1 -- 'Are you available for 15 minutes on Tuesday?' outperforms 'Would love to chat' by 2.1x based on your reply data."
"Remove the case study link from Step 3 -- click rate is 0.4% and it's not driving replies. Replace with a one-line proof point."
Targeting Refinement (This Sprint)

Audience and segmentation recommendations:

"Split the campaign by company size -- mid-market (200-1000 employees) has a 5.2% reply rate vs. 1.1% for enterprise (1000+). Create a separate enterprise sequence with longer nurture."
"Exclude [industry] from the next batch -- 0 positive replies from 85 sends. Reallocate to [better-performing industry]."
"Increase send volume on Tuesdays -- your Tuesday sends have 2x the reply rate of Friday sends."
A/B Test Suggestions (Next Campaign)

New tests to run based on identified patterns:

"Test a question-format subject line -- your current statement format averages 44% opens; industry data shows questions average 48-52% for your segment."
"Test sending at 7:30am local time vs. current 10am -- early morning sends show a 15% open rate lift in your last 3 campaigns."
"Test a 3-step sequence vs. current 5-step -- your Steps 4 and 5 generate 0.3% combined reply rate. A shorter sequence frees capacity for more leads."
Prioritization Matrix

Rank all recommendations by impact-to-effort ratio:

Priority	Impact	Effort	Action Timeline
P1	High	Low	Execute today
P2	High	Medium	Execute this week
P3	Medium	Low	Execute this week
P4	Medium	Medium	Execute this sprint
P5	Low	Low	Backlog / nice to have

Never generate more than 7 recommendations. Fewer, more impactful recommendations beat a laundry list.

Step 6: Format for Delivery

Structure the output for maximum clarity and actionability.

Summary Dashboard

Start with a high-level dashboard:

CAMPAIGN PERFORMANCE SUMMARY
Campaign: [Name]  |  Status: [Active/Paused]  |  Period: [Date Range]

Total Sends: 1,247    |  Deliverability: 97.2%
Open Rate:   52.3%    |  vs. Org Avg: +4.2%    |  Status: GOOD
Reply Rate:  3.8%     |  vs. Org Avg: +0.9%    |  Status: GOOD
Positive:    1.2%     |  vs. Org Avg: -0.3%    |  Status: WATCH
Bounce Rate: 4.1%     |  vs. Org Avg: +2.3%    |  Status: WARNING
Unsub Rate:  0.3%     |  vs. Org Avg: +0.1%    |  Status: OK

Reply Quality Score: 68/100 (Good)

Replies Needing Attention

List P1 and P2 replies that require human action:

REPLIES REQUIRING ACTION (5)

P1 - POSITIVE INTEREST
  [Contact Name] @ [Company] -- "Sounds interesting, can you send more details?"
  Action: Respond within 1 hour with personalized follow-up
  CRM: Create follow-up task, update status to Engaged

P1 - POSITIVE INTEREST
  [Contact Name] @ [Company] -- "Let's set up a call next week"
  Action: Send calendar link immediately
  CRM: Create meeting, associate with deal

P2 - QUESTION
  [Contact Name] @ [Company] -- "What's the pricing for this?"
  Action: Respond within 4 hours with pricing info
  CRM: Log interaction, create follow-up task

Slack Delivery Format

When delivering via Slack, use this condensed format:

Campaign Report: [Campaign Name]
Period: [Date Range]

Key Metrics:
  Sends: 1,247 | Opens: 52.3% | Replies: 3.8% | Bounces: 4.1%

Replies: 47 total
  Positive: 15 (P1) | Questions: 8 (P2) | Neutral: 10 | Negative: 6 | Auto: 8

Top Action Items:
  1. [Most important recommendation]
  2. [Second recommendation]
  3. [Third recommendation]

Replies needing attention: [count] -- check the full report for details.

Multi-Campaign Comparison

When analyzing multiple campaigns, add a comparison view:

CAMPAIGN COMPARISON

Campaign          Sends  Open%  Reply%  +Reply%  Bounce%  Status
Pipeline Nurture  1,247  52.3%  3.8%   1.2%     4.1%     WARNING
New Logos Q1      892    48.1%  4.2%   2.1%     1.3%     GOOD
Enterprise ABM    234    61.5%  6.8%   3.4%     0.9%     EXCELLENT
Reactivation      567    38.2%  1.9%   0.4%     2.8%     WATCH


Rank campaigns by positive reply rate (the metric that matters most for pipeline generation).

Quality Check

Before presenting the analysis, verify:

 Metrics are from the correct time range and campaign(s)?
 All percentages are calculated from unique events (not total events)?
 Reply classifications used the full reply text, not just snippets?
 Benchmark comparisons use the correct industry and org data?
 Every recommendation is specific (names a metric, a step, or a variant)?
 No generic advice like "improve your subject lines" or "test more"?
 Recommendations are prioritized and limited to 7 or fewer?
 P1 and P2 replies are highlighted with clear next actions?
 A/B test conclusions state whether results are statistically significant?
 Deliverability warnings are flagged if bounce rate exceeds 2%?
 The report opens with the most important finding, not just metrics?
 CRM update recommendations are included for classified replies?
Error Handling
"Instantly API rate limit exceeded"

Reduce the query scope. Start with summary-level campaign analytics (single API call), then selectively pull step-level and reply data only for campaigns the user cares about. Cache results and note the timestamp so the user knows when data was last refreshed.

"No active campaigns found"

Check for recently completed or paused campaigns (last 30 days). If found, analyze those and note they're not currently running. If no campaigns exist at all, inform the user and offer to help them set up their first campaign using the sales-sequence skill.

"Insufficient data for benchmarks"

If the campaign has fewer than 100 sends, warn that metrics are not yet statistically meaningful. Provide the raw numbers but caveat percentages. Recommend a minimum of 200-300 sends before drawing conclusions on open/reply rates, and 500+ sends per variant for A/B tests.

"Reply content unavailable"

If reply text can't be retrieved (API limitation or permission issue), skip classification and report only quantitative metrics. Note that reply classification requires reply content access and recommend the user check their Instantly API permissions.

"Campaign shows zero opens"

This is almost always a tracking issue, not a performance issue. Check:

Is open tracking enabled in Instantly?
Is the tracking domain configured correctly?
Are emails landing in spam? (Check bounce rate and deliverability indicators) Recommend the user verify their Instantly tracking settings before interpreting performance.
"Bounce rate is critically high (> 5%)"

This is an emergency. Recommend:

Pause the campaign immediately to protect domain reputation
Review the lead list for invalid emails (run through a verification service)
Check sending domain health (SPF, DKIM, DMARC records)
Reduce daily send volume by 50% when resuming
Consider warming up a new mailbox if the current one is burned
"User asks about a specific lead's reply"

If the user asks about a single reply rather than campaign-wide analysis, still pull campaign context (for benchmark comparison) but focus the response on that specific lead. Include the reply classification, recommended action, and any CRM data about that contact.

Weekly Installs
–
Repository
sixtysecondsapp/use60
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn