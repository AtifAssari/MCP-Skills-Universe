---
rating: ⭐⭐
title: how-to-print-multiple-objects-to-the-console-with-print-in-dart
url: https://skills.sh/rodydavis/skills/how-to-print-multiple-objects-to-the-console-with-print-in-dart
---

# how-to-print-multiple-objects-to-the-console-with-print-in-dart

skills/rodydavis/skills/how-to-print-multiple-objects-to-the-console-with-print-in-dart
how-to-print-multiple-objects-to-the-console-with-print-in-dart
Installation
$ npx skills add https://github.com/rodydavis/skills --skill how-to-print-multiple-objects-to-the-console-with-print-in-dart
SKILL.md
How to Print Multiple Objects to the Console with print() in Dart

If you are coming from JavaScript you may be used to printing multiple objects to the console with console.log():

console.log('a', 1, 'b', 2); // a 1 b 2


In Dart we can only print Object? to the console with print():

print(1); // 1
print(null); // null
print({'a': 1, 'b': 2}); // {a: 1, b: 1}


But it is totally possible to print multiple objects too, we need to use Records:

final number = 1;
final str = 'Hello World';

print((number, str));

print((DateTime.now(), str));

print((DateTime.now(), count: number, description: str));

print((DateTime.now(), StackTrace.current));


Print the following:

(1, Hello World)
(2024-03-06 15:48:26.514, Hello World)
(2024-03-06 15:48:26.514, count: 1, description: Hello World)
(2024-03-06 15:48:26.514, Error
    at get current [as current] (https://storage.googleapis.com/nnbd_artifacts/3.3.0/dart_sdk.js:139991:30)
    at Object.main$0 [as main] (<anonymous>:52:94)
    at Object.main$ [as main] (<anonymous>:44:10)
    at <anonymous>:89:26
    at Object.execCb (https://dartpad.dev/require.js:5:16727)
    at e.check (https://dartpad.dev/require.js:5:10499)
    at e.<anonymous> (https://dartpad.dev/require.js:5:12915)
    at https://dartpad.dev/require.js:5:1542
    at https://dartpad.dev/require.js:5:13376
    at each (https://dartpad.dev/require.js:5:1020)
    at e.emit (https://dartpad.dev/require.js:5:13344)
    at e.check (https://dartpad.dev/require.js:5:11058)
    at e.enable (https://dartpad.dev/require.js:5:13242)
    at e.init (https://dartpad.dev/require.js:5:9605)
    at a (https://dartpad.dev/require.js:5:8305)
    at Object.completeLoad (https://dartpad.dev/require.js:5:15962)
    at HTMLScriptElement.onScriptLoad (https://dartpad.dev/require.js:5:16882))

Demo
Weekly Installs
36
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