---
rating: ⭐⭐
title: sf-datacloud-segment
url: https://skills.sh/jaganpro/sf-skills/sf-datacloud-segment
---

# sf-datacloud-segment

skills/jaganpro/sf-skills/sf-datacloud-segment
sf-datacloud-segment
Installation
$ npx skills add https://github.com/jaganpro/sf-skills --skill sf-datacloud-segment
SKILL.md
sf-datacloud-segment: Data Cloud Segment Phase

Use this skill when the user needs audience and insight work: segments, calculated insights, publish workflows, member counts, or troubleshooting Data Cloud segment SQL.

When This Skill Owns the Task

Use sf-datacloud-segment when the work involves:

sf data360 segment *
sf data360 calculated-insight *
segment publish workflows
member counts and segment troubleshooting
calculated insight execution and verification

Delegate elsewhere when the user is:

still building DMOs, mappings, or identity resolution → sf-datacloud-harmonize
activating a segment downstream → sf-datacloud-act
writing read-only SQL or search-index queries → sf-datacloud-retrieve
Required Context to Gather First

Ask for or infer:

target org alias
unified DMO or base entity name
whether the user wants create, publish, inspect, or troubleshoot
whether the asset is a segment or calculated insight
expected success metric: member count, aggregate value, or publish status
Core Operating Rules
Treat Data Cloud segment SQL as distinct from CRM SOQL.
Run the shared readiness classifier before mutating audience assets: node ~/.claude/skills/sf-datacloud/scripts/diagnose-org.mjs -o <org> --phase segment --json.
Prefer reusable JSON definitions for repeatable segment and CI creation.
Use --api-version 64.0 when segment creation behavior is unstable on newer defaults.
Verify with counts or SQL after publish/run steps instead of assuming success.
Use SQL joins rather than segment members when readable member details are needed.
Recommended Workflow
1. Classify readiness for segment work
node ~/.claude/skills/sf-datacloud/scripts/diagnose-org.mjs -o <org> --phase segment --json

2. Inspect current state
sf data360 segment list -o <org> 2>/dev/null
sf data360 calculated-insight list -o <org> 2>/dev/null

3. Create with reusable JSON definitions
sf data360 segment create -o <org> -f segment.json --api-version 64.0 2>/dev/null
sf data360 calculated-insight create -o <org> -f ci.json 2>/dev/null

4. Publish or run explicitly
sf data360 segment publish -o <org> --name My_Segment 2>/dev/null
sf data360 calculated-insight run -o <org> --name Lifetime_Value 2>/dev/null

5. Verify with counts or SQL
sf data360 segment count -o <org> --name My_Segment 2>/dev/null
sf data360 query sql -o <org> --sql 'SELECT COUNT(*) FROM "UnifiedssotIndividualMain__dlm"' 2>/dev/null

High-Signal Gotchas
Segment creation can require --api-version 64.0.
segment members returns opaque IDs; use SQL joins when human-readable member details are needed.
Segment SQL is not SOQL.
Calculated insight assets and segment SQL have different limitations.
Publish/run steps may kick off asynchronous work even when the command returns quickly.
An empty segment or calculated-insight list usually means the module is reachable but unconfigured, not unavailable.
Output Format
Segment task: <segment / calculated-insight>
Action: <create / publish / inspect / troubleshoot>
Target org: <alias>
Artifacts: <definition files / commands>
Verification: <member count / query result / publish state>
Next step: <act / retrieve / follow-up>

References
README.md
../sf-datacloud/assets/definitions/calculated-insight.template.json
../sf-datacloud/assets/definitions/segment.template.json
../sf-datacloud/references/feature-readiness.md
../sf-datacloud/UPSTREAM.md
Weekly Installs
729
Repository
jaganpro/sf-skills
GitHub Stars
404
First Seen
Mar 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass