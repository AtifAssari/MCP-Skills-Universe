---
title: bknd-create-entity
url: https://skills.sh/cameronapak/bknd-skills/bknd-create-entity
---

# bknd-create-entity

skills/cameronapak/bknd-skills/bknd-create-entity
bknd-create-entity
Installation
$ npx skills add https://github.com/cameronapak/bknd-skills --skill bknd-create-entity
SKILL.md
Create Entity

Create a new entity (database table) in Bknd. Entities are the foundation of your data model.

Prerequisites
Bknd project initialized (npx bknd create or existing project)
For code mode: TypeScript project with bknd package installed
When to Use UI vs Code
Use UI Mode When
Exploring/prototyping quickly
Non-developer or visual learner
Making one-off changes
Testing schema ideas before committing to code
Use Code Mode When
Version control needed
Reproducible setups across environments
Team collaboration
CI/CD pipelines
Type safety required
UI Approach
Step 1: Access Admin Panel
Start your Bknd server: npx bknd run
Open browser to http://localhost:1337 (default port)
Navigate to Data section in sidebar
Step 2: Create Entity
Click + Add Entity button
Enter entity name (use plural, lowercase: posts, users, comments)
Configure primary key format:
Integer (default): Auto-incrementing ID
UUID: Universally unique identifier
Click Create
Step 3: Add Fields

After entity creation, you're taken to the field editor:

Click + Add Field
Select field type (text, number, boolean, date, enum, json)
Configure field options:
Name: snake_case (e.g., first_name, created_at)
Required: Toggle if field cannot be null
Default Value: Optional default
Click Save Field
Repeat for additional fields
Step 4: Sync Schema

Click Sync Database to apply changes to the actual database.

Code Approach
Step 1: Import Dependencies
import { em, entity, text, number, boolean, date, enumm, json } from "bknd";

Step 2: Define Entity

Create your entity within em():

const schema = em({
  posts: entity("posts", {
    title: text().required(),
    content: text(),
    published: boolean({ default_value: false }),
    view_count: number({ default_value: 0 }),
  }),
});

Step 3: Configure Primary Key (Optional)

Default is auto-incrementing integer. For UUID:

const schema = em({
  posts: entity("posts", {
    title: text().required(),
  }, {
    primary_format: "uuid",
  }),
});

Step 4: Export Types

Enable type-safe queries:

const schema = em({
  posts: entity("posts", {
    title: text().required(),
    content: text(),
  }),
});

// Extract and declare types
type Database = (typeof schema)["DB"];
declare module "bknd" {
  interface DB extends Database {}
}

Step 5: Use in App Configuration
import { App } from "bknd";

const app = new App({
  data: schema,
  // ... other config
});

Full Example
import { App, em, entity, text, number, boolean, date } from "bknd";

const schema = em({
  users: entity("users", {
    email: text().required().unique(),
    name: text(),
    active: boolean({ default_value: true }),
  }),
  posts: entity("posts", {
    title: text().required(),
    content: text(),
    published: boolean({ default_value: false }),
    published_at: date(),
  }),
});

type Database = (typeof schema)["DB"];
declare module "bknd" {
  interface DB extends Database {}
}

const app = new App({
  data: schema,
});

export default app;

Entity Naming Conventions
Convention	Example	Notes
Plural	users, posts	NOT user, post
Lowercase	blog_posts	NOT BlogPosts
snake_case	user_profiles	NOT userProfiles
Auto-Generated Fields

Every entity automatically includes:

Field	Type	Description
id	integer/uuid	Primary key (format depends on config)

Note: For created_at/updated_at, use the timestamps plugin or add manually:

entity("posts", {
  title: text().required(),
  created_at: date({ default_value: "now" }),
  updated_at: date(),
})

Common Pitfalls
Entity Already Exists

Error: Entity "posts" already defined

Fix: Each entity name must be unique within em(). Check for duplicates.

Invalid Entity Name

Error: Invalid entity name

Fix: Use lowercase letters, numbers, and underscores only. Must start with letter.

// ✅ Valid
entity("posts", { ... })
entity("user_profiles", { ... })
entity("blog_posts_2024", { ... })

// ❌ Invalid
entity("Posts", { ... })        // No uppercase
entity("2024_posts", { ... })   // Can't start with number
entity("post-items", { ... })   // No hyphens

Schema Not Syncing

Problem: Created entity in code but table doesn't exist in database.

Fix: Ensure you're using the schema in your App config:

const app = new App({
  data: schema,  // Must pass schema here
});


Then restart the server - Bknd auto-syncs on startup.

Missing Type Safety

Problem: api.data.readMany("posts", ...) has no type hints.

Fix: Add type declaration:

type Database = (typeof schema)["DB"];
declare module "bknd" {
  interface DB extends Database {}
}

Verification
UI Mode
Check entity appears in Data section
Click entity to see fields
Try creating a test record
Code Mode
// After app starts, verify entity exists
const api = app.getApi();
const result = await api.data.readMany("posts");
console.log(result); // Should return { data: [] } for empty entity

CLI Check
npx bknd debug routes
# Should show /api/data/posts endpoints

DOs and DON'Ts

DO:

Use plural, lowercase entity names
Start with essential fields; add more later
Add type declarations for type safety
Use primary_format: "uuid" for distributed systems

DON'T:

Use singular names (user instead of users)
Use PascalCase or camelCase for entity names
Create entities without at least one field
Forget to sync database after UI changes
Related Skills
bknd-add-field - Add fields to existing entity
bknd-define-relationship - Connect entities with relationships
bknd-modify-schema - Rename or change entity configuration
bknd-delete-entity - Safely remove an entity
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