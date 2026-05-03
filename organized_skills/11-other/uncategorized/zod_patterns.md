---
rating: ⭐⭐
title: zod-patterns
url: https://skills.sh/mx-space/core/zod-patterns
---

# zod-patterns

skills/mx-space/core/zod-patterns
zod-patterns
Installation
$ npx skills add https://github.com/mx-space/core --skill zod-patterns
SKILL.md
Zod Schema Patterns
Basic Pattern
import { z } from 'zod'
import { createZodDto } from 'nestjs-zod'

// Define Schema
export const MySchema = z.object({
  name: z.string().min(1),
  email: z.string().email(),
  age: z.number().int().positive().optional(),
})

// Create DTO class
export class MyDto extends createZodDto(MySchema) {}

// Partial DTO for updates
export class PartialMyDto extends createZodDto(MySchema.partial()) {}

Project Custom Validators

Location: apps/core/src/shared/schema/base.schema.ts

import {
  zMongoId,           // MongoDB ObjectId validation
  zNonEmptyString,    // Non-empty string
  zArrayUnique,       // Unique array elements
  zPinDate,           // Pin date validation
} from '~/shared/schema/base.schema'

const Schema = z.object({
  id: zMongoId,
  title: zNonEmptyString,
  tags: zArrayUnique(z.string()),
  pin: zPinDate,
})

Extending Base Schemas
import { WriteBaseSchema } from '~/shared/schema/write-base.schema'
import { ImageSchema } from '~/shared/schema/image.schema'

// Extend WriteBaseSchema (includes title, text, images, etc.)
export const PostSchema = WriteBaseSchema.extend({
  slug: zNonEmptyString,
  categoryId: zMongoId,
  tags: zArrayUnique(z.string()).optional(),
})

Common Patterns
Optional Fields with Defaults
z.boolean().default(true).optional()
z.number().default(0).optional()
z.array(z.string()).default([]).optional()

Preprocessing
// Empty string to null
z.preprocess(
  (val) => (val === '' ? null : val),
  z.string().nullable()
).optional()

// String to number
z.preprocess(
  (val) => (typeof val === 'string' ? parseInt(val, 10) : val),
  z.number()
)

Union Types
z.union([z.string(), z.number()])
z.enum(['draft', 'published', 'archived'])

Array Validation
// Basic array
z.array(z.string())

// Length constraints
z.array(z.string()).min(1).max(10)

// Unique elements
zArrayUnique(z.string())

Nested Objects
const AddressSchema = z.object({
  street: z.string(),
  city: z.string(),
})

const UserSchema = z.object({
  name: z.string(),
  address: AddressSchema.optional(),
  addresses: z.array(AddressSchema).optional(),
})

Conditional Validation
// refine for custom validation
z.object({
  password: z.string(),
  confirmPassword: z.string(),
}).refine(
  (data) => data.password === data.confirmPassword,
  { message: 'Passwords must match' }
)

Mapping to TypeGoose Models
// Model
export class PostModel extends WriteBaseModel {
  @prop({ required: true })
  slug!: string

  @prop({ type: () => [String] })
  tags?: string[]
}

// Schema
export const PostSchema = WriteBaseSchema.extend({
  slug: zNonEmptyString,           // Maps to required
  tags: z.array(z.string()).optional(), // Maps to optional field
})

Type Inference
// Infer type from Schema
type MyType = z.infer<typeof MySchema>

// Use in Service
async create(data: z.infer<typeof MySchema>) {
  return this.model.create(data)
}

Weekly Installs
37
Repository
mx-space/core
GitHub Stars
518
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass