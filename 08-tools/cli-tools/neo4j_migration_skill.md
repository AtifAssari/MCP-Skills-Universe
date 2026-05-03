---
title: neo4j-migration-skill
url: https://skills.sh/neo4j-contrib/neo4j-skills/neo4j-migration-skill
---

# neo4j-migration-skill

skills/neo4j-contrib/neo4j-skills/neo4j-migration-skill
neo4j-migration-skill
Installation
$ npx skills add https://github.com/neo4j-contrib/neo4j-skills --skill neo4j-migration-skill
SKILL.md
Neo4j migration skill

This skill uses online guides to upgrade old Neo4j codebases and Cypher queries. It handles all official Neo4j drivers and Cypher syntax migration.

When to use

Use this skill when:

a user asks to upgrade a Neo4j driver in languages: .NET, Go, Java, Javascript, Python
a user wants to upgrade Cypher queries from 4.x or 5.x syntax to 2025.x/2026.x (Cypher 25)
When NOT to use this skill
Writing new Cypher queries → use neo4j-cypher-skill
Database administration or CLI tasks (backup, restore, import, cypher-shell) → use neo4j-cli-tools-skill
Starting a new Neo4j project from scratch → use neo4j-getting-started-skill
Instructions

At the beginning, ALWAYS ask a user what Neo4j version is going to be used after the upgrade. Note, the Neo4j database's version is not upgraded as part of this skill, we just need that information a) If the user says that most recent, fetch the version from the supported version list along with the most recent driver version b) Otherwise, analyze the supported versions list and choose the most recent driver version for given Neo4j version

Analyze the codebase in order to determine what additional documentation to include, focus only on dependencies' files (e.g. package.json, requirements.txt, pom.xml etc.). If the codebase uses Neo4j driver for:

.NET then include .NET migration guide
Go then include Go migration guide
Java then include Java migration guide
Javascript/Node.JS then include Javascript migration guide
Python then include Python migration guide

Important: when you plan the upgrade, always include replacement of deprecated functions in the plan

Cypher Query Migration (4.x / 5.x → Cypher 25)
Ask the user what target Neo4j version will be used after the upgrade
Scan the codebase for Cypher query strings (look in .cypher files, string literals in driver code, OGM/SDN @Query annotations, etc.)
Apply these substitutions to every query found:
Old syntax	Cypher 25 replacement
[:REL*1..5]	-[:REL]-{1,5}
[:REL*]	-[:REL]-{1,}
shortestPath((a)-[*]->(b))	SHORTEST 1 (a)(()-[]->()){1,}(b)
allShortestPaths((a)-[*]->(b))	ALL SHORTEST (a)(()-[]->()){1,}(b)
id(n)	elementId(n)
CALL { WITH x ... }	CALL (x) { ... }
-- SQL comment	// Cypher comment
CALL db.index.vector.queryNodes(...)	SEARCH n IN (VECTOR INDEX idx FOR $emb LIMIT k) SCORE AS score (2026.01+; keep procedure for older)
Prepend CYPHER 25 to every query
Fetch the migration guide for any syntax not covered above: https://neo4j.com/docs/cypher-manual/25/deprecations-additions-removals-compatibility/
Weekly Installs
78
Repository
neo4j-contrib/n…j-skills
GitHub Stars
39
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn