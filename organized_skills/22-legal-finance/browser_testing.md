---
rating: ⭐⭐⭐
title: browser-testing
url: https://skills.sh/serkan-ozal/browser-devtools-skills/browser-testing
---

# browser-testing

skills/serkan-ozal/browser-devtools-skills/browser-testing
browser-testing
Installation
$ npx skills add https://github.com/serkan-ozal/browser-devtools-skills --skill browser-testing
SKILL.md
Browser Testing Skill

Automated browser testing, interaction automation, and form testing using Browser DevTools CLI.

When to Use

This skill activates when:

User asks to test a web page or application
User wants to automate browser interactions
User needs to verify UI behavior
User wants to automate form submission
User needs to test form validation
User mentions multi-step forms or wizards
User wants to test login/signup flows
Capabilities
Navigation
browser-devtools-cli navigation go-to --url "https://example.com"
browser-devtools-cli navigation go-back-or-forward --direction back
browser-devtools-cli navigation go-back-or-forward --direction forward
browser-devtools-cli navigation reload

Interaction

All accept CSS selector or ref (e1, @e1) from ARIA snapshot.

browser-devtools-cli interaction click --selector "#button"
browser-devtools-cli interaction click --selector "e1"   # ref from a11y take-aria-snapshot
browser-devtools-cli interaction fill --selector "#input" --value "text"
browser-devtools-cli interaction select --selector "#dropdown" --value "option"
browser-devtools-cli interaction hover --selector "#element"
browser-devtools-cli interaction press-key --key "Enter"
browser-devtools-cli interaction scroll --mode bottom
browser-devtools-cli interaction drag --source-selector "#drag" --target-selector "#drop"

Content Capture
browser-devtools-cli content take-screenshot --name "screenshot"
browser-devtools-cli content get-as-html
browser-devtools-cli content get-as-text
browser-devtools-cli content save-as-pdf --name "page"

Synchronization
browser-devtools-cli sync wait-for-network-idle

Mocking & Stubbing
browser-devtools-cli stub mock-http-response --pattern "**/api/**" --response '{"status":200}'
browser-devtools-cli stub intercept-http-request --pattern "**/api/**" --modifications '{"headers":{}}'
browser-devtools-cli stub list
browser-devtools-cli stub clear

Basic Testing Workflow
Navigate: Go to the page under test
Wait: Ensure page is fully loaded
Snapshot (optional): a11y take-aria-snapshot to get refs (e1, e2) for stable element targeting
Interact: Click, fill, scroll (use --selector "e1" for refs or CSS selector)
Verify: Check page state, take screenshots
Document: Report results
Form Automation Patterns
Basic Form Fill
# Fill text input
browser-devtools-cli interaction fill \
  --selector "#email" \
  --value "test@example.com"

# Fill password
browser-devtools-cli interaction fill \
  --selector "#password" \
  --value "SecurePass123"

# Click submit
browser-devtools-cli interaction click \
  --selector "button[type=submit]"

Select Dropdown
browser-devtools-cli interaction select \
  --selector "#country" \
  --value "US"

Checkbox/Radio
# Check checkbox
browser-devtools-cli interaction click \
  --selector "#terms-checkbox"

# Select radio option
browser-devtools-cli interaction click \
  --selector "input[name=plan][value=premium]"

Multi-Step Wizard
SESSION="--session-id wizard-test"

# Step 1: Personal Info
browser-devtools-cli $SESSION interaction fill --selector "#name" --value "John Doe"
browser-devtools-cli $SESSION interaction fill --selector "#email" --value "john@example.com"
browser-devtools-cli $SESSION interaction click --selector "#next-step"

# Wait for step 2
browser-devtools-cli $SESSION sync wait-for-network-idle

# Step 2: Address
browser-devtools-cli $SESSION interaction fill --selector "#address" --value "123 Main St"
browser-devtools-cli $SESSION interaction select --selector "#state" --value "CA"
browser-devtools-cli $SESSION interaction click --selector "#next-step"

# Step 3: Confirm
browser-devtools-cli $SESSION sync wait-for-network-idle
browser-devtools-cli $SESSION interaction click --selector "#submit"

Validation Testing
Test Required Fields
# Submit empty form
browser-devtools-cli interaction click --selector "button[type=submit]"

# Check for error messages
browser-devtools-cli content get-as-text --selector ".error-message"

Test Invalid Input
# Invalid email
browser-devtools-cli interaction fill --selector "#email" --value "not-an-email"
browser-devtools-cli interaction click --selector "button[type=submit]"

# Check validation error
browser-devtools-cli content get-as-html --selector ".email-error"

Session-Based Testing
SESSION="--session-id my-test"

# Navigate
browser-devtools-cli $SESSION navigation go-to --url "https://example.com"

# Interact
browser-devtools-cli $SESSION interaction click --selector ".login-btn"
browser-devtools-cli $SESSION interaction fill --selector "#email" --value "test@example.com"

# Verify
browser-devtools-cli $SESSION content take-screenshot --name "after-login"

# Cleanup
browser-devtools-cli session delete my-test

Best Practices
Use sessions for multi-step flows
Wait for network idle after navigation and actions
Take screenshots after important actions for verification
Use specific selectors to avoid wrong elements
Test empty submission first for validation testing
Clear fields before filling (use interaction fill which clears first)
Handle dynamic fields with wait strategies
Screenshot after errors for documentation
Batch steps when useful: For long flows, run execute --code "..." with callTool() reduces round-trips (see browser-devtools-cli execute reference).
Weekly Installs
39
Repository
serkan-ozal/bro…s-skills
GitHub Stars
7
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail