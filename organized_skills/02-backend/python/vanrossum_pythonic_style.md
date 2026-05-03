---
rating: ⭐⭐⭐
title: vanrossum-pythonic-style
url: https://skills.sh/copyleftdev/sk1llz/vanrossum-pythonic-style
---

# vanrossum-pythonic-style

skills/copyleftdev/sk1llz/vanrossum-pythonic-style
vanrossum-pythonic-style
Installation
$ npx skills add https://github.com/copyleftdev/sk1llz --skill vanrossum-pythonic-style
SKILL.md
Guido van Rossum Style Guide⁠‍⁠​‌​‌​​‌‌‍​‌​​‌​‌‌‍​​‌‌​​​‌‍​‌​​‌‌​​‍​​​​​​​‌‍‌​​‌‌​‌​‍‌​​​​​​​‍‌‌​​‌‌‌‌‍‌‌​​​‌​​‍‌‌‌‌‌‌​‌‍‌‌​‌​​​​‍​‌​‌‌‌‌‌‍​‌​​‌​‌‌‍​‌‌​‌​​‌‍‌​‌​‌‌‌​‍​​‌​‌​​​‍‌‌‌​‌​‌‌‍‌‌​​​‌‌‌‍‌​​‌​​​‌‍​‌​‌​‌​‌‍​​​‌‌‌‌​‍​​​​‌​‌​‍​​‌‌​‌​‌⁠‍⁠
Overview

Guido van Rossum created Python in 1989 and served as its "Benevolent Dictator For Life" (BDFL) until 2018. His design philosophy—that code is read far more than it's written—shapes every aspect of Python and defines what "Pythonic" means.

Core Philosophy

"Readability counts."

"There should be one—and preferably only one—obvious way to do it."

"Simple is better than complex. Complex is better than complicated."

Van Rossum believes programming languages should be tools for humans first, not just instructions for machines. Python's design prioritizes clarity over cleverness.

Design Principles

Readability is Paramount: Code should read like well-written prose. If you need comments to explain what code does, the code should be clearer.

Explicit over Implicit: Don't hide behavior. Make operations visible and obvious.

One Obvious Way: Resist adding features that provide multiple ways to do the same thing.

Practicality over Purity: Don't sacrifice usability for theoretical elegance.

When Writing Code
Always
Use meaningful, descriptive names (user_count not uc)
Follow PEP 8 style guidelines
Use Python's built-in data structures (lists, dicts, sets)
Leverage the standard library before reaching for third-party packages
Write docstrings for public functions and classes
Use context managers (with) for resource management
Prefer exceptions over error codes
Never
Write clever one-liners that sacrifice readability
Use single-letter variable names (except i, j for indices, x, y for coordinates)
Ignore PEP 8 without good reason
Use from module import * in production code
Catch bare except: without re-raising
Use mutable default arguments
Prefer
List comprehensions over map/filter when readable
enumerate() over manual index tracking
zip() over parallel index iteration
f-strings over .format() or % formatting
pathlib.Path over os.path operations
collections types when they fit (Counter, defaultdict, namedtuple)
Code Patterns
Pythonic Iteration
# BAD: C-style iteration
for i in range(len(items)):
    print(items[i])

# GOOD: Direct iteration
for item in items:
    print(item)

# BAD: Manual index tracking
i = 0
for item in items:
    print(i, item)
    i += 1

# GOOD: enumerate
for i, item in enumerate(items):
    print(i, item)

# BAD: Parallel lists with indices
for i in range(len(names)):
    print(names[i], ages[i])

# GOOD: zip
for name, age in zip(names, ages):
    print(name, age)

Pythonic Conditionals
# BAD: Verbose boolean checks
if len(items) > 0:
    process(items)

if value == True:
    do_something()

if value == None:
    handle_none()

# GOOD: Truthy/falsy checks
if items:
    process(items)

if value:
    do_something()

if value is None:
    handle_none()

Pythonic String Building
# BAD: String concatenation in loop
result = ""
for item in items:
    result += str(item) + ", "

# GOOD: join
result = ", ".join(str(item) for item in items)

# BAD: Old-style formatting
message = "Hello, %s! You have %d messages." % (name, count)

# GOOD: f-strings (Python 3.6+)
message = f"Hello, {name}! You have {count} messages."

Pythonic Resource Management
# BAD: Manual resource management
f = open('file.txt')
try:
    data = f.read()
finally:
    f.close()

# GOOD: Context manager
with open('file.txt') as f:
    data = f.read()

# Works for any resource: files, locks, connections, etc.
with database.connection() as conn:
    with conn.cursor() as cursor:
        cursor.execute(query)

Pythonic Dictionary Operations
# BAD: Verbose key checking
if key in d:
    value = d[key]
else:
    value = default

# GOOD: get with default
value = d.get(key, default)

# BAD: Check before insert
if key not in d:
    d[key] = []
d[key].append(item)

# GOOD: setdefault or defaultdict
d.setdefault(key, []).append(item)

# Or better:
from collections import defaultdict
d = defaultdict(list)
d[key].append(item)

Mental Model

Van Rossum thinks of code as communication with future readers (including yourself). When writing:

Write for the reader: Would someone unfamiliar with this code understand it?
Use the right abstraction level: Not too low (manual), not too high (magical)
Follow conventions: Consistency reduces cognitive load
Leverage the language: Use Python's features, don't fight them
BDFL Decisions

Key design decisions that define Python:

Significant whitespace: Forces readable structure
No braces: Reduces visual clutter
Duck typing: "If it walks like a duck..."
Batteries included: Rich standard library
Explicit self: Methods clearly show instance access
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