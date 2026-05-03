---
title: aws-lambda-java-integration
url: https://skills.sh/giuseppe-trisciuoglio/developer-kit/aws-lambda-java-integration
---

# aws-lambda-java-integration

skills/giuseppe-trisciuoglio/developer-kit/aws-lambda-java-integration
aws-lambda-java-integration
Installation
$ npx skills add https://github.com/giuseppe-trisciuoglio/developer-kit --skill aws-lambda-java-integration
SKILL.md
AWS Lambda Java Integration

Patterns for creating high-performance AWS Lambda functions in Java with optimized cold starts.

Overview

This skill provides complete patterns for AWS Lambda Java development, covering two main approaches:

Micronaut Framework - Full-featured framework with AOT compilation, dependency injection, and cold start < 1s
Raw Java - Minimal overhead approach with cold start < 500ms

Both approaches support API Gateway and ALB integration with production-ready configurations.

When to Use
Deploying Java functions to AWS Lambda
Optimizing cold starts below 1 second
Choosing between Micronaut and Raw Java approaches
Configuring API Gateway or ALB integration
Setting up CI/CD pipelines for Java Lambda
Instructions
1. Choose Your Approach
Approach	Cold Start	Best For	Complexity
Micronaut	< 1s	Complex apps, DI needed, enterprise	Medium
Raw Java	< 500ms	Simple handlers, minimal overhead	Low

Validate: Confirm the approach fits your use case before proceeding.

2. Project Structure
my-lambda-function/
├── build.gradle (or pom.xml)
├── src/main/java/com/example/Handler.java
└── serverless.yml (or template.yaml)


Validate: Verify project structure matches the template.

3. Implementation Examples
Micronaut Handler
@FunctionBean("my-function")
public class MyFunction implements Function<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    private final MyService service;

    public MyFunction(MyService service) {
        this.service = service;
    }

    @Override
    public APIGatewayProxyResponseEvent apply(APIGatewayProxyRequestEvent request) {
        // Process request
        return new APIGatewayProxyResponseEvent()
            .withStatusCode(200)
            .withBody("{\"message\": \"Success\"}");
    }
}

Raw Java Handler
public class MyHandler implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    private static final MyService service = new MyService();

    @Override
    public APIGatewayProxyResponseEvent handleRequest(APIGatewayProxyRequestEvent request, Context context) {
        return new APIGatewayProxyResponseEvent()
            .withStatusCode(200)
            .withBody("{\"message\": \"Success\"}");
    }
}


Validate: Run sam local invoke to verify handler works before deployment.

Core Patterns
Connection Management
// Initialize once, reuse across invocations
private static final DynamoDbClient dynamoDb = DynamoDbClient.builder()
    .region(Region.US_EAST_1)
    .build();

// Avoid: Creating clients in handler (slow on every invocation)

Error Handling
@Override
public APIGatewayProxyResponseEvent handleRequest(APIGatewayProxyRequestEvent request, Context context) {
    try {
        return successResponse(process(request));
    } catch (ValidationException e) {
        return errorResponse(400, e.getMessage());
    } catch (Exception e) {
        context.getLogger().log("Error: " + e.getMessage());
        return errorResponse(500, "Internal error");
    }
}

Best Practices
Configuration
Memory: Start with 512MB, adjust based on profiling
Timeout: Micronaut 10-30s, Raw Java 5-10s
Runtime: Java 17 or 21 for best performance
Packaging
Use Gradle Shadow Plugin or Maven Shade Plugin
Exclude unnecessary dependencies
Monitoring
Enable X-Ray tracing for performance analysis
Use CloudWatch Insights to track cold vs warm starts
Deployment Options
Serverless Framework
service: my-java-lambda
provider:
  name: aws
  runtime: java21
  memorySize: 512
  timeout: 10
package:
  artifact: build/libs/function.jar
functions:
  api:
    handler: com.example.Handler
    events:
      - http:
          path: /{proxy+}
          method: ANY


Validate: Run serverless deploy with --stage dev first.

AWS SAM
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Resources:
  MyFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: build/libs/function.jar
      Handler: com.example.Handler
      Runtime: java21
      MemorySize: 512
      Timeout: 10
      Events:
        ApiEvent:
          Type: Api
          Properties:
            Path: /{proxy+}
            Method: ANY


Validate: Run sam validate before deploying.

Constraints and Warnings
Java-Specific Constraints
Reflection: Minimize use; prefer AOT compilation (Micronaut)
Classpath scanning: Slows cold start; use explicit configuration
Large frameworks: Spring Boot adds significant cold start overhead
Common Pitfalls
Initialization in handler - Causes repeated work on warm invocations
Oversized JARs - Include only required dependencies
Insufficient memory - Java needs more memory than Node.js/Python
No timeout handling - Always set appropriate timeouts
References

For detailed guidance on specific topics:

Micronaut Lambda - Complete Micronaut setup, AOT configuration, DI optimization
Raw Java Lambda - Minimal handler patterns, singleton caching, JAR packaging
Serverless Deployment - Serverless Framework, SAM, CI/CD pipelines, provisioned concurrency
Testing Lambda - JUnit 5, SAM Local, integration testing, performance measurement
Examples
Example 1: Create a Micronaut Lambda Function

Input:

Create a Java Lambda function using Micronaut to handle user REST API


Process:

Configure Gradle project with Micronaut plugin
Create Handler class extending MicronautRequestHandler
Implement methods for GET/POST/PUT/DELETE
Configure application.yml with AOT optimizations
Set up packaging with Shadow plugin
Validate: Test locally with SAM CLI before deploying

Output:

Complete project structure
Handler with dependency injection
serverless.yml deployment configuration
Example 2: Optimize Cold Start for Raw Java

Input:

My Java Lambda has 3 second cold start, how do I optimize it?


Process:

Analyze initialization code
Move AWS client creation to static fields
Reduce dependencies in build.gradle
Configure optimized JVM options
Consider provisioned concurrency
Validate: Measure cold start with CloudWatch metrics after changes

Output:

Refactored code with singleton pattern
Minimized JAR
Cold start < 500ms
Example 3: Deploy with GitHub Actions

Input:

Configure CI/CD for Java Lambda with SAM


Process:

Create GitHub Actions workflow
Configure Gradle build with Shadow
Set up SAM build and deploy
Add test stage before deployment
Configure environment protection for prod

Output:

Complete .github/workflows/deploy.yml
Multi-stage pipeline (dev/staging/prod)
Integrated test automation
Version

Version: 1.0.0

Weekly Installs
533
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