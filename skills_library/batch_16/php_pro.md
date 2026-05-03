---
title: php-pro
url: https://skills.sh/404kidwiz/claude-supercode-skills/php-pro
---

# php-pro

skills/404kidwiz/claude-supercode-skills/php-pro
php-pro
Installation
$ npx skills add https://github.com/404kidwiz/claude-supercode-skills --skill php-pro
SKILL.md
PHP Pro
Purpose

Provides expert guidance on modern PHP development using PHP 8.2+ features, modern patterns, and the Composer ecosystem. Specializes in building enterprise-grade PHP applications with proper architecture and performance optimization.

When to Use
Building modern PHP applications
Using PHP 8.2+ features (readonly, enums, attributes)
Working with Composer and packages
Implementing PSR standards
Optimizing PHP performance
Modernizing legacy PHP codebases
Building APIs with pure PHP
Using Symfony components standalone
Quick Start

Invoke this skill when:

Developing PHP 8.2+ applications
Working with Composer packages
Implementing PSR standards
Optimizing PHP performance
Modernizing legacy PHP

Do NOT invoke when:

Laravel-specific development → use /laravel-specialist
WordPress development → use /wordpress-master
General API design → use /api-designer
Database design → use /database-administrator
Decision Framework
PHP Project Type?
├── Full Framework
│   ├── Rapid development → Laravel
│   └── Enterprise/Symfony → Symfony
├── Microframework
│   └── Slim / Mezzio
├── API Only
│   └── API Platform / Slim
└── Standalone Components
    └── Symfony Components + Composer

Core Workflows
1. Modern PHP Setup
Install PHP 8.2+ with required extensions
Initialize Composer project
Configure PSR-4 autoloading
Set up coding standards (PHP-CS-Fixer, PHPStan)
Configure error handling
Implement dependency injection
2. PHP 8.2+ Feature Usage
Use readonly classes for DTOs
Apply enums for fixed value sets
Leverage attributes for metadata
Use named arguments for clarity
Implement intersection types
Apply null-safe operator
3. Performance Optimization
Enable OPcache with proper settings
Use preloading for stable code
Implement JIT where beneficial
Profile with Xdebug/Blackfire
Optimize database queries
Implement caching layers
Best Practices
Use strict types in all files (declare(strict_types=1))
Follow PSR-12 coding standards
Use type hints for all parameters and returns
Leverage Composer for autoloading
Use PHPStan or Psalm for static analysis
Write tests with PHPUnit or Pest
Anti-Patterns
Anti-Pattern	Problem	Correct Approach
No type hints	Runtime errors	Use strict types
Global state	Hard to test	Dependency injection
Manual autoloading	Error-prone	Composer autoload
Suppressing errors (@)	Hidden bugs	Handle errors properly
No static analysis	Type bugs	PHPStan/Psalm
Weekly Installs
92
Repository
404kidwiz/claud…e-skills
GitHub Stars
76
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass