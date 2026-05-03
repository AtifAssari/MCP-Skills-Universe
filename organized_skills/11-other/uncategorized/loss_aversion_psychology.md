---
rating: ⭐⭐⭐
title: loss-aversion-psychology
url: https://skills.sh/flpbalada/my-opencode-config/loss-aversion-psychology
---

# loss-aversion-psychology

skills/flpbalada/my-opencode-config/loss-aversion-psychology
loss-aversion-psychology
Installation
$ npx skills add https://github.com/flpbalada/my-opencode-config --skill loss-aversion-psychology
SKILL.md
Loss Aversion Psychology - Losses Loom Larger Than Gains

Loss Aversion is a cognitive bias discovered by Daniel Kahneman and Amos Tversky showing that people feel losses approximately twice as strongly as equivalent gains. This asymmetry profoundly influences decision-making and behavior.

When to Use This Skill
Designing retention and anti-churn features
Crafting pricing and upgrade messaging
Creating urgency in conversion funnels
Building streak and progress features
Writing copy for landing pages
Framing feature benefits
Core Concepts
The 2:1 Ratio
        Psychological Impact
              ^
              |         Gains
              |        /
              |      /
     +--------|----/---------> Value
              |  /
           Loss|/
              |
              |  The loss curve is ~2x steeper
              v


A $100 loss feels as bad as a $200 gain feels good.

Prospect Theory Framework
Concept	Description	Example
Reference Point	Current state as baseline	"You currently have X"
Loss Frame	Emphasis on what could be lost	"Don't lose your progress"
Gain Frame	Emphasis on what could be gained	"Get 50% more"
Endowment Effect	Valuing owned things higher	Free trial creates ownership
When Loss Framing Works Best
Situation	Loss Frame Effective?
High stakes decisions	Yes
Preventing bad outcomes	Yes
Risk-averse audiences	Yes
Building habits	Yes
Low-involvement decisions	Less effective
Exploratory behavior	Less effective
Analysis Framework
Step 1: Identify Loss Opportunities

Map user journey for potential loss frames:

Stage	What User Has	Potential Loss
Trial	Access to features	Losing access
Active	Progress/data	Losing progress
At-risk	Streak/status	Breaking streak
Churned	History/investment	Losing history
Step 2: Choose Frame Appropriately
Decision: Frame as loss or gain?

Consider:
├── User relationship stage
│   └── New users: Gains more welcoming
│   └── Existing users: Losses more motivating
├── Action reversibility
│   └── Reversible: Lighter touch OK
│   └── Irreversible: Loss frame powerful
└── Ethical considerations
    └── Does this genuinely help the user?

Step 3: Implement Ethically
Approach	Ethical	Manipulative
"Your streak will reset"	Honest reminder	Manufactured guilt
"Unused credits expire"	Clear policy	Hidden deadline
"Limited time offer"	Genuine scarcity	Fake urgency
Output Template
## Loss Aversion Analysis

**Feature/Message:** [Name] **Date:** [Date]

### Current Framing

**As gain:** [Current copy/design] **User response:** [Current metrics]

### Loss Frame Opportunity

**What user has:** [Established value] **Potential loss:** [What could be lost]
**Loss frame version:** [Proposed copy/design]

### Ethical Check

- [ ] User genuinely benefits from taking action
- [ ] Loss is real, not manufactured
- [ ] Messaging is honest and transparent
- [ ] Would we be comfortable if users knew the psychology?

### Implementation Plan

| Element  | Current   | Proposed | Expected Impact |
| -------- | --------- | -------- | --------------- |
| [Copy 1] | [Text]    | [Text]   | [Estimate]      |
| [Design] | [Current] | [Change] | [Estimate]      |

Real-World Examples
Example 1: Duolingo Streaks

Mechanism: Users build daily learning streaks Loss frame: "Don't lose your 47-day streak!" Psychology:

Streak = accumulated investment (endowment)
Breaking it = losing days of effort
Effect: 2x stronger than "Build a 48-day streak!"
Example 2: LinkedIn Profile Completion

Gain frame: "Complete your profile to get more views" Loss frame: "You're missing out on 40% more profile views"

The loss frame outperforms because it highlights what you're currently losing.

Example 3: Trial Expiration

Weak: "Your trial ends tomorrow" Strong: "Tomorrow you'll lose access to:

47 saved projects
12 team members
All your custom settings"

Making the loss concrete and specific amplifies the effect.

Ethical Guidelines
Do
Use loss framing for genuinely beneficial actions
Be honest about what's at stake
Give users real control and options
Balance loss frames with positive experiences
Test that users feel good after taking action
Avoid
Manufacturing fake urgency or scarcity
Guilt-tripping for engagement metrics
Hiding information to create loss anxiety
Using loss aversion on vulnerable users
Dark patterns that exploit psychology
The Ethics Test

Ask: "If users knew exactly how this works psychologically, would they:

Thank us for the helpful reminder?
Feel manipulated and resentful?"

If (2), reconsider the approach.

Best Practices
Effective Loss Messaging
Element	Example
Specific	"Lose your 23 saved items" not "Lose your data"
Immediate	"Expires tonight" not "Expires soon"
Personal	"Your progress" not "Progress"
Recoverable	Show how to prevent the loss
Timing Matters
Timing	Effectiveness
Too early	Feels irrelevant, ignored
Just right	Motivates action
Too late	Creates resentment
After loss	Recovery opportunity
Integration with Other Methods
Method	Combined Use
Hooked Model	Investment phase creates loss potential
Fogg Behavior Model	Loss increases motivation
Cognitive Biases	Combine with other biases carefully
Progressive Disclosure	Reveal loss implications gradually
Resources
Thinking, Fast and Slow - Daniel Kahneman
Predictably Irrational - Dan Ariely
Prospect Theory Original Paper - Kahneman & Tversky
Weekly Installs
25
Repository
flpbalada/my-op…e-config
GitHub Stars
239
First Seen
Jan 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass