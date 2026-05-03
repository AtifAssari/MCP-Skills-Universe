---
title: zod-4
url: https://skills.sh/prowler-cloud/prowler/zod-4
---

# zod-4

skills/prowler-cloud/prowler/zod-4
zod-4
Installation
$ npx skills add https://github.com/prowler-cloud/prowler --skill zod-4
Summary

Zod 4 schema validation patterns for forms, APIs, and type-safe parsing.

Covers breaking changes from Zod 3, including new top-level validators (z.email(), z.uuid(), z.url()) and updated object configuration syntax
Includes patterns for primitives, objects, arrays, records, tuples, unions, and discriminated unions with practical examples
Demonstrates transformations, coercion, preprocessing, refinements, and custom error handling with Zod 4's error parameter syntax
Provides React Hook Form integration example using zodResolver for form validation with type inference
SKILL.md
Breaking Changes from Zod 3
// ❌ Zod 3 (OLD)
z.string().email()
z.string().uuid()
z.string().url()
z.string().nonempty()
z.object({ name: z.string() }).required_error("Required")

// ✅ Zod 4 (NEW)
z.email()
z.uuid()
z.url()
z.string().min(1)
z.object({ name: z.string() }, { error: "Required" })

Basic Schemas
import { z } from "zod";

// Primitives
const stringSchema = z.string();
const numberSchema = z.number();
const booleanSchema = z.boolean();
const dateSchema = z.date();

// Top-level validators (Zod 4)
const emailSchema = z.email();
const uuidSchema = z.uuid();
const urlSchema = z.url();

// With constraints
const nameSchema = z.string().min(1).max(100);
const ageSchema = z.number().int().positive().max(150);
const priceSchema = z.number().min(0).multipleOf(0.01);

Object Schemas
const userSchema = z.object({
  id: z.uuid(),
  email: z.email({ error: "Invalid email address" }),
  name: z.string().min(1, { error: "Name is required" }),
  age: z.number().int().positive().optional(),
  role: z.enum(["admin", "user", "guest"]),
  metadata: z.record(z.string(), z.unknown()).optional(),
});

type User = z.infer<typeof userSchema>;

// Parsing
const user = userSchema.parse(data);  // Throws on error
const result = userSchema.safeParse(data);  // Returns { success, data/error }

if (result.success) {
  console.log(result.data);
} else {
  console.log(result.error.issues);
}

Arrays and Records
// Arrays
const tagsSchema = z.array(z.string()).min(1).max(10);
const numbersSchema = z.array(z.number()).nonempty();

// Records (objects with dynamic keys)
const scoresSchema = z.record(z.string(), z.number());
// { [key: string]: number }

// Tuples
const coordinatesSchema = z.tuple([z.number(), z.number()]);
// [number, number]

Unions and Discriminated Unions
// Simple union
const stringOrNumber = z.union([z.string(), z.number()]);

// Discriminated union (more efficient)
const resultSchema = z.discriminatedUnion("status", [
  z.object({ status: z.literal("success"), data: z.unknown() }),
  z.object({ status: z.literal("error"), error: z.string() }),
]);

Transformations
// Transform during parsing
const lowercaseEmail = z.email().transform(email => email.toLowerCase());

// Coercion (convert types)
const numberFromString = z.coerce.number();  // "42" → 42
const dateFromString = z.coerce.date();      // "2024-01-01" → Date

// Preprocessing
const trimmedString = z.preprocess(
  val => typeof val === "string" ? val.trim() : val,
  z.string()
);

Refinements
const passwordSchema = z.string()
  .min(8)
  .refine(val => /[A-Z]/.test(val), {
    message: "Must contain uppercase letter",
  })
  .refine(val => /[0-9]/.test(val), {
    message: "Must contain number",
  });

// With superRefine for multiple errors
const formSchema = z.object({
  password: z.string(),
  confirmPassword: z.string(),
}).superRefine((data, ctx) => {
  if (data.password !== data.confirmPassword) {
    ctx.addIssue({
      code: z.ZodIssueCode.custom,
      message: "Passwords don't match",
      path: ["confirmPassword"],
    });
  }
});

Optional and Nullable
// Optional (T | undefined)
z.string().optional()

// Nullable (T | null)
z.string().nullable()

// Both (T | null | undefined)
z.string().nullish()

// Default values
z.string().default("unknown")
z.number().default(() => Math.random())

Error Handling
// Zod 4: Use 'error' param instead of 'message'
const schema = z.object({
  name: z.string({ error: "Name must be a string" }),
  email: z.email({ error: "Invalid email format" }),
  age: z.number().min(18, { error: "Must be 18 or older" }),
});

// Custom error map
const customSchema = z.string({
  error: (issue) => {
    if (issue.code === "too_small") {
      return "String is too short";
    }
    return "Invalid string";
  },
});

React Hook Form Integration
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";

const schema = z.object({
  email: z.email(),
  password: z.string().min(8),
});

type FormData = z.infer<typeof schema>;

function Form() {
  const { register, handleSubmit, formState: { errors } } = useForm<FormData>({
    resolver: zodResolver(schema),
  });

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register("email")} />
      {errors.email && <span>{errors.email.message}</span>}
    </form>
  );
}

Weekly Installs
539
Repository
prowler-cloud/prowler
GitHub Stars
13.7K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass