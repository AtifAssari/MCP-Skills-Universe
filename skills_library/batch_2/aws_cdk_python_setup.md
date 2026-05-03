---
title: aws-cdk-python-setup
url: https://skills.sh/github/awesome-copilot/aws-cdk-python-setup
---

# aws-cdk-python-setup

skills/github/awesome-copilot/aws-cdk-python-setup
aws-cdk-python-setup
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill aws-cdk-python-setup
SKILL.md
AWS CDK Python Setup Instructions

This skill provides setup guidance for working with AWS CDK (Cloud Development Kit) projects using Python.

Prerequisites

Before starting, ensure the following tools are installed:

Node.js ≥ 14.15.0 — Required for the AWS CDK CLI
Python ≥ 3.7 — Used for writing CDK code
AWS CLI — Manages credentials and resources
Git — Version control and project management
Installation Steps
1. Install AWS CDK CLI
npm install -g aws-cdk
cdk --version

2. Configure AWS Credentials
# Install AWS CLI (if not installed)
brew install awscli

# Configure credentials
aws configure


Enter your AWS Access Key, Secret Access Key, default region, and output format when prompted.

3. Create a New CDK Project
mkdir my-cdk-project
cd my-cdk-project
cdk init app --language python


Your project will include:

app.py — Main application entry point
my_cdk_project/ — CDK stack definitions
requirements.txt — Python dependencies
cdk.json — Configuration file
4. Set Up Python Virtual Environment
# macOS/Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate

5. Install Python Dependencies
pip install -r requirements.txt


Primary dependencies:

aws-cdk-lib — Core CDK constructs
constructs — Base construct library
Development Workflow
Synthesize CloudFormation Templates
cdk synth


Generates cdk.out/ containing CloudFormation templates.

Deploy Stacks to AWS
cdk deploy


Reviews and confirms deployment to the configured AWS account.

Bootstrap (First Deployment Only)
cdk bootstrap


Prepares environment resources like S3 buckets for asset storage.

Best Practices
Always activate the virtual environment before working.
Run cdk diff before deployment to preview changes.
Use development accounts for testing.
Follow Pythonic naming and directory conventions.
Keep requirements.txt pinned for consistent builds.
Troubleshooting Tips

If issues occur, check:

AWS credentials are correctly configured.
Default region is set properly.
Node.js and Python versions meet minimum requirements.
Run cdk doctor to diagnose environment issues.
Weekly Installs
1.3K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Mar 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass