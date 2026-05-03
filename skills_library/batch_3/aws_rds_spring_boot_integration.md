---
title: aws-rds-spring-boot-integration
url: https://skills.sh/giuseppe-trisciuoglio/developer-kit/aws-rds-spring-boot-integration
---

# aws-rds-spring-boot-integration

skills/giuseppe-trisciuoglio/developer-kit/aws-rds-spring-boot-integration
aws-rds-spring-boot-integration
Installation
$ npx skills add https://github.com/giuseppe-trisciuoglio/developer-kit --skill aws-rds-spring-boot-integration
Summary

Production-ready AWS RDS configuration patterns for Spring Boot applications with Aurora, MySQL, and PostgreSQL.

Supports Aurora MySQL, Aurora PostgreSQL, and standard MySQL/PostgreSQL with datasource configuration, HikariCP connection pooling, and SSL encryption
Includes environment-specific profiles (dev/prod), Flyway database migrations, and read/write endpoint splitting for read-heavy workloads
Provides security patterns using environment variables and AWS Secrets Manager integration for credential management
Covers connection pool optimization, failover handling, monitoring setup, and health check endpoints for production deployments
SKILL.md
AWS RDS Spring Boot Integration
Overview

Configure AWS RDS databases (Aurora, MySQL, PostgreSQL) with Spring Boot applications. Provides patterns for datasource configuration, HikariCP connection pooling, SSL connections, environment-specific configurations, and AWS Secrets Manager integration.

When to Use

Use when configuring HikariCP connection pools for RDS workloads, implementing read/write split with Aurora replicas, setting up IAM database authentication, enabling SSL/TLS connections, managing database migrations with Flyway, or troubleshooting RDS connectivity issues.

Instructions

Follow these steps to configure AWS RDS with Spring Boot:

Add Dependencies — Include Spring Data JPA, database driver (MySQL/PostgreSQL), and Flyway

Configure Datasource — Set connection properties in application.yml

Configure HikariCP — Optimize pool settings for your RDS workload

Set Up SSL — Enable encrypted connections to RDS

Configure Profiles — Set environment-specific configurations (dev/prod)

Add Migrations — Create Flyway scripts for schema management

Validate Connectivity — Run health check to verify database connection

If validation fails: Check security group rules, verify credentials, ensure RDS is accessible from your network, and confirm SSL certificate configuration.

Run Migrations — Apply Flyway migrations only after connectivity validation passes

Quick Start
Step 1: Add Dependencies

Maven (pom.xml):

<dependencies>
    <!-- Spring Data JPA -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-jpa</artifactId>
    </dependency>

    <!-- Aurora MySQL Driver -->
    <dependency>
        <groupId>com.mysql</groupId>
        <artifactId>mysql-connector-j</artifactId>
        <version>8.2.0</version>
        <scope>runtime</scope>
    </dependency>

    <!-- Aurora PostgreSQL Driver (alternative) -->
    <dependency>
        <groupId>org.postgresql</groupId>
        <artifactId>postgresql</artifactId>
        <scope>runtime</scope>
    </dependency>

    <!-- Flyway for database migrations -->
    <dependency>
        <groupId>org.flywaydb</groupId>
        <artifactId>flyway-core</artifactId>
    </dependency>

    <!-- Validation -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-validation</artifactId>
    </dependency>
</dependencies>


Gradle (build.gradle):

dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-data-jpa'
    implementation 'org.springframework.boot:spring-boot-starter-validation'

    // Aurora MySQL
    runtimeOnly 'com.mysql:mysql-connector-j:8.2.0'

    // Aurora PostgreSQL (alternative)
    runtimeOnly 'org.postgresql:postgresql'

    // Flyway
    implementation 'org.flywaydb:flyway-core'
}

Step 2: Basic Datasource Configuration

Use the configuration in the Examples section below. For PostgreSQL, change:

Driver: org.postgresql.Driver
URL: jdbc:postgresql://... with ?ssl=true&sslmode=require
Dialect: org.hibernate.dialect.PostgreSQLDialect
Step 3: Set Up Environment Variables
# Production environment variables
export DB_PASSWORD=YourStrongPassword123!
export SPRING_PROFILES_ACTIVE=prod

# For development
export SPRING_PROFILES_ACTIVE=dev

Database Migration Setup

Create migration files for Flyway:

src/main/resources/db/migration/
├── V1__create_users_table.sql
├── V2__add_phone_column.sql
└── V3__create_orders_table.sql


V1__create_users_table.sql:

CREATE TABLE users (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_email (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

Examples
Example 1: Aurora MySQL Configuration
spring:
  datasource:
    url: jdbc:mysql://myapp-aurora-cluster.cluster-abc123xyz.us-east-1.rds.amazonaws.com:3306/devops
    username: admin
    password: ${DB_PASSWORD}
    driver-class-name: com.mysql.cj.jdbc.Driver
    hikari:
      maximum-pool-size: 20
      minimum-idle: 5
      connection-timeout: 20000
  jpa:
    hibernate:
      ddl-auto: validate
    open-in-view: false

Example 2: Aurora PostgreSQL with SSL
spring.datasource.url=jdbc:postgresql://myapp-aurora-pg-cluster.cluster-abc123xyz.us-east-1.rds.amazonaws.com:5432/devops?ssl=true&sslmode=require
spring.datasource.username=${DB_USERNAME}
spring.datasource.password=${DB_PASSWORD}
spring.datasource.hikari.maximum-pool-size=30
spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.PostgreSQLDialect

Example 3: Read/Write Split Configuration
@Configuration
public class DataSourceConfiguration {

    @Bean
    @Primary
    public DataSource dataSource(
            @Qualifier("writerDataSource") DataSource writerDataSource,
            @Qualifier("readerDataSource") DataSource readerDataSource) {
        Map<Object, Object> targetDataSources = new HashMap<>();
        targetDataSources.put("writer", writerDataSource);
        targetDataSources.put("reader", readerDataSource);

        RoutingDataSource routingDataSource = new RoutingDataSource();
        routingDataSource.setTargetDataSources(targetDataSources);
        routingDataSource.setDefaultTargetDataSource(writerDataSource);

        return routingDataSource;
    }
}

Constraints and Warnings
HikariCP pool size must respect RDS instance connection limits
Security groups must allow traffic from your application's IP range
Use AWS Secrets Manager instead of hardcoding credentials
Enable storage autoscaling to prevent storage exhaustion
Best Practices
HikariCP: Enable leak detection and configure timeouts for failover scenarios
Security: Enable SSL/TLS; use IAM Database Authentication when possible
Performance: Disable open-in-view; use appropriate indexing and batch operations
Monitoring: Enable Spring Boot Actuator with database health checks
Testing

Verify connectivity with this health check endpoint:

@RestController
@RequestMapping("/api/health")
public class DatabaseHealthController {
    @Autowired
    private DataSource dataSource;

    @GetMapping("/db-connection")
    public ResponseEntity<Map<String, Object>> testDatabaseConnection() {
        Map<String, Object> response = new HashMap<>();
        try (Connection connection = dataSource.getConnection()) {
            response.put("status", "success");
            response.put("database", connection.getCatalog());
            response.put("connected", true);
            return ResponseEntity.ok(response);
        } catch (Exception e) {
            response.put("status", "failed");
            response.put("error", e.getMessage());
            response.put("connected", false);
            return ResponseEntity.status(HttpStatus.SERVICE_UNAVAILABLE).body(response);
        }
    }
}

curl http://localhost:8080/api/health/db-connection

Support

For detailed troubleshooting and advanced configuration, refer to:

AWS RDS Aurora Advanced Configuration
AWS RDS Aurora Troubleshooting Guide
AWS RDS Aurora documentation
Spring Boot Data RDS Aurora documentation
Weekly Installs
691
Repository
giuseppe-trisci…oper-kit
GitHub Stars
233
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail