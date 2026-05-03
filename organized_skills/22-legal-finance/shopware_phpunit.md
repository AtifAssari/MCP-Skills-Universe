---
rating: ⭐⭐
title: shopware-phpunit
url: https://skills.sh/friendsofshopware/agent-skills/shopware-phpunit
---

# shopware-phpunit

skills/friendsofshopware/agent-skills/shopware-phpunit
shopware-phpunit
Installation
$ npx skills add https://github.com/friendsofshopware/agent-skills --skill shopware-phpunit
SKILL.md
Shopware PHPUnit Best Practices
When to Apply
Writing new PHPUnit tests for a Shopware 6 plugin or app
Setting up test infrastructure for a Shopware project
Testing repositories, services, commands, or event subscribers
Writing integration tests that require the Shopware kernel
Testing Storefront controllers or Store API / Admin API routes
Debugging failing tests in a Shopware context
Rule Categories by Priority
Priority	Category	Prefix	Description
CRITICAL	Test Setup	setup-	Kernel bootstrap, base test classes, PHPUnit configuration
HIGH	Integration Testing	integration-	Repository tests, service tests, database transactions
HIGH	API Testing	api-	Store API and Admin API endpoint testing
MEDIUM	Mocking	mock-	Service mocking, dependency injection in tests
MEDIUM	Data	data-	Test data creation, fixtures, cleanup
LOW	Performance	perf-	Test execution speed, parallel testing
How to Use

Read relevant reference files from the references/ directory based on the task at hand. Files are prefixed by category for easy discovery.

External References
Shopware Developer Documentation - Testing
PHPUnit Documentation
Weekly Installs
53
Repository
friendsofshopwa…t-skills
GitHub Stars
9
First Seen
Feb 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass