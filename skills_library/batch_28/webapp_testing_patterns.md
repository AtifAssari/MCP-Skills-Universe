---
title: webapp-testing-patterns
url: https://skills.sh/bobmatnyc/claude-mpm-skills/webapp-testing-patterns
---

# webapp-testing-patterns

skills/bobmatnyc/claude-mpm-skills/webapp-testing-patterns
webapp-testing-patterns
Installation
$ npx skills add https://github.com/bobmatnyc/claude-mpm-skills --skill webapp-testing-patterns
SKILL.md
Playwright Patterns Reference

Complete guide to Playwright automation patterns, selectors, and best practices.

Table of Contents
Selectors
Wait Strategies
Element Interactions
Assertions
Test Organization
Network Interception
Screenshots and Videos
Debugging
Parallel Execution
Selectors
Text Selectors

Most readable and maintainable approach when text is unique:

page.click('text=Login')
page.click('text="Sign Up"')  # Exact match
page.click('text=/log.*in/i')  # Regex, case-insensitive

Role-Based Selectors

Semantic selectors based on ARIA roles:

page.click('role=button[name="Submit"]')
page.fill('role=textbox[name="Email"]', 'user@example.com')
page.click('role=link[name="Learn more"]')
page.check('role=checkbox[name="Accept terms"]')

CSS Selectors

Traditional CSS selectors for precise targeting:

page.click('#submit-button')
page.fill('.email-input', 'user@example.com')
page.click('button.primary')
page.click('nav > ul > li:first-child')

XPath Selectors

For complex DOM navigation:

page.click('xpath=//button[contains(text(), "Submit")]')
page.click('xpath=//div[@class="modal"]//button[@type="submit"]')

Data Attributes

Best practice for test-specific selectors:

page.click('[data-testid="submit-btn"]')
page.fill('[data-test="email-input"]', 'test@example.com')

Chaining Selectors

Combine selectors for precision:

page.locator('div.modal').locator('button.submit').click()
page.locator('role=dialog').locator('text=Confirm').click()

Selector Best Practices

Priority order (most stable to least stable):

data-testid attributes (most stable)
role= selectors (semantic, accessible)
text= selectors (readable, but text may change)
id attributes (stable if not dynamic)
CSS classes (less stable, may change with styling)
XPath (fragile, avoid if possible)
Wait Strategies
Load State Waits

Essential for dynamic applications:

# Wait for network to be idle (most common)
page.goto('http://localhost:3000')
page.wait_for_load_state('networkidle')

# Wait for DOM to be ready
page.wait_for_load_state('domcontentloaded')

# Wait for full load including images
page.wait_for_load_state('load')

Element Waits

Wait for specific elements before interacting:

# Wait for element to be visible
page.wait_for_selector('button.submit', state='visible')

# Wait for element to be hidden
page.wait_for_selector('.loading-spinner', state='hidden')

# Wait for element to exist in DOM (may not be visible)
page.wait_for_selector('.modal', state='attached')

# Wait for element to be removed from DOM
page.wait_for_selector('.error-message', state='detached')

Timeout Waits

Fixed time delays (use sparingly):

# Wait for animations to complete
page.wait_for_timeout(500)

# Wait for delayed content (better to use wait_for_selector)
page.wait_for_timeout(2000)

Custom Wait Conditions

Wait for JavaScript conditions:

# Wait for custom JavaScript condition
page.wait_for_function('() => document.querySelector(".data").innerText !== "Loading..."')

# Wait for variable to be set
page.wait_for_function('() => window.appReady === true')

Auto-Waiting

Playwright automatically waits for elements to be actionable:

# These automatically wait for element to be:
# - Visible
# - Stable (not animating)
# - Enabled (not disabled)
# - Not obscured by other elements
page.click('button.submit')  # Auto-waits
page.fill('input.email', 'test@example.com')  # Auto-waits

Element Interactions
Clicking
# Basic click
page.click('button.submit')

# Click with options
page.click('button.submit', button='right')  # Right-click
page.click('button.submit', click_count=2)  # Double-click
page.click('button.submit', modifiers=['Control'])  # Ctrl+click

# Force click (bypass actionability checks)
page.click('button.submit', force=True)

Filling Forms
# Text inputs
page.fill('input[name="email"]', 'user@example.com')
page.type('input[name="search"]', 'query', delay=100)  # Type with delay

# Clear then fill
page.fill('input[name="email"]', '')
page.fill('input[name="email"]', 'new@example.com')

# Press keys
page.press('input[name="search"]', 'Enter')
page.press('input[name="text"]', 'Control+A')

Dropdowns and Selects
# Select by label
page.select_option('select[name="country"]', label='United States')

# Select by value
page.select_option('select[name="country"]', value='us')

# Select by index
page.select_option('select[name="country"]', index=2)

# Select multiple options
page.select_option('select[multiple]', ['option1', 'option2'])

Checkboxes and Radio Buttons
# Check a checkbox
page.check('input[type="checkbox"]')

# Uncheck a checkbox
page.uncheck('input[type="checkbox"]')

# Check a radio button
page.check('input[value="option1"]')

# Toggle checkbox
if page.is_checked('input[type="checkbox"]'):
    page.uncheck('input[type="checkbox"]')
else:
    page.check('input[type="checkbox"]')

File Uploads
# Upload single file
page.set_input_files('input[type="file"]', '/path/to/file.pdf')

# Upload multiple files
page.set_input_files('input[type="file"]', ['/path/to/file1.pdf', '/path/to/file2.pdf'])

# Clear file input
page.set_input_files('input[type="file"]', [])

Hover and Focus
# Hover over element
page.hover('button.tooltip-trigger')

# Focus element
page.focus('input[name="email"]')

# Blur element
page.evaluate('document.activeElement.blur()')

Assertions
Element Visibility
from playwright.sync_api import expect

# Expect element to be visible
expect(page.locator('button.submit')).to_be_visible()

# Expect element to be hidden
expect(page.locator('.error-message')).to_be_hidden()

Text Content
# Expect exact text
expect(page.locator('.title')).to_have_text('Welcome')

# Expect partial text
expect(page.locator('.message')).to_contain_text('success')

# Expect text matching pattern
expect(page.locator('.code')).to_have_text(re.compile(r'\d{6}'))

Element State
# Expect element to be enabled/disabled
expect(page.locator('button.submit')).to_be_enabled()
expect(page.locator('button.submit')).to_be_disabled()

# Expect checkbox to be checked
expect(page.locator('input[type="checkbox"]')).to_be_checked()

# Expect element to be editable
expect(page.locator('input[name="email"]')).to_be_editable()

Attributes and Values
# Expect attribute value
expect(page.locator('img')).to_have_attribute('src', '/logo.png')

# Expect CSS class
expect(page.locator('button')).to_have_class('btn-primary')

# Expect input value
expect(page.locator('input[name="email"]')).to_have_value('user@example.com')

Count and Collections
# Expect specific count
expect(page.locator('li')).to_have_count(5)

# Get all elements and assert
items = page.locator('li').all()
assert len(items) == 5

Test Organization
Basic Test Structure
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # Test logic here
    page.goto('http://localhost:3000')
    page.wait_for_load_state('networkidle')

    browser.close()

Using Pytest (Recommended)
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

def test_login(page):
    page.goto('http://localhost:3000')
    page.fill('input[name="email"]', 'user@example.com')
    page.fill('input[name="password"]', 'password123')
    page.click('button[type="submit"]')
    expect(page.locator('.welcome-message')).to_be_visible()

Test Grouping with Describe Blocks
class TestAuthentication:
    def test_successful_login(self, page):
        # Test successful login
        pass

    def test_failed_login(self, page):
        # Test failed login
        pass

    def test_logout(self, page):
        # Test logout
        pass

Setup and Teardown
@pytest.fixture(autouse=True)
def setup_and_teardown(page):
    # Setup - runs before each test
    page.goto('http://localhost:3000')
    page.wait_for_load_state('networkidle')

    yield  # Test runs here

    # Teardown - runs after each test
    page.evaluate('localStorage.clear()')

Network Interception
Mock API Responses
# Intercept and mock API response
def handle_route(route):
    route.fulfill(
        status=200,
        body='{"success": true, "data": "mocked"}',
        headers={'Content-Type': 'application/json'}
    )

page.route('**/api/data', handle_route)
page.goto('http://localhost:3000')

Block Resources
# Block images and stylesheets for faster tests
page.route('**/*.{png,jpg,jpeg,gif,svg,css}', lambda route: route.abort())

Wait for Network Responses
# Wait for specific API call
with page.expect_response('**/api/users') as response_info:
    page.click('button.load-users')
response = response_info.value
assert response.status == 200

Screenshots and Videos
Screenshots
# Full page screenshot
page.screenshot(path='/tmp/screenshot.png', full_page=True)

# Element screenshot
page.locator('.modal').screenshot(path='/tmp/modal.png')

# Screenshot with custom dimensions
page.set_viewport_size({'width': 1920, 'height': 1080})
page.screenshot(path='/tmp/desktop.png')

Video Recording
browser = p.chromium.launch(headless=True)
context = browser.new_context(record_video_dir='/tmp/videos/')
page = context.new_page()

# Perform actions...

context.close()  # Video saved on close

Debugging
Pause Execution
page.pause()  # Opens Playwright Inspector

Console Logs
def handle_console(msg):
    print(f"[{msg.type}] {msg.text}")

page.on("console", handle_console)

Slow Motion
browser = p.chromium.launch(headless=False, slow_mo=1000)  # 1 second delay

Verbose Logging
# Set DEBUG environment variable
# DEBUG=pw:api python test.py

Parallel Execution
Pytest Parallel
# Install pytest-xdist
pip install pytest-xdist

# Run tests in parallel
pytest -n auto  # Auto-detect CPU cores
pytest -n 4     # Run with 4 workers

Browser Context Isolation
# Each test gets isolated context (cookies, localStorage, etc.)
@pytest.fixture
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture
def page(context):
    return context.new_page()

Weekly Installs
179
Repository
bobmatnyc/claud…m-skills
GitHub Stars
40
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass