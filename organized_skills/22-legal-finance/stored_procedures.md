---
rating: ⭐⭐
title: stored-procedures
url: https://skills.sh/aj-geddes/useful-ai-prompts/stored-procedures
---

# stored-procedures

skills/aj-geddes/useful-ai-prompts/stored-procedures
stored-procedures
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill stored-procedures
SKILL.md
Stored Procedures & Functions
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Implement stored procedures, functions, and triggers for business logic, data validation, and performance optimization. Covers procedure design, error handling, and performance considerations.

When to Use
Business logic encapsulation
Complex multi-step operations
Data validation and constraints
Audit trail maintenance
Performance optimization
Code reusability across applications
Trigger-based automation
Quick Start

PostgreSQL - Scalar Function:

-- Create function returning single value
CREATE OR REPLACE FUNCTION calculate_order_total(
  p_subtotal DECIMAL,
  p_tax_rate DECIMAL,
  p_shipping DECIMAL
)
RETURNS DECIMAL AS $$
BEGIN
  RETURN ROUND((p_subtotal * (1 + p_tax_rate) + p_shipping)::NUMERIC, 2);
END;
$$ LANGUAGE plpgsql IMMUTABLE;

-- Use in queries
SELECT id, subtotal, calculate_order_total(subtotal, 0.08, 10) as total
FROM orders;

-- Or in application code
SELECT * FROM orders
WHERE calculate_order_total(subtotal, 0.08, 10) > 100;

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Simple Functions	Simple Functions
Stored Procedures	Stored Procedures
Simple Procedures	Simple Procedures
Complex Procedures with Error Handling	Complex Procedures with Error Handling
PostgreSQL Triggers	PostgreSQL Triggers
MySQL Triggers	MySQL Triggers
Best Practices
✅ DO
Follow established patterns and conventions
Write clean, maintainable code
Add appropriate documentation
Test thoroughly before deploying
❌ DON'T
Skip testing or validation
Ignore error handling
Hard-code configuration values
Weekly Installs
274
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn