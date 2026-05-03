---
rating: ⭐⭐
title: mapstruct-patterns
url: https://skills.sh/emvnuel/skill.md/mapstruct-patterns
---

# mapstruct-patterns

skills/emvnuel/skill.md/mapstruct-patterns
mapstruct-patterns
Installation
$ npx skills add https://github.com/emvnuel/skill.md --skill mapstruct-patterns
SKILL.md
MapStruct Patterns for Jakarta EE

Best practices for using MapStruct with constructor-based mapping to achieve compile-time safety. When constructors change, mappings fail to compile — no runtime surprises.

Core Philosophy

Use constructors, not setters. This gives you compile-time errors when fields change.

Records naturally enforce this. For mutable entities, use the @Default annotation.

CDI Setup
@Mapper(componentModel = "cdi")  // CDI injection
public interface OrderMapper {
    OrderResponse toResponse(Order order);
}

The @Default Annotation Trick

MapStruct uses any annotation named @Default to select the constructor. Create your own:

package com.example.mapstruct;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

@Target(ElementType.CONSTRUCTOR)
@Retention(RetentionPolicy.CLASS)
public @interface Default {
}

Usage on Mutable Entities
@Entity
public class Order {

    @Id @GeneratedValue
    private Long id;
    private String customerId;
    private BigDecimal total;
    private OrderStatus status;

    // JPA needs this
    protected Order() {}

    // MapStruct uses this - CHANGE HERE = COMPILER ERROR in mapper
    @Default
    public Order(String customerId, BigDecimal total, OrderStatus status) {
        this.customerId = customerId;
        this.total = total;
        this.status = status;
    }
}

Records (Ideal Case)

Records automatically work with constructor mapping:

// No @Default needed - single constructor
public record OrderResponse(
    String orderId,
    String customerId,
    String total,
    String status
) {}

@Mapper(componentModel = "cdi")
public interface OrderMapper {

    @Mapping(target = "orderId", source = "id")
    @Mapping(target = "total", expression = "java(order.getTotal().toString())")
    OrderResponse toResponse(Order order);
}

Key Patterns
1. Constructor-Based Mapping
@Mapper(componentModel = "cdi")
public interface CustomerMapper {

    // MapStruct uses Customer constructor, fail if signature changes
    Customer toEntity(CreateCustomerRequest request);

    // MapStruct uses CustomerResponse constructor
    CustomerResponse toResponse(Customer customer);
}

2. Custom @Default for Entities
@Entity
public class Product {

    @Id @GeneratedValue
    private Long id;
    private String name;
    private BigDecimal price;
    private String category;

    protected Product() {}

    @Default  // Your custom annotation
    public Product(String name, BigDecimal price, String category) {
        this.name = name;
        this.price = price;
        this.category = category;
    }
}

Anti-Pattern: Setter-Based Mapping
// ❌ Can add field to DTO, forget mapper, get null at runtime
public class OrderDTO {
    private String id;
    private String status;
    private String newField;  // Added later, no error!

    // Just setters...
}

// ✓ Add field to constructor = compiler error in mapper
public record OrderDTO(String id, String status, String newField) {}

Compile-Time Safety Benefit
// Before: Record has 3 fields
public record OrderResponse(String id, String status, String total) {}

// After: Added customerName field
public record OrderResponse(String id, String status, String total, String customerName) {}

// Mapper now FAILS TO COMPILE until you add the mapping:
@Mapper(componentModel = "cdi")
public interface OrderMapper {
    @Mapping(target = "customerName", source = "customer.name")  // Must add this
    OrderResponse toResponse(Order order);
}

Cookbook Index
Setup & Configuration
cdi-setup - CDI/MicroProfile setup
default-annotation - Custom @Default annotation
Mapping Patterns
constructor-mapping - Constructor-based mapping
record-mapping - Java Records mapping
entity-mapping - JPA entity mapping
Weekly Installs
13
Repository
emvnuel/skill.md
GitHub Stars
1
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass