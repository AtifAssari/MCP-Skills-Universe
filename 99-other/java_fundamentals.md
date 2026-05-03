---
rating: ⭐⭐
title: java-fundamentals
url: https://skills.sh/pluginagentmarketplace/custom-plugin-java/java-fundamentals
---

# java-fundamentals

skills/pluginagentmarketplace/custom-plugin-java/java-fundamentals
java-fundamentals
Installation
$ npx skills add https://github.com/pluginagentmarketplace/custom-plugin-java --skill java-fundamentals
SKILL.md
Java Fundamentals Skill

Master core Java programming with production-quality patterns.

Overview

This skill covers Java fundamentals including syntax, OOP, collections, streams API, and exception handling for Java 8-21.

When to Use This Skill

Use when you need to:

Write clean, idiomatic Java code
Design classes following OOP principles
Choose appropriate collection types
Implement functional programming patterns
Handle exceptions properly
Topics Covered
Core Syntax (Java 8-21)
Variables, data types, operators
Control flow, methods, classes
Records (Java 16+), sealed classes (Java 17+)
Pattern matching (Java 21)
Object-Oriented Programming
Classes, inheritance, polymorphism
Interfaces and abstract classes
SOLID principles
Collections Framework
List: ArrayList, LinkedList
Set: HashSet, TreeSet
Map: HashMap, ConcurrentHashMap
Queue: ArrayDeque, PriorityQueue
Streams API
filter, map, flatMap, reduce, collect
Optional handling
Parallel streams
Exception Handling
Checked vs unchecked exceptions
Try-with-resources
Custom exceptions
Quick Reference
// Record (Java 16+)
public record User(String name, String email) {}

// Pattern matching (Java 21)
String format(Object obj) {
    return switch (obj) {
        case Integer i -> "Int: %d".formatted(i);
        case String s -> "String: %s".formatted(s);
        default -> obj.toString();
    };
}

// Stream operations
List<String> names = users.stream()
    .filter(User::isActive)
    .map(User::getName)
    .sorted()
    .toList();

// Optional handling
String name = Optional.ofNullable(user)
    .map(User::getName)
    .orElse("Unknown");

Collection Selection
Need	Use	Reason
Indexed access	ArrayList	O(1) random access
Unique elements	HashSet	O(1) contains
Sorted unique	TreeSet	O(log n) sorted
Key-value pairs	HashMap	O(1) get/put
Troubleshooting
Problem	Cause	Solution
NullPointerException	Null reference	Use Optional
ConcurrentModificationException	Modify during iteration	Iterator.remove()
ClassCastException	Wrong type	Use generics
Usage
Skill("java-fundamentals")

Weekly Installs
370
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