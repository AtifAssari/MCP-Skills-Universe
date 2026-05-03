---
title: factory-function-composition
url: https://skills.sh/epicenterhq/epicenter/factory-function-composition
---

# factory-function-composition

skills/epicenterhq/epicenter/factory-function-composition
factory-function-composition
Installation
$ npx skills add https://github.com/epicenterhq/epicenter --skill factory-function-composition
SKILL.md
Factory Function Composition

This skill helps you apply factory function patterns for clean dependency injection and function composition in TypeScript.

Related Skills: See method-shorthand-jsdoc for when to move helpers into the return object. See refactoring for caller counting and inlining single-use extractions.

When to Apply This Skill

Use this pattern when you see:

A function that takes a client/resource as its first argument
Options from different layers (client, service, method) mixed together
Client creation happening inside functions that shouldn't own it
Functions that are hard to test because they create their own dependencies
The Universal Signature

Every factory function follows this signature:

function createSomething(dependencies, options?) {
	return {
		/* methods */
	};
}

First argument: Always the resource(s). Either a single client or a destructured object of multiple dependencies.
Second argument: Optional configuration specific to this factory. Never client config—that belongs at client creation.

Two arguments max. First is resources, second is config. No exceptions.

The Core Pattern
// Single dependency
function createService(client, options = {}) {
	return {
		method(methodOptions) {
			// Uses client, options, and methodOptions
		},
	};
}

// Multiple dependencies
function createService({ db, cache }, options = {}) {
	return {
		method(methodOptions) {
			// Uses db, cache, options, and methodOptions
		},
	};
}

// Usage
const client = createClient(clientOptions);
const service = createService(client, serviceOptions);
service.method(methodOptions);

Key Principles
Client configuration belongs at client creation time — don't pipe clientOptions through your factory
Each layer has its own options — client, service, and method options stay separate
Dependencies come first — factory functions take dependencies as the first argument
Return objects with methods — not standalone functions that need the resource passed in
Recognizing the Anti-Patterns
Anti-Pattern 1: Function takes client as first argument
// Bad
function doSomething(client, options) { ... }
doSomething(client, options);

// Good
const service = createService(client);
service.doSomething(options);

Anti-Pattern 2: Client creation hidden inside
// Bad
function doSomething(clientOptions, methodOptions) {
	const client = createClient(clientOptions); // Hidden!
	// ...
}

// Good
const client = createClient(clientOptions);
const service = createService(client);
service.doSomething(methodOptions);

Anti-Pattern 3: Mixed options blob
// Bad
doSomething({
	timeout: 5000, // Client option
	retries: 3, // Client option
	endpoint: '/users', // Method option
	payload: data, // Method option
});

// Good
const client = createClient({ timeout: 5000, retries: 3 });
const service = createService(client);
service.doSomething({ endpoint: '/users', payload: data });

Anti-Pattern 4: Multiple layers hidden
// Bad
function doSomething(clientOptions, serviceOptions, methodOptions) {
	const client = createClient(clientOptions);
	const service = createService(client, serviceOptions);
	return service.method(methodOptions);
}

// Good — each layer visible and configurable
const client = createClient(clientOptions);
const service = createService(client, serviceOptions);
service.method(methodOptions);

Multiple Dependencies

When your service needs multiple clients:

function createService(
	{ db, cache, http }, // Dependencies as destructured object
	options = {}, // Service options
) {
	return {
		method(methodOptions) {
			// Uses db, cache, http
		},
	};
}

// Usage
const db = createDbConnection(dbOptions);
const cache = createCacheClient(cacheOptions);
const http = createHttpClient(httpOptions);

const service = createService({ db, cache, http }, serviceOptions);
service.method(methodOptions);

The Canonical Internal Shape

The previous sections cover the external signature—(deps, options?) → return { methods }. This section covers what goes inside the function body. Every factory function follows a four-zone ordering:

// Option A — destructure in the signature (preferred for small dep lists)
function createSomething({ db, cache }: Deps, options?) {
	const maxRetries = options?.maxRetries ?? 3;
	// ...
}

// Option B — destructure in zone 1 (fine when you also need the deps object itself)
function createSomething(deps: Deps, options?) {
	const { db, cache } = deps;
	const maxRetries = options?.maxRetries ?? 3;
	// ...
}


Both are valid. The point is that by the time you reach zone 2, all dependencies and config are bound to const names. The four zones:

function createSomething({ db, cache }, options?) {
	// Zone 1 — Immutable state (const from deps/options)
	const maxRetries = options?.maxRetries ?? 3;

	// Zone 2 — Mutable state (let declarations)
	let connectionCount = 0;
	let lastError: Error | null = null;

	// Zone 3 — Private helpers
	function resetState() {
		connectionCount = 0;
		lastError = null;
	}

	// Zone 4 — Public API (always last)
	return {
		connect() { ... },
		disconnect() { ... },
		get errorCount() { return connectionCount; },
	};
}


Zones 1 and 2 can merge when there's little state. Zone 3 is empty for small factories. But the return object is always last—it's the complete public API.

The this Decision Rule

Inside the return object, public methods sometimes need to call other public methods. Use this.method() for that—method shorthand gives proper this binding.

If a function is called both by return-object methods and by pre-return initialization logic, it belongs in zone 3 (private helpers). Call it directly by name; no this needed.

Where the function lives	How to call it
Return object (zone 4)	this.method() from sibling methods
Private helper (zone 3)	Direct call by name: helperFn()
Both zones need it	Keep in zone 3, call by name everywhere

See Closures Are Better Privacy Than Keywords for the full rationale and real codebase examples.

The Mental Model

Think of it as a chain where each link:

Receives a resource from the previous link
Adds its own configuration
Produces something for the next link
createClient(...)  →  createService(client, ...)  →  service.method(...)
     ↑                       ↑                            ↑
 clientOptions          serviceOptions              methodOptions

Benefits
Testability: Inject mock clients easily
Reusability: Share clients across multiple services
Flexibility: Configure each layer independently
Clarity: Clear ownership of configuration at each level
References

See the full articles for more details:

The Universal Factory Function Signature — signature explained in depth
Stop Passing Clients as Arguments — practical guide
The Factory Function Pattern — detailed explanation
Factory Method Patterns — separating options and method patterns
Closures Are Better Privacy Than Keywords — internal anatomy and why closures beat class keywords
Weekly Installs
60
Repository
epicenterhq/epicenter
GitHub Stars
4.5K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass