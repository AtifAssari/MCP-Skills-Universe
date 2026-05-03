---
rating: ⭐⭐⭐
title: burpsuite-project-parser
url: https://skills.sh/trailofbits/skills/burpsuite-project-parser
---

# burpsuite-project-parser

skills/trailofbits/skills/burpsuite-project-parser
burpsuite-project-parser
Installation
$ npx skills add https://github.com/trailofbits/skills --skill burpsuite-project-parser
Summary

Search and extract HTTP traffic, audit findings, and security data from Burp Suite project files via CLI.

Queries proxy history, site map, and audit items using regex patterns on request/response headers and bodies
Requires Burp Suite Professional and the burpsuite-project-file-parser extension; delegates parsing to Burp's Java runtime
Enforces sub-component filters (headers, bodies) instead of full dumps to prevent gigabyte-scale data retrieval; mandatory truncation of body content to 1000 characters
Includes investigation workflow for triaging findings by severity and confidence, with output as JSON for piping to jq or grep
SKILL.md
Burp Project Parser

Search and extract data from Burp Suite project files using the burpsuite-project-file-parser extension.

When to Use
Searching response headers or bodies with regex patterns
Extracting security audit findings from Burp projects
Dumping proxy history or site map data
Analyzing HTTP traffic captured in a Burp project file
Prerequisites

This skill delegates parsing to Burp Suite Professional - it does not parse .burp files directly.

Required:

Burp Suite Professional - Must be installed (portswigger.net)
burpsuite-project-file-parser extension - Provides CLI functionality

Install the extension:

Download from github.com/BuffaloWill/burpsuite-project-file-parser
In Burp Suite: Extender → Extensions → Add
Select the downloaded JAR file
Quick Reference

Use the wrapper script:

{baseDir}/scripts/burp-search.sh /path/to/project.burp [FLAGS]


The script uses environment variables for platform compatibility:

BURP_JAVA: Path to Java executable
BURP_JAR: Path to burpsuite_pro.jar

See Platform Configuration for setup instructions.

Sub-Component Filters (USE THESE)

ALWAYS use sub-component filters instead of full dumps. Full proxyHistory or siteMap can return gigabytes of data. Sub-component filters return only what you need.

Available Filters
Filter	Returns	Typical Size
proxyHistory.request.headers	Request line + headers only	Small (< 1KB/record)
proxyHistory.request.body	Request body only	Variable
proxyHistory.response.headers	Status + headers only	Small (< 1KB/record)
proxyHistory.response.body	Response body only	LARGE - avoid
siteMap.request.headers	Same as above for site map	Small
siteMap.request.body		Variable
siteMap.response.headers		Small
siteMap.response.body		LARGE - avoid
Default Approach

Start with headers, not bodies:

# GOOD - headers only, safe to retrieve
{baseDir}/scripts/burp-search.sh project.burp proxyHistory.request.headers | head -c 50000
{baseDir}/scripts/burp-search.sh project.burp proxyHistory.response.headers | head -c 50000

# BAD - full records include bodies, can be gigabytes
{baseDir}/scripts/burp-search.sh project.burp proxyHistory  # NEVER DO THIS


Only fetch bodies for specific URLs after reviewing headers, and ALWAYS truncate:

# 1. First, find interesting URLs from headers
{baseDir}/scripts/burp-search.sh project.burp proxyHistory.response.headers | \
  jq -r 'select(.headers | test("text/html")) | .url' | head -n 20

# 2. Then search bodies with targeted regex - MUST truncate body to 1000 chars
{baseDir}/scripts/burp-search.sh project.burp "responseBody='.*specific-pattern.*'" | \
  head -n 10 | jq -c '.body = (.body[:1000] + "...[TRUNCATED]")'


HARD RULE: Body content > 1000 chars must NEVER enter context. If the user needs full body content, they must view it in Burp Suite's UI.

Regex Search Operations
Search Response Headers
responseHeader='.*regex.*'


Searches all response headers. Output: {"url":"...", "header":"..."}

Example - find server signatures:

responseHeader='.*(nginx|Apache|Servlet).*' | head -c 50000

Search Response Bodies
responseBody='.*regex.*'


MANDATORY: Always truncate body content to 1000 chars max. Response bodies can be megabytes each.

# REQUIRED format - always truncate .body field
{baseDir}/scripts/burp-search.sh project.burp "responseBody='.*<form.*action.*'" | \
  head -n 10 | jq -c '.body = (.body[:1000] + "...[TRUNCATED]")'


Never retrieve full body content. If you need to see more of a specific response, ask the user to open it in Burp Suite's UI.

Other Operations
Extract Audit Items
auditItems


Returns all security findings. Output includes: name, severity, confidence, host, port, protocol, url.

Note: Audit items are small (no bodies) - safe to retrieve with head -n 100.

Dump Proxy History (AVOID)
proxyHistory


NEVER use this directly. Use sub-component filters instead:

proxyHistory.request.headers
proxyHistory.response.headers
Dump Site Map (AVOID)
siteMap


NEVER use this directly. Use sub-component filters instead.

Output Limits (REQUIRED)

CRITICAL: Always check result size BEFORE retrieving data. A broad search can return thousands of records, each potentially megabytes. This will overflow the context window.

Step 1: Always Check Size First

Before any search, check BOTH record count AND byte size:

# Check record count AND total bytes - never skip this step
{baseDir}/scripts/burp-search.sh project.burp proxyHistory | wc -cl
{baseDir}/scripts/burp-search.sh project.burp "responseHeader='.*Server.*'" | wc -cl
{baseDir}/scripts/burp-search.sh project.burp auditItems | wc -cl


The wc -cl output shows: <bytes> <lines> (e.g., 524288 42 means 512KB across 42 records).

Interpret the results - BOTH must pass:

Metric	Safe	Narrow search	Too broad	STOP
Lines	< 50	50-200	200+	1000+
Bytes	< 50KB	50-200KB	200KB+	1MB+

A single 10MB response on one line will show high byte count but only 1 line - the byte check catches this.

Step 2: Refine Broad Searches

If count/size is too high:

Use sub-component filters (see table above):

# Instead of: proxyHistory (gigabytes)
# Use: proxyHistory.request.headers (kilobytes)


Narrow regex patterns:

# Too broad (matches everything):
responseHeader='.*'

# Better - target specific headers:
responseHeader='.*X-Frame-Options.*'
responseHeader='.*Content-Security-Policy.*'


Filter with jq before retrieving:

# Get only specific content types
{baseDir}/scripts/burp-search.sh project.burp proxyHistory.response.headers | \
  jq -c 'select(.url | test("/api/"))' | head -n 50

Step 3: Always Truncate Output

Even after narrowing, always pipe through truncation:

# ALWAYS use head -c to limit total bytes (max 50KB)
{baseDir}/scripts/burp-search.sh project.burp proxyHistory.request.headers | head -c 50000

# For body searches, truncate each JSON object's body field:
{baseDir}/scripts/burp-search.sh project.burp "responseBody='pattern'" | \
  head -n 20 | jq -c '.body = (.body | if length > 1000 then .[:1000] + "...[TRUNCATED]" else . end)'

# Limit both record count AND byte size:
{baseDir}/scripts/burp-search.sh project.burp auditItems | head -n 50 | head -c 50000


Hard limits to enforce:

head -c 50000 (50KB max) on ALL output
Truncate .body fields to 1000 chars - MANDATORY, no exceptions
jq -c '.body = (.body[:1000] + "...[TRUNCATED]")'


Never run these without counting first AND truncating:

proxyHistory / siteMap (full dumps - always use sub-component filters)
responseBody='...' searches (bodies can be megabytes each)
Any broad regex like .* or .+
Investigation Workflow

Identify scope - What are you looking for? (specific vuln type, endpoint, header pattern)

Search audit items first - Start with Burp's findings:

{baseDir}/scripts/burp-search.sh project.burp auditItems | jq 'select(.severity == "High")'


Check confidence scores - Filter for actionable findings:

... | jq 'select(.confidence == "Certain" or .confidence == "Firm")'


Extract affected URLs - Get the attack surface:

... | jq -r '.url' | sort -u


Search raw traffic for context - Examine actual requests/responses:

{baseDir}/scripts/burp-search.sh project.burp "responseBody='pattern'"


Validate manually - Burp findings are indicators, not proof. Verify each one.

Understanding Results
Severity vs Confidence

Burp reports both severity (High/Medium/Low) and confidence (Certain/Firm/Tentative). Use both when triaging:

Combination	Meaning
High + Certain	Likely real vulnerability, prioritize investigation
High + Tentative	Often a false positive, verify before reporting
Medium + Firm	Worth investigating, may need manual validation

A "High severity, Tentative confidence" finding is frequently a false positive. Don't report findings based on severity alone.

When Proxy History is Incomplete

Proxy history only contains what Burp captured. It may be missing traffic due to:

Scope filters excluding domains
Intercept settings dropping requests
Browser traffic not routed through Burp proxy

If you don't find expected traffic, check Burp's scope and proxy settings in the original project.

HTTP Body Encoding

Response bodies may be gzip compressed, chunked, or use non-UTF8 encoding. Regex patterns that work on plaintext may silently fail on encoded responses. If searches return fewer results than expected:

Check if responses are compressed
Try broader patterns or search headers first
Use Burp's UI to inspect raw vs rendered response
Rationalizations to Reject

Common shortcuts that lead to missed vulnerabilities or false reports:

Shortcut	Why It's Wrong
"This regex looks good"	Verify on sample data first—encoding and escaping cause silent failures
"High severity = must fix"	Check confidence score too; Burp has false positives
"All audit items are relevant"	Filter by actual threat model; not every finding matters for every app
"Proxy history is complete"	May be filtered by Burp scope/intercept settings; you see only what Burp captured
"Burp found it, so it's a vuln"	Burp findings require manual verification—they indicate potential issues, not proof
Output Format

All output is JSON, one object per line. Pipe to jq for formatting:

{baseDir}/scripts/burp-search.sh project.burp auditItems | jq .


Filter with grep:

{baseDir}/scripts/burp-search.sh project.burp auditItems | grep -i "sql injection"

Examples

Search for CORS headers (with byte limit):

{baseDir}/scripts/burp-search.sh project.burp "responseHeader='.*Access-Control.*'" | head -c 50000


Get all high-severity findings (audit items are small, but still limit):

{baseDir}/scripts/burp-search.sh project.burp auditItems | jq -c 'select(.severity == "High")' | head -n 100


Extract just request URLs from proxy history:

{baseDir}/scripts/burp-search.sh project.burp proxyHistory.request.headers | jq -r '.request.url' | head -n 200


Search response bodies (MUST truncate body to 1000 chars):

{baseDir}/scripts/burp-search.sh project.burp "responseBody='.*password.*'" | \
  head -n 10 | jq -c '.body = (.body[:1000] + "...[TRUNCATED]")'

Platform Configuration

The wrapper script requires two environment variables to locate Burp Suite's bundled Java and JAR file.

macOS
export BURP_JAVA="/Applications/Burp Suite Professional.app/Contents/Resources/jre.bundle/Contents/Home/bin/java"
export BURP_JAR="/Applications/Burp Suite Professional.app/Contents/Resources/app/burpsuite_pro.jar"

Windows
$env:BURP_JAVA = "C:\Program Files\BurpSuiteProfessional\jre\bin\java.exe"
$env:BURP_JAR = "C:\Program Files\BurpSuiteProfessional\burpsuite_pro.jar"

Linux
export BURP_JAVA="/opt/BurpSuiteProfessional/jre/bin/java"
export BURP_JAR="/opt/BurpSuiteProfessional/burpsuite_pro.jar"


Add these exports to your shell profile (.bashrc, .zshrc, etc.) for persistence.

Manual Invocation

If not using the wrapper script, invoke directly:

"$BURP_JAVA" -jar -Djava.awt.headless=true "$BURP_JAR" \
  --project-file=/path/to/project.burp [FLAGS]

Weekly Installs
1.7K
Repository
trailofbits/skills
GitHub Stars
5.0K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykFail