---
title: injection-checking
url: https://skills.sh/yaklang/hack-skills/injection-checking
---

# injection-checking

skills/yaklang/hack-skills/injection-checking
injection-checking
Installation
$ npx skills add https://github.com/yaklang/hack-skills --skill injection-checking
SKILL.md
Injection Testing Router

This is the routing entry point when input reaches a dangerous interpreter or execution environment.

After confirming this is an injection-class issue, use it to decide whether it is mainly browser context, database, template engine, server-side requests, XML parsing, or system commands.

When to Use
Input reaches HTML, JS, SQL, templates, URL fetchers, XML parsers, or shell
You have not yet decided whether to start with XSS, SQLi, SSRF, XXE, SSTI, CMDi, or NoSQL
You need to choose the correct deep-topic skill based on input flow
Skill Map
XSS Cross Site Scripting
SQLi SQL Injection
SSRF Server Side Request Forgery
XXE XML External Entity
SSTI Server Side Template Injection
CMDi Command Injection
NoSQL Injection
Deserialization Insecure
JNDI Injection
Expression Language Injection
CRLF Injection
Extra Injection Types (SSI, LDAP, XPath)
Request Smuggling
Prototype Pollution
Type Juggling
HTTP Parameter Pollution
XSLT Injection
CSV Formula Injection
Recommended Flow
First identify the final sink of the input
Then choose the topic skill that best matches that interpreter
Small payload samples and quick triage are merged into each main skill; no extra payload router is needed
Related Categories
file-access-vuln
Weekly Installs
330
Repository
yaklang/hack-skills
GitHub Stars
368
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykFail