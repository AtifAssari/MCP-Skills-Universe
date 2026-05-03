---
rating: ⭐⭐⭐
title: m15-anti-pattern
url: https://skills.sh/zhanghandong/rust-skills/m15-anti-pattern
---

# m15-anti-pattern

skills/zhanghandong/rust-skills/m15-anti-pattern
m15-anti-pattern
Installation
$ npx skills add https://github.com/zhanghandong/rust-skills --skill m15-anti-pattern
Summary

Identify and resolve common Rust code anti-patterns during review.

Covers eight major anti-patterns with explanations and idiomatic alternatives, including excessive cloning, unwrap in production, and fighting the borrow checker
Provides a thinking framework to distinguish symptoms from root causes and trace issues to underlying design problems
Includes quick reference tables for beginner mistakes, code smells, common error patterns, and deprecated approaches with fixes
Links anti-patterns to related skills (ownership, error handling, performance) for deeper understanding
SKILL.md
Anti-Patterns

Layer 2: Design Choices

Core Question

Is this pattern hiding a design problem?

When reviewing code:

Is this solving the symptom or the cause?
Is there a more idiomatic approach?
Does this fight or flow with Rust?
Anti-Pattern → Better Pattern
Anti-Pattern	Why Bad	Better
.clone() everywhere	Hides ownership issues	Proper references or ownership
.unwrap() in production	Runtime panics	?, expect, or handling
Rc when single owner	Unnecessary overhead	Simple ownership
unsafe for convenience	UB risk	Find safe pattern
OOP via Deref	Misleading API	Composition, traits
Giant match arms	Unmaintainable	Extract to methods
String everywhere	Allocation waste	&str, Cow<str>
Ignoring #[must_use]	Lost errors	Handle or let _ =
Thinking Prompt

When seeing suspicious code:

Is this symptom or cause?

Clone to avoid borrow? → Ownership design issue
Unwrap "because it won't fail"? → Unhandled case

What would idiomatic code look like?

References instead of clones
Iterators instead of index loops
Pattern matching instead of flags

Does this fight Rust?

Fighting borrow checker → restructure
Excessive unsafe → find safe pattern
Trace Up ↑

To design understanding:

"Why does my code have so many clones?"
    ↑ Ask: Is the ownership model correct?
    ↑ Check: m09-domain (data flow design)
    ↑ Check: m01-ownership (reference patterns)

Anti-Pattern	Trace To	Question
Clone everywhere	m01-ownership	Who should own this data?
Unwrap everywhere	m06-error-handling	What's the error strategy?
Rc everywhere	m09-domain	Is ownership clear?
Fighting lifetimes	m09-domain	Should data structure change?
Trace Down ↓

To implementation (Layer 1):

"Replace clone with proper ownership"
    ↓ m01-ownership: Reference patterns
    ↓ m02-resource: Smart pointer if needed

"Replace unwrap with proper handling"
    ↓ m06-error-handling: ? operator
    ↓ m06-error-handling: expect with message

Top 5 Beginner Mistakes
Rank	Mistake	Fix
1	Clone to escape borrow checker	Use references
2	Unwrap in production	Propagate with ?
3	String for everything	Use &str
4	Index loops	Use iterators
5	Fighting lifetimes	Restructure to own data
Code Smell → Refactoring
Smell	Indicates	Refactoring
Many .clone()	Ownership unclear	Clarify data flow
Many .unwrap()	Error handling missing	Add proper handling
Many pub fields	Encapsulation broken	Private + accessors
Deep nesting	Complex logic	Extract methods
Long functions	Multiple responsibilities	Split
Giant enums	Missing abstraction	Trait + types
Common Error Patterns
Error	Anti-Pattern Cause	Fix
E0382 use after move	Cloning vs ownership	Proper references
Panic in production	Unwrap everywhere	?, matching
Slow performance	String for all text	&str, Cow
Borrow checker fights	Wrong structure	Restructure
Memory bloat	Rc/Arc everywhere	Simple ownership
Deprecated → Better
Deprecated	Better
Index-based loops	.iter(), .enumerate()
collect::<Vec<_>>() then iterate	Chain iterators
Manual unsafe cell	Cell, RefCell
mem::transmute for casts	as or TryFrom
Custom linked list	Vec, VecDeque
lazy_static!	std::sync::OnceLock
Quick Review Checklist
 No .clone() without justification
 No .unwrap() in library code
 No pub fields with invariants
 No index loops when iterator works
 No String where &str suffices
 No ignored #[must_use] warnings
 No unsafe without SAFETY comment
 No giant functions (>50 lines)
Related Skills
When	See
Ownership patterns	m01-ownership
Error handling	m06-error-handling
Mental models	m14-mental-model
Performance	m10-performance
Weekly Installs
5.3K
Repository
zhanghandong/rust-skills
GitHub Stars
1.1K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass