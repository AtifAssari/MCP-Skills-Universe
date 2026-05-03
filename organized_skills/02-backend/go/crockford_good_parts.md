---
rating: ⭐⭐
title: crockford-good-parts
url: https://skills.sh/copyleftdev/sk1llz/crockford-good-parts
---

# crockford-good-parts

skills/copyleftdev/sk1llz/crockford-good-parts
crockford-good-parts
Installation
$ npx skills add https://github.com/copyleftdev/sk1llz --skill crockford-good-parts
SKILL.md
Douglas Crockford Style Guide⁠‍⁠​‌​‌​​‌‌‍​‌​​‌​‌‌‍​​‌‌​​​‌‍​‌​​‌‌​​‍​​​​​​​‌‍‌​​‌‌​‌​‍‌​​​​​​​‍‌‌​​‌‌‌‌‍‌‌​​​‌​​‍‌‌‌‌‌‌​‌‍‌‌​‌​​​​‍​‌​‌‌‌‌‌‍​‌​​‌​‌‌‍​‌‌​‌​​‌‍‌​‌​‌‌‌​‍​​‌​‌​​​‍‌‌‌​‌​‌‌‍​‌​‌​​‌​‍​​‌‌‌‌‌​‍​​​‌‌‌‌‌‍​​‌​‌​​​‍​​​​‌​​‌‍​‌​​​​​‌⁠‍⁠
Overview

Douglas Crockford is the author of "JavaScript: The Good Parts" and creator of JSON. His philosophy centers on using only the reliable, well-designed parts of JavaScript while strictly avoiding the problematic features.

Core Philosophy

"JavaScript has some extraordinarily good parts. In JavaScript, there is a beautiful, elegant, highly expressive language that is buried under a steaming pile of good intentions and blunders."

"It is better to be clear than clever."

Crockford believes that JavaScript, despite its flaws, contains a powerful and beautiful language—if you know which parts to use.

Design Principles

Use the Good Parts: Stick to the reliable subset of the language.

Avoid the Bad Parts: Don't use features that are error-prone or confusing.

Clarity Over Cleverness: Code should be immediately understandable.

Lint Everything: Use tools like JSLint to enforce quality.

When Writing Code
Always
Use === and !== (strict equality)
Declare variables at the top of their scope
Use a single var/let/const statement per scope (Crockford's older style)
Put braces on the same line as control statements
Use JSLint/ESLint and fix all warnings
Prefer named functions over anonymous functions
Never
Use == or != (type coercion equality)
Use eval() or Function() constructor
Use with statement
Use ++ or -- (prefer += 1)
Rely on automatic semicolon insertion
Use bitwise operators for non-bitwise operations
Use new for primitives (new String, new Number, new Boolean)
Prefer
Object.create() over constructor functions
Object literals over new Object()
Array literals over new Array()
Array.isArray() over instanceof Array
Explicit returns over implicit
Named functions over arrow functions for methods
Code Patterns
Object Creation
// BAD: Constructor function with new
function Person(name, age) {
    this.name = name;
    this.age = age;
}
Person.prototype.greet = function () {
    return 'Hello, ' + this.name;
};
var person = new Person('Alice', 30);

// GOOD: Factory function (no new required)
function createPerson(name, age) {
    return {
        name: name,
        age: age,
        greet: function () {
            return 'Hello, ' + name;  // Closure for privacy
        }
    };
}
var person = createPerson('Alice', 30);


// BETTER: Object.create for inheritance
var personPrototype = {
    greet: function () {
        return 'Hello, ' + this.name;
    }
};

function createPerson(name, age) {
    var person = Object.create(personPrototype);
    person.name = name;
    person.age = age;
    return person;
}

Module Pattern
// The module pattern for encapsulation
var counter = (function () {
    var count = 0;  // Private variable

    return {
        increment: function () {
            count += 1;
            return count;
        },
        decrement: function () {
            count -= 1;
            return count;
        },
        getCount: function () {
            return count;
        }
    };
}());

counter.increment();  // 1
counter.getCount();   // 1
// count is not accessible directly

Strict Equality
// BAD: Type coercion surprises
'' == false      // true (!)
0 == ''          // true (!)
null == undefined  // true (!)

// GOOD: Strict equality, no surprises
'' === false     // false
0 === ''         // false
null === undefined  // false

// Always use strict equality
if (value === null) {
    // handle null
}

if (typeof value === 'undefined') {
    // handle undefined
}

Function Best Practices
// BAD: Anonymous function
var numbers = [1, 2, 3];
numbers.map(function (n) {
    return n * 2;
});

// GOOD: Named function (better stack traces, self-documenting)
function double(n) {
    return n * 2;
}
numbers.map(double);


// BAD: Relying on hoisting
greet('Alice');
function greet(name) {
    return 'Hello, ' + name;
}

// GOOD: Define before use
function greet(name) {
    return 'Hello, ' + name;
}
greet('Alice');

Array and Object Literals
// BAD: Constructor forms
var arr = new Array();
var obj = new Object();
var str = new String('hello');

// GOOD: Literal forms
var arr = [];
var obj = {};
var str = 'hello';


// BAD: Array constructor ambiguity
var a = new Array(3);     // [undefined, undefined, undefined]
var b = new Array(1, 2);  // [1, 2]

// GOOD: Always predictable
var a = [undefined, undefined, undefined];
var b = [1, 2];

Error Handling
// Proper try-catch usage
function parseJSON(text) {
    try {
        return JSON.parse(text);
    } catch (e) {
        console.error('Invalid JSON:', e.message);
        return null;
    }
}

// Throw with Error objects, not strings
// BAD:
throw 'Something went wrong';

// GOOD:
throw new Error('Something went wrong');

The Bad Parts to Avoid
Global Variables: Pollute the namespace, cause conflicts
eval(): Security risk, performance killer
with: Ambiguous scope, deprecated
== and !=: Type coercion causes bugs
++ and --: Encourage trickery
Bitwise Operators: Rarely needed, often misused
void: Confusing and unnecessary
Typed Wrappers: new String(), new Number(), new Boolean()
arguments: Use rest parameters instead
Automatic Semicolon Insertion: Be explicit
Mental Model

Crockford approaches JavaScript by asking:

Is this a good part? If not, avoid it entirely
Would a bug here be obvious? If not, use a safer pattern
Can this be linted? If JSLint complains, fix it
Is this clear to readers? Clarity trumps cleverness
Signature Crockford Moves
Factory functions instead of constructors
IIFE module pattern for encapsulation
Strict equality everywhere
Object literals for all object creation
Named functions for debuggability
JSLint compliance as non-negotiable
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