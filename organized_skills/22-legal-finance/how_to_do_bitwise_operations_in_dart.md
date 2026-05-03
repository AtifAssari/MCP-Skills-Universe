---
rating: ⭐⭐
title: how-to-do-bitwise-operations-in-dart
url: https://skills.sh/rodydavis/skills/how-to-do-bitwise-operations-in-dart
---

# how-to-do-bitwise-operations-in-dart

skills/rodydavis/skills/how-to-do-bitwise-operations-in-dart
how-to-do-bitwise-operations-in-dart
Installation
$ npx skills add https://github.com/rodydavis/skills --skill how-to-do-bitwise-operations-in-dart
SKILL.md
How to do Bitwise operations in Dart

In Dart it is possible to do Bitwise Operations with int and bool types.

AND 

Checks if the left and right side are both true. Learn more.

// int
print(0 & 1); // 0
print(1 & 0); // 0
print(1 & 1); // 1
print(0 & 0); // 0

// bool
print(false & true); // false
print(true & false); // false
print(true & true); // true
print(false & false); // false

OR 
Inclusive 

Checks if either the left or right side are true. Learn more.

// int
print(0 | 1); // 1
print(1 | 0); // 1
print(1 | 1); // 1
print(0 | 0); // 0

// bool
print(false | true); // true
print(true | false); // true
print(true | true); // true
print(false | false); // false

Exclusive 

Checks if both the left or right side are true but not both. Learn more.

// int
print(0 ^ 1); // 1
print(1 ^ 0); // 1
print(1 ^ 1); // 0
print(0 ^ 0); // 0

// bool
print(false ^ true); // true
print(true ^ false); // true
print(true ^ true); // false
print(false ^ false); // false

NAND 

Negated AND operation.

// int
print(~(0 & 1) & 1); // 1
print(~(1 & 0) & 1); // 1
print(~(1 & 1) & 1); // 0
print(~(0 & 0) & 1); // 1

// bool
print(!(false & true)); // true
print(!(true & false)); // true
print(!(true & true)); // false
print(!(false & false)); // true

NOR 

Negated inclusive OR operation.

// int
print(~(0 | 1) & 1); // 0
print(~(1 | 0) & 1); // 0
print(~(1 | 1) & 1); // 0
print(~(0 | 0) & 1); // 1

// bool
print(!(false | true)); // false
print(!(true | false)); // false
print(!(true | true)); // false
print(!(false | false)); // true

XNOR 

Negated exclusive OR operation.

// int
print(~(0 ^ 1) & 1); // 0
print(~(1 ^ 0) & 1); // 0
print(~(1 ^ 1) & 1); // 1
print(~(0 ^ 0) & 1); // 1

// bool
print(!(false ^ true)); // false
print(!(true ^ false)); // false
print(!(true ^ true)); // true
print(!(false ^ false)); // true

Weekly Installs
34
Repository
rodydavis/skills
GitHub Stars
40
First Seen
Feb 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass