---
rating: ⭐⭐
title: workflow-automation
url: https://skills.sh/ruvnet/ruflo/workflow-automation
---

# workflow-automation

skills/ruvnet/ruflo/workflow-automation
workflow-automation
Installation
$ npx skills add https://github.com/ruvnet/ruflo --skill workflow-automation
SKILL.md
Workflow Automation Skill
Purpose

Create and execute automated workflows for complex multi-step processes.

When to Trigger
Multi-step automated processes
Reusable workflow creation
Complex task orchestration
CI/CD pipeline setup
Commands
Create Workflow
npx claude-flow workflow create --name "deploy-flow" --template ci

Execute Workflow
npx claude-flow workflow execute --name "deploy-flow" --env production

List Workflows
npx claude-flow workflow list

Export Template
npx claude-flow workflow export --name "deploy-flow" --format yaml

View Status
npx claude-flow workflow status --name "deploy-flow"

Built-in Templates
Template	Description
ci	Continuous integration pipeline
deploy	Deployment workflow
test	Testing workflow
release	Release automation
review	Code review workflow
Workflow Structure
name: example-workflow
steps:
  - name: analyze
    agent: researcher
    task: "Analyze requirements"
  - name: implement
    agent: coder
    depends: [analyze]
    task: "Implement solution"
  - name: test
    agent: tester
    depends: [implement]
    task: "Write and run tests"

Best Practices
Define clear step dependencies
Use appropriate agent types per step
Include validation gates
Export workflows for reuse
Weekly Installs
201
Repository
ruvnet/ruflo
GitHub Stars
35.8K
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass