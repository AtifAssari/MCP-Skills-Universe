---
title: dart-best-practices
url: https://skills.sh/kevmoo/dash_skills/dart-best-practices
---

# dart-best-practices

skills/kevmoo/dash_skills/dart-best-practices
dart-best-practices
Installation
$ npx skills add https://github.com/kevmoo/dash_skills --skill dart-best-practices
SKILL.md
Dart Best Practices
1. When to use this skill

Use this skill when:

Writing or reviewing Dart code.
Looking for guidance on idiomatic Dart usage.
2. Best Practices
Multi-line Strings

Prefer using multi-line strings (''') over concatenating strings with + and \n, especially for large blocks of text like SQL queries, HTML, or PEM-encoded keys. This improves readability and avoids lines_longer_than_80_chars lint errors by allowing natural line breaks.

Avoid:

final pem = '-----BEGIN RSA PRIVATE KEY-----\n' +
    base64Encode(fullBytes) +
    '\n-----END RSA PRIVATE KEY-----';


Prefer:

final pem = '''
-----BEGIN RSA PRIVATE KEY-----
${base64Encode(fullBytes)}
-----END RSA PRIVATE KEY-----''';

Line Length

Avoid lines longer than 80 characters, even in Markdown files and comments. This ensures code is readable in split-screen views and on smaller screens without horizontal scrolling.

Prefer: Target 80 characters for wrapping text. Exceptions are allowed for long URLs or identifiers that cannot be broken.

Discovery
Multi-line Strings

To find candidates for multi-line strings, search for string concatenation with + involving newlines:

Regex: ['"]\s*\+\s*['"]
Regex: \+\s*['"].*\\n
Line Length
Rely on the lines_longer_than_80_chars lint from the analyzer.
Related Skills
dart-modern-features: For idiomatic usage of modern Dart features like Pattern Matching (useful for deep JSON extraction), Records, and Switch Expressions.
Weekly Installs
565
Repository
kevmoo/dash_skills
GitHub Stars
131
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass