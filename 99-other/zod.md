---
rating: ⭐⭐⭐
title: zod
url: https://skills.sh/secondsky/claude-skills/zod
---

# zod

skills/secondsky/claude-skills/zod
zod
Installation
$ npx skills add https://github.com/secondsky/claude-skills --skill zod
SKILL.md
Zod: TypeScript-First Schema Validation
Overview

Zod is a TypeScript-first validation library that enables developers to define schemas for validating data at runtime while automatically inferring static TypeScript types. With zero dependencies and a 2kb core bundle (gzipped), Zod provides immutable, composable validation with comprehensive error handling.

Installation
bun add zod
# or
bun add zod
# or
bun add zod
# or
yarn add zod


Requirements:

TypeScript v5.5+ with "strict": true in tsconfig.json
Zod 4.x (4.1.12+)

Important: This skill documents Zod 4.x features. The following APIs require Zod 4 and are NOT available in Zod 3.x:

z.codec() - Bidirectional transformations
z.iso.date(), z.iso.time(), z.iso.datetime(), z.iso.duration() - ISO format validators
z.toJSONSchema() - JSON Schema generation
z.treeifyError(), z.prettifyError(), z.flattenError() - New error formatting helpers
.meta() - Enhanced metadata (Zod 3.x only has .describe())
Unified error parameter - Replaces message, invalid_type_error, required_error, errorMap

For Zod 3.x compatibility or migration guidance, see https://zod.dev

Migrating from Zod v3 to v4

Load references/migration-guide.md for complete v3 to v4 migration documentation.

Quick Summary

Zod v4 introduces breaking changes for better performance:

Error customization: Use unified error parameter (replaces message, invalid_type_error, required_error)
Number validation: Stricter - rejects Infinity and unsafe integers
String formats: Now top-level functions (z.email() vs z.string().email())
Object defaults: Applied even in optional fields
Deprecated APIs: Use .extend() (not .merge()), z.treeifyError() (not error.format())
Function validation: Use .implement() method
UUID validation: Stricter RFC 9562/4122 compliance

→ Load references/migration-guide.md for: Complete breaking changes, migration checklist, gradual migration strategy, rollback instructions

Core Concepts
Basic Usage Pattern
import { z } from "zod";

// Define schema
const UserSchema = z.object({
  username: z.string(),
  age: z.number().int().positive(),
  email: z.string().email(),
});

// Infer TypeScript type
type User = z.infer<typeof UserSchema>;

// Validate data (throws on error)
const user = UserSchema.parse(data);

// Validate data (returns result object)
const result = UserSchema.safeParse(data);
if (result.success) {
  console.log(result.data); // Typed!
} else {
  console.error(result.error); // ZodError
}

Parsing Methods

Use the appropriate parsing method based on error handling needs:

.parse(data) - Throws ZodError on invalid input; returns strongly-typed data on success
.safeParse(data) - Returns { success: true, data } or { success: false, error } (no exceptions)
.parseAsync(data) - For schemas with async refinements/transforms
.safeParseAsync(data) - Async version that doesn't throw

Best Practice: Use .safeParse() to avoid try-catch blocks and leverage discriminated unions.

Primitive Types
Strings
z.string()                    // Basic string
z.string().min(5)            // Minimum length
z.string().max(100)          // Maximum length
z.string().length(10)        // Exact length
z.string().email()           // Email validation
z.string().url()             // URL validation
z.string().uuid()            // UUID format
z.string().regex(/^\d+$/)    // Custom pattern
z.string().startsWith("pre") // Prefix check
z.string().endsWith("suf")   // Suffix check
z.string().trim()            // Auto-trim whitespace
z.string().toLowerCase()     // Auto-lowercase
z.string().toUpperCase()     // Auto-uppercase

// ISO formats (Zod 4+)
z.iso.date()                 // YYYY-MM-DD
z.iso.time()                 // HH:MM:SS
z.iso.datetime()             // ISO 8601 datetime
z.iso.duration()             // ISO 8601 duration

// Network formats
z.ipv4()                     // IPv4 address
z.ipv6()                     // IPv6 address
z.cidrv4()                   // IPv4 CIDR notation
z.cidrv6()                   // IPv6 CIDR notation

// Other formats
z.jwt()                      // JWT token
z.nanoid()                   // Nanoid
z.cuid()                     // CUID
z.cuid2()                    // CUID2
z.ulid()                     // ULID
z.base64()                   // Base64 encoded
z.hex()                      // Hexadecimal

Numbers
z.number()                   // Basic number
z.number().int()             // Integer only
z.number().positive()        // > 0
z.number().nonnegative()     // >= 0
z.number().negative()        // < 0
z.number().nonpositive()     // <= 0
z.number().min(0)            // Minimum value
z.number().max(100)          // Maximum value
z.number().gt(0)             // Greater than
z.number().gte(0)            // Greater than or equal
z.number().lt(100)           // Less than
z.number().lte(100)          // Less than or equal
z.number().multipleOf(5)     // Must be multiple of 5
z.int()                      // Shorthand for z.number().int()
z.int32()                    // 32-bit integer
z.nan()                      // NaN value

Coercion (Type Conversion)
z.coerce.string()            // Convert to string
z.coerce.number()            // Convert to number
z.coerce.boolean()           // Convert to boolean
z.coerce.bigint()            // Convert to bigint
z.coerce.date()              // Convert to Date

// Example: Parse query parameters
const QuerySchema = z.object({
  page: z.coerce.number().int().positive(),
  limit: z.coerce.number().int().max(100).default(10),
});

// "?page=5&limit=20" -> { page: 5, limit: 20 }

Other Primitives
z.boolean()                  // Boolean
z.date()                     // Date object
z.date().min(new Date("2020-01-01"))
z.date().max(new Date("2030-12-31"))
z.bigint()                   // BigInt
z.symbol()                   // Symbol
z.null()                     // Null
z.undefined()                // Undefined
z.void()                     // Void (undefined)

Complex Types
Objects
const PersonSchema = z.object({
  name: z.string(),
  age: z.number(),
  address: z.object({
    street: z.string(),
    city: z.string(),
    country: z.string(),
  }),
});

type Person = z.infer<typeof PersonSchema>;

// Object methods
PersonSchema.shape                 // Access shape
PersonSchema.keyof()              // Get union of keys
PersonSchema.extend({ role: z.string() })  // Add fields
PersonSchema.pick({ name: true }) // Pick specific fields
PersonSchema.omit({ age: true })  // Omit fields
PersonSchema.partial()            // Make all fields optional
PersonSchema.required()           // Make all fields required
PersonSchema.deepPartial()        // Recursively optional

// Strict vs loose objects
z.strictObject({ ... })           // No extra keys allowed (throws)
z.object({ ... })                 // Strips extra keys (default)
z.looseObject({ ... })            // Allows extra keys

Arrays
z.array(z.string())              // String array
z.array(z.number()).min(1)       // At least 1 element
z.array(z.number()).max(10)      // At most 10 elements
z.array(z.number()).length(5)    // Exactly 5 elements
z.array(z.number()).nonempty()   // At least 1 element

// Nested arrays
z.array(z.array(z.number()))     // number[][]

Tuples
z.tuple([z.string(), z.number()]) // [string, number]
z.tuple([z.string(), z.number()]).rest(z.boolean()) // [string, number, ...boolean[]]

Enums and Literals
// Enum
const RoleEnum = z.enum(["admin", "user", "guest"]);
type Role = z.infer<typeof RoleEnum>; // "admin" | "user" | "guest"

// Literal values
z.literal("exact_value")
z.literal(42)
z.literal(true)

// Native TypeScript enum
enum Fruits {
  Apple,
  Banana,
}
z.nativeEnum(Fruits)

// Enum methods
RoleEnum.enum.admin              // "admin"
RoleEnum.exclude(["guest"])      // Exclude values
RoleEnum.extract(["admin", "user"]) // Include only

Unions
// Basic union
z.union([z.string(), z.number()])

// Discriminated union (better performance & type inference)
const ResponseSchema = z.discriminatedUnion("status", [
  z.object({ status: z.literal("success"), data: z.any() }),
  z.object({ status: z.literal("error"), message: z.string() }),
]);

type Response = z.infer<typeof ResponseSchema>;
// { status: "success", data: any } | { status: "error", message: string }

Intersections
const BaseSchema = z.object({ id: z.string() });
const ExtendedSchema = z.object({ name: z.string() });

const Combined = z.intersection(BaseSchema, ExtendedSchema);
// Equivalent to: z.object({ id: z.string(), name: z.string() })

Records and Maps
// Record: object with typed keys and values
z.record(z.string())             // { [key: string]: string }
z.record(z.string(), z.number()) // { [key: string]: number }

// Partial record (some keys optional)
z.partialRecord(z.enum(["a", "b"]), z.string())

// Map
z.map(z.string(), z.number())    // Map<string, number>
z.set(z.string())                // Set<string>

Advanced Patterns

Load references/advanced-patterns.md for complete advanced validation and transformation patterns.

Quick Reference

Refinements (custom validation):

z.string().refine((val) => val.length >= 8, "Too short");
z.object({ password, confirmPassword }).superRefine((data, ctx) => { /* ... */ });


Transformations (modify data):

z.string().transform((val) => val.trim());
z.string().pipe(z.coerce.number());


Codecs (bidirectional transforms - NEW in v4.1):

const DateCodec = z.codec(
  z.iso.datetime(),
  z.date(),
  {
    decode: (str) => new Date(str),
    encode: (date) => date.toISOString(),
  }
);


Recursive Types:

const CategorySchema: z.ZodType<Category> = z.lazy(() =>
  z.object({ name: z.string(), subcategories: z.array(CategorySchema) })
);


Optional/Nullable:

z.string().optional()            // string | undefined
z.string().nullable()            // string | null
z.string().default("default")    // Provides default if undefined


Readonly & Brand:

z.object({ ... }).readonly()     // Readonly properties
z.string().brand<"UserId">()     // Nominal typing


→ Load references/advanced-patterns.md for: Complete refinement patterns, async validation, codec examples, composable schemas, conditional validation, performance optimization

Error Handling

Load references/error-handling.md for complete error formatting and customization guide.

Quick Reference

Error Formatting Methods:

// For forms
const { fieldErrors } = z.flattenError(error);

// For nested data
const tree = z.treeifyError(error);
const nameError = tree.properties?.user?.properties?.name?.errors?.[0];

// For debugging
console.log(z.prettifyError(error));


Custom Error Messages (three levels):

// 1. Schema-level (highest priority)
z.string({ error: "Custom message" });
z.string().min(5, "Too short");

// 2. Per-parse level
schema.parse(data, { error: (issue) => ({ message: "..." }) });

// 3. Global level
z.config({ customError: (issue) => ({ message: "..." }) });


Localization (40+ languages):

z.config(z.locales.es());  // Spanish
z.config(z.locales.fr());  // French


→ Load references/error-handling.md for: Complete error formatting examples, custom error patterns, localization setup, error code reference

Type Inference

Load references/type-inference.md for complete type inference and metadata documentation.

Quick Reference

Basic Type Inference:

const UserSchema = z.object({ name: z.string() });
type User = z.infer<typeof UserSchema>; // { name: string }


Input vs Output (for transforms):

const TransformSchema = z.string().transform((s) => s.length);
type Input = z.input<typeof TransformSchema>;   // string
type Output = z.output<typeof TransformSchema>; // number


JSON Schema Conversion:

const jsonSchema = z.toJSONSchema(UserSchema, {
  target: "openapi-3.0",
  metadata: true,
});


Metadata:

// Add metadata
const EmailSchema = z.string().email().meta({
  title: "Email Address",
  description: "User's email address",
});

// Create custom registry
const formRegistry = z.registry<FormFieldMeta>();


→ Load references/type-inference.md for: Complete type inference patterns, JSON Schema options, metadata system, custom registries, brand types

Functions

Validate function inputs and outputs:

const AddFunction = z.function()
  .args(z.number(), z.number())  // Arguments
  .returns(z.number());           // Return type

// Implement typed function
const add = AddFunction.implement((a, b) => {
  return a + b; // Type-checked!
});

// Async functions
const FetchFunction = z.function()
  .args(z.string())
  .returns(z.promise(z.object({ data: z.any() })))
  .implementAsync(async (url) => {
    const response = await fetch(url);
    return response.json();
  });

Common Patterns
Environment Variables
const EnvSchema = z.object({
  NODE_ENV: z.enum(["development", "production", "test"]),
  DATABASE_URL: z.string().url(),
  PORT: z.coerce.number().int().positive().default(3000),
  API_KEY: z.string().min(32),
});

// Validate on startup
const env = EnvSchema.parse(process.env);

// Now use typed env
console.log(env.PORT); // number

API Request Validation
const CreateUserRequest = z.object({
  username: z.string().min(3).max(20),
  email: z.string().email(),
  password: z.string().min(8),
  age: z.number().int().positive().optional(),
});

// Express example
app.post("/users", async (req, res) => {
  const result = CreateUserRequest.safeParse(req.body);

  if (!result.success) {
    return res.status(400).json({
      errors: z.flattenError(result.error).fieldErrors,
    });
  }

  const user = await createUser(result.data);
  res.json(user);
});

Form Validation
const FormSchema = z.object({
  firstName: z.string().min(1, "First name required"),
  lastName: z.string().min(1, "Last name required"),
  email: z.string().email("Invalid email"),
  age: z.coerce.number().int().min(18, "Must be 18+"),
  agreeToTerms: z.literal(true, {
    errorMap: () => ({ message: "Must accept terms" }),
  }),
});

type FormData = z.infer<typeof FormSchema>;

Partial Updates
const UserSchema = z.object({
  id: z.string(),
  name: z.string(),
  email: z.string().email(),
});

// For PATCH requests: make everything optional except id
const UpdateUserSchema = UserSchema.partial().required({ id: true });

type UpdateUser = z.infer<typeof UpdateUserSchema>;
// { id: string; name?: string; email?: string }

Composable Schemas
// Base schemas
const TimestampSchema = z.object({
  createdAt: z.date(),
  updatedAt: z.date(),
});

const AuthorSchema = z.object({
  authorId: z.string(),
  authorName: z.string(),
});

// Compose into larger schemas
const PostSchema = z.object({
  id: z.string(),
  title: z.string(),
  content: z.string(),
}).merge(TimestampSchema).merge(AuthorSchema);

Ecosystem Integration

Load references/ecosystem-integrations.md for complete framework and tooling integration guide.

Quick Reference

ESLint Plugins:

eslint-plugin-zod-x - Enforces best practices
eslint-plugin-import-zod - Enforces import style

Framework Integrations:

tRPC - End-to-end typesafe APIs
React Hook Form - Form validation (see react-hook-form-zod skill)
Prisma - Generate Zod from database models
NestJS - DTOs and validation pipes

Code Generation:

orval - OpenAPI → Zod
Hey API - OpenAPI to TypeScript + Zod
kubb - API toolkit with codegen

→ Load references/ecosystem-integrations.md for: Setup instructions, integration examples, Hono middleware, Drizzle ORM patterns

Troubleshooting

Load references/troubleshooting.md for complete troubleshooting guide, performance tips, and best practices.

Quick Reference

Common Issues:

TypeScript strict mode required → Enable in tsconfig.json
Large bundle size → Use z.lazy() for code splitting
Slow async refinements → Cache or debounce
Circular dependencies → Use z.lazy()
Slow unions → Use z.discriminatedUnion()
Transform vs refine confusion → Use .refine() for validation, .transform() for modification

Performance Tips:

Use .discriminatedUnion() (5-10x faster than .union())
Cache schema instances
Use .safeParse() (avoids try-catch overhead)
Lazy load large schemas

Best Practices:

Define schemas at module level
Use type inference (z.infer)
Add custom error messages
Validate at system boundaries
Compose small schemas
Document with .meta()

→ Load references/troubleshooting.md for: Detailed solutions, performance optimization, best practices, testing patterns

Quick Reference
// Primitives
z.string(), z.number(), z.boolean(), z.date(), z.bigint()

// Collections
z.array(), z.tuple(), z.object(), z.record(), z.map(), z.set()

// Special types
z.enum(), z.union(), z.discriminatedUnion(), z.intersection()
z.literal(), z.any(), z.unknown(), z.never()

// Modifiers
.optional(), .nullable(), .nullish(), .default(), .catch()
.readonly(), .brand()

// Validation
.min(), .max(), .length(), .regex(), .email(), .url(), .uuid()
.refine(), .superRefine()

// Transformation
.transform(), .pipe(), .codec()

// Parsing
.parse(), .safeParse(), .parseAsync(), .safeParseAsync()

// Type inference
z.infer<typeof Schema>, z.input<typeof Schema>, z.output<typeof Schema>

// Error handling
z.flattenError(), z.treeifyError(), z.prettifyError()

// JSON Schema
z.toJSONSchema(schema, options)

// Metadata
.meta(), .describe()

// Object methods
.extend(), .pick(), .omit(), .partial(), .required(), .merge()

When to Load References

Load references/migration-guide.md when:

Upgrading from Zod v3 to v4
Questions about breaking changes
Need migration checklist or rollback strategy
Errors related to deprecated APIs (.merge(), error.format(), etc.)
Number validation issues with Infinity or unsafe integers

Load references/error-handling.md when:

Need to format errors for forms or UI
Implementing custom error messages
Questions about z.flattenError(), z.treeifyError(), or z.prettifyError()
Setting up localization for error messages
Need error code reference or pattern examples

Load references/advanced-patterns.md when:

Implementing custom refinements or async validation
Need bidirectional transformations (codecs)
Working with recursive types or self-referential data
Questions about .refine(), .transform(), or .codec()
Need performance optimization patterns
Implementing conditional validation

Load references/type-inference.md when:

Questions about TypeScript type inference
Need to generate JSON Schema for OpenAPI or AI
Implementing metadata system for forms or documentation
Need custom registries for type-safe metadata
Questions about z.infer, z.input, z.output
Using brand types for ID safety

Load references/ecosystem-integrations.md when:

Integrating with tRPC, React Hook Form, Prisma, or NestJS
Setting up ESLint plugins for best practices
Generating Zod schemas from OpenAPI (orval, Hey API, kubb)
Questions about Hono middleware or Drizzle ORM
Need framework-specific integration examples

Load references/troubleshooting.md when:

Encountering TypeScript strict mode errors
Bundle size concerns or lazy loading needs
Performance issues with large unions or async refinements
Questions about circular dependencies
Need best practices or testing patterns
Confusion between .refine() and .transform()
Additional Resources
Official Docs: https://zod.dev
GitHub: https://github.com/colinhacks/zod
TypeScript Playground: https://zod-playground.vercel.app
ESLint Plugin (Best Practices): https://github.com/JoshuaKGoldberg/eslint-plugin-zod-x
tRPC Integration: https://trpc.io
Ecosystem: https://zod.dev/ecosystem

Production Notes:

Package version: 4.1.12+ (Zod 4.x stable)
Zero dependencies
Bundle size: 2kb (gzipped)
TypeScript 5.5+ required
Strict mode required
Last verified: 2025-11-17
Skill version: 2.0.0 (Updated with v4.1 enhancements)

What's New in This Version:

✨ Comprehensive v3 to v4 migration guide with breaking changes
✨ Enhanced error customization with three-level system
✨ Expanded metadata API with registry system
✨ Improved error formatting with practical examples
✨ Built-in localization support for 40+ locales
✨ Detailed codec documentation with real-world patterns
✨ Performance improvements and architectural changes explained
Weekly Installs
298
Repository
secondsky/claude-skills
GitHub Stars
129
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass