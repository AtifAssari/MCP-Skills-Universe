---
rating: ⭐⭐
title: how-to-store-sqlite-as-nosql-store
url: https://skills.sh/rodydavis/skills/how-to-store-sqlite-as-nosql-store
---

# how-to-store-sqlite-as-nosql-store

skills/rodydavis/skills/how-to-store-sqlite-as-nosql-store
how-to-store-sqlite-as-nosql-store
Installation
$ npx skills add https://github.com/rodydavis/skills --skill how-to-store-sqlite-as-nosql-store
SKILL.md
How to store SQLite as NoSQL Store

SQLite is a very capable edge database that can store various shapes of data.

NoSQL databases are very popular due to the schema-less nature of storing of the data but it is totally possible to store these documents in SQLite.

SQLite actually has great JSON support and even supports JSONB.

Create the table 

To store JSON documents we need to create a table to store the values as strings.

CREATE TABLE documents (
  path TEXT NOT NULL PRIMARY KEY,
  data TEXT,
  ttl INTEGER,
  created INTEGER NOT NULL,
  updated INTEGER NOT NULL,
  UNIQUE(path)
);


path

data

ttl

created

updated

/posts/1

{"id":1}

NULL

0

0

/posts/2

{"id":2}

NULL

0

0

/users/1

{"id":1}

NULL

0

0

The basic idea is to store a JSON object and an unique path.

There is an optional TTL to automatically delete rows when they reach the stale date.

Save a document 

To save a document we can encode our JSON as a string or binary and save in in the table with a unique path.

INSERT OR REPLACE 
INTO documents (path, data, ttl, created, updated) 
VALUES (:path, :data, :ttl, :created, :updated)
RETURNING *;


You can also use JSON functions to save the Object to a valid JSON string.

INSERT OR REPLACE 
INTO documents (path, data, ttl, created, updated) 
VALUES ("/posts/1", json('{"id" 1}'), NULL, 0, 0)
RETURNING *;


path

data

ttl

created

updated

/posts/1

{"id":1}

NULL

0

0

Reading a document 

To read a document we just need the path. If a TTL is set we can calculate if the current date is greater than the offset and not return the document.

SELECT * FROM documents 
WHERE path = :path
AND (
	(ttl IS NOT NULL AND ttl + updated < unixepoch())
	OR
	ttl IS NULL
);


path

data

ttl

created

updated

/posts/1

{"id":1}

NULL

0

0

Get documents for a collection 

We can query all the docs for a given collection using some built-in functions and a path prefix:

SELECT *
FROM documents 
WHERE (
	path LIKE :prefix
	AND
	(LENGTH(path) - LENGTH(REPLACE(path, '/', ''))) = (LENGTH(:prefix) - LENGTH(REPLACE(:prefix, '/', '')))
)
AND (
	(ttl IS NOT NULL AND ttl + updated < unixepoch())
	OR
	ttl IS NULL
)
ORDER BY created;


It is expected to search for a :prefix with the /% at the end:

"/my/path/%" // search for /my/path

Deleting expired documents 

Using the TTL field we can delete all expired documents:

DELETE FROM documents
WHERE ttl IS NOT NULL
AND ttl + updated < unixepoch();

Demo
Weekly Installs
37
Repository
rodydavis/skills
GitHub Stars
40
First Seen
Feb 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass