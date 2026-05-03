---
rating: ⭐⭐⭐
title: rust-patterns
url: https://skills.sh/phrazzld/claude-config/rust-patterns
---

# rust-patterns

skills/phrazzld/claude-config/rust-patterns
rust-patterns
Installation
$ npx skills add https://github.com/phrazzld/claude-config --skill rust-patterns
SKILL.md
Rust Patterns

Ownership-first, zero-cost abstractions, no hidden complexity.

Error Handling

Always use Result<T, E>. Never panic for expected failures:

// Use thiserror for library error types
#[derive(Debug, thiserror::Error)]
pub enum UserError {
    #[error("user not found: {0}")]
    NotFound(String),
    #[error("invalid email format")]
    InvalidEmail,
    #[error("database error: {0}")]
    Database(#[from] sqlx::Error),
}

// Use anyhow for applications (context chaining)
fn fetch_user(id: &str) -> anyhow::Result<User> {
    let user = db.get(id)
        .context("fetching user from database")?;
    Ok(user)
}


Propagate with ?, add context at boundaries.

Ownership Patterns

Borrowing > Cloning:

// Good: Borrow for read-only
fn process(items: &[Item]) -> usize { ... }

// Good: Take ownership when storing/transforming
fn consume(items: Vec<Item>) -> Output { ... }

// Avoid: Excessive cloning
fn bad(items: &Vec<Item>) {
    let copy = items.clone(); // Usually unnecessary
}


Fight the borrow checker → redesign, don't circumvent.

Trait Design

Small, focused traits (1-3 methods):

trait Readable {
    type Item;
    fn read(&self) -> Self::Item;
}

trait Writable {
    type Item;
    fn write(&mut self, item: Self::Item);
}

// Compose through bounds
fn copy<R, W>(src: &R, dst: &mut W)
where
    R: Readable<Item = Vec<u8>>,
    W: Writable<Item = Vec<u8>>,
{ ... }


Consumer-side interfaces. Static dispatch by default.

Configuration

Cargo features for compile-time options:

[features]
default = ["json"]
json = ["serde_json"]
database = ["sqlx"]
full = ["json", "database"]

#[cfg(feature = "json")]
pub mod json_support { ... }

Unsafe

Minimize. Document with // SAFETY: comments:

// SAFETY: We verified ptr is non-null and properly aligned
// in the caller's bounds check above
unsafe { *ptr }


Abstract behind safe interfaces.

Anti-Patterns
unwrap() / expect() for recoverable errors
Result<T, String> (use typed errors)
Excessive Rc<RefCell<T>> (redesign ownership)
Monolithic traits (10+ methods)
Reflection instead of generics
Fighting borrow checker with unsafe
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