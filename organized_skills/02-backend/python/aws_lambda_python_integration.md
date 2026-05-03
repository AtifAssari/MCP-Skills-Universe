---
rating: ⭐⭐⭐
title: aws-lambda-python-integration
url: https://skills.sh/giuseppe-trisciuoglio/developer-kit/aws-lambda-python-integration
---

# aws-lambda-python-integration

skills/giuseppe-trisciuoglio/developer-kit/aws-lambda-python-integration
aws-lambda-python-integration
Installation
$ npx skills add https://github.com/giuseppe-trisciuoglio/developer-kit --skill aws-lambda-python-integration
SKILL.md
AWS Lambda Python Integration

Patterns for creating high-performance AWS Lambda functions in Python with optimized cold starts and clean architecture.

Overview

AWS Lambda Python integration with two approaches: AWS Chalice (full-featured framework) and Raw Python (minimal overhead). Both support API Gateway/ALB integration with production-ready configurations.

When to Use

Use this skill when:

Creating new Lambda functions in Python
Migrating existing Python applications to Lambda
Optimizing cold start performance for Python Lambda
Choosing between framework-based and minimal Python approaches
Configuring API Gateway or ALB integration
Setting up deployment pipelines for Python Lambda
Instructions
1. Choose Your Approach
Approach	Cold Start	Best For	Complexity
AWS Chalice	< 200ms	REST APIs, rapid development, built-in routing	Low
Raw Python	< 100ms	Simple handlers, maximum control, minimal dependencies	Low
2. Project Structure
AWS Chalice Structure
my-chalice-app/
├── app.py                    # Main application with routes
├── requirements.txt          # Dependencies
├── .chalice/
│   ├── config.json          # Chalice configuration
│   └── deploy/              # Deployment artifacts
├── chalicelib/              # Additional modules
│   ├── __init__.py
│   └── services.py
└── tests/
    └── test_app.py

Raw Python Structure
my-lambda-function/
├── lambda_function.py       # Handler entry point
├── requirements.txt         # Dependencies
├── template.yaml            # SAM/CloudFormation template
└── src/                     # Additional modules
    ├── __init__.py
    ├── handlers.py
    └── utils.py

3. Implementation Examples

See the References section for detailed implementation guides. Quick examples:

AWS Chalice:

from chalice import Chalice
app = Chalice(app_name='my-api')

@app.route('/')
def index():
    return {'message': 'Hello from Chalice!'}


Raw Python:

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Hello from Lambda!'})
    }

Core Concepts
Cold Start Optimization

Key strategies:

Initialize at module level - Persists across warm invocations
Use lazy loading - Defer heavy imports until needed
Cache boto3 clients - Reuse connections between invocations

See Raw Python Lambda for detailed patterns.

Connection Management

Create clients at module level and reuse:

_dynamodb = None

def get_table():
    global _dynamodb
    if _dynamodb is None:
        _dynamodb = boto3.resource('dynamodb').Table('my-table')
    return _dynamodb

Environment Configuration
class Config:
    TABLE_NAME = os.environ.get('TABLE_NAME')
    DEBUG = os.environ.get('DEBUG', 'false').lower() == 'true'

    @classmethod
    def validate(cls):
        if not cls.TABLE_NAME:
            raise ValueError("TABLE_NAME required")

Best Practices
Memory and Timeout Configuration
Memory: Start with 256MB for simple handlers, 512MB for complex operations
Timeout: Set based on expected processing time
Simple handlers: 3-5 seconds
API with DB calls: 10-15 seconds
Data processing: 30-60 seconds
Dependencies

Keep requirements.txt minimal:

# Core AWS SDK - always needed
boto3>=1.35.0

# Only add what you need
requests>=2.32.0  # If calling external APIs
pydantic>=2.5.0   # If using data validation

Error Handling

Return proper HTTP codes with request ID:

def lambda_handler(event, context):
    try:
        result = process_event(event)
        return {'statusCode': 200, 'body': json.dumps(result)}
    except ValueError as e:
        return {'statusCode': 400, 'body': json.dumps({'error': str(e)})}
    except Exception as e:
        print(f"Error: {str(e)}")  # Log to CloudWatch
        return {'statusCode': 500, 'body': json.dumps({'error': 'Internal error'})}


See Raw Python Lambda for structured error patterns.

Logging

Use structured logging for CloudWatch Insights:

import logging, json
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Structured log
logger.info(json.dumps({
    'eventType': 'REQUEST',
    'requestId': context.aws_request_id,
    'path': event.get('path')
}))


See Raw Python Lambda for advanced patterns.

Deployment Options
Quick Start

Validation Checkpoint: Always run serverless print or sam validate before deploying to catch configuration errors early.

Serverless Framework:

# serverless.yml
service: my-python-api
provider:
  name: aws
  runtime: python3.12  # or python3.11
functions:
  api:
    handler: lambda_function.lambda_handler
    events:
      - http:
          path: /{proxy+}
          method: ANY


AWS SAM:

# template.yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31

Resources:
  ApiFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: ./
      Handler: lambda_function.lambda_handler
      Runtime: python3.12  # or python3.11
      Events:
        ApiEvent:
          Type: Api
          Properties:
            Path: /{proxy+}
            Method: ANY


AWS Chalice:

chalice new-project my-api
cd my-api
chalice local 8080  # Test locally before deploying
chalice deploy --stage dev


Validation Checkpoint: Test locally with chalice local or sam local invoke before deploying to production.

For complete deployment configurations including CI/CD, environment-specific settings, and advanced SAM/Serverless patterns, see Serverless Deployment.

Constraints and Warnings
Lambda Limits
Deployment package: 250MB unzipped maximum (50MB zipped)
Memory: 128MB to 10GB
Timeout: 15 minutes maximum
Concurrent executions: 1000 default (adjustable)
Environment variables: 4KB total size
Python-Specific Considerations
Cold start: Python has excellent cold start performance; avoid heavy imports at module level
Dependencies: Keep requirements.txt minimal; use Lambda Layers for shared dependencies
Native dependencies: Must be compiled for Amazon Linux 2 (x86_64 or arm64)
Common Pitfalls
Importing heavy libraries at module level - Defer to function level if not always needed
Not handling Lambda context - Use context.get_remaining_time_in_millis() for timeout awareness
Not validating input - Always validate and sanitize event data
Printing sensitive data - Be careful with logs and CloudWatch

Error Recovery: If deployment fails, check CloudWatch logs for initialization errors and run sam logs to diagnose issues.

Security Considerations
Never hardcode credentials; use IAM roles and environment variables
Validate all input data
Use least privilege IAM policies
Enable CloudTrail for audit logging
References

For detailed guidance on specific topics:

AWS Chalice - Complete Chalice setup, routing, middleware, deployment
Raw Python Lambda - Minimal handler patterns, module caching, packaging
Serverless Deployment - Serverless Framework, SAM, CI/CD pipelines
Testing Lambda - pytest, moto, SAM Local, localstack
Examples
Example 1: Create an AWS Chalice REST API

Input:

Create a Python Lambda REST API using AWS Chalice for a todo application


Process:

Initialize Chalice project with chalice new-project
Configure routes for CRUD operations
Set up DynamoDB integration
Configure deployment stages
Deploy with chalice deploy

Output:

Complete Chalice project structure
REST API with CRUD endpoints
DynamoDB table configuration
Deployment configuration
Example 2: Optimize Cold Start for Raw Python

Input:

My Python Lambda has slow cold start, how do I optimize it?


Process:

Analyze imports and initialization code
Move heavy imports inside functions (lazy loading)
Cache boto3 clients at module level
Remove unnecessary dependencies
Use provisioned concurrency if needed

Output:

Refactored code with lazy loading
Optimized cold start < 100ms
Dependency analysis
Example 3: Deploy with GitHub Actions

Input:

Configure CI/CD for Python Lambda with SAM


Process:

Create GitHub Actions workflow
Set up Python environment and dependencies
Run pytest with coverage
Package with SAM
Deploy to dev/prod stages

Output:

Complete .github/workflows/deploy.yml
Multi-stage pipeline
Integrated test automation
Version

Version: 1.0.0

Weekly Installs
575
Repository
giuseppe-trisci…oper-kit
GitHub Stars
233
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass