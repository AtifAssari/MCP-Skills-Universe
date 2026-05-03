---
rating: ⭐⭐⭐
title: payload
url: https://skills.sh/payloadcms/skills/payload
---

# payload

skills/payloadcms/skills/payload
payload
Installation
$ npx skills add https://github.com/payloadcms/skills --skill payload
Summary

TypeScript-first Next.js CMS with admin panel, REST/GraphQL APIs, and row-level access control.

Collections, fields, hooks, and access control with type-safe patterns; supports drafts, versioning, relationships, and virtual fields
Local API, REST, and GraphQL query interfaces with nested property filtering, AND/OR logic, and depth-based relationship population
Critical security patterns: Local API access control requires overrideAccess: false to enforce permissions; transactions need req threading; hook context flags prevent infinite loops
Database and storage adapters, multi-language localization, background jobs queue, custom endpoints, and plugin architecture for extensibility
SKILL.md
Payload Application Development

Payload is a Next.js native CMS with TypeScript-first architecture, providing admin panel, database management, REST/GraphQL APIs, authentication, and file storage.

Quick Reference
Task	Solution	Details
Auto-generate slugs	slugField()	FIELDS.md#slug-field-helper
Restrict content by user	Access control with query	ACCESS-CONTROL.md#row-level-security-with-complex-queries
Local API user ops	user + overrideAccess: false	QUERIES.md#access-control-in-local-api
Draft/publish workflow	versions: { drafts: true }	COLLECTIONS.md#versioning--drafts
Computed fields	virtual: true with afterRead	FIELDS.md#virtual-fields
Conditional fields	admin.condition	FIELDS.md#conditional-fields
Custom field validation	validate function	FIELDS.md#text-field
Filter relationship list	filterOptions on field	FIELDS.md#relationship
Select specific fields	select parameter	QUERIES.md#local-api
Auto-set author/dates	beforeChange hook	HOOKS.md#collection-hooks
Prevent hook loops	req.context check	HOOKS.md#hook-context
Cascading deletes	beforeDelete hook	HOOKS.md#collection-hooks
Geospatial queries	point field with near/within	FIELDS.md#point-geolocation
Reverse relationships	join field type	FIELDS.md#join-fields
Next.js revalidation	Context control in afterChange	HOOKS.md#nextjs-revalidation-with-context-control
Query by relationship	Nested property syntax	QUERIES.md#nested-properties
Complex queries	AND/OR logic	QUERIES.md#andor-logic
Transactions	Pass req to operations	ADAPTERS.md#threading-req-through-operations
Background jobs	Jobs queue with tasks	ADVANCED.md#jobs-queue
Custom API routes	Collection custom endpoints	ADVANCED.md#custom-endpoints
Cloud storage	Storage adapter plugins	ADAPTERS.md#storage-adapters
Multi-language	localization config + localized: true	ADVANCED.md#localization
Create plugin	(options) => (config) => Config	PLUGIN-DEVELOPMENT.md#plugin-architecture
Plugin package setup	Package structure with SWC	PLUGIN-DEVELOPMENT.md#plugin-package-structure
Add fields to collection	Map collections, spread fields	PLUGIN-DEVELOPMENT.md#adding-fields-to-collections
Plugin hooks	Preserve existing hooks in array	PLUGIN-DEVELOPMENT.md#adding-hooks
Check field type	Type guard functions	FIELD-TYPE-GUARDS.md
Quick Start
npx create-payload-app@latest my-app
cd my-app
pnpm dev

Minimal Config
import { buildConfig } from 'payload'
import { mongooseAdapter } from '@payloadcms/db-mongodb'
import { lexicalEditor } from '@payloadcms/richtext-lexical'
import path from 'path'
import { fileURLToPath } from 'url'

const filename = fileURLToPath(import.meta.url)
const dirname = path.dirname(filename)

export default buildConfig({
  admin: {
    user: 'users',
    importMap: {
      baseDir: path.resolve(dirname),
    },
  },
  collections: [Users, Media],
  editor: lexicalEditor(),
  secret: process.env.PAYLOAD_SECRET,
  typescript: {
    outputFile: path.resolve(dirname, 'payload-types.ts'),
  },
  db: mongooseAdapter({
    url: process.env.DATABASE_URL,
  }),
})

Essential Patterns
Basic Collection
import type { CollectionConfig } from 'payload'

export const Posts: CollectionConfig = {
  slug: 'posts',
  admin: {
    useAsTitle: 'title',
    defaultColumns: ['title', 'author', 'status', 'createdAt'],
  },
  fields: [
    { name: 'title', type: 'text', required: true },
    { name: 'slug', type: 'text', unique: true, index: true },
    { name: 'content', type: 'richText' },
    { name: 'author', type: 'relationship', relationTo: 'users' },
  ],
  timestamps: true,
}


For more collection patterns (auth, upload, drafts, live preview), see COLLECTIONS.md.

Common Fields
// Text field
{ name: 'title', type: 'text', required: true }

// Relationship
{ name: 'author', type: 'relationship', relationTo: 'users', required: true }

// Rich text
{ name: 'content', type: 'richText', required: true }

// Select
{ name: 'status', type: 'select', options: ['draft', 'published'], defaultValue: 'draft' }

// Upload
{ name: 'image', type: 'upload', relationTo: 'media' }


For all field types (array, blocks, point, join, virtual, conditional, etc.), see FIELDS.md.

Hook Example
export const Posts: CollectionConfig = {
  slug: 'posts',
  hooks: {
    beforeChange: [
      async ({ data, operation }) => {
        if (operation === 'create') {
          data.slug = slugify(data.title)
        }
        return data
      },
    ],
  },
  fields: [{ name: 'title', type: 'text' }],
}


For all hook patterns, see HOOKS.md. For access control, see ACCESS-CONTROL.md.

Access Control with Type Safety
import type { Access } from 'payload'
import type { User } from '@/payload-types'

// Type-safe access control
export const adminOnly: Access = ({ req }) => {
  const user = req.user as User
  return user?.roles?.includes('admin') || false
}

// Row-level access control
export const ownPostsOnly: Access = ({ req }) => {
  const user = req.user as User
  if (!user) return false
  if (user.roles?.includes('admin')) return true

  return {
    author: { equals: user.id },
  }
}

Query Example
// Local API
const posts = await payload.find({
  collection: 'posts',
  where: {
    status: { equals: 'published' },
    'author.name': { contains: 'john' },
  },
  depth: 2,
  limit: 10,
  sort: '-createdAt',
})

// Query with populated relationships
const post = await payload.findByID({
  collection: 'posts',
  id: '123',
  depth: 2, // Populates relationships (default is 2)
})
// Returns: { author: { id: "user123", name: "John" } }

// Without depth, relationships return IDs only
const post = await payload.findByID({
  collection: 'posts',
  id: '123',
  depth: 0,
})
// Returns: { author: "user123" }


For all query operators and REST/GraphQL examples, see QUERIES.md.

Getting Payload Instance
// In API routes (Next.js)
import { getPayload } from 'payload'
import config from '@payload-config'

export async function GET() {
  const payload = await getPayload({ config })

  const posts = await payload.find({
    collection: 'posts',
  })

  return Response.json(posts)
}

// In Server Components
import { getPayload } from 'payload'
import config from '@payload-config'

export default async function Page() {
  const payload = await getPayload({ config })
  const { docs } = await payload.find({ collection: 'posts' })

  return <div>{docs.map(post => <h1 key={post.id}>{post.title}</h1>)}</div>
}

Logger Usage
// ✅ Valid: single string
payload.logger.error('Something went wrong')

// ✅ Valid: object with msg and err
payload.logger.error({ msg: 'Failed to process', err: error })

// ❌ Invalid: don't pass error as second argument
payload.logger.error('Failed to process', error)

// ❌ Invalid: use `err` not `error`, use `msg` not `message`
payload.logger.error({ message: 'Failed', error: error })

Security Pitfalls
1. Local API Access Control (CRITICAL)

By default, Local API operations bypass ALL access control, even when passing a user.

// ❌ SECURITY BUG: Passes user but ignores their permissions
await payload.find({
  collection: 'posts',
  user: someUser, // Access control is BYPASSED!
})

// ✅ SECURE: Actually enforces the user's permissions
await payload.find({
  collection: 'posts',
  user: someUser,
  overrideAccess: false, // REQUIRED for access control
})


When to use each:

overrideAccess: true (default) - Server-side operations you trust (cron jobs, system tasks)
overrideAccess: false - When operating on behalf of a user (API routes, webhooks)

See QUERIES.md#access-control-in-local-api.

2. Transaction Failures in Hooks

Nested operations in hooks without req break transaction atomicity.

// ❌ DATA CORRUPTION RISK: Separate transaction
hooks: {
  afterChange: [
    async ({ doc, req }) => {
      await req.payload.create({
        collection: 'audit-log',
        data: { docId: doc.id },
        // Missing req - runs in separate transaction!
      })
    },
  ]
}

// ✅ ATOMIC: Same transaction
hooks: {
  afterChange: [
    async ({ doc, req }) => {
      await req.payload.create({
        collection: 'audit-log',
        data: { docId: doc.id },
        req, // Maintains atomicity
      })
    },
  ]
}


See ADAPTERS.md#threading-req-through-operations.

3. Infinite Hook Loops

Hooks triggering operations that trigger the same hooks create infinite loops.

// ❌ INFINITE LOOP
hooks: {
  afterChange: [
    async ({ doc, req }) => {
      await req.payload.update({
        collection: 'posts',
        id: doc.id,
        data: { views: doc.views + 1 },
        req,
      }) // Triggers afterChange again!
    },
  ]
}

// ✅ SAFE: Use context flag
hooks: {
  afterChange: [
    async ({ doc, req, context }) => {
      if (context.skipHooks) return

      await req.payload.update({
        collection: 'posts',
        id: doc.id,
        data: { views: doc.views + 1 },
        context: { skipHooks: true },
        req,
      })
    },
  ]
}


See HOOKS.md#context.

Project Structure
src/
├── app/
│   ├── (frontend)/
│   │   └── page.tsx
│   └── (payload)/
│       └── admin/[[...segments]]/page.tsx
├── collections/
│   ├── Posts.ts
│   ├── Media.ts
│   └── Users.ts
├── globals/
│   └── Header.ts
├── components/
│   └── CustomField.tsx
├── hooks/
│   └── slugify.ts
└── payload.config.ts

Type Generation
// payload.config.ts
export default buildConfig({
  typescript: {
    outputFile: path.resolve(dirname, 'payload-types.ts'),
  },
  // ...
})

// Usage
import type { Post, User } from '@/payload-types'

Reference Documentation
FIELDS.md - All field types, validation, admin options
FIELD-TYPE-GUARDS.md - Type guards for runtime field type checking and narrowing
COLLECTIONS.md - Collection configs, auth, upload, drafts, live preview
HOOKS.md - Collection hooks, field hooks, context patterns
ACCESS-CONTROL.md - Collection, field, global access control, RBAC, multi-tenant
ACCESS-CONTROL-ADVANCED.md - Context-aware, time-based, subscription-based access, factory functions, templates
QUERIES.md - Query operators, Local/REST/GraphQL APIs
ENDPOINTS.md - Custom API endpoints: authentication, helpers, request/response patterns
ADAPTERS.md - Database, storage, email adapters, transactions
ADVANCED.md - Authentication, jobs, endpoints, components, plugins, localization
PLUGIN-DEVELOPMENT.md - Plugin architecture, monorepo structure, patterns, best practices
Resources
llms-full.txt: https://payloadcms.com/llms-full.txt
Docs: https://payloadcms.com/docs
GitHub: https://github.com/payloadcms/payload
Examples: https://github.com/payloadcms/payload/tree/main/examples
Templates: https://github.com/payloadcms/payload/tree/main/templates
Weekly Installs
2.9K
Repository
payloadcms/skills
GitHub Stars
73
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn