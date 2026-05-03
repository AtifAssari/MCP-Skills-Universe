---
rating: ⭐⭐⭐
title: unit-test-mapper-converter
url: https://skills.sh/giuseppe-trisciuoglio/developer-kit/unit-test-mapper-converter
---

# unit-test-mapper-converter

skills/giuseppe-trisciuoglio/developer-kit/unit-test-mapper-converter
unit-test-mapper-converter
Installation
$ npx skills add https://github.com/giuseppe-trisciuoglio/developer-kit --skill unit-test-mapper-converter
Summary

Unit testing patterns for MapStruct mappers and custom converters with comprehensive transformation validation.

Covers field mapping accuracy, null handling, type conversions, nested objects, bidirectional mapping, enum mapping, and partial updates
Includes Maven and Gradle setup with MapStruct, JUnit 5, and AssertJ dependencies
Provides patterns for testing simple mappings, nested hierarchies, custom @Mapping annotations, enum @ValueMapping, and @MappingTarget partial updates
Demonstrates round-trip validation, recursive comparison for complex structures, and null input handling across all mapper scenarios
SKILL.md
Unit Testing Mappers and Converters
Overview

Provides patterns for unit testing MapStruct mappers and custom converter classes. Covers field mapping accuracy, null handling, type conversions, nested object transformations, bidirectional mapping, enum mapping, and partial updates.

When to Use
Writing mapping tests for MapStruct mapper implementations
Testing custom entity-to-DTO converters and bean mappings
Validating nested object mapping and collection transformations
Instructions
1. Validate Generated Mapper Classes

Before testing, verify generated mapper classes exist:

# Maven
ls target/generated-sources/

# Gradle
ls build/generated/sources/


If generated classes are missing:

Run mvn compile (Maven) or ./gradlew compileJava (Gradle)
Check that the MapStruct annotation processor is configured
Verify @Mapper interfaces are in a compiled source set
2. Test Null Handling
assertThat(mapper.toDto(null)).isNull();


Configure nullValueMappingStrategy in mapper if null should return empty/default.

If null tests fail:

Add nullValueMappingStrategy = NullValueMappingStrategy.RETURN_NULL to @Mapper
Or use nullValuePropertyMappingStrategy for nested property handling
3. Test Bidirectional Mapping
User restored = mapper.toEntity(mapper.toDto(original));
assertThat(restored).usingRecursiveComparison().isEqualTo(original);


If bidirectional tests fail:

Check @Mapping annotations for field name mismatches
Verify both directions are explicitly mapped if auto-mapping fails
Use unmappedTargetPolicy = ReportingPolicy.ERROR to catch missing mappings
4. Test Nested Object Mapping
assertThat(dto.getNested()).usingRecursiveComparison().isEqualTo(expected);


If nested tests fail:

Ensure nested mapper exists or is referenced via uses = NestedMapper.class
Check collection element mappings with elementMappingStrategy
5. Test Custom Expressions

Custom expressions in @Mapping(target = "field", expression = "java(...)") are not compile-time validated.

If expression tests fail:

Verify the expression syntax and method signatures
Check that imported classes are accessible from the expression context
6. Test Enum Mappings

Use @ValueMapping for enum-to-enum translations. Test all enum values exhaustively.

Best Practices
Use Mappers.getMapper() for standalone tests, Spring injection for integration tests
Use usingRecursiveComparison() for complex nested structures
Test all mapper methods including collection transformations
Verify null handling for all nullable source fields
Test bidirectional mapping catches asymmetries between entity→DTO and DTO→entity
Keep mapper tests focused on transformation correctness, not implementation details
Constraints and Warnings
Compile-time generation: MapStruct generates code at compile time—verify generated classes exist before running tests
Null handling: Configure nullValueMappingStrategy and nullValuePropertyMappingStrategy appropriately
Expression validation: Expressions in @Mapping are not validated at compile time—test them explicitly
Circular dependencies: MapStruct cannot handle circular dependencies between mappers
Collection immutability: Mapping immutable collections may require special configuration
Date/Time: Verify date/time objects map correctly across timezones
Examples

Complete executable test with imports:

package com.example.mapper;

import org.junit.jupiter.api.Test;
import org.mapstruct.factory.Mappers;
import static org.assertj.core.api.Assertions.*;

class UserMapperCompleteTest {
  private final UserMapper mapper = Mappers.getMapper(UserMapper.class);

  @Test
  void shouldMapUserToDto() {
    User user = new User(1L, "Alice", "alice@example.com", 25);
    UserDto dto = mapper.toDto(user);
    assertThat(dto)
      .isNotNull()
      .extracting(UserDto::getName, UserDto::getEmail)
      .containsExactly("Alice", "alice@example.com");
  }

  @Test
  void shouldMaintainRoundTrip() {
    User original = new User(1L, "Alice", "alice@example.com", 25);
    assertThat(mapper.toEntity(mapper.toDto(original)))
      .usingRecursiveComparison()
      .isEqualTo(original);
  }

  @Test
  void shouldHandleNullInput() {
    assertThat(mapper.toDto(null)).isNull();
  }
}


Additional examples in: references/examples.md

Weekly Installs
701
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