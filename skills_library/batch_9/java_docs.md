---
title: java-docs
url: https://skills.sh/github/awesome-copilot/java-docs
---

# java-docs

skills/github/awesome-copilot/java-docs
java-docs
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill java-docs
Summary

Javadoc best practices for documenting Java types, methods, and members.

Public and protected members require Javadoc comments; package-private and private members are encouraged, especially for complex code
Use standard tags: @param for parameters, @return for return values, @throws for exceptions, @see for cross-references, and @since for version tracking
First sentence serves as summary description and should end with a period; parameter descriptions start lowercase without periods
Use {@inheritDoc} to inherit documentation from base classes unless behavior changes significantly, and {@code} or <pre>{@code}</pre> for inline and block code snippets
SKILL.md
Java Documentation (Javadoc) Best Practices
Public and protected members should be documented with Javadoc comments.
It is encouraged to document package-private and private members as well, especially if they are complex or not self-explanatory.
The first sentence of the Javadoc comment is the summary description. It should be a concise overview of what the method does and end with a period.
Use @param for method parameters. The description starts with a lowercase letter and does not end with a period.
Use @return for method return values.
Use @throws or @exception to document exceptions thrown by methods.
Use @see for references to other types or members.
Use {@inheritDoc} to inherit documentation from base classes or interfaces.
Unless there is major behavior change, in which case you should document the differences.
Use @param <T> for type parameters in generic types or methods.
Use {@code} for inline code snippets.
Use <pre>{@code ... }</pre> for code blocks.
Use @since to indicate when the feature was introduced (e.g., version number).
Use @version to specify the version of the member.
Use @author to specify the author of the code.
Use @deprecated to mark a member as deprecated and provide an alternative.
Weekly Installs
9.4K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass