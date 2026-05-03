---
rating: ⭐⭐
title: java-spring-boot
url: https://skills.sh/pluginagentmarketplace/custom-plugin-java/java-spring-boot
---

# java-spring-boot

skills/pluginagentmarketplace/custom-plugin-java/java-spring-boot
java-spring-boot
Installation
$ npx skills add https://github.com/pluginagentmarketplace/custom-plugin-java --skill java-spring-boot
Summary

Production-ready Spring Boot applications with REST APIs, security, data access, and monitoring.

Covers REST API development with Spring MVC/WebFlux, request validation, and exception handling via @ControllerAdvice
Includes Spring Security configuration for OAuth2, JWT authentication, method-level authorization, and CORS/CSRF protection
Provides Spring Data JPA patterns: repositories, query methods, pagination, auditing, and transaction management
Integrates Actuator for health checks, Micrometer metrics, custom endpoints, and Prometheus monitoring
Supports Spring Boot 3.x with auto-configuration, profiles, bean lifecycle management, and DevTools hot reload
SKILL.md
Java Spring Boot Skill

Build production-ready Spring Boot applications with modern best practices.

Overview

This skill covers Spring Boot development including REST APIs, security configuration, data access, actuator monitoring, and cloud integration. Follows Spring Boot 3.x patterns with emphasis on production readiness.

When to Use This Skill

Use when you need to:

Create REST APIs with Spring MVC/WebFlux
Configure Spring Security (OAuth2, JWT)
Set up database access with Spring Data
Enable monitoring with Actuator
Integrate with Spring Cloud
Topics Covered
Spring Boot Core
Auto-configuration and starters
Application properties and profiles
Bean lifecycle and configuration
DevTools and hot reload
REST API Development
@RestController and @RequestMapping
Request/response handling
Validation with Bean Validation
Exception handling with @ControllerAdvice
Spring Security
SecurityFilterChain configuration
OAuth2 and JWT authentication
Method security (@PreAuthorize)
CORS and CSRF configuration
Spring Data JPA
Repository pattern
Query methods and @Query
Pagination and sorting
Auditing and transactions
Actuator & Monitoring
Health checks and probes
Metrics with Micrometer
Custom endpoints
Prometheus integration
Quick Reference
// REST Controller
@RestController
@RequestMapping("/api/users")
@Validated
public class UserController {

    @GetMapping("/{id}")
    public ResponseEntity<User> getUser(@PathVariable Long id) {
        return userService.findById(id)
            .map(ResponseEntity::ok)
            .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    public ResponseEntity<User> createUser(@Valid @RequestBody UserRequest request) {
        User user = userService.create(request);
        URI location = URI.create("/api/users/" + user.getId());
        return ResponseEntity.created(location).body(user);
    }
}

// Security Configuration
@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        return http
            .csrf(csrf -> csrf.disable())
            .sessionManagement(s -> s.sessionCreationPolicy(STATELESS))
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/actuator/health/**").permitAll()
                .requestMatchers("/api/public/**").permitAll()
                .anyRequest().authenticated())
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(Customizer.withDefaults()))
            .build();
    }
}

// Exception Handler
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(EntityNotFoundException.class)
    public ProblemDetail handleNotFound(EntityNotFoundException ex) {
        return ProblemDetail.forStatusAndDetail(NOT_FOUND, ex.getMessage());
    }
}

Configuration Templates
# application.yml
spring:
  application:
    name: ${APP_NAME:my-service}
  profiles:
    active: ${SPRING_PROFILES_ACTIVE:local}
  jpa:
    open-in-view: false
    properties:
      hibernate:
        jdbc.batch_size: 50

management:
  endpoints:
    web:
      exposure:
        include: health,info,metrics,prometheus
  endpoint:
    health:
      probes:
        enabled: true

server:
  error:
    include-stacktrace: never

Common Patterns
Layer Architecture
Controller → Service → Repository → Database
     ↓           ↓          ↓
   DTOs      Entities    Entities

Validation Patterns
public record CreateUserRequest(
    @NotBlank @Size(max = 100) String name,
    @Email @NotBlank String email,
    @NotNull @Min(18) Integer age
) {}

Troubleshooting
Common Issues
Problem	Cause	Solution
Bean not found	Missing @Component	Add annotation or @Bean
Circular dependency	Constructor injection	Use @Lazy or refactor
401 Unauthorized	Security config	Check permitAll paths
Slow startup	Heavy auto-config	Exclude unused starters
Debug Properties
debug=true
logging.level.org.springframework.security=DEBUG
spring.jpa.show-sql=true

Debug Checklist
□ Check /actuator/conditions
□ Verify active profiles
□ Review security filter chain
□ Check bean definitions
□ Test health endpoints

Usage
Skill("java-spring-boot")

Related Skills
java-testing - Spring test patterns
java-jpa-hibernate - Data access
Weekly Installs
10.5K
Repository
pluginagentmark…gin-java
GitHub Stars
34
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass