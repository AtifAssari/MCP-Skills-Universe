---
title: aws-sdk-java-v2-core
url: https://skills.sh/giuseppe-trisciuoglio/developer-kit/aws-sdk-java-v2-core
---

# aws-sdk-java-v2-core

skills/giuseppe-trisciuoglio/developer-kit/aws-sdk-java-v2-core
aws-sdk-java-v2-core
Installation
$ npx skills add https://github.com/giuseppe-trisciuoglio/developer-kit --skill aws-sdk-java-v2-core
Summary

Core patterns and configuration for AWS SDK for Java 2.x service clients, authentication, and HTTP management.

Covers client builder patterns, credential provider chains (environment variables, profiles, IAM roles, SSO), and lifecycle management with try-with-resources
Supports Apache HTTP client for sync operations and Netty for async, with connection pooling, timeout configuration, and SSL optimization
Includes Spring Boot integration with @ConfigurationProperties, bean definitions, and externalized configuration
Provides error handling patterns, streaming response management, and testing strategies with LocalStack and Testcontainers
Best practices emphasize client reuse, proper timeout settings, resource cleanup, and security (no hardcoded credentials, IAM roles, least privilege)
SKILL.md
AWS SDK for Java 2.x Core Patterns
Overview

Use this skill to set up AWS SDK for Java 2.x clients with production-safe defaults.

It focuses on the decisions that matter most:

how credentials and region are resolved
how to configure sync and async HTTP clients
how to apply timeouts, retries, lifecycle management, and tests

Keep SKILL.md focused on setup and delivery flow. Use the references/ files for deeper API details and expanded examples.

When to Use
Creating or hardening AWS SDK for Java 2.x service clients
Wiring Spring Boot beans for AWS integration
Debugging auth, region, or credential issues
Choosing between sync (S3Client, DynamoDbClient) and async (S3AsyncClient, SqsAsyncClient) clients
Instructions
1. Select the service client type
Sync clients (S3Client, DynamoDbClient) for request/response flows
Async clients (S3AsyncClient, SqsAsyncClient) for concurrency, streaming, or backpressure
Reuse one client per service and configuration profile
2. Configure credential and region resolution

Use DefaultCredentialsProvider with environment-aware defaults:

local dev: shared AWS config, SSO, or environment variables
CI/CD: web identity or injected environment variables
AWS runtime: ECS task roles, EKS IRSA, or EC2 instance profiles

Override only for multi-account access, test isolation, or profile switching.

Verify: Call StsClient.getCallerIdentity() at startup to confirm credentials resolve.

3. Configure HTTP client, timeouts, and retries

Set production values explicitly:

API call timeout and attempt timeout
connection timeout and max connections or concurrency
retry strategy aligned with service quotas and idempotency

Use ApacheHttpClient for sync and NettyNioAsyncHttpClient for async.

Verify: Confirm timeouts and retry behavior under failure conditions.

4. Wire clients as application-level dependencies

In Spring Boot:

expose clients as @Bean singletons
inject through constructors
keep credential and region in configuration files

Verify: Check clients are not created inside hot execution paths.

Close custom HTTP clients and SDK clients during shutdown if lifecycle is not managed automatically.

5. Handle failures at integration boundaries

At the boundary layer:

catch SdkException or service-specific exceptions
distinguish retryable failures from auth, quota, and validation failures
log request context, never secrets or raw credentials
6. Run integration tests before shipping
verify region and caller identity in the target environment
run tests against LocalStack, Testcontainers, or a sandbox account
use @PostConstruct in Spring Boot configuration to fail fast on startup if credentials are missing
StsClient stsClient = StsClient.builder().build();
GetCallerIdentityResponse identity = stsClient.getCallerIdentity();
// Logs: Successfully authenticated as: {identity.arn()}

Examples
Example 1: Spring Boot sync client with explicit HTTP and timeout settings
@Configuration
public class AwsClientConfiguration {

    @Bean
    S3Client s3Client() {
        return S3Client.builder()
            .region(Region.of("eu-south-2"))
            .credentialsProvider(DefaultCredentialsProvider.create())
            .httpClientBuilder(ApacheHttpClient.builder()
                .maxConnections(100)
                .connectionTimeout(Duration.ofSeconds(3)))
            .overrideConfiguration(ClientOverrideConfiguration.builder()
                .apiCallAttemptTimeout(Duration.ofSeconds(10))
                .apiCallTimeout(Duration.ofSeconds(30))
                .build())
            .build();
    }
}

Example 2: Async client for high-concurrency workloads
SqsAsyncClient sqsAsyncClient = SqsAsyncClient.builder()
    .region(Region.US_EAST_1)
    .credentialsProvider(DefaultCredentialsProvider.create())
    .httpClientBuilder(NettyNioAsyncHttpClient.builder()
        .maxConcurrency(200)
        .connectionTimeout(Duration.ofSeconds(3))
        .readTimeout(Duration.ofSeconds(20)))
    .overrideConfiguration(ClientOverrideConfiguration.builder()
        .apiCallTimeout(Duration.ofSeconds(30))
        .build())
    .build();

Best Practices
Default to DefaultCredentialsProvider unless a project requirement says otherwise.
Keep region selection explicit for server-side services.
Reuse SDK clients instead of constructing them per request.
Tune retries with service quotas and idempotency in mind.
Put business mapping on top of the SDK, not inside controllers.
Keep integration tests close to the configuration that creates the clients.
Move deep service-specific examples to dedicated skills such as S3, DynamoDB, Bedrock, or Secrets Manager.
Constraints and Warnings
Do not embed access keys or session tokens in source code, examples, or configuration files.
Static credentials are acceptable only for tightly scoped local tests.
Missing region or invalid credential resolution often fails only at first call, so verify startup assumptions explicitly.
Async clients require lifecycle management for the underlying HTTP resources.
Excessive retries can amplify throttling and increase latency.
Proxy, TLS, and metric publisher APIs can vary by chosen HTTP stack and SDK version; adapt examples to the versions already used by the project.
References
references/api-reference.md
references/best-practices.md
references/developer-guide.md
Related Skills
aws-sdk-java-v2-secrets-manager
aws-sdk-java-v2-s3
aws-sdk-java-v2-dynamodb
aws-sdk-java-v2-bedrock
Weekly Installs
688
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