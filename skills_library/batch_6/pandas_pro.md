---
title: pandas-pro
url: https://skills.sh/jeffallan/claude-skills/pandas-pro
---

# pandas-pro

skills/jeffallan/claude-skills/pandas-pro
pandas-pro
Installation
$ npx skills add https://github.com/jeffallan/claude-skills --skill pandas-pro
Summary

Expert pandas data manipulation with vectorized operations, memory optimization, and production-grade validation patterns.

Covers core workflows: data assessment, transformation design, efficient implementation, result validation, and memory profiling
Includes reference guides and code patterns for DataFrame operations, data cleaning, aggregation, merging, and time series resampling
Enforces vectorized operations over iteration, proper indexing with .loc[]/.iloc[], and explicit missing value handling
Provides memory optimization techniques including categorical type conversion, numeric downcasting, and chunking strategies for large datasets
SKILL.md
Pandas Pro

Expert pandas developer specializing in efficient data manipulation, analysis, and transformation workflows with production-grade performance patterns.

Core Workflow
Assess data structure — Examine dtypes, memory usage, missing values, data quality:
print(df.dtypes)
print(df.memory_usage(deep=True).sum() / 1e6, "MB")
print(df.isna().sum())
print(df.describe(include="all"))

Design transformation — Plan vectorized operations, avoid loops, identify indexing strategy
Implement efficiently — Use vectorized methods, method chaining, proper indexing
Validate results — Check dtypes, shapes, null counts, and row counts:
assert result.shape[0] == expected_rows, f"Row count mismatch: {result.shape[0]}"
assert result.isna().sum().sum() == 0, "Unexpected nulls after transform"
assert set(result.columns) == expected_cols

Optimize — Profile memory, apply categorical types, use chunking if needed
Reference Guide

Load detailed guidance based on context:

Topic	Reference	Load When
DataFrame Operations	references/dataframe-operations.md	Indexing, selection, filtering, sorting
Data Cleaning	references/data-cleaning.md	Missing values, duplicates, type conversion
Aggregation & GroupBy	references/aggregation-groupby.md	GroupBy, pivot, crosstab, aggregation
Merging & Joining	references/merging-joining.md	Merge, join, concat, combine strategies
Performance Optimization	references/performance-optimization.md	Memory usage, vectorization, chunking
Code Patterns
Vectorized Operations (before/after)
# ❌ AVOID: row-by-row iteration
for i, row in df.iterrows():
    df.at[i, 'tax'] = row['price'] * 0.2

# ✅ USE: vectorized assignment
df['tax'] = df['price'] * 0.2

Safe Subsetting with .copy()
# ❌ AVOID: chained indexing triggers SettingWithCopyWarning
df['A']['B'] = 1

# ✅ USE: .loc[] with explicit copy when mutating a subset
subset = df.loc[df['status'] == 'active', :].copy()
subset['score'] = subset['score'].fillna(0)

GroupBy Aggregation
summary = (
    df.groupby(['region', 'category'], observed=True)
    .agg(
        total_sales=('revenue', 'sum'),
        avg_price=('price', 'mean'),
        order_count=('order_id', 'nunique'),
    )
    .reset_index()
)

Merge with Validation
merged = pd.merge(
    left_df, right_df,
    on=['customer_id', 'date'],
    how='left',
    validate='m:1',          # asserts right key is unique
    indicator=True,
)
unmatched = merged[merged['_merge'] != 'both']
print(f"Unmatched rows: {len(unmatched)}")
merged.drop(columns=['_merge'], inplace=True)

Missing Value Handling
# Forward-fill then interpolate numeric gaps
df['price'] = df['price'].ffill().interpolate(method='linear')

# Fill categoricals with mode, numerics with median
for col in df.select_dtypes(include='object'):
    df[col] = df[col].fillna(df[col].mode()[0])
for col in df.select_dtypes(include='number'):
    df[col] = df[col].fillna(df[col].median())

Time Series Resampling
daily = (
    df.set_index('timestamp')
    .resample('D')
    .agg({'revenue': 'sum', 'sessions': 'count'})
    .fillna(0)
)

Pivot Table
pivot = df.pivot_table(
    values='revenue',
    index='region',
    columns='product_line',
    aggfunc='sum',
    fill_value=0,
    margins=True,
)

Memory Optimization
# Downcast numerics and convert low-cardinality strings to categorical
df['category'] = df['category'].astype('category')
df['count'] = pd.to_numeric(df['count'], downcast='integer')
df['score'] = pd.to_numeric(df['score'], downcast='float')
print(df.memory_usage(deep=True).sum() / 1e6, "MB after optimization")

Constraints
MUST DO
Use vectorized operations instead of loops
Set appropriate dtypes (categorical for low-cardinality strings)
Check memory usage with .memory_usage(deep=True)
Handle missing values explicitly (don't silently drop)
Use method chaining for readability
Preserve index integrity through operations
Validate data quality before and after transformations
Use .copy() when modifying subsets to avoid SettingWithCopyWarning
MUST NOT DO
Iterate over DataFrame rows with .iterrows() unless absolutely necessary
Use chained indexing (df['A']['B']) — use .loc[] or .iloc[]
Ignore SettingWithCopyWarning messages
Load entire large datasets without chunking
Use deprecated methods (.ix, .append() — use pd.concat())
Convert to Python lists for operations possible in pandas
Assume data is clean without validation
Output Templates

When implementing pandas solutions, provide:

Code with vectorized operations and proper indexing
Comments explaining complex transformations
Memory/performance considerations if dataset is large
Data validation checks (dtypes, nulls, shapes)

Documentation

Weekly Installs
2.2K
Repository
jeffallan/claude-skills
GitHub Stars
8.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass