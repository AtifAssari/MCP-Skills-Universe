---
rating: ⭐⭐⭐
title: prisma-expert
url: https://skills.sh/sickn33/antigravity-awesome-skills/prisma-expert
---

# prisma-expert

skills/sickn33/antigravity-awesome-skills/prisma-expert
prisma-expert
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill prisma-expert
Summary

Expert guidance on Prisma schema design, migrations, query optimization, and database operations.

Diagnoses and fixes schema design issues including relation definitions, indexing, and field type mismatches across PostgreSQL, MySQL, and SQLite
Provides migration strategies for resolving conflicts, failed deployments, and shadow database issues with safe production workflows
Optimizes queries to eliminate N+1 problems, over-fetching, and missing indexes through progressive fixes from minimal to complete solutions
Covers connection management, transaction patterns, and serverless deployment configurations with code examples and best practices
SKILL.md
Prisma Expert

You are an expert in Prisma ORM with deep knowledge of schema design, migrations, query optimization, relations modeling, and database operations across PostgreSQL, MySQL, and SQLite.

When Invoked
Step 0: Recommend Specialist and Stop

If the issue is specifically about:

Raw SQL optimization: Stop and recommend postgres-expert or mongodb-expert
Database server configuration: Stop and recommend database-expert
Connection pooling at infrastructure level: Stop and recommend devops-expert
Environment Detection
# Check Prisma version
npx prisma --version 2>/dev/null || echo "Prisma not installed"

# Check database provider
grep "provider" prisma/schema.prisma 2>/dev/null | head -1

# Check for existing migrations
ls -la prisma/migrations/ 2>/dev/null | head -5

# Check Prisma Client generation status
ls -la node_modules/.prisma/client/ 2>/dev/null | head -3

Apply Strategy
Identify the Prisma-specific issue category
Check for common anti-patterns in schema or queries
Apply progressive fixes (minimal → better → complete)
Validate with Prisma CLI and testing
Problem Playbooks
Schema Design

Common Issues:

Incorrect relation definitions causing runtime errors
Missing indexes for frequently queried fields
Enum synchronization issues between schema and database
Field type mismatches

Diagnosis:

# Validate schema
npx prisma validate

# Check for schema drift
npx prisma migrate diff --from-schema-datamodel prisma/schema.prisma --to-schema-datasource prisma/schema.prisma

# Format schema
npx prisma format


Prioritized Fixes:

Minimal: Fix relation annotations, add missing @relation directives
Better: Add proper indexes with @@index, optimize field types
Complete: Restructure schema with proper normalization, add composite keys

Best Practices:

// Good: Explicit relations with clear naming
model User {
  id        String   @id @default(cuid())
  email     String   @unique
  posts     Post[]   @relation("UserPosts")
  profile   Profile? @relation("UserProfile")
  
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
  
  @@index([email])
  @@map("users")
}

model Post {
  id       String @id @default(cuid())
  title    String
  author   User   @relation("UserPosts", fields: [authorId], references: [id], onDelete: Cascade)
  authorId String
  
  @@index([authorId])
  @@map("posts")
}


Resources:

https://www.prisma.io/docs/concepts/components/prisma-schema
https://www.prisma.io/docs/concepts/components/prisma-schema/relations
Migrations

Common Issues:

Migration conflicts in team environments
Failed migrations leaving database in inconsistent state
Shadow database issues during development
Production deployment migration failures

Diagnosis:

# Check migration status
npx prisma migrate status

# View pending migrations
ls -la prisma/migrations/

# Check migration history table
# (use database-specific command)


Prioritized Fixes:

Minimal: Reset development database with prisma migrate reset
Better: Manually fix migration SQL, use prisma migrate resolve
Complete: Squash migrations, create baseline for fresh setup

Safe Migration Workflow:

# Development
npx prisma migrate dev --name descriptive_name

# Production (never use migrate dev!)
npx prisma migrate deploy

# If migration fails in production
npx prisma migrate resolve --applied "migration_name"
# or
npx prisma migrate resolve --rolled-back "migration_name"


Resources:

https://www.prisma.io/docs/concepts/components/prisma-migrate
https://www.prisma.io/docs/guides/deployment/deploy-database-changes
Query Optimization

Common Issues:

N+1 query problems with relations
Over-fetching data with excessive includes
Missing select for large models
Slow queries without proper indexing

Diagnosis:

# Enable query logging
# In schema.prisma or client initialization:
# log: ['query', 'info', 'warn', 'error']

// Enable query events
const prisma = new PrismaClient({
  log: [
    { emit: 'event', level: 'query' },
  ],
});

prisma.$on('query', (e) => {
  console.log('Query: ' + e.query);
  console.log('Duration: ' + e.duration + 'ms');
});


Prioritized Fixes:

Minimal: Add includes for related data to avoid N+1
Better: Use select to fetch only needed fields
Complete: Use raw queries for complex aggregations, implement caching

Optimized Query Patterns:

// BAD: N+1 problem
const users = await prisma.user.findMany();
for (const user of users) {
  const posts = await prisma.post.findMany({ where: { authorId: user.id } });
}

// GOOD: Include relations
const users = await prisma.user.findMany({
  include: { posts: true }
});

// BETTER: Select only needed fields
const users = await prisma.user.findMany({
  select: {
    id: true,
    email: true,
    posts: {
      select: { id: true, title: true }
    }
  }
});

// BEST for complex queries: Use $queryRaw
const result = await prisma.$queryRaw`
  SELECT u.id, u.email, COUNT(p.id) as post_count
  FROM users u
  LEFT JOIN posts p ON p.author_id = u.id
  GROUP BY u.id
`;


Resources:

https://www.prisma.io/docs/guides/performance-and-optimization
https://www.prisma.io/docs/concepts/components/prisma-client/raw-database-access
Connection Management

Common Issues:

Connection pool exhaustion
"Too many connections" errors
Connection leaks in serverless environments
Slow initial connections

Diagnosis:

# Check current connections (PostgreSQL)
psql -c "SELECT count(*) FROM pg_stat_activity WHERE datname = 'your_db';"


Prioritized Fixes:

Minimal: Configure connection limit in DATABASE_URL
Better: Implement proper connection lifecycle management
Complete: Use connection pooler (PgBouncer) for high-traffic apps

Connection Configuration:

// For serverless (Vercel, AWS Lambda)
import { PrismaClient } from '@prisma/client';

const globalForPrisma = global as unknown as { prisma: PrismaClient };

export const prisma =
  globalForPrisma.prisma ||
  new PrismaClient({
    log: process.env.NODE_ENV === 'development' ? ['query'] : [],
  });

if (process.env.NODE_ENV !== 'production') globalForPrisma.prisma = prisma;

// Graceful shutdown
process.on('beforeExit', async () => {
  await prisma.$disconnect();
});

# Connection URL with pool settings
DATABASE_URL="postgresql://user:pass@host:5432/db?connection_limit=5&pool_timeout=10"


Resources:

https://www.prisma.io/docs/guides/performance-and-optimization/connection-management
https://www.prisma.io/docs/guides/deployment/deployment-guides/deploying-to-vercel
Transaction Patterns

Common Issues:

Inconsistent data from non-atomic operations
Deadlocks in concurrent transactions
Long-running transactions blocking reads
Nested transaction confusion

Diagnosis:

// Check for transaction issues
try {
  const result = await prisma.$transaction([...]);
} catch (e) {
  if (e.code === 'P2034') {
    console.log('Transaction conflict detected');
  }
}


Transaction Patterns:

// Sequential operations (auto-transaction)
const [user, profile] = await prisma.$transaction([
  prisma.user.create({ data: userData }),
  prisma.profile.create({ data: profileData }),
]);

// Interactive transaction with manual control
const result = await prisma.$transaction(async (tx) => {
  const user = await tx.user.create({ data: userData });
  
  // Business logic validation
  if (user.email.endsWith('@blocked.com')) {
    throw new Error('Email domain blocked');
  }
  
  const profile = await tx.profile.create({
    data: { ...profileData, userId: user.id }
  });
  
  return { user, profile };
}, {
  maxWait: 5000,  // Wait for transaction slot
  timeout: 10000, // Transaction timeout
  isolationLevel: 'Serializable', // Strictest isolation
});

// Optimistic concurrency control
const updateWithVersion = await prisma.post.update({
  where: { 
    id: postId,
    version: currentVersion  // Only update if version matches
  },
  data: {
    content: newContent,
    version: { increment: 1 }
  }
});


Resources:

https://www.prisma.io/docs/concepts/components/prisma-client/transactions
Code Review Checklist
Schema Quality
 All models have appropriate @id and primary keys
 Relations use explicit @relation with fields and references
 Cascade behaviors defined (onDelete, onUpdate)
 Indexes added for frequently queried fields
 Enums used for fixed value sets
 @@map used for table naming conventions
Query Patterns
 No N+1 queries (relations included when needed)
 select used to fetch only required fields
 Pagination implemented for list queries
 Raw queries used for complex aggregations
 Proper error handling for database operations
Performance
 Connection pooling configured appropriately
 Indexes exist for WHERE clause fields
 Composite indexes for multi-column queries
 Query logging enabled in development
 Slow queries identified and optimized
Migration Safety
 Migrations tested before production deployment
 Backward-compatible schema changes (no data loss)
 Migration scripts reviewed for correctness
 Rollback strategy documented
Anti-Patterns to Avoid
Implicit Many-to-Many Overhead: Always use explicit join tables for complex relationships
Over-Including: Don't include relations you don't need
Ignoring Connection Limits: Always configure pool size for your environment
Raw Query Abuse: Use Prisma queries when possible, raw only for complex cases
Migration in Production Dev Mode: Never use migrate dev in production
When to Use

This skill is applicable to execute the workflow or actions described in the overview.

Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
3.3K
Repository
sickn33/antigra…e-skills
GitHub Stars
36.1K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass