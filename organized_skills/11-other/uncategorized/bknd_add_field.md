---
title: bknd-add-field
url: https://skills.sh/cameronapak/bknd-skills/bknd-add-field
---

# bknd-add-field

skills/cameronapak/bknd-skills/bknd-add-field
bknd-add-field
Installation
$ npx skills add https://github.com/cameronapak/bknd-skills --skill bknd-add-field
SKILL.md
Add Field to Entity

Add a new field (column) to an existing entity in Bknd.

Prerequisites
Existing Bknd entity (see bknd-create-entity)
For code mode: Access to your schema file
When to Use UI vs Code
Use UI Mode When
Quick iteration/prototyping
Non-developer adding fields
Testing field configurations before coding
Use Code Mode When
Version control needed
Reproducible schema changes
Type safety required
Team collaboration
UI Approach
Step 1: Access Entity
Start server: npx bknd run
Open http://localhost:1337
Navigate to Data section
Click on the target entity (e.g., posts)
Step 2: Add Field
Click + Add Field
Select field type from dropdown:
Text: Strings, emails, URLs
Number: Integers, decimals
Boolean: True/false
Date: Timestamps
Enum: Fixed set of values
JSON: Unstructured data
Enter field name (snake_case: first_name, created_at)
Step 3: Configure Options

Based on field type, configure:

All Types:

Required: Toggle on if field cannot be null
Default Value: Set a default

Text:

Min/Max Length
Pattern (regex validation)

Number:

Minimum/Maximum values
Multiple Of (for integers)

Enum:

Add enum values (one per line)
Step 4: Save and Sync
Click Save Field
Click Sync Database to apply changes
Code Approach
Step 1: Locate Entity Definition

Find your entity in the schema:

const schema = em({
  posts: entity("posts", {
    title: text().required(),
    // Add new fields here
  }),
});

Step 2: Add Field

Add the new field to the entity's field object:

const schema = em({
  posts: entity("posts", {
    title: text().required(),
    subtitle: text(),           // NEW: optional text field
    view_count: number(),       // NEW: optional number field
  }),
});

Step 3: Restart Server

Bknd auto-syncs schema on startup. Restart your server to apply changes.

Field Types Reference
Text Field
import { text } from "bknd";

entity("users", {
  // Basic optional text
  bio: text(),

  // Required text
  email: text().required(),

  // Unique constraint
  username: text().unique(),

  // With validation
  slug: text({
    minLength: 3,
    maxLength: 100,
    pattern: "^[a-z0-9-]+$",
  }).required(),

  // With default value
  status: text({ default_value: "active" }),
})

Number Field
import { number } from "bknd";

entity("products", {
  // Basic number
  quantity: number(),

  // Required with validation
  price: number({
    minimum: 0,
    maximum: 99999.99,
  }).required(),

  // Integer only (multipleOf: 1)
  rating: number({
    minimum: 1,
    maximum: 5,
    multipleOf: 1,
  }),
})

Boolean Field
import { boolean } from "bknd";

entity("posts", {
  // Defaults to false
  published: boolean(),

  // Default true
  active: boolean({ default_value: true }),
})

Date Field
import { date } from "bknd";

entity("events", {
  // Basic date
  start_date: date().required(),

  // Auto-set to current time
  created_at: date({ default_value: "now" }),
})

Enum Field

Note: Import is enumm (double 'm') to avoid JS reserved word.

import { enumm } from "bknd";

entity("posts", {
  // Array syntax
  status: enumm({
    enum: ["draft", "published", "archived"],
    default_value: "draft",
  }).required(),

  // Object syntax (key-value)
  priority: enumm({
    enum: {
      LOW: "low",
      MEDIUM: "medium",
      HIGH: "high",
    },
    default_value: "MEDIUM",
  }),
})

JSON Field
import { json } from "bknd";

entity("users", {
  // Untyped JSON
  metadata: json(),

  // Typed JSON (TypeScript only, no runtime validation)
  preferences: json<{
    theme: "light" | "dark";
    notifications: boolean;
  }>(),

  // With default
  tags: json<string[]>({ default_value: [] }),
})

JSON Schema Field

For runtime-validated JSON:

import { jsonschema } from "bknd";

entity("webhooks", {
  payload: jsonschema({
    type: "object",
    properties: {
      event: { type: "string" },
      timestamp: { type: "number" },
    },
    required: ["event", "timestamp"],
  }),
})

Media Field

For file attachments:

import { media } from "bknd";

entity("posts", {
  // Single file
  cover_image: media({ entity: "posts" }),

  // Multiple files with constraints
  gallery: media({
    entity: "posts",
    min_items: 1,
    max_items: 10,
    mime_types: ["image/jpeg", "image/png", "image/webp"],
  }),
})

Field Modifiers

Chain modifiers after field type:

Modifier	Description	Example
.required()	Cannot be null	text().required()
.unique()	Unique constraint	text().unique()
.default(value)	Default value	text().default("pending")
.references(target)	Foreign key	number().references("users.id")

Chaining example:

entity("users", {
  email: text().required().unique(),
  role: text().default("user"),
  org_id: number().references("organizations.id"),
})

Field Naming Conventions
Convention	Example	Notes
snake_case	first_name	NOT firstName
Lowercase	created_at	NOT CreatedAt
Descriptive	published_at	NOT pub
Common Pitfalls
Field Already Exists

Error: Field "title" already exists on entity "posts"

Fix: Each field name must be unique within an entity. Choose a different name.

Invalid Field Name

Error: Invalid field name

Fix: Use lowercase letters, numbers, and underscores. Must start with letter.

// Valid
title: text()
first_name: text()
item_2: text()

// Invalid
Title: text()        // No uppercase
2_item: text()       // Can't start with number
first-name: text()   // No hyphens

Enum Import Mistake

Error: enum is a reserved word

Fix: Import and use enumm (double 'm'):

// Wrong
import { enum } from "bknd";

// Correct
import { enumm } from "bknd";

status: enumm({ enum: ["a", "b"] })

Missing Required Modifier on Existing Data

Problem: Adding .required() to field on entity with existing null values.

Fix: Either:

Update existing records to have non-null values first
Add a default value: text({ default_value: "N/A" }).required()
Keep field optional
Field Changes Not Reflecting

Problem: Added field in code but not appearing.

Fixes:

Restart the server (schema syncs on startup)
Verify field is in the correct entity definition
Check for syntax errors in schema
Verification
UI Mode
Click on entity in Data section
Verify new field appears in field list
Create a test record with the new field
Code Mode
const api = app.getApi();

// Create record with new field
const result = await api.data.createOne("posts", {
  title: "Test",
  subtitle: "New field test",  // Your new field
});
console.log(result);

CLI Check
npx bknd debug paths
# Check entity fields in output

DOs and DON'Ts

DO:

Use snake_case for field names
Start with optional fields; make required later if needed
Add default values for required fields on existing data
Use appropriate field types (don't store numbers as text)

DON'T:

Use enum import (use enumm)
Add .required() to existing entities without defaults
Use camelCase or PascalCase for field names
Create redundant fields (e.g., id is auto-generated)
Related Skills
bknd-create-entity - Create a new entity first
bknd-define-relationship - Add relationships between entities
bknd-modify-schema - Rename or change field types
bknd-crud-create - Insert data using new fields
Weekly Installs
13
Repository
cameronapak/bknd-skills
GitHub Stars
3
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass