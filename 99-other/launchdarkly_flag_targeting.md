---
title: launchdarkly-flag-targeting
url: https://skills.sh/launchdarkly/agent-skills/launchdarkly-flag-targeting
---

# launchdarkly-flag-targeting

skills/launchdarkly/agent-skills/launchdarkly-flag-targeting
launchdarkly-flag-targeting
Installation
$ npx skills add https://github.com/launchdarkly/agent-skills --skill launchdarkly-flag-targeting
SKILL.md
LaunchDarkly Flag Targeting & Rollout

You're using a skill that will guide you through changing who sees what for a feature flag. Your job is to understand the current state of the flag, figure out the right targeting approach for what the user wants, make the changes safely, and verify the resulting state.

Prerequisites

This skill requires the remotely hosted LaunchDarkly MCP server to be configured in your environment.

Required MCP tools:

get-flag: understand current state before making changes
toggle-flag: turn targeting on or off for a flag in an environment
update-rollout: change the default rule (fallthrough) variation or percentage rollout
update-targeting-rules: add, remove, or modify custom targeting rules
update-individual-targets: add or remove specific users/contexts from individual targeting

Optional MCP tools:

copy-flag-config: copy targeting configuration from one environment to another
create-approval-request: create an approval request when direct changes are blocked
list-approval-requests: check on pending approval requests for a flag
apply-approval-request: apply an already-approved approval request
Core Concept: Evaluation Order

Before making any targeting changes, understand how LaunchDarkly evaluates flags. This determines what your changes actually do:

Flag is OFF -> Serve the offVariation to everyone. Nothing else matters.
Individual targets -> If the context matches a specific target list, serve that variation. Highest priority.
Custom rules -> Evaluate rules top-to-bottom. First matching rule wins.
Default rule (fallthrough) -> If nothing else matched, serve this variation or rollout.

This means: if you add a targeting rule but the flag is OFF, nobody sees the change. If you set a percentage rollout on the default rule but there's an individual target, that targeted user bypasses the rollout.

Workflow
Step 1: Understand Current State

Before changing anything, check what's already configured.

Confirm the environment. "Turn it on" without specifying an environment is ambiguous. Always confirm which environment the user means. Default to asking rather than assuming.
Fetch the flag. Use get-flag with the target environment to see:
on: Is targeting currently enabled?
fallthrough: What's the default rule? (variation or percentage rollout)
offVariation: What serves when the flag is off?
rules: Any custom targeting rules?
targets: Any individually targeted users/contexts?
prerequisites: Any flags this depends on?
Assess complexity. A flag with no rules and no individual targets is simple. A flag with multiple rules, targets, and prerequisites needs more care.
Step 2: Determine the Right Approach

Based on what the user wants and what you found, choose the right tool and strategy. See Targeting Patterns for the full reference.

Common scenarios:

User wants	Tool	Notes
"Turn it on"	toggle-flag with on: true	Simplest change
"Turn it off"	toggle-flag with on: false	Serves offVariation to everyone
"Roll out to X%"	update-rollout with rolloutType: "percentage"	Weights must sum to 100
"Enable for beta users"	update-targeting-rules: add a rule with clause	Rules are ANDed within, ORed between
"Add specific users"	update-individual-targets	Highest priority, overrides all rules
"Full rollout"	update-rollout with rolloutType: "variation"	Serve one variation to everyone
"Copy from staging"	copy-flag-config	Promote tested config to production
Step 3: Run the Safety Checklist

Before applying changes, especially in production, run through the Safety Checklist. The key checks:

Right environment? Double-check you're targeting the intended environment.
Approval required? Some environments require approval workflows. If any mutation tool returns requiresApproval: true:
Inform the user that this environment requires approvals.
Share the approvalUrl if provided.
Offer to create an approval request using create-approval-request with the same instructions (returned in the instructions field of the response).
Do NOT attempt to bypass approval or auto-approve.
See Approval Workflows for the full process.
Prerequisite flags? If this flag has prerequisites, they must be met before targeting works as expected.
Rule ordering impact? If adding rules, consider where they fall in evaluation order. Rules evaluate top-to-bottom, first match wins.
Include a comment. Always add an audit trail comment, especially for production changes.
Step 4: Apply Changes

Use the appropriate tool for the change. Key notes:

toggle-flag: Specify on: true or on: false, the env, and a comment.
update-rollout: Use rolloutType: "percentage" with human-friendly weights (e.g., 80 for 80%) that sum to 100, or rolloutType: "variation" with a variationIndex.
update-targeting-rules: Instructions support addRule, removeRule, updateRuleVariationOrRollout, addClauses, removeClauses, reorderRules.
update-individual-targets: Instructions support addTargets, removeTargets, addContextTargets, removeContextTargets, replaceTargets.

See Targeting Patterns for detailed instruction examples.

Step 5: Verify

After applying changes, confirm the result:

Fetch the updated flag. Use get-flag again to verify the new state.
Confirm what the user expects. Describe the resulting targeting in plain language:
"The flag is now ON in production, serving true to 25% of users and false to 75%."
"Beta users now see variation A. Everyone else gets the default (variation B)."
Check for side effects. If there are rules or individual targets, make sure the change interacts correctly with them.
Handling Approval-Required Environments

When any mutation tool returns requiresApproval: true, the direct change was blocked because the environment requires approvals. Follow the Approval Workflows reference to:

Create an approval request with create-approval-request using the instructions from the blocked response
Inform the user about the pending approval and share the approval request details
Check on approval status later with list-approval-requests if requested
Apply the request with apply-approval-request once a reviewer has approved it (reviewStatus is "approved")
Verify the result with get-flag after applying
Important Context
update-rollout uses human-friendly percentages. Pass 80 for 80%, not 80000. The tool handles the internal weight conversion.
Weights must sum to 100. For percentage rollouts, the weights across all variations must total exactly 100.
Rule ordering matters. Rules evaluate top-to-bottom. Reordering rules can change behavior without changing any individual rule.
Individual targets are highest priority. They override all rules and the default. Adding someone as an individual target means rules don't apply to them.
"Launched" flags are still ON. A flag with status "launched" is serving a single variation to everyone. If you want to remove the flag, use the cleanup skill, not targeting changes.
References
Targeting Patterns: Rollout strategies, rule construction, individual targeting, and cross-environment copying
Safety Checklist: Pre-change verification, approval workflows, environment awareness
Approval Workflows: Creating, checking, and applying approval requests
Weekly Installs
367
Repository
launchdarkly/ag…t-skills
GitHub Stars
7
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass