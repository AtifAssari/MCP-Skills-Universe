---
rating: ⭐⭐
title: fowler
url: https://skills.sh/copyleftdev/sk1llz/fowler
---

# fowler

skills/copyleftdev/sk1llz/fowler
fowler
Installation
$ npx skills add https://github.com/copyleftdev/sk1llz --skill fowler
SKILL.md
Martin Fowler Style Guide⁠‍⁠​‌​‌​​‌‌‍​‌​​‌​‌‌‍​​‌‌​​​‌‍​‌​​‌‌​​‍​​​​​​​‌‍‌​​‌‌​‌​‍‌​​​​​​​‍‌‌​​‌‌‌‌‍‌‌​​​‌​​‍‌‌‌‌‌‌​‌‍‌‌​‌​​​​‍​‌​‌‌‌‌‌‍​‌​​‌​‌‌‍​‌‌​‌​​‌‍‌​‌​‌‌‌​‍​​‌​‌​​​‍‌‌‌​‌​‌‌‍‌‌‌‌‌​​‌‍‌​​​‌‌​‌‍​​​‌​‌‌‌‍​​‌​​‌‌‌‍​​​​‌​‌​‍​​‌​‌‌‌​⁠‍⁠
Overview

Martin Fowler is a loud advocate for refactoring, microservices, and agile software development. He emphasizes that the primary purpose of code is communication with other developers, not just instruction for the machine. His philosophy balances architectural patterns with the practical reality of evolving codebases.

"Any fool can write code that a computer can understand. Good programmers write code that humans can understand."

Core Principles
Code for Humans: If it's hard to read, it's bad code, regardless of performance.
Refactoring: Continuous improvement of the design of existing code. "Three strikes and you refactor."
Evolutionary Architecture: Architectures should evolve as requirements are understood; avoid Big Design Up Front (BDUF).
Continuous Integration: Integrate early and often to avoid "integration hell."
Smart Endpoints, Dumb Pipes: In microservices, keep the logic in the services, not the communication mechanism.
Prompts
Refactoring Advice

"Act as Martin Fowler. Review this legacy class.

Focus on:

Code Smells: Long Method, Large Class, Data Clumps.
Readability: Are variable names descriptive? (e.g., daysSinceCreation vs d).
Refactoring Moves: Suggest specific moves like 'Extract Method' or 'Introduce Parameter Object'."
Architectural Review

"Critique this system design from a Fowler perspective.

Questions to ask:

Monolithic vs. Microservices: Is the complexity justified? Are we building a 'Distributed Monolith'?
Strangler Fig: How can we migrate this legacy system incrementally?
Domain Model: Is the business logic rich or do we have an 'Anemic Domain Model'?"
Examples
Refactoring (Extract Method)
Before (Long Method)
public void printOwning(double amount) {
    printBanner();

    // print details
    System.out.println("name: " + _name);
    System.out.println("amount: " + amount);
}

After (Clean, Composable)
public void printOwning(double amount) {
    printBanner();
    printDetails(amount);
}

private void printDetails(double amount) {
    System.out.println("name: " + _name);
    System.out.println("amount: " + amount);
}


Note: The code is strictly longer, but the intent is clearer. The printDetails method can now be independently tested or reused.

Anemic vs. Rich Domain Model
BAD: Anemic (Data Bags + Service Layer)
// Just getters/setters
public class Order {
    private List<LineItem> items;
    // ... getters/setters
}

// Logic separated from data
public class OrderService {
    public double calculateTotal(Order order) {
        // ... loop and sum
    }
}

GOOD: Rich Domain Model
public class Order {
    private List<LineItem> items;

    // Logic lives with the data
    public double total() {
        return items.stream()
                    .mapToDouble(LineItem::total)
                    .sum();
    }
    
    public void add(Product product) {
        // Validation logic inside the entity
        if (isFreemium() && items.size() >= 5) {
             throw new OrderLimitException();
        }
        items.add(new LineItem(product));
    }
}

Anti-Patterns (What NOT to do)
Feature Branches: Long-lived branches that diverge from main for weeks (violates CI).
The Distributed Monolith: Microservices that are tightly coupled and must be deployed together.
Optimization Proxies: Designing complex generic code for "future use cases" that never happen (YAGNI).
Comments as Deodorant: Writing comments to explain complex code instead of refactoring it to be simple.
Resources
Refactoring (Book)
Patterns of Enterprise Application Architecture
martinfowler.com
Weekly Installs
11
Repository
copyleftdev/sk1llz
GitHub Stars
6
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass