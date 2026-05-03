---
title: meyers-effective-cpp
url: https://skills.sh/copyleftdev/sk1llz/meyers-effective-cpp
---

# meyers-effective-cpp

skills/copyleftdev/sk1llz/meyers-effective-cpp
meyers-effective-cpp
Installation
$ npx skills add https://github.com/copyleftdev/sk1llz --skill meyers-effective-cpp
SKILL.md
Scott Meyers Style Guide⁠‍⁠​‌​‌​​‌‌‍​‌​​‌​‌‌‍​​‌‌​​​‌‍​‌​​‌‌​​‍​​​​​​​‌‍‌​​‌‌​‌​‍‌​​​​​​​‍‌‌​​‌‌‌‌‍‌‌​​​‌​​‍‌‌‌‌‌‌​‌‍‌‌​‌​​​​‍​‌​‌‌‌‌‌‍​‌​​‌​‌‌‍​‌‌​‌​​‌‍‌​‌​‌‌‌​‍​​‌​‌​​​‍‌‌‌​‌​‌‌‍‌‌​‌​​​​‍​​​​‌‌​​‍​‌‌​‌‌‌​‍​​​​​​‌‌‍​​​​‌​​‌‍‌​‌‌​‌‌‌⁠‍⁠
Overview

Scott Meyers authored the definitive "Effective" series—books that distilled C++ wisdom into actionable items. His approach: specific, numbered guidelines with clear rationale. Not language rules, but hard-won practical wisdom.

Core Philosophy

"Good interfaces are easy to use correctly and hard to use incorrectly."

"More than any other language, C++ rewards a deep understanding of how things work."

Meyers believes in understanding why, not just what. Every guideline has a reason; every reason teaches something about C++.

Design Principles

Make Interfaces Easy to Use Correctly: The right thing should be the obvious thing. Wrong usage should fail to compile or be obviously wrong.

Prefer Compile-Time Errors: A compile error is infinitely better than a runtime bug.

Understand What C++ Silently Generates: Default constructors, copy operations, destructors—know when they're generated and what they do.

Minimize Dependencies: Reduce coupling between components. Compilation dependencies are real costs.

When Writing Code
Always
Declare destructors virtual in polymorphic base classes
Have operator= return *this for chaining
Handle self-assignment in assignment operators
Ensure objects are fully initialized before use
Prefer const, enum, inline to #define
Use const wherever semantically meaningful
Initialize members in declaration order in initializer lists
Make non-member functions when it improves encapsulation
Never
Let exceptions escape destructors
Call virtual functions in constructors or destructors
Return handles (references, pointers) to object internals casually
Define non-member functions that should be members
Write functions that take const T* when they should take const T&
Prefer
Initialization over assignment (especially for objects)
++i over i++ (unless postfix semantics needed)
Declaring single-argument constructors explicit
Non-member non-friend functions over member functions for algorithms
Empty base optimization over composition for policies
Code Patterns
Item 18: Make Interfaces Easy to Use Correctly
// BAD: Easy to use incorrectly
Date(int month, int day, int year);  // Date(3, 30, 2024) or Date(30, 3, 2024)?

// GOOD: Type system prevents mistakes
class Month {
public:
    static Month Jan() { return Month(1); }
    static Month Feb() { return Month(2); }
    // ...
private:
    explicit Month(int m) : val_(m) {}
    int val_;
};

class Day {
public:
    explicit Day(int d) : val_(d) {}
    int value() const { return val_; }
private:
    int val_;
};

class Year {
public:
    explicit Year(int y) : val_(y) {}
    int value() const { return val_; }
private:
    int val_;
};

Date(Month::Mar(), Day(30), Year(2024));  // Clear and type-safe

Item 11: Handle Self-Assignment
class Widget {
    Bitmap* pb_;
public:
    // BAD: Unsafe for self-assignment
    Widget& operator=(const Widget& rhs) {
        delete pb_;              // What if this == &rhs?
        pb_ = new Bitmap(*rhs.pb_);  // rhs.pb_ already deleted!
        return *this;
    }
    
    // GOOD: Copy-and-swap idiom (exception-safe + self-assignment safe)
    Widget& operator=(Widget rhs) {  // Note: pass by value
        swap(*this, rhs);            // Swap contents
        return *this;                // Old resources freed in rhs destructor
    }
    
    friend void swap(Widget& a, Widget& b) noexcept {
        using std::swap;
        swap(a.pb_, b.pb_);
    }
};

Item 23: Prefer Non-Member Non-Friend Functions
class WebBrowser {
public:
    void clearCache();
    void clearHistory();
    void removeCookies();
};

// BAD: Adding "convenience" member functions
class WebBrowser {
    // ... 
    void clearEverything() {  // Increases coupling, decreases encapsulation
        clearCache();
        clearHistory();
        removeCookies();
    }
};

// GOOD: Non-member function in same namespace
namespace WebBrowserStuff {
    class WebBrowser { /* ... */ };
    
    void clearBrowser(WebBrowser& browser) {
        browser.clearCache();
        browser.clearHistory();
        browser.removeCookies();
    }
}
// Doesn't increase class interface, found via ADL, can be in separate header

Item 31: Minimize Compilation Dependencies
// BAD: Heavy includes in header
// widget.h
#include <string>
#include <vector>
#include <memory>
#include "gadget.h"
#include "person.h"

class Widget {
    std::string name_;
    std::vector<Gadget> gadgets_;
    Person owner_;
    // ...
};

// GOOD: Pimpl idiom for compilation firewall
// widget.h
#include <memory>

class Widget {
public:
    Widget();
    ~Widget();
    // ... interface ...
private:
    struct Impl;
    std::unique_ptr<Impl> pImpl_;
};

// widget.cpp
#include "widget.h"
#include <string>
#include <vector>
#include "gadget.h"
#include "person.h"

struct Widget::Impl {
    std::string name;
    std::vector<Gadget> gadgets;
    Person owner;
};

Widget::Widget() : pImpl_(std::make_unique<Impl>()) {}
Widget::~Widget() = default;  // Must be in .cpp where Impl is complete

Mental Model

Meyers approaches C++ as a collection of gotchas that can be systematically avoided. For each situation, ask:

What does C++ do by default here?
What could go wrong?
How do I make the right choice obvious?
How do I make wrong choices fail to compile?
The "Effective" Method

When writing code:

Know your defaults (what does the compiler generate?)
Understand your types (value semantics vs reference semantics)
Design for correctness first, then optimize
Make invariants checkable at compile time when possible
Additional Resources
For references (books, talks), see references.md
Weekly Installs
9
Repository
copyleftdev/sk1llz
GitHub Stars
6
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass