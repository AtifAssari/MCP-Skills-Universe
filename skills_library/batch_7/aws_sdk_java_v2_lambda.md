---
title: aws-sdk-java-v2-lambda
url: https://skills.sh/giuseppe-trisciuoglio/developer-kit/aws-sdk-java-v2-lambda
---

# aws-sdk-java-v2-lambda

skills/giuseppe-trisciuoglio/developer-kit/aws-sdk-java-v2-lambda
aws-sdk-java-v2-lambda
Installation
$ npx skills add https://github.com/giuseppe-trisciuoglio/developer-kit --skill aws-sdk-java-v2-lambda
Summary

AWS Lambda function invocation, management, and Spring Boot integration using AWS SDK for Java 2.x.

Supports synchronous and asynchronous Lambda invocation with JSON payload serialization and typed response parsing
Covers function lifecycle operations: create, update, delete, list, and retrieve configurations including environment variables and concurrency settings
Includes Spring Boot integration patterns with bean configuration, service abstractions, and type-safe Lambda invoker services
Provides error handling for Lambda-specific failures, payload size constraints (6MB sync, 256KB async), and timeout management up to 15 minutes
SKILL.md
AWS SDK for Java 2.x - AWS Lambda
Overview

AWS Lambda is a compute service that runs code without managing servers. Use this skill to implement AWS Lambda operations using AWS SDK for Java 2.x in applications and services.

When to Use
Invoking Lambda functions from Java applications
Deploying and updating Lambda functions via SDK
Managing function configurations and layers
Integrating Lambda with Spring Boot applications
Quick Reference
Operation	SDK Method	Use Case
Invoke	invoke()	Synchronous/async function invocation
List Functions	listFunctions()	Get all Lambda functions
Get Config	getFunction()	Retrieve function configuration
Create Function	createFunction()	Create new Lambda function
Update Code	updateFunctionCode()	Deploy new function code
Update Config	updateFunctionConfiguration()	Modify settings (timeout, memory, env vars)
Delete Function	deleteFunction()	Remove Lambda function
Instructions
1. Add Dependencies

Include Lambda SDK dependency in pom.xml:

<dependency>
    <groupId>software.amazon.awssdk</groupId>
    <artifactId>lambda</artifactId>
</dependency>


See client-setup.md for complete setup.

2. Create Client

Instantiate LambdaClient with proper configuration:

LambdaClient lambdaClient = LambdaClient.builder()
    .region(Region.US_EAST_1)
    .build();


For async operations, use LambdaAsyncClient.

3. Invoke Lambda Function

Synchronous invocation:

InvokeRequest request = InvokeRequest.builder()
    .functionName("my-function")
    .payload(SdkBytes.fromUtf8String(payload))
    .build();

InvokeResponse response = lambdaClient.invoke(request);

return response.payload().asUtf8String();


See invocation-patterns.md for patterns.

4. Handle Responses

Parse response payloads and check for errors:

if (response.functionError() != null) {
    throw new LambdaInvocationException("Lambda error: " + response.functionError());
}

String result = response.payload().asUtf8String();

5. Manage Functions

Create, update, or delete Lambda functions:

// Create
CreateFunctionRequest createRequest = CreateFunctionRequest.builder()
    .functionName("my-function")
    .runtime(Runtime.JAVA17)
    .role(roleArn)
    .code(code)
    .build();

lambdaClient.createFunction(createRequest);

// Verify function is active before proceeding
GetFunctionRequest getRequest = GetFunctionRequest.builder()
    .functionName("my-function")
    .build();
GetFunctionResponse getResponse = lambdaClient.getFunction(getRequest);
if (!"Active".equals(getResponse.configuration().state())) {
    throw new IllegalStateException("Function not active: " + getResponse.configuration().stateReason());
}

// Update code
UpdateFunctionCodeRequest updateCodeRequest = UpdateFunctionCodeRequest.builder()
    .functionName("my-function")
    .zipFile(SdkBytes.fromByteArray(zipBytes))
    .build();

lambdaClient.updateFunctionCode(updateCodeRequest);

// Wait for deployment to complete
Waiter<GetFunctionConfigurationRequest> waiter = lambdaClient.waiter();
waiter.waitUntilFunctionUpdatedActive(GetFunctionConfigurationRequest.builder()
    .functionName("my-function")
    .build());


See function-management.md for complete patterns.

6. Configure Environment

Set environment variables and concurrency limits:

Environment env = Environment.builder()
    .variables(Map.of(
        "DB_URL", "jdbc:postgresql://db",
        "LOG_LEVEL", "INFO"
    ))
    .build();

UpdateFunctionConfigurationRequest configRequest = UpdateFunctionConfigurationRequest.builder()
    .functionName("my-function")
    .environment(env)
    .timeout(60)
    .memorySize(512)
    .build();

lambdaClient.updateFunctionConfiguration(configRequest);

7. Integrate with Spring Boot

Configure Lambda beans and services:

@Configuration
public class LambdaConfiguration {
    @Bean
    public LambdaClient lambdaClient() {
        return LambdaClient.builder()
            .region(Region.US_EAST_1)
            .build();
    }
}

@Service
public class LambdaInvokerService {
    public <T, R> R invoke(String functionName, T request, Class<R> responseType) {
        // Implementation
    }
}


See spring-boot-integration.md for complete integration.

8. Test Locally

Use mocks or LocalStack for development testing.

See testing.md for testing patterns.

Examples
Basic Invocation
public String invokeFunction(LambdaClient client, String functionName, String payload) {
    InvokeRequest request = InvokeRequest.builder()
        .functionName(functionName)
        .payload(SdkBytes.fromUtf8String(payload))
        .build();

    InvokeResponse response = client.invoke(request);

    if (response.functionError() != null) {
        throw new RuntimeException("Lambda error: " + response.functionError());
    }

    return response.payload().asUtf8String();
}

Async Invocation
public void invokeAsync(LambdaClient client, String functionName, Map<String, Object> event) {
    String jsonPayload = new ObjectMapper().writeValueAsString(event);

    InvokeRequest request = InvokeRequest.builder()
        .functionName(functionName)
        .invocationType(InvocationType.EVENT)
        .payload(SdkBytes.fromUtf8String(jsonPayload))
        .build();

    client.invoke(request);
}

Spring Boot Service
@Service
public class LambdaService {
    private final LambdaClient lambdaClient;

    public UserResponse processUser(UserRequest request) {
        String payload = objectMapper.writeValueAsString(request);

        InvokeResponse response = lambdaClient.invoke(
            InvokeRequest.builder()
                .functionName("user-processor")
                .payload(SdkBytes.fromUtf8String(payload))
                .build()
        );

        return objectMapper.readValue(
            response.payload().asUtf8String(),
            UserResponse.class
        );
    }
}


See examples.md for more examples.

Best Practices
Reuse clients: Create LambdaClient/LambdaAsyncClient once; they are thread-safe
Use async client: For fire-and-forget invocations, use LambdaAsyncClient with CompletableFuture
Verify deployments: Always wait for function state to be Active after create/update operations
Limit payload size: Keep request/response payloads under 256KB for async, 6MB for sync invocations
Configure timeouts: Set client read timeout slightly higher than Lambda function timeout
Use latest runtime: Specify Runtime.JAVA17 or newer for improved cold start performance
Constraints and Warnings
Payload Limit: 6MB (sync), 256KB (async invocation)
Timeout: Max 900 seconds (15 minutes) per invocation
Cold Starts: JVM-based functions have longer cold starts; use GraalVM Native Image for improvement
Deployment Size: Function code + layers must not exceed 50MB (zipped) or 250MB (unzipped)
Concurrency: Default 1000 per region; use reserved concurrency to guarantee capacity
Cost: Monitor with CloudWatch metrics; set billing alerts to prevent runaway costs
References
client-setup.md — Client configuration and setup
invocation-patterns.md — Synchronous and async invocation patterns
function-management.md — Create, update, delete functions
spring-boot-integration.md — Spring Boot configuration and services
testing.md — Unit and integration testing patterns
examples.md — Complete code examples and integration patterns
official-documentation.md — AWS Lambda concepts and API reference
Related Skills
aws-sdk-java-v2-core — Core AWS SDK patterns and client configuration
spring-boot-dependency-injection — Spring dependency injection best practices
unit-test-service-layer — Service testing patterns with Mockito
spring-boot-actuator — Production monitoring and health checks
External Resources
Lambda Examples on GitHub
Lambda API Reference
AWS Lambda Developer Guide
Weekly Installs
689
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