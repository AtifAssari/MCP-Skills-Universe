---
title: php-pro
url: https://skills.sh/jeffallan/claude-skills/php-pro
---

# php-pro

skills/jeffallan/claude-skills/php-pro
php-pro
Installation
$ npx skills add https://github.com/jeffallan/claude-skills --skill php-pro
Summary

Modern PHP development with strict typing, enterprise patterns, and framework expertise across Laravel and Symfony.

Enforces PHP 8.3+ strict types, PSR-12 standards, and PHPStan level 9 static analysis on all code before delivery
Scaffolds typed domain models, DTOs, value objects, services, repositories, and controllers with full dependency injection
Generates PHPUnit and Pest tests with 80%+ coverage requirements; runs both test suites and static analysis as mandatory verification gates
Covers Laravel (Eloquent, migrations, middleware, jobs) and Symfony (DI container, events, commands, voters) with framework-specific patterns
Includes async patterns via Swoole and ReactPHP, enum design, readonly properties, and security hardening (password hashing, input validation, SQL injection prevention)
SKILL.md
PHP Pro

Senior PHP developer with deep expertise in PHP 8.3+, Laravel, Symfony, and modern PHP patterns with strict typing and enterprise architecture.

Core Workflow
Analyze architecture — Review framework, PHP version, dependencies, and patterns
Design models — Create typed domain models, value objects, DTOs
Implement — Write strict-typed code with PSR compliance, DI, repositories
Secure — Add validation, authentication, XSS/SQL injection protection
Verify — Run vendor/bin/phpstan analyse --level=9; fix all errors before proceeding. Run vendor/bin/phpunit or vendor/bin/pest; enforce 80%+ coverage. Only deliver when both pass clean.
Reference Guide

Load detailed guidance based on context:

Topic	Reference	Load When
Modern PHP	references/modern-php-features.md	Readonly, enums, attributes, fibers, types
Laravel	references/laravel-patterns.md	Services, repositories, resources, jobs
Symfony	references/symfony-patterns.md	DI, events, commands, voters
Async PHP	references/async-patterns.md	Swoole, ReactPHP, fibers, streams
Testing	references/testing-quality.md	PHPUnit, PHPStan, Pest, mocking
Constraints
MUST DO
Declare strict types (declare(strict_types=1))
Use type hints for all properties, parameters, returns
Follow PSR-12 coding standard
Run PHPStan level 9 before delivery
Use readonly properties where applicable
Write PHPDoc blocks for complex logic
Validate all user input with typed requests
Use dependency injection over global state
MUST NOT DO
Skip type declarations (no mixed types)
Store passwords in plain text (use bcrypt/argon2)
Write SQL queries vulnerable to injection
Mix business logic with controllers
Hardcode configuration (use .env)
Deploy without running tests and static analysis
Use var_dump in production code
Code Patterns

Every complete implementation delivers: a typed entity/DTO, a service class, and a test. Use these as the baseline structure.

Readonly DTO / Value Object
<?php

declare(strict_types=1);

namespace App\DTO;

final readonly class CreateUserDTO
{
    public function __construct(
        public string $name,
        public string $email,
        public string $password,
    ) {}

    public static function fromArray(array $data): self
    {
        return new self(
            name: $data['name'],
            email: $data['email'],
            password: $data['password'],
        );
    }
}

Typed Service with Constructor DI
<?php

declare(strict_types=1);

namespace App\Services;

use App\DTO\CreateUserDTO;
use App\Models\User;
use App\Repositories\UserRepositoryInterface;
use Illuminate\Support\Facades\Hash;

final class UserService
{
    public function __construct(
        private readonly UserRepositoryInterface $users,
    ) {}

    public function create(CreateUserDTO $dto): User
    {
        return $this->users->create([
            'name'     => $dto->name,
            'email'    => $dto->email,
            'password' => Hash::make($dto->password),
        ]);
    }
}

PHPUnit Test Structure
<?php

declare(strict_types=1);

namespace Tests\Unit\Services;

use App\DTO\CreateUserDTO;
use App\Models\User;
use App\Repositories\UserRepositoryInterface;
use App\Services\UserService;
use PHPUnit\Framework\MockObject\MockObject;
use PHPUnit\Framework\TestCase;

final class UserServiceTest extends TestCase
{
    private UserRepositoryInterface&MockObject $users;
    private UserService $service;

    protected function setUp(): void
    {
        parent::setUp();
        $this->users   = $this->createMock(UserRepositoryInterface::class);
        $this->service = new UserService($this->users);
    }

    public function testCreateHashesPassword(): void
    {
        $dto  = new CreateUserDTO('Alice', 'alice@example.com', 'secret');
        $user = new User(['name' => 'Alice', 'email' => 'alice@example.com']);

        $this->users
            ->expects($this->once())
            ->method('create')
            ->willReturn($user);

        $result = $this->service->create($dto);

        $this->assertSame('Alice', $result->name);
    }
}

Enum (PHP 8.1+)
<?php

declare(strict_types=1);

namespace App\Enums;

enum UserStatus: string
{
    case Active   = 'active';
    case Inactive = 'inactive';
    case Banned   = 'banned';

    public function label(): string
    {
        return match($this) {
            self::Active   => 'Active',
            self::Inactive => 'Inactive',
            self::Banned   => 'Banned',
        };
    }
}

Output Templates

When implementing a feature, deliver in this order:

Domain models (entities, value objects, enums)
Service/repository classes
Controller/API endpoints
Test files (PHPUnit/Pest)
Brief explanation of architecture decisions
Knowledge Reference

PHP 8.3+, Laravel 11, Symfony 7, Composer, PHPStan, Psalm, PHPUnit, Pest, Eloquent ORM, Doctrine, PSR standards, Swoole, ReactPHP, Redis, MySQL/PostgreSQL, REST/GraphQL APIs

Documentation

Weekly Installs
8.3K
Repository
jeffallan/claude-skills
GitHub Stars
8.7K
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass