---
title: test-json-sql-join
url: https://skills.sh/bdambrosio/cognitive_workbench/test-json-sql-join
---

# test-json-sql-join

skills/bdambrosio/cognitive_workbench/test-json-sql-join
test-json-sql-join
Installation
$ npx skills add https://github.com/bdambrosio/cognitive_workbench --skill test-json-sql-join
SKILL.md
Test Join Primitive

Self-contained: Creates test data internally

Input:

Creates $papers: A, B, C, D
Creates $authors: A (Alice), B (Bob), E (Eve)

Operation: Inner join on id field

Expected Output: $joined collection with 2 items (A and B have matches)

Paper A + Author Alice
Paper B + Author Bob
Weekly Installs
27
Repository
bdambrosio/cogn…orkbench
GitHub Stars
9
First Seen
Feb 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass