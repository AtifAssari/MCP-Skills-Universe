---
title: cloud-migration-planning
url: https://skills.sh/aj-geddes/useful-ai-prompts/cloud-migration-planning
---

# cloud-migration-planning

skills/aj-geddes/useful-ai-prompts/cloud-migration-planning
cloud-migration-planning
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill cloud-migration-planning
SKILL.md
Cloud Migration Planning
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Cloud migration planning involves assessing current infrastructure, designing migration strategies, executing migrations with minimal downtime, and validating outcomes. Support lift-and-shift, replatforming, and refactoring approaches for smooth cloud adoption.

When to Use
Moving from on-premises to cloud
Cloud platform consolidation
Legacy system modernization
Reducing data center costs
Improving scalability and availability
Meeting compliance requirements
Disaster recovery enhancement
Technology refresh initiatives
Quick Start

Minimal working example:

# Cloud migration assessment tool
from enum import Enum
from typing import Dict, List, Tuple
from dataclasses import dataclass

class MigrationStrategy(Enum):
    LIFT_AND_SHIFT = "lift_and_shift"  # Rehost
    REPLATFORM = "replatform"          # Rehost with optimizations
    REFACTOR = "refactor"              # Rebuild for cloud
    REPURCHASE = "repurchase"          # Switch to SaaS
    RETIRE = "retire"                  # Decommission

class ApplicationComplexity(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

@dataclass
class ApplicationAssessment:
    name: str
    complexity: ApplicationComplexity
    dependencies: List[str]
    estimated_effort: int  # days
    business_criticality: int  # 1-10
    current_costs: float  # annual
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Migration Assessment and Planning	Migration Assessment and Planning
Database Migration Strategies	Database Migration Strategies
Terraform Migration Infrastructure	Terraform Migration Infrastructure
Cutover Validation Checklist	Cutover Validation Checklist
Best Practices
✅ DO
Perform thorough discovery and assessment
Run parallel systems during transition
Test thoroughly before cutover
Have rollback plan ready
Monitor closely post-migration
Document all changes
Train operations team
Maintain previous systems temporarily
❌ DON'T
Rush migration without planning
Migrate without testing
Forget rollback procedures
Ignore dependencies
Skip stakeholder communication
Migrate everything at once
Forget to update documentation
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
SocketWarn
SnykFail