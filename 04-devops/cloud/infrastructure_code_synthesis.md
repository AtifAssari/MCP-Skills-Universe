---
title: infrastructure-code-synthesis
url: https://skills.sh/qodex-ai/ai-agent-skills/infrastructure-code-synthesis
---

# infrastructure-code-synthesis

skills/qodex-ai/ai-agent-skills/infrastructure-code-synthesis
infrastructure-code-synthesis
Installation
$ npx skills add https://github.com/qodex-ai/ai-agent-skills --skill infrastructure-code-synthesis
SKILL.md
AWS CDK Development

This skill provides comprehensive guidance for developing AWS infrastructure using the Cloud Development Kit (CDK), with integrated MCP servers for accessing latest AWS knowledge and CDK utilities.

AWS Documentation Requirement

CRITICAL: This skill requires AWS MCP tools for accurate, up-to-date AWS information.

Before Answering AWS Questions

Always verify using AWS MCP tools (if available):

mcp__aws-mcp__aws___search_documentation or mcp__*awsdocs*__aws___search_documentation - Search AWS docs
mcp__aws-mcp__aws___read_documentation or mcp__*awsdocs*__aws___read_documentation - Read specific pages
mcp__aws-mcp__aws___get_regional_availability - Check service availability

If AWS MCP tools are unavailable:

Guide user to configure AWS MCP: See AWS MCP Setup Guide
Help determine which option fits their environment:
Has uvx + AWS credentials → Full AWS MCP Server
No Python/credentials → AWS Documentation MCP (no auth)
If cannot determine → Ask user which option to use
Integrated MCP Servers

This skill includes the CDK MCP server automatically configured with the plugin:

AWS CDK MCP Server

When to use: For CDK-specific guidance and utilities

Get CDK construct recommendations
Retrieve CDK best practices
Access CDK pattern suggestions
Validate CDK configurations
Get help with CDK-specific APIs

Important: Leverage this server for CDK construct guidance and advanced CDK operations.

When to Use This Skill

Use this skill when:

Creating new CDK stacks or constructs
Refactoring existing CDK infrastructure
Implementing Lambda functions within CDK
Following AWS CDK best practices
Validating CDK stack configurations before deployment
Verifying AWS service capabilities and regional availability
Core CDK Principles
Resource Naming

CRITICAL: Do NOT explicitly specify resource names when they are optional in CDK constructs.

Why: CDK-generated names enable:

Reusable patterns: Deploy the same construct/pattern multiple times without conflicts
Parallel deployments: Multiple stacks can deploy simultaneously in the same region
Cleaner shared logic: Patterns and shared code can be initialized multiple times without name collision
Stack isolation: Each stack gets uniquely identified resources automatically

Pattern: Let CDK generate unique names automatically using CloudFormation's naming mechanism.

// ❌ BAD - Explicit naming prevents reusability and parallel deployments
new lambda.Function(this, 'MyFunction', {
  functionName: 'my-lambda',  // Avoid this
  // ...
});

// ✅ GOOD - Let CDK generate unique names
new lambda.Function(this, 'MyFunction', {
  // No functionName specified - CDK generates: StackName-MyFunctionXXXXXX
  // ...
});


Security Note: For different environments (dev, staging, prod), follow AWS Security Pillar best practices by using separate AWS accounts rather than relying on resource naming within a single account. Account-level isolation provides stronger security boundaries.

Lambda Function Development

Use the appropriate Lambda construct based on runtime:

TypeScript/JavaScript: Use @aws-cdk/aws-lambda-nodejs

import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';

new NodejsFunction(this, 'MyFunction', {
  entry: 'lambda/handler.ts',
  handler: 'handler',
  // Automatically handles bundling, dependencies, and transpilation
});


Python: Use @aws-cdk/aws-lambda-python

import { PythonFunction } from '@aws-cdk/aws-lambda-python-alpha';

new PythonFunction(this, 'MyFunction', {
  entry: 'lambda',
  index: 'handler.py',
  handler: 'handler',
  // Automatically handles dependencies and packaging
});


Benefits:

Automatic bundling and dependency management
Transpilation handled automatically
No manual packaging required
Consistent deployment patterns
Pre-Deployment Validation

Use a multi-layer validation strategy for comprehensive CDK quality checks:

Layer 1: Real-Time IDE Feedback (Recommended)

For TypeScript/JavaScript projects:

Install cdk-nag for synthesis-time validation:

npm install --save-dev cdk-nag


Add to your CDK app:

import { Aspects } from 'aws-cdk-lib';
import { AwsSolutionsChecks } from 'cdk-nag';

const app = new App();
Aspects.of(app).add(new AwsSolutionsChecks());


Optional - VS Code users: Install CDK NAG Validator extension for faster feedback on file save.

For Python/Java/C#/Go projects: cdk-nag is available in all CDK languages and provides the same synthesis-time validation.

Layer 2: Synthesis-Time Validation (Required)

Synthesis with cdk-nag: Validate stack with comprehensive rules

cdk synth  # cdk-nag runs automatically via Aspects


Suppress legitimate exceptions with documented reasons:

import { NagSuppressions } from 'cdk-nag';

// Document WHY the exception is needed
NagSuppressions.addResourceSuppressions(resource, [
  {
    id: 'AwsSolutions-L1',
    reason: 'Lambda@Edge requires specific runtime for CloudFront compatibility'
  }
]);

Layer 3: Pre-Commit Safety Net

Build: Ensure compilation succeeds

npm run build  # or language-specific build command


Tests: Run unit and integration tests

npm test  # or pytest, mvn test, etc.


Validation Script: Meta-level checks

./scripts/validate-stack.sh


The validation script now focuses on:

Language detection
Template size and resource count analysis
Synthesis success verification
(Note: Detailed anti-pattern checks are handled by cdk-nag)
Workflow Guidelines
Development Workflow
Design: Plan infrastructure resources and relationships
Verify AWS Services: Use AWS Documentation MCP to confirm service availability and features
Check regional availability for all required services
Verify service limits and quotas
Confirm latest API specifications
Implement: Write CDK constructs following best practices
Use CDK MCP server for construct recommendations
Reference CDK best practices via MCP tools
Validate: Run pre-deployment checks (see above)
Synthesize: Generate CloudFormation templates
Review: Examine synthesized templates for correctness
Deploy: Deploy to target environment
Verify: Confirm resources are created correctly
Stack Organization
Use nested stacks for complex applications
Separate concerns into logical construct boundaries
Export values that other stacks may need
Use CDK context for environment-specific configuration
Testing Strategy
Unit test individual constructs
Integration test stack synthesis
Snapshot test CloudFormation templates
Validate resource properties and relationships
Using MCP Servers Effectively
When to Use AWS Documentation MCP

Always verify before implementing:

New AWS service features or configurations
Service availability in target regions
API parameter specifications
Service limits and quotas
Security best practices for AWS services

Example scenarios:

"Check if Lambda supports Python 3.13 runtime"
"Verify DynamoDB is available in eu-south-2"
"What are the current Lambda timeout limits?"
"Get latest S3 encryption options"
When to Use CDK MCP Server

Leverage for CDK-specific guidance:

CDK construct selection and usage
CDK API parameter options
CDK best practice patterns
Construct property configurations
CDK-specific optimizations

Example scenarios:

"What's the recommended CDK construct for API Gateway REST API?"
"How to configure NodejsFunction bundling options?"
"Best practices for CDK stack organization"
"CDK construct for DynamoDB with auto-scaling"
MCP Usage Best Practices
Verify First: Always check AWS Documentation MCP before implementing new features
Regional Validation: Check service availability in target deployment regions
CDK Guidance: Use CDK MCP for construct-specific recommendations
Stay Current: MCP servers provide latest information beyond knowledge cutoff
Combine Sources: Use both skill patterns and MCP servers for comprehensive guidance
CDK Patterns Reference

For detailed CDK patterns, anti-patterns, and architectural guidance, refer to the comprehensive reference:

File: references/cdk-patterns.md

This reference includes:

Common CDK patterns and their use cases
Anti-patterns to avoid
Security best practices
Cost optimization strategies
Performance considerations
Additional Resources
Validation Script: scripts/validate-stack.sh - Pre-deployment validation
CDK Patterns: references/cdk-patterns.md - Detailed pattern library
AWS Documentation MCP: Integrated for latest AWS information
CDK MCP Server: Integrated for CDK-specific guidance
GitHub Actions Integration

When GitHub Actions workflow files exist in the repository, ensure all checks defined in .github/workflows/ pass before committing. This prevents CI/CD failures and maintains code quality standards.

Weekly Installs
65
Repository
qodex-ai/ai-agent-skills
GitHub Stars
6
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass