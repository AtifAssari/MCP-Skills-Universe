---
title: axum
url: https://skills.sh/bobmatnyc/claude-mpm-skills/axum
---

# axum

skills/bobmatnyc/claude-mpm-skills/axum
axum
Installation
$ npx skills add https://github.com/bobmatnyc/claude-mpm-skills --skill axum
SKILL.md
Axum (Rust) - Production Web APIs
Overview

Axum is a Rust web framework built on Hyper and Tower. Use it for type-safe request handling with composable middleware, structured errors, and excellent testability.

Quick Start
Minimal server

✅ Correct: typed handler + JSON response

use axum::{routing::get, Json, Router};
use serde::Serialize;
use std::net::SocketAddr;

#[derive(Serialize)]
struct Health {
    status: &'static str,
}

async fn health() -> Json<Health> {
    Json(Health { status: "ok" })
}

#[tokio::main]
async fn main() {
    let app = Router::new().route("/health", get(health));

    let addr: SocketAddr = "0.0.0.0:3000".parse().unwrap();
    let listener = tokio::net::TcpListener::bind(addr).await.unwrap();
    axum::serve(listener, app).await.unwrap();
}


❌ Wrong: block the async runtime

async fn handler() {
    std::thread::sleep(std::time::Duration::from_secs(1)); // blocks executor
}

Core Concepts
Router + handlers

Handlers are async functions that return something implementing IntoResponse.

✅ Correct: route nesting

use axum::{routing::get, Router};

fn router() -> Router {
    let api = Router::new()
        .route("/users", get(list_users))
        .route("/users/:id", get(get_user));

    Router::new().nest("/api/v1", api)
}

async fn list_users() -> &'static str { "[]" }
async fn get_user() -> &'static str { "{}" }

Extractors

Prefer extractors for parsing and validation at the boundary:

Path<T>: typed path params
Query<T>: query strings
Json<T>: JSON bodies
State<T>: shared application state

✅ Correct: typed path + JSON

use axum::{extract::Path, Json};
use serde::{Deserialize, Serialize};

#[derive(Deserialize)]
struct CreateUser {
    email: String,
}

#[derive(Serialize)]
struct User {
    id: String,
    email: String,
}

async fn create_user(Json(body): Json<CreateUser>) -> Json<User> {
    Json(User { id: "1".into(), email: body.email })
}

async fn get_user(Path(id): Path<String>) -> Json<User> {
    Json(User { id, email: "a@example.com".into() })
}

Production Patterns
1) Shared state (DB pool, config, clients)

Use State<Arc<AppState>> and keep state immutable where possible.

✅ Correct: AppState via Arc

use axum::{extract::State, routing::get, Router};
use std::sync::Arc;

#[derive(Clone)]
struct AppState {
    build_sha: &'static str,
}

async fn version(State(state): State<Arc<AppState>>) -> String {
    state.build_sha.to_string()
}

fn app(state: Arc<AppState>) -> Router {
    Router::new().route("/version", get(version)).with_state(state)
}

2) Structured error handling (IntoResponse)

Centralize error mapping to HTTP status codes and JSON.

✅ Correct: AppError converts into response

use axum::{http::StatusCode, response::IntoResponse, Json};
use serde::Serialize;

#[derive(Debug)]
enum AppError {
    NotFound,
    BadRequest(&'static str),
    Internal,
}

#[derive(Serialize)]
struct ErrorBody {
    error: &'static str,
}

impl IntoResponse for AppError {
    fn into_response(self) -> axum::response::Response {
        let (status, msg) = match self {
            AppError::NotFound => (StatusCode::NOT_FOUND, "not_found"),
            AppError::BadRequest(_) => (StatusCode::BAD_REQUEST, "bad_request"),
            AppError::Internal => (StatusCode::INTERNAL_SERVER_ERROR, "internal"),
        };

        (status, Json(ErrorBody { error: msg })).into_response()
    }
}

3) Middleware (Tower layers)

Use tower-http for production-grade layers: tracing, timeouts, request IDs, CORS.

✅ Correct: trace + timeout + CORS

use axum::{routing::get, Router};
use std::time::Duration;
use tower::ServiceBuilder;
use tower_http::{
    cors::{Any, CorsLayer},
    timeout::TimeoutLayer,
    trace::TraceLayer,
};

fn app() -> Router {
    let layers = ServiceBuilder::new()
        .layer(TraceLayer::new_for_http())
        .layer(TimeoutLayer::new(Duration::from_secs(10)))
        .layer(CorsLayer::new().allow_origin(Any));

    Router::new()
        .route("/health", get(|| async { "ok" }))
        .layer(layers)
}

4) Graceful shutdown

Terminate on SIGINT/SIGTERM and let in-flight requests drain.

✅ Correct: with_graceful_shutdown

async fn shutdown_signal() {
    let ctrl_c = async {
        tokio::signal::ctrl_c().await.ok();
    };

    #[cfg(unix)]
    let terminate = async {
        tokio::signal::unix::signal(tokio::signal::unix::SignalKind::terminate())
            .ok()
            .and_then(|mut s| s.recv().await);
    };

    #[cfg(not(unix))]
    let terminate = std::future::pending::<()>();

    tokio::select! {
        _ = ctrl_c => {}
        _ = terminate => {}
    }
}

#[tokio::main]
async fn main() {
    let app = app();
    let listener = tokio::net::TcpListener::bind("0.0.0.0:3000").await.unwrap();

    axum::serve(listener, app)
        .with_graceful_shutdown(shutdown_signal())
        .await
        .unwrap();
}

Testing

Test routers without sockets using tower::ServiceExt.

✅ Correct: request/response test

use axum::{body::Body, http::Request, Router};
use tower::ServiceExt;

#[tokio::test]
async fn health_returns_ok() {
    let app: Router = super::app();

    let res = app
        .oneshot(Request::builder().uri("/health").body(Body::empty()).unwrap())
        .await
        .unwrap();

    assert_eq!(res.status(), 200);
}

Decision Trees
Axum vs other Rust frameworks
Prefer Axum for Tower middleware composition and typed extractors.
Prefer Actix Web for a mature ecosystem and actor-style runtime model.
Prefer Warp for functional filters and minimalism.
Anti-Patterns
Block the async runtime (std::thread::sleep, blocking I/O inside handlers).
Use unwrap() in request paths; return structured errors instead.
Run without timeouts; add request timeouts and upstream deadlines.
Resources
Axum docs: https://docs.rs/axum
Tower HTTP layers: https://docs.rs/tower-http
Tracing: https://docs.rs/tracing
Weekly Installs
255
Repository
bobmatnyc/claud…m-skills
GitHub Stars
40
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass