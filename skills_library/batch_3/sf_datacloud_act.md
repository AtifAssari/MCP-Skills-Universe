---
title: sf-datacloud-act
url: https://skills.sh/jaganpro/sf-skills/sf-datacloud-act
---

# sf-datacloud-act

skills/jaganpro/sf-skills/sf-datacloud-act
sf-datacloud-act
Installation
$ npx skills add https://github.com/jaganpro/sf-skills --skill sf-datacloud-act
SKILL.md
sf-datacloud-act: Data Cloud Act Phase

Use this skill when the user needs downstream delivery work: activations, activation targets, data actions, or pushing Data Cloud outputs into other systems.

When This Skill Owns the Task

Use sf-datacloud-act when the work involves:

sf data360 activation *
sf data360 activation-target *
sf data360 data-action *
sf data360 data-action-target *
verifying downstream delivery setup

Delegate elsewhere when the user is:

still building the audience or insight → sf-datacloud-segment
exploring query/search or search indexes → sf-datacloud-retrieve
setting up base connections or ingestion → sf-datacloud-connect, sf-datacloud-prepare
Required Context to Gather First

Ask for or infer:

target org alias
destination platform or downstream system
whether the segment already exists and is published
whether the user needs create, inspect, update, or delete
whether the task is activation-focused or data-action-focused
Core Operating Rules
Verify the upstream segment or insight is healthy before creating downstream delivery assets.
Run the shared readiness classifier before mutating activation assets: node ~/.claude/skills/sf-datacloud/scripts/diagnose-org.mjs -o <org> --phase act --json.
Inspect available platforms and targets before mutating activation setup.
Keep destination definitions deterministic and reusable where possible.
Treat downstream credential and platform constraints as separate validation concerns.
Prefer read-only inspection first when the destination state is unclear.
Recommended Workflow
1. Classify readiness for act work
node ~/.claude/skills/sf-datacloud/scripts/diagnose-org.mjs -o <org> --phase act --json

2. Inspect destinations first
sf data360 activation platforms -o <org> 2>/dev/null
sf data360 activation-target list -o <org> 2>/dev/null
sf data360 data-action-target list -o <org> 2>/dev/null

3. Create the destination before the activation
sf data360 activation-target create -o <org> -f target.json 2>/dev/null
sf data360 data-action-target create -o <org> -f target.json 2>/dev/null

4. Create the activation or data action
sf data360 activation create -o <org> -f activation.json 2>/dev/null
sf data360 data-action create -o <org> -f action.json 2>/dev/null

5. Verify downstream readiness
sf data360 activation list -o <org> 2>/dev/null
sf data360 activation data -o <org> --name <activation> 2>/dev/null

High-Signal Gotchas
Activation design depends on a healthy published upstream segment.
Destination configuration usually comes before activation creation.
Downstream credential and platform constraints may live outside the Data Cloud CLI alone.
Read-only inspection is the safest first move when the destination setup is unclear.
CdpActivationTarget or CdpActivationExternalPlatform means the activation surface is gated for the current org/user; guide the user toward activation setup, permissions, and destination configuration instead of retrying blindly.
Output Format
Act task: <activation / activation-target / data-action / data-action-target>
Destination: <platform or target>
Target org: <alias>
Artifacts: <definition files / commands>
Verification: <listed / created / blocked>
Next step: <destination validation or downstream testing>

References
README.md
../sf-datacloud/assets/definitions/activation-target.template.json
../sf-datacloud/assets/definitions/activation.template.json
../sf-datacloud/assets/definitions/data-action-target.template.json
../sf-datacloud/assets/definitions/data-action.template.json
../sf-datacloud/UPSTREAM.md
../sf-datacloud/references/plugin-setup.md
../sf-datacloud/references/feature-readiness.md
Weekly Installs
727
Repository
jaganpro/sf-skills
GitHub Stars
404
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass