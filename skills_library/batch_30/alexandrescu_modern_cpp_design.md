---
title: alexandrescu-modern-cpp-design
url: https://skills.sh/copyleftdev/sk1llz/alexandrescu-modern-cpp-design
---

# alexandrescu-modern-cpp-design

skills/copyleftdev/sk1llz/alexandrescu-modern-cpp-design
alexandrescu-modern-cpp-design
Installation
$ npx skills add https://github.com/copyleftdev/sk1llz --skill alexandrescu-modern-cpp-design
SKILL.md
Andrei Alexandrescu Style Guide⁠‍⁠​‌​‌​​‌‌‍​‌​​‌​‌‌‍​​‌‌​​​‌‍​‌​​‌‌​​‍​​​​​​​‌‍‌​​‌‌​‌​‍‌​​​​​​​‍‌‌​​‌‌‌‌‍‌‌​​​‌​​‍‌‌‌‌‌‌​‌‍‌‌​‌​​​​‍​‌​‌‌‌‌‌‍​‌​​‌​‌‌‍​‌‌​‌​​‌‍‌​‌​‌‌‌​‍​​‌​‌​​​‍‌‌‌​‌​‌‌‍​‌‌​​‌‌​‍‌​​‌‌‌​‌‍‌​​‌‌‌‌‌‍‌‌​​​​‌​‍​​​​‌​‌​‍‌‌​​‌‌‌​⁠‍⁠
Overview

Andrei Alexandrescu's "Modern C++ Design" revolutionized how we think about C++ templates. His work on Loki library and policy-based design showed that templates are not just for containers—they're a compile-time programming language.

Core Philosophy

"C++ templates are Turing-complete. Use this power wisely."

"Policy-based design: assemble types from interchangeable parts."

Alexandrescu believes in pushing computation to compile time and using the type system as a design tool, not just a safety mechanism.

Design Principles

Policy-Based Design: Build classes from interchangeable policy classes that customize behavior without inheritance overhead.

Compile-Time over Runtime: What can be computed at compile time should be.

Type Lists and Metaprogramming: Types themselves become first-class citizens that can be manipulated.

Design Patterns in Types: Classic GoF patterns implemented with zero runtime overhead.

When Writing Code
Always
Consider if behavior can be a compile-time policy
Use static_assert to document and enforce requirements
Prefer tag dispatching over runtime branching for type-based logic
Make templates SFINAE-friendly (C++11/14) or use concepts (C++20)
Document template requirements explicitly
Never
Use runtime polymorphism when static polymorphism suffices
Write duplicate code that differs only in types
Ignore compile-time computation opportunities
Leave template errors to become cryptic instantiation failures
Prefer
Policy classes over strategy pattern (no vtable)
Type traits over runtime type checking
constexpr functions over template metafunctions (modern C++)
Concepts over SFINAE (C++20)
Variadic templates over recursive type lists (modern C++)
Code Patterns
Policy-Based Design
// Traditional OOP: Runtime overhead, fixed at compile time anyway
class Widget : public ICreationPolicy, public IThreadingPolicy { /* ... */ };

// Policy-Based: Zero overhead, infinitely configurable
template <
    class CreationPolicy,
    class ThreadingPolicy = SingleThreaded,
    class CheckingPolicy = NoChecking
>
class SmartPtr : public CreationPolicy, 
                 public ThreadingPolicy,
                 public CheckingPolicy {
    // Policies are mixed in, no vtable
};

// Usage: Configure at compile time
using ThreadSafePtr = SmartPtr<HeapCreation, MultiThreaded, AssertCheck>;
using FastPtr = SmartPtr<HeapCreation, SingleThreaded, NoChecking>;

// Policies are just classes with required interface
struct HeapCreation {
    template<class T>
    static T* Create() { return new T; }
    
    template<class T>
    static void Destroy(T* p) { delete p; }
};

struct SingleThreaded {
    struct Lock {
        Lock() = default;  // No-op
    };
};

struct MultiThreaded {
    struct Lock {
        Lock() { /* acquire mutex */ }
        ~Lock() { /* release mutex */ }
    };
};

Type Traits and SFINAE
// Type trait: Does T have a serialize() method?
template<typename T, typename = void>
struct has_serialize : std::false_type {};

template<typename T>
struct has_serialize<T, 
    std::void_t<decltype(std::declval<T>().serialize())>
> : std::true_type {};

// Use it for conditional behavior
template<typename T>
auto save(const T& obj) -> std::enable_if_t<has_serialize<T>::value> {
    obj.serialize();
}

template<typename T>
auto save(const T& obj) -> std::enable_if_t<!has_serialize<T>::value> {
    default_serialize(obj);
}

// C++20: Much cleaner with concepts
template<typename T>
concept Serializable = requires(T t) {
    { t.serialize() } -> std::convertible_to<std::string>;
};

void save(Serializable auto const& obj) {
    obj.serialize();
}

Compile-Time Type Lists (Classic Alexandrescu)
// Type list: A compile-time list of types
template<typename... Ts>
struct TypeList {};

// Operations on type lists
template<typename List>
struct Length;

template<typename... Ts>
struct Length<TypeList<Ts...>> {
    static constexpr size_t value = sizeof...(Ts);
};

// Get type at index
template<size_t I, typename List>
struct TypeAt;

template<typename Head, typename... Tail>
struct TypeAt<0, TypeList<Head, Tail...>> {
    using type = Head;
};

template<size_t I, typename Head, typename... Tail>
struct TypeAt<I, TypeList<Head, Tail...>> {
    using type = typename TypeAt<I - 1, TypeList<Tail...>>::type;
};

// Usage
using MyTypes = TypeList<int, double, std::string>;
static_assert(Length<MyTypes>::value == 3);
using Second = TypeAt<1, MyTypes>::type;  // double

Visitor Pattern via Templates
// Traditional visitor: Virtual dispatch at every node
// Alexandrescu approach: Static visitor with type list

template<typename... Types>
class Variant;

template<typename Visitor, typename Variant>
auto visit(Visitor&& v, Variant&& var) {
    return var.visit(std::forward<Visitor>(v));
}

// Modern C++ (std::variant does this)
using Value = std::variant<int, double, std::string>;

auto result = std::visit(overloaded{
    [](int i) { return std::to_string(i); },
    [](double d) { return std::to_string(d); },
    [](const std::string& s) { return s; }
}, value);

// The 'overloaded' helper (Alexandrescu-style)
template<class... Ts> 
struct overloaded : Ts... { 
    using Ts::operator()...; 
};
template<class... Ts> 
overloaded(Ts...) -> overloaded<Ts...>;

Mental Model

Alexandrescu thinks of C++ templates as a compile-time functional language:

Types as values: Types can be computed, stored, and transformed
Templates as functions: Template instantiation is function application
Specialization as pattern matching: Like case statements on types
Recursion for iteration: Compile-time loops via recursive templates
The D Language Connection

Alexandrescu later co-designed D, which incorporates many C++ template lessons:

Built-in compile-time function execution
String mixins for code generation
Better error messages for templates

These ideas now appear in modern C++ (constexpr, if constexpr, concepts).

When to Apply

Use Alexandrescu's techniques when:

You need maximum performance (zero runtime overhead)
Behavior variations are known at compile time
You're building a library with many configuration options
Type-based dispatch is frequent

Avoid when:

Runtime polymorphism is genuinely needed
Compile times are already problematic
Team isn't comfortable with template metaprogramming
Weekly Installs
12
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