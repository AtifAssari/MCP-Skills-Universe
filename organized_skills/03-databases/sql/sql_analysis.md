---
rating: ⭐⭐
title: sql analysis
url: https://skills.sh/danhvb/my-ba-skills/sql-analysis
---

# sql analysis

skills/danhvb/my-ba-skills/SQL Analysis
SQL Analysis
Installation
$ npx skills add https://github.com/danhvb/my-ba-skills --skill 'SQL Analysis'
SKILL.md
SQL Analysis Skill
Purpose

Enable BAs to validate data requirements, understand current data states, and perform independent data analysis without relying solely on developers.

When to Use
Validating migration data.
Understanding current data structures (As-Is).
Troubleshooting user issues ("Why can't I see this order?").
Generating ad-hoc reports for stakeholders.
Core SQL Concepts for BAs
1. The SELECT Statement
SELECT column1, column2   -- What do you want?
FROM table_name           -- From where?
WHERE condition           -- Filter logic
ORDER BY column1 DESC;    -- Sorting

2. Filtering (WHERE)
WHERE status = 'Active' (Exact match)
WHERE quantity > 10 (Comparison)
WHERE name LIKE 'Smith%' (Partial match)
WHERE status IN ('New', 'Open') (List)
WHERE end_date IS NULL (Finding missing data)
3. Aggregation (GROUP BY)

Summarizing data.

SELECT status, COUNT(*) as total_orders
FROM orders
GROUP BY status;

4. Joining Tables (JOIN)

Connecting related data.

INNER JOIN: Only matching records (A ∩ B). "Show me customers who have orders."
LEFT JOIN: All from Left, matches from Right (A + A∩B). "Show me ALL customers, and their orders if any." (Good for finding customers with NO orders).
Common Analysis Queries
Data Quality Check

"Are there any duplicate customers by email?"

SELECT email, COUNT(*)
FROM customers
GROUP BY email
HAVING COUNT(*) > 1;


"Are there orders without a valid user?"

SELECT o.order_id
FROM orders o
LEFT JOIN users u ON o.user_id = u.id
WHERE u.id IS NULL;

Process Analysis

"How long does it take to ship an order?"

SELECT 
    AVG(DATEDIFF(day, order_date, shipped_date)) as avg_days_to_ship,
    MAX(DATEDIFF(day, order_date, shipped_date)) as max_days
FROM orders
WHERE shipped_date IS NOT NULL;

Integration Spec Validation

"What are the distinct values for 'Payment Method' so we can map them?"

SELECT DISTINCT payment_method
FROM transactions;

Best Practices
Read-Only Access: Ensure you only have SELECT permissions (ro-user).
Limit Results: Always use LIMIT 10 (or TOP 10) when exploring new tables.
No Production Performance Impact: Avoid running heavy queries (e.g., Joining 5 huge tables) during peak hours.
Understand NULLs: COUNT(column) ignores NULLs; COUNT(*) counts everything.
Tools
DBeaver: Universal DB Tool.
Metabase / Redash: Visual SQL Builders.
Lark Base: Can import CSV results for sharing.
Weekly Installs
–
Repository
danhvb/my-ba-skills
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass