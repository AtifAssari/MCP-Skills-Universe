---
title: command-generator
url: https://skills.sh/catlog22/claude-code-workflow/command-generator
---

# command-generator

skills/catlog22/claude-code-workflow/command-generator
command-generator
Installation
$ npx skills add https://github.com/catlog22/claude-code-workflow --skill command-generator
SKILL.md

Invoked when user requests "create command", "new command", or "command generator".

<required_reading>

@.claude/skills/command-generator/specs/command-design-spec.md
@.claude/skills/command-generator/templates/command-md.md </required_reading>

Extract from $ARGUMENTS or skill args:

Parameter	Required	Validation	Example
$SKILL_NAME	Yes	/^[a-z][a-z0-9-]*$/, min 1 char	deploy, create
$DESCRIPTION	Yes	min 10 chars	"Deploy application to production"
$LOCATION	Yes	"project" or "user"	project
$GROUP	No	/^[a-z][a-z0-9-]*$/ or null	issue, workflow
$ARGUMENT_HINT	No	any string or empty	"<url> [--priority 1-5]"

Validation rules:

Missing required param → Error with specific message (e.g., "skillName is required")
Invalid $SKILL_NAME pattern → Error: "skillName must be lowercase alphanumeric with hyphens, starting with a letter"
Invalid $LOCATION → Error: "location must be 'project' or 'user'"
Invalid $GROUP pattern → Warning, continue

Normalize: trim + lowercase for $SKILL_NAME, $LOCATION, $GROUP.

Path mapping:

Location	Base Directory
project	.claude/commands
user	~/.claude/commands (expand ~ to $HOME)

Path construction:

If $GROUP:
  $TARGET_DIR = {base}/{$GROUP}
  $TARGET_PATH = {base}/{$GROUP}/{$SKILL_NAME}.md
Else:
  $TARGET_DIR = {base}
  $TARGET_PATH = {base}/{$SKILL_NAME}.md


Check if $TARGET_PATH already exists → store as $FILE_EXISTS (true/false).

Infer the command's domain from $SKILL_NAME, $DESCRIPTION, and $ARGUMENT_HINT:

Signal	Extract
$SKILL_NAME	Action verb (deploy, create, analyze, sync) → step naming
$DESCRIPTION	Domain keywords → execution logic, error scenarios
$ARGUMENT_HINT	Flags/args → parse_input step details, validation rules
$GROUP	Command family → related commands, shared patterns

Determine command complexity:

Complexity	Criteria	Steps to Generate
Simple	Single action, no flags	2-3 steps
Standard	1-2 flags, clear workflow	3-4 steps
Complex	Multiple flags, multi-phase	4-6 steps

If complexity is unclear, ask user:

AskUserQuestion(
  header: "Command Scope",
  question: "What are the main execution steps for this command?",
  options: [
    { label: "Simple", description: "Single action: validate → execute → report" },
    { label: "Standard", description: "Multi-step: parse → process → verify → report" },
    { label: "Complex", description: "Full workflow: parse → explore → execute → verify → report" },
    { label: "I'll describe", description: "Let me specify the steps" }
  ]
)


Store as $COMMAND_STEPS, $ERROR_SCENARIOS, $SUCCESS_CONDITIONS.

This is the core generation step. Draft the COMPLETE command file — not a template with placeholders — using the gathered requirements.

YAML Frontmatter:

---
name: $SKILL_NAME
description: $DESCRIPTION
argument-hint: $ARGUMENT_HINT  # only if provided
---


<purpose> section: Write 2-3 sentences describing:

What the command does (action + target)
When it's invoked (trigger conditions)
What it produces (output artifacts or effects)

<required_reading> section: Infer from domain:

If command reads config → @.claude/CLAUDE.md or relevant config files
If command modifies code → relevant source directories
If command is part of a group → other commands in the same group

<process> section with <step> blocks:

For each step in $COMMAND_STEPS, generate a <step name="snake_case"> block containing:

parse_input (always first, priority="first"):

Parse $ARGUMENTS for flags and positional args derived from $ARGUMENT_HINT
Include specific flag detection logic (e.g., if arguments contain "--env")
Include validation with specific error messages
Include decision routing table if multiple modes exist

Domain-specific execution steps (2-4 steps):

Each step has a bold action description
Include concrete shell commands, file operations, or tool calls
Use $UPPER_CASE variables for user input, ${computed} for derived values
Include conditional logic with specific conditions (not generic)
Reference actual file paths and tool names

report (always last):

Format output with banner and status
Include file paths, timestamps, next step suggestions

Shell Correctness Checklist (MANDATORY for every shell block):

Rule	Wrong	Correct
Multi-line output	echo "{ ... }" (unquoted multi-line)	cat <<'EOF' > file...EOF (heredoc)
Variable init	Use $VAR after conditional	VAR="default" BEFORE any conditional that sets it
Error exit	echo "Error: ..." (no exit)	echo "Error: ..." # (see code: E00X) + exit 1
Quoting	$VAR in commands	"$VAR" (double-quoted in all expansions)
Exit on fail	Command chain without checks	set -e or explicit `
Command from var	$CMD --flag (word-split fragile)	eval "$CMD" --flag or use array: cmd=(...); "${cmd[@]}"
Prerequisites	Implicit git/curl usage	Declare in <prerequisites> section

Golden Example — a correctly-written execution step:

<step name="run_deployment">
**Execute deployment to target environment.**

$DEPLOY_STATUS="pending"  # Initialize before conditional

```bash
# Save current state for rollback
cp .deploy/latest.json .deploy/previous.json 2>/dev/null || true

# Write deployment manifest via heredoc
cat <<EOF > .deploy/latest.json
{
  "env": "$ENV",
  "tag": "$DEPLOY_TAG",
  "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "commit": "$(git rev-parse --short HEAD)",
  "status": "deploying"
}
EOF

# Execute deployment
if ! deploy_cmd --env "$ENV" --tag "$DEPLOY_TAG" 2>&1 | tee .deploy/latest.log; then
  echo "Error: Deployment to $ENV failed" # (see code: E004)
  exit 1
fi

$DEPLOY_STATUS="success"

Condition	Action
Deploy succeeds	Update status → "deployed", continue to verify
Deploy fails	Log error # (see code: E004), exit 1
$ROLLBACK_MODE	Load .deploy/previous.json, redeploy prior version

Optional <prerequisites> section (include when command uses external tools):

<prerequisites>
- git (2.20+) — version control operations
- curl — health check endpoints
- jq — JSON processing (optional)
</prerequisites>


<error_codes> table: Generate 3-6 specific error codes:

Derive from $ARGUMENT_HINT validation failures (E001-E003)
Derive from domain-specific failure modes (E004+)
Include 1-2 warnings (W001+)
Each code has: Code, Severity, Description, Stage (which step triggers it)
Cross-reference rule: Every # (see code: E00X) comment in <process> MUST have a matching row in <error_codes>, and every error code row MUST be referenced by at least one inline comment

<success_criteria> checkboxes: Generate 4-8 verifiable conditions:

Input validation passed
Each execution step completed its action
Output artifacts exist / effects applied
Report displayed

Quality rules for generated content:

NO bracket placeholders ([Describe...], [List...]) — all content must be concrete
Steps must contain actionable logic, not descriptions of what to do
Error codes must reference specific failure conditions from this command's domain
Success criteria must be verifiable (not "command works correctly")
Every shell block must pass the Shell Correctness Checklist above
Follow patterns from @.claude/skills/command-generator/templates/command-md.md for structural reference only

If $FILE_EXISTS: Warn: "Command file already exists at {path}. Will overwrite."

mkdir -p "$TARGET_DIR"


Write the drafted content to $TARGET_PATH using Write tool.

Verify: Read back the file and confirm:

File exists and is non-empty
Contains <purpose> tag with concrete content (no placeholders)
Contains at least 2 <step name= blocks with shell code or tool calls
Contains <error_codes> with at least 3 rows including Stage column
Contains <success_criteria> with at least 4 checkboxes
No unresolved {{...}} or [...] placeholders remain
Every # (see code: E0XX) has a matching <error_codes> row (cross-ref check)
Every shell block uses heredoc for multi-line output (no bare multi-line echo)
All state variables initialized before conditional use
All error paths include exit 1 after error message

If verification fails: Fix the content in-place using Edit tool.

Report completion:

Command generated successfully!

File: {$TARGET_PATH}
Name: {$SKILL_NAME}
Description: {$DESCRIPTION}
Location: {$LOCATION}
Group: {$GROUP or "(none)"}
Steps: {number of <step> blocks generated}
Error codes: {number of error codes}

Next Steps:
1. Review and customize {$TARGET_PATH}
2. Test: /{$GROUP}:{$SKILL_NAME} or /{$SKILL_NAME}


<error_codes>

Code	Severity	Description	Stage
E001	error	skillName is required	validate_params
E002	error	description is required (min 10 chars)	validate_params
E003	error	location is required ("project" or "user")	validate_params
E004	error	skillName must be lowercase alphanumeric with hyphens	validate_params
E005	error	Failed to infer command domain from description	gather_requirements
E006	error	Failed to write command file	write_file
E007	error	Generated content contains unresolved placeholders	write_file
W001	warning	group must be lowercase alphanumeric with hyphens	validate_params
W002	warning	Command file already exists, will overwrite	write_file
W003	warning	Could not infer required_reading, using defaults	draft_content

</error_codes>

<success_criteria>

 All required parameters validated ($SKILL_NAME, $DESCRIPTION, $LOCATION)
 Target path resolved with correct scope (project vs user) and group
 Command domain inferred from description and argument hint
 Concrete <purpose> drafted (no placeholders)
 2-6 <step> blocks generated with domain-specific logic
 <error_codes> table generated with 3+ specific codes
 <success_criteria> generated with 4+ verifiable checkboxes
 File written to $TARGET_PATH and verified
 Zero bracket placeholders in final output
 Completion report displayed </success_criteria>
Weekly Installs
27
Repository
catlog22/claude…workflow
GitHub Stars
1.9K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass