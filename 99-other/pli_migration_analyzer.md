---
title: pli-migration-analyzer
url: https://skills.sh/dauquangthanh/hanoi-rainbow/pli-migration-analyzer
---

# pli-migration-analyzer

skills/dauquangthanh/hanoi-rainbow/pli-migration-analyzer
pli-migration-analyzer
Installation
$ npx skills add https://github.com/dauquangthanh/hanoi-rainbow --skill pli-migration-analyzer
SKILL.md
PL/I Migration Analyzer

Analyzes legacy PL/I programs and generates Java migration strategies. Extracts business logic, data structures, procedures, and dependencies to produce actionable migration plans.

Workflow
1. Discover PL/I Programs

Find PL/I source files in the workspace:

find . -name "*.pli" -o -name "*.PLI" -o -name "*.pl1"

2. Analyze Program Structure

For each PL/I program, extract:

Entry points: PROCEDURE OPTIONS(MAIN)
Declarations: DCL statements (FIXED DECIMAL, FIXED BINARY, CHARACTER, BIT, structures)
Procedures: Nested procedures and functions
File operations: OPEN, READ, WRITE, CLOSE statements
Exception handling: ON conditions (ENDFILE, ERROR, etc.)
Dependencies: CALL statements, %INCLUDE directives

Use scripts for automation:

extract-structure.py <source_file> - Extract structural information
analyze-dependencies.sh <directory> - Generate dependency graph
estimate-complexity.py <source_file> - Estimate migration effort
3. Map to Java Design

Convert PL/I elements to Java:

Structures → POJOs with appropriate types
Procedures → Service methods
File operations → Java I/O or database operations
ON conditions → try-catch exception handling
Arrays → Lists or arrays (adjust 1-based to 0-based indexing)

Critical Type Mapping:

FIXED DECIMAL(n,m) → BigDecimal (NEVER float/double)
FIXED BINARY(n) → int, long
CHARACTER(n) → String
BIT(1) → boolean
4. Generate Java Implementation

Create Java classes using:

generate-java-classes.py <data_structure_file> - Generate POJOs from structures

Ensure:

BigDecimal for all financial calculations
Proper exception handling (no GO TO)
Array bounds adjustment (1-based → 0-based)
String operations adjustment (SUBSTR is 1-based, substring is 0-based)
5. Produce Migration Report

Generate comprehensive report with:

Program Overview: Purpose, entry points, complexity estimate
Dependencies: Called procedures, included files, external references
Data Structures: Tables with PL/I types and Java equivalents
Business Logic Summary: Key algorithms and rules
Java Design: Proposed classes, methods, packages
Migration Estimate: Effort in person-days, risk assessment
Action Items: Prioritized tasks with owners

Use template: assets/migration-report-template.md

Quick Reference
Common Conversions

Procedure to Method:

CALC_TOTAL: PROCEDURE(qty, price) RETURNS(FIXED DECIMAL(15,2));
    result = qty * price;
    RETURN(result);
END CALC_TOTAL;


→

public BigDecimal calcTotal(BigDecimal qty, BigDecimal price) {
    return qty.multiply(price);
}


File I/O to Streams:

DO WHILE(¬eof);
    READ FILE(infile) INTO(rec);
    CALL process_record(rec);
END;


→

try (BufferedReader reader = Files.newBufferedReader(path)) {
    reader.lines().forEach(this::processRecord);
}

Critical Rules
Use BigDecimal for FIXED DECIMAL - Float/double lose precision
Arrays are 1-based in PL/I, 0-based in Java - Adjust loops and indices
Refactor GO TO statements - Use structured control flow
ON conditions map to try-catch - Exception handling strategy required
SUBSTR is 1-based - Java substring is 0-based and end-exclusive
Detailed References

For comprehensive information:

Type mapping & patterns: pli-reference.md - Complete data type conversions, code patterns, migration checklist, common pitfalls
Pseudocode translation: pseudocode-pli-rules.md - Rules for converting PL/I to pseudocode
Transaction handling: transaction-handling.md - Database transaction patterns
Performance: performance-patterns.md - Optimization strategies
Messaging: messaging-integration.md - Event-driven patterns
Testing: testing-strategy.md - Test approach and validation
Output Format

Structure migration reports with these sections:

# [Program Name] Migration Analysis

## Executive Summary
High-level overview and recommendations

## Program Overview
Purpose, functionality, complexity metrics

## Dependencies
Procedure calls, file dependencies, external references

## Data Structures
Tables mapping PL/I structures to Java classes

## Business Logic Analysis
Key algorithms, rules, calculations

## Java Design Proposal
Package structure, class design, API interfaces

## Migration Estimate
Effort (person-days), risk level, timeline

## Action Items
Prioritized tasks with acceptance criteria

Weekly Installs
12
Repository
dauquangthanh/h…-rainbow
GitHub Stars
10
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass