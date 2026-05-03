---
title: etl pipeline
url: https://skills.sh/claude-office-skills/skills/etl-pipeline
---

# etl pipeline

skills/claude-office-skills/skills/ETL Pipeline
ETL Pipeline
Installation
$ npx skills add https://github.com/claude-office-skills/skills --skill 'ETL Pipeline'
SKILL.md
ETL Pipeline

Comprehensive skill for designing and automating Extract, Transform, Load data pipelines.

Pipeline Architecture
Core ETL Flow
DATA PIPELINE ARCHITECTURE:
┌─────────────────────────────────────────────────────────┐
│                     EXTRACT                              │
├─────────┬─────────┬─────────┬─────────┬─────────────────┤
│ Postgres│  MySQL  │ MongoDB │  APIs   │  Files (CSV/JSON)│
└────┬────┴────┬────┴────┬────┴────┬────┴────────┬────────┘
     │         │         │         │              │
     └─────────┴─────────┴────┬────┴──────────────┘
                              ▼
┌─────────────────────────────────────────────────────────┐
│                    TRANSFORM                             │
│  • Clean & Validate    • Aggregate & Join               │
│  • Normalize           • Calculate Metrics              │
│  • Deduplicate         • Apply Business Rules           │
└────────────────────────┬────────────────────────────────┘
                         ▼
┌─────────────────────────────────────────────────────────┐
│                      LOAD                                │
├─────────────┬─────────────┬─────────────┬───────────────┤
│  BigQuery   │  Snowflake  │  Redshift   │  Data Lake    │
└─────────────┴─────────────┴─────────────┴───────────────┘

Source Connectors
Database Connections
sources:
  postgres:
    type: postgresql
    host: db.example.com
    port: 5432
    database: production
    ssl: true
    extraction:
      method: incremental
      key: updated_at
      batch_size: 10000

  mysql:
    type: mysql
    host: mysql.example.com
    port: 3306
    database: analytics
    extraction:
      method: cdc
      binlog: true

  mongodb:
    type: mongodb
    connection_string: mongodb+srv://...
    database: app_data
    extraction:
      method: change_streams

API Sources
api_sources:
  stripe:
    type: rest_api
    base_url: https://api.stripe.com/v1
    auth: bearer_token
    endpoints:
      - /charges
      - /customers
      - /subscriptions
    pagination: cursor
    rate_limit: 100/second

  salesforce:
    type: salesforce
    instance_url: https://company.salesforce.com
    auth: oauth2
    objects:
      - Account
      - Opportunity
      - Contact
    bulk_api: true

Transformation Layer
Common Transformations
# Data Cleaning
transformations = {
    "clean_nulls": {
        "operation": "fill_null",
        "columns": ["email", "phone"],
        "value": "unknown"
    },
    
    "standardize_dates": {
        "operation": "date_parse",
        "columns": ["created_at", "updated_at"],
        "format": "ISO8601"
    },
    
    "normalize_currency": {
        "operation": "convert_currency",
        "source_column": "amount",
        "currency_column": "currency",
        "target": "USD"
    },
    
    "deduplicate": {
        "operation": "distinct",
        "key_columns": ["customer_id", "transaction_id"],
        "keep": "latest"
    }
}

Aggregation Rules
-- Daily Revenue Aggregation
SELECT 
    DATE(created_at) as date,
    product_category,
    COUNT(*) as transactions,
    SUM(amount) as total_revenue,
    AVG(amount) as avg_order_value,
    COUNT(DISTINCT customer_id) as unique_customers
FROM orders
WHERE created_at >= '${start_date}'
GROUP BY 1, 2

Join Operations
joins:
  - name: enrich_orders
    left: orders
    right: customers
    type: left
    on:
      - left: customer_id
        right: id
    select:
      - orders.*
      - customers.email
      - customers.segment
      - customers.lifetime_value

  - name: add_product_details
    left: enriched_orders
    right: products
    type: left
    on:
      - left: product_id
        right: id

Load Strategies
BigQuery Load
bigquery_load:
  project: my-project
  dataset: analytics
  table: fact_orders
  
  schema:
    - name: order_id
      type: STRING
      mode: REQUIRED
    - name: customer_id
      type: STRING
    - name: amount
      type: NUMERIC
    - name: created_at
      type: TIMESTAMP
  
  load_config:
    write_disposition: WRITE_APPEND
    create_disposition: CREATE_IF_NEEDED
    clustering_fields: [customer_id]
    time_partitioning:
      field: created_at
      type: DAY

Snowflake Load
snowflake_load:
  warehouse: ETL_WH
  database: ANALYTICS
  schema: PUBLIC
  table: FACT_ORDERS
  
  staging:
    stage: '@MY_STAGE'
    file_format: JSON
  
  copy_options:
    on_error: CONTINUE
    purge: true
    match_by_column_name: CASE_INSENSITIVE

Pipeline Orchestration
DAG Definition
pipeline:
  name: daily_analytics_etl
  schedule: "0 2 * * *"  # 2 AM daily
  
  tasks:
    - id: extract_orders
      type: extract
      source: postgres
      query: "SELECT * FROM orders WHERE date = '${execution_date}'"
      
    - id: extract_customers
      type: extract
      source: postgres
      query: "SELECT * FROM customers"
      
    - id: transform_data
      type: transform
      dependencies: [extract_orders, extract_customers]
      operations:
        - join_customers
        - calculate_metrics
        - apply_business_rules
      
    - id: load_warehouse
      type: load
      dependencies: [transform_data]
      target: bigquery
      table: fact_orders
      
    - id: notify_complete
      type: notification
      dependencies: [load_warehouse]
      channel: slack
      message: "Daily ETL completed successfully"

Error Handling
error_handling:
  retry:
    max_attempts: 3
    delay_seconds: 300
    exponential_backoff: true
  
  on_failure:
    - log_error
    - send_alert
    - save_failed_records
  
  dead_letter:
    enabled: true
    destination: s3://etl-errors/
    retention_days: 30

Data Quality
Validation Rules
quality_checks:
  - name: null_check
    column: customer_id
    rule: not_null
    severity: error
    
  - name: range_check
    column: amount
    rule: between
    min: 0
    max: 100000
    severity: warning
    
  - name: uniqueness
    columns: [order_id]
    rule: unique
    severity: error
    
  - name: referential_integrity
    column: product_id
    reference_table: products
    reference_column: id
    severity: error
    
  - name: freshness
    column: updated_at
    rule: max_age_hours
    value: 24
    severity: warning

Quality Metrics Dashboard
DATA QUALITY REPORT - ${date}
═══════════════════════════════════════
Total Records Processed: 1,250,000
Passed Validation:       1,247,500 (99.8%)
Failed Validation:           2,500 (0.2%)

ISSUES BY TYPE:
┌─────────────────┬────────┬──────────┐
│ Issue Type      │ Count  │ Severity │
├─────────────────┼────────┼──────────┤
│ Null values     │ 1,200  │ Warning  │
│ Invalid format  │   850  │ Error    │
│ Out of range    │   300  │ Warning  │
│ Duplicates      │   150  │ Error    │
└─────────────────┴────────┴──────────┘

Monitoring & Alerting
Pipeline Metrics
metrics:
  - name: pipeline_duration
    type: gauge
    labels: [pipeline_name, status]
    
  - name: records_processed
    type: counter
    labels: [pipeline_name, source, destination]
    
  - name: error_count
    type: counter
    labels: [pipeline_name, error_type]
    
  - name: data_freshness
    type: gauge
    labels: [table_name]

Alert Configuration
alerts:
  - name: pipeline_failed
    condition: status == 'failed'
    channels: [pagerduty, slack]
    
  - name: high_error_rate
    condition: error_rate > 0.05
    channels: [slack]
    
  - name: slow_pipeline
    condition: duration > 2 * avg_duration
    channels: [slack]
    
  - name: data_freshness
    condition: freshness_hours > 24
    channels: [email]

Best Practices
Incremental Loading: Use incremental extraction when possible
Idempotency: Ensure pipelines can be re-run safely
Partitioning: Partition large tables by date
Monitoring: Track pipeline health metrics
Documentation: Document all transformations
Testing: Test with sample data before production
Version Control: Track pipeline changes in git
Weekly Installs
–
Repository
claude-office-s…s/skills
GitHub Stars
94
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn