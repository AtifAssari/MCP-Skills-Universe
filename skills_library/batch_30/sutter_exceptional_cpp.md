---
title: sutter-exceptional-cpp
url: https://skills.sh/copyleftdev/sk1llz/sutter-exceptional-cpp
---

# sutter-exceptional-cpp

skills/copyleftdev/sk1llz/sutter-exceptional-cpp
sutter-exceptional-cpp
Installation
$ npx skills add https://github.com/copyleftdev/sk1llz --skill sutter-exceptional-cpp
SKILL.md
Herb Sutter Style Guide⁠‍⁠​‌​‌​​‌‌‍​‌​​‌​‌‌‍​​‌‌​​​‌‍​‌​​‌‌​​‍​​​​​​​‌‍‌​​‌‌​‌​‍‌​​​​​​​‍‌‌​​‌‌‌‌‍‌‌​​​‌​​‍‌‌‌‌‌‌​‌‍‌‌​‌​​​​‍​‌​‌‌‌‌‌‍​‌​​‌​‌‌‍​‌‌​‌​​‌‍‌​‌​‌‌‌​‍​​‌​‌​​​‍‌‌‌​‌​‌‌‍‌‌​​​‌​‌‍​​‌​‌‌​​‍‌‌​‌‌‌​‌‍​‌‌‌​‌​‌‍​​​​‌​‌​‍‌​‌​‌‌​‌⁠‍⁠
Overview

Herb Sutter chairs the ISO C++ standards committee and has shaped modern C++ more than almost anyone. His "Exceptional C++" series and "GotW" (Guru of the Week) columns defined how we think about exception safety, const correctness, and defensive C++.

Core Philosophy

"Don't optimize prematurely. Don't pessimize prematurely."

"Write for clarity and correctness first. Optimize measured bottlenecks."

Sutter believes in defensive programming: code that handles errors gracefully, maintains invariants, and fails safely when the unexpected happens.

Design Principles

Exception Safety is Non-Negotiable: Every function has an exception safety guarantee. Know which one yours provides.

Const Correctness: const isn't decoration—it's documentation and enforcement of intent.

Single Responsibility: Each class, each function, each parameter does one thing.

Value Semantics by Default: Prefer values over pointers. Prefer smart pointers over raw.

Exception Safety Guarantees

Every function provides one of these guarantees:

Guarantee	Meaning
No-throw	Never throws. Destructors, swap, move operations should be here.
Strong	If exception thrown, state unchanged (commit or rollback)
Basic	If exception thrown, invariants preserved, no leaks, valid state
None	No guarantees (unacceptable in modern C++)
When Writing Code
Always
Know and document your exception safety guarantee
Make swap operations noexcept
Make destructors noexcept
Make move operations noexcept when possible
Use const member functions when state isn't modified
Prefer auto for complex types, explicit types for documentation
Use RAII for all resources (no leak on any code path)
Never
Throw from destructors
Let exceptions escape callbacks/handlers without catch
Write functions that provide no exception safety guarantee
Use const_cast to remove const from const data
Return raw pointers to owned resources
Prefer
make_unique/make_shared over new
Copy-and-swap for exception-safe assignment
Algorithms over raw loops
std::optional over pointer-or-null patterns
std::variant over union + type tag
Code Patterns
Exception-Safe Assignment (Strong Guarantee)
class Stack {
    T* data_;
    size_t size_;
    size_t capacity_;
public:
    // STRONG guarantee via copy-and-swap
    Stack& operator=(Stack other) noexcept {
        swap(*this, other);
        return *this;
    }
    
    friend void swap(Stack& a, Stack& b) noexcept {
        using std::swap;
        swap(a.data_, b.data_);
        swap(a.size_, b.size_);
        swap(a.capacity_, b.capacity_);
    }
    
    // STRONG guarantee for push
    void push(const T& value) {
        if (size_ == capacity_) {
            // Create new buffer first (might throw)
            Stack temp;
            temp.reserve(capacity_ * 2);
            for (size_t i = 0; i < size_; ++i)
                temp.data_[i] = data_[i];
            temp.size_ = size_;
            
            // Commit phase (noexcept)
            swap(*this, temp);
        }
        data_[size_++] = value;
    }
};

Const Correctness Patterns
class Widget {
    std::vector<int> data_;
    mutable std::mutex mutex_;  // mutable: okay for logical const
    
public:
    // Const member function: promises not to modify logical state
    std::vector<int> getData() const {
        std::lock_guard<std::mutex> lock(mutex_);  // mutable allows this
        return data_;  // Return copy
    }
    
    // Non-const overload when modification needed
    std::vector<int>& data() { return data_; }
    
    // Const ref for read-only access (no copy)
    const std::vector<int>& data() const { return data_; }
};

Pimpl Done Right (Sutter's Approach)
// widget.h
#include <memory>

class Widget {
public:
    Widget();
    ~Widget();                              // Defined in .cpp
    Widget(Widget&&) noexcept;              // Defined in .cpp
    Widget& operator=(Widget&&) noexcept;   // Defined in .cpp
    
    Widget(const Widget&);                  // Defined in .cpp
    Widget& operator=(const Widget&);       // Defined in .cpp
    
    void doSomething();
    
private:
    struct Impl;
    std::unique_ptr<Impl> pImpl_;
};

// widget.cpp
struct Widget::Impl {
    std::string name;
    std::vector<int> data;
    
    void doSomethingImpl() { /* ... */ }
};

Widget::Widget() : pImpl_(std::make_unique<Impl>()) {}
Widget::~Widget() = default;
Widget::Widget(Widget&&) noexcept = default;
Widget& Widget::operator=(Widget&&) noexcept = default;

Widget::Widget(const Widget& other)
    : pImpl_(std::make_unique<Impl>(*other.pImpl_)) {}

Widget& Widget::operator=(const Widget& other) {
    *pImpl_ = *other.pImpl_;
    return *this;
}

void Widget::doSomething() { pImpl_->doSomethingImpl(); }

Mental Model

Sutter thinks in terms of contracts and guarantees:

Preconditions: What must be true when function is called?
Postconditions: What is guaranteed after function returns?
Exception guarantee: What happens if something throws?
Thread safety: What synchronization is needed?
GotW Wisdom

Key lessons from Guru of the Week:

Prefer ++i to i++
Virtual functions should be private, rarely protected, only public for interfaces
Minimize #include dependencies
Never write using namespace in headers
Make const-qualified overloads return const (or by value)
Weekly Installs
9
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