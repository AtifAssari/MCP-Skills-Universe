---
title: hyperexecute-skill
url: https://skills.sh/lambdatest/agent-skills/hyperexecute-skill
---

# hyperexecute-skill

skills/lambdatest/agent-skills/hyperexecute-skill
hyperexecute-skill
Installation
$ npx skills add https://github.com/lambdatest/agent-skills --skill hyperexecute-skill
SKILL.md
HyperExecute Skill
Core Patterns
Basic YAML Configuration
---
version: 0.1
globalTimeout: 90
testSuiteTimeout: 90
testSuiteStep: 90

runson: linux  # or win, mac

autosplit: true
retryOnFailure: true
maxRetries: 2

concurrency: 10

pre:
  - npm install
  - npx playwright install

testDiscovery:
  type: raw
  mode: dynamic
  command: grep -rn 'test(' tests/ --include='*.spec.ts' -l

testRunnerCommand: npx playwright test $test --project=chromium

framework:
  name: playwright
  args:
    buildName: "HyperExecute Build"

env:
  LT_USERNAME: ${LT_USERNAME}
  LT_ACCESS_KEY: ${LT_ACCESS_KEY}

Matrix Mode (Cross-Browser)
version: 0.1
runson: linux
concurrency: 10

matrix:
  browser: ["chromium", "firefox", "webkit"]
  os: ["linux"]

pre:
  - npm install
  - npx playwright install

testSuites:
  - npx playwright test --project=$browser

Hybrid Mode
version: 0.1
runson: linux
concurrency: 5

testDiscovery:
  type: raw
  mode: static
  command: cat testSuites.txt

testRunnerCommand: mvn test -Dtest=$test

pre:
  - mvn compile -DskipTests

post:
  - cat target/surefire-reports/*.txt

Upload & Run
# Download CLI
curl -O https://downloads.lambdatest.com/hyperexecute/linux/hyperexecute
chmod +x hyperexecute

# Execute
./hyperexecute --user $LT_USERNAME --key $LT_ACCESS_KEY \
  --config hyperexecute.yaml

Framework Examples

Selenium + Java:

pre:
  - mvn compile -DskipTests
testDiscovery:
  type: raw
  mode: dynamic
  command: grep -rn '@Test' src/test --include='*.java' -l | sed 's|src/test/java/||;s|.java||;s|/|.|g'
testRunnerCommand: mvn test -Dtest=$test


Cypress:

pre:
  - npm install
testDiscovery:
  type: raw
  mode: dynamic
  command: find cypress/e2e -name '*.cy.js' | sed 's|cypress/e2e/||'
testRunnerCommand: npx cypress run --spec "cypress/e2e/$test"


Pytest:

pre:
  - pip install -r requirements.txt
testDiscovery:
  type: raw
  mode: dynamic
  command: grep -rn 'def test_' tests/ --include='*.py' -l
testRunnerCommand: pytest $test -v

Anti-Patterns
Bad	Good	Why
Low concurrency	concurrency: 10+	Underusing HE speed
No pre step	Install deps in pre	Missing dependencies
Static discovery only	mode: dynamic with autosplit	Better parallelism
No retries	retryOnFailure: true	Flaky test resilience
Quick Reference
Task	Command
Run	./hyperexecute --config hyperexecute.yaml
With vars	./hyperexecute --config he.yaml --vars "browser=chrome"
Debug	--verbose flag
Download CLI	https://downloads.lambdatest.com/hyperexecute/<os>/hyperexecute
Deep Patterns

For advanced patterns, debugging guides, CI/CD integration, and best practices, see reference/playbook.md.

Weekly Installs
41
Repository
lambdatest/agent-skills
GitHub Stars
247
First Seen
Feb 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail