---
title: knitwork-x
url: https://skills.sh/hairyf/knitwork-x/knitwork-x
---

# knitwork-x

skills/hairyf/knitwork-x/knitwork-x
knitwork-x
Installation
$ npx skills add https://github.com/hairyf/knitwork-x --skill knitwork-x
SKILL.md

knitwork-x provides programmatic code generation for JavaScript and TypeScript. It is forked from knitwork and adds comprehensive TypeScript helpers: ESM (import/export), strings, variables, classes, interfaces, functions, types, control flow (if/try/loop/switch), and serialization (object/array/map/set). All gen* functions return strings suitable for splicing into source; they are pure and do not mutate inputs.

Use this skill when an agent needs to generate code strings (e.g. for codegen tools, plugins, or dynamic module output).

Core References
Topic	Description	Reference
Overview	Purpose, install, when to use	core-overview
ESM	Import, export, default export, dynamic import	core-esm
String	genString, escapeString, genTemplateLiteral	core-string
Variable	genVariable, genVariableName	core-variable
Design Guidelines	Naming, params, options (for contributors)	core-design-guidelines
Features
Topic	Description	Reference
Class	genClass, genConstructor, genProperty, genMethod, getter/setter	features-class
Interface	genInterface, genIndexSignature	features-interface
Enum	genEnum, genConstEnum	features-enum
Function	genFunction, genArrowFunction, genBlock, genParam	features-function
Type	genTypeAlias, genUnion, genIntersection, genMappedType, etc.	features-type
Conditional	genConditionalType, genTernary	features-conditional
Decorator	genDecorator	features-decorator
Module & Namespace	genModule, genNamespace, genDeclareNamespace	features-module-namespace
Condition	genIf, genElse, genElseIf	features-condition
Try	genTry, genCatch, genFinally	features-try
Loop	genFor, genForOf, genWhile, genDoWhile	features-loop
Switch	genSwitch, genCase, genDefault	features-switch
Statement	genReturn, genThrow, genPrefixedBlock	features-statement
Object & Serialization	genObject, genArray, genMap, genSet, genTypeObject	features-object
Utils	genComment, genKey, genLiteral, genRegExp, wrapInDelimiters	features-utils
Key Points
Return type: Every gen* function returns a string (code fragment).
Options: Most accept an optional options object (e.g. export, singleQuotes, indent); default to {}.
Indent: When supported, pass indent as the last parameter; use indent + " " for nested blocks.
Strings: Use genString(input, options) for quoted/escaped output so singleQuotes is respected.
Composing: Combine gen* outputs (e.g. genClass(..., [genConstructor(...)])) to build larger snippets.
Weekly Installs
307
Repository
hairyf/knitwork-x
GitHub Stars
3
First Seen
Feb 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass