---
title: how-to-do-full-text-search-with-sqlite
url: https://skills.sh/rodydavis/skills/how-to-do-full-text-search-with-sqlite
---

# how-to-do-full-text-search-with-sqlite

skills/rodydavis/skills/how-to-do-full-text-search-with-sqlite
how-to-do-full-text-search-with-sqlite
Installation
$ npx skills add https://github.com/rodydavis/skills --skill how-to-do-full-text-search-with-sqlite
SKILL.md
How to do Full Text Search with SQLite

SQLite has a powerful way to add new functionality via loadable extensions. The first-party ones include fts5, json1 and a couple others.

When building applications it is common to add searching features based on data coming from tables and you may already have queries for fuzzy searching with LIKE. You may be excited to hear that SQLite can easily add fully query capabilities over a dataset all with just a simple MATCH keyword. 👀

Creating your first search index 

Full text search in SQLite requires storing the index in VIRTUAL tables, which allow for optimized storage of the index based on the queries we will execute against it.

You can create the virtual table for the index making sure to include the USING directive for the fts5 target.

CREATE VIRTUAL TABLE posts_fts USING fts5 (
    title,
    description,
    content,
    content=posts,
    content_rowid=id
);


Text IDs are also supported instead of just INTEGERS.

This is a standard callout. You can customize its content and even the icon.

Contentless tables 

You can also create a contentless table that will not be based on any existing tables:

CREATE VIRTUAL TABLE example_fts USING fts5 (
    name,
    description,
    content=''
);

Keeping the index up to date 

By having the source content be stored in another table we need to make sure to keep both tables in sync and avoid updating the index in a hot path when trying to make a query.

By default when you create table it will be empty, even if the source table is populated. You do have various options for populating the index.

Update by query 

If you use a contentless table or want to pull in data from a view you can update by query.

INSERT INTO posts_fts (id, title, description, content)
SELECT id, title, description, content FROM posts;

Rebuild command 

Using the rebuild command it will update the index based on the content table specified.

INSERT INTO posts_fts(posts_fts) VALUES('rebuild');

Triggers 

We can use SQLite triggers to automatically keep the records updated:

CREATE TRIGGER posts_insert AFTER INSERT ON posts BEGIN
  INSERT INTO posts_fts(id, title, description, content)
  VALUES (new.id, new.title, new.description, new.content);
END;

CREATE TRIGGER posts_delete AFTER DELETE ON posts BEGIN
  INSERT INTO posts_fts(posts_fts, id, title, description, content)
  VALUES ('delete', old.id, old.title, old.description, old.content);
END;

CREATE TRIGGER posts_update AFTER UPDATE ON posts BEGIN
  INSERT INTO posts_fts(posts_fts, id, title, description, content)
  VALUES ('delete', old.id, old.title, old.description, old.content);
  INSERT INTO posts_fts(id, title, description, content)
  VALUES (new.id, new.title, new.description, new.content);
END;


This will always ensure the two tables are in sync for any CRUD actions on the source table.

Searching the index 
Query syntax 

Here is the supported query syntax:

<phrase>    := string [*]
<phrase>    := <phrase> + <phrase>
<neargroup> := NEAR ( <phrase> <phrase> ... [, N] )
<query>     := [ [-] <colspec> :] [^] <phrase>
<query>     := [ [-] <colspec> :] <neargroup>
<query>     := [ [-] <colspec> :] ( <query> )
<query>     := <query> AND <query>
<query>     := <query> OR <query>
<query>     := <query> NOT <query>
<colspec>   := colname
<colspec>   := { colname1 colname2 ... }


To preform an actual query on the index we will need to use the MATCH keyword and order by the rank.

SELECT posts.* FROM posts_fts
INNER JOIN posts ON posts.id = posts_fts.rowid
WHERE posts_fts MATCH :query
ORDER BY rank;

Demo
Reference 
https://www.sqlite.org/fts5.html
https://docs.datasette.io/en/latest/full_text_search.html
Weekly Installs
54
Repository
rodydavis/skills
GitHub Stars
40
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass