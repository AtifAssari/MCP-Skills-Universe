---
rating: ⭐⭐⭐
title: loki
url: https://skills.sh/julianobarbosa/claude-code-skills/loki
---

# loki

skills/julianobarbosa/claude-code-skills/loki
loki
Installation
$ npx skills add https://github.com/julianobarbosa/claude-code-skills --skill loki
SKILL.md
Grafana Loki Skill

Comprehensive guide for Grafana Loki - the cost-effective, horizontally-scalable log aggregation system inspired by Prometheus.

What is Loki?

Loki is a horizontally-scalable, highly-available, multi-tenant log aggregation system that:

Indexes only metadata (labels) - Not full log content like traditional systems
Stores compressed chunks in affordable object storage (S3, GCS, Azure Blob)
Uses Prometheus-style labels for organizing log streams
Multi-tenant by default with built-in tenant isolation
Cost-efficient - Dramatically smaller index and lower operational costs
Architecture Overview
Core Components
Component	Purpose
Distributor	Validates requests, preprocesses labels, routes to ingesters
Ingester	Buffers logs in memory, compresses into chunks, writes to storage
Querier	Executes LogQL queries from ingesters and storage
Query Frontend	Accelerates queries via splitting, caching, scheduling
Query Scheduler	Manages per-tenant query queues for fairness
Index Gateway	Serves index queries for TSDB stores
Compactor	Merges index files, manages retention, handles deletion
Ruler	Evaluates alerting and recording rules
Data Flow

Write Path:

Log Source → Distributor → Ingester → Object Storage
                                    ↓
                              Chunks + Indexes


Read Path:

Query → Query Frontend → Query Scheduler → Querier
                                             ↓
                                    Ingesters + Storage

Deployment Modes
1. Monolithic Mode (-target=all)
All components in single process
Best for: Initial experimentation, small-scale (~20GB logs/day)
Simplest approach
2. Simple Scalable Deployment (SSD) - Recommended Default
deploymentMode: SimpleScalable

write:
  replicas: 3   # Distributor + Ingester

read:
  replicas: 2   # Query Frontend + Querier

backend:
  replicas: 2   # Compactor + Index Gateway + Query Scheduler + Ruler

3. Microservices Mode (Distributed)
deploymentMode: Distributed

ingester:
  replicas: 3
  zoneAwareReplication:
    enabled: true

distributor:
  replicas: 3

querier:
  replicas: 3

queryFrontend:
  replicas: 2

queryScheduler:
  replicas: 2

compactor:
  replicas: 1

indexGateway:
  replicas: 2

Schema Configuration

Recommended: TSDB with Schema v13

loki:
  schemaConfig:
    configs:
      - from: "2024-04-01"
        store: tsdb
        object_store: azure  # or s3, gcs
        schema: v13
        index:
          prefix: loki_index_
          period: 24h

Storage Configuration
Azure Blob Storage (Recommended for Azure)
loki:
  storage:
    type: azure
    bucketNames:
      chunks: loki-chunks
      ruler: loki-ruler
      admin: loki-admin
    azure:
      accountName: <storage-account-name>
      # Option 1: User-Assigned Managed Identity (Recommended)
      useManagedIdentity: true
      useFederatedToken: false
      userAssignedId: <identity-client-id>
      # Option 2: Account Key (Dev only)
      # accountKey: <account-key>
      requestTimeout: 30s

AWS S3
loki:
  storage:
    type: s3
    bucketNames:
      chunks: my-loki-chunks-2024
      ruler: my-loki-ruler-2024
      admin: my-loki-admin-2024
    s3:
      endpoint: s3.us-east-1.amazonaws.com
      region: us-east-1
      # Use IAM roles or access keys
      accessKeyId: <access-key>
      secretAccessKey: <secret-key>
      s3ForcePathStyle: false

Google Cloud Storage
loki:
  storage:
    type: gcs
    bucketNames:
      chunks: my-loki-gcs-bucket
    gcs:
      bucketName: my-loki-gcs-bucket
      # Uses Workload Identity or service account

Chunk Configuration Best Practices
loki:
  ingester:
    chunk_encoding: snappy        # Recommended (fast + efficient)
    chunk_target_size: 1572864    # ~1.5MB compressed
    max_chunk_age: 2h             # Max time before flush
    chunk_idle_period: 30m        # Flush idle chunks
    flush_check_period: 30s
    flush_op_timeout: 10m

Setting	Recommended	Purpose
chunk_encoding	snappy	Best speed-to-compression balance
chunk_target_size	1.5MB	Target compressed chunk size
max_chunk_age	2h	Limits memory and data loss exposure
chunk_idle_period	30m	Flushes inactive streams
Limits Configuration
loki:
  limits_config:
    # Retention
    retention_period: 744h              # 31 days

    # Ingestion limits
    ingestion_rate_mb: 50
    ingestion_burst_size_mb: 100
    per_stream_rate_limit: 3MB
    per_stream_rate_limit_burst: 15MB

    # Query limits
    max_query_series: 10000
    max_query_lookback: 720h
    max_entries_limit_per_query: 10000

    # Required for OTLP
    allow_structured_metadata: true
    volume_enabled: true

    # Sample rejection
    reject_old_samples: true
    reject_old_samples_max_age: 168h    # 7 days
    max_label_names_per_series: 25

Compactor Configuration
loki:
  compactor:
    retention_enabled: true
    retention_delete_delay: 2h
    retention_delete_worker_count: 50
    compaction_interval: 10m
    delete_request_store: azure         # Match your storage type

Caching Configuration

Recommended: Separate Memcached instances

# Helm values for Loki caching
memcached:
  # Results cache
  frontend:
    replicas: 3
    memcached:
      maxItemMemory: 1024               # 1GB
      maxItemSize: 5m
      connectionLimit: 1024

  # Chunks cache
  chunks:
    replicas: 3
    memcached:
      maxItemMemory: 4096               # 4GB
      maxItemSize: 2m
      connectionLimit: 1024

# Enable caching in Loki config
loki:
  chunk_store_config:
    chunk_cache_config:
      memcached_client:
        host: loki-memcached-chunks.monitoring.svc
        service: memcached-client

LogQL Query Language
Basic Queries
# Stream selector
{job="api-server"}

# Multiple labels
{job="api-server", env="prod"}

# Label matchers
{namespace=~".*-prod"}           # Regex match
{level!="debug"}                  # Not equal

# Filter expressions
{job="api-server"} |= "error"     # Contains
{job="api-server"} != "debug"     # Not contains
{job="api-server"} |~ "err.*"     # Regex match
{job="api-server"} !~ "debug.*"   # Regex not match

Pipeline Stages
# JSON parsing
{job="api-server"} | json

# Extract specific fields
{job="api-server"} | json | line_format "{{.message}}"

# Label extraction
{job="api-server"} | logfmt | level="error"

# Pattern matching
{job="api-server"} | pattern "<ip> - - [<_>] \"<method> <path>\"" | method="POST"

Metric Queries
# Count logs per minute
count_over_time({job="api-server"}[1m])

# Rate of errors
rate({job="api-server"} |= "error" [5m])

# Bytes rate
bytes_rate({job="api-server"}[5m])

# Sum by label
sum by (namespace) (rate({job="api-server"}[5m]))

# Top 10 by volume
topk(10, sum by (namespace) (bytes_rate({}[5m])))

OpenTelemetry Integration
Native OTLP (Recommended - Loki 3.0+)

OpenTelemetry Collector Config:

exporters:
  otlphttp:
    endpoint: http://loki-gateway:3100/otlp
    headers:
      X-Scope-OrgID: "my-tenant"

service:
  pipelines:
    logs:
      receivers: [otlp]
      exporters: [otlphttp]


Loki Config:

loki:
  limits_config:
    allow_structured_metadata: true    # Required for OTLP


Key Benefits:

Log body stored as plain text (not JSON encoded)
17 default resource attributes auto-indexed
Simpler queries without JSON parsing
Better storage efficiency
Resource Attribute Mapping
OTLP Attribute	Loki Label
service.name	service_name
service.namespace	service_namespace
k8s.pod.name	k8s_pod_name
k8s.namespace.name	k8s_namespace_name
cloud.region	cloud_region
Kubernetes Helm Deployment
Add Repository
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update

Install with Values
helm install loki grafana/loki \
  --namespace monitoring \
  --values values.yaml

Production Values Example
deploymentMode: Distributed

loki:
  auth_enabled: true

  schemaConfig:
    configs:
      - from: "2024-04-01"
        store: tsdb
        object_store: azure
        schema: v13
        index:
          prefix: loki_index_
          period: 24h

  storage:
    type: azure
    azure:
      accountName: mystorageaccount
      useManagedIdentity: true
      userAssignedId: <client-id>
    bucketNames:
      chunks: loki-chunks
      ruler: loki-ruler
      admin: loki-admin

  limits_config:
    retention_period: 2160h             # 90 days
    allow_structured_metadata: true

ingester:
  replicas: 3
  zoneAwareReplication:
    enabled: true
  resources:
    requests:
      cpu: 2
      memory: 8Gi
    limits:
      cpu: 4
      memory: 16Gi

querier:
  replicas: 3
  maxUnavailable: 2

queryFrontend:
  replicas: 2

distributor:
  replicas: 3

compactor:
  replicas: 1

indexGateway:
  replicas: 2
  maxUnavailable: 1

# Gateway for external access
gateway:
  service:
    type: LoadBalancer

# Monitoring
monitoring:
  serviceMonitor:
    enabled: true

Azure Identity Configuration
User-Assigned Managed Identity (Recommended)

1. Create Identity:

az identity create \
  --name loki-identity \
  --resource-group <rg>

IDENTITY_CLIENT_ID=$(az identity show --name loki-identity --resource-group <rg> --query clientId -o tsv)
IDENTITY_PRINCIPAL_ID=$(az identity show --name loki-identity --resource-group <rg> --query principalId -o tsv)


2. Assign to Node Pool:

az vmss identity assign \
  --resource-group <aks-node-rg> \
  --name <vmss-name> \
  --identities /subscriptions/<sub>/resourceGroups/<rg>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/loki-identity


3. Grant Storage Permission:

az role assignment create \
  --role "Storage Blob Data Contributor" \
  --assignee-object-id $IDENTITY_PRINCIPAL_ID \
  --scope /subscriptions/<sub>/resourceGroups/<rg>/providers/Microsoft.Storage/storageAccounts/<storage>


4. Configure Loki:

loki:
  storage:
    azure:
      useManagedIdentity: true
      userAssignedId: <IDENTITY_CLIENT_ID>

Multi-Tenancy
loki:
  auth_enabled: true

# Query with tenant header
curl -H "X-Scope-OrgID: tenant-a" \
  "http://loki:3100/loki/api/v1/query?query={job=\"app\"}"

# Multi-tenant queries (if enabled)
# X-Scope-OrgID: tenant-a|tenant-b

Troubleshooting
Common Issues

1. Container Not Found (Azure)

# Create required containers
az storage container create --name loki-chunks --account-name <storage>
az storage container create --name loki-ruler --account-name <storage>
az storage container create --name loki-admin --account-name <storage>


2. Authorization Failure (Azure)

# Verify RBAC assignment
az role assignment list --scope /subscriptions/<sub>/resourceGroups/<rg>/providers/Microsoft.Storage/storageAccounts/<storage>

# Assign if missing
az role assignment create \
  --role "Storage Blob Data Contributor" \
  --assignee-object-id <principal-id> \
  --scope <storage-scope>

# Restart pod to refresh token
kubectl delete pod -n monitoring <ingester-pod>


3. Ingester OOM

# Increase memory limits
ingester:
  resources:
    limits:
      memory: 16Gi


4. Query Timeout

loki:
  querier:
    query_timeout: 5m
    max_concurrent: 8
  query_scheduler:
    max_outstanding_requests_per_tenant: 2048

Diagnostic Commands
# Check pod status
kubectl get pods -n monitoring -l app.kubernetes.io/name=loki

# Check ingester logs
kubectl logs -n monitoring -l app.kubernetes.io/component=ingester --tail=100

# Check compactor logs
kubectl logs -n monitoring -l app.kubernetes.io/component=compactor --tail=100

# Verify readiness
kubectl exec -it <loki-pod> -n monitoring -- wget -qO- http://localhost:3100/ready

# Check configuration
kubectl exec -it <loki-pod> -n monitoring -- cat /etc/loki/config/config.yaml

API Reference
Ingestion
# Push logs
POST /loki/api/v1/push

# OTLP logs
POST /otlp/v1/logs

Query
# Instant query
GET /loki/api/v1/query?query={job="app"}&time=<timestamp>

# Range query
GET /loki/api/v1/query_range?query={job="app"}&start=<start>&end=<end>

# Labels
GET /loki/api/v1/labels
GET /loki/api/v1/label/<name>/values

# Series
GET /loki/api/v1/series

# Tail (WebSocket)
GET /loki/api/v1/tail?query={job="app"}

Health
GET /ready
GET /metrics

Reference Documentation

For detailed configuration by topic:

Storage Configuration: Object stores, retention, WAL
LogQL Reference: Query syntax and examples
OpenTelemetry Integration: OTLP configuration
External Resources
Official Loki Documentation
Loki Helm Chart
LogQL Documentation
Loki GitHub Repository
Weekly Installs
80
Repository
julianobarbosa/…e-skills
GitHub Stars
64
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass