---
title: domain-web
url: https://skills.sh/actionbook/rust-skills/domain-web
---

# domain-web

skills/actionbook/rust-skills/domain-web
domain-web
Originally fromzhanghandong/rust-skills
Installation
$ npx skills add https://github.com/actionbook/rust-skills --skill domain-web
SKILL.md
Web Domain

Layer 3: Domain Constraints

Domain Constraints → Design Implications
Domain Rule	Design Constraint	Rust Implication
Stateless HTTP	No request-local globals	State in extractors
Concurrency	Handle many connections	Async, Send + Sync
Latency SLA	Fast response	Efficient ownership
Security	Input validation	Type-safe extractors
Observability	Request tracing	tracing + tower layers
Critical Constraints
Async by Default
RULE: Web handlers must not block
WHY: Block one task = block many requests
RUST: async/await, spawn_blocking for CPU work

State Management
RULE: Shared state must be thread-safe
WHY: Handlers run on any thread
RUST: Arc<T>, Arc<RwLock<T>> for mutable

Request Lifecycle
RULE: Resources live only for request duration
WHY: Memory management, no leaks
RUST: Extractors, proper ownership

Trace Down ↓

From constraints to design (Layer 2):

"Need shared application state"
    ↓ m07-concurrency: Use Arc for thread-safe sharing
    ↓ m02-resource: Arc<RwLock<T>> for mutable state

"Need request validation"
    ↓ m05-type-driven: Validated extractors
    ↓ m06-error-handling: IntoResponse for errors

"Need middleware stack"
    ↓ m12-lifecycle: Tower layers
    ↓ m04-zero-cost: Trait-based composition

Framework Comparison
Framework	Style	Best For
axum	Functional, tower	Modern APIs
actix-web	Actor-based	High performance
warp	Filter composition	Composable APIs
rocket	Macro-driven	Rapid development
Key Crates
Purpose	Crate
HTTP server	axum, actix-web
HTTP client	reqwest
JSON	serde_json
Auth/JWT	jsonwebtoken
Session	tower-sessions
Database	sqlx, diesel
Middleware	tower
Design Patterns
Pattern	Purpose	Implementation
Extractors	Request parsing	State(db), Json(payload)
Error response	Unified errors	impl IntoResponse
Middleware	Cross-cutting	Tower layers
Shared state	App config	Arc<AppState>
Code Pattern: Axum Handler
async fn handler(
    State(db): State<Arc<DbPool>>,
    Json(payload): Json<CreateUser>,
) -> Result<Json<User>, AppError> {
    let user = db.create_user(&payload).await?;
    Ok(Json(user))
}

// Error handling
impl IntoResponse for AppError {
    fn into_response(self) -> Response {
        let (status, message) = match self {
            Self::NotFound => (StatusCode::NOT_FOUND, "Not found"),
            Self::Internal(_) => (StatusCode::INTERNAL_SERVER_ERROR, "Internal error"),
        };
        (status, Json(json!({"error": message}))).into_response()
    }
}

Common Mistakes
Mistake	Domain Violation	Fix
Blocking in handler	Latency spike	spawn_blocking
Rc in state	Not Send + Sync	Use Arc
No validation	Security risk	Type-safe extractors
No error response	Bad UX	IntoResponse impl
Trace to Layer 1
Constraint	Layer 2 Pattern	Layer 1 Implementation
Async handlers	Async/await	tokio runtime
Thread-safe state	Shared state	Arc, Arc<RwLock>
Request lifecycle	Extractors	Ownership via From
Middleware	Tower layers	Trait-based composition
Related Skills
When	See
Async patterns	m07-concurrency
State management	m02-resource
Error handling	m06-error-handling
Middleware design	m12-lifecycle
Weekly Installs
460
Repository
actionbook/rust-skills
GitHub Stars
1.1K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass