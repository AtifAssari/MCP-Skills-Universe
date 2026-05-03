---
title: service-pattern-nestjs
url: https://skills.sh/allenlin90/eridu-services/service-pattern-nestjs
---

# service-pattern-nestjs

skills/allenlin90/eridu-services/service-pattern-nestjs
service-pattern-nestjs
Installation
$ npx skills add https://github.com/allenlin90/eridu-services --skill service-pattern-nestjs
SKILL.md
Service Pattern - NestJS

Complete implementation guide for NestJS Services in Eridu.

Canonical Examples

Study these real implementations as the source of truth:

Model Service: task-template.service.ts
Schema File: task-template.schema.ts
Base Service: base-model.service.ts

Detailed code examples: See references/service-examples.md

Core Responsibilities

Services act as the business logic layer. They should:

Implement business logic - Handle domain rules and operations
Coordinate data access - Call repositories to fetch/persist data
Validate input - Check data before persistence
Handle errors - Transform low-level errors to domain errors
Coordinate operations - Orchestrate multi-entity workflows
Manage transactions - Ensure data consistency
Domain Transition Rule

If an operation is a business-state transition (not a generic field update), model it as an explicit service action with clear invariants.

Examples of required invariants:

allowed current state(s),
blocking conditions (for example active tasks),
required audit context (reason, actor, timestamp),
idempotent behavior under retries/concurrency.

Controller PATCH handlers should call this explicit service action rather than bypassing invariants through generic update payloads.

Service Architecture

Layered Pattern:

Controller (HTTP boundary)
    ↓
Service (Business logic)
    ├─ Model Services (single entity)
    └─ Orchestration Services (multiple entities)
    ↓
Repository (Data access)
    ↓
Database

Model Services

Handle CRUD operations for a single entity. Focused on single entity, simple CRUD operations, dependency on one or more repositories.

Orchestration Services

Coordinate multiple entities for complex workflows. Handle complex business workflows, use transactions for atomicity.

Model Service Structure

🔴 Critical: Extend BaseModelService<T> for standard CRUD.

import { Injectable } from '@nestjs/common';
import { BaseModelService } from '@/lib/services/base-model.service';
import { UtilityService } from '@/utility/utility.service';

@Injectable()
export class UserService extends BaseModelService {
  // UID_PREFIX has NO trailing underscore (e.g., 'user', not 'user_')
  static readonly UID_PREFIX = 'user';
  protected readonly uidPrefix = UserService.UID_PREFIX;

  constructor(
    private readonly userRepository: UserRepository,
    protected readonly utilityService: UtilityService,
  ) {
    super(utilityService);
  }
}

When Does a Model Service Justify Existing?

A model service exists to:

Generate UIDs (this.generateUid()) — even thin services serve this purpose
Enforce invariants before/after persistence
Translate domain payloads into repository calls
Be the stable public API of the module

A service with only pass-through methods is acceptable when:

It provides a consistent pattern with sibling modules
It generates UIDs (join table services)
Its methods may gain logic in the future

A service that does NOT generate UIDs and has zero logic should be questioned — consider whether the orchestration should just call the parent module's service.

Avoiding ORM Coupling in Services

🔴 Critical: Services MUST NEVER import or use Prisma types in method signatures or business logic.

Why: We use the repository pattern to encapsulate all database concerns. Services should be completely decoupled from the ORM to allow changing the database layer without touching business logic.

Rule 1: Define Payload Types in Schema Files

Schema files MAY use Prisma.* types to define payload types:

// ✅ ALLOWED: In schema file
import type { Prisma } from '@prisma/client';

export type CreateTaskTemplatePayload = Omit<
  Prisma.TaskTemplateCreateInput,
  'uid' | 'version'
> & {
  uid?: string;
  currentSchema: any;
};

Rule 2: Services Import Payload Types, NOT Prisma Types
// ✅ GOOD: Service imports payload type from schema
import type { CreateTaskTemplatePayload } from './schemas/task-template.schema';

async createTemplateWithSnapshot(
  payload: CreateTaskTemplatePayload,
): Promise<TaskTemplate> {
  return this.repository.create({
    ...payload,
    uid: this.generateUid(),
  });
}

// ❌ BAD: Service imports Prisma types
import { Prisma } from '@prisma/client';

async create(payload: Prisma.TaskTemplateCreateInput): Promise<TaskTemplate> {
  // ...
}

Rule 3: Use Parameters<Repo['method']> for Pass-Through

For methods that simply pass arguments to the repository, use Parameters<> to match the repository signature:

// ✅ GOOD: Service signature matches repository
async getTaskTemplates(
  ...args: Parameters<TaskTemplateRepository['findPaginated']>
): Promise<{ data: TaskTemplate[]; total: number }> {
  return this.repository.findPaginated(...args);
}

async findOne(
  ...args: Parameters<TaskTemplateRepository['findOne']>
): Promise<TaskTemplate | null> {
  return this.repository.findOne(...args);
}


Benefits:

Service has zero Prisma imports
Service signature automatically matches repository
Changing ORM only requires updating repository
Service tests don't need to mock Prisma types

Tradeoff awareness: Parameters<Repository['method']> couples the service method signature to the repository signature. Changing the repository method signature changes the service's public API.

Use this pattern when:

The method is a genuine pass-through with no business logic
The service needs to expose a repository query for orchestration callers

Mark these as @internal if they are not intended for controllers:

/** @internal For orchestration use only. Controllers use findByUid(). */
async findOne(...args: Parameters<TaskRepository['findOne']>)

Rule 5: Never Call Zod .parse() Inside a Service

🔴 Critical: Services MUST NOT call Zod .parse() on their input payloads.

Why: The controller/DTO layer (via nestjs-zod and ZodValidationPipe) is the HTTP boundary. By the time a method reaches the service, the payload has already been validated and is fully typed. Parsing again is a double-parse, it moves validation responsibility into the wrong layer, and it breaks the single-responsibility principle.

// ❌ BAD: Service re-validates a payload that was already validated by the DTO
import { createUserSchema } from '@eridu/api-types/users';

async run(payload: unknown): Promise<Result> {
  const validated = createUserSchema.parse(payload); // ← WRONG
  ...
}

// ✅ GOOD: Service accepts the already-typed payload
import type { CreateUserRequest } from '@eridu/api-types/users';

async run(payload: CreateUserRequest): Promise<Result> {
  // payload is already validated — use it directly
  ...
}


The matching controller uses a Zod DTO to handle validation before the service is called:

// Controller DTO (nestjs-zod validates on ingress):
export class CreateUserDto extends createZodDto(createUserRequestSchema) {}

// Controller method — payload is validated before service.run() is called:
@Post()
async create(@Body() payload: CreateUserDto) {
  return this.userService.run(payload); // typed, already valid
}


Anti-pattern signature:

// Any service method with `payload: unknown` that calls `.parse()` is wrong.
async doSomething(payload: unknown): Promise<X> {
  const data = someSchema.parse(payload); // ← move this to a DTO


This rule also applies to DTO composition. When building a derived DTO schema (e.g., a detail DTO that extends a base DTO), do NOT call .parse() of the base DTO inside the derived transform. Instead, inline the transform logic so the object is only parsed once through a single .pipe() chain.

// ❌ BAD: nested .parse() inside transform causes double validation
export const detailDto = baseSchema.extend({ extra: z.string() })
  .transform((obj) => ({
    ...baseDto.parse(obj),   // ← re-runs full base validation
    extra: obj.extra,
  }))
  .pipe(detailApiSchema);

// ✅ GOOD: inline the transform, single parse pass
export const detailDto = baseSchema.extend({ extra: z.string() })
  .transform((obj) => ({
    id: obj.uid,
    name: obj.name,
    // ... inline base fields directly
    extra: obj.extra,
  }))
  .pipe(detailApiSchema);

Rule 4: Repository Owns Where-Clause Building

The repository layer is responsible for building ORM-specific where clauses. Services pass domain-level parameters:

// ✅ GOOD: Repository accepts domain parameters
// Repository method signature:
async findPaginated(params: {
  skip?: number;
  take?: number;
  name?: string;
  uid?: string;
  includeDeleted?: boolean;
  studioUid?: string;
  orderBy?: 'asc' | 'desc';
}): Promise<{ data: TaskTemplate[]; total: number }>


The repository then builds the Prisma where clause internally:

// Inside repository:
const where: Prisma.TaskTemplateWhereInput = {};

if (!includeDeleted) {
  where.deletedAt = null;
}

if (name) {
  where.name = { contains: name, mode: 'insensitive' };
}

if (studioUid) {
  where.studio = { uid: studioUid };
}

CRUD Operations
Create with ID Generation
async createUser(data: CreateUserDto): Promise<User> {
  return this.userRepository.create({
    uid: this.generateUid(), // Helper from BaseModelService
    email: data.email,
    name: data.name,
  });
}

Read with Verification
async getUserById(uid: string): Promise<User> {
  const user = await this.userRepository.findByUid(uid);
  if (!user) throw HttpError.notFound('User', uid);
  return user;
}

Error Handling by Service Type

Differentiate your error handling strategy based on the service type:

1. Model Services (Single Entity)

Pattern: Return null, let Controller handle 404.

// Service
async getUserById(uid: string): Promise<User | null> {
  return this.userRepository.findByUid(uid);
}

// Controller
@Get(':id')
async getUser(@Param('id') id: string) {
  const user = await this.userService.getUserById(id);
  this.ensureResourceExists(user, 'User', id); // Throws 404
  return user;
}

2. Orchestration Services (Complex Workflows)

Pattern: Throw Domain Exceptions or business logic errors directly.

Orchestration services often enforce rules that the controller cannot know about (e.g., "User must be a member of this Studio to be assigned").

// Service
async assignUserToStudio(userUid: string, studioUid: string) {
  const isMember = await this.membershipService.isMember(userUid, studioUid);
  
  if (!isMember) {
    // ✅ ACCEPTABLE: detailed business error
    throw HttpError.forbidden('User is not a member of this studio');
  }
}


[!TIP] Preferred: Throw custom Domain Exceptions (e.g., InvalidAssigneeError) and use a global Exception Filter to map them to HTTP responses. Acceptable: Use HttpError utility for immediate feedback in non-critical paths. Avoid: Throwing generic NotFoundException for simple lookups — stick to null + ensureResourceExists.

3. Update/Delete Operations

Controller verifies existence BEFORE calling the mutation service (Controller-Checks Pattern).

// Controller
@Patch(':id')
async updateUser(@Param('id') id: string, @Body() dto: UpdateUserDto) {
  // 1. Verify existence
  const user = await this.userService.getUserById(id);
  this.ensureResourceExists(user, 'User', id);
  
  // 2. Perform operation
  return this.userService.updateUser(id, dto);
}

@Delete(':id')
async deleteUser(@Param('id') id: string) {
  // 1. Verify existence
  const user = await this.userService.getUserById(id);
  this.ensureResourceExists(user, 'User', id);
  
  // 2. Perform operation
  await this.userService.deleteUser(id);
}

Bulk Operations

🟡 Recommended: Use Repository bulk methods, DO NOT loop in Service.

async createManyUsers(users: CreateUserDto[]) {
  // Map DTOs to internal structure (e.g. add UIDs)
  const data = users.map(u => ({
    ...u,
    uid: this.generateUid()
  }));
  
  // Single DB Call
  return this.userRepository.createMany(data);
}

Optimistic Locking Pattern

🟡 Recommended: For versioned entities, use version checks to prevent concurrent update conflicts.

async updateTemplateWithSnapshot(
  where: Parameters<TaskTemplateRepository['updateWithVersionCheck']>[0],
  payload: Parameters<TaskTemplateRepository['updateWithVersionCheck']>[1],
): Promise<TaskTemplate> {
  if (payload.currentSchema && !this.validateSchema(payload.currentSchema)) {
    throw HttpError.badRequest('Invalid schema');
  }

  try {
    if (payload.currentSchema) {
      const newVersion = (payload.version as number) + 1;
      return await this.repository.updateWithVersionCheck(where, {
        name: payload.name,
        description: payload.description,
        currentSchema: payload.currentSchema,
        version: newVersion,
        snapshots: {
          create: {
            version: newVersion,
            schema: payload.currentSchema,
          },
        },
      });
    }

    return await this.repository.update(where, {
      name: payload.name,
      description: payload.description,
    });
  } catch (error) {
    if (error instanceof VersionConflictError) {
      throw HttpError.conflict(
        `Record is out of date. Please refresh your record and try again.`,
      );
    }
    throw error;
  }
}

Including Relations

Question: Should services expose include parameters?

Short Answer: Avoid it when possible, but it's acceptable for internal orchestration APIs.

Recommended Pattern: Dedicated Methods
// ✅ GOOD: Dedicated methods for different data shapes
async getTaskById(uid: string): Promise<Task>
async getTaskWithAssignee(uid: string): Promise<Task & { assignee: User }>
async getTaskWithTemplate(uid: string): Promise<Task & { template: TaskTemplate }>

Acceptable Pattern: Internal Orchestration API
// ✅ ACCEPTABLE: For orchestration services that need flexibility
/**
 * @internal
 * Internal method for orchestration services.
 * Controllers should use dedicated methods like getTaskWithAssignee().
 */
async findOne(
  ...args: Parameters<TaskRepository['findOne']>
): Promise<Task | null> {
  return this.taskRepository.findOne(...args);
}


When to use each:

Dedicated methods: For controller-facing APIs (preferred)
Parameters spread: For internal flexibility (acceptable, mark as @internal)
Orchestration Services

🔴 Critical: Coordinate multiple services/repositories using Transactions.

See Database Patterns for transaction rules.

import { Transactional } from '@nestjs-cls/transactional';

@Injectable()
export class ShowOrchestrationService {
  constructor(
    private readonly showService: ShowService,
    private readonly assignmentService: AssignmentService,
  ) {}

  // Apply @Transactional() on the orchestration method — never pass `tx` as a parameter.
  // CLS propagates the transaction automatically to all repository calls.
  @Transactional()
  async createShowWithAssignments(data: CreateShowDto) {
    const show = await this.showService.createShow(data);
    await this.assignmentService.createAssignments(show.id, data.assignments);
    return show;
  }
}


[!WARNING] Never use the old $transaction(async (tx) => { ... }) pattern with tx parameter passing. This is the legacy pattern. All new orchestration must use @Transactional(). Repositories access the active CLS transaction client via TransactionHost injected by the adapter.

Best Practices Checklist
 Extend BaseModelService
 Define UID_PREFIX static constant (no trailing underscore)
 Inject UtilityService
 Use this.generateUid()
 🔴 Critical: Define Payload types in schema files (not in service)
 🔴 Critical: NEVER call Zod .parse() inside a service — accept typed payloads, let the DTO layer validate
 🔴 Critical: NEVER import or use Prisma.* types in service method signatures
 🔴 Critical: Use Parameters<Repository['methodName']> for pass-through methods
 🔴 Critical: Delegate filter building to repository layer (not service)
 🔴 Critical: Return null (don't throw) if record missing in Read operations
 🔴 Critical: Let Controller handle 404 checks (using ensureResourceExists)
 🔴 Critical: Never throw NotFoundException in Service (business logic only)
 Catch VersionConflictError and rethrow as HttpError.conflict()
 🟡 Recommended: Prefer dedicated methods over exposing include parameters
 Mark methods with @internal JSDoc if they're for orchestration only
Related Skills
Repository Pattern NestJS - Data access patterns
Backend Controller Pattern NestJS - Controller patterns
Database Patterns - Transactions, soft delete, locking
Data Validation - Input validation patterns
Weekly Installs
8
Repository
allenlin90/erid…services
GitHub Stars
1
First Seen
Mar 14, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass