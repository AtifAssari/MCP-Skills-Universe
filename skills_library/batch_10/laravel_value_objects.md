---
title: laravel-value-objects
url: https://skills.sh/leeovery/claude-laravel/laravel-value-objects
---

# laravel-value-objects

skills/leeovery/claude-laravel/laravel-value-objects
laravel-value-objects
Installation
$ npx skills add https://github.com/leeovery/claude-laravel --skill laravel-value-objects
SKILL.md
Laravel Value Objects

Value objects are simple, immutable objects representing domain concepts.

Related guides:

DTOs - DTOs are for data transfer, value objects for domain concepts
When to Use

Use value objects when:

Complex domain value with behavior
Immutability required
Rich validation logic
Need equality comparison
Encapsulating domain rules

Use DTOs when:

Transferring data between layers
No domain behavior needed
See DTOs
Simple Value Object
<?php

declare(strict_types=1);

namespace App\Values;

use App\Enums\ProcessResult as ProcessResultEnum;

class ProcessResult
{
    public function __construct(
        public readonly ProcessResultEnum $result,
        public readonly ?string $message = null,
    ) {}

    public static function success(?string $message = null): self
    {
        return new self(ProcessResultEnum::Success, $message);
    }

    public static function skip(?string $message = null): self
    {
        return new self(ProcessResultEnum::Skip, $message);
    }

    public static function fail(?string $message = null): self
    {
        return new self(ProcessResultEnum::Fail, $message);
    }

    public function isSuccess(): bool
    {
        return $this->result === ProcessResultEnum::Success;
    }

    public function isFail(): bool
    {
        return $this->result === ProcessResultEnum::Fail;
    }
}

Money Value Object

View full implementation →

Usage Examples
ProcessResult
// In actions
return ProcessResult::success('Order processed successfully');
return ProcessResult::skip('Order already processed');
return ProcessResult::fail('Payment declined');

// Checking results
if ($result->isSuccess()) {
    // Handle success
}

if ($result->isFail()) {
    // Handle failure
}

Money
// Creating money values
$price = Money::fromDollars(29.99);
$tax = Money::fromDollars(2.40);
$shipping = Money::fromCents(500);  // $5.00

// Operations
$subtotal = $price->add($tax);
$total = $subtotal->add($shipping);

// Multiplication
$bulkPrice = $price->multiply(10);

// Display
echo $total->formatted();  // "37.39"

// Comparison
if ($total->equals($expectedTotal)) {
    // Amounts match
}

Key Patterns
1. Immutability

Use readonly properties:

public readonly int $amount;
public readonly string $currency;

2. Static Factory Methods

Named constructors for common scenarios:

public static function fromDollars(float $dollars): self
public static function success(?string $message = null): self

3. Private Constructor

Force use of factory methods:

private function __construct(/* ... */) {}

4. Domain Logic

Encapsulate domain rules:

public function add(Money $other): self
{
    $this->assertSameCurrency($other);
    return new self($this->amount + $other->amount, $this->currency);
}

5. Return New Instances

Operations return new instances (immutability):

public function add(Money $other): self
{
    return new self($this->amount + $other->amount, $this->currency);
}

Directory Structure
app/Values/
├── Money.php
├── ProcessResult.php
├── Coordinate.php
└── EmailAddress.php

Summary

Value objects:

Are immutable (use readonly)
Have static factory methods
Encapsulate domain logic
Return new instances from operations
Validate in constructor

Use for domain concepts with behavior, not simple data transfer.

Weekly Installs
28
Repository
leeovery/claude-laravel
GitHub Stars
43
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass