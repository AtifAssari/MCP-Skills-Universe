---
rating: ⭐⭐
title: browser-e2e-tester
url: https://skills.sh/adaptationio/skrillz/browser-e2e-tester
---

# browser-e2e-tester

skills/adaptationio/skrillz/browser-e2e-tester
browser-e2e-tester
Installation
$ npx skills add https://github.com/adaptationio/skrillz --skill browser-e2e-tester
SKILL.md
Browser E2E Tester

Runs browser-based end-to-end tests to verify feature implementation meets acceptance criteria.

Quick Start
Run Feature Tests
from scripts.e2e_tester import E2ETester

tester = E2ETester(project_dir)
result = await tester.test_feature("auth-001")

if result.passed:
    print(f"Feature verified: {result.feature_id}")
else:
    print(f"Failed: {result.failures}")

Run All Tests
results = await tester.test_all_features()
print(f"Passed: {results.passed}/{results.total}")

E2E Testing Workflow
┌─────────────────────────────────────────────────────────────┐
│                    E2E TEST WORKFLOW                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. SETUP                                                   │
│     ├─ Load feature acceptance criteria                    │
│     ├─ Start test server (if needed)                       │
│     ├─ Initialize browser automation                       │
│     └─ Set test timeout                                    │
│                                                             │
│  2. EXECUTE                                                 │
│     ├─ Navigate to feature entry point                     │
│     ├─ Execute test steps                                  │
│     ├─ Capture screenshots on failure                      │
│     └─ Record test artifacts                               │
│                                                             │
│  3. VERIFY                                                  │
│     ├─ Check expected outcomes                             │
│     ├─ Validate UI state                                   │
│     ├─ Verify API responses                                │
│     └─ Assert data persistence                             │
│                                                             │
│  4. REPORT                                                  │
│     ├─ Generate test report                                │
│     ├─ Update feature status                               │
│     └─ Store failure artifacts                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘

Test Result Structure
@dataclass
class TestResult:
    feature_id: str
    passed: bool
    duration_ms: int
    steps_executed: int
    steps_passed: int
    failures: list[str]
    screenshots: list[Path]
    artifacts: dict

Supported Test Frameworks
Framework	Integration	Use Case
Playwright	Native	Modern web apps
Puppeteer	Adapter	Chrome-focused
Selenium	Adapter	Legacy browsers
Cypress	CLI	Component tests
Feature Acceptance Format
{
  "feature_id": "auth-001",
  "acceptance_criteria": [
    {
      "step": "Navigate to login page",
      "action": "goto",
      "target": "/login"
    },
    {
      "step": "Enter credentials",
      "action": "fill",
      "target": "#email",
      "value": "test@example.com"
    },
    {
      "step": "Submit form",
      "action": "click",
      "target": "button[type=submit]"
    },
    {
      "step": "Verify redirect",
      "action": "assert_url",
      "expected": "/dashboard"
    }
  ]
}

Integration Points
coding-agent: Triggers tests after implementation
progress-tracker: Reports test metrics
error-recoverer: Handles test failures
checkpoint-manager: Restores state on failure
References
references/E2E-PATTERNS.md - Test patterns
references/BROWSER-AUTOMATION.md - Automation guide
Scripts
scripts/e2e_tester.py - Core tester
scripts/browser_controller.py - Browser automation
scripts/test_reporter.py - Report generation
scripts/acceptance_parser.py - Criteria parser
Weekly Installs
17
Repository
adaptationio/skrillz
GitHub Stars
9
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass