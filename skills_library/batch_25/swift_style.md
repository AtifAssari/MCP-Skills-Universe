---
title: swift_style
url: https://skills.sh/swiftzilla/skills/swift_style
---

# swift_style

skills/swiftzilla/skills/swift_style
swift_style
Installation
$ npx skills add https://github.com/swiftzilla/skills --skill swift_style
SKILL.md
Swift Style

This skill provides comprehensive style guidelines for writing clean, idiomatic, and maintainable Swift code.

Overview

Swift style guidelines cover naming conventions, access control, type selection, and code organization patterns that make your code more readable and professional.

Available References
Naming & Conventions
Variables and Constants - var vs let, naming conventions, immutability
Functions - Function naming, parameter labels, return types
Types & Protocols
Types - Struct vs Class vs Enum, value vs reference semantics
Protocols - Protocol-Oriented Programming (POP), composition, extensions
Code Organization
Access Control - public, private, internal, fileprivate, open
Quick Reference
Naming Conventions
Category	Case	Example
Types & Protocols	UpperCamelCase	String, UIViewController
Variables, Functions	lowerCamelCase	userID, fetchData()
Boolean Properties	is, has, should	isEmpty, hasPermission
Constants	lowerCamelCase	maxConnections
Type Selection Guide
Need identity or reference semantics?
├── YES → Use Class
└── NO → Need inheritance?
    ├── YES → Use Class
    └── NO → Modeling finite states?
        ├── YES → Use Enum
        └── NO → Use Struct (default)

Access Levels
Modifier	Visibility	Use When
private	Enclosing declaration	Strict encapsulation
fileprivate	Same file	File-local helpers
internal (default)	Same module	Implementation details
public	Everywhere	Public API
open	Everywhere + subclassable	Extensible frameworks
Best Practices
Default to structs - Use simplest type that expresses intent
Use let by default - Only use var when mutation needed
Prefer protocols over inheritance - More flexible composition
Keep functions focused - Single responsibility
Use access control - Expose only what's necessary
Follow naming conventions - Descriptive, Swifty names
For More Information

Each reference file contains detailed information, code examples, and best practices for specific topics. Visit https://swiftzilla.dev for comprehensive Swift documentation.

Weekly Installs
35
Repository
swiftzilla/skills
GitHub Stars
6
First Seen
Jan 28, 2026