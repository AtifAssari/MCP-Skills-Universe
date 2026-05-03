---
title: aws-lambda-functions
url: https://skills.sh/aj-geddes/useful-ai-prompts/aws-lambda-functions
---

# aws-lambda-functions

skills/aj-geddes/useful-ai-prompts/aws-lambda-functions
aws-lambda-functions
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill aws-lambda-functions
SKILL.md
AWS Lambda Functions
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

AWS Lambda enables you to run code without provisioning or managing servers. Build serverless applications using event-driven triggers, pay only for compute time consumed, and scale automatically with workload.

When to Use
API endpoints and webhooks
Scheduled batch jobs and data processing
Real-time file processing (S3 uploads)
Event-driven workflows (SNS, SQS)
Microservices and backend APIs
Data transformations and ETL jobs
IoT and sensor data processing
WebSocket connections
Quick Start

Minimal working example:

# Create Lambda execution role
aws iam create-role \
  --role-name lambda-execution-role \
  --assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Principal": {"Service": "lambda.amazonaws.com"},
      "Action": "sts:AssumeRole"
    }]
  }'

# Attach basic execution policy
aws iam attach-role-policy \
  --role-name lambda-execution-role \
  --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole

# Create function from ZIP
zip function.zip index.js
aws lambda create-function \
  --function-name my-function \
  --runtime nodejs18.x \
  --role arn:aws:iam::ACCOUNT:role/lambda-execution-role \
  --handler index.handler \
  --zip-file fileb://function.zip \
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Basic Lambda Function with AWS CLI	Basic Lambda Function with AWS CLI
Lambda Function with Node.js	Lambda Function with Node.js
Terraform Lambda Deployment	Terraform Lambda Deployment
Lambda with SAM (Serverless Application Model)	Lambda with SAM (Serverless Application Model)
Lambda Layers for Code Sharing	Lambda Layers for Code Sharing
Best Practices
✅ DO
Use environment variables for configuration
Implement proper error handling and logging
Optimize package size and dependencies
Set appropriate timeout and memory
Use Lambda Layers for shared code
Implement concurrency limits
Enable X-Ray tracing for debugging
Use reserved concurrency for critical functions
❌ DON'T
Store sensitive data in code
Create long-running operations (>15 min)
Ignore cold start optimization
Forget to handle concurrent executions
Ignore CloudWatch metrics
Use too much memory unnecessarily
Weekly Installs
440
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass