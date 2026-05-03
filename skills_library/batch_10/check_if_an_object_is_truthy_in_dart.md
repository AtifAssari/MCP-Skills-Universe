---
title: check-if-an-object-is-truthy-in-dart
url: https://skills.sh/rodydavis/skills/check-if-an-object-is-truthy-in-dart
---

# check-if-an-object-is-truthy-in-dart

skills/rodydavis/skills/check-if-an-object-is-truthy-in-dart
check-if-an-object-is-truthy-in-dart
Installation
$ npx skills add https://github.com/rodydavis/skills --skill check-if-an-object-is-truthy-in-dart
SKILL.md
Check if an Object is Truthy in Dart

If you are coming from language like JavaScript you may be used to checking if an object is truthy.

if (true)
if ({})
if ([])
if (42)
if ("0")
if ("false")
if (new Date())
if (-42)
if (12n)
if (3.14)
if (-3.14)
if (Infinity)
if (-Infinity)


In Dart you need to explicitly check if an object is not null, true/false or determine if the value is true based on the type.

It is possible however to use Dart extensions to add the truthy capability.

extension on Object? {
  bool get isTruthy => truthy(this);
}

bool truthy(Object? val) {
  if (val == null) return false;
  if (val is bool) return val;
  if (val is num && val == 0) return false;
  if (val is String && (val == 'false' || val == '')) return false;
  if (val is Iterable && val.isEmpty) return false;
  if (val is Map && val.isEmpty) return false;
  return true;
}


This will now make it possible for any object to be evaluated as a truthy value in if statements or value assignments.

Prints the following:

(null, false)
(, false)
(false, false)
(true, true)
(0, false)
(1, true)
(false, false)
(true, true)
([], false)
([1, 2, 3], true)
({}, false)
({1, 2, 3}, true)
({a: 1, b: 2}, true)

Demo
Weekly Installs
36
Repository
rodydavis/skills
GitHub Stars
40
First Seen
Feb 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass