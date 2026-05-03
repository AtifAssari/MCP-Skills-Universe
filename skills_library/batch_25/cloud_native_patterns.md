---
title: cloud-native-patterns
url: https://skills.sh/nguyenhuuca/assessment/cloud-native-patterns
---

# cloud-native-patterns

skills/nguyenhuuca/assessment/cloud-native-patterns
cloud-native-patterns
Installation
$ npx skills add https://github.com/nguyenhuuca/assessment --skill cloud-native-patterns
SKILL.md
Cloud-Native Patterns
Twelve-Factor App
Codebase: One codebase, many deploys
Dependencies: Explicitly declare and isolate
Config: Store in environment
Backing Services: Treat as attached resources
Build, Release, Run: Strictly separate stages
Processes: Execute as stateless processes
Port Binding: Export services via port
Concurrency: Scale out via process model
Disposability: Fast startup and graceful shutdown
Dev/Prod Parity: Keep environments similar
Logs: Treat as event streams
Admin Processes: Run as one-off processes
Resilience Patterns
Circuit Breaker (Resilience4j + Spring Boot)

Prevent cascading failures by failing fast.

// Add dependency: io.github.resilience4j:resilience4j-spring-boot3

// Configuration
@Configuration
public class ResilienceConfig {
    @Bean
    public CircuitBreakerConfig circuitBreakerConfig() {
        return CircuitBreakerConfig.custom()
            .failureRateThreshold(50)
            .waitDurationInOpenState(Duration.ofSeconds(30))
            .slidingWindowSize(10)
            .build();
    }
}

// Service with circuit breaker
@Service
public class ExternalApiService {
    private final RestTemplate restTemplate;
    private final CircuitBreaker circuitBreaker;

    @CircuitBreaker(name = "externalApi", fallbackMethod = "fallback")
    public String callExternalApi(String request) {
        return restTemplate.getForObject(
            "https://api.example.com/data",
            String.class
        );
    }

    private String fallback(String request, Exception ex) {
        return "Fallback response: Service unavailable";
    }
}

Retry with Backoff (Resilience4j)
// Configuration
@Configuration
public class RetryConfig {
    @Bean
    public io.github.resilience4j.retry.RetryConfig retryConfig() {
        return io.github.resilience4j.retry.RetryConfig.custom()
            .maxAttempts(3)
            .waitDuration(Duration.ofSeconds(1))
            .retryExceptions(IOException.class, TimeoutException.class)
            .ignoreExceptions(BusinessException.class)
            .build();
    }
}

// Service with retry
@Service
public class DataService {
    @Retry(name = "dataService", fallbackMethod = "fallback")
    public Data fetchData(Long id) {
        // May throw transient exceptions
        return externalDataSource.fetch(id);
    }

    private Data fallback(Long id, Exception ex) {
        // Return cached or default value
        return Data.defaultValue();
    }
}

// Spring Retry alternative (simpler)
@Retryable(
    value = {RemoteAccessException.class},
    maxAttempts = 3,
    backoff = @Backoff(delay = 1000, multiplier = 2)
)
public String callRemoteService() {
    return restTemplate.getForObject(url, String.class);
}

Bulkhead

Isolate failures to prevent system-wide impact.

Service Communication
Synchronous
REST/HTTP
gRPC
Asynchronous
Message queues (RabbitMQ, SQS)
Event streaming (Kafka)
Health Checks (Spring Boot Actuator)
// Add dependency: spring-boot-starter-actuator

// application.yaml
management:
  endpoints:
    web:
      exposure:
        include: health,info,metrics
  endpoint:
    health:
      show-details: always
  health:
    readiness-state:
      enabled: true
    liveness-state:
      enabled: true

// Built-in endpoints
// GET /actuator/health - Overall health
// GET /actuator/health/liveness - Kubernetes liveness probe
// GET /actuator/health/readiness - Kubernetes readiness probe

// Custom health indicator
@Component
public class DatabaseHealthIndicator implements HealthIndicator {
    private final DataSource dataSource;

    @Override
    public Health health() {
        try (Connection conn = dataSource.getConnection()) {
            if (conn.isValid(1000)) {
                return Health.up()
                    .withDetail("database", "PostgreSQL")
                    .withDetail("status", "reachable")
                    .build();
            }
        } catch (Exception e) {
            return Health.down()
                .withException(e)
                .build();
        }
        return Health.down().build();
    }
}

// Custom readiness check
@Component
public class CacheReadinessIndicator implements HealthIndicator {
    private final CacheManager cacheManager;

    @Override
    public Health health() {
        try {
            // Test cache connectivity
            boolean cacheHealthy = testCache();
            if (cacheHealthy) {
                return Health.up().build();
            }
        } catch (Exception e) {
            return Health.down().withException(e).build();
        }
        return Health.down().build();
    }
}

Container Best Practices
One process per container
Use multi-stage builds
Run as non-root user
Use health checks
Keep images small
Weekly Installs
12
Repository
nguyenhuuca/assessment
GitHub Stars
24
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass