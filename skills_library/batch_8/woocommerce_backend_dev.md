---
title: woocommerce-backend-dev
url: https://skills.sh/woocommerce/woocommerce/woocommerce-backend-dev
---

# woocommerce-backend-dev

skills/woocommerce/woocommerce/woocommerce-backend-dev
woocommerce-backend-dev
Installation
$ npx skills add https://github.com/woocommerce/woocommerce --skill woocommerce-backend-dev
SKILL.md
WooCommerce Backend Development

This skill provides guidance for developing WooCommerce backend PHP code according to project standards and conventions.

When to Use This Skill

ALWAYS invoke this skill before:

Writing new PHP unit tests (*Test.php files)
Creating new PHP classes
Modifying existing backend PHP code
Adding hooks or filters
Instructions

Follow WooCommerce project conventions when adding or modifying backend PHP code:

Creating new code structures: See file-entities.md for conventions on creating classes and organizing files (but for new unit test files see unit-tests.md).
Naming conventions: See code-entities.md for naming methods, variables, and parameters
Coding style: See coding-conventions.md for general coding standards and best practices
Type annotations: See type-annotations.md for PHPStan-aware PHPDoc annotations
Working with hooks: See hooks.md for hook callback conventions and documentation
Dependency injection: See dependency-injection.md for DI container usage
Data integrity: See data-integrity.md for ensuring data integrity when performing CRUD operations
Writing tests: See unit-tests.md for unit testing conventions
Key Principles
Always follow WordPress Coding Standards
Use class methods instead of standalone functions
Place new internal classes in src/Internal/ by default
Use PSR-4 autoloading with Automattic\WooCommerce namespace
Write comprehensive unit tests for new functionality
Run linting and tests before committing changes
Version Information

To determine the next WooCommerce version number for @since annotations:

Read the $version property in includes/class-woocommerce.php on the trunk branch
Remove the -dev suffix if present
Example: If trunk shows 10.4.0-dev, use @since 10.4.0
Note: When reviewing PRs against trunk, the version in trunk is correct even if it seems "future" relative to released versions
Weekly Installs
523
Repository
woocommerce/woocommerce
GitHub Stars
10.3K
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass