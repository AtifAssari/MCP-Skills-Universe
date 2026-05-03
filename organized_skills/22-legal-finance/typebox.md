---
rating: ⭐⭐
title: typebox
url: https://skills.sh/epicenterhq/epicenter/typebox
---

# typebox

skills/epicenterhq/epicenter/typebox
typebox
Installation
$ npx skills add https://github.com/epicenterhq/epicenter --skill typebox
SKILL.md
TypeBox and TypeMap
Package Names

Use typebox, not @sinclair/typebox. The @sinclair/typebox package is deprecated.

// Correct
import { Type } from 'typebox';
import { Compile } from 'typebox/compile';
import { Value } from 'typebox/value';

// Wrong - deprecated
import { Type } from '@sinclair/typebox';

When to Use What
Need	Use
Define schemas	typebox with Type.*
Standard Schema support	@sinclair/typemap
Translate between libraries	@sinclair/typemap
High-performance validation	Compile() from either
One-off validation	Value.Check() from typebox
TypeMap for Standard Schema

TypeBox doesn't implement Standard Schema natively. Use TypeMap:

import { Compile } from '@sinclair/typemap';
import { Type } from 'typebox';

// From TypeBox schema
const validator = Compile(
	Type.Object({
		name: Type.String(),
		age: Type.Number(),
	}),
);

// Standard Schema interface
const result = validator['~standard'].validate({ name: 'Alice', age: 30 });

TypeMap Accepts Everything

Compile() from TypeMap accepts:

import { Compile } from '@sinclair/typemap';

// TypeScript syntax strings
const v1 = Compile(`{ name: string, age: number }`);

// TypeBox schemas
const v2 = Compile(Type.Object({ x: Type.Number() }));

// Zod schemas
const v3 = Compile(z.object({ x: z.number() }));

// Valibot schemas
const v4 = Compile(v.object({ x: v.number() }));


All return validators with ['~standard'].validate().

TypeBox Compile vs TypeMap Compile
// TypeBox Compile - returns Validator with Check/Parse
import { Compile } from 'typebox/compile';
const validator = Compile(schema);
validator.Check(value); // boolean
validator.Parse(value); // throws or returns typed value

// TypeMap Compile - returns Standard Schema validator
import { Compile } from '@sinclair/typemap';
const validator = Compile(schema);
validator['~standard'].validate(value); // { value } or { issues }


Use TypeMap when you need Standard Schema compatibility. Use TypeBox directly when you don't.

Translation Functions

TypeMap translates between libraries:

import { Syntax, TypeBox, Zod, Valibot } from '@sinclair/typemap';

const syntax = `{ name: string }`;
const tbSchema = TypeBox(syntax);
const zodSchema = Zod(syntax);
const valibotSchema = Valibot(syntax);
const backToSyntax = Syntax(zodSchema);

Performance

TypeMap's compiled validators are ~100x faster than native Zod:

Library	10M iterations
Zod native	~4,669ms
TypeMap	~47ms
References
TypeMap is the Real Deal
TypeBox is a Beast
Why TypeBox Won't Implement Standard Schema
Weekly Installs
59
Repository
epicenterhq/epicenter
GitHub Stars
4.5K
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass