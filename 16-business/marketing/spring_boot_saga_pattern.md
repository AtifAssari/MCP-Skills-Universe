---
rating: ⭐⭐
title: spring-boot-saga-pattern
url: https://skills.sh/giuseppe-trisciuoglio/developer-kit/spring-boot-saga-pattern
---

# spring-boot-saga-pattern

skills/giuseppe-trisciuoglio/developer-kit/spring-boot-saga-pattern
spring-boot-saga-pattern
Installation
$ npx skills add https://github.com/giuseppe-trisciuoglio/developer-kit --skill spring-boot-saga-pattern
Summary

Distributed transaction management across microservices using choreography or orchestration patterns.

Supports two saga approaches: choreography-based (event-driven, decoupled) and orchestration-based (centralized coordinator with easier tracking)
Requires compensating transactions for every forward operation to ensure rollback capability and eventual consistency
Integrates with Spring Boot 3.x, Kafka, RabbitMQ, and frameworks like Axon Framework, Eventuate Tram, and Camunda
Emphasizes idempotent operations, persistent saga state, timeout handling, and dead-letter queues for failure scenarios
Includes monitoring, distributed tracing, and testing strategies for complex multi-service workflows
SKILL.md
Spring Boot Saga Pattern
Overview

Implements distributed transactions across microservices using the Saga Pattern. Replaces two-phase commit with a sequence of local transactions and compensating actions. Supports choreography (event-driven) and orchestration (centralized coordinator) approaches with Kafka, RabbitMQ, or Axon Framework.

When to Use
Building distributed transactions across multiple microservices
Replacing two-phase commit (2PC) with a more scalable solution
Handling transaction rollback when a service fails
Ensuring eventual consistency in microservices architecture
Implementing compensating transactions for failed operations
Coordinating complex business processes spanning multiple services

Trigger phrases: distributed transactions, saga pattern, compensating transactions, microservices transaction, eventual consistency, rollback across services, orchestration pattern, choreography pattern

Instructions
1. Design Transaction Flow

Map the sequence of operations and their compensating transactions:

Order → Payment → Inventory → Shipment
  ↓        ↓        ↓          ↓
Cancel  Refund   Release    Cancel


Validation: Verify every forward step has a corresponding compensation.

2. Choose Implementation Approach
Approach	Use Case	Stack
Choreography	Greenfield, few participants	Spring Cloud Stream + Kafka/RabbitMQ
Orchestration	Complex workflows, brownfield	Axon Framework, Eventuate Tram, Camunda

Validation: Review team expertise and system complexity before choosing.

3. Implement Services with Local Transactions

Each service completes its local ACID transaction atomically:

@Service
@RequiredArgsConstructor
public class OrderService {
    private final OrderRepository orderRepository;
    private final KafkaTemplate<String, Object> kafka;

    @Transactional
    public Order createOrder(CreateOrderCommand cmd) {
        Order order = orderRepository.save(new Order(cmd.orderId(), cmd.items()));
        kafka.send("order.created", new OrderCreatedEvent(order.getId(), order.getItems()));
        return order;
    }
}


Validation: Test that local transaction commits before event is published.

4. Implement Compensating Transactions

Every forward operation requires an idempotent compensation:

@Service
@RequiredArgsConstructor
public class PaymentService {
    private final PaymentRepository paymentRepository;
    private final KafkaTemplate<String, Object> kafka;

    public void processPayment(PaymentRequest request) {
        Payment payment = paymentRepository.save(new Payment(request.orderId(), request.amount()));
        kafka.send("payment.processed", new PaymentProcessedEvent(payment.getId(), request.orderId()));
    }

    @Transactional
    public void refundPayment(String paymentId) {
        paymentRepository.findById(paymentId)
            .ifPresent(p -> {
                p.setStatus(REFUNDED);
                paymentRepository.save(p);
                kafka.send("payment.refunded", new PaymentRefundedEvent(paymentId));
            });
    }
}


Validation: Confirm compensation can execute safely multiple times (idempotency).

5. Set Up Message Broker

Configure Kafka with idempotent consumers:

@Configuration
@EnableKafka
public class KafkaConfig {
    @Bean
    public ConcurrentKafkaListenerContainerFactory<String, Object> kafkaListenerContainerFactory(
            ConsumerFactory<String, Object> consumerFactory) {
        ConcurrentKafkaListenerContainerFactory<String, Object> factory =
            new ConcurrentKafkaListenerContainerFactory<>();
        factory.setConsumerFactory(consumerFactory);
        factory.setCommonErrorHandler(new DefaultErrorHandler());
        return factory;
    }
}


Validation: Enable transactional ID and verify exactly-once semantics.

6. Implement Saga Orchestrator (Orchestration Only)
@Service
@RequiredArgsConstructor
public class OrderSagaOrchestrator {
    private final KafkaTemplate<String, Object> kafka;
    private final SagaStateRepository sagaStateRepo;

    public void startSaga(OrderRequest request) {
        String sagaId = UUID.randomUUID().toString();
        sagaStateRepo.save(new SagaState(sagaId, STARTED, LocalDateTime.now()));
        kafka.send("saga.order.start", new StartOrderSagaCommand(sagaId, request));
    }

    @KafkaListener(topics = "payment.failed")
    public void handlePaymentFailed(PaymentFailedEvent event) {
        kafka.send("order.compensate", new CompensateOrderCommand(event.getSagaId()));
        kafka.send("inventory.compensate", new ReleaseInventoryCommand(event.getSagaId()));
        sagaStateRepo.updateStatus(event.getSagaId(), FAILED);
    }
}


Validation: Verify saga state persists before sending commands. Check compensation triggers on each failure path.

7. Implement Event Handlers (Choreography Only)
@Service
public class OrderEventHandler {
    private final OrderService orderService;
    private final KafkaTemplate<String, Object> kafka;

    @KafkaListener(topics = "payment.processed", groupId = "order-service")
    public void onPaymentProcessed(PaymentProcessedEvent event) {
        try {
            InventoryReservedEvent result = orderService.reserveInventory(event.toInventoryRequest());
            kafka.send("inventory.reserved", result);
        } catch (InsufficientInventoryException e) {
            kafka.send("inventory.insufficient", new InsufficientInventoryEvent(event.getOrderId(), event.getPaymentId()));
        }
    }
}


Validation: Test that each event handler correctly triggers the next step or compensation.

8. Add Monitoring and Observability
@Configuration
public class SagaMetricsConfig {
    @Bean
    public MeterRegistry meterRegistry() {
        return new PrometheusMeterRegistry(PrometheusConfig.DEFAULT);
    }
}


Track: saga execution duration, compensation count, failure rate, stuck sagas.

Validation: Set up alerts for sagas exceeding expected duration.

Best Practices

Design:

Make compensating transactions idempotent using database constraints or deduplication tables
Use immutable events (Java records) to prevent accidental mutation
Store saga state in persistent storage for recovery

Error Handling:

Implement circuit breakers for inter-service calls
Use dead-letter queues for messages exceeding retry limits
Set appropriate timeouts per saga step (30s default, configurable)

Monitoring:

Track saga status: PENDING, COMPLETED, COMPENSATING, FAILED
Monitor compensation execution time
Alert when sagas exceed SLA duration
Constraints and Warnings
Every forward transaction MUST have a corresponding compensating transaction
Compensating transactions MUST be idempotent to handle retry scenarios
Saga state MUST be persisted to handle failures and recovery
Never use synchronous communication between saga participants
Sagas provide eventual consistency, not strong consistency
Test all failure scenarios including partial failures
Consider Axon Framework or Eventuate for complex orchestrations
Ensure message brokers are highly available
Examples
Choreography-Based Saga
// Application.java
@SpringBootApplication
@EnableKafka
@EnableKafkaListeners
public class OrderApplication {
    public static void main(String[] args) {
        SpringApplication.run(OrderApplication.class, args);
    }
}

// Event Classes (immutable)
public record OrderCreatedEvent(String orderId, List<OrderItem> items) {}
public record PaymentProcessedEvent(String paymentId, String orderId) {}
public record InventoryReservedEvent(String reservationId, String orderId) {}
public record PaymentFailedEvent(String orderId, String reason) {}
public record InsufficientInventoryEvent(String orderId, String paymentId) {}

// OrderService with compensation
@Service
@RequiredArgsConstructor
public class OrderService {
    private final OrderRepository orderRepository;
    private final KafkaTemplate<String, Object> kafka;

    @KafkaListener(topics = "payment.failed", groupId = "order-service")
    public void handleCompensation(PaymentFailedEvent event) {
        orderRepository.findByOrderId(event.orderId())
            .ifPresent(order -> {
                order.setStatus(CANCELLED);
                orderRepository.save(order);
            });
    }
}

Orchestration-Based Saga with Axon Framework
// Command
@Aggregate
public class OrderAggregate {
    @AggregateIdentifier
    private String orderId;

    @CommandHandler
    public OrderAggregate(CreateOrderCommand cmd) {
        apply(new OrderCreatedEvent(cmd.orderId(), cmd.items()));
    }

    @EventSourcingHandler
    public void on(OrderCreatedEvent event) {
        this.orderId = event.orderId();
    }

    @CommandHandler
    public void handle(CancelOrderCommand cmd) {
        apply(new OrderCancelledEvent(cmd.orderId(), cmd.reason()));
    }
}

References
Saga Pattern Definition
Choreography Implementation
Orchestration Implementation
Compensating Transactions
State Management
Error Handling and Retry
Testing Strategies
Pitfalls and Solutions
Examples
Weekly Installs
714
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