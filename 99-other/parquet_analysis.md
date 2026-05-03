---
title: parquet-analysis
url: https://skills.sh/brojonat/llmsrules/parquet-analysis
---

# parquet-analysis

skills/brojonat/llmsrules/parquet-analysis
parquet-analysis
Installation
$ npx skills add https://github.com/brojonat/llmsrules --skill parquet-analysis
SKILL.md
Parquet Analysis with Python and Ibis

Analyze parquet files using Ibis, a database-agnostic Python DataFrame API. Ibis translates Python operations into optimized queries for the underlying backend (DuckDB by default for parquet files).

Quick Start
Basic workflow
import ibis

# Connect to DuckDB (optimized for parquet)
con = ibis.duckdb.connect()

# Read parquet file
table = con.read_parquet("data.parquet")

# Explore
print(table.schema())      # View schema
print(table.head(10))      # Preview data
print(table.describe())    # Summary statistics

# Filter and aggregate
summary = (
    table
    .filter(table.amount > 100)
    .group_by("category")
    .aggregate(
        total=table.amount.sum(),
        avg=table.amount.mean(),
        count=table.count()
    )
)
print(summary.execute())

# Export
con.to_parquet(summary, "output.parquet")

Core Operations
Select and filter
# Select columns
selected = table.select("id", "amount", "date")

# Filter rows
filtered = table.filter(
    (table.amount > 100) &
    (table.date >= "2024-01-01")
)

# Sort
sorted_data = table.order_by(table.amount.desc())

Transform
# Add computed columns
enriched = table.mutate(
    revenue=table.quantity * table.unit_price,
    year=table.date.year(),
    size=ibis.case()
        .when(table.amount < 100, "small")
        .when(table.amount < 1000, "medium")
        .else_("large")
        .end()
)

Aggregate
# Group by and summarize
by_category = (
    table.group_by("category")
    .aggregate(
        total=table.amount.sum(),
        avg=table.amount.mean(),
        count=table.count()
    )
)

Join
# Read and join multiple files
customers = con.read_parquet("customers.parquet")
orders = con.read_parquet("orders.parquet")

joined = (
    orders
    .join(customers, orders.customer_id == customers.id, how="left")
    .select(
        orders.order_id,
        orders.amount,
        customers.name
    )
)

Export
# To parquet
con.to_parquet(result, "output.parquet")

# To CSV (via pandas)
df = result.execute()
df.to_csv("output.csv", index=False)

Common Patterns
Data quality checks
# Row count
row_count = table.count().execute()

# Check for nulls
null_counts = table.select([
    col.isnull().sum().name(f"{col}_nulls")
    for col in table.columns
]).execute()

# Value distribution
table.group_by("category").aggregate(count=table.count()).execute()

Time-based analysis
# Monthly aggregation
monthly = (
    table.mutate(month=table.date.truncate("M"))
    .group_by("month")
    .aggregate(total=table.amount.sum())
    .order_by("month")
)

# Extract date components
dated = table.mutate(
    year=table.date.year(),
    month=table.date.month(),
    quarter=table.date.quarter()
)

Window functions
# Rank within groups
ranked = table.mutate(
    rank=table.amount.rank().over(
        ibis.window(group_by="category", order_by=table.amount.desc())
    )
)

# Running total
with_cumsum = table.mutate(
    cumulative=table.amount.sum().over(
        ibis.window(order_by="date", rows=(None, 0))
    )
)

Best Practices
Filter early: Apply filters before aggregations to reduce data volume
Use lazy evaluation: Ibis operations don't execute until .execute() is called - chain operations before executing
Handle nulls: Check for and handle null values explicitly
Leverage selectors for column operations (see REFERENCE.md)
Detailed Resources
EXAMPLES.md - Complete examples for all common tasks
REFERENCE.md - Detailed API reference for Ibis operations
scripts/analyze.py - Complete working example script
scripts/template.py - Quick-start template for your analyses
../ibis-data/SKILL.md - Additional Ibis context and patterns
Scripts
Complete analysis workflow

Run the full example script:

python scripts/analyze.py


This demonstrates:

Data exploration and quality checks
Transformations and enrichment
Aggregations and filtering
Joins (if multiple files available)
Multiple export formats
Optional visualization
Quick-start template

Copy and customize the template:

cp scripts/template.py my_analysis.py
# Edit with your file paths and logic
python my_analysis.py

Installation

Install required packages:

uv add "ibis-framework[duckdb]"

# Optional for visualization
uv add matplotlib

Troubleshooting

Import error: Ensure ibis-framework[duckdb] is installed

Large files: DuckDB handles large parquet files efficiently. For very large datasets:

Filter early and aggressively
Use selective column reading: con.read_parquet("file.parquet", columns=["id", "amount"])
Process in chunks or use more selective queries

Schema mismatches in joins: Ensure column types match using .cast():

table = table.mutate(id=table.id.cast("int64"))


Performance: For complex queries, check the generated SQL with ibis.to_sql(table) to understand what's being executed

Weekly Installs
12
Repository
brojonat/llmsrules
First Seen
6 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass