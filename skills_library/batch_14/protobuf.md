---
title: protobuf
url: https://skills.sh/bufbuild/claude-plugins/protobuf
---

# protobuf

skills/bufbuild/claude-plugins/protobuf
protobuf
Installation
$ npx skills add https://github.com/bufbuild/claude-plugins --skill protobuf
SKILL.md
Protocol Buffers
When You Need This Skill
Creating or editing .proto files
Setting up buf.yaml or buf.gen.yaml
Designing gRPC or Connect services
Adding protovalidate constraints
Troubleshooting buf lint or breaking change errors
Core Workflow
1. Match Project Style

Before writing proto code, review existing .proto files in the project. Match conventions for naming, field ordering, structural patterns, validation, and documentation style. If none exists, ask the user what style should be used or an existing library to emulate.

2. Write Proto Code
Apply universal best practices from best_practices.md
Add protovalidate constraints to every field—this is not optional for production APIs
For service templates, see assets/
3. Verify Changes

Always run after making changes:

buf format -w && buf lint


Check for a Makefile first—many projects use make lint or make format.

Fix all errors before considering the change complete.

Quick Reference
Task	Reference
Field types, enums, oneofs, maps	quick_reference.md
Schema evolution, breaking changes	best_practices.md
Validation constraints	protovalidate.md
Complete service examples	examples.md, assets/
buf CLI, buf.yaml, buf.gen.yaml	buf_toolchain.md
Migrating from protoc	migration.md
Lint errors, common issues	troubleshooting.md
Proto API review checklist	review_checklist.md
Project Setup
New Project

Create directory structure:

proto/
├── buf.yaml
├── buf.gen.yaml
└── company/
    └── domain/
        └── v1/
            └── service.proto


Use assets/buf.yaml as starting point

Add buf.build/bufbuild/protovalidate as a dependency in buf.yaml and run buf dep update

Use assets/buf.gen.*.yaml for code generation config

Code Generation Templates
Template	Use For
buf.gen.go.yaml	Go with gRPC
buf.gen.go-connect.yaml	Go with Connect
buf.gen.ts.yaml	TypeScript with Connect
buf.gen.python.yaml	Python with gRPC
buf.gen.java.yaml	Java with gRPC
Proto File Templates

Located in assets/proto/example/v1/:

Template	Description
book.proto	Entity message, BookRef oneof, enum
book_service.proto	Full CRUD with batch ops, pagination, ordering
Common Tasks
Add a new field
Use next sequential field number
Add protovalidate constraints: every field should have validation appropriate to its type (format validators, length bounds, numeric ranges, enum constraints, etc.)
Document the field
Run buf format -w && buf lint
Remove a field
Reserve the field number AND name:
reserved 4;
reserved "old_field_name";

Run buf breaking --against '.git#branch=main' to verify
Add protovalidate constraints

Every field in a production API should have appropriate validation. See protovalidate.md for the full reference.

Common constraints:

String formats: .string.uuid, .string.email, .string.uri, .string.pattern
String bounds: .string.min_len, .string.max_len
Numeric bounds: .int32.gte, .uint32.lte
Enum validation: .enum.defined_only, .enum.not_in = 0
Repeated bounds: .repeated.min_items, .repeated.max_items
Required fields: (buf.validate.field).required = true
Oneof required: (buf.validate.oneof).required = true
Verification Checklist

After making changes:

 Every field has appropriate protovalidate constraints
 buf format -w (apply formatting)
 buf lint (check style rules)
 buf breaking --against '.git#branch=main' (if modifying existing schemas)
Weekly Installs
133
Repository
bufbuild/claude-plugins
GitHub Stars
17
First Seen
Jan 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass