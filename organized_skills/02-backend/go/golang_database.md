---
rating: ⭐⭐
title: golang-database
url: https://skills.sh/samber/cc-skills-golang/golang-database
---

# golang-database

skills/samber/cc-skills-golang/golang-database
golang-database
Installation
$ npx skills add https://github.com/samber/cc-skills-golang --skill golang-database
SKILL.md

Persona: You are a Go backend engineer who writes safe, explicit, and observable database code. You treat SQL as a first-class language — no ORMs, no magic — and you catch data integrity issues at the boundary, not deep in the application.

Modes:

Write mode — generating new repository functions, query helpers, or transaction wrappers: follow the skill's sequential instructions; launch a background agent to grep for existing query patterns and naming conventions in the codebase before generating new code.
Review/debug mode — auditing or debugging existing database code: use a sub-agent to scan for missing rows.Close(), un-parameterized queries, missing context propagation, and absent error checks in parallel with reading the business logic.

Community default. A company skill that explicitly supersedes samber/cc-skills-golang@golang-database skill takes precedence.

Go Database Best Practices

Go's database/sql provides a solid foundation for database access. Use sqlx or pgx on top of it for ergonomics — never an ORM.

When using sqlx or pgx, refer to the library's official documentation and code examples for current API signatures.

Best Practices Summary
Use sqlx or pgx, not ORMs — ORMs hide SQL, generate unpredictable queries, and make debugging harder
Queries MUST use parameterized placeholders — NEVER concatenate user input into SQL strings
Context MUST be passed to all database operations — use *Context method variants (QueryContext, ExecContext, GetContext)
sql.ErrNoRows MUST be handled explicitly — distinguish "not found" from real errors using errors.Is
Rows MUST be closed after iteration — defer rows.Close() immediately after QueryContext calls
NEVER use db.Query for statements that don't return rows — Query returns *Rows which must be closed; if you forget, the connection leaks back to the pool. Use db.Exec instead
Use transactions for multi-statement operations — wrap related writes in BeginTxx/Commit
Use SELECT ... FOR UPDATE when reading data you intend to modify — prevents race conditions
Set custom isolation levels when default READ COMMITTED is insufficient (e.g., serializable for financial operations)
Handle NULLable columns with pointer fields (*string, *int) or sql.NullXxx types
Connection pool MUST be configured — SetMaxOpenConns, SetMaxIdleConns, SetConnMaxLifetime, SetConnMaxIdleTime
Use external tools for migrations — golang-migrate or Flyway, never hand-rolled or AI-generated migration SQL
Batch operations in reasonable sizes — not row-by-row (too many round trips), not millions at once (locks and memory)
Never create or modify database schemas — a schema that looks correct on toy data can create hotspots, lock contention, or missing indexes under real production load. Schema design requires understanding of data volumes, access patterns, and production constraints that AI does not have
Avoid hidden SQL features — do not rely on triggers, views, materialized views, stored procedures, or row-level security in application code
Library Choice
Library	Best for	Struct scanning	PostgreSQL-specific
database/sql	Portability, minimal deps	Manual Scan	No
sqlx	Multi-database projects	StructScan	No
pgx	PostgreSQL (30-50% faster)	pgx.RowToStructByName	Yes (COPY, LISTEN, arrays)
GORM/ent	Avoid	Magic	Abstracted away

Why NOT ORMs:

Unpredictable query generation — N+1 problems you cannot see in code
Magic hooks and callbacks (BeforeCreate, AfterUpdate) make debugging harder
Schema migrations coupled to application code
Learning the ORM API is harder than learning SQL, and the abstraction leaks
Parameterized Queries
// ✗ VERY BAD — SQL injection vulnerability
query := fmt.Sprintf("SELECT * FROM users WHERE email = '%s'", email)

// ✓ Good — parameterized (PostgreSQL)
var user User
err := db.GetContext(ctx, &user, "SELECT id, name, email FROM users WHERE email = $1", email)

// ✓ Good — parameterized (MySQL)
err := db.GetContext(ctx, &user, "SELECT id, name, email FROM users WHERE email = ?", email)

Dynamic IN clauses
query, args, err := sqlx.In("SELECT * FROM users WHERE id IN (?)", ids)
if err != nil {
    return fmt.Errorf("building IN clause: %w", err)
}
query = db.Rebind(query) // adjust placeholders for your driver
err = db.SelectContext(ctx, &users, query, args...)

Dynamic column names

Never interpolate column names from user input. Use an allowlist:

allowed := map[string]bool{"name": true, "email": true, "created_at": true}
if !allowed[sortCol] {
    return fmt.Errorf("invalid sort column: %s", sortCol)
}
query := fmt.Sprintf("SELECT id, name, email FROM users ORDER BY %s", sortCol)


For more injection prevention patterns, see the samber/cc-skills-golang@golang-security skill.

Struct Scanning and NULLable Columns

Use db:"column_name" tags for sqlx, pgx.CollectRows with pgx.RowToStructByName for pgx. Handle NULLable columns with pointer fields (*string, *time.Time) — they work cleanly with both scanning and JSON marshaling. See Scanning Reference for examples of all approaches.

Error Handling
func GetUser(id string) (*User, error) {
    var user User

    err := db.GetContext(ctx, &user, "SELECT id, name FROM users WHERE id = $1", id)
    if err != nil {
        if errors.Is(err, sql.ErrNoRows) {
            return nil, ErrUserNotFound // translate to domain error
        }
        return nil, fmt.Errorf("querying user %s: %w", id, err)
    }

    return &user, nil
}


or:

func GetUser(id string) (u *User, exists bool, err error) {
    var user User

    err := db.GetContext(ctx, &user, "SELECT id, name FROM users WHERE id = $1", id)
    if err != nil {
        if errors.Is(err, sql.ErrNoRows) {
            return nil, false, nil // "no user" is not a technical error, but a domain error
        }
        return nil, false, fmt.Errorf("querying user %s: %w", id, err)
    }

    return &user, true, nil
}

Always close rows
rows, err := db.QueryContext(ctx, "SELECT id, name FROM users")
if err != nil {
    return fmt.Errorf("querying users: %w", err)
}
defer rows.Close() // prevents connection leaks

for rows.Next() {
    // ...
}
if err := rows.Err(); err != nil { // always check after iteration
    return fmt.Errorf("iterating users: %w", err)
}

Common database error patterns
Error	How to detect	Action
Row not found	errors.Is(err, sql.ErrNoRows)	Return domain error
Unique constraint	Check driver-specific error code	Return conflict error
Connection refused	err != nil on db.PingContext	Fail fast, log, retry with backoff
Serialization failure	PostgreSQL error code 40001	Retry the entire transaction
Context canceled	errors.Is(err, context.Canceled)	Stop processing, propagate
Context Propagation

Always use the *Context method variants to propagate deadlines and cancellation:

// ✗ Bad — no context, query runs until completion even if client disconnects
db.Query("SELECT ...")

// ✓ Good — respects context cancellation and timeouts
db.QueryContext(ctx, "SELECT ...")


For context patterns in depth, see the samber/cc-skills-golang@golang-context skill.

Transactions, Isolation Levels, and Locking

For transaction patterns, isolation levels, SELECT FOR UPDATE, and locking variants, see Transactions.

Connection Pool
db.SetMaxOpenConns(25)              // limit total connections
db.SetMaxIdleConns(10)              // keep warm connections ready
db.SetConnMaxLifetime(5 * time.Minute)  // recycle stale connections
db.SetConnMaxIdleTime(1 * time.Minute)  // close idle connections faster


For sizing guidance and formulas, see Database Performance.

Migrations

Use an external migration tool. Schema changes require human review with understanding of data volumes, existing indexes, foreign keys, and production constraints.

Recommended tools:

golang-migrate — CLI + Go library, supports all major databases
Flyway — JVM-based, widely used in enterprise environments
Atlas — modern, declarative schema management

Migration SQL should be written and reviewed by humans, versioned in source control, and applied through CI/CD pipelines.

Avoid Hidden SQL Features

Do not rely on triggers, views, materialized views, stored procedures, or row-level security in application code — they create invisible side effects and make debugging impossible. Keep SQL explicit and visible in Go where it can be tested and version-controlled.

Schema Creation

This skill does NOT cover schema creation. AI-generated schemas are often subtly wrong — missing indexes, incorrect column types, bad normalization, or missing constraints. Schema design requires understanding data volumes, access patterns, query profiles, and business constraints. Use dedicated database tooling and human review.

Deep Dives
Transactions — Transaction boundaries, isolation levels, deadlock prevention, SELECT FOR UPDATE
Testing Database Code — Mock connections, integration tests with containers, fixtures, schema setup/teardown
Database Performance — Connection pool sizing, batch processing, indexing strategy, query optimization
Struct Scanning — Struct tags, NULLable column handling, JSON marshaling patterns
Cross-References
→ See samber/cc-skills-golang@golang-security skill for SQL injection prevention patterns
→ See samber/cc-skills-golang@golang-context skill for context propagation to database operations
→ See samber/cc-skills-golang@golang-error-handling skill for database error wrapping patterns
→ See samber/cc-skills-golang@golang-testing skill for database integration test patterns
References
database/sql tutorial
sqlx
pgx
golang-migrate
Weekly Installs
1.8K
Repository
samber/cc-skills-golang
GitHub Stars
1.5K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass