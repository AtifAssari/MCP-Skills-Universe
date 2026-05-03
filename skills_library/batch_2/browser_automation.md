---
title: browser automation
url: https://skills.sh/claude-office-skills/skills/browser-automation
---

# browser automation

skills/claude-office-skills/skills/Browser Automation
Browser Automation
Installation
$ npx skills add https://github.com/claude-office-skills/skills --skill 'Browser Automation'
SKILL.md
Browser Automation

Automate web browser interactions for scraping, testing, and workflow automation.

Core Capabilities
Navigation
navigation:
  goto:
    url: "https://example.com"
    wait_until: "networkidle"
    timeout: 30000
    
  actions:
    - wait_for_selector: ".content"
    - scroll_to_bottom: true
    - wait_for_navigation: true

Element Interaction
interactions:
  click:
    selector: "button.submit"
    options:
      click_count: 1
      delay: 100
      
  type:
    selector: "input[name='email']"
    text: "user@example.com"
    options:
      delay: 50  # Human-like typing
      
  select:
    selector: "select#country"
    value: "US"
    
  file_upload:
    selector: "input[type='file']"
    files: ["document.pdf"]

Data Extraction
scraping:
  extract_text:
    selector: ".article-content"
    
  extract_all:
    selector: ".product-card"
    fields:
      name: ".product-name"
      price: ".price"
      url:
        selector: "a"
        attribute: "href"
        
  extract_table:
    selector: "table.data"
    output: json

Screenshots & PDF
capture:
  screenshot:
    path: "screenshot.png"
    full_page: true
    type: "png"
    
  pdf:
    path: "page.pdf"
    format: "A4"
    print_background: true

Workflow Examples
Form Automation
// Login and fill form
await page.goto('https://app.example.com/login');
await page.fill('#email', 'user@example.com');
await page.fill('#password', 'securepass');
await page.click('button[type="submit"]');
await page.waitForNavigation();

// Navigate to form
await page.click('a[href="/new-entry"]');
await page.fill('#title', 'Automated Entry');
await page.fill('#description', 'Created via automation');
await page.click('button.submit');

Web Scraping
scraping_workflow:
  - navigate: "https://news.example.com"
  - wait: ".article-list"
  - extract_all:
      selector: ".article"
      fields:
        title: "h2"
        summary: ".excerpt"
        link:
          selector: "a"
          attribute: "href"
  - paginate:
      next_button: ".pagination .next"
      max_pages: 10
  - output: "articles.json"

E2E Testing
test_workflow:
  - name: "User Registration"
    steps:
      - goto: "/register"
      - fill:
          "#email": "test@example.com"
          "#password": "Test123!"
      - click: "button[type='submit']"
      - assert:
          selector: ".success-message"
          text_contains: "Welcome"

Best Practices
Wait Strategies: Use proper waits
Error Handling: Catch navigation failures
Rate Limiting: Be respectful to servers
Headless Mode: Use for production
Selectors: Prefer data-testid attributes
Screenshots: Capture on failures
Weekly Installs
–
Repository
claude-office-s…s/skills
GitHub Stars
94
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail