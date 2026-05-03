---
rating: ⭐⭐
title: swift-style
url: https://skills.sh/johnrogers/claude-swift-engineering/swift-style
---

# swift-style

skills/johnrogers/claude-swift-engineering/swift-style
swift-style
Installation
$ npx skills add https://github.com/johnrogers/claude-swift-engineering --skill swift-style
Summary

Swift code style conventions for clean, readable, and idiomatic code.

Enforces naming conventions (UpperCamelCase for types, lowerCamelCase for everything else) and prioritizes clarity over brevity
Advocates the "golden path" pattern: early returns and guards to keep happy-path logic left-aligned, avoiding deep nesting
Covers code organization with extensions and MARK comments, memory management with weak captures, and access control best practices
Identifies five common mistakes: unnecessary abbreviations, nested conditionals, inconsistent self usage, vague type names, and implicit access control
SKILL.md
Swift Style Guide

Code style conventions for clean, readable Swift code.

Core Principles

Clarity > Brevity > Consistency

Code should compile without warnings.

Naming
UpperCamelCase — Types, protocols
lowerCamelCase — Everything else
Clarity at call site
No abbreviations except universal (URL, ID)
// Preferred
let maximumWidgetCount = 100
func fetchUser(byID id: String) -> User

Golden Path

Left-hand margin is the happy path. Don't nest if statements.

// Preferred
func process(value: Int?) throws -> Result {
    guard let value = value else {
        throw ProcessError.nilValue
    }
    guard value > 0 else {
        throw ProcessError.invalidValue
    }
    return compute(value)
}

Code Organization

Use extensions and MARK comments:

class MyViewController: UIViewController {
    // Core implementation
}

// MARK: - UITableViewDataSource
extension MyViewController: UITableViewDataSource { }

Spacing
Braces open on same line, close on new line
One blank line between methods
Colon: no space before, one space after
Self

Avoid self unless required by compiler.

// Preferred
func configure() {
    backgroundColor = .systemBackground
}

Computed Properties

Omit get for read-only:

var diameter: Double {
    radius * 2
}

Closures

Trailing closure only for single closure parameter.

Type Inference

Let compiler infer when clear. For empty collections, use type annotation:

var names: [String] = []

Syntactic Sugar
// Preferred
var items: [String]
var cache: [String: Int]
var name: String?

Access Control
private over fileprivate
Don't add internal (it's the default)
Access control as leading specifier
Memory Management
resource.request().onComplete { [weak self] response in
    guard let self else { return }
    self.updateModel(response)
}

Comments
Explain why, not what
Use // or ///, avoid /* */
Keep up-to-date or delete
Constants

Use case-less enum for namespacing:

enum Math {
    static let pi = 3.14159
}

Common Mistakes

Abbreviations beyond URL, ID, UUID — Abbreviations like cfg, mgr, ctx, desc hurt readability. Spell them out: configuration, manager, context, description. The three exceptions are URL, ID, UUID.

Nested guard/if statements — Deep nesting makes code hard to follow. Use early returns and guards to keep the happy path left-aligned.

Inconsistent self usage — Either always omit self (preferred) or always use it. Mixing makes code scanning harder and confuses capture semantics.

Overly generic type names — Manager, Handler, Helper, Coordinator are too vague. Names should explain responsibility: PaymentProcessor, EventDispatcher, ImageCache, NavigationCoordinator.

Implied access control — Don't skip access control. Explicit private, public helps future maintainers understand module boundaries. internal is default, so omit it.

Weekly Installs
1.4K
Repository
johnrogers/clau…ineering
GitHub Stars
201
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass