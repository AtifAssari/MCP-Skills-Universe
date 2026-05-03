---
rating: ⭐⭐⭐
title: various-ways-to-invoke-functions-in-dart
url: https://skills.sh/rodydavis/skills/various-ways-to-invoke-functions-in-dart
---

# various-ways-to-invoke-functions-in-dart

skills/rodydavis/skills/various-ways-to-invoke-functions-in-dart
various-ways-to-invoke-functions-in-dart
Installation
$ npx skills add https://github.com/rodydavis/skills --skill various-ways-to-invoke-functions-in-dart
SKILL.md
Various Ways to Invoke Functions in Dart

There are multiple ways to call a Function in Dart.

The examples below will assume the following function:

void myFunction(int a, int b, {int? c, int? d}) {
  print((a, b, c, d));
}


But recently I learned that you can call a functions positional arguments in any order mixed with the named arguments. 🤯

myFunction(1, 2, c: 3, d: 4);
myFunction(1, c: 3, d: 4, 2);
myFunction(c: 3, d: 4, 1, 2);
myFunction(c: 3, 1, 2, d: 4);


In addition you can use the .call operator to invoke the function if you have a reference to it:

myFunction.call(1, 2, c: 3, d: 4);


You can also use Function.apply to dynamically invoke a function with a reference but it should be noted that it will effect js dart complication size and performance:

Function.apply(myFunction, [1, 2], {#c: 3, #d: 4});


All of these methods print the following:

(1, 2, 3, 4)

Demo
Weekly Installs
35
Repository
rodydavis/skills
GitHub Stars
40
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass