---
title: n8n-validation-expert
url: https://skills.sh/czlonkowski/n8n-skills/n8n-validation-expert
---

# n8n-validation-expert

skills/czlonkowski/n8n-skills/n8n-validation-expert
n8n-validation-expert
Installation
$ npx skills add https://github.com/czlonkowski/n8n-skills --skill n8n-validation-expert
Summary

Expert guide for interpreting and fixing n8n validation errors.

Covers three severity levels: errors (block execution), warnings (optional fixes), and suggestions (nice-to-have improvements)
Includes five common error types with fix strategies: missing_required, invalid_value, type_mismatch, invalid_expression, and invalid_reference
Provides three validation profiles (minimal, runtime, strict, ai-friendly) for different workflow stages, with runtime recommended for pre-deployment checks
Auto-sanitization system automatically fixes operator structure issues on workflow saves, handling binary/unary operators and IF/Switch metadata
Explains the iterative validation loop (typically 2–3 cycles) and strategies for reducing false positives in production workflows
SKILL.md
n8n Validation Expert

Expert guide for interpreting and fixing n8n validation errors.

Validation Philosophy

Validate early, validate often

Validation is typically iterative:

Expect validation feedback loops
Usually 2-3 validate → fix cycles
Average: 23s thinking about errors, 58s fixing them

Key insight: Validation is an iterative process, not one-shot!

Error Severity Levels
1. Errors (Must Fix)

Blocks workflow execution - Must be resolved before activation

Types:

missing_required - Required field not provided
invalid_value - Value doesn't match allowed options
type_mismatch - Wrong data type (string instead of number)
invalid_reference - Referenced node doesn't exist
invalid_expression - Expression syntax error

Example:

{
  "type": "missing_required",
  "property": "channel",
  "message": "Channel name is required",
  "fix": "Provide a channel name (lowercase, no spaces, 1-80 characters)"
}

2. Warnings (Should Fix)

Doesn't block execution - Workflow can be activated but may have issues

Types:

best_practice - Recommended but not required
deprecated - Using old API/feature
performance - Potential performance issue

Example:

{
  "type": "best_practice",
  "property": "errorHandling",
  "message": "Slack API can have rate limits",
  "suggestion": "Add onError: 'continueRegularOutput' with retryOnFail"
}

3. Suggestions (Optional)

Nice to have - Improvements that could enhance workflow

Types:

optimization - Could be more efficient
alternative - Better way to achieve same result
The Validation Loop
Pattern from Telemetry

7,841 occurrences of this pattern:

1. Configure node
   ↓
2. validate_node (23 seconds thinking about errors)
   ↓
3. Read error messages carefully
   ↓
4. Fix errors
   ↓
5. validate_node again (58 seconds fixing)
   ↓
6. Repeat until valid (usually 2-3 iterations)

Example
// Iteration 1
let config = {
  resource: "channel",
  operation: "create"
};

const result1 = validate_node({
  nodeType: "nodes-base.slack",
  config,
  profile: "runtime"
});
// → Error: Missing "name"

// ⏱️  23 seconds thinking...

// Iteration 2
config.name = "general";

const result2 = validate_node({
  nodeType: "nodes-base.slack",
  config,
  profile: "runtime"
});
// → Error: Missing "text"

// ⏱️  58 seconds fixing...

// Iteration 3
config.text = "Hello!";

const result3 = validate_node({
  nodeType: "nodes-base.slack",
  config,
  profile: "runtime"
});
// → Valid! ✅


This is normal! Don't be discouraged by multiple iterations.

Validation Profiles

Choose the right profile for your stage:

minimal

Use when: Quick checks during editing

Validates:

Only required fields
Basic structure

Pros: Fastest, most permissive Cons: May miss issues

runtime (RECOMMENDED)

Use when: Pre-deployment validation

Validates:

Required fields
Value types
Allowed values
Basic dependencies

Pros: Balanced, catches real errors Cons: Some edge cases missed

This is the recommended profile for most use cases

ai-friendly

Use when: AI-generated configurations

Validates:

Same as runtime
Reduces false positives
More tolerant of minor issues

Pros: Less noisy for AI workflows Cons: May allow some questionable configs

strict

Use when: Production deployment, critical workflows

Validates:

Everything
Best practices
Performance concerns
Security issues

Pros: Maximum safety Cons: Many warnings, some false positives

Common Error Types
1. missing_required

What it means: A required field is not provided

How to fix:

Use get_node to see required fields
Add the missing field to your configuration
Provide an appropriate value

Example:

// Error
{
  "type": "missing_required",
  "property": "channel",
  "message": "Channel name is required"
}

// Fix
config.channel = "#general";

2. invalid_value

What it means: Value doesn't match allowed options

How to fix:

Check error message for allowed values
Use get_node to see options
Update to a valid value

Example:

// Error
{
  "type": "invalid_value",
  "property": "operation",
  "message": "Operation must be one of: post, update, delete",
  "current": "send"
}

// Fix
config.operation = "post";  // Use valid operation

3. type_mismatch

What it means: Wrong data type for field

How to fix:

Check expected type in error message
Convert value to correct type

Example:

// Error
{
  "type": "type_mismatch",
  "property": "limit",
  "message": "Expected number, got string",
  "current": "100"
}

// Fix
config.limit = 100;  // Number, not string

4. invalid_expression

What it means: Expression syntax error

How to fix:

Use n8n Expression Syntax skill
Check for missing {{}} or typos
Verify node/field references

Example:

// Error
{
  "type": "invalid_expression",
  "property": "text",
  "message": "Invalid expression: $json.name",
  "current": "$json.name"
}

// Fix
config.text = "={{$json.name}}";  // Add {{}}

5. invalid_reference

What it means: Referenced node doesn't exist

How to fix:

Check node name spelling
Verify node exists in workflow
Update reference to correct name

Example:

// Error
{
  "type": "invalid_reference",
  "property": "expression",
  "message": "Node 'HTTP Requets' does not exist",
  "current": "={{$node['HTTP Requets'].json.data}}"
}

// Fix - correct typo
config.expression = "={{$node['HTTP Request'].json.data}}";

6. patchNodeField Errors

What it means: A patchNodeField operation failed during n8n_update_partial_workflow

The patchNodeField operation is strict by design — it errors instead of silently continuing when something is wrong. This catches mistakes early but means you need to handle these specific error cases.

Error: Find string not found The patch's find value doesn't exist in the target field. This usually means the content was already changed, or the find string has a typo.

patchNodeField: find string not found in field "parameters.jsCode"


How to fix: Double-check the exact string. Use n8n_get_workflow to inspect the current field value. Whitespace and line endings matter — if unsure, use regex: true with \s+ for flexible whitespace matching.

Error: Ambiguous match (multiple occurrences) The find string appears more than once in the field. Without replaceAll: true, this is treated as ambiguous and rejected.

patchNodeField: find string matches 3 times in field "parameters.jsCode" — set replaceAll: true to replace all, or use a more specific find string


How to fix: Either set replaceAll: true if you want to replace all occurrences, or make your find string more specific to match only the intended location.

Error: Invalid regex pattern When regex: true, the pattern is validated for correctness and safety.

patchNodeField: invalid or unsafe regex pattern


How to fix: Check regex syntax. Nested quantifiers like (a+)+ and overlapping alternations like (\w|\d)+ are rejected as ReDoS risks. Simplify the pattern.

Auto-Sanitization System
What It Does

Automatically fixes common operator structure issues on ANY workflow update

Runs when:

n8n_create_workflow
n8n_update_partial_workflow
Any workflow save operation
What It Fixes
1. Binary Operators (Two Values)

Operators: equals, notEquals, contains, notContains, greaterThan, lessThan, startsWith, endsWith

Fix: Removes singleValue property (binary operators compare two values)

Before:

{
  "type": "boolean",
  "operation": "equals",
  "singleValue": true  // ❌ Wrong!
}


After (automatic):

{
  "type": "boolean",
  "operation": "equals"
  // singleValue removed ✅
}

2. Unary Operators (One Value)

Operators: isEmpty, isNotEmpty, true, false

Fix: Adds singleValue: true (unary operators check single value)

Before:

{
  "type": "boolean",
  "operation": "isEmpty"
  // Missing singleValue ❌
}


After (automatic):

{
  "type": "boolean",
  "operation": "isEmpty",
  "singleValue": true  // ✅ Added
}

3. IF/Switch Metadata

Fix: Adds complete conditions.options metadata for IF v2.2+ and Switch v3.2+

What It CANNOT Fix
1. Broken Connections

References to non-existent nodes

Solution: Use cleanStaleConnections operation in n8n_update_partial_workflow

2. Branch Count Mismatches

3 Switch rules but only 2 output connections

Solution: Add missing connections or remove extra rules

3. Paradoxical Corrupt States

API returns corrupt data but rejects updates

Solution: May require manual database intervention

False Positives
What Are They?

Validation warnings that are technically "wrong" but acceptable in your use case

Common False Positives
1. "Missing error handling"

Warning: No error handling configured

When acceptable:

Simple workflows where failures are obvious
Testing/development workflows
Non-critical notifications

When to fix: Production workflows handling important data

2. "No retry logic"

Warning: Node doesn't retry on failure

When acceptable:

APIs with their own retry logic
Idempotent operations
Manual trigger workflows

When to fix: Flaky external services, production automation

3. "Missing rate limiting"

Warning: No rate limiting for API calls

When acceptable:

Internal APIs with no limits
Low-volume workflows
APIs with server-side rate limiting

When to fix: Public APIs, high-volume workflows

4. "Unbounded query"

Warning: SELECT without LIMIT

When acceptable:

Small known datasets
Aggregation queries
Development/testing

When to fix: Production queries on large tables

Reducing False Positives

Use ai-friendly profile:

validate_node({
  nodeType: "nodes-base.slack",
  config: {...},
  profile: "ai-friendly"  // Fewer false positives
})

Validation Result Structure
Complete Response
{
  "valid": false,
  "errors": [
    {
      "type": "missing_required",
      "property": "channel",
      "message": "Channel name is required",
      "fix": "Provide a channel name (lowercase, no spaces)"
    }
  ],
  "warnings": [
    {
      "type": "best_practice",
      "property": "errorHandling",
      "message": "Slack API can have rate limits",
      "suggestion": "Add onError: 'continueRegularOutput'"
    }
  ],
  "suggestions": [
    {
      "type": "optimization",
      "message": "Consider using batch operations for multiple messages"
    }
  ],
  "summary": {
    "hasErrors": true,
    "errorCount": 1,
    "warningCount": 1,
    "suggestionCount": 1
  }
}

How to Read It
1. Check valid field
if (result.valid) {
  // ✅ Configuration is valid
} else {
  // ❌ Has errors - must fix before deployment
}

2. Fix errors first
result.errors.forEach(error => {
  console.log(`Error in ${error.property}: ${error.message}`);
  console.log(`Fix: ${error.fix}`);
});

3. Review warnings
result.warnings.forEach(warning => {
  console.log(`Warning: ${warning.message}`);
  console.log(`Suggestion: ${warning.suggestion}`);
  // Decide if you need to address this
});

4. Consider suggestions
// Optional improvements
// Not required but may enhance workflow

Workflow Validation
validate_workflow (Structure)

Validates entire workflow, not just individual nodes

Checks:

Node configurations - Each node valid
Connections - No broken references
Expressions - Syntax and references valid
Flow - Logical workflow structure

Example:

validate_workflow({
  workflow: {
    nodes: [...],
    connections: {...}
  },
  options: {
    validateNodes: true,
    validateConnections: true,
    validateExpressions: true,
    profile: "runtime"
  }
})

Common Workflow Errors
1. Broken Connections
{
  "error": "Connection from 'Transform' to 'NonExistent' - target node not found"
}


Fix: Remove stale connection or create missing node

2. Circular Dependencies
{
  "error": "Circular dependency detected: Node A → Node B → Node A"
}


Fix: Restructure workflow to remove loop

3. Multiple Start Nodes
{
  "warning": "Multiple trigger nodes found - only one will execute"
}


Fix: Remove extra triggers or split into separate workflows

4. Disconnected Nodes
{
  "warning": "Node 'Transform' is not connected to workflow flow"
}


Fix: Connect node or remove if unused

Recovery Strategies
Strategy 1: Start Fresh

When: Configuration is severely broken

Steps:

Note required fields from get_node
Create minimal valid configuration
Add features incrementally
Validate after each addition
Strategy 2: Binary Search

When: Workflow validates but executes incorrectly

Steps:

Remove half the nodes
Validate and test
If works: problem is in removed nodes
If fails: problem is in remaining nodes
Repeat until problem isolated
Strategy 3: Clean Stale Connections

When: "Node not found" errors

Steps:

n8n_update_partial_workflow({
  id: "workflow-id",
  operations: [{
    type: "cleanStaleConnections"
  }]
})

Strategy 4: Use Auto-fix

When: Validation errors that can be automatically resolved

Steps:

// Preview fixes (default - doesn't apply)
n8n_autofix_workflow({
  id: "workflow-id",
  applyFixes: false,
  confidenceThreshold: "medium"  // high, medium, low
})

// Review fixes, then apply
n8n_autofix_workflow({
  id: "workflow-id",
  applyFixes: true
})

Auto-Fix Capabilities

The n8n_autofix_workflow tool can fix these issue types:

expression-format - Missing = prefix in expressions (e.g., {{ $json.field }} → ={{ $json.field }})
typeversion-correction - Downgrades nodes with unsupported typeVersions
error-output-config - Removes conflicting onError settings
node-type-correction - Fixes unknown node types using similarity matching (90%+ confidence)
webhook-missing-path - Generates UUIDs for webhook nodes missing path configuration
typeversion-upgrade - Smart upgrades to latest node versions with auto-migration
version-migration - Guidance for complex breaking changes requiring manual steps

Confidence levels: high (90%+, safe to auto-apply), medium (70-89%, review recommended), low (<70%, manual review required)

// Preview all fixes
n8n_autofix_workflow({id: "workflow-id"})

// Only apply high-confidence fixes
n8n_autofix_workflow({
  id: "workflow-id",
  applyFixes: true,
  confidenceThreshold: "high"
})

// Target specific fix types
n8n_autofix_workflow({
  id: "workflow-id",
  fixTypes: ["expression-format", "typeversion-upgrade"],
  applyFixes: true
})


Post-update guidance: For version upgrades, check the postUpdateGuidance field in the response for step-by-step migration instructions.

Best Practices
✅ Do
Validate after every significant change
Read error messages completely
Fix errors iteratively (one at a time)
Use runtime profile for pre-deployment
Check valid field before assuming success
Trust auto-sanitization for operator issues
Use get_node when unclear about requirements
Document false positives you accept
❌ Don't
Skip validation before activation
Try to fix all errors at once
Ignore error messages
Use strict profile during development (too noisy)
Assume validation passed (always check result)
Manually fix auto-sanitization issues
Deploy with unresolved errors
Ignore all warnings (some are important!)
Detailed Guides

For comprehensive error catalogs and false positive examples:

ERROR_CATALOG.md - Complete list of error types with examples
FALSE_POSITIVES.md - When warnings are acceptable
Summary

Key Points:

Validation is iterative (avg 2-3 cycles, 23s + 58s)
Errors must be fixed, warnings are optional
Auto-sanitization fixes operator structures automatically
Use runtime profile for balanced validation
False positives exist - learn to recognize them
Read error messages - they contain fix guidance

Validation Process:

Validate → Read errors → Fix → Validate again
Repeat until valid (usually 2-3 iterations)
Review warnings and decide if acceptable
Deploy with confidence

Related Skills & Tools:

n8n MCP Tools Expert - Use validation tools correctly
n8n Expression Syntax - Fix expression errors
n8n Node Configuration - Understand required fields
n8n_audit_instance - Proactive security validation (hardcoded secrets, unauthenticated webhooks, missing error handling, data retention)
Weekly Installs
2.8K
Repository
czlonkowski/n8n-skills
GitHub Stars
4.7K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass