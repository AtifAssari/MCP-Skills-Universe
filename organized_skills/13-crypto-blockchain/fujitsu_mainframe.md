---
rating: ⭐⭐⭐
title: fujitsu-mainframe
url: https://skills.sh/dauquangthanh/hanoi-rainbow/fujitsu-mainframe
---

# fujitsu-mainframe

skills/dauquangthanh/hanoi-rainbow/fujitsu-mainframe
fujitsu-mainframe
Installation
$ npx skills add https://github.com/dauquangthanh/hanoi-rainbow --skill fujitsu-mainframe
SKILL.md
Fujitsu Mainframe Analyzer

Analyze and migrate Fujitsu mainframe systems (FACOM, BS2000/OSD, OSIV, NetCOBOL, PowerCOBOL, Fujitsu JCL, SYMFOWARE) to modern Java/cloud platforms.

Core Capabilities
1. Fujitsu COBOL Analysis

Extract NetCOBOL/PowerCOBOL programs, Fujitsu-specific verbs, proprietary file organizations (SAM/PAM/ISAM), SYMFOWARE embedded SQL, screen handling (ACCEPT/DISPLAY with CRT STATUS).

2. Fujitsu JCL Analysis

Parse JOB statements, STEP definitions, ASSIGN/FILEDEF statements, conditional execution, cataloged procedures, resource allocation.

3. BS2000/OSD System Analysis

Analyze ENTER statements, system commands, file handling (PAM, SAM, ISAM), job variables, SDF processing.

4. SYMFOWARE Database Migration

Extract embedded SQL, schemas, stored procedures, transactions. Migrate to PostgreSQL, Oracle, or SQL Server.

5. Migration to Modern Platforms

Generate Spring Boot microservices, REST APIs, cloud-native apps (AWS, Azure, GCP), containerized deployments (Docker, Kubernetes), CI/CD pipelines.

Workflow
Step 1: Discover Assets
find . -name "*.cbl" -o -name "*.CBL" -o -name "*.cob"  # COBOL
find . -name "*.ncb" -o -name "*.NCB"  # NetCOBOL
find . -name "*.fjcl" -o -name "*.jcl"  # JCL
find . -name "*.cpy" -o -name "*.CPY"  # Copybooks
find . -name "*.sdf" -o -name "*.SDF"  # SDF files

Step 2: Analyze Structure

Extract divisions, data structures, file definitions, screen definitions, embedded SQL, Fujitsu-specific extensions. Key features:

File organization: SEQUENTIAL, RELATIVE, INDEXED
Screen handling: CRT STATUS, screen control
Database: SYMFOWARE SQL
Fujitsu verbs: ACCEPT OMITTED, INSPECT extensions
Error handling: FILE STATUS, DECLARATIVES
Step 3: Map Dependencies

Build graphs: CALL hierarchies, copybook usage, file dependencies (FACOM), database access (SYMFOWARE), JCL sequences, screen definitions.

Step 4: Create Migration Strategy

Document architecture, Fujitsu-specific features, Java/cloud design, data migration, roadmap. Load references/migration-strategy.md for detailed framework.

Fujitsu-Specific Features
NetCOBOL Extensions
Windowing, GUI support (PowerCOBOL)
Enhanced ACCEPT/DISPLAY with positioning
Object-oriented: CLASS definitions
Extended exception handling
SYMFOWARE Database
Embedded SQL: SELECT, INSERT, UPDATE, DELETE
Cursors: DECLARE, OPEN, FETCH, CLOSE
Transactions: COMMIT, ROLLBACK
Migration: SYMFOWARE → PostgreSQL (cost), Oracle (enterprise), SQL Server
File Systems
Type	Description	Java Equivalent
SAM	Sequential	BufferedReader/Writer
PAM	Partitioned	File directory
ISAM	Indexed	Database with index
GDG	Versioned	Timestamp naming
Quick Patterns
COBOL → Java Spring Boot

Load references/migration-patterns.md for detailed examples. Quick overview:

Fujitsu COBOL:

SELECT EMPFILE ASSIGN TO "EMPDATA"
    ORGANIZATION IS INDEXED
    ACCESS MODE IS RANDOM
    RECORD KEY IS EMP-ID


Java JPA:

@Entity
@Table(name = "employees")
public class Employee {
    @Id
    private Integer empId;
    private String empName;
    private BigDecimal empSalary;
}

JCL → Shell + Kubernetes

Fujitsu JCL:

//STEP010  EXEC PGM=VALIDATE
//STEP020  EXEC PGM=PROCESS,COND=(0,EQ,STEP010)


Shell:

./validate && ./process


Load references/migration-patterns.md for Kubernetes CronJob examples.

Data Type Mappings

Load references/data-mappings.md for comprehensive tables. Critical mappings:

Fujitsu COBOL	Java	Notes
PIC 9(n)	int, long, BigInteger	Size dependent
PIC S9(n)V9(m)	BigDecimal	ALWAYS for decimals
PIC X(n)	String	Alphanumeric
COMP-3	BigDecimal	NEVER float/double
OCCURS n	List<T>	Prefer List over array
SYMFOWARE	PostgreSQL
CHAR(n)	CHAR(n)
VARCHAR(n)	VARCHAR(n)
DECIMAL(p,s)	NUMERIC(p,s)
TIMESTAMP	TIMESTAMP WITH TIME ZONE
BLOB	BYTEA
CLOB	TEXT
Migration Strategies
Strangler Fig Pattern (Recommended)

Gradually replace functionality. Lower risk, learn and adjust. Load references/migration-strategy.md for detailed steps.

Big Bang

Complete rewrite, single cutover. Higher risk, clean architecture. For smaller systems.

Hybrid

Core services modernized first, periphery later. Balanced risk/reward.

Output Requirements
Analysis Report Structure
Executive Summary - Overview, business impact, recommendation
Current State - Inventory, architecture, technology, dependencies
Fujitsu Features - NetCOBOL/PowerCOBOL, SYMFOWARE, file systems, screens, JCL
Target Design - Architecture, tech stack, microservices, data model, APIs
Migration Plan - Approach, timeline, resources, risks, costs
Technical Appendix - Code samples, mappings, utilities, testing

Load references/migration-strategy.md for complete frameworks and templates.

Critical Best Practices
ALWAYS use BigDecimal for COMP-3 and decimals (NEVER float/double)
Preserve business logic - understand before changing
Test with production data - validate conversions
Document Fujitsu extensions - proprietary features need special handling
Plan parallel run - compare outputs before cutover
Automate testing - regression suite for validation
Monitor everything - logging, metrics, alerts
Security first - authentication, authorization, encryption
Common Challenges & Solutions

Fujitsu-Specific Features → Custom adapters, equivalent libraries, re-implementation Screen Handling → User requirements gathering, modern UX design File Processing → ETL tools, Spring Batch Performance → Caching (Redis), async processing, DB optimization Transactions → Spring @Transactional, Saga pattern

Reference Files

When detailed information needed:

references/migration-patterns.md - Complete code examples for all migration patterns
references/data-mappings.md - Comprehensive type mappings, REDEFINES, dates, best practices
references/migration-strategy.md - Full framework: assessment, design, testing, cutover, costs

Load these files for in-depth guidance on specific topics.

Weekly Installs
12
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