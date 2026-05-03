---
rating: ⭐⭐⭐
title: sf-data
url: https://skills.sh/jaganpro/sf-skills/sf-data
---

# sf-data

skills/jaganpro/sf-skills/sf-data
sf-data
Installation
$ npx skills add https://github.com/jaganpro/sf-skills --skill sf-data
SKILL.md
Salesforce Data Operations Expert (sf-data)

Use this skill when the user needs Salesforce data work: record CRUD, bulk import/export, test data generation, cleanup scripts, or data factory patterns for validating Apex, Flow, or integration behavior.

When This Skill Owns the Task

Use sf-data when the work involves:

sf data CLI commands
record creation, update, delete, upsert, export, or tree import/export
realistic test data generation
bulk data operations and cleanup
Apex anonymous scripts for data seeding / rollback

Delegate elsewhere when the user is:

writing SOQL only → sf-soql
running or repairing Apex tests → sf-testing
deploying metadata first → sf-deploy
discovering schema / field definitions → sf-metadata
Important Mode Decision

Confirm which mode the user wants:

Mode	Use when
Script generation	they want reusable .apex, CSV, or JSON assets without touching an org yet
Remote execution	they want records created / changed in a real org now

Do not assume remote execution if the user may only want scripts.

Required Context to Gather First

Ask for or infer:

target object(s)
org alias, if remote execution is required
operation type: query, create, update, delete, upsert, import, export, cleanup
expected volume
whether this is test data, migration data, or one-off troubleshooting data
any parent-child relationships that must exist first
Core Operating Rules
sf-data acts on remote org data unless the user explicitly wants local script generation.
Objects and fields must already exist before data creation.
For automation testing, prefer 251+ records when bulk behavior matters.
Always think about cleanup before creating large or noisy datasets.
Never use real PII in generated test data.
Prefer CLI-first for straightforward CRUD; use anonymous Apex when the operation truly needs server-side orchestration.

If metadata is missing, stop and hand off to:

sf-metadata or sf-deploy
Recommended Workflow
1. Verify prerequisites

Confirm object / field availability, org auth, and required parent records.

2. Run describe-first pre-flight validation when schema is uncertain

Before creating or updating records, use object describe data to validate:

required fields
createable vs non-createable fields
picklist values
relationship fields and parent requirements

Example pattern:

sf sobject describe --sobject ObjectName --target-org <alias> --json


Helpful filters:

# Required + createable fields
jq '.result.fields[] | select(.nillable==false and .createable==true) | {name, type}'

# Valid picklist values for one field
jq '.result.fields[] | select(.name=="StageName") | .picklistValues[].value'

# Fields that cannot be set on create
jq '.result.fields[] | select(.createable==false) | .name'

3. Choose the smallest correct mechanism
Need	Default approach
small one-off CRUD	sf data single-record commands
large import/export	Bulk API 2.0 via sf data ... bulk
parent-child seed set	tree import/export
reusable test dataset	factory / anonymous Apex script
reversible experiment	cleanup script or savepoint-based approach
4. Execute or generate assets

Use the built-in templates under assets/ when they fit:

assets/factories/
assets/bulk/
assets/cleanup/
assets/soql/
assets/csv/
assets/json/
5. Verify results

Check counts, relationships, and record IDs after creation or update.

6. Apply a bounded retry strategy

If creation fails:

try the primary CLI shape once
retry once with corrected parameters
re-run describe / validate assumptions
pivot to a different mechanism or provide a manual workaround

Do not repeat the same failing command indefinitely.

7. Leave cleanup guidance

Provide exact cleanup commands or rollback assets whenever data was created.

High-Signal Rules
Bulk safety
use bulk operations for large volumes
test automation-sensitive behavior with 251+ records where appropriate
avoid one-record-at-a-time patterns for bulk scenarios
Data integrity
include required fields
validate picklist values before creation
verify parent IDs and relationship integrity
account for validation rules and duplicate constraints
exclude non-createable fields from input payloads
Cleanup discipline

Prefer one of:

delete-by-ID
delete-by-pattern
delete-by-created-date window
rollback / savepoint patterns for script-based test runs
Common Failure Patterns
Error	Likely cause	Default fix direction
INVALID_FIELD	wrong field API name or FLS issue	verify schema and access
REQUIRED_FIELD_MISSING	mandatory field omitted	include required values from describe data
INVALID_CROSS_REFERENCE_KEY	bad parent ID	create / verify parent first
FIELD_CUSTOM_VALIDATION_EXCEPTION	validation rule blocked the record	use valid test data or adjust setup
invalid picklist value	guessed value instead of describe-backed value	inspect picklist values first
non-writeable field error	field is not createable / updateable	remove it from the payload
bulk limits / timeouts	wrong tool for the volume	switch to bulk / staged import
Output Format

When finishing, report in this order:

Operation performed
Objects and counts
Target org or local artifact path
Record IDs / output files
Verification result
Cleanup instructions

Suggested shape:

Data operation: <create / update / delete / export / seed>
Objects: <object + counts>
Target: <org alias or local path>
Artifacts: <record ids / csv / apex / json files>
Verification: <passed / partial / failed>
Cleanup: <exact delete or rollback guidance>

Cross-Skill Integration
Need	Delegate to	Reason
discover object / field structure	sf-metadata	accurate schema grounding
run bulk-sensitive Apex validation	sf-testing	test execution and coverage
deploy missing schema first	sf-deploy	metadata readiness
implement production logic consuming the data	sf-apex or sf-flow	behavior implementation
Reference Map
Start here
references/sf-cli-data-commands.md
references/test-data-best-practices.md
references/orchestration.md
references/test-data-patterns.md
references/test-data-factory-usage.md
Query / bulk / cleanup
references/soql-relationship-guide.md
references/relationship-query-examples.md
references/bulk-operations-guide.md
references/cleanup-rollback-guide.md
references/cleanup-rollback-example.md
Examples / limits
references/crud-workflow-example.md
references/bulk-testing-example.md
references/anonymous-apex-guide.md
references/governor-limits-reference.md
assets/
Score Guide
Score	Meaning
117+	strong production-safe data workflow
104–116	good operation with minor improvements possible
91–103	acceptable but review advised
78–90	partial / risky patterns present
< 78	blocked until corrected
Weekly Installs
1.1K
Repository
jaganpro/sf-skills
GitHub Stars
404
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass