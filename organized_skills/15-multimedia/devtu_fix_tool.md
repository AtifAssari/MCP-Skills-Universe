---
rating: ⭐⭐⭐
title: devtu-fix-tool
url: https://skills.sh/mims-harvard/tooluniverse/devtu-fix-tool
---

# devtu-fix-tool

skills/mims-harvard/tooluniverse/devtu-fix-tool
devtu-fix-tool
Installation
$ npx skills add https://github.com/mims-harvard/tooluniverse --skill devtu-fix-tool
SKILL.md
Fix ToolUniverse Tools

Diagnose and fix failing ToolUniverse tools through systematic error identification, targeted fixes, and validation.

First Principles for Bug Fixes

Before writing any fix, ask: why does the user reach this failure state?

Prevent, don't recover — fix the root cause so the failure can't happen, rather than adding hint text after it does
Validate at input, not at output — wrong parameters, unknown disease names, unsupported drugs should be caught and rejected early with clear guidance, not discovered after a silent API call
Don't mask silent mutations — if input is auto-normalized (fusion notation, Title Case), either accept both forms natively OR reject with explicit guidance; never silently transform and hide it
Distinguish "no data" from "bad query" — zero results because the filter is wrong is different from zero results because the data doesn't exist; the response must distinguish these clearly
Fix the abstraction, not the instance — if a parameter name is inconsistent, fix the interface; don't add an alias list that grows forever

Anti-patterns to avoid:

Adding hint text to zero-result messages instead of validating upfront
Adding parameter aliases instead of fixing naming consistency
Post-hoc probing to rescue a failed query instead of pre-validating
Bug Verification (CRITICAL)

Before implementing any bug report, verify it via CLI first:

python3 -m tooluniverse.cli run <ToolName> '<json_args>'


Many agent-reported bugs are false positives caused by MCP interface confusion. Always confirm the bug is reproducible before implementing a fix.

Instructions

When fixing a failing tool:

Run targeted test to identify error:
python scripts/test_new_tools.py <tool-pattern> -v


Verify API is correct - search online for official API documentation to confirm endpoints, parameters, and patterns are correct

Identify error type (see Error Types section)

Apply appropriate fix based on error pattern

Regenerate tools if you modified JSON configs or tool classes:

python -m tooluniverse.generate_tools

Check and update tool tests if they exist in tests/tools/:
ls tests/tools/test_<tool-name>_tool.py


Verify fix by re-running both integration and unit tests

Provide fix summary with problem, root cause, solution, and test results

Where to Fix
Issue Type	File to Modify
Binary response	src/tooluniverse/*_tool.py + src/tooluniverse/data/*_tools.json
Schema mismatch	src/tooluniverse/data/*_tools.json (return_schema)
Missing data wrapper	src/tooluniverse/*_tool.py (operation methods)
Endpoint URL	src/tooluniverse/data/*_tools.json (endpoint field)
Invalid test example	src/tooluniverse/data/*_tools.json (test_examples)
Tool test updates	tests/tools/test_*_tool.py (if exists)
API key as parameter	src/tooluniverse/data/*_tools.json (remove param) + *_tool.py (use env var)
Tool not loading (optional key)	src/tooluniverse/data/*_tools.json (use optional_api_keys not required_api_keys)
Error Types
1. JSON Parsing Errors

Symptom: Expecting value: line 1 column 1 (char 0)

Cause: Tool expects JSON but receives binary data (images, PDFs, files)

Fix: Check Content-Type header. For binary responses, return a description string instead of parsing JSON. Update return_schema to {"type": "string"}.

2. Schema Validation Errors

Symptom: Schema Mismatch: At root: ... is not of type 'object' or Data: None

Cause: Missing data field wrapper OR wrong schema type

Fix depends on the error:

If Data: None → Add data wrapper to ALL operation methods (see Multi-Operation Pattern below)
If type mismatch → Update return_schema in JSON config:
Data is string: {"type": "string"}
Data is array: {"type": "array", "items": {...}}
Data is object: {"type": "object", "properties": {...}}

Key concept: Schema validates the data field content, NOT the full response.

3. Nullable Field Errors

Symptom: Schema Mismatch: At N->fieldName: None is not of type 'integer'

Cause: API returns None/null for optional fields

Fix: Allow nullable types in JSON config using {"type": ["<base_type>", "null"]}. Use for optional fields, not required identifiers.

4. Mutually Exclusive Parameter Errors

Symptom: Parameter validation failed for 'param_name': None is not of type 'integer' when passing a different parameter

Cause: Tool accepts EITHER paramA OR paramB (mutually exclusive), but both are defined with fixed types. When only one is provided, validation fails because the other is None.

Example:

{
  "neuron_id": {"type": "integer"},      // ❌ Fails when neuron_name is used
  "neuron_name": {"type": "string"}      // ❌ Fails when neuron_id is used
}


Fix: Make mutually exclusive parameters nullable:

{
  "neuron_id": {"type": ["integer", "null"]},      // ✅ Allows None
  "neuron_name": {"type": ["string", "null"]}      // ✅ Allows None
}


Common patterns:

id OR name parameters (get by ID or by name)
acronym OR name parameters (search by symbol or full name)
Optional filter parameters that may not be provided

Important: Also make truly optional parameters (like filter_field, filter_value) nullable even if not mutually exclusive.

5. Mixed Type Field Errors

Symptom: Schema Mismatch: At N->field: {object} is not of type 'string', 'null'

Cause: Field returns different structures depending on context

Fix: Use oneOf in JSON config for fields with multiple distinct schemas. Different from nullable ({"type": ["string", "null"]}) which is same base type + null.

6. Invalid Test Examples

Symptom: 404 ERROR - Not found or 400 Bad Request

Cause: Test example uses invalid/outdated IDs

Fix: Discover valid examples using the List → Get or Search → Details patterns below.

7. API Parameter Errors

Symptom: 400 Bad Request or parameter validation errors

Fix: Update parameter schema in JSON config with correct types, required fields, and enums.

8. API Key Configuration Errors

Symptom: Tool not loading when API key is optional, or api_key parameter causing confusion

Cause: Using required_api_keys for keys that should be optional, or exposing API key as tool parameter

Key differences:

required_api_keys: Tool is skipped if keys are missing
optional_api_keys: Tool loads and works without keys (with reduced performance)

Fix: Use optional_api_keys in JSON config for APIs that work anonymously but have better rate limits with keys. Read API key from environment only (os.environ.get()), never as a tool parameter.

9. API Endpoint Pattern Errors

Symptom: 404 for valid resources, or unexpected results

Fix: Verify official API docs - check if values belong in URL path vs query parameters.

10. Transient API Failures

Symptom: Tests fail intermittently with timeout/connection/5xx errors

Fix: Use pytest.skip() for transient errors in unit tests - don't fail on external API outages.

Common Fix Patterns
Schema Validation Pattern

Schema validates the data field content, not the full response. Match return_schema type to what's inside data (array, object, or string).

Multi-Operation Tool Pattern

Every internal method must return {"status": "...", "data": {...}}. Don't use alternative field names at top level.

Finding Valid Test Examples

When test examples fail with 400/404, discover valid IDs by:

List → Get: Call a list endpoint first, extract ID from results
Search → Details: Search for a known entity, use returned ID
Iterate Versions: Try different dataset versions if supported
Unit Test Management
Check for Unit Tests

After fixing a tool, check if unit tests exist:

ls tests/tools/test_<tool-name>_tool.py

When to Update Unit Tests

Update unit tests when you:

Change return structure: Update assertions checking result["data"] structure
Add/modify operations: Add test cases for new operations
Change error handling: Update error assertions
Modify required parameters: Update parameter validation tests
Fix schema issues: Ensure tests validate correct data structure
Add binary handling: Add tests for binary responses
Running Unit Tests
# Run specific tool tests
pytest tests/tools/test_<tool-name>_tool.py -v

# Run all unit tests
pytest tests/tools/ -v

Unit Test Checklist
 Check if tests/tools/test_<tool-name>_tool.py exists
 Run unit tests before and after fix
 Update assertions if data structure changed
 Ensure both direct and interface tests pass

For detailed unit test patterns and examples, see unit-tests-reference.md.

Verification
Run Integration Tests
python scripts/test_new_tools.py <pattern> -v

Run Unit Tests (if exist)
pytest tests/tools/test_<tool-name>_tool.py -v

Regenerate Tools

After modifying JSON configs or tool classes:

python -m tooluniverse.generate_tools


Regenerate after:

Changing src/tooluniverse/data/*_tools.json files
Modifying tool class implementations

Not needed for test script changes.

Output Format

After fixing, provide this summary:

Problem: [Brief description]

Root Cause: [Why it failed]

Solution: [What was changed]

Changes Made:

File 1: [Description]
File 2: [Description]
File 3 (if applicable): [Unit test updates]

Integration Test Results:

Before: X tests, Y passed (Z%), N failed, M schema invalid
After: X tests, X passed (100.0%), 0 failed, 0 schema invalid

Unit Test Results (if applicable):

Before: X tests, Y passed, Z failed
After: X tests, X passed, 0 failed
Testing Best Practices
Verify Parameter Names Before Testing

CRITICAL: Always read the tool's JSON config or generated wrapper to get the correct parameter names. Don't assume parameter names.

Example of incorrect testing:

# ❌ WRONG - assumed parameter name
AllenBrain_search_genes(query='Gad1')  # Fails: unexpected keyword 'query'


Correct approach:

# ✅ RIGHT - checked config first
# Config shows parameters: gene_acronym, gene_name
AllenBrain_search_genes(gene_acronym='Gad1')  # Works!


How to find correct parameter names:

Read the JSON config: src/tooluniverse/data/*_tools.json
Check the generated wrapper: src/tooluniverse/tools/<ToolName>.py
Look at test_examples in the JSON config
Systematic Testing Approach

When testing multiple tools:

Sample first: Test 1-2 tools per API to identify patterns
Categorize errors: Group by error type (param validation, API errors, data structure)
Fix systematically: Fix all tools with same issue type together
Regenerate once: Run python -m tooluniverse.generate_tools after all JSON changes
Verify all: Test all fixed tools comprehensively
Understanding Data Structure

Tools can return different data structures:

Object: {"data": {"id": 1, "name": "..."}} - single result
Array: {"data": [{"id": 1}, {"id": 2}]} - multiple results
String: {"data": "description text"} - text response

Test accordingly:

# For object data
result = tool()
data = result.get('data', {})
value = data.get('field_name')  # ✅

# For array data
result = tool()
items = result.get('data', [])
count = len(items)  # ✅
first = items[0] if items else {}  # ✅

Common Pitfalls
Schema validates data field, not full response
All methods need {"status": "...", "data": {...}} wrapper
JSON config changes require regeneration
Use optional_api_keys for APIs that work without keys
Check official API docs for correct endpoint patterns
Unit tests should skip on transient API failures, not fail
Mutually exclusive parameters MUST be nullable - most common new tool issue
Verify parameter names from configs - don't assume or guess
Test with correct data structure expectations - list vs dict vs string
Debugging
Inspect API response: Check status code, Content-Type header, and body preview
Check tool config: Load ToolUniverse and inspect the tool's configuration
Add debug prints: Log URL, params, status, and Content-Type in the run method
Quick Reference
Task	Command
Run integration tests	python scripts/test_new_tools.py <pattern> -v
Run unit tests	pytest tests/tools/test_<tool-name>_tool.py -v
Check if unit tests exist	ls tests/tools/test_<tool-name>_tool.py
Regenerate tools	python -m tooluniverse.generate_tools
Check status	git status --short | grep -E "(data|tools|.*_tool.py|tests/tools)"
Error Type	Fix Location
JSON parse error	src/tooluniverse/*_tool.py run() method
Schema mismatch	src/tooluniverse/data/*_tools.json return_schema
404 errors	src/tooluniverse/data/*_tools.json test_examples or endpoint
Parameter errors	src/tooluniverse/data/*_tools.json parameter schema
Unit test failures	tests/tools/test_*_tool.py assertions
Tool skipped (optional key)	src/tooluniverse/data/*_tools.json use optional_api_keys
API key as parameter	Remove from JSON params, use os.environ.get() in Python
Weekly Installs
206
Repository
mims-harvard/to…universe
GitHub Stars
1.3K
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn