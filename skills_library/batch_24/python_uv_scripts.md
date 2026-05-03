---
title: python-uv-scripts
url: https://skills.sh/basher83/lunar-claude/python-uv-scripts
---

# python-uv-scripts

skills/basher83/lunar-claude/python-uv-scripts
python-uv-scripts
Installation
$ npx skills add https://github.com/basher83/lunar-claude --skill python-uv-scripts
SKILL.md
Python Single-File Scripts with uv

Expert guidance for creating production-ready, self-contained Python scripts using uv's inline dependency management (PEP 723).

Quick Start
Create Your First uv Script
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx>=0.27.0",
#   "rich>=13.0.0",
# ]
# ///

import httpx
from rich import print

response = httpx.get("https://api.github.com")
print(f"[green]Status: {response.status_code}[/green]")


Make it executable:

chmod +x script.py
./script.py  # uv automatically installs dependencies

Convert Existing Script
# Add inline metadata to existing script
./tools/convert_to_uv.py existing_script.py

# Validate PEP 723 metadata
./tools/validate_script.py script.py

Core Concepts
What is PEP 723?

PEP 723 defines inline script metadata for Python files:

# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "package>=1.0.0",
# ]
# ///


Benefits:

✅ Dependencies live with the code
✅ No separate requirements.txt
✅ Reproducible execution
✅ Version constraints included
✅ Self-documenting
uv Script Execution Modes

Mode 1: Inline Dependencies (Recommended for utilities)

#!/usr/bin/env -S uv run --script
# /// script
# dependencies = ["httpx"]
# ///


Mode 2: Project Mode (For larger scripts)

uv run script.py  # Uses pyproject.toml

Mode 3: No Dependencies
#!/usr/bin/env -S uv run
# Standard library only

Critical Anti-Patterns: What NOT to Do
❌ NEVER Use [tool.uv.metadata]

WRONG - This will cause errors:

# /// script
# requires-python = ">=3.11"
# [tool.uv.metadata]        # ❌ THIS DOES NOT WORK
# purpose = "testing"
# ///


Error:

error: TOML parse error at line 3, column 7
unknown field `metadata`


Why: [tool.uv.metadata] is not part of PEP 723 and is not supported by uv.

CORRECT - Use Python docstrings for metadata:

# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Purpose: Testing automation
Team: DevOps
Author: team@example.com
"""


Valid tool.uv fields (if needed):

# /// script
# requires-python = ">=3.11"
# dependencies = []
# [tool.uv]
# exclude-newer = "2025-01-01T00:00:00Z"  # For reproducibility
# ///

Real-World Examples from This Repository
Example 1: Cluster Health Checker

See examples/03-production-ready/check_cluster_health_enhanced.py

Current version (basic):

#!/usr/bin/env python3
import subprocess
# Manual dependency installation required


Enhanced with uv (production-ready):

#!/usr/bin/env -S uv run --script --quiet
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "rich>=13.0.0",
#   "typer>=0.9.0",
# ]
# ///
"""
Purpose: Cluster health monitoring
Team: Infrastructure
"""

import typer
from rich.console import Console
from rich.table import Table

Example 2: CEPH Health Monitor

See examples/03-production-ready/ceph_health.py

Pattern: JSON API interaction with structured output

Best Practices from This Repository
1. Security Patterns

See reference/security-patterns.md for complete security guide including:

Secrets management (environment variables, keyring, Infisical)
Input validation
Dependency security
File operations security
Command execution security
2. Version Pinning Strategy

Following this repository's approach (from pyproject.toml):

# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx>=0.27.0",      # Minimum version for compatibility
#   "rich>=13.0.0",       # Known good version
#   "ansible>=11.1.0",    # Match project requirements
# ]
# ///


Pinning levels:

>=X.Y.Z - Minimum version (most flexible)
~=X.Y.Z - Compatible release (patch updates only)
==X.Y.Z - Exact version (most strict)

See reference/dependency-management.md.

3. Team Standards

File naming:

check_cluster_health.py    # ✅ Descriptive, snake_case
validate_template.py       # ✅ Action-oriented
cluster.py                 # ❌ Too generic


Shebang pattern:

#!/usr/bin/env -S uv run --script --quiet
# --quiet suppresses uv's own output


Documentation template:

#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Check Proxmox cluster health

Purpose: cluster-monitoring
Team: infrastructure
Author: devops@spaceships.work

Usage:
    python check_cluster_health.py [--node NODE] [--json]

Examples:
    python check_cluster_health.py --node foxtrot
    python check_cluster_health.py --json
"""

4. Error Handling Patterns

Following Ansible best practices from this repository:

import sys
import subprocess

def run_command(cmd: str) -> str:
    """Execute command with proper error handling"""
    try:
        result = subprocess.run(
            cmd.split(),
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error: Command failed: {cmd}", file=sys.stderr)
        print(f"  {e.stderr}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print(f"Error: Command not found: {cmd.split()[0]}", file=sys.stderr)
        sys.exit(1)


See patterns/error-handling.md.

5. Testing Patterns

Inline testing (for simple scripts):

#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///

def validate_ip(ip: str) -> bool:
    """Validate IP address format"""
    import re
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    return bool(re.match(pattern, ip))

# Inline tests
if __name__ == "__main__":
    import sys

    # Run tests if --test flag provided
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        assert validate_ip("192.168.1.1") == True
        assert validate_ip("256.1.1.1") == False
        print("All tests passed!")
        sys.exit(0)

    # Normal execution
    print(validate_ip("192.168.3.5"))


See workflows/testing-strategies.md.

When NOT to Use Single-File Scripts

See anti-patterns/when-not-to-use.md for details.

Use a proper project instead when:

❌ Script exceeds 500 lines
❌ Multiple modules/files needed
❌ Complex configuration management
❌ Requires packaging/distribution
❌ Shared library code across multiple scripts
❌ Web applications or long-running services

Example - Too Complex for Single File:

# This should be a uv project, not a script:
# - 15+ dependencies
# - Database models
# - API routes
# - Background workers
# - Configuration management
# - Multiple environments

Common Patterns

See pattern guides for complete examples:

CLI Applications - Typer, Click, argparse patterns
API Clients - httpx, requests, authentication
Data Processing - Polars, pandas, analysis
System Automation - psutil, subprocess, system admin
CI/CD Integration
GitHub Actions
name: Run Health Checks

on:
  schedule:
    - cron: '0 */6 * * *'  # Every 6 hours

jobs:
  health-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install uv
        uses: astral-sh/setup-uv@v3

      - name: Check cluster health
        run: |
          uv run --script tools/check_cluster_health.py --json
        env:
          PROXMOX_TOKEN: ${{ secrets.PROXMOX_TOKEN }}

GitLab CI
cluster-health:
  image: ghcr.io/astral-sh/uv:python3.11-bookworm-slim
  script:
    - uv run --script tools/check_cluster_health.py
  only:
    - schedules


See workflows/ci-cd-integration.md.

Tools Available
Script Validation
# Validate PEP 723 metadata
./tools/validate_script.py script.py

# Output:
# ✓ Valid PEP 723 metadata
# ✓ Python version specified
# ✓ Dependencies properly formatted

Script Conversion
# Convert requirements.txt-based script to uv
./tools/convert_to_uv.py old_script.py

# Creates:
# - old_script_uv.py with inline dependencies
# - Preserves original script

Progressive Disclosure

For deeper knowledge:

Reference Documentation
PEP 723 Specification - Complete inline metadata spec
Dependency Management - Version pinning strategies
Security Patterns - Secrets, validation, input sanitization
Pattern Guides
CLI Applications - Typer, Click, argparse patterns
API Clients - httpx, requests, authentication
Data Processing - Polars, pandas, analysis
System Automation - psutil, subprocess, system admin
Error Handling - Exception handling, logging

Note: See Common Patterns section above for quick access to these guides.

Working Examples
NetBox API Client - Production-ready API client with Infisical, validation, error handling, and Rich output
Cluster Health Checker - Production-ready monitoring script with Typer, Rich, and JSON output
Anti-Patterns
When NOT to Use - Signs you need a proper project
Common Mistakes - Pitfalls and how to avoid them
Workflows
Team Adoption - Rolling out uv scripts across teams
CI/CD Integration - GitHub Actions, GitLab CI
Testing Strategies - Inline tests, pytest integration
Related Skills
Ansible Best Practices - Many Ansible modules could be standalone uv scripts
Proxmox Infrastructure - Validation tools use this pattern
NetBox + PowerDNS Integration - API interaction scripts
Quick Reference
Shebang Options
# Standard script execution
#!/usr/bin/env -S uv run --script

# Quiet mode (suppress uv output)
#!/usr/bin/env -S uv run --script --quiet

# With Python version
#!/usr/bin/env -S uv run --script --python 3.11

Common Dependencies
# CLI applications
"typer>=0.9.0"        # Modern CLI framework
"click>=8.0.0"        # Alternative CLI framework
"rich>=13.0.0"        # Rich text and formatting

# API clients
"httpx>=0.27.0"       # Modern async HTTP client
"requests>=2.31.0"    # Traditional HTTP client

# Data processing
"polars>=0.20.0"      # Fast dataframe library
"pandas>=2.0.0"       # Traditional dataframe library

# Infrastructure
"ansible>=11.1.0"     # Automation (from this repo)
"infisical-python>=2.3.3"  # Secrets (from this repo)

# System automation
"psutil>=5.9.0"       # System monitoring

Metadata Template
#!/usr/bin/env -S uv run --script --quiet
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   # Add dependencies here
# ]
# ///
"""
One-line description

Purpose: describe-purpose
Team: team-name
Author: email@example.com

Usage:
    python script.py [OPTIONS]

Examples:
    python script.py --help
"""

Best Practices Summary
Always specify Python version - requires-python = ">=3.11"
Pin dependencies appropriately - Use >=X.Y.Z for utilities
Add metadata in docstrings - Put team info, purpose, and author in module docstring
Include comprehensive docstrings - Document purpose, usage, and examples
Handle errors gracefully - Use try/except with clear messages
Validate inputs - Check arguments before processing
Use quiet mode - --quiet flag for production scripts
Keep it focused - Single file, single purpose
Test inline - Add --test flag for simple validation
Secure secrets - Never hardcode, use env vars or keyring
Weekly Installs
8
Repository
basher83/lunar-claude
GitHub Stars
18
First Seen
Feb 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn