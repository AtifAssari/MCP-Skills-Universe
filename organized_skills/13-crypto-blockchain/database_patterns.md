---
rating: ⭐⭐⭐
title: database-patterns
url: https://skills.sh/phrazzld/claude-config/database-patterns
---

# database-patterns

skills/phrazzld/claude-config/database-patterns
database-patterns
Installation
$ npx skills add https://github.com/phrazzld/claude-config --skill database-patterns
SKILL.md
Database Patterns

Forward-only migrations, explicit transactions, measured optimization.

Migrations

Forward-only. No rollbacks. Maintain backward compatibility:

-- Add nullable column (backward compatible)
ALTER TABLE users ADD COLUMN phone VARCHAR(20);

-- Later: make required after backfill
ALTER TABLE users ALTER COLUMN phone SET NOT NULL;


Break large changes into smaller steps. Use feature flags during transitions.

Query Optimization

Always check execution plans before optimizing:

EXPLAIN ANALYZE SELECT * FROM orders WHERE user_id = 123;


Index based on actual query patterns:

-- Composite for common query
CREATE INDEX idx_orders_user_date ON orders (user_id, created_at DESC);

-- Partial for filtered queries
CREATE INDEX idx_orders_pending ON orders (status) WHERE status = 'pending';


Monitor unused indexes. Remove if idx_scan < 100.

N+1 Prevention

Always eager load in loops:

# Good
users = User.query.options(joinedload(User.posts)).all()

# Bad (N+1)
users = User.query.all()
for user in users:
    print(user.posts)  # N queries!

Transactions

Scope to single business operation. Keep short:

async with db.transaction():
    order = await create_order(data)
    await update_inventory(order.items)
    # Commit on exit

# OUTSIDE transaction: send emails, call external APIs
await send_confirmation(order)


Never hold transactions during external calls.

Connection Pooling
# Size based on measured peak concurrency
create_engine(
    url,
    pool_size=15,      # Based on load testing
    max_overflow=5,    # Burst capacity
    pool_timeout=30,   # Fail fast
    pool_recycle=3600, # Prevent stale connections
    pool_pre_ping=True # Validate before use
)


Monitor utilization. Alert at 80%.

Data Validation

Validate at boundaries, not just in database:

# Validate input before INSERT
validated = CreateUserSchema.parse(input)
if await email_exists(validated.email):
    raise ValidationError("Email taken")

# Validate output after retrieval (detect corruption)
return UserOutputSchema.parse(row)

Anti-Patterns
Rollback migrations (use forward-only)
Indexes without query pattern analysis
N+1 queries in loops
Long-running transactions with external calls
Relying only on DB constraints for validation
Default pool settings without measurement
References
audit-logging.md - Immutable audit trails
Weekly Installs
23
Repository
phrazzld/claude-config
GitHub Stars
8
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass