---
title: skill-harvester
url: https://skills.sh/jackspace/claudeskillz/skill-harvester
---

# skill-harvester

skills/jackspace/claudeskillz/skill-harvester
skill-harvester
Installation
$ npx skills add https://github.com/jackspace/claudeskillz --skill skill-harvester
SKILL.md
Skill Harvester

Transform your past work into reusable Claude Code skills automatically.

Overview

The Skill Harvester is a meta-skill that helps you systematically extract reusable patterns, workflows, and expertise from your Claude Code sessions and convert them into well-structured skills that can be shared and reused.

When to Use

Use this skill when:

Completing a significant project or work session
Identifying repetitive patterns across multiple sessions
Building organizational knowledge repositories
Creating team-wide skill libraries
Documenting complex workflows for future reuse
Converting infrastructure/tooling expertise into skills
After solving complex problems that could help future work
Skill Harvesting Process
1. Reflection & Analysis

Examine recent work:

# Review recent git commits
git log --oneline -20

# Analyze file changes
git diff HEAD~10..HEAD --stat

# Check which files were most modified
git log --pretty=format: --name-only | sort | uniq -c | sort -rg | head -20


Identify domains:

What technologies were used? (frameworks, languages, tools)
What problems were solved? (deployment, testing, optimization)
What patterns emerged? (error handling, API integration, workflow)
What expertise was developed? (domain knowledge, best practices)
2. Skill Identification

Questions to ask:

Reusability: Could this help in future projects?
Generalizability: Does it apply beyond this specific context?
Complexity: Is it non-trivial enough to warrant a skill?
Value: Would others benefit from this pattern?
Completeness: Can it be documented as a standalone skill?

Skill categories to consider:

Infrastructure: Docker, Kubernetes, cloud platforms, CI/CD
Backend: API design, database optimization, authentication
Frontend: Component patterns, state management, build optimization
DevOps: Deployment strategies, monitoring, automation
Data Engineering: ETL pipelines, data validation, transformation
Security: Auth patterns, encryption, vulnerability scanning
Testing: Test strategies, mocking, coverage analysis
Documentation: API docs, architecture diagrams, runbooks
3. Skill Template Creation

Essential components of a good skill:

---
name: skill-name (kebab-case)
description: Clear, concise 1-2 sentence description of what the skill does
license: MIT
tags: [relevant, searchable, tags]
---

# Skill Title

Brief overview paragraph explaining the skill's purpose and value.

## When to Use

- Specific scenario 1
- Specific scenario 2
- Specific scenario 3

## Core Concepts

Explain the fundamental ideas and principles.

## Workflow

Step-by-step process for using the skill.

### Step 1: [Action]
Detailed explanation with code examples.

### Step 2: [Action]
More details and examples.

## Common Patterns

### Pattern 1: [Name]
Description and example.

### Pattern 2: [Name]
Description and example.

## Best Practices

### ✅ DO
- Recommended approach 1
- Recommended approach 2

### ❌ DON'T
- Anti-pattern 1
- Anti-pattern 2

## Examples

### Example 1: [Scenario]
Full working example with explanation.

### Example 2: [Scenario]
Another complete example.

## Troubleshooting

### Issue 1: [Problem]
**Symptoms**: What you see
**Cause**: Why it happens
**Solution**: How to fix

## Reference

Quick reference table or cheat sheet.

## Additional Resources

- Links to relevant documentation
- Related skills
- External references

4. Content Extraction

Extract from various sources:

# From code files
# Look for:
# - Complex functions that solve specific problems
# - Utility scripts with general applicability
# - Configuration patterns that work well
# - Error handling strategies
# - Integration patterns

# From documentation
# Harvest:
# - README instructions
# - Setup guides
# - Troubleshooting notes
# - Architecture decisions
# - Lessons learned

# From git commits
git log --all --grep="fix\|feat\|refactor" --pretty=format:"%h %s" -20

# From issue trackers
# Extract:
# - Common problems and solutions
# - Debugging strategies
# - Workarounds and fixes

5. Skill Organization

Directory structure:

harvestable_skills/
├── automation/
│   ├── skill-name/
│   │   └── skill.md
├── backend/
├── devops/
├── frontend/
├── infrastructure/
├── testing/
└── documentation/


Categorization guidelines:

automation: Workflow automation, scripting, batch operations
backend: Server-side development, APIs, databases
cloud: Cloud platforms, serverless, infrastructure
data-engineering: Data processing, ETL, analytics
devops: CI/CD, deployment, monitoring
documentation: Documentation generation, diagrams
frontend: UI development, client-side frameworks
infrastructure: Container orchestration, VMs, networking
security: Authentication, authorization, encryption
testing: Test frameworks, strategies, automation
web-development: Full-stack web development patterns
Harvesting Strategies
Strategy 1: Domain Expertise Extraction

When you've worked extensively with a specific tool or technology:

Document the mental model: How does it work? What are the key concepts?
Capture common operations: What do you do most often?
Record gotchas: What are the common pitfalls?
Create quick reference: What do you always look up?

Example domains:

Database query optimization
Docker multi-stage builds
JWT authentication patterns
GraphQL schema design
Terraform module creation
Strategy 2: Workflow Pattern Extraction

When you've developed an effective workflow:

Map the steps: What's the sequence of actions?
Identify decision points: Where are choices made?
Document prerequisites: What's needed to start?
Capture success criteria: How do you know it worked?

Example workflows:

Blue-green deployments
Feature branch review process
Database migration strategies
API versioning approaches
Strategy 3: Problem-Solution Pattern Mining

When you've solved complex problems:

Describe the problem: What was broken/missing?
Explain the diagnosis: How did you identify it?
Detail the solution: What fixed it?
Generalize the pattern: How to prevent/solve similar issues?

Example patterns:

Memory leak debugging
Race condition resolution
Performance bottleneck analysis
Security vulnerability patching
Strategy 4: Tool Mastery Documentation

When you've become proficient with a tool:

Core operations: What are the essential commands?
Advanced features: What are the power-user tricks?
Integration patterns: How does it work with other tools?
Troubleshooting: Common errors and fixes?

Example tools:

kubectl for Kubernetes
AWS CLI for cloud operations
jq for JSON processing
git for version control
Automation Helpers
Bulk Skill Generation
#!/bin/bash
# bulk-harvest.sh - Generate multiple skills from a list

SKILLS_FILE="$1"
OUTPUT_DIR="harvestable_skills"

while IFS='|' read -r category name description; do
    # Skip header and empty lines
    [[ "$category" == "Category" ]] && continue
    [[ -z "$category" ]] && continue

    SKILL_DIR="$OUTPUT_DIR/$category/$name"
    mkdir -p "$SKILL_DIR"

    cat > "$SKILL_DIR/skill.md" << EOF
---
name: $name
description: $description
license: MIT
---

# ${name//\-/ }

$description

## When to Use

TODO: Add specific scenarios

## Implementation

TODO: Add implementation details

## Examples

TODO: Add working examples

## Best Practices

TODO: Add recommendations
EOF

    echo "✓ Created: $category/$name"
done < "$SKILLS_FILE"


Usage:

# Create skills-to-harvest.txt
cat > skills-to-harvest.txt << EOF
Category|Name|Description
devops|docker-layer-optimization|Optimize Docker image layers for faster builds and smaller images
backend|api-rate-limiting|Implement rate limiting for API endpoints with Redis
testing|snapshot-testing|Create and manage snapshot tests for UI components
EOF

./bulk-harvest.sh skills-to-harvest.txt

Git History Analysis
#!/bin/bash
# analyze-work.sh - Analyze recent work for harvestable patterns

echo "=== Most Modified Files ==="
git log --since="1 month ago" --pretty=format: --name-only | \
    sort | uniq -c | sort -rg | head -20

echo ""
echo "=== Technologies Used ==="
git log --since="1 month ago" --pretty=format:"%s" | \
    grep -oE "(docker|kubernetes|terraform|ansible|python|node|react|vue|postgres|redis|mongodb)" | \
    sort | uniq -c | sort -rg

echo ""
echo "=== Common Commit Themes ==="
git log --since="1 month ago" --pretty=format:"%s" | \
    grep -oE "^(feat|fix|refactor|docs|test|chore)" | \
    sort | uniq -c | sort -rg

echo ""
echo "=== Recent Problem Areas ==="
git log --since="1 month ago" --all --grep="fix\|bug\|issue" --pretty=format:"%h %s" | head -10

Quality Checklist

Before publishing a harvested skill, ensure:

Completeness:

 Clear, descriptive name (kebab-case)
 Concise description (1-2 sentences)
 "When to Use" section with specific scenarios
 Core concepts explained
 Step-by-step workflow
 At least 2 working examples
 Best practices (DO and DON'T)
 Troubleshooting section
 Quick reference or cheat sheet

Quality:

 Examples are copy-pasteable and work
 Code is well-commented
 Explanations are clear and concise
 Covers common edge cases
 Includes error handling
 Performance considerations mentioned
 Security implications addressed
 Links to official documentation

Usefulness:

 Solves a real problem
 Applicable to multiple scenarios
 More efficient than starting from scratch
 Includes domain expertise
 Provides actionable guidance

Organization:

 Placed in correct category
 Properly tagged
 No duplication with existing skills
 Clear relationship to related skills
Integration Workflow
Step 1: Create in Harvestable Directory
mkdir -p harvestable_skills/[category]/[skill-name]
# Create skill.md with full content

Step 2: Review and Refine
Test all examples
Verify instructions
Add missing sections
Improve clarity
Step 3: Move to Skills Collection
# Copy to final location
cp -r harvestable_skills/[category]/[skill-name] skills/

# Or organize by category
cp -r harvestable_skills/[category]/[skill-name] skills-by-category/[category]/

Step 4: Commit and Share
git add skills/ harvestable_skills/
git commit -m "🎯 Harvest skills: [description]"
git push

Examples of Harvested Skills
Example 1: From Infrastructure Work → Skill

Original work: Managing Proxmox VE cluster with containers and VMs

Harvested skill: proxmox-manager

Container lifecycle management
VM provisioning
GPU passthrough configuration
Network troubleshooting
Backup and restore procedures
Example 2: From Problem Solving → Skill

Original work: Dealing with Claude Code timeouts during bulk operations

Harvested skill: session-timeout-handler

Chunking strategies
Checkpoint patterns
Progress tracking
Resume mechanisms
Background process management
Example 3: From Workflow → Skill

Original work: Managing multiple Git repositories with Claude-specific branching

Harvested skill: claude-git-branching

Branch naming conventions
Push with retry logic
Multi-repo coordination
Conflict resolution
PR automation
Tips for Effective Harvesting
🎯 Focus on Value

Harvest skills that:

Save significant time
Reduce errors
Encode expertise
Enable new capabilities
Solve recurring problems
📝 Document Context

Include:

Why this approach works
When to use alternatives
Trade-offs and considerations
Real-world scenarios
Lessons learned
🔄 Iterate and Improve
Start with basic version
Add examples from actual use
Incorporate feedback
Refine based on experience
Version as needed
🤝 Share and Collaborate
Contribute to team repositories
Accept contributions
Review and merge improvements
Build on others' skills
Create skill compositions
Skill Composition

Combine multiple skills for powerful workflows:

# Example: Full-Stack Deployment Skill

Combines:
- docker-optimization (build efficient images)
- kubernetes-deploy (deploy to cluster)
- database-migration (update schema)
- health-check-monitoring (verify deployment)
- rollback-strategy (revert if needed)

Measurement and Tracking

Track the value of your skills:

# Track skill usage
echo "$(date): Used skill-harvester for project X" >> ~/.claude/skill-usage.log

# Count skill reuse
grep "skill-harvester" ~/.claude/skill-usage.log | wc -l

# Measure time saved
# Before: 4 hours to set up manually
# After: 20 minutes with skill
# Savings: 3.67 hours per use

Advanced Patterns
Pattern 1: Progressive Disclosure

Start with simple template, add complexity as needed:

Basic: Essential operations only
Intermediate: Common patterns and variations
Advanced: Edge cases and optimizations
Expert: Deep dives and internals
Pattern 2: Skill Families

Create related skills that work together:

database-skills/
├── postgres-optimization/
├── postgres-backup/
├── postgres-replication/
└── postgres-monitoring/

Pattern 3: Meta-Skills

Skills that help create or manage other skills:

skill-harvester (this skill)
skill-tester (validate skills work)
skill-documenter (generate documentation)
skill-versioner (manage versions)
Resources
Skill Repositories
anthropics/claude-code-skills
Community skill collections
Team-specific repositories
Tools
Git for version control
Markdown for documentation
YAML for metadata
Shell scripts for automation
Best Practices
Follow Claude Code skill conventions
Use consistent formatting
Include metadata frontmatter
Tag appropriately
Version when needed

Version: 1.0.0 Author: Harvested from your_claude_skills repository Last Updated: 2025-11-18 License: MIT

Quick Start
Reflect: Review your recent work (git log, files changed, problems solved)
Identify: List 3-7 skills worth harvesting
Create: Use the skill template for each
Organize: Place in appropriate category
Commit: Add to repository
Share: Push and make available to team

Remember: The best skills solve real problems and encode genuine expertise. Happy harvesting! 🎯

Weekly Installs
33
Repository
jackspace/claudeskillz
GitHub Stars
14
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass