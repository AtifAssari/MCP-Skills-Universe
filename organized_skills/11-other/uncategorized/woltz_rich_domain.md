---
rating: ⭐⭐
title: woltz-rich-domain
url: https://skills.sh/tarcisioandrade/rich-domain/woltz-rich-domain
---

# woltz-rich-domain

skills/tarcisioandrade/rich-domain/woltz-rich-domain
woltz-rich-domain
Installation
$ npx skills add https://github.com/tarcisioandrade/rich-domain --skill woltz-rich-domain
SKILL.md
@woltz/rich-domain

TypeScript library for Domain-Driven Design with automatic change tracking and Standard Schema validation.

Requirements
Node.js >= 22.12
TypeScript >= 5.4
Ecosystem
Package	Purpose
@woltz/rich-domain	Core DDD building blocks
@woltz/rich-domain-prisma	Prisma ORM adapter
@woltz/rich-domain-typeorm	TypeORM adapter
@woltz/rich-domain-criteria-zod	Zod schemas for Criteria API
@woltz/rich-domain-export	Multi-format data export
Quick Start
1. Define a Value Object
import { ValueObject } from "@woltz/rich-domain";
import { z } from "zod";

class Email extends ValueObject<string> {
  protected static validation = {
    schema: z.string().email(),
  };

  getDomain(): string {
    return this.value.split("@")[1];
  }
}

2. Define an Entity
import { Entity, Id, type EntityValidation } from "@woltz/rich-domain";

const PostSchema = z.object({
  id: z.custom<Id>(),
  title: z.string().min(1),
  content: z.string(),
  published: z.boolean(),
});
export type PostProps = z.infer<typeof PostSchema>;

class Post extends Entity<PostProps> {
  protected static validation: EntityValidation<PostProps> = {
    schema: PostSchema,
  };

  publish(): void {
    this.props.published = true;
  }

  get title() {
    return this.props.title;
  }
}

3. Define an Aggregate
import {
  Aggregate,
  Id,
  type EntityValidation,
  type EntityHooks,
} from "@woltz/rich-domain";
import { UserCreatedEvent } from "./events";
import { Email } from "./email";

const UserSchema = z.object({
  id: z.custom<Id>(),
  email: z.custom<Email>(),
  name: z.string().min(2),
  posts: z.array(z.instanceof(Post)),
  createdAt: z.date(),
});
export type UserProps = z.infer<typeof UserSchema>;

class User extends Aggregate<UserProps, "createdAt"> {
  protected static validation: EntityValidation<UserProps> = {
    schema: UserSchema,
  };
  protected static hooks: EntityHooks<UserProps, User> = {
    onBeforeCreate: (props) => {
      if (!props.createdAt) props.createdAt = new Date();
    },
    onCreate: (entity) => {
      if (entity.isNew()) {
        entity.addDomainEvent(new UserCreatedEvent({ id: entity.id.value }));
      }
    },
  };

  getTypedChanges() {
    interface Entities {
      Post: Post;
    }
    return this.getChanges<Entities>();
  }

  addPost(title: string, content: string): void {
    this.props.posts.push(new Post({ title, content, published: false }));
  }

  get email() {
    return this.props.email.value;
  }
  get posts() {
    return this.props.posts;
  }
}

4. Use Change Tracking
const user = await userRepository.findById(userId);

// Make changes
user.addPost("New Post", "Content");
user.posts[0].publish();

// Get changes automatically
// We strongly recommend using this `getTypedChanges` helper pattern for better DX
const changes = user.getTypedChanges();
// { creates: [...], updates: [...], deletes: [...] }

// After saving
user.markAsClean();

5. Query with Criteria
import { Criteria } from "@woltz/rich-domain";

// fully type-safe, fields inferred from schema
const criteria = Criteria.create<User>()
  .where("status", "equals", "active")
  .whereContains("email", "@company.com")
  .orderBy("createdAt", "desc")
  .paginate(1, 20);

const result = await userRepository.find(criteria);

Core Principles
Aggregates define consistency boundaries - Modify entities through their aggregate root
Value Objects are immutable - Use clone() to create modified copies
Id tracks new vs existing - new Id() for INSERT, Id.from(value) for UPDATE
Change tracking is automatic - Use getChanges() and markAsClean()
Repositories abstract persistence - Domain layer doesn't know about database
References

For detailed documentation on specific topics:

Core Concepts - Entities, Aggregates, Value Objects, Lifecycle Hooks
Domain Events - Event-driven architecture with example using BullMQ
Criteria API - Type-safe query building with filters, ordering, pagination
Criteria Zod - Zod schemas for API query validation
Schema Registry - EntitySchemaRegistry for field mapping and relationships
Prisma Adapter - PrismaRepository, UnitOfWork, Transactions
TypeORM Adapter - TypeORMRepository, change tracking
Export - CSV, JSON export with streaming support

DO NOT read all files at once. Load based on context.

Resources
Documentation
Weekly Installs
13
Repository
tarcisioandrade…h-domain
GitHub Stars
3
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass