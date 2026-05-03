---
title: authoring-dags
url: https://skills.sh/astronomer/agents/authoring-dags
---

# authoring-dags

skills/astronomer/agents/authoring-dags
authoring-dags
Installation
$ npx skills add https://github.com/astronomer/agents --skill authoring-dags
Summary

Guided workflow for creating Apache Airflow DAGs with validation and testing integration.

Structured six-phase approach: discover environment and existing patterns, plan DAG structure, implement following best practices, validate with af CLI commands, test with user consent, and iterate on fixes
CLI commands for discovery (af config connections, af config providers, af dags list) and validation (af dags errors, af dags get, af dags explore) provide immediate feedback on DAG correctness
Integrates with testing-dags skill for comprehensive test-debug-fix-retest workflows and supports Astro-specific features like astro dev parse and DAG-only deploys
References external best practices documentation covering correct patterns, anti-patterns, and Airflow 3-specific behavior
SKILL.md
Contains Hooks

This skill uses Claude hooks which can execute code automatically in response to events. Review carefully before installing.

DAG Authoring Skill

This skill guides you through creating and validating Airflow DAGs using best practices and af CLI commands.

For testing and debugging DAGs, see the testing-dags skill which covers the full test -> debug -> fix -> retest workflow.

Running the CLI

These commands assume af is on PATH. Run via astro otto to get it automatically, or install standalone with uv tool install astro-airflow-mcp.

Workflow Overview
+-----------------------------------------+
| 1. DISCOVER                             |
|    Understand codebase & environment    |
+-----------------------------------------+
                 |
+-----------------------------------------+
| 2. PLAN                                 |
|    Propose structure, get approval      |
+-----------------------------------------+
                 |
+-----------------------------------------+
| 3. IMPLEMENT                            |
|    Write DAG following patterns         |
+-----------------------------------------+
                 |
+-----------------------------------------+
| 4. VALIDATE                             |
|    Check import errors, warnings        |
+-----------------------------------------+
                 |
+-----------------------------------------+
| 5. TEST (with user consent)             |
|    Trigger, monitor, check logs         |
+-----------------------------------------+
                 |
+-----------------------------------------+
| 6. ITERATE                              |
|    Fix issues, re-validate              |
+-----------------------------------------+

Phase 1: Discover

Before writing code, understand the context.

Explore the Codebase

Use file tools to find existing patterns:

Glob for **/dags/**/*.py to find existing DAGs
Read similar DAGs to understand conventions
Check requirements.txt for available packages
Query the Airflow Environment

Use af CLI commands to understand what's available:

Command	Purpose
af config connections	What external systems are configured
af config variables	What configuration values exist
af config providers	What operator packages are installed
af config version	Version constraints and features
af dags list	Existing DAGs and naming conventions
af config pools	Resource pools for concurrency

Example discovery questions:

"Is there a Snowflake connection?" -> af config connections
"What Airflow version?" -> af config version
"Are S3 operators available?" -> af config providers
Phase 2: Plan

Based on discovery, propose:

DAG structure - Tasks, dependencies, schedule
Operators to use - Based on available providers
Connections needed - Existing or to be created
Variables needed - Existing or to be created
Packages needed - Additions to requirements.txt

Get user approval before implementing.

Phase 3: Implement

Write the DAG following best practices (see below). Key steps:

Create DAG file in appropriate location
Update requirements.txt if needed
Save the file
Phase 4: Validate

Use af CLI as a feedback loop to validate your DAG.

Step 1: Check Import Errors

After saving, check for parse errors (Airflow will have already parsed the file):

af dags errors

If your file appears -> fix and retry
If no errors -> continue

Common causes: missing imports, syntax errors, missing packages.

Step 2: Verify DAG Exists
af dags get <dag_id>


Check: DAG exists, schedule correct, tags set, paused status.

Step 3: Check Warnings
af dags warnings


Look for deprecation warnings or configuration issues.

Step 4: Explore DAG Structure
af dags explore <dag_id>


Returns in one call: metadata, tasks, dependencies, source code.

On Astro

If you're running on Astro, you can also validate locally before deploying:

Parse check: Run astro dev parse to catch import errors and DAG-level issues without starting a full Airflow environment
DAG-only deploy: Once validated, use astro deploy --dags for fast DAG-only deploys that skip the Docker image build — ideal for iterating on DAG code
Phase 5: Test

See the testing-dags skill for comprehensive testing guidance.

Once validation passes, test the DAG using the workflow in the testing-dags skill:

Get user consent -- Always ask before triggering
Trigger and wait -- af runs trigger-wait <dag_id> --timeout 300
Analyze results -- Check success/failure status
Debug if needed -- af runs diagnose <dag_id> <run_id> and af tasks logs <dag_id> <run_id> <task_id>
Quick Test (Minimal)
# Ask user first, then:
af runs trigger-wait <dag_id> --timeout 300


For the full test -> debug -> fix -> retest loop, see testing-dags.

Phase 6: Iterate

If issues found:

Fix the code
Check for import errors: af dags errors
Re-validate (Phase 4)
Re-test using the testing-dags skill workflow (Phase 5)
CLI Quick Reference
Phase	Command	Purpose
Discover	af config connections	Available connections
Discover	af config variables	Configuration values
Discover	af config providers	Installed operators
Discover	af config version	Version info
Validate	af dags errors	Parse errors (check first!)
Validate	af dags get <dag_id>	Verify DAG config
Validate	af dags warnings	Configuration warnings
Validate	af dags explore <dag_id>	Full DAG inspection

Testing commands -- See the testing-dags skill for af runs trigger-wait, af runs diagnose, af tasks logs, etc.

Best Practices & Anti-Patterns

For code patterns and anti-patterns, see reference/best-practices.md.

Read this reference when writing new DAGs or reviewing existing ones. It covers what patterns are correct (including Airflow 3-specific behavior) and what to avoid.

Related Skills
testing-dags: For testing DAGs, debugging failures, and the test -> fix -> retest loop
debugging-dags: For troubleshooting failed DAGs
deploying-airflow: For deploying DAGs to production (Astro or open-source)
migrating-airflow-2-to-3: For migrating DAGs to Airflow 3
Weekly Installs
665
Repository
astronomer/agents
GitHub Stars
354
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass