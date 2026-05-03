---
title: spring-data-jpa
url: https://skills.sh/giuseppe-trisciuoglio/developer-kit/spring-data-jpa
---

# spring-data-jpa

skills/giuseppe-trisciuoglio/developer-kit/spring-data-jpa
spring-data-jpa
Installation
$ npx skills add https://github.com/giuseppe-trisciuoglio/developer-kit --skill spring-data-jpa
Summary

Persistence layer patterns for Spring Data JPA repositories, entities, queries, and advanced features.

Create repository interfaces extending JpaRepository with derived queries, custom @Query methods, and automatic CRUD operations
Configure entity relationships (one-to-one, one-to-many, many-to-many) with appropriate cascade types and fetch strategies
Implement pagination, sorting, database auditing with timestamps and user tracking, and transaction management
Optimize performance using database indexes, @EntityGraph to prevent N+1 queries, and proper fetch strategies (LAZY vs EAGER)
Support UUID primary keys, multiple database configurations, and read-only transaction annotations for query optimization
SKILL.md
Spring Data JPA
Overview

Provides patterns for Spring Data JPA repositories, entity relationships, queries, pagination, auditing, and transactions.

When to Use

Creating repositories with CRUD operations, entity relationships, @Query annotations, pagination, auditing, or UUID primary keys.

Instructions
Create Repository Interfaces

To implement a repository interface:

Extend the appropriate repository interface:

@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    // Custom methods defined here
}


Use derived queries for simple conditions:

Optional<User> findByEmail(String email);
List<User> findByStatusOrderByCreatedDateDesc(String status);


Implement custom queries with @Query:

@Query("SELECT u FROM User u WHERE u.status = :status")
List<User> findActiveUsers(@Param("status") String status);

Configure Entities

Define entities with proper annotations:

@Entity
@Table(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, length = 100)
    private String email;
}


Configure relationships using appropriate cascade types:

@OneToMany(mappedBy = "user", cascade = CascadeType.ALL, orphanRemoval = true)
private List<Order> orders = new ArrayList<>();


Validation: Test cascade behavior with a small dataset before applying to production data. Verify delete operations don't cascade unexpectedly.

Set up database auditing:

@CreatedDate
@Column(nullable = false, updatable = false)
private LocalDateTime createdDate;

Apply Query Patterns
Use derived queries for simple conditions
Use @Query for complex queries
Return Optional for single results
Use Pageable for pagination
Apply @Modifying for update/delete operations
Manage Transactions
Mark read-only operations with @Transactional(readOnly = true)
Use explicit transaction boundaries for modifying operations
Specify rollback conditions when needed
Validate and Optimize

1. Verify entity configuration:

Test cascade behavior in a transaction before production deployment
Validate bidirectional relationships sync correctly

2. Optimize query performance:

Run EXPLAIN ANALYZE on queries against large tables
If performance issues detected: add indexes → verify with EXPLAIN → repeat
Use @EntityGraph to prevent N+1 queries

3. Validate pagination:

Ensure indexed columns support pagination queries
Test with large datasets to verify cursor stability
Examples
Basic CRUD Repository
@Repository
public interface ProductRepository extends JpaRepository<Product, Long> {
    // Derived query
    List<Product> findByCategory(String category);

    // Custom query
    @Query("SELECT p FROM Product p WHERE p.price > :minPrice")
    List<Product> findExpensiveProducts(@Param("minPrice") BigDecimal minPrice);
}

Pagination Implementation
@Service
public class ProductService {
    private final ProductRepository repository;

    public Page<Product> getProducts(int page, int size) {
        Pageable pageable = PageRequest.of(page, size, Sort.by("name").ascending());
        return repository.findAll(pageable);
    }
}

Entity with Auditing
@Entity
@EntityListeners(AuditingEntityListener.class)
public class Order {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @CreatedDate
    @Column(nullable = false, updatable = false)
    private LocalDateTime createdDate;

    @LastModifiedDate
    private LocalDateTime lastModifiedDate;

    @CreatedBy
    @Column(nullable = false, updatable = false)
    private String createdBy;
}

Best Practices
Entity Design
Use constructor injection exclusively (never field injection)
Prefer immutable fields with final modifiers
Use Java records (16+) or @Value for DTOs
Always provide proper @Id and @GeneratedValue annotations
Use explicit @Table and @Column annotations
Performance Optimization
Use appropriate fetch strategies (LAZY vs EAGER)
Implement pagination for large datasets
Use database indexes for frequently queried fields
Consider using @EntityGraph to avoid N+1 query problems
Reference Documentation

For comprehensive examples, detailed patterns, and advanced configurations, see:

Examples - Complete code examples for common scenarios
Reference - Detailed patterns and advanced configurations
Constraints and Warnings
Never expose JPA entities directly in REST APIs; always use DTOs to prevent lazy loading issues.
Avoid N+1 query problems by using @EntityGraph or JOIN FETCH in queries.
Be cautious with CascadeType.REMOVE on large collections as it can cause performance issues.
Do not use EAGER fetch type for collections; it can cause excessive database queries.
Avoid long-running transactions as they can cause database lock contention.
Use @Transactional(readOnly = true) for read operations to enable optimizations.
Be aware of the first-level cache; entities may not reflect database changes within the same transaction.
UUID primary keys can cause index fragmentation; consider using sequential UUIDs or Long IDs.
Pagination on large datasets requires proper indexing to avoid full table scans.
Weekly Installs
835
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