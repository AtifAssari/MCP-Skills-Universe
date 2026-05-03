---
rating: ⭐⭐
title: spring-data-jdbc
url: https://skills.sh/claude-dev-suite/claude-dev-suite/spring-data-jdbc
---

# spring-data-jdbc

skills/claude-dev-suite/claude-dev-suite/spring-data-jdbc
spring-data-jdbc
Installation
$ npx skills add https://github.com/claude-dev-suite/claude-dev-suite --skill spring-data-jdbc
SKILL.md
Spring Data JDBC - Quick Reference

Full Reference: See advanced.md for custom row mappers, ID generation, auditing, event listeners, and Testcontainers integration.

Deep Knowledge: Use mcp__documentation__fetch_docs with technology: spring-data-jdbc for comprehensive documentation.

Why Spring Data JDBC over JPA?
Spring Data JDBC	Spring Data JPA
No lazy loading	Lazy loading
No dirty checking	Auto dirty checking
No session/cache	First-level cache
Explicit SQL	Generated SQL
Fast startup	Slower startup
Dependencies
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jdbc</artifactId>
</dependency>

Entity Mapping
@Table("users")
public class User {
    @Id
    private Long id;
    private String username;
    private String email;

    @Column("created_at")
    private LocalDateTime createdAt;
}

Aggregate Design
@Table("orders")
public class Order {
    @Id
    private Long id;
    private Long customerId;  // Reference by ID, not entity
    private OrderStatus status;

    @MappedCollection(idColumn = "order_id")
    private Set<OrderItem> items = new HashSet<>();

    public void addItem(Long productId, int quantity, BigDecimal price) {
        items.add(new OrderItem(productId, quantity, price));
    }

    public BigDecimal getTotal() {
        return items.stream()
            .map(OrderItem::getSubtotal)
            .reduce(BigDecimal.ZERO, BigDecimal::add);
    }
}

// Aggregate member (no @Id - lifecycle managed by root)
public class OrderItem {
    private Long productId;
    private int quantity;
    private BigDecimal unitPrice;

    public BigDecimal getSubtotal() {
        return unitPrice.multiply(BigDecimal.valueOf(quantity));
    }
}

Repository Pattern
public interface OrderRepository extends CrudRepository<Order, Long> {

    List<Order> findByCustomerId(Long customerId);
    List<Order> findByStatus(OrderStatus status);

    @Query("SELECT * FROM orders WHERE status = :status ORDER BY created_at DESC LIMIT :limit")
    List<Order> findRecentByStatus(OrderStatus status, int limit);

    @Modifying
    @Query("UPDATE orders SET status = :newStatus WHERE status = :oldStatus AND created_at < :before")
    int updateOldOrders(OrderStatus oldStatus, OrderStatus newStatus, LocalDateTime before);

    boolean existsByCustomerIdAndStatus(Long customerId, OrderStatus status);
}

Schema
CREATE TABLE orders (
    id BIGSERIAL PRIMARY KEY,
    customer_id BIGINT NOT NULL,
    status VARCHAR(50) NOT NULL
);

CREATE TABLE order_item (
    order_id BIGINT NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
    product_id BIGINT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL
);

When NOT to Use This Skill
Need lazy loading - Use spring-data-jpa for complex entity graphs
Reactive applications - Use spring-r2dbc for non-blocking access
Complex ORM features - Use JPA for second-level cache, dirty checking
Anti-Patterns
Anti-Pattern	Problem	Solution
JPA-style entity graphs	Not supported	Design proper aggregates
Embedding other aggregates	Coupling	Reference by ID only
Large aggregates	Performance issues	Keep aggregates small
Missing CASCADE on FK	Orphan records	Add ON DELETE CASCADE
Quick Troubleshooting
Problem	Diagnostic	Fix
Entity not saved	Check @Id generation	Configure ID callback or auto-increment
Children not persisted	Check @MappedCollection	Add idColumn properly
Column not mapped	Check naming	Use @Column for custom names
Transaction not working	Check @Transactional	Ensure Spring proxy
Best Practices
Do	Don't
Design proper aggregates	Use JPA-style entity graphs
Reference other aggregates by ID	Embed other aggregate roots
Keep aggregates small	Create huge aggregate graphs
Use immutable value objects	Mutate embedded objects directly
Production Checklist
 Aggregate boundaries defined
 Schema matches entity mapping
 Indexes on query columns
 Foreign keys with CASCADE
 Transaction boundaries clear
 Connection pool configured
Reference Documentation
Spring Data JDBC Reference
Weekly Installs
29
Repository
claude-dev-suit…ev-suite
GitHub Stars
12
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass