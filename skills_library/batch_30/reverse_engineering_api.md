---
title: reverse-engineering-api
url: https://skills.sh/kalil0321/reverse-api-engineer/reverse-engineering-api
---

# reverse-engineering-api

skills/kalil0321/reverse-api-engineer/reverse-engineering-api
reverse-engineering-api
Installation
$ npx skills add https://github.com/kalil0321/reverse-api-engineer --skill reverse-engineering-api
SKILL.md
Reverse Engineering API Skill

This skill enables you to reverse engineer web APIs by:

Controlling a browser with HAR recording enabled
Analyzing captured network traffic
Generating production-ready Python API clients
Prerequisites
Playwright MCP: You must have access to Playwright MCP tools for browser control
HAR Recording: The browser must be configured to record HAR files
Python: For running analysis scripts and generated clients
Workflow Overview
[User Task] -> [Browser Capture] -> [HAR Analysis] -> [API Client Generation] -> [Testing & Refinement]

Phase 0: Preparation (Using HAR Helper Scripts)
Available Helper Scripts

This skill provides Python utilities for HAR analysis located at:

Script Directory: plugins/reverse-api-engineer/skills/reverse-engineering-api/scripts/

Available Scripts:

har_filter.py - Filter HAR files to API endpoints only
har_analyze.py - Extract structured endpoint information
har_validate.py - Validate generated code against HAR analysis
har_utils.py - Shared utility functions
Script Usage Pattern

Use these scripts in sequence for optimal code generation:

# 1. Filter HAR to remove noise (static assets, analytics, CDN)
python {SKILL_DIR}/scripts/har_filter.py {har_path} --output filtered.har --stats

# 2. Analyze endpoints and extract patterns
python {SKILL_DIR}/scripts/har_analyze.py filtered.har --output analysis.json

# 3. Read analysis for code generation guidance
cat analysis.json

# 4. Generate API client code based on analysis

# 5. Validate generated code
python {SKILL_DIR}/scripts/har_validate.py api_client.py analysis.json

Why Use These Scripts?

har_filter.py benefits:

Reduces HAR file size by 80-90% (removes noise)
Focuses analysis on actual API calls
Significantly improves code generation quality
Outputs statistics showing what was filtered

har_analyze.py benefits:

Provides structured endpoint information
Detects authentication patterns automatically
Identifies pagination mechanisms
Extracts request/response schemas
Groups endpoints by pattern

har_validate.py benefits:

Ensures all endpoints are implemented
Validates authentication handling
Checks for proper error handling
Calculates coverage score (must be >= 90)
Identifies missing features
Task Tracking

Use TodoWrite to track workflow progress:

Mark tasks as pending, in_progress, or completed
Only ONE task should be in_progress at a time
Complete ALL tasks - never stop early

Example TodoWrite usage:

TodoWrite([
  {"content": "Filter HAR using har_filter.py", "status": "in_progress", "activeForm": "Filtering HAR"},
  {"content": "Analyze HAR using har_analyze.py", "status": "pending", "activeForm": "Analyzing endpoints"},
  {"content": "Generate API client", "status": "pending", "activeForm": "Generating code"},
  {"content": "Validate using har_validate.py", "status": "pending", "activeForm": "Validating code"},
  {"content": "Test implementation", "status": "pending", "activeForm": "Testing API client"}
])


CRITICAL: Task tracking ensures complete workflow execution. Never skip tasks or stop early.

Phase 1: Browser Capture with HAR Recording
Starting the Browser

When starting a browser session for API capture:

Launch browser with HAR recording enabled via Playwright MCP
Generate a unique run ID: {run_id}
Configure HAR output path: ~/.reverse-api/runs/har/{run_id}/recording.har
During Capture

Navigate autonomously to trigger the API calls needed:

Login flows (capture authentication)
Data fetching (capture GET endpoints)
Form submissions (capture POST/PUT endpoints)
Pagination (capture query parameter patterns)
On Browser Close

When the browser closes, note the HAR file location:

HAR file saved to: ~/.reverse-api/runs/har/{run_id}/recording.har

Phase 2: HAR Analysis
Reading the HAR File

HAR files are JSON with this structure:

{
  "log": {
    "entries": [
      {
        "request": {
          "method": "GET|POST|PUT|DELETE",
          "url": "https://api.example.com/endpoint",
          "headers": [...],
          "postData": {...}
        },
        "response": {
          "status": 200,
          "headers": [...],
          "content": {...}
        }
      }
    ]
  }
}

Filtering Relevant Entries

Filter out noise by excluding:

Static assets: .js, .css, .png, .jpg, .svg, .woff, .ico
Analytics: google-analytics, segment, mixpanel, hotjar
Ads: doubleclick, adsense, facebook.com/tr
CDN resources: cloudflare, cdn., static.

Focus on:

API endpoints: /api/, /v1/, /v2/, /graphql
XHR/Fetch requests with JSON responses
Requests with authentication headers
Extracting Patterns

For each relevant endpoint, extract:

URL Pattern: Base URL, path, query parameters
Method: GET, POST, PUT, DELETE, PATCH
Headers:
Required headers (Authorization, Content-Type, custom headers)
Optional headers (User-Agent, Accept)
Request Body: JSON schema, form data structure
Response Schema: JSON structure, status codes
Authentication: See references/AUTH_PATTERNS.md
Phase 3: API Client Generation
Code Structure

Generate a Python module with:

{output_dir}/
  api_client.py    # Main API client class
  README.md        # Usage documentation

api_client.py Template
"""
Auto-generated API client for {domain}
Generated from HAR capture on {date}
"""

import requests
from typing import Optional, Dict, Any, List
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class {ClassName}Client:
    """API client for {domain}."""
    
    def __init__(
        self,
        base_url: str = "{base_url}",
        session: Optional[requests.Session] = None,
    ):
        self.base_url = base_url.rstrip("/")
        self.session = session or requests.Session()
        self._setup_session()
    
    def _setup_session(self):
        """Configure session with default headers."""
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (compatible)",
            "Accept": "application/json",
            # Add other required headers
        })
    
    def _request(
        self,
        method: str,
        endpoint: str,
        **kwargs,
    ) -> requests.Response:
        """Make an HTTP request with error handling."""
        url = f"{self.base_url}{endpoint}"
        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")
            raise
    
    # Generated endpoint methods go here
    def get_example(self, param: str) -> Dict[str, Any]:
        """
        Fetch example data.
        
        Args:
            param: Description of parameter
            
        Returns:
            JSON response data
        """
        response = self._request("GET", f"/api/example/{param}")
        return response.json()


# Example usage
if __name__ == "__main__":
    client = {ClassName}Client()
    # Example calls

Code Quality Requirements

All generated code must include:

Type hints for all parameters and return values
Docstrings for all public methods
Error handling with try-except blocks
Logging for debugging
Session management for connection reuse
Authentication handling based on detected patterns
Phase 4: Testing & Refinement
Testing the Generated Client

After generating the client:

Run the example usage section
Verify responses match expected structure
Handle any errors encountered
Iteration Protocol

You have up to 5 attempts to fix issues:

Attempt 1: Initial implementation
  - What was tried
  - What failed (if anything)
  - What was changed

Attempt 2: Refinement
  ...

Common Issues
Issue	Solution
403 Forbidden	Add missing headers, check authentication
Bot detection	Switch to Playwright with stealth mode
Rate limiting	Add delays, respect Retry-After headers
Session expiry	Implement token refresh logic
CORS errors	Use server-side requests (not applicable to Python)
Domain Discovery (Optional)

Before capture, you may want to map the domain to understand its structure.

Using the Mapper Script

Run scripts/mapper.py to quickly discover:

All pages on the domain or subdomains
Subdomains

It is useful for generalizing your scripts on multitenants websites.

For example, for Ashby ATS or Workday it's useful to find other companies using this ATS when trying to generalize your script.

python scripts/mapper.py https://example.com

Using the Sitemap Parser

Run scripts/sitemap.py to extract URLs from sitemaps:

python scripts/sitemap.py https://example.com

Output Locations
HAR files: ~/.reverse-api/runs/har/{run_id}/
Generated scripts: ./{task_name}
Example Session
User: "Create an API client for the Apple Jobs website"


1. [Browser Capture]
   Launch browser with HAR recording
   Navigate to jobs.apple.com
   Perform search, browse listings
   Close browser
   HAR saved to: ~/.reverse-api/runs/har/{run_id}/recording.har

   Note: you can monitor browser requests with the Playwright MCP

2. [HAR Analysis]
   Found endpoints:
   - GET /api/role/search?query=...
   - GET /api/role/{id}
   Authentication: None required (public API)

3. [Generate Client]
   Create : {task_name}/api_client.py
   
4. [Test]
   Ran example usage - Success!
   
5. [Summary]
   Generated Apple Jobs API client with:
   - search_roles(query, location, page)
   - get_role(role_id)
   Files: ./{task_name}/

Weekly Installs
129
Repository
kalil0321/rever…engineer
GitHub Stars
662
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail