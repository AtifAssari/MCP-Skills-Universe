---
rating: ⭐⭐
title: neo4j-cypher
url: https://skills.sh/michaelkeevildown/claude-agents-skills/neo4j-cypher
---

# neo4j-cypher

skills/michaelkeevildown/claude-agents-skills/neo4j-cypher
neo4j-cypher
Installation
$ npx skills add https://github.com/michaelkeevildown/claude-agents-skills --skill neo4j-cypher
SKILL.md
Neo4j Cypher
When to Use

Use this skill when writing, reviewing, or debugging Cypher queries for Neo4j. Covers query patterns, performance optimization, fraud-detection domain queries, and Neo4j 5+ syntax.

Core Query Patterns
MATCH and Filtering
-- Basic node match with property filter
MATCH (c:Customer {customerId: $customerId})
RETURN c

-- Relationship traversal
MATCH (c:Customer)-[:HAS_ACCOUNT]->(a:Account)
WHERE a.status = 'active'
RETURN c, a

-- Variable-length paths
MATCH path = (a:Account)-[:TRANSACTION*1..5]->(b:Account)
RETURN path

-- Multiple relationship types
MATCH (c:Customer)-[:HAS_EMAIL|HAS_PHONE|HAS_SSN]->(pii)
RETURN c, pii

OPTIONAL MATCH

Use when the related data may not exist. Without OPTIONAL, rows with no match are dropped entirely.

MATCH (c:Customer {customerId: $customerId})
OPTIONAL MATCH (c)-[:HAS_EMAIL]->(e:Email)
OPTIONAL MATCH (c)-[:HAS_PHONE]->(p:Phone)
RETURN c, collect(DISTINCT e) AS emails, collect(DISTINCT p) AS phones

WITH Chaining

Use WITH to pipe results between query stages, filter intermediate results, and control cardinality.

MATCH (c:Customer)-[:HAS_ACCOUNT]->(a:Account)
MATCH (a)-[:PERFORM]->(tx:Transaction)
WITH c, a, count(tx) AS txCount, sum(tx.amount) AS totalAmount
WHERE txCount > 10
RETURN c.customerId, a.accountNumber, txCount, totalAmount
ORDER BY totalAmount DESC

Aggregation
-- Group and aggregate
MATCH (a:Account)-[:PERFORM]->(tx:Transaction)
WITH a, count(tx) AS txCount, sum(tx.amount) AS total, avg(tx.amount) AS avgAmount
RETURN a.accountNumber, txCount, total, avgAmount
ORDER BY total DESC
LIMIT 20

-- collect() for lists — use DISTINCT to avoid duplicates from cartesian products
MATCH (c:Customer)-[:HAS_ACCOUNT]->(a:Account)
OPTIONAL MATCH (a)-[:PERFORM]->(tx:Transaction)
RETURN c.customerId,
       collect(DISTINCT a.accountNumber) AS accounts,
       count(DISTINCT tx) AS transactionCount

UNWIND

Expand a list into rows. Useful for parameterized batch operations.

UNWIND $accountNumbers AS accNum
MATCH (a:Account {accountNumber: accNum})
RETURN a

CASE Expressions
MATCH (tx:Transaction)
RETURN tx.amount,
  CASE
    WHEN tx.amount > 10000 THEN 'high'
    WHEN tx.amount > 1000 THEN 'medium'
    ELSE 'low'
  END AS riskTier

Subqueries (CALL {})
MATCH (c:Customer)
CALL (c) {
  MATCH (c)-[:HAS_ACCOUNT]->(a:Account)-[:PERFORM]->(tx:Transaction)
  RETURN sum(tx.amount) AS totalSpend
}
RETURN c.customerId, totalSpend
ORDER BY totalSpend DESC

Write Operations
CREATE and MERGE
-- CREATE always creates new
CREATE (c:Customer {customerId: $id, firstName: $first, lastName: $last})

-- MERGE finds or creates — always specify the minimal unique key
MERGE (e:Email {address: $email})
ON CREATE SET e.createdAt = datetime()
ON MATCH SET e.lastSeen = datetime()

-- MERGE relationship
MATCH (c:Customer {customerId: $customerId})
MATCH (e:Email {address: $email})
MERGE (c)-[:HAS_EMAIL]->(e)

SET and REMOVE
MATCH (a:Account {accountNumber: $accNum})
SET a.status = 'frozen', a.frozenAt = datetime(), a:Frozen
REMOVE a:Active

DELETE
-- Delete node and all its relationships
MATCH (n:TempNode {id: $id})
DETACH DELETE n

-- Delete specific relationship
MATCH (c:Customer)-[r:HAS_EMAIL]->(e:Email {address: $email})
DELETE r

Performance
Index Usage

Always create indexes on properties used in MATCH/WHERE lookups.

-- Property index (most common)
CREATE INDEX customer_id FOR (c:Customer) ON (c.customerId)

-- Composite index
CREATE INDEX account_lookup FOR (a:Account) ON (a.accountNumber, a.status)

-- Text index for CONTAINS/STARTS WITH
CREATE TEXT INDEX email_text FOR (e:Email) ON (e.address)

-- Verify indexes
SHOW INDEXES

EXPLAIN and PROFILE
-- EXPLAIN: shows plan without executing
EXPLAIN MATCH (c:Customer {customerId: '123'})-[:HAS_ACCOUNT]->(a:Account) RETURN c, a

-- PROFILE: executes and shows actual rows/db hits per operator
PROFILE MATCH (c:Customer {customerId: '123'})-[:HAS_ACCOUNT]->(a:Account) RETURN c, a


Look for:

NodeByLabelScan → missing index, add one
CartesianProduct → unconnected MATCH clauses, connect them or use WITH
Eager → query plan can't stream, may cause memory issues on large datasets
High db hits relative to result rows → inefficient traversal
Parameterized Queries

Always use parameters ($param) instead of string interpolation. This enables query plan caching and prevents injection.

-- Good
MATCH (c:Customer {customerId: $customerId}) RETURN c

-- Bad — no plan cache, injection risk
MATCH (c:Customer {customerId: '${userInput}'}) RETURN c

Avoiding Cartesian Products
-- BAD: two unconnected MATCH clauses = cartesian product
MATCH (a:Account)
MATCH (b:Bank)
RETURN a, b  -- rows = |accounts| × |banks|

-- GOOD: connect through relationships
MATCH (a:Account)-[:PERFORM]->(tx:Transaction)-[:BENEFITS_TO]->(b:Bank)
RETURN a, tx, b

-- GOOD: if truly independent, use UNION or separate queries

Limit Early, Filter Early
-- Push WHERE as early as possible
MATCH (c:Customer)
WHERE c.nationality = $country    -- filter before traversal
MATCH (c)-[:HAS_ACCOUNT]->(a:Account)-[:PERFORM]->(tx:Transaction)
WHERE tx.amount > $threshold
RETURN c, a, tx

Fraud-Domain Patterns
Shared PII Detection (Synthetic Identity)
MATCH (c1:Customer)-[:HAS_EMAIL|HAS_PHONE|HAS_SSN]->(pii)<-[:HAS_EMAIL|HAS_PHONE|HAS_SSN]-(c2:Customer)
WHERE c1 <> c2
WITH c1, c2, collect(pii) AS sharedPII, count(pii) AS sharedCount
WHERE sharedCount >= 2
RETURN c1.customerId, c2.customerId, sharedCount,
       [p IN sharedPII | labels(p)[0]] AS sharedTypes

Transaction Ring Detection
-- Circular fund flow (Neo4j 5.9+ quantified path patterns)
MATCH path = (a:Account)-[:PERFORM]->(first_tx)
  ((tx_i)-[:BENEFITS_TO]->(a_i)-[:PERFORM]->(tx_j)
   WHERE tx_i.date < tx_j.date)*
  (last_tx)-[:BENEFITS_TO]->(a)
WHERE size(apoc.coll.toSet([a] + a_i)) = size([a] + a_i)
RETURN path

Fund Flow / Money Trail
-- Trace where money went from a specific account
MATCH (source:Account {accountNumber: $accNum})
MATCH path = (source)-[:PERFORM]->(tx:Transaction)-[:BENEFITS_TO]->(dest)
RETURN dest, tx.amount, tx.date, labels(dest)[0] AS destType
ORDER BY tx.date DESC

Network Expansion (1-hop, 2-hop)
-- All entities within 2 hops of a customer
MATCH path = (c:Customer {customerId: $customerId})-[*1..2]-(connected)
RETURN path

Community Detection (with GDS)
-- Project graph
CALL gds.graph.project('fraud-network', 'Customer',
  {LINKED: {type: 'LINKED', orientation: 'UNDIRECTED'}})

-- Run Weakly Connected Components
CALL gds.wcc.stream('fraud-network')
YIELD nodeId, componentId
WITH componentId, collect(gds.util.asNode(nodeId).customerId) AS members
WHERE size(members) > 1
RETURN componentId, members, size(members) AS clusterSize
ORDER BY clusterSize DESC

-- Clean up projection
CALL gds.graph.drop('fraud-network')

Centrality (PageRank / Betweenness)
CALL gds.pageRank.stream('fraud-network')
YIELD nodeId, score
RETURN gds.util.asNode(nodeId).customerId AS customerId, score
ORDER BY score DESC
LIMIT 20

Neo4j 5+ Features
Element IDs (replaces internal integer IDs)
-- Neo4j 5+: use elementId() instead of id()
MATCH (n:Customer)
WHERE elementId(n) = $elementId
RETURN n

-- In Bloom scene actions
MATCH (n) WHERE elementId(n) IN $nodes RETURN n

Quantified Path Patterns (5.9+)
-- Match paths of variable length with inline predicates
MATCH path = (a:Account)
  (()-[:PERFORM]->(tx:Transaction)-[:BENEFITS_TO]->()
   WHERE tx.amount > 1000){2,5}
  (b:Account)
RETURN path

Temporal Types
-- datetime(), date(), time(), duration()
CREATE (tx:Transaction {
  timestamp: datetime(),
  settlementDate: date('2024-03-15'),
  processingTime: duration('PT2H30M')
})

-- Filtering by date range
MATCH (tx:Transaction)
WHERE tx.timestamp >= datetime($startDate)
  AND tx.timestamp <= datetime($endDate)
RETURN tx

-- Date arithmetic
MATCH (tx:Transaction)
WHERE tx.timestamp >= datetime() - duration({days: 30})
RETURN tx

COUNT {} and EXISTS {} Subqueries
-- Count subquery (Neo4j 5+)
MATCH (c:Customer)
WHERE COUNT {
  (c)-[:HAS_ACCOUNT]->(a:Account)-[:PERFORM]->(tx:Transaction)
  WHERE tx.amount > 10000
} > 5
RETURN c

-- EXISTS subquery
MATCH (c:Customer)
WHERE EXISTS {
  (c)-[:HAS_EMAIL]->(e:Email)<-[:HAS_EMAIL]-(other:Customer)
  WHERE c <> other
}
RETURN c

Anti-Patterns
1. Collecting without DISTINCT

When multiple OPTIONAL MATCH clauses create cartesian products between collected lists:

-- BAD: emails × phones duplicates
MATCH (c:Customer)
OPTIONAL MATCH (c)-[:HAS_EMAIL]->(e:Email)
OPTIONAL MATCH (c)-[:HAS_PHONE]->(p:Phone)
RETURN c, collect(e) AS emails, collect(p) AS phones

-- GOOD: use DISTINCT
RETURN c, collect(DISTINCT e) AS emails, collect(DISTINCT p) AS phones

2. MERGE on Too Many Properties
-- BAD: if any property differs, creates duplicate
MERGE (c:Customer {customerId: $id, firstName: $first, lastName: $last})

-- GOOD: merge on unique key, set other props
MERGE (c:Customer {customerId: $id})
ON CREATE SET c.firstName = $first, c.lastName = $last

3. Unbounded Variable-Length Paths
-- BAD: can explode on connected graphs
MATCH path = (a)-[*]->(b) RETURN path

-- GOOD: always bound the length
MATCH path = (a)-[*1..5]->(b) RETURN path

4. Using Labels in WHERE Instead of MATCH
-- BAD: scans all nodes then filters
MATCH (n) WHERE 'Customer' IN labels(n) RETURN n

-- GOOD: label in MATCH uses label index
MATCH (n:Customer) RETURN n

5. String Concatenation for Dynamic Queries
-- BAD: no plan caching, injection risk
"MATCH (n {id: '" + userId + "'}) RETURN n"

-- GOOD: use parameters
MATCH (n {id: $userId}) RETURN n

6. Loading Too Much Data
-- BAD: returns everything
MATCH (n) RETURN n

-- GOOD: limit and paginate
MATCH (n:Customer)
RETURN n
ORDER BY n.customerId
SKIP $offset
LIMIT $pageSize

Weekly Installs
13
Repository
michaelkeevildo…s-skills
GitHub Stars
1
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass