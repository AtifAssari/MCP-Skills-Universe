---
title: github-actions-oidc-aws
url: https://skills.sh/loxosceles/ai-dev/github-actions-oidc-aws
---

# github-actions-oidc-aws

skills/loxosceles/ai-dev/github-actions-oidc-aws
github-actions-oidc-aws
Installation
$ npx skills add https://github.com/loxosceles/ai-dev --skill github-actions-oidc-aws
SKILL.md
GitHub Actions OIDC Authentication for AWS

This is a reference pattern. Learn from the approach, adapt to your context — don't copy verbatim.

Status: 🔴 CRITICAL PATTERN
Category: CI/CD / Infrastructure
Applies To: Any project using GitHub Actions to deploy to AWS

Overview

Secure authentication pattern for GitHub Actions workflows to access AWS resources using OpenID Connect (OIDC) instead of long-lived IAM credentials. Eliminates the need to store AWS access keys in GitHub secrets.

Key Benefits:

No long-lived credentials to rotate or leak
Temporary credentials with automatic expiration
Repository-scoped access control
Audit trail via AWS CloudTrail
Industry best practice (AWS + GitHub recommended)
Problem

GitHub Actions workflows need to authenticate to AWS to deploy infrastructure, trigger pipelines, or manage resources. Traditional approaches have security issues:

Anti-Pattern: Static IAM Credentials

# ❌ Security risk: long-lived credentials in secrets
- uses: aws-actions/configure-aws-credentials@v4
  with:
    aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
    aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}


Problems:

Credentials never expire (must be manually rotated)
If leaked, attacker has persistent access
No way to scope to specific repositories
Difficult to audit which workflow used credentials
Violates principle of least privilege
Solution

Use GitHub's OIDC provider to issue temporary credentials via AWS IAM role assumption.

Flow:

GitHub Actions → OIDC Token → AWS STS → Temporary Credentials → AWS Resources


How it works:

GitHub Actions requests OIDC token from GitHub
Workflow presents token to AWS STS
AWS validates token against IAM OIDC provider
AWS issues temporary credentials (valid 1 hour)
Workflow uses temporary credentials to access AWS
Components
1. AWS IAM OIDC Provider

Establishes trust between AWS and GitHub's OIDC issuer.

Configuration:

URL: https://token.actions.githubusercontent.com
Audience: sts.amazonaws.com
Thumbprint: 1c58a3a8518e8759bf075b76b750d4f2df264fcd (GitHub root CA)

Why root CA thumbprint?

More stable than intermediate certificate
GitHub can rotate intermediate certs without breaking trust
Recommended by AWS documentation
2. IAM Role with Trust Policy

Role that GitHub Actions can assume, with trust policy restricting access.

Trust Policy Structure:

{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {
      "Federated": "arn:aws:iam::{account}:oidc-provider/token.actions.githubusercontent.com"
    },
    "Action": "sts:AssumeRoleWithWebIdentity",
    "Condition": {
      "StringEquals": {
        "token.actions.githubusercontent.com:aud": "sts.amazonaws.com"
      },
      "StringLike": {
        "token.actions.githubusercontent.com:sub": "repo:{owner}/{repo}:*"
      }
    }
  }]
}


Trust Policy Scoping Options:

# All branches and tags
"repo:owner/repo:*"

# Specific branch only
"repo:owner/repo:ref:refs/heads/main"

# Multiple branches
["repo:owner/repo:ref:refs/heads/main", "repo:owner/repo:ref:refs/heads/dev"]

# Pull requests
"repo:owner/repo:pull_request"

# Environment-specific
"repo:owner/repo:environment:production"

3. IAM Permissions Policy

Defines what the role can do in AWS (principle of least privilege).

Examples by use case:

Pipeline Trigger Only:

{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": "codepipeline:StartPipelineExecution",
    "Resource": "arn:aws:codepipeline:*:{account}:pipeline-name-*"
  }]
}


Direct S3 Deployment:

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:PutObject", "s3:DeleteObject", "s3:ListBucket"],
      "Resource": ["arn:aws:s3:::bucket-name", "arn:aws:s3:::bucket-name/*"]
    },
    {
      "Effect": "Allow",
      "Action": "cloudfront:CreateInvalidation",
      "Resource": "*"
    }
  ]
}


Infrastructure Deployment (use with caution):

{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": "*",
    "Resource": "*"
  }]
}

4. GitHub Actions Workflow Configuration

Workflow must request OIDC token and assume role.

Required Permissions:

permissions:
  id-token: write  # Required for OIDC token
  contents: read   # Required to checkout code


Authentication Step:

- uses: aws-actions/configure-aws-credentials@v4
  with:
    role-to-assume: arn:aws:iam::{account}:role/{role-name}
    aws-region: {region}

Implementation
Step 1: Create OIDC Provider (One-Time Setup)

Choose your infrastructure tool:

AWS CDK (TypeScript):

import * as iam from 'aws-cdk-lib/aws-iam';

const provider = new iam.OpenIdConnectProvider(this, 'GitHubProvider', {
  url: 'https://token.actions.githubusercontent.com',
  clientIds: ['sts.amazonaws.com'],
  thumbprints: ['1c58a3a8518e8759bf075b76b750d4f2df264fcd']
});


Terraform:

resource "aws_iam_openid_connect_provider" "github" {
  url = "https://token.actions.githubusercontent.com"
  client_id_list = ["sts.amazonaws.com"]
  thumbprint_list = ["1c58a3a8518e8759bf075b76b750d4f2df264fcd"]
}


AWS CLI:

aws iam create-open-id-connect-provider \
  --url https://token.actions.githubusercontent.com \
  --client-id-list sts.amazonaws.com \
  --thumbprint-list 1c58a3a8518e8759bf075b76b750d4f2df264fcd


CloudFormation:

GitHubOIDCProvider:
  Type: AWS::IAM::OIDCProvider
  Properties:
    Url: https://token.actions.githubusercontent.com
    ClientIdList:
      - sts.amazonaws.com
    ThumbprintList:
      - 1c58a3a8518e8759bf075b76b750d4f2df264fcd

Step 2: Create IAM Role

AWS CDK (TypeScript):

const role = new iam.Role(this, 'GitHubActionsRole', {
  roleName: 'GitHubActionsRole',
  assumedBy: new iam.WebIdentityPrincipal(provider.openIdConnectProviderArn, {
    StringEquals: {
      'token.actions.githubusercontent.com:aud': 'sts.amazonaws.com'
    },
    StringLike: {
      'token.actions.githubusercontent.com:sub': `repo:${owner}/${repo}:*`
    }
  }),
  inlinePolicies: {
    DeploymentPermissions: new iam.PolicyDocument({
      statements: [
        new iam.PolicyStatement({
          effect: iam.Effect.ALLOW,
          actions: ['codepipeline:StartPipelineExecution'],
          resources: [`arn:aws:codepipeline:*:${this.account}:pipeline-*`]
        })
      ]
    })
  }
});


Terraform:

resource "aws_iam_role" "github_actions" {
  name = "GitHubActionsRole"
  
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = {
        Federated = aws_iam_openid_connect_provider.github.arn
      }
      Action = "sts:AssumeRoleWithWebIdentity"
      Condition = {
        StringEquals = {
          "token.actions.githubusercontent.com:aud" = "sts.amazonaws.com"
        }
        StringLike = {
          "token.actions.githubusercontent.com:sub" = "repo:${var.github_owner}/${var.github_repo}:*"
        }
      }
    }]
  })
}

resource "aws_iam_role_policy" "github_actions" {
  name = "deployment-permissions"
  role = aws_iam_role.github_actions.id
  
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = "codepipeline:StartPipelineExecution"
      Resource = "arn:aws:codepipeline:*:${data.aws_caller_identity.current.account_id}:pipeline-*"
    }]
  })
}

Step 3: Update GitHub Actions Workflow

Before (Static Credentials):

name: Deploy
on: [push]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1
      
      - run: aws s3 sync ./dist s3://my-bucket


After (OIDC):

name: Deploy
on: [push]

permissions:
  id-token: write
  contents: read

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789012:role/GitHubActionsRole
          aws-region: us-east-1
      
      - run: aws s3 sync ./dist s3://my-bucket

Step 4: Remove Old Secrets (Cleanup)
# List current secrets
gh secret list

# Remove old credentials
gh secret remove AWS_ACCESS_KEY_ID
gh secret remove AWS_SECRET_ACCESS_KEY

Configuration Management
Avoid Hardcoding Account IDs

Anti-Pattern:

role-to-assume: arn:aws:iam::123456789012:role/GitHubActionsRole


Better: Use Repository Variables:

role-to-assume: arn:aws:iam::${{ vars.AWS_ACCOUNT_ID }}:role/GitHubActionsRole


Best: Read from Configuration File:

- name: Load config
  id: config
  run: |
    echo "account=$(grep '^AWS_ACCOUNT_ID=' .env | cut -d'=' -f2)" >> $GITHUB_OUTPUT
    echo "region=$(grep '^AWS_REGION=' .env | cut -d'=' -f2)" >> $GITHUB_OUTPUT

- uses: aws-actions/configure-aws-credentials@v4
  with:
    role-to-assume: arn:aws:iam::${{ steps.config.outputs.account }}:role/GitHubActionsRole
    aws-region: ${{ steps.config.outputs.region }}

Deployment Patterns
Pattern A: Pipeline Trigger

GitHub Actions triggers AWS CodePipeline, which handles actual deployment.

Use When:

Complex multi-stage deployments
Need AWS-native deployment history
Want to trigger from multiple sources
Build requires significant compute resources

Workflow:

permissions:
  id-token: write
  contents: read

jobs:
  trigger:
    runs-on: ubuntu-latest
    steps:
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::${{ vars.AWS_ACCOUNT_ID }}:role/GitHubActionsRole
          aws-region: ${{ vars.AWS_REGION }}
      
      - run: aws codepipeline start-pipeline-execution --name my-pipeline


IAM Permissions:

{
  "Effect": "Allow",
  "Action": "codepipeline:StartPipelineExecution",
  "Resource": "arn:aws:codepipeline:*:*:pipeline-name"
}

Pattern B: Direct Deployment

GitHub Actions performs full deployment (build + deploy).

Use When:

Simple static site deployments
Want fast feedback loops
Prefer GitHub Actions native features
Cost-conscious (avoid CodePipeline/CodeBuild costs)

Workflow:

permissions:
  id-token: write
  contents: read

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      
      - run: npm ci && npm run build
      
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::${{ vars.AWS_ACCOUNT_ID }}:role/GitHubActionsRole
          aws-region: ${{ vars.AWS_REGION }}
      
      - run: |
          aws s3 sync dist/ s3://my-bucket/ --delete
          aws cloudfront create-invalidation --distribution-id ${{ vars.CF_DIST_ID }} --paths "/*"


IAM Permissions:

{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:PutObject", "s3:DeleteObject", "s3:ListBucket"],
      "Resource": ["arn:aws:s3:::bucket/*", "arn:aws:s3:::bucket"]
    },
    {
      "Effect": "Allow",
      "Action": "cloudfront:CreateInvalidation",
      "Resource": "*"
    }
  ]
}

Pattern C: Infrastructure Deployment

GitHub Actions deploys infrastructure changes (CDK, Terraform, CloudFormation).

Use When:

Infrastructure as Code workflows
Want PR-based infrastructure reviews
Need to validate changes before merge

Workflow:

permissions:
  id-token: write
  contents: read
  pull-requests: write  # For PR comments

jobs:
  plan:
    if: github.event_name == 'pull_request'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::${{ vars.AWS_ACCOUNT_ID }}:role/GitHubActionsTerraformRole
          aws-region: ${{ vars.AWS_REGION }}
      
      - run: terraform plan -out=plan.tfplan
      
      - uses: actions/github-script@v7
        with:
          script: |
            // Post plan to PR comment
  
  apply:
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::${{ vars.AWS_ACCOUNT_ID }}:role/GitHubActionsTerraformRole
          aws-region: ${{ vars.AWS_REGION }}
      
      - run: terraform apply -auto-approve


IAM Permissions: Typically requires broad permissions (AdministratorAccess or PowerUserAccess). Consider using separate roles for plan (read-only) vs apply (write).

Multi-Environment Strategy
Separate Roles per Environment

Recommended: Create separate roles for dev/staging/prod with different permissions.

CDK Example:

['dev', 'prod'].forEach(env => {
  new iam.Role(this, `GitHubActionsRole-${env}`, {
    roleName: `GitHubActionsRole-${env}`,
    assumedBy: new iam.WebIdentityPrincipal(provider.openIdConnectProviderArn, {
      StringEquals: {
        'token.actions.githubusercontent.com:aud': 'sts.amazonaws.com'
      },
      StringLike: {
        'token.actions.githubusercontent.com:sub': 
          env === 'prod' 
            ? `repo:${owner}/${repo}:ref:refs/heads/main`
            : `repo:${owner}/${repo}:ref:refs/heads/dev`
      }
    })
  });
});


Workflow:

- name: Determine environment
  id: env
  run: |
    if [ "${{ github.ref }}" = "refs/heads/main" ]; then
      echo "name=prod" >> $GITHUB_OUTPUT
    else
      echo "name=dev" >> $GITHUB_OUTPUT
    fi

- uses: aws-actions/configure-aws-credentials@v4
  with:
    role-to-assume: arn:aws:iam::${{ vars.AWS_ACCOUNT_ID }}:role/GitHubActionsRole-${{ steps.env.outputs.name }}
    aws-region: ${{ vars.AWS_REGION }}

Security Considerations
1. Principle of Least Privilege

Always grant minimum permissions required:

// ❌ Too broad
{
  "Effect": "Allow",
  "Action": "*",
  "Resource": "*"
}

// ✅ Specific
{
  "Effect": "Allow",
  "Action": "codepipeline:StartPipelineExecution",
  "Resource": "arn:aws:codepipeline:us-east-1:123456789012:my-pipeline"
}

2. Repository Scoping

Always restrict to specific repository:

// ❌ Any repository in organization
"token.actions.githubusercontent.com:sub": "repo:my-org/*"

// ✅ Specific repository
"token.actions.githubusercontent.com:sub": "repo:my-org/my-repo:*"

// ✅ Even more specific (main branch only)
"token.actions.githubusercontent.com:sub": "repo:my-org/my-repo:ref:refs/heads/main"

3. Audience Validation

Always validate audience:

{
  "StringEquals": {
    "token.actions.githubusercontent.com:aud": "sts.amazonaws.com"
  }
}

4. Session Duration

Default: 1 hour (sufficient for most workflows)

Custom duration (if needed):

- uses: aws-actions/configure-aws-credentials@v4
  with:
    role-to-assume: arn:aws:iam::123456789012:role/GitHubActionsRole
    role-duration-seconds: 3600  # 1 hour (default)
    aws-region: us-east-1

5. CloudTrail Auditing

Monitor role assumptions:

aws cloudtrail lookup-events \
  --lookup-attributes AttributeKey=EventName,AttributeValue=AssumeRoleWithWebIdentity \
  --max-results 10


Key fields to monitor:

userIdentity.principalId: GitHub repository and workflow
requestParameters.roleArn: Which role was assumed
sourceIPAddress: GitHub Actions IP range
userAgent: GitHub Actions user agent
Troubleshooting
Error: "Not authorized to perform sts:AssumeRoleWithWebIdentity"

Cause: Trust policy doesn't match workflow context.

Check:

Repository name matches trust policy
Branch/tag matches trust policy condition
Workflow has id-token: write permission

Debug:

- name: Debug OIDC token
  run: |
    curl -H "Authorization: bearer $ACTIONS_ID_TOKEN_REQUEST_TOKEN" \
      "$ACTIONS_ID_TOKEN_REQUEST_URL&audience=sts.amazonaws.com" | jq

Error: "OpenIDConnect provider not found"

Cause: OIDC provider not created or wrong ARN.

Fix:

# List providers
aws iam list-open-id-connect-providers

# Check provider details
aws iam get-open-id-connect-provider \
  --open-id-connect-provider-arn arn:aws:iam::123456789012:oidc-provider/token.actions.githubusercontent.com

Error: "Access Denied" after successful authentication

Cause: Role lacks required permissions.

Fix: Update role's permissions policy to include required actions.

Workflow doesn't request OIDC token

Cause: Missing id-token: write permission.

Fix:

permissions:
  id-token: write  # Add this
  contents: read

Migration Checklist

Migrating from static credentials to OIDC:

 Create OIDC provider in AWS account
 Create IAM role with trust policy
 Attach permissions policy to role
 Test role assumption manually (optional)
 Update workflow to use OIDC
 Add permissions block to workflow
 Replace credential secrets with role ARN
 Test workflow in non-production environment
 Verify CloudTrail logs show role assumption
 Deploy to production
 Remove old AWS credential secrets from GitHub
 Revoke/delete old IAM user (if applicable)
 Document role ARN and permissions
References
GitHub Actions OIDC Documentation
AWS IAM OIDC Provider Documentation
aws-actions/configure-aws-credentials
GitHub OIDC Token Claims
AWS Security Blog: Use IAM roles to connect GitHub Actions
Progressive Improvement

If the developer corrects a behavior that this skill should have prevented, suggest a specific amendment to this skill to prevent the same correction in the future.

Weekly Installs
41
Repository
loxosceles/ai-dev
First Seen
Mar 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass