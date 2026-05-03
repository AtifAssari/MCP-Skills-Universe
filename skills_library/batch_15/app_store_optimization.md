---
title: app-store-optimization
url: https://skills.sh/manojbajaj95/claude-gtm-plugin/app-store-optimization
---

# app-store-optimization

skills/manojbajaj95/claude-gtm-plugin/app-store-optimization
app-store-optimization
Installation
$ npx skills add https://github.com/manojbajaj95/claude-gtm-plugin --skill app-store-optimization
SKILL.md
App Store Optimization (ASO)

ASO tools for researching keywords, optimizing metadata, analyzing competitors, and improving app store visibility on Apple App Store and Google Play Store.

Table of Contents
Keyword Research Workflow
Metadata Optimization Workflow
Competitor Analysis Workflow
App Launch Workflow
A/B Testing Workflow
Before/After Examples
Tools and References
Keyword Research Workflow

Discover and evaluate keywords that drive app store visibility.

Workflow: Conduct Keyword Research
Define target audience and core app functions:
Primary use case (what problem does the app solve)
Target user demographics
Competitive category
Generate seed keywords from:
App features and benefits
User language (not developer terminology)
App store autocomplete suggestions
Expand keyword list using:
Modifiers (free, best, simple)
Actions (create, track, organize)
Audiences (for students, for teams, for business)
Evaluate each keyword:
Search volume (estimated monthly searches)
Competition (number and quality of ranking apps)
Relevance (alignment with app function)
Score and prioritize keywords:
Primary: Title and keyword field (iOS)
Secondary: Subtitle and short description
Tertiary: Full description only
Map keywords to metadata locations
Document keyword strategy for tracking
Validation: Keywords scored; placement mapped; no competitor brand names included; no plurals in iOS keyword field
Keyword Evaluation Criteria
Factor	Weight	High Score Indicators
Relevance	35%	Describes core app function
Volume	25%	10,000+ monthly searches
Competition	25%	Top 10 apps have <4.5 avg rating
Conversion	15%	Transactional intent ("best X app")
Keyword Placement Priority
Location	Search Weight	Character Limit
App Title	Highest	30 (iOS) / 50 (Android)
Subtitle (iOS)	High	30
Keyword Field (iOS)	High	100
Short Description (Android)	High	80
Full Description	Medium	4,000

See: references/keyword-research-guide.md

Metadata Optimization Workflow

Optimize app store listing elements for search ranking and conversion.

Workflow: Optimize App Metadata
Audit current metadata against platform limits:
Title character count and keyword presence
Subtitle/short description usage
Keyword field efficiency (iOS)
Description keyword density
Optimize title following formula:
[Brand Name] - [Primary Keyword] [Secondary Keyword]

Write subtitle (iOS) or short description (Android):
Focus on primary benefit
Include secondary keyword
Use action verbs
Optimize keyword field (iOS only):
Remove duplicates from title
Remove plurals (Apple indexes both forms)
No spaces after commas
Prioritize by score
Rewrite full description:
Hook paragraph with value proposition
Feature bullets with keywords
Social proof section
Call to action
Validate character counts for each field
Calculate keyword density (target 2-3% primary)
Validation: All fields within character limits; primary keyword in title; no keyword stuffing (>5%); natural language preserved
Platform Character Limits
Field	Apple App Store	Google Play Store
Title	30 characters	50 characters
Subtitle	30 characters	N/A
Short Description	N/A	80 characters
Keywords	100 characters	N/A
Promotional Text	170 characters	N/A
Full Description	4,000 characters	4,000 characters
What's New	4,000 characters	500 characters
Description Structure
PARAGRAPH 1: Hook (50-100 words)
├── Address user pain point
├── State main value proposition
└── Include primary keyword

PARAGRAPH 2-3: Features (100-150 words)
├── Top 5 features with benefits
├── Bullet points for scanability
└── Secondary keywords naturally integrated

PARAGRAPH 4: Social Proof (50-75 words)
├── Download count or rating
├── Press mentions or awards
└── Summary of user testimonials

PARAGRAPH 5: Call to Action (25-50 words)
├── Clear next step
└── Reassurance (free trial, no signup)


See: references/platform-requirements.md

Competitor Analysis Workflow

Analyze top competitors to identify keyword gaps and positioning opportunities.

Workflow: Analyze Competitor ASO Strategy
Identify top 10 competitors:
Direct competitors (same core function)
Indirect competitors (overlapping audience)
Category leaders (top downloads)
Extract competitor keywords from:
App titles and subtitles
First 100 words of descriptions
Visible metadata patterns
Build competitor keyword matrix:
Map which keywords each competitor targets
Calculate coverage percentage per keyword
Identify keyword gaps:
Keywords with <40% competitor coverage
High volume terms competitors miss
Long-tail opportunities
Analyze competitor visual assets:
Icon design patterns
Screenshot messaging and style
Video presence and quality
Compare ratings and review patterns:
Average rating by competitor
Common praise themes
Common complaint themes
Document positioning opportunities
Validation: 10+ competitors analyzed; keyword matrix complete; gaps identified with volume estimates; visual audit documented
Competitor Analysis Matrix
Analysis Area	Data Points
Keywords	Title keywords, description frequency
Metadata	Character utilization, keyword density
Visuals	Icon style, screenshot count/style
Ratings	Average rating, total count, velocity
Reviews	Top praise, top complaints
Gap Analysis Template
Opportunity Type	Example	Action
Keyword gap	"habit tracker" (40% coverage)	Add to keyword field
Feature gap	Competitor lacks widget	Highlight in screenshots
Visual gap	No videos in top 5	Create app preview
Messaging gap	None mention "free"	Test free positioning
App Launch Workflow

Execute a structured launch for maximum initial visibility.

Workflow: Launch App to Stores
Complete pre-launch preparation (4 weeks before):
Finalize keywords and metadata
Prepare all visual assets
Set up analytics (Firebase, Mixpanel)
Build press kit and media list
Submit for review (2 weeks before):
Complete all store requirements
Verify compliance with guidelines
Prepare launch communications
Configure post-launch systems:
Set up review monitoring
Prepare response templates
Configure rating prompt timing
Execute launch day:
Verify app is live in both stores
Announce across all channels
Begin review response cycle
Monitor initial performance (days 1-7):
Track download velocity hourly
Monitor reviews and respond within 24 hours
Document any issues for quick fixes
Conduct 7-day retrospective:
Compare performance to projections
Identify quick optimization wins
Plan first metadata update
Schedule first update (2 weeks post-launch)
Validation: App live in stores; analytics tracking; review responses within 24h; download velocity documented; first update scheduled
Pre-Launch Checklist
Category	Items
Metadata	Title, subtitle, description, keywords
Visual Assets	Icon, screenshots (all sizes), video
Compliance	Age rating, privacy policy, content rights
Technical	App binary, signing certificates
Analytics	SDK integration, event tracking
Marketing	Press kit, social content, email ready
Launch Timing Considerations
Factor	Recommendation
Day of week	Tuesday-Wednesday (avoid weekends)
Time of day	Morning in target market timezone
Seasonal	Align with relevant category seasons
Competition	Avoid major competitor launch dates

See: references/aso-best-practices.md

A/B Testing Workflow

Test metadata and visual elements to improve conversion rates.

Workflow: Run A/B Test
Select test element (prioritize by impact):
Icon (highest impact)
Screenshot 1 (high impact)
Title (high impact)
Short description (medium impact)
Form hypothesis:
If we [change], then [metric] will [improve/increase] by [amount]
because [rationale].

Create variants:
Control: Current version
Treatment: Single variable change
Calculate required sample size:
Baseline conversion rate
Minimum detectable effect (usually 5%)
Statistical significance (95%)
Launch test:
Apple: Use Product Page Optimization
Android: Use Store Listing Experiments
Run test for minimum duration:
At least 7 days
Until statistical significance reached
Analyze results:
Compare conversion rates
Check statistical significance
Document learnings
Validation: Single variable tested; sample size sufficient; significance reached (95%); results documented; winner implemented
A/B Test Prioritization
Element	Conversion Impact	Test Complexity
App Icon	10-25% lift possible	Medium (design needed)
Screenshot 1	15-35% lift possible	Medium
Title	5-15% lift possible	Low
Short Description	5-10% lift possible	Low
Video	10-20% lift possible	High
Sample Size Quick Reference
Baseline CVR	Impressions Needed (per variant)
1%	31,000
2%	15,500
5%	6,200
10%	3,100
Test Documentation Template
TEST ID: ASO-2025-001
ELEMENT: App Icon
HYPOTHESIS: A bolder color icon will increase conversion by 10%
START DATE: [Date]
END DATE: [Date]

RESULTS:
├── Control CVR: 4.2%
├── Treatment CVR: 4.8%
├── Lift: +14.3%
├── Significance: 97%
└── Decision: Implement treatment

LEARNINGS:
- Bold colors outperform muted tones in this category
- Apply to screenshot backgrounds for next test

Before/After Examples
Title Optimization

Productivity App:

Version	Title	Analysis
Before	"MyTasks"	No keywords, brand only (8 chars)
After	"MyTasks - Todo List & Planner"	Primary + secondary keywords (29 chars)

Fitness App:

Version	Title	Analysis
Before	"FitTrack Pro"	Generic modifier (12 chars)
After	"FitTrack: Workout Log & Gym"	Category keywords (27 chars)
Subtitle Optimization (iOS)
Version	Subtitle	Analysis
Before	"Get Things Done"	Vague, no keywords
After	"Daily Task Manager & Planner"	Two keywords, benefit clear
Keyword Field Optimization (iOS)

Before (Inefficient - 89 chars, 8 keywords):

task manager, todo list, productivity app, daily planner, reminder app


After (Optimized - 97 chars, 14 keywords):

task,todo,checklist,reminder,organize,daily,planner,schedule,deadline,goals,habit,widget,sync,team


Improvements:

Removed spaces after commas (+8 chars)
Removed duplicates (task manager → task)
Removed plurals (reminders → reminder)
Removed words in title
Added more relevant keywords
Description Opening

Before:

MyTasks is a comprehensive task management solution designed
to help busy professionals organize their daily activities
and boost productivity.


After:

Forget missed deadlines. MyTasks keeps every task, reminder,
and project in one place—so you focus on doing, not remembering.
Trusted by 500,000+ professionals.


Improvements:

Leads with user pain point
Specific benefit (not generic "boost productivity")
Social proof included
Keywords natural, not stuffed
Screenshot Caption Evolution
Version	Caption	Issue
Before	"Task List Feature"	Feature-focused, passive
Better	"Create Task Lists"	Action verb, but still feature
Best	"Never Miss a Deadline"	Benefit-focused, emotional
Tools and References
Scripts
Script	Purpose	Usage
keyword_analyzer.py	Analyze keywords for volume and competition	python keyword_analyzer.py --keywords "todo,task,planner"
metadata_optimizer.py	Validate metadata character limits and density	python metadata_optimizer.py --platform ios --title "App Title"
competitor_analyzer.py	Extract and compare competitor keywords	python competitor_analyzer.py --competitors "App1,App2,App3"
aso_scorer.py	Calculate overall ASO health score	python aso_scorer.py --app-id com.example.app
ab_test_planner.py	Plan tests and calculate sample sizes	python ab_test_planner.py --cvr 0.05 --lift 0.10
review_analyzer.py	Analyze review sentiment and themes	python review_analyzer.py --app-id com.example.app
launch_checklist.py	Generate platform-specific launch checklists	python launch_checklist.py --platform ios
localization_helper.py	Manage multi-language metadata	python localization_helper.py --locales "en,es,de,ja"
References
Document	Content
platform-requirements.md	iOS and Android metadata specs, visual asset requirements
aso-best-practices.md	Optimization strategies, rating management, launch tactics
keyword-research-guide.md	Research methodology, evaluation framework, tracking
Assets
Template	Purpose
aso-audit-template.md	Structured audit checklist for app store listings
Platform Limitations
Data Constraints
Constraint	Impact
No official keyword volume data	Estimates based on third-party tools
Competitor data limited to public info	Cannot see internal metrics
Review access limited to public reviews	No access to private feedback
Historical data unavailable for new apps	Cannot compare to past performance
Platform Behavior
Platform	Behavior
iOS	Keyword changes require app submission
iOS	Promotional text editable without update
Android	Metadata changes index in 1-2 hours
Android	No separate keyword field (use description)
Both	Algorithm changes without notice
When Not to Use This Skill
Scenario	Alternative
Web apps	Use web SEO skills
Enterprise apps (not public)	Internal distribution tools
Beta/TestFlight only	Focus on feedback, not ASO
Paid advertising strategy	Use paid acquisition skills
Related Skills
Skill	Integration Point
content-creator	App description copywriting
marketing-demand-acquisition	Launch promotion campaigns
marketing-strategy-pmm	Go-to-market planning
Weekly Installs
129
Repository
manojbajaj95/cl…m-plugin
GitHub Stars
43
First Seen
Mar 11, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn