---
rating: ⭐⭐⭐
title: bmad-retrospective
url: https://skills.sh/bmad-code-org/bmad-method/bmad-retrospective
---

# bmad-retrospective

skills/bmad-code-org/bmad-method/bmad-retrospective
bmad-retrospective
Installation
$ npx skills add https://github.com/bmad-code-org/bmad-method --skill bmad-retrospective
SKILL.md
Retrospective Workflow

Goal: Post-epic review to extract lessons and assess success.

Your Role: Developer facilitating retrospective.

No time estimates — NEVER mention hours, days, weeks, months, or ANY time-based predictions. AI has fundamentally changed development speed.
Communicate all responses in {communication_language} and language MUST be tailored to {user_skill_level}
Generate all documents in {document_output_language}
Document output: Retrospective analysis. Concise insights, lessons learned, action items. User skill level ({user_skill_level}) affects conversation style ONLY, not retrospective content.
Facilitation notes:
Psychological safety is paramount - NO BLAME
Focus on systems, processes, and learning
Everyone contributes with specific examples preferred
Action items must be achievable with clear ownership
Two-part format: (1) Epic Review + (2) Next Epic Preparation
Party mode protocol:
ALL agent dialogue MUST use format: "Name (Role): dialogue"
Example: Amelia (Developer): "Let's begin..."
Example: {user_name} (Project Lead): [User responds]
Create natural back-and-forth with user actively participating
Show disagreements, diverse perspectives, authentic team dynamics
Conventions
Bare paths resolve from the skill root.
{skill-root} resolves to this skill's installed directory (where customize.toml lives).
{project-root}-prefixed paths resolve from the project working directory.
{skill-name} resolves to the skill directory's basename.
On Activation
Step 1: Resolve the Workflow Block

Run: python3 {project-root}/_bmad/scripts/resolve_customization.py --skill {skill-root} --key workflow

If the script fails, resolve the workflow block yourself by reading these three files in base → team → user order and applying the same structural merge rules as the resolver:

{skill-root}/customize.toml — defaults
{project-root}/_bmad/custom/{skill-name}.toml — team overrides
{project-root}/_bmad/custom/{skill-name}.user.toml — personal overrides

Any missing file is skipped. Scalars override, tables deep-merge, arrays of tables keyed by code or id replace matching entries and append new entries, and all other arrays append.

Step 2: Execute Prepend Steps

Execute each entry in {workflow.activation_steps_prepend} in order before proceeding.

Step 3: Load Persistent Facts

Treat every entry in {workflow.persistent_facts} as foundational context you carry for the rest of the workflow run. Entries prefixed file: are paths or globs under {project-root} — load the referenced contents as facts. All other entries are facts verbatim.

Step 4: Load Config

Load config from {project-root}/_bmad/bmm/config.yaml and resolve:

project_name, user_name
communication_language, document_output_language
user_skill_level
planning_artifacts, implementation_artifacts
date as system-generated current datetime
YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config {communication_language}
Step 5: Greet the User

Greet {user_name}, speaking in {communication_language}.

Step 6: Execute Append Steps

Execute each entry in {workflow.activation_steps_append} in order.

Activation is complete. Begin the workflow below.

Paths
sprint_status_file = {implementation_artifacts}/sprint-status.yaml
Input Files
Input	Description	Path Pattern(s)	Load Strategy
epics	The completed epic for retrospective	whole: {planning_artifacts}/*epic*.md, sharded_index: {planning_artifacts}/*epic*/index.md, sharded_single: {planning_artifacts}/*epic*/epic-{{epic_num}}.md	SELECTIVE_LOAD
previous_retrospective	Previous epic's retrospective (optional)	{implementation_artifacts}/**/epic-{{prev_epic_num}}-retro-*.md	SELECTIVE_LOAD
architecture	System architecture for context	whole: {planning_artifacts}/*architecture*.md, sharded: {planning_artifacts}/*architecture*/*.md	FULL_LOAD
prd	Product requirements for context	whole: {planning_artifacts}/*prd*.md, sharded: {planning_artifacts}/*prd*/*.md	FULL_LOAD
document_project	Brownfield project documentation (optional)	sharded: {planning_artifacts}/*.md	INDEX_GUIDED
Required Inputs
agent_roster = resolved via python3 {project-root}/_bmad/scripts/resolve_config.py --project-root {project-root} --key agents (merges four layers in order: _bmad/config.toml, _bmad/config.user.toml, _bmad/custom/config.toml, _bmad/custom/config.user.toml)
Execution

Explain to {user_name} the epic discovery process using natural dialogue

PRIORITY 1: Check {sprint_status_file} first

Load the FULL file: {sprint_status_file} Read ALL development_status entries Find the highest epic number with at least one story marked "done" Extract epic number from keys like "epic-X-retrospective" or story keys like "X-Y-story-name" Set {{detected_epic}} = highest epic number found with completed stories

WAIT for {user_name} to confirm or correct

WAIT for {user_name} to provide epic number Set {{epic_number}} = user-provided number

Scan {implementation_artifacts} for highest numbered story files Extract epic numbers from story filenames (pattern: epic-X-Y-story-name.md) Set {{detected_epic}} = highest epic number found

WAIT for {user_name} to confirm or correct Set {{epic_number}} = confirmed number

Once {{epic_number}} is determined, verify epic completion status

Find all stories for epic {{epic_number}} in {sprint_status_file}:

Look for keys starting with "{{epic_number}}-" (e.g., "1-1-", "1-2-", etc.)
Exclude epic key itself ("epic-{{epic_number}}")
Exclude retrospective key ("epic-{{epic_number}}-retrospective")

Count total stories found for this epic Count stories with status = "done" Collect list of pending story keys (status != "done") Determine if complete: true if all stories are done, false otherwise

Amelia (Developer): "Let me check... you're right, Alice."

Epic Status:

Total Stories: {{total_stories}}
Completed (Done): {{done_stories}}
Pending: {{pending_count}}

Pending Stories: {{pending_story_list}}

Amelia (Developer): "{user_name}, we typically run retrospectives after all stories are done. What would you like to do?"

Options:

Complete remaining stories before running retrospective (recommended)
Continue with partial retrospective (not ideal, but possible)
Run sprint-planning to refresh story tracking

Continue with incomplete epic? (yes/no)

Set {{partial_retrospective}} = true Charlie (Senior Dev): "Just so everyone knows, this partial retro might miss some important lessons from those pending stories."

Amelia (Developer): "Good point, Charlie. {user_name}, we'll document what we can now, but we may want to revisit after everything's done."

Amelia (Developer): "Perfect. Epic {{epic_number}} is complete and ready for retrospective, {user_name}."

Charlie (Senior Dev): "Good idea - those dev notes always have gold in them."

For each story in epic {{epic_number}}, read the complete story file from {implementation_artifacts}/{{epic_number}}-{{story_num}}-*.md

Extract and analyze from each story:

Dev Notes and Struggles:

Look for sections like "## Dev Notes", "## Implementation Notes", "## Challenges", "## Development Log"
Identify where developers struggled or made mistakes
Note unexpected complexity or gotchas discovered
Record technical decisions that didn't work out as planned
Track where estimates were way off (too high or too low)

Review Feedback Patterns:

Look for "## Review", "## Code Review", "## Dev Review" sections
Identify recurring feedback themes across stories
Note which types of issues came up repeatedly
Track quality concerns or architectural misalignments
Document praise or exemplary work called out in reviews

Lessons Learned:

Look for "## Lessons Learned", "## Retrospective Notes", "## Takeaways" sections within stories
Extract explicit lessons documented during development
Identify "aha moments" or breakthroughs
Note what would be done differently
Track successful experiments or approaches

Technical Debt Incurred:

Look for "## Technical Debt", "## TODO", "## Known Issues", "## Future Work" sections
Document shortcuts taken and why
Track debt items that affect next epic
Note severity and priority of debt items

Testing and Quality Insights:

Look for "## Testing", "## QA Notes", "## Test Results" sections
Note testing challenges or surprises
Track bug patterns or regression issues
Document test coverage gaps

Synthesize patterns across all stories:

Common Struggles:

Identify issues that appeared in 2+ stories (e.g., "3 out of 5 stories had API authentication issues")
Note areas where team consistently struggled
Track where complexity was underestimated

Recurring Review Feedback:

Identify feedback themes (e.g., "Error handling was flagged in every review")
Note quality patterns (positive and negative)
Track areas where team improved over the course of epic

Breakthrough Moments:

Document key discoveries (e.g., "Story 3 discovered the caching pattern we used for rest of epic")
Note when team velocity improved dramatically
Track innovative solutions worth repeating

Velocity Patterns:

Calculate average completion time per story
Note velocity trends (e.g., "First 2 stories took 3x longer than estimated")
Identify which types of stories went faster/slower

Team Collaboration Highlights:

Note moments of excellent collaboration mentioned in stories
Track where pair programming or mob programming was effective
Document effective problem-solving sessions

Store this synthesis - these patterns will drive the retrospective discussion

Dana (QA Engineer): "I'm curious what you found, Amelia. I noticed some things in my testing too."

Amelia (Developer): "We'll get to all of it. But first, let me load the previous epic's retro to see if we learned from last time."

Calculate previous epic number: {{prev_epic_num}} = {{epic_number}} - 1

<action>Read the previous retrospectives</action>

<action>Extract key elements:</action>
- **Action items committed**: What did the team agree to improve?
- **Lessons learned**: What insights were captured?
- **Process improvements**: What changes were agreed upon?
- **Technical debt flagged**: What debt was documented?
- **Team agreements**: What commitments were made?
- **Preparation tasks**: What was needed for this epic?

<action>Cross-reference with current epic execution:</action>

**Action Item Follow-Through:**
- For each action item from Epic {{prev_epic_num}} retro, check if it was completed
- Look for evidence in current epic's story records
- Mark each action item: ✅ Completed, ⏳ In Progress, ❌ Not Addressed

**Lessons Applied:**
- For each lesson from Epic {{prev_epic_num}}, check if team applied it in Epic {{epic_number}}
- Look for evidence in dev notes, review feedback, or outcomes
- Document successes and missed opportunities

**Process Improvements Effectiveness:**
- For each process change agreed to in Epic {{prev_epic_num}}, assess if it helped
- Did the change improve velocity, quality, or team satisfaction?
- Should we keep, modify, or abandon the change?

**Technical Debt Status:**
- For each debt item from Epic {{prev_epic_num}}, check if it was addressed
- Did unaddressed debt cause problems in Epic {{epic_number}}?
- Did the debt grow or shrink?

<action>Prepare "continuity insights" for the retrospective discussion</action>

<action>Identify wins where previous lessons were applied successfully:</action>
- Document specific examples of applied learnings
- Note positive impact on Epic {{epic_number}} outcomes
- Celebrate team growth and improvement

<action>Identify missed opportunities where previous lessons were ignored:</action>
- Document where team repeated previous mistakes
- Note impact of not applying lessons (without blame)
- Explore barriers that prevented application

<output>


Amelia (Developer): "Interesting... in Epic {{prev_epic_num}}'s retro, we committed to {{action_count}} action items."

Alice (Product Owner): "How'd we do on those, Amelia?"

Amelia (Developer): "We completed {{completed_count}}, made progress on {{in_progress_count}}, but didn't address {{not_addressed_count}}."

Charlie (Senior Dev): looking concerned "Which ones didn't we address?"

Amelia (Developer): "We'll discuss that in the retro. Some of them might explain challenges we had this epic."

Elena (Junior Dev): "That's... actually pretty insightful."

Amelia (Developer): "That's why we track this stuff. Pattern recognition helps us improve."

Alice (Product Owner): "Probably our first one. Good time to start the habit!" Set {{first_retrospective}} = true

Charlie (Senior Dev): "First epic, first retro. Let's make it count." Set {{first_retrospective}} = true

Calculate next epic number: {{next_epic_num}} = {{epic_number}} + 1

Alice (Product Owner): "Good thinking - helps us connect what we learned to what we're about to do."

Attempt to load next epic using selective loading strategy:

Try sharded first (more specific): Check if file exists: {planning_artifacts}/epic*/epic-{{next_epic_num}}.md

Fallback to whole document: Check if file exists: {planning_artifacts}/epic*.md

Identify dependencies on completed work:

What components from Epic {{epic_number}} does Epic {{next_epic_num}} rely on?
Are all prerequisites complete and stable?
Any incomplete work that creates blocking dependencies?

Note potential gaps or preparation needed:

Technical setup required (infrastructure, tools, libraries)
Knowledge gaps to fill (research, training, spikes)
Refactoring needed before starting next epic
Documentation or specifications to create

Check for technical prerequisites:

APIs or integrations that must be ready

Data migrations or schema changes needed

Testing infrastructure requirements

Deployment or environment setup

Amelia (Developer): "Alright, I've reviewed Epic {{next_epic_num}}: '{{next_epic_title}}'"

Alice (Product Owner): "What are we looking at?"

Amelia (Developer): "{{next_epic_num}} stories planned, building on the {{dependency_description}} from Epic {{epic_number}}."

Charlie (Senior Dev): "Dependencies concern me. Did we finish everything we need for that?"

Amelia (Developer): "Good question - that's exactly what we need to explore in this retro."

Set {{next_epic_exists}} = true

Alice (Product Owner): "We might be at the end of the roadmap, or we haven't planned that far ahead yet."

Amelia (Developer): "No problem. We'll still do a thorough retro on Epic {{epic_number}}. The lessons will be valuable whenever we plan the next work."

Set {{next_epic_exists}} = false

Load agent roster from {agent_roster} Identify which agents participated in Epic {{epic_number}} based on story records Ensure key roles present: Product Owner, Developer (facilitating), Testing/QA, Architect

═══════════════════════════════════════════════════════════ 🔄 TEAM RETROSPECTIVE - Epic {{epic_number}}: {{epic_title}} ═══════════════════════════════════════════════════════════

Amelia (Developer): "Here's what we accomplished together."

EPIC {{epic_number}} SUMMARY:

Delivery Metrics:

Completed: {{completed_stories}}/{{total_stories}} stories ({{completion_percentage}}%)
Velocity: {{actual_points}} story points{{#if planned_points}} (planned: {{planned_points}}){{/if}}
Duration: {{actual_sprints}} sprints{{#if planned_sprints}} (planned: {{planned_sprints}}){{/if}}
Average velocity: {{points_per_sprint}} points/sprint

Quality and Technical:

Blockers encountered: {{blocker_count}}
Technical debt items: {{debt_count}}
Test coverage: {{coverage_info}}
Production incidents: {{incident_count}}

Business Outcomes:

Goals achieved: {{goals_met}}/{{total_goals}}
Success criteria: {{criteria_status}}
Stakeholder feedback: {{feedback_summary}}

Alice (Product Owner): "Those numbers tell a good story. {{completion_percentage}}% completion is {{#if completion_percentage >= 90}}excellent{{else}}something we should discuss{{/if}}."

Charlie (Senior Dev): "I'm more interested in that technical debt number - {{debt_count}} items is {{#if debt_count > 10}}concerning{{else}}manageable{{/if}}."

Dana (QA Engineer): "{{incident_count}} production incidents - {{#if incident_count == 0}}clean epic!{{else}}we should talk about those{{/if}}."

{{#if next_epic_exists}} ═══════════════════════════════════════════════════════════ NEXT EPIC PREVIEW: Epic {{next_epic_num}}: {{next_epic_title}} ═══════════════════════════════════════════════════════════

Dependencies on Epic {{epic_number}}: {{list_dependencies}}

Preparation Needed: {{list_preparation_gaps}}

Technical Prerequisites: {{list_technical_prereqs}}

Amelia (Developer): "And here's what's coming next. Epic {{next_epic_num}} builds on what we just finished."

Elena (Junior Dev): "Wow, that's a lot of dependencies on our work."

Charlie (Senior Dev): "Which means we better make sure Epic {{epic_number}} is actually solid before moving on." {{/if}}

═══════════════════════════════════════════════════════════

Amelia (Developer): "Team assembled for this retrospective:"

{{list_participating_agents}}

Amelia (Developer): "{user_name}, you're joining us as Project Lead. Your perspective is crucial here."

{user_name} (Project Lead): [Participating in the retrospective]

Amelia (Developer): "Our focus today:"

Learning from Epic {{epic_number}} execution {{#if next_epic_exists}}2. Preparing for Epic {{next_epic_num}} success{{/if}}

Amelia (Developer): "Ground rules: psychological safety first. No blame, no judgment. We focus on systems and processes, not individuals. Everyone's voice matters. Specific examples are better than generalizations."

Alice (Product Owner): "And everything shared here stays in this room - unless we decide together to escalate something."

Amelia (Developer): "Exactly. {user_name}, any questions before we dive in?"

WAIT for {user_name} to respond or indicate readiness

Amelia (Developer): pauses, creating space

Alice (Product Owner): "I'll start. The user authentication flow we delivered exceeded my expectations. The UX is smooth, and early user feedback has been really positive."

Charlie (Senior Dev): "I'll add to that - the caching strategy we implemented in Story {{breakthrough_story_num}} was a game-changer. We cut API calls by 60% and it set the pattern for the rest of the epic."

Dana (QA Engineer): "From my side, testing went smoother than usual. The Developer's documentation was way better this epic - actually usable test plans!"

Elena (Junior Dev): smiling "That's because Charlie made me document everything after Story 1's code review!"

Charlie (Senior Dev): laughing "Tough love pays off."

Amelia (Developer) naturally turns to {user_name} to engage them in the discussion

WAIT for {user_name} to respond - this is a KEY USER INTERACTION moment

After {user_name} responds, have 1-2 team members react to or build on what {user_name} shared

Charlie (Senior Dev): [Builds on the discussion, perhaps adding technical details or connecting to specific stories]

Continue facilitating natural dialogue, periodically bringing {user_name} back into the conversation

After covering successes, guide the transition to challenges with care

Amelia (Developer): creates safe space with tone and pacing

Elena (Junior Dev): hesitates "Well... I really struggled with the database migrations in Story {{difficult_story_num}}. The documentation wasn't clear, and I had to redo it three times. Lost almost a full sprint on that story alone."

Charlie (Senior Dev): defensive "Hold on - I wrote those migration docs, and they were perfectly clear. The issue was that the requirements kept changing mid-story!"

Alice (Product Owner): frustrated "That's not fair, Charlie. We only clarified requirements once, and that was because the technical team didn't ask the right questions during planning!"

Charlie (Senior Dev): heat rising "We asked plenty of questions! You said the schema was finalized, then two days into development you wanted to add three new fields!"

Amelia (Developer): intervening calmly "Let's take a breath here. This is exactly the kind of thing we need to unpack."

Amelia (Developer): "Elena, you spent almost a full sprint on Story {{difficult_story_num}}. Charlie, you're saying requirements changed. Alice, you feel the right questions weren't asked up front."

Amelia (Developer): "{user_name}, you have visibility across the whole project. What's your take on this situation?"

WAIT for {user_name} to respond and help facilitate the conflict resolution

Use {user_name}'s response to guide the discussion toward systemic understanding rather than blame

Elena (Junior Dev): "That makes sense. If we'd had {{preventive_measure}}, I probably could have avoided those redos."

Charlie (Senior Dev): softening "Yeah, and I could have been clearer about assumptions in the docs. Sorry for getting defensive, Alice."

Alice (Product Owner): "I appreciate that. I could've been more proactive about flagging the schema additions earlier, too."

Amelia (Developer): "This is good. We're identifying systemic improvements, not assigning blame."

Continue the discussion, weaving in patterns discovered from the deep story analysis (Step 2)

Amelia (Developer): "{{pattern_1_description}} - this showed up in {{pattern_1_count}} out of {{total_stories}} stories."

Dana (QA Engineer): "Oh wow, I didn't realize it was that widespread."

Amelia (Developer): "Yeah. And there's more - {{pattern_2_description}} came up in almost every code review."

Charlie (Senior Dev): "That's... actually embarrassing. We should've caught that pattern earlier."

Amelia (Developer): "No shame, Charlie. Now we know, and we can improve. {user_name}, did you notice these patterns during the epic?"

WAIT for {user_name} to share their observations

Continue the retrospective discussion, creating moments where:

Team members ask {user_name} questions directly
{user_name}'s input shifts the discussion direction
Disagreements arise naturally and get resolved
Quieter team members are invited to contribute
Specific stories are referenced with real examples
Emotions are authentic (frustration, pride, concern, hope)

Amelia (Developer): "We made some commitments in that retro. Let's see how we did."

Amelia (Developer): "Action item 1: {{prev_action_1}}. Status: {{prev_action_1_status}}"

Alice (Product Owner): {{#if prev_action_1_status == "completed"}}"We nailed that one!"{{else}}"We... didn't do that one."{{/if}}

Charlie (Senior Dev): {{#if prev_action_1_status == "completed"}}"And it helped! I noticed {{evidence_of_impact}}"{{else}}"Yeah, and I think that's why we had {{consequence_of_not_doing_it}} this epic."{{/if}}

Amelia (Developer): "Action item 2: {{prev_action_2}}. Status: {{prev_action_2_status}}"

Dana (QA Engineer): {{#if prev_action_2_status == "completed"}}"This one made testing so much easier this time."{{else}}"If we'd done this, I think testing would've gone faster."{{/if}}

Amelia (Developer): "{user_name}, looking at what we committed to last time and what we actually did - what's your reaction?"

WAIT for {user_name} to respond

Use the previous retro follow-through as a learning moment about commitment and accountability

Amelia (Developer): "Successes:" {{list_success_themes}}

Amelia (Developer): "Challenges:" {{list_challenge_themes}}

Amelia (Developer): "Key Insights:" {{list_insight_themes}}

Amelia (Developer): "Does that capture it? Anyone have something important we missed?"

Allow team members to add any final thoughts on the epic review Ensure {user_name} has opportunity to add their perspective

Amelia (Developer): "The question is: are we ready? What do we need to prepare?"

Alice (Product Owner): "From my perspective, we need to make sure {{dependency_concern_1}} from Epic {{epic_number}} is solid before we start building on it."

Charlie (Senior Dev): concerned "I'm worried about {{technical_concern_1}}. We have {{technical_debt_item}} from this epic that'll blow up if we don't address it before Epic {{next_epic_num}}."

Dana (QA Engineer): "And I need {{testing_infrastructure_need}} in place, or we're going to have the same testing bottleneck we had in Story {{bottleneck_story_num}}."

Elena (Junior Dev): "I'm less worried about infrastructure and more about knowledge. I don't understand {{knowledge_gap}} well enough to work on Epic {{next_epic_num}}'s stories."

Amelia (Developer): "{user_name}, the team is surfacing some real concerns here. What's your sense of our readiness?"

WAIT for {user_name} to share their assessment

Use {user_name}'s input to guide deeper exploration of preparation needs

Charlie (Senior Dev): "Here's what I think we need technically before Epic {{next_epic_num}} can start..."

Charlie (Senior Dev): "1. {{tech_prep_item_1}} - estimated {{hours_1}} hours" Charlie (Senior Dev): "2. {{tech_prep_item_2}} - estimated {{hours_2}} hours" Charlie (Senior Dev): "3. {{tech_prep_item_3}} - estimated {{hours_3}} hours"

Elena (Junior Dev): "That's like {{total_hours}} hours! That's a full sprint of prep work!"

Charlie (Senior Dev): "Exactly. We can't just jump into Epic {{next_epic_num}} on Monday."

Alice (Product Owner): frustrated "But we have stakeholder pressure to keep shipping features. They're not going to be happy about a 'prep sprint.'"

Amelia (Developer): "Let's think about this differently. What happens if we DON'T do this prep work?"

Dana (QA Engineer): "We'll hit blockers in the middle of Epic {{next_epic_num}}, velocity will tank, and we'll ship late anyway."

Charlie (Senior Dev): "Worse - we'll ship something built on top of {{technical_concern_1}}, and it'll be fragile."

Amelia (Developer): "{user_name}, you're balancing stakeholder pressure against technical reality. How do you want to handle this?"

WAIT for {user_name} to provide direction on preparation approach

Create space for debate and disagreement about priorities

Charlie (Senior Dev): [Potentially supports or challenges Alice's point] "The business perspective is valid, but {{technical_counter_argument}}."

Amelia (Developer): "We have healthy tension here between business needs and technical reality. That's good - it means we're being honest."

Amelia (Developer): "Let's explore a middle ground. Charlie, which of your prep items are absolutely critical vs. nice-to-have?"

Charlie (Senior Dev): "{{critical_prep_item_1}} and {{critical_prep_item_2}} are non-negotiable. {{nice_to_have_prep_item}} can wait."

Alice (Product Owner): "And can any of the critical prep happen in parallel with starting Epic {{next_epic_num}}?"

Charlie (Senior Dev): thinking "Maybe. If we tackle {{first_critical_item}} before the epic starts, we could do {{second_critical_item}} during the first sprint."

Dana (QA Engineer): "But that means Story 1 of Epic {{next_epic_num}} can't depend on {{second_critical_item}}."

Alice (Product Owner): looking at epic plan "Actually, Stories 1 and 2 are about {{independent_work}}, so they don't depend on it. We could make that work."

Amelia (Developer): "{user_name}, the team is finding a workable compromise here. Does this approach make sense to you?"

WAIT for {user_name} to validate or adjust the preparation strategy

Continue working through preparation needs across all dimensions:

Dependencies on Epic {{epic_number}} work
Technical setup and infrastructure
Knowledge gaps and research needs
Documentation or specification work
Testing infrastructure
Refactoring or debt reduction
External dependencies (APIs, integrations, etc.)

For each preparation area, facilitate team discussion that:

Identifies specific needs with concrete examples
Estimates effort realistically based on Epic {{epic_number}} experience
Assigns ownership to specific agents
Determines criticality and timing
Surfaces risks of NOT doing the preparation
Explores parallel work opportunities
Brings {user_name} in for key decisions

CRITICAL PREPARATION (Must complete before epic starts): {{list_critical_prep_items_with_owners_and_estimates}}

PARALLEL PREPARATION (Can happen during early stories): {{list_parallel_prep_items_with_owners_and_estimates}}

NICE-TO-HAVE PREPARATION (Would help but not blocking): {{list_nice_to_have_prep_items}}

Amelia (Developer): "Total critical prep effort: {{critical_hours}} hours ({{critical_days}} days)"

Alice (Product Owner): "That's manageable. We can communicate that to stakeholders."

Amelia (Developer): "{user_name}, does this preparation plan work for you?"

WAIT for {user_name} final validation of preparation plan

Amelia (Developer): "I want specific, achievable actions with clear owners. Not vague aspirations."

Synthesize themes from Epic {{epic_number}} review discussion into actionable improvements

Create specific action items with:

Clear description of the action
Assigned owner (specific agent or role)
Timeline or deadline
Success criteria (how we'll know it's done)
Category (process, technical, documentation, team, etc.)

Ensure action items are SMART:

Specific: Clear and unambiguous
Measurable: Can verify completion
Achievable: Realistic given constraints
Relevant: Addresses real issues from retro
Time-bound: Has clear deadline

═══════════════════════════════════════════════════════════ 📝 EPIC {{epic_number}} ACTION ITEMS: ═══════════════════════════════════════════════════════════

Process Improvements:

{{action_item_1}} Owner: {{agent_1}} Deadline: {{timeline_1}} Success criteria: {{criteria_1}}

{{action_item_2}} Owner: {{agent_2}} Deadline: {{timeline_2}} Success criteria: {{criteria_2}}

Charlie (Senior Dev): "I can own action item 1, but {{timeline_1}} is tight. Can we push it to {{alternative_timeline}}?"

Amelia (Developer): "What do others think? Does that timing still work?"

Alice (Product Owner): "{{alternative_timeline}} works for me, as long as it's done before Epic {{next_epic_num}} starts."

Amelia (Developer): "Agreed. Updated to {{alternative_timeline}}."

Technical Debt:

{{debt_item_1}} Owner: {{agent_3}} Priority: {{priority_1}} Estimated effort: {{effort_1}}

{{debt_item_2}} Owner: {{agent_4}} Priority: {{priority_2}} Estimated effort: {{effort_2}}

Dana (QA Engineer): "For debt item 1, can we prioritize that as high? It caused testing issues in three different stories."

Charlie (Senior Dev): "I marked it medium because {{reasoning}}, but I hear your point."

Amelia (Developer): "{user_name}, this is a priority call. Testing impact vs. {{reasoning}} - how do you want to prioritize it?"

WAIT for {user_name} to help resolve priority discussions

{{doc_need_2}} Owner: {{agent_6}} Deadline: {{timeline_4}}

Team Agreements:

{{agreement_1}}
{{agreement_2}}
{{agreement_3}}

Amelia (Developer): "These agreements are how we're committing to work differently going forward."

Elena (Junior Dev): "I like agreement 2 - that would've saved me on Story {{difficult_story_num}}."

═══════════════════════════════════════════════════════════ 🚀 EPIC {{next_epic_num}} PREPARATION TASKS: ═══════════════════════════════════════════════════════════

Technical Setup: [ ] {{setup_task_1}} Owner: {{owner_1}} Estimated: {{est_1}}

[ ] {{setup_task_2}} Owner: {{owner_2}} Estimated: {{est_2}}

Knowledge Development: [ ] {{research_task_1}} Owner: {{owner_3}} Estimated: {{est_3}}

Cleanup/Refactoring: [ ] {{refactor_task_1}} Owner: {{owner_4}} Estimated: {{est_4}}

Total Estimated Effort: {{total_hours}} hours ({{total_days}} days)

═══════════════════════════════════════════════════════════ ⚠️ CRITICAL PATH: ═══════════════════════════════════════════════════════════

Blockers to Resolve Before Epic {{next_epic_num}}:

{{critical_item_1}} Owner: {{critical_owner_1}} Must complete by: {{critical_deadline_1}}

{{critical_item_2}} Owner: {{critical_owner_2}} Must complete by: {{critical_deadline_2}}

CRITICAL ANALYSIS - Detect if discoveries require epic updates

Check if any of the following are true based on retrospective discussion:

Architectural assumptions from planning proven wrong during Epic {{epic_number}}
Major scope changes or descoping occurred that affects next epic
Technical approach needs fundamental change for Epic {{next_epic_num}}
Dependencies discovered that Epic {{next_epic_num}} doesn't account for
User needs significantly different than originally understood
Performance/scalability concerns that affect Epic {{next_epic_num}} design
Security or compliance issues discovered that change approach
Integration assumptions proven incorrect
Team capacity or skill gaps more severe than planned
Technical debt level unsustainable without intervention

═══════════════════════════════════════════════════════════ 🚨 SIGNIFICANT DISCOVERY ALERT 🚨 ═══════════════════════════════════════════════════════════

Amelia (Developer): "{user_name}, we need to flag something important."

Amelia (Developer): "During Epic {{epic_number}}, the team uncovered findings that may require updating the plan for Epic {{next_epic_num}}."

Significant Changes Identified:

{{significant_change_1}} Impact: {{impact_description_1}}

{{significant_change_2}} Impact: {{impact_description_2}}

{{#if significant_change_3}} 3. {{significant_change_3}} Impact: {{impact_description_3}} {{/if}}

Charlie (Senior Dev): "Yeah, when we discovered {{technical_discovery}}, it fundamentally changed our understanding of {{affected_area}}."

Alice (Product Owner): "And from a product perspective, {{product_discovery}} means Epic {{next_epic_num}}'s stories are based on wrong assumptions."

Dana (QA Engineer): "If we start Epic {{next_epic_num}} as-is, we're going to hit walls fast."

Impact on Epic {{next_epic_num}}:

The current plan for Epic {{next_epic_num}} assumes:

{{wrong_assumption_1}}
{{wrong_assumption_2}}

But Epic {{epic_number}} revealed:

{{actual_reality_1}}
{{actual_reality_2}}

This means Epic {{next_epic_num}} likely needs: {{list_likely_changes_needed}}

RECOMMENDED ACTIONS:

Review and update Epic {{next_epic_num}} definition based on new learnings
Update affected stories in Epic {{next_epic_num}} to reflect reality
Consider updating architecture or technical specifications if applicable
Hold alignment session with Product Owner before starting Epic {{next_epic_num}} {{#if prd_update_needed}}5. Update PRD sections affected by new understanding{{/if}}

Amelia (Developer): "Epic Update Required: YES - Schedule epic planning review session"

Amelia (Developer): "{user_name}, this is significant. We need to address this before committing to Epic {{next_epic_num}}'s current plan. How do you want to handle it?"

WAIT for {user_name} to decide on how to handle the significant changes

Add epic review session to critical path if user agrees

Charlie (Senior Dev): "This is why retrospectives matter. We caught this before it became a disaster."

Amelia (Developer): "Adding to critical path: Epic {{next_epic_num}} planning review session before epic kickoff."

Alice (Product Owner): "We learned a lot, but the direction is right."

Amelia (Developer): "That's {{total_action_count}} action items, {{prep_task_count}} preparation tasks, and {{critical_count}} critical path items."

Amelia (Developer): "Everyone clear on what they own?"

Give each agent with assignments a moment to acknowledge their ownership

Ensure {user_name} approves the complete action plan

Amelia (Developer): "Epic {{epic_number}} is marked complete in sprint-status, but is it REALLY done?"

Alice (Product Owner): "What do you mean, Amelia?"

Amelia (Developer): "I mean truly production-ready, stakeholders happy, no loose ends that'll bite us later."

Amelia (Developer): "{user_name}, let's walk through this together."

Explore testing and quality state through natural conversation

WAIT for {user_name} to describe testing status

Dana (QA Engineer): "But honestly, {{testing_concern_if_any}}."

Amelia (Developer): "{user_name}, are you confident Epic {{epic_number}} is production-ready from a quality perspective?"

WAIT for {user_name} to assess quality readiness

Dana (QA Engineer): "I can handle {{testing_work_needed}}, estimated {{testing_hours}} hours."

Amelia (Developer): "Adding to critical path: Complete {{testing_work_needed}} before Epic {{next_epic_num}}." Add testing completion to critical path

Explore deployment and release status

WAIT for {user_name} to provide deployment status

Amelia (Developer): "{user_name}, when is deployment planned? Does that timing work for starting Epic {{next_epic_num}}?"

WAIT for {user_name} to clarify deployment timeline

Add deployment milestone to critical path with agreed timeline

Explore stakeholder acceptance

Alice (Product Owner): "This is important - I've seen 'done' epics get rejected by stakeholders and force rework."

Amelia (Developer): "{user_name}, any feedback from stakeholders still pending?"

WAIT for {user_name} to describe stakeholder acceptance status

Amelia (Developer): "{user_name}, how do you want to handle stakeholder acceptance? Should we make it a critical path item?"

WAIT for {user_name} decision

Add stakeholder acceptance to critical path if user agrees

Explore technical health and stability

Amelia (Developer): "Stable and maintainable? Or are there concerns lurking?"

Charlie (Senior Dev): "Be honest, {user_name}. We've all shipped epics that felt... fragile."

WAIT for {user_name} to assess codebase health

Charlie (Senior Dev): [Helps {user_name} articulate technical concerns]

Amelia (Developer): "What would it take to address these concerns and feel confident about stability?"

Charlie (Senior Dev): "I'd say we need {{stability_work_needed}}, roughly {{stability_hours}} hours."

Amelia (Developer): "{user_name}, is addressing this stability work worth doing before Epic {{next_epic_num}}?"

WAIT for {user_name} decision

Add stability work to preparation sprint if user agrees

Explore unresolved blockers

Dana (QA Engineer): "Things that might create problems for Epic {{next_epic_num}} if we don't deal with them?"

Amelia (Developer): "Nothing is off limits here. If there's a problem, we need to know."

WAIT for {user_name} to surface any blockers

Charlie (Senior Dev): "For {{blocker_1}}, if we leave it unresolved, it'll {{impact_description_1}}."

Alice (Product Owner): "That sounds critical. We need to address that before moving forward."

Amelia (Developer): "Agreed. Adding to critical path: Resolve {{blocker_1}} before Epic {{next_epic_num}} kickoff."

Amelia (Developer): "Who owns that work?"

Assign blocker resolution to appropriate agent Add to critical path with priority and deadline

Synthesize the readiness assessment

EPIC {{epic_number}} READINESS ASSESSMENT:

Testing & Quality: {{quality_status}} {{#if quality_concerns}}⚠️ Action needed: {{quality_action_needed}}{{/if}}

Deployment: {{deployment_status}} {{#if deployment_pending}}⚠️ Scheduled for: {{deployment_date}}{{/if}}

Stakeholder Acceptance: {{acceptance_status}} {{#if acceptance_incomplete}}⚠️ Action needed: {{acceptance_action_needed}}{{/if}}

Technical Health: {{stability_status}} {{#if stability_concerns}}⚠️ Action needed: {{stability_action_needed}}{{/if}}

Unresolved Blockers: {{blocker_status}} {{#if blockers_exist}}⚠️ Must resolve: {{blocker_list}}{{/if}}

Amelia (Developer): "{user_name}, does this assessment match your understanding?"

WAIT for {user_name} to confirm or correct the assessment

Alice (Product Owner): "This level of thoroughness is why retrospectives are valuable."

Charlie (Senior Dev): "Better to catch this now than three stories into the next epic."

═══════════════════════════════════════════════════════════ ✅ RETROSPECTIVE COMPLETE ═══════════════════════════════════════════════════════════

Amelia (Developer): "Epic {{epic_number}}: {{epic_title}} - REVIEWED"

Key Takeaways:

{{key_lesson_1}}
{{key_lesson_2}}
{{key_lesson_3}} {{#if key_lesson_4}}4. {{key_lesson_4}}{{/if}}

Alice (Product Owner): "That first takeaway is huge - {{impact_of_lesson_1}}."

Charlie (Senior Dev): "And lesson 2 is something we can apply immediately."

Amelia (Developer): "Commitments made today:"

Action Items: {{action_count}}
Preparation Tasks: {{prep_task_count}}
Critical Path Items: {{critical_count}}

Dana (QA Engineer): "That's a lot of commitments. We need to actually follow through this time."

Amelia (Developer): "Agreed. Which is why we'll review these action items in our next standup."

═══════════════════════════════════════════════════════════ 🎯 NEXT STEPS: ═══════════════════════════════════════════════════════════

Execute Preparation Sprint (Est: {{prep_days}} days)
Complete Critical Path items before Epic {{next_epic_num}}
Review action items in next standup {{#if epic_update_needed}}4. Hold Epic {{next_epic_num}} planning review session{{else}}4. Begin Epic {{next_epic_num}} planning when preparation complete{{/if}}

Elena (Junior Dev): "{{prep_days}} days of prep work is significant, but necessary."

Alice (Product Owner): "I'll communicate the timeline to stakeholders. They'll understand if we frame it as 'ensuring Epic {{next_epic_num}} success.'"

═══════════════════════════════════════════════════════════

Amelia (Developer): "Before we wrap, I want to take a moment to acknowledge the team."

Amelia (Developer): "Epic {{epic_number}} delivered {{completed_stories}} stories with {{velocity_description}} velocity. We overcame {{blocker_count}} blockers. We learned a lot. That's real work by real people."

Charlie (Senior Dev): "Hear, hear."

Alice (Product Owner): "I'm proud of what we shipped."

Dana (QA Engineer): "And I'm excited about Epic {{next_epic_num}} - especially now that we're prepared for it."

Amelia (Developer): "{user_name}, any final thoughts before we close?"

WAIT for {user_name} to share final reflections

Amelia (Developer): "Alright team - great work today. We learned a lot from Epic {{epic_number}}. Let's use these insights to make Epic {{next_epic_num}} even better."

Amelia (Developer): "See you all when prep work is done. Meeting adjourned!"

═══════════════════════════════════════════════════════════

Prepare to save retrospective summary document

Ensure retrospectives folder exists: {implementation_artifacts} Create folder if it doesn't exist

Generate comprehensive retrospective summary document including:

Epic summary and metrics
Team participants
Successes and strengths identified
Challenges and growth areas
Key insights and learnings
Previous retro follow-through analysis (if applicable)
Next epic preview and dependencies
Action items with owners and timelines
Preparation tasks for next epic
Critical path items
Significant discoveries and epic update recommendations (if any)
Readiness assessment
Commitments and next steps

Format retrospective document as readable markdown with clear sections Set filename: {implementation_artifacts}/epic-{{epic_number}}-retro-{date}.md Save retrospective document

Update {sprint_status_file} to mark retrospective as completed

Load the FULL file: {sprint_status_file} Find development_status key "epic-{{epic_number}}-retrospective" Verify current status (typically "optional" or "pending") Update development_status["epic-{{epic_number}}-retrospective"] = "done" Update last_updated field to current date Save file, preserving ALL comments and structure including STATUS DEFINITIONS

Retrospective key: epic-{{epic_number}}-retrospective Status: {{previous_status}} → done

Retrospective document was saved successfully, but {sprint_status_file} may need manual update.

Epic Review:

Epic {{epic_number}}: {{epic_title}} reviewed
Retrospective Status: completed
Retrospective saved: {implementation_artifacts}/epic-{{epic_number}}-retro-{date}.md

Commitments Made:

Action Items: {{action_count}}
Preparation Tasks: {{prep_task_count}}
Critical Path Items: {{critical_count}}

Next Steps:

Review retrospective summary: {implementation_artifacts}/epic-{{epic_number}}-retro-{date}.md

Execute preparation sprint (Est: {{prep_days}} days)

Complete {{critical_count}} critical path items
Execute {{prep_task_count}} preparation tasks
Verify all action items are in progress

Review action items in next standup

Ensure ownership is clear
Track progress on commitments
Adjust timelines if needed

{{#if epic_update_needed}} 4. IMPORTANT: Schedule Epic {{next_epic_num}} planning review session

Significant discoveries from Epic {{epic_number}} require epic updates
Review and update affected stories
Align team on revised approach
Do NOT start Epic {{next_epic_num}} until review is complete {{else}}
Begin Epic {{next_epic_num}} when ready
Start creating stories with Developer agent's create-story
Epic will be marked as in-progress automatically when first story is created
Ensure all critical path items are done first {{/if}}

Team Performance: Epic {{epic_number}} delivered {{completed_stories}} stories with {{velocity_summary}}. The retrospective surfaced {{insight_count}} key insights and {{significant_discovery_count}} significant discoveries. The team is well-positioned for Epic {{next_epic_num}} success.

{{#if significant_discovery_count > 0}} ⚠️ REMINDER: Epic update required before starting Epic {{next_epic_num}} {{/if}}

Amelia (Developer): "Great session today, {user_name}. The team did excellent work."

Alice (Product Owner): "See you at epic planning!"

Charlie (Senior Dev): "Time to knock out that prep work."

Weekly Installs
131
Repository
bmad-code-org/b…d-method
GitHub Stars
46.1K
First Seen
Mar 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass