---
title: domain-driven-design
url: https://skills.sh/nguyenhuuca/assessment/domain-driven-design
---

# domain-driven-design

skills/nguyenhuuca/assessment/domain-driven-design
domain-driven-design
Installation
$ npx skills add https://github.com/nguyenhuuca/assessment --skill domain-driven-design
SKILL.md
Domain-Driven Design
Core Concepts
Ubiquitous Language

Use the same terminology as domain experts. Code should read like business documentation.

Bounded Context

A boundary within which a particular domain model is defined and applicable.

Context Map

Shows how bounded contexts relate to each other.

Building Blocks
Entity

Has identity that persists over time. Equality based on ID.

@Entity
@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true)
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @EqualsAndHashCode.Include
    private Long id;

    @Embedded
    private Email email;

    private String name;

    @Builder.Default
    private Instant createdAt = Instant.now();
}

Value Object

Immutable, equality based on attributes.

@Embeddable
@Value
public class Email {
    private String value;

    private Email(String value) {
        this.value = value;
    }

    public static Email of(String value) {
        if (value == null || !value.contains("@")) {
            throw new IllegalArgumentException("Invalid email");
        }
        return new Email(value);
    }

    // Lombok @Value makes it immutable and generates equals/hashCode
}

Aggregate

Cluster of entities and value objects with a root entity.

@Entity
@Data
public class Order { // Aggregate Root
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @OneToMany(cascade = CascadeType.ALL, orphanRemoval = true)
    @JoinColumn(name = "order_id")
    private List<OrderItem> items = new ArrayList<>();

    private Long userId;

    @Enumerated(EnumType.STRING)
    private OrderStatus status;

    // Business logic in domain model
    public void addItem(Long productId, int quantity) {
        // Business rules enforced here
        if (this.status != OrderStatus.DRAFT) {
            throw new IllegalStateException("Cannot add items to submitted order");
        }
        OrderItem item = OrderItem.builder()
            .productId(productId)
            .quantity(quantity)
            .build();
        this.items.add(item);
    }

    public Money getTotal() {
        return items.stream()
            .map(OrderItem::getSubtotal)
            .reduce(Money.zero(), Money::add);
    }

    public void submit() {
        if (items.isEmpty()) {
            throw new IllegalStateException("Cannot submit empty order");
        }
        this.status = OrderStatus.SUBMITTED;
    }
}

Repository

Abstracts data access for aggregates.

@Repository
public interface OrderRepository extends JpaRepository<Order, Long> {
    Optional<Order> findById(Long id);

    @Query("SELECT o FROM Order o LEFT JOIN FETCH o.items WHERE o.id = :id")
    Optional<Order> findByIdWithItems(@Param("id") Long id);

    List<Order> findByUserIdAndStatus(Long userId, OrderStatus status);
}

Domain Event

Something that happened in the domain.

@Value
@Builder
public class OrderPlaced {
    Long orderId;
    Long userId;
    Instant occurredAt;
}

// Publishing domain events with Spring
@Service
@Transactional
public class OrderService {
    private final OrderRepository orderRepository;
    private final ApplicationEventPublisher eventPublisher;

    public void placeOrder(Long orderId) {
        Order order = orderRepository.findById(orderId)
            .orElseThrow(() -> new OrderNotFoundException(orderId));

        order.submit();
        orderRepository.save(order);

        // Publish domain event
        OrderPlaced event = OrderPlaced.builder()
            .orderId(order.getId())
            .userId(order.getUserId())
            .occurredAt(Instant.now())
            .build();
        eventPublisher.publishEvent(event);
    }
}

// Event listener
@Component
public class OrderEventHandler {
    @EventListener
    @Async
    public void handleOrderPlaced(OrderPlaced event) {
        // Send confirmation email, update inventory, etc.
    }
}

Strategic Patterns
Anti-Corruption Layer

Translate between your model and external systems.

Shared Kernel

Shared subset of domain model between contexts.

Customer-Supplier

Upstream provides what downstream needs.

Weekly Installs
10
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