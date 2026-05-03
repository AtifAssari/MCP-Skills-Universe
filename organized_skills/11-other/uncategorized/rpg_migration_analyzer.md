---
rating: ⭐⭐
title: rpg-migration-analyzer
url: https://skills.sh/dauquangthanh/hanoi-rainbow/rpg-migration-analyzer
---

# rpg-migration-analyzer

skills/dauquangthanh/hanoi-rainbow/rpg-migration-analyzer
rpg-migration-analyzer
Installation
$ npx skills add https://github.com/dauquangthanh/hanoi-rainbow --skill rpg-migration-analyzer
SKILL.md
RPG Migration Analyzer

Analyzes legacy RPG programs (RPG III/IV/ILE) from AS/400 and IBM i systems for migration to modern Java applications, extracting business logic, data structures, file operations, and generating actionable migration strategies.

Overview

This skill provides comprehensive analysis and migration planning for RPG (Report Program Generator) applications. It extracts program specifications, converts RPG data types to Java equivalents, maps file operations to modern database access patterns, and generates implementation-ready Java code structures.

Key Migration Focus: RPG to Java with proper handling of packed decimals (BigDecimal), data structures (POJOs), file operations (JPA/JDBC), indicators (boolean variables), and business logic preservation.

When to Use This Skill

Use this skill when:

Analyzing RPG source files (.rpg, .rpgle, .RPGLE) for modernization
Planning migration from AS/400 or IBM i systems to Java
Converting RPG data structures (D-specs) to Java classes
Mapping RPG file operations (F-specs) to database access patterns
Understanding RPG program dependencies and call chains
Generating Java code equivalents from RPG business logic
Estimating complexity and effort for RPG migration projects
Creating migration documentation and strategy reports
Modernizing legacy mainframe applications to microservices
User mentions: RPG analysis, AS/400 migration, IBM i modernization, Report Program Generator, packed decimal conversion
Core Capabilities
1. Program Analysis

Extract and analyze RPG program components:

Specification types: H-spec (header/control), F-spec (file definitions), D-spec (data definitions), C-spec (calculation/logic), P-spec (procedures)
Data structures: D-specs with nested structures, arrays (DIM), external references (EXTNAME), qualifiers (LIKEDS, QUALIFIED)
File definitions: Physical files, logical files, display files (WORKSTN), printer files
Business logic: Calculation specifications, control structures (IF/ELSE/DO/FOR), expressions (EVAL)
Indicators: Legacy indicators (*IN01-*IN99), built-in indicators (*INLR,*INOF)
Built-in functions: String functions (%SUBST, %TRIM, %SCAN), date functions (%DATE, %DAYS), math functions (%DEC, %INT), file status (%EOF, %FOUND, %ERROR)
Error handling: %ERROR, %STATUS, ON-ERROR blocks
2. Data Structure Mapping

Convert RPG data definitions to Java equivalents:

D-spec conversion: Data structure definitions to Java classes (POJOs)
Data type mapping:
Packed decimal (P) → BigDecimal (preserve precision)
Zoned decimal (S) → BigDecimal (decimal with sign)
Character (A) → String
Date (D) → LocalDate
Time (T) → LocalTime
Timestamp (Z) → LocalDateTime
Indicator (N) → boolean
Binary integer (I) → int or long
Arrays (DIM): Convert to Java List<T> or arrays T[]
Nested data structures: Convert LIKEDS to nested Java classes
External data structures (EXTNAME): Generate JPA entities from database table definitions
Initialization (INZ): Map to Java field initializers or constructors
3. File Operations

Parse and convert RPG file I/O to modern database access:

File types: Physical files (DISK), logical files (keyed access), display files (WORKSTN), printer files (PRINTER)
Access methods: Sequential (full read), keyed (direct access by key), arrival sequence
I/O operations:
READ/READE → JPA query methods, JDBC ResultSet iteration
WRITE → JPA persist(), JDBC INSERT
UPDATE → JPA merge(), JDBC UPDATE
DELETE → JPA remove(), JDBC DELETE
CHAIN → JPA findById(), Optional pattern
SETLL/READE loop → JPA findBy...() queries with ordering
File status: %EOF (end of file), %FOUND (record found), %ERROR (I/O error) → Java exceptions or Optional
Transaction boundaries: Identify commit boundaries (COMMIT operation code)
4. Java Migration Strategy

Generate modern Java implementation patterns:

POJOs: Plain Old Java Objects from D-spec data structures
JPA Entities: @Entity annotations for database tables (from EXTNAME files)
Repository pattern: Spring Data JPA repositories for file operations
Service methods: Business logic from procedures and subroutines
Bean Validation: @NotNull, @Size, @DecimalMin/Max from RPG field validations
Exception handling: Convert %ERROR patterns to try-catch blocks with custom exceptions
Collections: Java Collections API (List, Map, Set) from RPG arrays and data structures
DTOs: Data Transfer Objects for service boundaries
Transaction management: @Transactional annotations for commit boundaries
5. Dependency Analysis

Map program relationships and external dependencies:

Program calls: CALLB (bound procedure calls), CALLP (prototyped procedure calls)
Service programs: BNDDIR (binding directories), *SRVPGM objects
File dependencies: All physical/logical files accessed by the program
Database tables: DB2 for i tables referenced (EXTNAME)
/COPY members: Include files, copy source members, prototypes
Call chains: Identify calling programs and called programs
Shared data areas: *DTAARA usage
Message queues: QMHSNDPM (send program message)
Instructions

Follow these steps to analyze and migrate RPG programs to Java:

Step 1: Locate RPG Source Files

Find RPG source files (.rpg, .rpgle, .RPGLE extensions for RPG III/IV/ILE free-format).

find . -name "*.rpg" -o -name "*.rpgle" -o -name "*.RPGLE"

Step 2: Analyze Program Structure

Extract specifications (H, F, D, C, P), data structures, file definitions, procedures, and dependencies.

Automation: Run scripts/extract-structure.py for automated extraction.

Step 3: Map Data Types

Convert RPG to Java types - CRITICAL: Always use BigDecimal for packed/zoned decimals (never float/double).

RPG Type	Java Type	Key Notes
nP m (packed)	BigDecimal	MUST preserve precision
nS m (zoned)	BigDecimal	Decimal with sign
A (char)	String	Character data
D/T/Z (date/time)	LocalDate/LocalTime/LocalDateTime	Date fields
N (indicator)	boolean	True/False flags
I (integer)	int or long	Binary integer
DIM(n) (array)	List<T> or T[]	Arrays
Step 4: Convert Code Patterns

Transform RPG operations to Java - key conversions:

Calculations: EVAL expressions → BigDecimal arithmetic methods
File I/O: CHAIN → findById() with Optional, READ → query methods
Arrays: Adjust 1-based (RPG) to 0-based (Java) indexing
Strings: %SUBST(1-based) → substring(0-based)
Indicators: *IN01 → named boolean variables

See pseudocode-rpg-rules.md for comprehensive conversion patterns.

Step 5: Generate Java Implementation

Create:

POJOs from D-spec data structures (scripts/generate-java-classes.py)
JPA entities for database tables
Repository interfaces (Spring Data JPA)
Service methods for business logic
Exception handling and validation
Step 6: Analyze Dependencies

Map program calls (CALLB/CALLP), file dependencies, /COPY members, service programs.

Automation: Run scripts/analyze-dependencies.sh or .ps1

Step 7: Create Migration Report

Generate documentation with program overview, dependencies, data mappings, Java design, and complexity estimate.

Template: Use assets/migration-report-template.md

Step 8: Validate and Test

Verify: BigDecimal usage, index adjustments, transaction boundaries, error handling, unit tests with AS/400 data samples.

Quick Reference
Critical Migration Rules
ALWAYS use BigDecimal for RPG packed (P) and zoned (S) decimals - never float/double
Adjust indexing: RPG uses 1-based arrays/strings, Java uses 0-based
Replace indicators: Convert *IN01-*IN99 to descriptive boolean variables
File operations: CHAIN → findById(), READ → query methods with Optional
String functions: %SUBST(1:10) → substring(0, 10) - adjust positions
Date operations: RPG date functions → LocalDate/LocalTime API
Transactions: Identify COMMIT operations → @Transactional annotations
Error handling: %ERROR/%STATUS → try-catch with custom exceptions
Example: Data Structure to Java Class

RPG D-spec:

D Employee   DS
D   EmpId             6  0
D   EmpName          30  A
D   Salary           63  2P


Java POJO:

public class Employee {
    private int empId;
    private String empName;
    private BigDecimal salary;  // 6 digits, 2 decimals
    // getters/setters
}

Example: File Operation Conversion

RPG CHAIN:

C     custId  CHAIN  CUSTFILE
C             IF     %FOUND(CUSTFILE)


Java with JPA:

customerRepository.findById(custId).ifPresent(customer -> {
    // process customer
});

// Service usage
public class CustomerService {
    @Autowired
    private CustomerRepository customerRepository;

    public Optional<Customer> findCustomer(Integer custId) {
        return customerRepository.findById(custId);
    }
}

Edge Cases
Case 1: Packed Decimal Precision

Problem: Using double/float causes precision errors. Solution: Always use BigDecimal from String literals: new BigDecimal("123.45")

Case 2: Array Index Shift

Problem: RPG 1-based, Java 0-based. Solution: Adjust all array/string index references. Test thoroughly.

Case 3: External Data Structures

Problem: EXTNAME without DDL source. Solution: Use DSPFFD command, query DB2 SYSTABLES/SYSCOLUMNS, or create entities from runtime data.

Case 4: Legacy Indicators

Problem: *IN01-*IN99 for control flow. Solution: Replace with descriptive booleans: boolean invalidAmount = false;

Case 5: Date Century Handling

Problem: 2-digit years (Y2K). Solution: Use 4-digit LocalDate, apply century window logic, document assumptions.

Guidelines
BigDecimal mandatory: Never float/double for packed/zoned decimals
Named booleans: Replace *IN01-99 with descriptive names
Database access: Map file I/O to JPA/JDBC operations
JPA entities: Create from EXTNAME physical file definitions
Exception handling: Convert %ERROR/%FOUND to exceptions/Optional
Test with AS/400 data: Validate with actual legacy system data
Transactions: Identify COMMIT operations → @Transactional
Document rules: Extract and document implicit business logic
Character encoding: Verify EBCDIC → Unicode conversions
Batch processing: Convert batch jobs to Spring Batch framework
Error Handling
Type 1: File I/O Errors

Detection: %ERROR or %STATUS checks. Handling: Use try-catch with custom exceptions (CustomerNotFoundException, DataAccessException)

Type 2: Arithmetic Overflow

Detection: Insufficient field size. Handling: BigDecimal with appropriate scale/precision, catch ArithmeticException

Type 3: Missing Dependencies

Detection: Missing /COPY members. Handling: Track all includes, create shared interfaces, use Maven/Gradle dependencies

Additional Resources

See detailed documentation in the references/ directory:

RPG Translation Rules (Organized by Topic)

The RPG translation rules are organized into focused, topic-specific files for easier navigation:

pseudocode-rpg-rules.md - Master index with quick start guide and file navigation
pseudocode-rpg-core-rules.md - Foundation: specs, data types, basic operations, file I/O
pseudocode-rpg-functions.md - Built-in functions (BIFs): string, date/time, math, array functions
pseudocode-rpg-data-structures.md - Data structure patterns: QUALIFIED, LIKEDS, OVERLAY, I/O specs
pseudocode-rpg-patterns.md - Common idioms, translation patterns, pitfalls, critical rules
pseudocode-rpg-advanced.md - ILE RPG, embedded SQL, web services, IFS, XML/JSON, threading
pseudocode-rpg-migration-guide.md - Migration workflow, best practices, refactoring strategies
Other Reference Documentation
pseudocode-common-rules.md - General pseudocode syntax and conventions
testing-strategy.md - Testing approach for RPG to Java migration validation
transaction-handling.md - AS/400 transaction patterns to Java transaction management
performance-patterns.md - Performance optimization patterns for migrated code
messaging-integration.md - Message queue and integration patterns for IBM i systems
Scripts

Python and shell scripts for automated analysis in scripts/:

analyze-dependencies.sh/ps1 - Scans RPG source for CALLB, CALLP, /COPY; generates dependency graph
extract-structure.py - Parses RPG specs (H, F, D, C, P); outputs structured JSON
generate-java-classes.py - Creates Java POJOs from RPG data structures with proper types
estimate-complexity.py - Calculates migration complexity score and effort estimate
Templates
migration-report-template.md - Standard format for migration analysis reports
java-class-template.java - Template for generated Java classes

analyze-dependencies.sh / .ps1

Scans RPG source files for CALLB, CALLP, /COPY references
Generates dependency graph in JSON format
Identifies circular dependencies

Usage:

./scripts/analyze-dependencies.sh /path/to/rpg/source


extract-structure.py

Extracts program structure (H/F/D/C/P specs)
Lists all variables, data structures, files
Identifies subroutines and procedures
Outputs JSON structure file

Usage:

python scripts/extract-structure.py PROGRAM.rpgle --output structure.json


generate-java-classes.py

Generates Java POJO classes from RPG data structures
Creates proper field types (BigDecimal for packed decimals)
Adds getters, setters, constructors
Generates Bean Validation annotations

Usage:

python scripts/generate-java-classes.py structure.json --output-dir ./src/main/java


estimate-complexity.py

Calculates migration complexity score
Analyzes LOC, dependencies, file operations
Provides effort estimate (hours/days)
Generates priority ranking

Usage:

python scripts/estimate-complexity.py structure.json --report complexity-report.md

Templates

Use the migration report template for consistent documentation:

migration-report-template.md - Standard format for migration analysis reports
java-class-template.java - Template for generated Java classes with proper structure
Integration with Development Tools

This skill integrates with various development and analysis tools:

IBM i / AS/400 Tools
Source Entry Utility (SEU): Extract source code from AS/400
Programming Development Manager (PDM): Access member lists and source files
WRKMBRPDM: Work with source members
DSPFFD: Display file field descriptions for database structure analysis
DSPPGMREF: Display program references and dependencies
Database Tools
DB2 for i: Query system catalogs (SYSTABLES, SYSCOLUMNS) for metadata
IBM Data Studio: Visual database design and SQL development
DBeaver: Universal database tool with DB2 support
Modern Development Environment
IntelliJ IDEA: Java development with Spring Boot support
Eclipse: Java IDE with JPA tooling
VS Code: Lightweight editor with Java extensions
Git: Version control for both legacy source and new Java code
Migration Support Tools
Spring Initializr: Bootstrap Spring Boot projects
JPA Buddy: IntelliJ plugin for JPA entity generation
Liquibase/Flyway: Database migration version control
Maven/Gradle: Build automation and dependency management
Testing and Validation
JUnit 5: Unit testing framework
Spring Boot Test: Integration testing support
Mockito: Mocking framework for unit tests
TestContainers: Database integration testing with containers
Weekly Installs
24
Repository
dauquangthanh/h…-rainbow
GitHub Stars
10
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass