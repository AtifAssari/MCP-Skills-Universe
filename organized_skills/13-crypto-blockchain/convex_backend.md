---
rating: ⭐⭐
title: convex-backend
url: https://skills.sh/cloudai-x/claude-workflow-v2/convex-backend
---

# convex-backend

skills/cloudai-x/claude-workflow-v2/convex-backend
convex-backend
Installation
$ npx skills add https://github.com/cloudai-x/claude-workflow-v2 --skill convex-backend
SKILL.md
Convex Backend Guidelines
When to Load
Trigger: Convex-specific development, writing Convex functions, schemas, queries, mutations, actions, or real-time subscriptions
Skip: Project does not use Convex as its backend

Comprehensive guide for building Convex backends with TypeScript. Covers function syntax, validators, schemas, queries, mutations, actions, scheduling, and file storage.

When to Apply

Reference these guidelines when:

Writing new Convex functions (queries, mutations, actions)
Defining database schemas and validators
Implementing real-time data fetching
Setting up cron jobs or scheduled functions
Working with file storage
Designing API structure
Rule Categories
Category	Impact	Description
Function Syntax	CRITICAL	New function syntax with args/returns/handler
Validators	CRITICAL	Type-safe argument and return validation
Schema Design	HIGH	Table definitions, indexes, system fields
Query Patterns	HIGH	Efficient data fetching with indexes
Mutation Patterns	MEDIUM	Database writes, patch vs replace
Action Patterns	MEDIUM	External API calls, Node.js runtime
Scheduling	MEDIUM	Crons and delayed function execution
File Storage	LOW	Blob storage and metadata
Quick Reference
Function Registration
// Public functions (exposed to clients)
import { query, mutation, action } from "./_generated/server";

// Internal functions (only callable from other Convex functions)
import {
  internalQuery,
  internalMutation,
  internalAction,
} from "./_generated/server";

Function Syntax (Always Use This)
export const myFunction = query({
  args: { name: v.string() },
  returns: v.string(),
  handler: async (ctx, args) => {
    return "Hello " + args.name;
  },
});

Common Validators
Type	Validator	Example
String	v.string()	"hello"
Number	v.number()	3.14
Boolean	v.boolean()	true
ID	v.id("tableName")	doc._id
Array	v.array(v.string())	["a", "b"]
Object	v.object({...})	{name: "x"}
Optional	v.optional(v.string())	undefined
Union	v.union(v.string(), v.number())	"x" or 1
Literal	v.literal("status")	"status"
Null	v.null()	null
Function References
// Public functions
import { api } from "./_generated/api";
api.example.myQuery; // convex/example.ts → myQuery

// Internal functions
import { internal } from "./_generated/api";
internal.example.myInternalMutation;

Query with Index
// Schema
messages: defineTable({...}).index("by_channel", ["channelId"])

// Query
await ctx.db
  .query("messages")
  .withIndex("by_channel", (q) => q.eq("channelId", channelId))
  .order("desc")
  .take(10);

Key Rules
Always include args and returns validators on all functions
Use v.null() for void returns - never omit return validator
Use withIndex() not filter() - define indexes in schema
Use internalQuery/Mutation/Action for private functions
Actions cannot access ctx.db - use runQuery/runMutation instead
Include type annotations when calling functions in same file
Full Compiled Document

For the complete guide with all rules and detailed code examples, see: AGENTS.md

Weekly Installs
124
Repository
cloudai-x/claud…kflow-v2
GitHub Stars
1.4K
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass