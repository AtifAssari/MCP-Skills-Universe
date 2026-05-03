---
rating: ⭐⭐⭐⭐⭐
title: qe-github-code-review
url: https://skills.sh/proffesor-for-testing/agentic-qe/qe-github-code-review
---

# qe-github-code-review

skills/proffesor-for-testing/agentic-qe/qe-github-code-review
qe-github-code-review
Installation
$ npx skills add https://github.com/proffesor-for-testing/agentic-qe --skill qe-github-code-review
SKILL.md
GitHub Code Review Skill

AI-Powered Code Review: Deploy specialized review agents to perform comprehensive, intelligent code reviews that go beyond traditional static analysis.

🎯 Quick Start
Simple Review
# Initialize review swarm for PR
gh pr view 123 --json files,diff | npx ruv-swarm github review-init --pr 123

# Post review status
gh pr comment 123 --body "🔍 Multi-agent code review initiated"

Complete Review Workflow
# Get PR context with gh CLI
PR_DATA=$(gh pr view 123 --json files,additions,deletions,title,body)
PR_DIFF=$(gh pr diff 123)

# Initialize comprehensive review
npx ruv-swarm github review-init \
  --pr 123 \
  --pr-data "$PR_DATA" \
  --diff "$PR_DIFF" \
  --agents "security,performance,style,architecture,accessibility" \
  --depth comprehensive

📚 Table of Contents
Multi-Agent Review System
Specialized Review Agents
PR-Based Swarm Management
Automated Workflows
Quality Gates & Checks
Security Review Agent
Performance Review Agent
Architecture Review Agent
Style & Convention Agent
Accessibility Agent
Context-Aware Reviews
Learning from History
Cross-PR Analysis
Custom Review Agents
CI/CD Integration
Webhook Handlers
PR Comment Commands
Automated Fixes
🚀 Core Features
Multi-Agent Review System

Deploy specialized AI agents for comprehensive code review:

# Initialize review swarm with GitHub CLI integration
PR_DATA=$(gh pr view 123 --json files,additions,deletions,title,body)
PR_DIFF=$(gh pr diff 123)

# Start multi-agent review
npx ruv-swarm github review-init \
  --pr 123 \
  --pr-data "$PR_DATA" \
  --diff "$PR_DIFF" \
  --agents "security,performance,style,architecture,accessibility" \
  --depth comprehensive

# Post initial review status
gh pr comment 123 --body "🔍 Multi-agent code review initiated"


Benefits:

✅ Parallel review by specialized agents
✅ Comprehensive coverage across multiple domains
✅ Faster review cycles with coordinated analysis
✅ Consistent quality standards enforcement
🤖 Specialized Review Agents
Security Review Agent

Focus: Identify security vulnerabilities and suggest fixes

# Get changed files from PR
CHANGED_FILES=$(gh pr view 123 --json files --jq '.files[].path')

# Run security-focused review
SECURITY_RESULTS=$(npx ruv-swarm github review-security \
  --pr 123 \
  --files "$CHANGED_FILES" \
  --check "owasp,cve,secrets,permissions" \
  --suggest-fixes)

# Post findings based on severity
if echo "$SECURITY_RESULTS" | grep -q "critical"; then
  # Request changes for critical issues
  gh pr review 123 --request-changes --body "$SECURITY_RESULTS"
  gh pr edit 123 --add-label "security-review-required"
else
  # Post as comment for non-critical issues
  gh pr comment 123 --body "$SECURITY_RESULTS"
fi

{
  "checks": [
    "SQL injection vulnerabilities",
    "XSS attack vectors",
    "Authentication bypasses",
    "Authorization flaws",
    "Cryptographic weaknesses",
    "Dependency vulnerabilities",
    "Secret exposure",
    "CORS misconfigurations"
  ],
  "actions": [
    "Block PR on critical issues",
    "Suggest secure alternatives",
    "Add security test cases",
    "Update security documentation"
  ]
}

🔒 **Security Issue: [Type]**

**Severity**: 🔴 Critical / 🟡 High / 🟢 Low

**Description**:
[Clear explanation of the security issue]

**Impact**:
[Potential consequences if not addressed]

**Suggested Fix**:
```language
[Code example of the fix]


References:

OWASP Guide
Security Best Practices

</details>

---

### Performance Review Agent

**Focus:** Analyze performance impact and optimization opportunities

```bash
# Run performance analysis
npx ruv-swarm github review-performance \
  --pr 123 \
  --profile "cpu,memory,io" \
  --benchmark-against main \
  --suggest-optimizations

{
  "metrics": [
    "Algorithm complexity (Big O analysis)",
    "Database query efficiency",
    "Memory allocation patterns",
    "Cache utilization",
    "Network request optimization",
    "Bundle size impact",
    "Render performance"
  ],
  "benchmarks": [
    "Compare with baseline",
    "Load test simulations",
    "Memory leak detection",
    "Bottleneck identification"
  ]
}

Architecture Review Agent

Focus: Evaluate design patterns and architectural decisions

# Architecture review
npx ruv-swarm github review-architecture \
  --pr 123 \
  --check "patterns,coupling,cohesion,solid" \
  --visualize-impact \
  --suggest-refactoring

{
  "patterns": [
    "Design pattern adherence",
    "SOLID principles",
    "DRY violations",
    "Separation of concerns",
    "Dependency injection",
    "Layer violations",
    "Circular dependencies"
  ],
  "metrics": [
    "Coupling metrics",
    "Cohesion scores",
    "Complexity measures",
    "Maintainability index"
  ]
}

Style & Convention Agent

Focus: Enforce coding standards and best practices

# Style enforcement with auto-fix
npx ruv-swarm github review-style \
  --pr 123 \
  --check "formatting,naming,docs,tests" \
  --auto-fix "formatting,imports,whitespace"

{
  "checks": [
    "Code formatting",
    "Naming conventions",
    "Documentation standards",
    "Comment quality",
    "Test coverage",
    "Error handling patterns",
    "Logging standards"
  ],
  "auto-fix": [
    "Formatting issues",
    "Import organization",
    "Trailing whitespace",
    "Simple naming issues"
  ]
}

🔄 PR-Based Swarm Management
Create Swarm from PR
# Create swarm from PR description using gh CLI
gh pr view 123 --json body,title,labels,files | npx ruv-swarm swarm create-from-pr

# Auto-spawn agents based on PR labels
gh pr view 123 --json labels | npx ruv-swarm swarm auto-spawn

# Create swarm with full PR context
gh pr view 123 --json body,labels,author,assignees | \
  npx ruv-swarm swarm init --from-pr-data

Label-Based Agent Assignment

Map PR labels to specialized agents:

{
  "label-mapping": {
    "bug": ["debugger", "tester"],
    "feature": ["architect", "coder", "tester"],
    "refactor": ["analyst", "coder"],
    "docs": ["researcher", "writer"],
    "performance": ["analyst", "optimizer"],
    "security": ["security", "authentication", "audit"]
  }
}

Topology Selection by PR Size
# Automatic topology selection based on PR complexity
# Small PR (< 100 lines): ring topology
# Medium PR (100-500 lines): mesh topology
# Large PR (> 500 lines): hierarchical topology
npx ruv-swarm github pr-topology --pr 123

🎬 PR Comment Commands

Execute swarm commands directly from PR comments:

<!-- In PR comment -->
/swarm init mesh 6
/swarm spawn coder "Implement authentication"
/swarm spawn tester "Write unit tests"
/swarm status
/swarm review --agents security,performance

// webhook-handler.js
const { createServer } = require('http');
const { execSync } = require('child_process');

createServer((req, res) => {
  if (req.url === '/github-webhook') {
    const event = JSON.parse(body);

    if (event.action === 'opened' && event.pull_request) {
      execSync(`npx ruv-swarm github pr-init ${event.pull_request.number}`);
    }

    if (event.comment && event.comment.body.startsWith('/swarm')) {
      const command = event.comment.body;
      execSync(`npx ruv-swarm github handle-comment --pr ${event.issue.number} --command "${command}"`);
    }

    res.writeHead(200);
    res.end('OK');
  }
}).listen(3000);

⚙️ Review Configuration
Configuration File
# .github/review-swarm.yml
version: 1
review:
  auto-trigger: true
  required-agents:
    - security
    - performance
    - style
  optional-agents:
    - architecture
    - accessibility
    - i18n

  thresholds:
    security: block      # Block merge on security issues
    performance: warn    # Warn on performance issues
    style: suggest       # Suggest style improvements

  rules:
    security:
      - no-eval
      - no-hardcoded-secrets
      - proper-auth-checks
      - validate-input
    performance:
      - no-n-plus-one
      - efficient-queries
      - proper-caching
      - optimize-loops
    architecture:
      - max-coupling: 5
      - min-cohesion: 0.7
      - follow-patterns
      - avoid-circular-deps

Custom Review Triggers
{
  "triggers": {
    "high-risk-files": {
      "paths": ["**/auth/**", "**/payment/**", "**/admin/**"],
      "agents": ["security", "architecture"],
      "depth": "comprehensive",
      "require-approval": true
    },
    "performance-critical": {
      "paths": ["**/api/**", "**/database/**", "**/cache/**"],
      "agents": ["performance", "database"],
      "benchmarks": true,
      "regression-threshold": "5%"
    },
    "ui-changes": {
      "paths": ["**/components/**", "**/styles/**", "**/pages/**"],
      "agents": ["accessibility", "style", "i18n"],
      "visual-tests": true,
      "responsive-check": true
    }
  }
}

🤖 Automated Workflows
Auto-Review on PR Creation
# .github/workflows/auto-review.yml
name: Automated Code Review
on:
  pull_request:
    types: [opened, synchronize]
  issue_comment:
    types: [created]

jobs:
  swarm-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0

      - name: Setup GitHub CLI
        run: echo "${{ secrets.GITHUB_TOKEN }}" | gh auth login --with-token

      - name: Run Review Swarm
        run: |
          # Get PR context with gh CLI
          PR_NUM=${{ github.event.pull_request.number }}
          PR_DATA=$(gh pr view $PR_NUM --json files,title,body,labels)
          PR_DIFF=$(gh pr diff $PR_NUM)

          # Run swarm review
          REVIEW_OUTPUT=$(npx ruv-swarm github review-all \
            --pr $PR_NUM \
            --pr-data "$PR_DATA" \
            --diff "$PR_DIFF" \
            --agents "security,performance,style,architecture")

          # Post review results
          echo "$REVIEW_OUTPUT" | gh pr review $PR_NUM --comment -F -

          # Update PR status
          if echo "$REVIEW_OUTPUT" | grep -q "approved"; then
            gh pr review $PR_NUM --approve
          elif echo "$REVIEW_OUTPUT" | grep -q "changes-requested"; then
            gh pr review $PR_NUM --request-changes -b "See review comments above"
          fi

      - name: Update Labels
        run: |
          # Add labels based on review results
          if echo "$REVIEW_OUTPUT" | grep -q "security"; then
            gh pr edit $PR_NUM --add-label "security-review"
          fi
          if echo "$REVIEW_OUTPUT" | grep -q "performance"; then
            gh pr edit $PR_NUM --add-label "performance-review"
          fi

💬 Intelligent Comment Generation
Generate Contextual Review Comments
# Get PR diff with context
PR_DIFF=$(gh pr diff 123 --color never)
PR_FILES=$(gh pr view 123 --json files)

# Generate review comments
COMMENTS=$(npx ruv-swarm github review-comment \
  --pr 123 \
  --diff "$PR_DIFF" \
  --files "$PR_FILES" \
  --style "constructive" \
  --include-examples \
  --suggest-fixes)

# Post comments using gh CLI
echo "$COMMENTS" | jq -c '.[]' | while read -r comment; do
  FILE=$(echo "$comment" | jq -r '.path')
  LINE=$(echo "$comment" | jq -r '.line')
  BODY=$(echo "$comment" | jq -r '.body')
  COMMIT_ID=$(gh pr view 123 --json headRefOid -q .headRefOid)

  # Create inline review comments
  gh api \
    --method POST \
    /repos/:owner/:repo/pulls/123/comments \
    -f path="$FILE" \
    -f line="$LINE" \
    -f body="$BODY" \
    -f commit_id="$COMMIT_ID"
done

Batch Comment Management
# Manage review comments efficiently
npx ruv-swarm github review-comments \
  --pr 123 \
  --group-by "agent,severity" \
  --summarize \
  --resolve-outdated

🚪 Quality Gates & Checks
Status Checks
# Required status checks in branch protection
protection_rules:
  required_status_checks:
    strict: true
    contexts:
      - "review-swarm/security"
      - "review-swarm/performance"
      - "review-swarm/architecture"
      - "review-swarm/tests"

Define Quality Gates
# Set quality gate thresholds
npx ruv-swarm github quality-gates \
  --define '{
    "security": {"threshold": "no-critical"},
    "performance": {"regression": "<5%"},
    "coverage": {"minimum": "80%"},
    "architecture": {"complexity": "<10"},
    "duplication": {"maximum": "5%"}
  }'

Track Review Metrics
# Monitor review effectiveness
npx ruv-swarm github review-metrics \
  --period 30d \
  --metrics "issues-found,false-positives,fix-rate,time-to-review" \
  --export-dashboard \
  --format json

🎓 Advanced Features
Context-Aware Reviews

Analyze PRs with full project context:

# Review with comprehensive context
npx ruv-swarm github review-context \
  --pr 123 \
  --load-related-prs \
  --analyze-impact \
  --check-breaking-changes \
  --dependency-analysis

Learning from History

Train review agents on your codebase patterns:

# Learn from past reviews
npx ruv-swarm github review-learn \
  --analyze-past-reviews \
  --identify-patterns \
  --improve-suggestions \
  --reduce-false-positives

# Train on your codebase
npx ruv-swarm github review-train \
  --learn-patterns \
  --adapt-to-style \
  --improve-accuracy

Cross-PR Analysis

Coordinate reviews across related pull requests:

# Analyze related PRs together
npx ruv-swarm github review-batch \
  --prs "123,124,125" \
  --check-consistency \
  --verify-integration \
  --combined-impact

Multi-PR Swarm Coordination
# Coordinate swarms across related PRs
npx ruv-swarm github multi-pr \
  --prs "123,124,125" \
  --strategy "parallel" \
  --share-memory

🛠️ Custom Review Agents
Create Custom Agent
// custom-review-agent.js
class CustomReviewAgent {
  constructor(config) {
    this.config = config;
    this.rules = config.rules || [];
  }

  async review(pr) {
    const issues = [];

    // Custom logic: Check for TODO comments in production code
    if (await this.checkTodoComments(pr)) {
      issues.push({
        severity: 'warning',
        file: pr.file,
        line: pr.line,
        message: 'TODO comment found in production code',
        suggestion: 'Resolve TODO or create issue to track it'
      });
    }

    // Custom logic: Verify API versioning
    if (await this.checkApiVersioning(pr)) {
      issues.push({
        severity: 'error',
        file: pr.file,
        line: pr.line,
        message: 'API endpoint missing versioning',
        suggestion: 'Add /v1/, /v2/ prefix to API routes'
      });
    }

    return issues;
  }

  async checkTodoComments(pr) {
    // Implementation
    const todoRegex = /\/\/\s*TODO|\/\*\s*TODO/gi;
    return todoRegex.test(pr.diff);
  }

  async checkApiVersioning(pr) {
    // Implementation
    const apiRegex = /app\.(get|post|put|delete)\(['"]\/api\/(?!v\d+)/;
    return apiRegex.test(pr.diff);
  }
}

module.exports = CustomReviewAgent;

Register Custom Agent
# Register custom review agent
npx ruv-swarm github register-agent \
  --name "custom-reviewer" \
  --file "./custom-review-agent.js" \
  --category "standards"

🔧 CI/CD Integration
Integration with Build Pipeline
# .github/workflows/build-and-review.yml
name: Build and Review
on: [pull_request]

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm install
      - run: npm test
      - run: npm run build

  swarm-review:
    needs: build-and-test
    runs-on: ubuntu-latest
    steps:
      - name: Run Swarm Review
        run: |
          npx ruv-swarm github review-all \
            --pr ${{ github.event.pull_request.number }} \
            --include-build-results

Automated PR Fixes
# Auto-fix common issues
npx ruv-swarm github pr-fix 123 \
  --issues "lint,test-failures,formatting" \
  --commit-fixes \
  --push-changes

Progress Updates to PR
# Post swarm progress to PR using gh CLI
PROGRESS=$(npx ruv-swarm github pr-progress 123 --format markdown)

gh pr comment 123 --body "$PROGRESS"

# Update PR labels based on progress
if [[ $(echo "$PROGRESS" | grep -o '[0-9]\+%' | sed 's/%//') -gt 90 ]]; then
  gh pr edit 123 --add-label "ready-for-review"
fi

📋 Complete Workflow Examples
Example 1: Security-Critical PR
# Review authentication system changes
npx ruv-swarm github review-init \
  --pr 456 \
  --agents "security,authentication,audit" \
  --depth "maximum" \
  --require-security-approval \
  --penetration-test

Example 2: Performance-Sensitive PR
# Review database optimization
npx ruv-swarm github review-init \
  --pr 789 \
  --agents "performance,database,caching" \
  --benchmark \
  --profile \
  --load-test

Example 3: UI Component PR
# Review new component library
npx ruv-swarm github review-init \
  --pr 321 \
  --agents "accessibility,style,i18n,docs" \
  --visual-regression \
  --component-tests \
  --responsive-check

Example 4: Feature Development PR
# Review new feature implementation
gh pr view 456 --json body,labels,files | \
  npx ruv-swarm github pr-init 456 \
    --topology hierarchical \
    --agents "architect,coder,tester,security" \
    --auto-assign-tasks

Example 5: Bug Fix PR
# Review bug fix with debugging focus
npx ruv-swarm github pr-init 789 \
  --topology mesh \
  --agents "debugger,analyst,tester" \
  --priority high \
  --regression-test

📊 Monitoring & Analytics
Review Dashboard
# Launch real-time review dashboard
npx ruv-swarm github review-dashboard \
  --real-time \
  --show "agent-activity,issue-trends,fix-rates,coverage"

Generate Review Reports
# Create comprehensive review report
npx ruv-swarm github review-report \
  --format "markdown" \
  --include "summary,details,trends,recommendations" \
  --email-stakeholders \
  --export-pdf

PR Swarm Analytics
# Generate PR-specific analytics
npx ruv-swarm github pr-report 123 \
  --metrics "completion-time,agent-efficiency,token-usage,issue-density" \
  --format markdown \
  --compare-baseline

Export to GitHub Insights
# Export metrics to GitHub Insights
npx ruv-swarm github export-metrics \
  --pr 123 \
  --to-insights \
  --dashboard-url

🔐 Security Considerations
Best Practices
Token Permissions: Ensure GitHub tokens have minimal required scopes
Command Validation: Validate all PR comments before execution
Rate Limiting: Implement rate limits for PR operations
Audit Trail: Log all swarm operations for compliance
Secret Management: Never expose API keys in PR comments or logs
Security Checklist
 GitHub token scoped to repository only
 Webhook signatures verified
 Command injection protection enabled
 Rate limiting configured
 Audit logging enabled
 Secrets scanning active
 Branch protection rules enforced
📚 Best Practices
1. Review Configuration
✅ Define clear review criteria upfront
✅ Set appropriate severity thresholds
✅ Configure agent specializations for your stack
✅ Establish override procedures for emergencies
2. Comment Quality
✅ Provide actionable, specific feedback
✅ Include code examples with suggestions
✅ Reference documentation and best practices
✅ Maintain respectful, constructive tone
3. Performance Optimization
✅ Cache analysis results to avoid redundant work
✅ Use incremental reviews for large PRs
✅ Enable parallel agent execution
✅ Batch comment operations efficiently
4. PR Templates
<!-- .github/pull_request_template.md -->
## Swarm Configuration
- Topology: [mesh/hierarchical/ring/star]
- Max Agents: [number]
- Auto-spawn: [yes/no]
- Priority: [high/medium/low]

## Tasks for Swarm
- [ ] Task 1 description
- [ ] Task 2 description
- [ ] Task 3 description

## Review Focus Areas
- [ ] Security review
- [ ] Performance analysis
- [ ] Architecture validation
- [ ] Accessibility check

5. Auto-Merge When Ready
# Auto-merge when swarm completes and passes checks
SWARM_STATUS=$(npx ruv-swarm github pr-status 123)

if [[ "$SWARM_STATUS" == "complete" ]]; then
  # Check review requirements
  REVIEWS=$(gh pr view 123 --json reviews --jq '.reviews | length')

  if [[ $REVIEWS -ge 2 ]]; then
    # Enable auto-merge
    gh pr merge 123 --auto --squash
  fi
fi

🔗 Integration with Claude Code
Workflow Pattern
Claude Code reads PR diff and context
Swarm coordinates review approach based on PR type
Agents work in parallel on different review aspects
Progress updates posted to PR automatically
Final review performed before marking ready
Example: Complete PR Management
[Single Message - Parallel Execution]:
  // Initialize coordination
  mcp__claude-flow__swarm_init { topology: "hierarchical", maxAgents: 5 }
  mcp__claude-flow__agent_spawn { type: "reviewer", name: "Senior Reviewer" }
  mcp__claude-flow__agent_spawn { type: "tester", name: "QA Engineer" }
  mcp__claude-flow__agent_spawn { type: "coordinator", name: "Merge Coordinator" }

  // Create and manage PR using gh CLI
  Bash("gh pr create --title 'Feature: Add authentication' --base main")
  Bash("gh pr view 54 --json files,diff")
  Bash("gh pr review 54 --approve --body 'LGTM after automated review'")

  // Execute tests and validation
  Bash("npm test")
  Bash("npm run lint")
  Bash("npm run build")

  // Track progress
  TodoWrite { todos: [
    { content: "Complete code review", status: "completed", activeForm: "Completing code review" },
    { content: "Run test suite", status: "completed", activeForm: "Running test suite" },
    { content: "Validate security", status: "completed", activeForm: "Validating security" },
    { content: "Merge when ready", status: "pending", activeForm: "Merging when ready" }
  ]}

🆘 Troubleshooting
Common Issues

Solution:

# Check swarm status
npx ruv-swarm swarm-status

# Verify GitHub CLI authentication
gh auth status

# Re-initialize swarm
npx ruv-swarm github review-init --pr 123 --force


Solution:

# Verify GitHub token permissions
gh auth status

# Check API rate limits
gh api rate_limit

# Use batch comment posting
npx ruv-swarm github review-comments --pr 123 --batch


Solution:

# Use incremental review for large PRs
npx ruv-swarm github review-init --pr 123 --incremental

# Reduce agent count
npx ruv-swarm github review-init --pr 123 --agents "security,style" --max-agents 3

# Enable parallel processing
npx ruv-swarm github review-init --pr 123 --parallel --cache-results

📖 Additional Resources
Related Skills
github-pr-manager - Comprehensive PR lifecycle management
github-workflow-automation - Automate GitHub workflows
swarm-coordination - Advanced swarm orchestration
Documentation
GitHub CLI Documentation
RUV Swarm Guide
Claude Flow Integration
Support
GitHub Issues: Report bugs and request features
Community: Join discussions and share experiences
Examples: Browse example configurations and workflows
📄 License

This skill is part of the Claude Code Flow project and is licensed under the MIT License.

Last Updated: 2025-10-19 Version: 1.0.0 Maintainer: Claude Code Flow Team

Weekly Installs
42
Repository
proffesor-for-t…entic-qe
GitHub Stars
334
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykFail