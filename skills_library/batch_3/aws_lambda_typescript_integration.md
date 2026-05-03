---
title: aws-lambda-typescript-integration
url: https://skills.sh/giuseppe-trisciuoglio/developer-kit/aws-lambda-typescript-integration
---

# aws-lambda-typescript-integration

skills/giuseppe-trisciuoglio/developer-kit/aws-lambda-typescript-integration
aws-lambda-typescript-integration
Installation
$ npx skills add https://github.com/giuseppe-trisciuoglio/developer-kit --skill aws-lambda-typescript-integration
SKILL.md
AWS Lambda TypeScript Integration

Patterns for creating high-performance AWS Lambda functions in TypeScript with optimized cold starts.

Overview

Two approaches for TypeScript Lambda:

NestJS Framework - Dependency injection, modular architecture, larger bundle (100KB+)
Raw TypeScript - Minimal overhead, smaller bundle (<50KB), maximum control

Both support API Gateway and ALB integration.

When to Use
Creating new Lambda functions in TypeScript
Optimizing cold start performance
Choosing between NestJS and minimal TypeScript
Configuring API Gateway or ALB integration
Setting up CI/CD for TypeScript Lambda
Instructions
1. Choose Your Approach
Approach	Cold Start	Bundle Size	Best For	Complexity
NestJS	< 500ms	Larger (100KB+)	Complex APIs, enterprise apps, DI needed	Medium
Raw TypeScript	< 100ms	Smaller (< 50KB)	Simple handlers, microservices, minimal deps	Low
2. Project Structure
NestJS Structure
my-nestjs-lambda/
├── src/
│   ├── app.module.ts
│   ├── main.ts
│   ├── lambda.ts           # Lambda entry point
│   └── modules/
│       └── api/
├── package.json
├── tsconfig.json
└── serverless.yml

Raw TypeScript Structure
my-ts-lambda/
├── src/
│   ├── handlers/
│   │   └── api.handler.ts
│   ├── services/
│   └── utils/
├── dist/                   # Compiled output
├── package.json
├── tsconfig.json
└── template.yaml

3. Implementation Examples

See the References section for detailed implementation guides. Quick examples:

NestJS Handler:

// lambda.ts
import { NestFactory } from '@nestjs/core';
import { ExpressAdapter } from '@nestjs/platform-express';
import serverlessExpress from '@codegenie/serverless-express';
import { Context, Handler } from 'aws-lambda';
import express from 'express';
import { AppModule } from './src/app.module';

let cachedServer: Handler;

async function bootstrap(): Promise<Handler> {
  const expressApp = express();
  const adapter = new ExpressAdapter(expressApp);
  const nestApp = await NestFactory.create(AppModule, adapter);
  await nestApp.init();
  return serverlessExpress({ app: expressApp });
}

export const handler: Handler = async (event: any, context: Context) => {
  if (!cachedServer) {
    cachedServer = await bootstrap();
  }
  return cachedServer(event, context);
};


Raw TypeScript Handler:

// src/handlers/api.handler.ts
import { APIGatewayProxyEvent, APIGatewayProxyResult, Context } from 'aws-lambda';

export const handler = async (
  event: APIGatewayProxyEvent,
  context: Context
): Promise<APIGatewayProxyResult> => {
  return {
    statusCode: 200,
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message: 'Hello from TypeScript Lambda!' })
  };
};

Core Concepts
Cold Start Optimization

TypeScript cold start depends on bundle size and initialization code. Key strategies:

Lazy Loading - Defer heavy imports until needed
Tree Shaking - Remove unused code from bundle
Minification - Use esbuild or terser for smaller bundles
Instance Caching - Cache initialized services between invocations

See Raw TypeScript Lambda for detailed patterns.

Connection Management

Create clients at module level and reuse:

// GOOD: Initialize once, reuse across invocations
import { DynamoDBClient } from '@aws-sdk/client-dynamodb';

const dynamoClient = new DynamoDBClient({ region: process.env.AWS_REGION });

export const handler = async (event: APIGatewayProxyEvent) => {
  // Use dynamoClient - already initialized
};

Environment Configuration
// src/config/env.config.ts
export const env = {
  region: process.env.AWS_REGION || 'us-east-1',
  tableName: process.env.TABLE_NAME || '',
  debug: process.env.DEBUG === 'true',
};

// Validate required variables
if (!env.tableName) {
  throw new Error('TABLE_NAME environment variable is required');
}

Best Practices
Memory and Timeout Configuration
Memory: Start with 512MB for NestJS, 256MB for raw TypeScript
Timeout: Set based on cold start + expected processing time
NestJS: 10-30 seconds for cold start buffer
Raw TypeScript: 3-10 seconds typically sufficient
Dependencies

Keep package.json minimal:

{
  "dependencies": {
    "aws-lambda": "^3.1.0",
    "@aws-sdk/client-dynamodb": "^3.450.0"
  },
  "devDependencies": {
    "typescript": "^5.3.0",
    "esbuild": "^0.19.0"
  }
}

Error Handling

Return proper HTTP codes with structured errors:

export const handler = async (event: APIGatewayProxyEvent): Promise<APIGatewayProxyResult> => {
  try {
    const result = await processEvent(event);
    return {
      statusCode: 200,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(result)
    };
  } catch (error) {
    console.error('Error processing request:', error);
    return {
      statusCode: 500,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ error: 'Internal server error' })
    };
  }
};

Logging

Use structured logging for CloudWatch Insights:

const log = (level: string, message: string, meta?: object) => {
  console.log(JSON.stringify({
    level,
    message,
    timestamp: new Date().toISOString(),
    ...meta
  }));
};

log('info', 'Request processed', { requestId: context.awsRequestId });

Deployment Options
Quick Start

Serverless Framework:

service: my-typescript-api

provider:
  name: aws
  runtime: nodejs20.x

functions:
  api:
    handler: dist/handler.handler
    events:
      - http:
          path: /{proxy+}
          method: ANY


AWS SAM:

AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31

Resources:
  ApiFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: dist/
      Handler: handler.handler
      Runtime: nodejs20.x
      Events:
        ApiEvent:
          Type: Api
          Properties:
            Path: /{proxy+}
            Method: ANY

Deployment Validation

Pre-deploy checks:

Run npm test - verify all tests pass
Run npm run build - confirm TypeScript compiles without errors
Verify bundle size < 50MB (unzipped)
Run serverless invoke local or sam local invoke - test locally

Post-deploy verification:

Run serverless invoke or aws lambda invoke - verify handler executes
Test API endpoint via curl or Postman
Check CloudWatch logs for errors
Verify cold start time meets SLA

For complete deployment configurations including CI/CD, see Serverless Deployment.

Constraints and Warnings
Lambda Limits
Deployment package: 250MB unzipped maximum (50MB zipped)
Memory: 128MB to 10GB
Timeout: 15 minutes maximum
Concurrent executions: 1000 default (adjustable)
Environment variables: 4KB total size
TypeScript-Specific Considerations
Bundle size: TypeScript compiles to JavaScript; use bundlers to minimize size
Cold start: Node.js 20.x offers best performance
Dependencies: Use Lambda Layers for shared dependencies
Native modules: Must be compiled for Amazon Linux 2
Common Pitfalls
Importing heavy libraries at module level - Defer to lazy loading if not always needed
Not bundling dependencies - Include all production dependencies in the package
Missing type definitions - Install @types/aws-lambda for proper event typing
No timeout handling - Use context.getRemainingTimeInMillis() for long operations
Security Considerations
Never hardcode credentials; use IAM roles and environment variables
Input Validation for Event Data: All incoming event data (API Gateway request bodies, S3 event objects, SQS message bodies) is untrusted external content; always validate and sanitize before processing to prevent injection attacks
Content Sanitization: When processing S3 objects or SQS message payloads, treat the content as untrusted third-party data; apply appropriate validation, schema checks, and sanitization before acting on it
Validate all input data
Use least privilege IAM policies
Enable CloudTrail for audit logging
Sanitize logs to avoid leaking sensitive data
References

For detailed guidance on specific topics:

NestJS Lambda - Complete NestJS setup, dependency injection, Express/Fastify adapters
Raw TypeScript Lambda - Minimal handler patterns, bundling, tree shaking
Serverless Config - Serverless Framework and SAM configuration
Serverless Deployment - CI/CD pipelines, environment management
Testing - Jest, integration testing, SAM Local
Examples
Example 1: Create a NestJS REST API

Input: Create a TypeScript Lambda REST API using NestJS for a todo application

Process:

Initialize NestJS project with nest new
Install Lambda dependencies: @codegenie/serverless-express, aws-lambda
Create lambda.ts entry point with Express adapter
Configure serverless.yml with API Gateway events
Deploy with Serverless Framework

Validation:

Run serverless invoke local -f api - verify handler works
Check bundle size < 250MB
Test deployed endpoint returns 200 OK

Output: NestJS project with REST API, DynamoDB integration, deployment config

Example 2: Create a Raw TypeScript Lambda

Input: Create a minimal TypeScript Lambda function with optimal cold start

Process:

Set up TypeScript project with esbuild
Create handler with proper AWS types
Configure minimal dependencies
Set up SAM or Serverless deployment
Optimize bundle size with tree shaking

Validation:

Run sam local invoke - test locally before deploying
Verify bundle < 50KB with du -sh dist/
Confirm cold start < 100ms via CloudWatch

Output: Minimal TypeScript Lambda, bundle < 50KB, cold start < 100ms

Example 3: Deploy with GitHub Actions

Input: Configure CI/CD for TypeScript Lambda with SAM

Process:

Create GitHub Actions workflow
Set up Node.js environment
Run tests with Jest
Bundle with esbuild
Deploy with SAM

Validation:

Verify CI pipeline runs npm test successfully
Confirm sam validate passes in pipeline
Check CloudFormation stack created successfully

Output: GitHub Actions workflow, multi-stage pipeline, test automation

Version

Version: 1.0.0

Weekly Installs
582
Repository
giuseppe-trisci…oper-kit
GitHub Stars
233
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass