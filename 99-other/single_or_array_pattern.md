---
title: single-or-array-pattern
url: https://skills.sh/epicenterhq/epicenter/single-or-array-pattern
---

# single-or-array-pattern

skills/epicenterhq/epicenter/single-or-array-pattern
single-or-array-pattern
Installation
$ npx skills add https://github.com/epicenterhq/epicenter --skill single-or-array-pattern
SKILL.md
Single-or-Array Pattern

Accept both single items and arrays, normalize at the top, process uniformly.

Quick Reference
function create(itemOrItems: T | T[]): Promise<Result<void, E>> {
	const items = Array.isArray(itemOrItems) ? itemOrItems : [itemOrItems];
	// ... implementation works on items array
}

The Structure
Accept T | T[] as the parameter type
Normalize with Array.isArray() at the top of the function
All logic works against the array — one code path
function createServer(clientOrClients: Client | Client[], options?: Options) {
	const clients = Array.isArray(clientOrClients)
		? clientOrClients
		: [clientOrClients];

	// All real logic here, working with the array
	for (const client of clients) {
		// ...
	}
}

Naming Conventions
Parameter	Normalized Variable
recordingOrRecordings	recordings
clientOrClients	clients
itemOrItems	items
paramsOrParamsArray	paramsArray
When to Use

Good fit:

CRUD operations (create, update, delete)
Batch processing APIs
Factory functions accepting dependencies
Any "do this to one or many" scenario

Skip when:

Single vs batch have different semantics
Return types vary significantly
Array version needs different options
Codebase Examples
Server Factory (packages/server/src/server.ts)
function createServer(
	clientOrClients: AnyWorkspaceClient | AnyWorkspaceClient[],
	options?: ServerOptions,
) {
	const clients = Array.isArray(clientOrClients)
		? clientOrClients
		: [clientOrClients];

	// All server setup logic directly here
	const workspaces: Record<string, AnyWorkspaceClient> = {};
	for (const client of clients) {
		workspaces[client.id] = client;
	}
	// ...
}

Database Service (apps/whispering/src/lib/services/isomorphic/db/web.ts)
delete: async (recordingOrRecordings) => {
  const recordings = Array.isArray(recordingOrRecordings)
    ? recordingOrRecordings
    : [recordingOrRecordings];
  const ids = recordings.map((r) => r.id);
  return tryAsync({
    try: () => db.recordings.bulkDelete(ids),
    catch: (error) => DbError.MutationFailed({ cause: error }),
  });
},

Query Mutations (apps/whispering/src/lib/query/isomorphic/db.ts)
delete: defineMutation({
  mutationFn: async (recordings: Recording | Recording[]) => {
    const recordingsArray = Array.isArray(recordings)
      ? recordings
      : [recordings];

    for (const recording of recordingsArray) {
      services.db.recordings.revokeAudioUrl(recording.id);
    }

    const { error } = await services.db.recordings.delete(recordingsArray);
    if (error) return Err(error);
    return Ok(undefined);
  },
}),

Anti-Patterns
Don't: Separate functions for single vs array
// Harder to maintain, users must remember two APIs
function createRecording(recording: Recording): Promise<...>;
function createRecordings(recordings: Recording[]): Promise<...>;

Don't: Force arrays everywhere
// Awkward for single items
createRecordings([recording]); // Ugly

Don't: Duplicate logic in overloads
// BAD: Logic duplicated
function create(item: T) {
	return db.insert(item); // Duplicated
}
function create(items: T[]) {
	return db.bulkInsert(items); // Different code path
}

// GOOD: Single implementation
function create(itemOrItems: T | T[]) {
	const items = Array.isArray(itemOrItems) ? itemOrItems : [itemOrItems];
	return db.bulkInsert(items); // One code path
}

References
Full article — detailed explanation with more examples
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