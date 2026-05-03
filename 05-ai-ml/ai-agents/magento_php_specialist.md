---
rating: ⭐⭐
title: magento-php-specialist
url: https://skills.sh/maxnorm/magento2-agent-skills/magento-php-specialist
---

# magento-php-specialist

skills/maxnorm/magento2-agent-skills/magento-php-specialist
magento-php-specialist
Installation
$ npx skills add https://github.com/maxnorm/magento2-agent-skills --skill magento-php-specialist
SKILL.md
Magento 2 PHP Specialist

Expert specialist in leveraging advanced PHP techniques and modern practices to create high-performance, maintainable Magento 2 applications following enterprise development standards.

When to Use
Writing PHP code for Magento 2
Implementing business logic
Ensuring code quality and standards
Working with modern PHP features
Implementing design patterns
PHP Standards (STRICT ENFORCEMENT)
PSR-12 Compliance
PSR-12: Strictly adhere to PSR-12 coding standards
Magento2 Coding Standard: Follow standards in vendor/magento/magento-coding-standard/Magento2
Strict Types: declare(strict_types=1); required
EditorConfig: Check project's .editorconfig for indentation (4 spaces), line endings (LF), encoding (UTF-8)
Code Structure Requirements
Opening Braces: Classes and methods must have opening braces on their own line (PSR-12)
Constructor Property Promotion: Use with readonly modifier where appropriate
Type Hinting: All parameters and return types must be type-hinted
Strict Comparisons: Always use === and !== (never == or !=)
Constructor PHPDoc: Must include @param annotation for each parameter
Modern PHP Features
Constructor Property Promotion: Use constructor property promotion
Readonly Properties: Use readonly modifier where appropriate
Union Types: Use union types for flexible type hints
Match Expressions: Use match expressions instead of switch when appropriate
Named Arguments: Use named arguments for clarity
Code Example
<?php

/**
 * Copyright © 2025 CompanyName. All rights reserved.
 */

declare(strict_types=1);

namespace CompanyName\ModuleName\Model;

use CompanyName\ModuleName\Api\ConfigInterface;
use CompanyName\ModuleName\Api\RepositoryInterface;

class Service
{
    /**
     * @param RepositoryInterface $repository
     * @param ConfigInterface $config
     */
    public function __construct(
        private readonly RepositoryInterface $repository,
        private readonly ConfigInterface $config
    ) {
    }

    /**
     * @param int $id
     * @return EntityInterface|null
     */
    public function getById(int $id): ?EntityInterface
    {
        if ($id <= 0) {
            return null;
        }

        return $this->repository->getById($id);
    }
}

Best Practices
Object-Oriented Programming
Composition Over Inheritance: Prefer composition patterns
Dependency Injection: Constructor injection only - avoid service locators
Single Responsibility: One purpose per class/method
Interface Segregation: Use small, focused interfaces
SOLID Principles: Follow SOLID principles
Code Quality
Type Safety: 100% type coverage - parameters, return types, properties
Error Handling: Comprehensive exception handling
Logging: Use \Psr\Log\LoggerInterface for logging
Documentation: Minimal PHPDoc with @param, @return, @throws
Testing: Write unit tests for business logic
Magento-Specific Patterns
Service Contracts: Use service contracts for APIs
Repository Pattern: Implement repository pattern for data access
Factory Pattern: Use factories for object creation
Plugin Pattern: Use plugins to extend functionality
Observer Pattern: Use observers for event-driven architecture
References
PSR-12 Coding Standard
Adobe Commerce PHP Development
Coding Standards

Focus on writing clean, maintainable PHP code that follows Magento best practices.

Weekly Installs
95
Repository
maxnorm/magento…t-skills
GitHub Stars
9
First Seen
Feb 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass