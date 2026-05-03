---
rating: ⭐⭐
title: neo4j-cypher-guide
url: https://skills.sh/tomasonjo/blogs/neo4j-cypher-guide
---

# neo4j-cypher-guide

skills/tomasonjo/blogs/neo4j-cypher-guide
neo4j-cypher-guide
Installation
$ npx skills add https://github.com/tomasonjo/blogs --skill neo4j-cypher-guide
SKILL.md
Neo4j Modern Cypher Query Guide

This skill helps generate Neo4j Cypher read queries using modern syntax patterns and avoiding deprecated features. It focuses on efficient query patterns for graph traversal and data retrieval.

Quick Compatibility Check

When generating Cypher queries, immediately avoid these REMOVED features:

❌ id() function → Use elementId()
❌ Implicit grouping keys → Use explicit WITH clauses
❌ Pattern expressions for lists → Use pattern comprehension or COLLECT subqueries
❌ Repeated relationship variables → Use unique variable names
❌ Automatic list to boolean coercion → Use explicit checks
Core Principles for Query Generation
Use modern syntax patterns - QPP for complex traversals, CALL subqueries for complex reads
Optimize during traversal - Filter early within patterns, not after expansion
Always filter nulls when sorting - Add IS NOT NULL checks for sorted properties
Explicit is better than implicit - Always use explicit grouping and type checking
Critical Sorting Rule

ALWAYS filter NULL values when sorting:

// WRONG - May include null values
MATCH (n:Node)
RETURN n.name, n.value
ORDER BY n.value

// CORRECT - Filter nulls before sorting
MATCH (n:Node)
WHERE n.value IS NOT NULL
RETURN n.name, n.value
ORDER BY n.value

Query Pattern Selection Guide
For Simple Queries

Use standard Cypher patterns with modern syntax:

MATCH (n:Label {property: value})
WHERE n.otherProperty IS :: STRING
RETURN n

For Variable-Length Paths

Consider Quantified Path Patterns (QPP) for better performance:

// Instead of: MATCH (a)-[*1..5]->(b)
// Use: MATCH (a)-[]-{1,5}(b)

// With filtering:
MATCH (a)((n WHERE n.active)-[]->(m)){1,5}(b)

For Aggregations

Use COUNT{}, EXISTS{}, and COLLECT{} subqueries:

MATCH (p:Person)
WHERE count{(p)-[:KNOWS]->()} > 5
RETURN p.name, 
       exists{(p)-[:MANAGES]->()} AS isManager

For Complex Read Operations

Use CALL subqueries for sophisticated data retrieval:

MATCH (d:Department)
CALL (d) {
  MATCH (d)<-[:WORKS_IN]-(p:Person)
  WHERE p.salary IS NOT NULL  // Filter nulls
  WITH p ORDER BY p.salary DESC
  LIMIT 3
  RETURN collect(p.name) AS topEarners
}
RETURN d.name, topEarners

Common Query Transformations
Counting Patterns
// Old: RETURN size((n)-[]->())
// Modern: RETURN count{(n)-[]->()}

Checking Existence
// Old: WHERE exists((n)-[:REL]->())
// Modern: WHERE EXISTS {MATCH (n)-[:REL]->()}
// Also valid: WHERE exists{(n)-[:REL]->()}

Element IDs
// Old: WHERE id(n) = 123
// Modern: WHERE elementId(n) = "4:abc123:456"
// Note: elementId returns a string, not integer

Sorting with Null Handling
// Always add null check
MATCH (n:Node)
WHERE n.sortProperty IS NOT NULL
RETURN n
ORDER BY n.sortProperty

// Or use NULLS LAST
MATCH (n:Node)
RETURN n
ORDER BY n.sortProperty NULLS LAST

When to Load Reference Documentation

Load the appropriate reference file when:

references/deprecated-syntax.md
Migrating queries from older Neo4j versions
Encountering syntax errors with legacy queries
Need complete list of removed/deprecated features
references/subqueries.md
Working with CALL subqueries for reads
Using COLLECT or COUNT subqueries
Handling complex aggregations
Implementing sorting with null filtering
references/qpp.md
Optimizing variable-length path queries
Need early filtering during traversal
Working with paths longer than 3-4 hops
Complex pattern matching requirements
Query Generation Checklist

Before finalizing any generated query:

✅ No deprecated functions (id, btree indexes, etc.)
✅ Explicit grouping for aggregations
✅ NULL filters for all sorted properties
✅ Appropriate subquery patterns for reads
✅ Consider QPP for paths with filtering needs
✅ Use COUNT{} instead of size() for pattern counting
✅ Variable scope clauses in CALL subqueries
✅ Unique variable names for relationships
Error Resolution Patterns
"Implicit grouping key" errors
// Problem: RETURN n.prop, count(*) + n.other
// Solution: WITH n.prop AS prop, n.other AS other, count(*) AS cnt
//          RETURN prop, cnt + other

"id() function not found"
// Use elementId() but note it returns a string, not integer

"Repeated variable" errors
// Problem: MATCH (a)-[r*]->(), (b)-[r*]->()
// Solution: MATCH (a)-[r1*]->(), (b)-[r2*]->()

Performance Tips
Start with indexed properties - Always anchor patterns with indexed lookups
Filter early in QPP - Apply WHERE clauses within the pattern
Filter nulls before sorting - Prevent unexpected results and improve performance
Limit expansion depth - Use reasonable upper bounds in quantifiers
Use EXISTS for existence checks - More efficient than counting
Profile queries - Use PROFILE to identify bottlenecks
Modern Cypher Features
Label Expressions
WHERE n:Label1|Label2  // OR
WHERE n:Label1&Label2  // AND
WHERE n:!Archived      // NOT

Type Predicates
WHERE n.prop IS :: STRING
WHERE n.value IS :: INTEGER NOT NULL
WHERE n.data IS :: LIST<STRING>

Subquery Patterns for Reads
COUNT{} - Count patterns efficiently
EXISTS{} - Check pattern existence
COLLECT{} - Collect complex results
CALL{} - Execute subqueries for complex reads
Quantified Path Patterns
Inline filtering during traversal
Access to nodes and relationships in patterns
Significant performance improvements (up to 1000x)
Support for complex, multi-hop patterns

Always prefer modern syntax patterns for better performance and maintainability.

Weekly Installs
138
Repository
tomasonjo/blogs
GitHub Stars
1.6K
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass