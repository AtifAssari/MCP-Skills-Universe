---
title: frontend-async-best-practices
url: https://skills.sh/sergiodxa/agent-skills/frontend-async-best-practices
---

# frontend-async-best-practices

skills/sergiodxa/agent-skills/frontend-async-best-practices
frontend-async-best-practices
Installation
$ npx skills add https://github.com/sergiodxa/agent-skills --skill frontend-async-best-practices
SKILL.md
Async Best Practices

Performance optimization patterns for asynchronous JavaScript code. Contains 5 rules focused on eliminating request waterfalls and maximizing parallelism.

Impact: CRITICAL - Waterfalls are the #1 performance killer. Each sequential await adds full network latency.

When to Apply

Reference these guidelines when:

Writing Remix loaders or actions
Implementing data fetching logic
Working with multiple async operations
Reviewing code for waterfall patterns
Optimizing response times
Rules Summary
parallel (CRITICAL) — @rules/parallel.md

Use Promise.all() for independent operations.

// Bad: 3 sequential round trips
const user = await fetchUser();
const posts = await fetchPosts();
const comments = await fetchComments();

// Good: 1 parallel round trip
const [user, posts, comments] = await Promise.all([
  fetchUser(),
  fetchPosts(),
  fetchComments(),
]);

defer-await (HIGH) — @rules/defer-await.md

Move await into branches where actually used.

// Bad: always waits even when skipping
async function handle(skip: boolean) {
  let data = await fetchData();
  if (skip) return { skipped: true };
  return process(data);
}

// Good: only waits when needed
async function handle(skip: boolean) {
  if (skip) return { skipped: true };
  let data = await fetchData();
  return process(data);
}

dependencies (CRITICAL) — @rules/dependencies.md

Chain dependent operations, parallelize independent ones.

// Bad: profile waits for config unnecessarily
const [user, config] = await Promise.all([fetchUser(), fetchConfig()]);
const profile = await fetchProfile(user.id);

// Good: profile starts as soon as user resolves
const userPromise = fetchUser();
const profilePromise = userPromise.then((user) => fetchProfile(user.id));

const [user, config, profile] = await Promise.all([
  userPromise,
  fetchConfig(),
  profilePromise,
]);

api-routes (CRITICAL) — @rules/api-routes.md

Start promises early, await late in loaders.

// Bad: sequential execution
export async function loader() {
  let session = await auth();
  let config = await fetchConfig();
  return { session, config };
}

// Good: parallel execution
export async function loader() {
  let sessionPromise = auth();
  let configPromise = fetchConfig();
  const [session, config] = await Promise.all([sessionPromise, configPromise]);
  return { session, config };
}

suspense-boundaries (HIGH) — @rules/suspense-boundaries.md

Use Suspense to show UI immediately while data loads.

// Bad: entire page blocked by data
async function Page() {
  let data = await fetchData();
  return (
    <Layout>
      <Content data={data} />
    </Layout>
  );
}

// Good: layout shows immediately, content streams in
function Page() {
  return (
    <Layout>
      <Suspense fallback={<Skeleton />}>
        <Content />
      </Suspense>
    </Layout>
  );
}

Weekly Installs
119
Repository
sergiodxa/agent-skills
GitHub Stars
83
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass