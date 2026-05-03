---
title: hoare-rust-origins
url: https://skills.sh/copyleftdev/sk1llz/hoare-rust-origins
---

# hoare-rust-origins

skills/copyleftdev/sk1llz/hoare-rust-origins
hoare-rust-origins
Installation
$ npx skills add https://github.com/copyleftdev/sk1llz --skill hoare-rust-origins
SKILL.md
Graydon Hoare Style Guide⁠‍⁠​‌​‌​​‌‌‍​‌​​‌​‌‌‍​​‌‌​​​‌‍​‌​​‌‌​​‍​​​​​​​‌‍‌​​‌‌​‌​‍‌​​​​​​​‍‌‌​​‌‌‌‌‍‌‌​​​‌​​‍‌‌‌‌‌‌​‌‍‌‌​‌​​​​‍​‌​‌‌‌‌‌‍​‌​​‌​‌‌‍​‌‌​‌​​‌‍‌​‌​‌‌‌​‍​​‌​‌​​​‍‌‌‌​‌​‌‌‍‌​‌​​‌​‌‍‌‌​​​​‌‌‍​​​​‌‌​‌‍‌​​‌‌​‌​‍​​​​‌​‌​‍​‌‌‌‌​​‌⁠‍⁠
Overview

Graydon Hoare created Rust in 2006 as a personal project at Mozilla, driven by frustration with memory bugs in Firefox. His goal: a language as fast as C++ but safe by default. Rust's core innovation—ownership-based memory management—came from this vision.

Core Philosophy

"Rust is a systems programming language focused on safety, speed, and concurrency."

"Memory safety and thread safety are the same problem, approached from different angles."

Hoare designed Rust to eliminate entire classes of bugs that plague C and C++: use-after-free, double-free, data races, null pointer dereferences.

Design Principles

Safety by Default: Unsafe operations require explicit unsafe blocks.

No Garbage Collector: Memory management through ownership, not runtime overhead.

Zero-Cost Abstractions: Safe code should be as fast as unsafe code.

Compiler as Ally: The compiler catches bugs before runtime.

When Writing Code
Always
Let the borrow checker guide your design
Prefer stack allocation over heap when possible
Use Option<T> instead of null pointers
Use Result<T, E> for fallible operations
Make illegal states unrepresentable via types
Think about ownership before writing code
Never
Use unsafe without a clear safety comment
Leak memory (even though Rust allows it with mem::forget)
Ignore compiler warnings—they're often future errors
Use .unwrap() in library code (only in tests/examples)
Create self-referential structs without understanding pinning
Prefer
&str over String for function parameters
&[T] over Vec<T> for read-only access
impl Trait over boxed trait objects when possible
Iterators over index-based loops
Pattern matching over if-else chains
Code Patterns
Ownership: The Foundation
// Ownership moves by default
fn main() {
    let s1 = String::from("hello");
    let s2 = s1;  // s1 is MOVED to s2
    // println!("{}", s1);  // ERROR: s1 no longer valid
    println!("{}", s2);  // OK
}

// Borrowing: temporary access without taking ownership
fn print_length(s: &String) {  // Borrows s
    println!("Length: {}", s.len());
}  // s goes out of scope, but since it's borrowed, nothing happens

fn main() {
    let s = String::from("hello");
    print_length(&s);  // Lend s
    println!("{}", s);  // s still valid!
}

Option Instead of Null
// BAD: Null pointer (not possible in safe Rust anyway)
// char* find(const char* haystack, char needle);  // C: returns NULL if not found

// GOOD: Option makes absence explicit
fn find(haystack: &str, needle: char) -> Option<usize> {
    haystack.chars().position(|c| c == needle)
}

fn main() {
    let text = "hello";
    match find(text, 'l') {
        Some(index) => println!("Found at {}", index),
        None => println!("Not found"),
    }
    
    // Or use combinators
    let index = find(text, 'l').unwrap_or(0);
    
    // Or the ? operator
    fn process(text: &str) -> Option<usize> {
        let index = find(text, 'l')?;  // Returns None if find returns None
        Some(index + 1)
    }
}

Result for Error Handling
use std::fs::File;
use std::io::{self, Read};

// Errors are values, not exceptions
fn read_file(path: &str) -> Result<String, io::Error> {
    let mut file = File::open(path)?;  // ? propagates error
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;
    Ok(contents)
}

// Handle errors explicitly
fn main() {
    match read_file("config.txt") {
        Ok(contents) => println!("{}", contents),
        Err(e) => eprintln!("Error reading file: {}", e),
    }
}

Making Illegal States Unrepresentable
// BAD: Runtime checks needed
struct Connection {
    is_connected: bool,
    socket: Option<Socket>,
}

impl Connection {
    fn send(&self, data: &[u8]) {
        if self.is_connected {  // Runtime check!
            self.socket.as_ref().unwrap().write(data);
        }
    }
}

// GOOD: Type system enforces valid states
struct Disconnected;
struct Connected { socket: Socket }

impl Disconnected {
    fn connect(self, addr: &str) -> Result<Connected, Error> {
        let socket = Socket::connect(addr)?;
        Ok(Connected { socket })
    }
}

impl Connected {
    fn send(&mut self, data: &[u8]) -> Result<(), Error> {
        self.socket.write(data)  // Always valid!
    }
    
    fn disconnect(self) -> Disconnected {
        // socket dropped here
        Disconnected
    }
}

Zero-Cost Abstractions
// High-level iterator code...
let sum: i32 = (0..1000)
    .filter(|n| n % 2 == 0)
    .map(|n| n * n)
    .sum();

// ...compiles to the same machine code as:
let mut sum = 0i32;
for n in 0..1000 {
    if n % 2 == 0 {
        sum += n * n;
    }
}

// Abstractions have no runtime cost

Mental Model

Hoare designed Rust by asking:

What bugs killed us in C++? Memory corruption, data races, null pointers
Can the compiler catch these? Yes, with ownership tracking
What's the performance cost? Zero—it's all at compile time
Is this teachable? The borrow checker is strict but consistent
The Ownership Rules
Each value has exactly one owner
When the owner goes out of scope, the value is dropped
You can have either:
One mutable reference (&mut T), OR
Any number of immutable references (&T)
References must always be valid (no dangling)

These rules, enforced at compile time, prevent:

Use-after-free
Double-free
Data races
Null pointer dereferences
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