---
rating: ⭐⭐
title: aws-sdk-java-v2-rds
url: https://skills.sh/giuseppe-trisciuoglio/developer-kit/aws-sdk-java-v2-rds
---

# aws-sdk-java-v2-rds

skills/giuseppe-trisciuoglio/developer-kit/aws-sdk-java-v2-rds
aws-sdk-java-v2-rds
Installation
$ npx skills add https://github.com/giuseppe-trisciuoglio/developer-kit --skill aws-sdk-java-v2-rds
Summary

AWS RDS instance and snapshot management using AWS SDK for Java 2.x.

Covers core RDS operations: creating and modifying DB instances, managing snapshots, parameter groups, and querying instance metadata across PostgreSQL, MySQL, Aurora, and other engines
Includes security patterns for VPC configuration, encryption, IAM authentication, and deletion protection; Multi-AZ and automated backup setup for high availability
Provides Spring Boot and Lambda integration examples with connection pooling, credential management, and service layer patterns
Features best practices for resource management, cost optimization, monitoring via CloudWatch, and comprehensive error handling with retry logic
SKILL.md
AWS SDK for Java v2 - RDS Management
Overview

This skill provides comprehensive guidance for working with Amazon RDS (Relational Database Service) using the AWS SDK for Java 2.x, covering database instance management, snapshots, parameter groups, and RDS operations.

When to Use
Creating, modifying, or deleting RDS database instances
Managing DB snapshots, parameter groups, and configurations
Setting up Multi-AZ deployments and automated backups
Connecting Lambda functions to RDS databases
Monitoring instance status and performance
Instructions

Follow these steps to work with Amazon RDS:

Add Dependencies - Include AWS RDS SDK dependency and database drivers
Create RDS Client - Instantiate RdsClient with proper region and credentials
Create DB Instance - Use createDBInstance() with appropriate configuration
Configure Security - Set up VPC security groups and encryption
Set Up Backups - Configure automated backup windows and retention
Monitor Status - Use describeDBInstances() to check instance state
Create Snapshots - Take manual snapshots before major changes
Handle Failover - Configure Multi-AZ for high availability
Getting Started
RDS Client Setup

The RdsClient is the main entry point for interacting with Amazon RDS.

Basic Client Creation:

import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.rds.RdsClient;

RdsClient rdsClient = RdsClient.builder()
    .region(Region.US_EAST_1)
    .build();

// Use client
describeInstances(rdsClient);

// Always close the client
rdsClient.close();


Client with Custom Configuration:

import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;

RdsClient rdsClient = RdsClient.builder()
    .region(Region.US_WEST_2)
    .credentialsProvider(ProfileCredentialsProvider.create("myprofile"))
    .httpClient(ApacheHttpClient.builder()
        .connectionTimeout(Duration.ofSeconds(30))
        .socketTimeout(Duration.ofSeconds(60))
        .build())
    .build();

Describing DB Instances
DescribeDbInstancesResponse response = rdsClient.describeDBInstances();
for (DBInstance instance : response.dbInstances()) {
    System.out.println(instance.dbInstanceArn() + " - " + instance.dbInstanceStatus());
}

Key Operations
Creating DB Instances
CreateDbInstanceRequest request = CreateDbInstanceRequest.builder()
    .dbInstanceIdentifier(dbInstanceIdentifier)
    .dbName(dbName)
    .engine("postgres")
    .engineVersion("15.4")
    .dbInstanceClass("db.t3.micro")
    .allocatedStorage(20)
    .masterUsername(masterUsername)
    .masterUserPassword(masterPassword)
    .publiclyAccessible(false)
    .build();

CreateDbInstanceResponse response = rdsClient.createDBInstance(request);

// VALIDATION CHECKPOINT: Wait for instance to be available
rdsClient.waiter().waitUntilDBInstanceAvailable(
    DescribeDbInstancesRequest.builder().dbInstanceIdentifier(dbInstanceIdentifier).build()
);
System.out.println("Instance " + dbInstanceIdentifier + " is available!");

Managing DB Parameter Groups
CreateDbParameterGroupRequest request = CreateDbParameterGroupRequest.builder()
    .dbParameterGroupName(groupName)
    .dbParameterGroupFamily("postgres15")
    .description(description)
    .build();
rdsClient.createDBParameterGroup(request);

Managing DB Snapshots
CreateDbSnapshotRequest request = CreateDbSnapshotRequest.builder()
    .dbInstanceIdentifier(dbInstanceIdentifier)
    .dbSnapshotIdentifier(snapshotIdentifier)
    .build();
CreateDbSnapshotResponse response = rdsClient.createDBSnapshot(request);

Integration Patterns
Spring Boot Integration

Refer to references/spring-boot-integration.md for complete Spring Boot integration examples including:

Spring Boot configuration with application properties
RDS client bean configuration
Service layer implementation
REST controller design
Exception handling
Testing strategies
Lambda Integration

Refer to references/lambda-integration.md for Lambda integration examples including:

Traditional Lambda + RDS connections
Lambda with connection pooling
Using AWS Secrets Manager for credentials
Lambda with AWS SDK for RDS management
Security configuration and best practices
Advanced Operations
Modifying DB Instances
ModifyDbInstanceRequest request = ModifyDbInstanceRequest.builder()
    .dbInstanceIdentifier(dbInstanceIdentifier)
    .dbInstanceClass(newInstanceClass)
    .applyImmediately(false)
    .build();
rdsClient.modifyDBInstance(request);

Deleting DB Instances
// VALIDATION CHECKPOINT: Verify instance exists and check status
DBInstance instance = rdsClient.describeDBInstances(
    DescribeDbInstancesRequest.builder().dbInstanceIdentifier(dbInstanceIdentifier).build()
).dbInstances().get(0);

if ("available".equals(instance.dbInstanceStatus())) {
    DeleteDbInstanceRequest request = DeleteDbInstanceRequest.builder()
        .dbInstanceIdentifier(dbInstanceIdentifier)
        .skipFinalSnapshot(false)
        .finalDBSnapshotIdentifier(snapshotId)
        .build();
    rdsClient.deleteDBInstance(request);
}

Examples
Complete RDS Instance Creation with Validation
public String createSecurePostgreSQLInstance(RdsClient rdsClient,
                                            String instanceIdentifier,
                                            String dbName,
                                            String masterUsername,
                                            String masterPassword,
                                            String vpcSecurityGroupId) {
    // Create instance with security settings
    CreateDbInstanceRequest request = CreateDbInstanceRequest.builder()
        .dbInstanceIdentifier(instanceIdentifier)
        .dbName(dbName)
        .masterUsername(masterUsername)
        .masterUserPassword(masterPassword)
        .engine("postgres")
        .engineVersion("15.4")
        .dbInstanceClass("db.t3.micro")
        .allocatedStorage(20)
        .storageEncrypted(true)
        .vpcSecurityGroupIds(vpcSecurityGroupId)
        .publiclyAccessible(false)
        .multiAZ(true)
        .backupRetentionPeriod(7)
        .deletionProtection(true)
        .build();

    rdsClient.createDBInstance(request);

    // VALIDATION: Wait for instance availability
    rdsClient.waiter().waitUntilDBInstanceAvailable(
        DescribeDbInstancesRequest.builder().dbInstanceIdentifier(instanceIdentifier).build()
    );
    System.out.println("Instance " + instanceIdentifier + " is available!");
    return instanceIdentifier;
}

Best Practices

Security: Enable encryption (storageEncrypted=true), use VPC security groups, disable public access.

High Availability: Enable Multi-AZ for production workloads.

Backups: Configure automated backups with 7+ day retention.

Deletion Protection: Enable deletionProtection(true) for production databases.

Resource Management: Always close clients with try-with-resources:

try (RdsClient rdsClient = RdsClient.builder().region(Region.US_EAST_1).build()) {
    // Use client
}

Dependencies
<dependency>
    <groupId>software.amazon.awssdk</groupId>
    <artifactId>rds</artifactId>
    <version>2.20.0</version>
</dependency>
<dependency>
    <groupId>org.postgresql</groupId>
    <artifactId>postgresql</artifactId>
    <version>42.6.0</version>
</dependency>

Reference Documentation

For detailed API reference, see:

API Reference - Complete API documentation and data models
Spring Boot Integration - Spring Boot patterns and examples
Lambda Integration - Lambda function patterns and best practices
Error Handling

See API Reference for comprehensive error handling patterns including common exceptions, error response structure, and pagination support.

Constraints and Warnings
Instance Limits: Account limits on DB instances per region
Multi-AZ Costs: Approximately doubles compute costs
Snapshot Costs: Manual snapshots billed per storage used
Deletion Protection: Cannot delete instances with protection enabled
Maintenance Windows: Instances may be unavailable during updates
Weekly Installs
682
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