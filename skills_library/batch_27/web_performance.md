---
title: web-performance
url: https://skills.sh/alexanderstephenthompson/claude-hub/web-performance
---

# web-performance

skills/alexanderstephenthompson/claude-hub/web-performance
web-performance
Installation
$ npx skills add https://github.com/alexanderstephenthompson/claude-hub --skill web-performance
SKILL.md
Web Performance Skill

Version: 1.0 Stack: Apollo Client/Server + Redis + CloudFront + S3

Performance problems are invisible during development. Local servers are fast. Test data is small. You don't notice the 3MB bundle, the N+1 queries, or the full-table scan until real users on real connections with real data report that the page takes 8 seconds to load. By then, fixing it requires rearchitecting the caching layer, splitting the bundle, and rewriting queries — all at once, under pressure.

Performance patterns applied from the start are cheap. Performance fixes applied after launch are expensive. These rules are the cheap version.

Core Principles
Measure First — Profile before optimizing. Don't guess.
Cache at Every Layer — CDN → API → Database → In-Memory.
Minimize Payload — Send only what's needed.
Defer Non-Critical — Load critical path first, everything else later.
Perceived Performance — Optimistic UI makes things feel faster.
Core Web Vitals Targets
Metric	What It Measures	Target	Critical
LCP (Largest Contentful Paint)	Main content loaded	< 2.5s	< 4s
INP (Interaction to Next Paint)	Input responsiveness	< 200ms	< 500ms
CLS (Cumulative Layout Shift)	Visual stability	< 0.1	< 0.25
Apollo Client Caching

Configure InMemoryCache with type policies for pagination merging and computed fields. Use cache-and-network as default fetch policy (stale-while-revalidate). Use optimistic updates for mutations to make UI feel instant.

Fetch Policies
Policy	Use Case
cache-first	Static data (categories, config)
cache-and-network	Data that changes (products, user data)
network-only	Always fresh (order status, real-time)
cache-only	Offline mode, known-cached data

See assets/caching-patterns.md for cache configuration, fetch policy examples, and optimistic update patterns.

Redis Caching

Cache-aside pattern: check cache → miss → fetch DB → store in cache. Invalidate on writes. Use tag-based invalidation for list queries.

TTL Guidelines
Data Type	TTL	Reason
Static config	24h+	Rarely changes
Product catalog	1h	Changes occasionally
User sessions	30m	Security balance
Cart data	7d	User convenience
Search results	5m	Balance freshness/speed
Real-time data	No cache	Must be live

See assets/caching-patterns.md for Redis cache service, cache-aside pattern, and invalidation examples.

CloudFront & S3 Optimization

Immutable assets (hashed filenames) get 365-day cache. API routes get no CDN caching. Images get resize-on-demand with WebP format, lazy loading, and 2x srcSet for retina.

See assets/caching-patterns.md for CDK configuration and image optimization component.

Bundle Optimization

Route-based code splitting with React.lazy. Dynamic imports for heavy libraries (load only when needed). Analyze with source-map-explorer.

Bundle Size Guidelines
Category	Target	Action if Exceeded
Initial JS	< 100KB gzipped	Code split, tree shake
Vendor chunk	< 150KB gzipped	Lazy load, find alternatives
Route chunk	< 50KB gzipped	Split further
Total initial load	< 200KB gzipped	Audit dependencies

See assets/optimization-patterns.md for code splitting, dynamic import, and bundle analysis examples.

React Performance

Use useMemo for expensive computations, useCallback for stable callbacks passed to memoized children, and memo for list item components. Don't memoize simple values, always-changing values, or handlers on non-memoized children. Use virtualization for long lists (100+ items).

See assets/optimization-patterns.md for memoization, when-NOT-to-memoize, and virtualization examples.

Database Performance

Select only needed fields. Use include sparingly. Use raw queries for complex aggregations. Add compound indices on filtered/sorted columns.

See assets/optimization-patterns.md for Prisma query optimization and index strategy.

Anti-Patterns
Anti-Pattern	Problem	Fix
Fetching all fields	Over-fetching, slow	Select only needed fields
No pagination	Memory issues, slow	Cursor-based pagination
Cache everything	Stale data, complexity	Cache strategically by TTL
Premature optimization	Wasted effort	Measure first, optimize hotspots
Sync heavy operations	Blocks response	Background jobs (Bull)
No CDN for static assets	Slow global delivery	CloudFront for static files
Unoptimized images	Huge downloads	Resize, compress, WebP
Blocking bundle	Slow initial load	Code split, lazy load
Checklist
Frontend
 Code split by route
 Heavy libraries lazy loaded
 Images lazy loaded
 Images optimized (WebP, sized)
 Bundle < 200KB initial
 useMemo/useCallback where beneficial
 Long lists virtualized
Apollo
 Cache policies configured
 Pagination merges correctly
 Optimistic updates for mutations
 Fetch policy matches data freshness needs
Redis
 Hot data cached
 TTLs appropriate for data type
 Cache invalidation on updates
 Connection pooling configured
Database
 Indices on filtered/sorted columns
 Select only needed fields
 N+1 queries eliminated (DataLoader)
 Expensive queries analyzed
CDN
 Static assets on CloudFront
 Immutable assets cached forever
 Dynamic content not cached at edge
 HTTPS enforced
When to Consider Alternatives
Situation	Consider
Global real-time data	Redis Pub/Sub or WebSockets
Heavy computation	Background workers (Bull)
Large file uploads	Direct S3 presigned URLs
Search-heavy	Elasticsearch or Algolia
Edge computing needs	CloudFront Functions or Lambda@Edge
References
assets/caching-patterns.md — Apollo cache config, Redis, CloudFront, image optimization
assets/optimization-patterns.md — Bundle splitting, React memoization, virtualization, DB optimization
Weekly Installs
22
Repository
alexanderstephe…aude-hub
GitHub Stars
1
First Seen
Feb 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass