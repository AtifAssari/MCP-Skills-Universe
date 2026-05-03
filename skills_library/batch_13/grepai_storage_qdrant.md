---
title: grepai-storage-qdrant
url: https://skills.sh/yoanbernabeu/grepai-skills/grepai-storage-qdrant
---

# grepai-storage-qdrant

skills/yoanbernabeu/grepai-skills/grepai-storage-qdrant
grepai-storage-qdrant
Installation
$ npx skills add https://github.com/yoanbernabeu/grepai-skills --skill grepai-storage-qdrant
SKILL.md
GrepAI Storage with Qdrant

This skill covers using Qdrant as the storage backend for GrepAI, offering high-performance vector search.

When to Use This Skill
Need fastest possible search performance
Very large codebases (50K+ files)
Already using Qdrant infrastructure
Want advanced vector search features
What is Qdrant?

Qdrant is a purpose-built vector database offering:

⚡ Extremely fast vector similarity search
📏 Excellent scalability
🔧 Advanced filtering capabilities
🐳 Easy Docker deployment
Prerequisites
Qdrant server running
Network access to Qdrant
Advantages
Benefit	Description
⚡ Performance	Fastest vector search
📏 Scalability	Handles millions of vectors
🔍 Advanced	Filtering, payloads, sharding
🐳 Easy deploy	Docker-ready
☁️ Cloud option	Qdrant Cloud available
Setting Up Qdrant
Option 1: Docker (Recommended)
# Run Qdrant with persistent storage
docker run -d \
  --name grepai-qdrant \
  -p 6333:6333 \
  -p 6334:6334 \
  -v qdrant_storage:/qdrant/storage \
  qdrant/qdrant


Ports:

6333: REST API
6334: gRPC API (used by GrepAI)
Option 2: Docker Compose
# docker-compose.yml
version: '3.8'
services:
  qdrant:
    image: qdrant/qdrant
    ports:
      - "6333:6333"
      - "6334:6334"
    volumes:
      - qdrant_storage:/qdrant/storage
    environment:
      - QDRANT__SERVICE__GRPC_PORT=6334

volumes:
  qdrant_storage:

docker-compose up -d

Option 3: Qdrant Cloud
Sign up at cloud.qdrant.io
Create a cluster
Get your endpoint and API key
Configuration
Basic Configuration (Local)
# .grepai/config.yaml
store:
  backend: qdrant
  qdrant:
    endpoint: localhost
    port: 6334

With TLS (Production)
store:
  backend: qdrant
  qdrant:
    endpoint: qdrant.company.com
    port: 6334
    use_tls: true

With API Key (Qdrant Cloud)
store:
  backend: qdrant
  qdrant:
    endpoint: your-cluster.aws.cloud.qdrant.io
    port: 6334
    use_tls: true
    api_key: ${QDRANT_API_KEY}


Set the environment variable:

export QDRANT_API_KEY="your-api-key"

Configuration Options
Option	Default	Description
endpoint	localhost	Qdrant server hostname
port	6334	gRPC port
use_tls	false	Enable TLS encryption
api_key	none	Authentication key
Verifying Setup
Check Qdrant is Running
# REST API health check
curl http://localhost:6333/health

# Expected: {"status":"ok"}

Check Collections (after indexing)
# List collections
curl http://localhost:6333/collections

# Get collection info
curl http://localhost:6333/collections/grepai

From GrepAI
grepai status

# Should show Qdrant backend info

Qdrant Dashboard

Access the web dashboard at http://localhost:6333/dashboard:

View collections
Browse vectors
Execute queries
Monitor performance
Performance Characteristics
Search Latency
Codebase Size	Vectors	Search Time
Small (1K files)	5,000	<10ms
Medium (10K files)	50,000	<20ms
Large (100K files)	500,000	<50ms
Memory Usage

Qdrant loads vectors into memory for fast search:

Vectors	Dimensions	Memory
10,000	768	~60 MB
100,000	768	~600 MB
1,000,000	768	~6 GB
Advanced Configuration
Qdrant Server Configuration

Create config/production.yaml:

storage:
  storage_path: /qdrant/storage

service:
  grpc_port: 6334
  http_port: 6333
  max_request_size_mb: 32

optimizers:
  memmap_threshold_kb: 200000
  indexing_threshold_kb: 50000


Mount in Docker:

docker run -d \
  -v ./config:/qdrant/config \
  -v qdrant_storage:/qdrant/storage \
  qdrant/qdrant

Collection Settings

GrepAI creates a collection named grepai with:

Vector size: matches your embedding dimensions
Distance: Cosine similarity
On-disk storage for large datasets
Clustering (Advanced)

For very large deployments, Qdrant supports distributed mode:

# qdrant config
cluster:
  enabled: true
  p2p:
    port: 6335

Backup and Restore
Snapshot Creation
# Create snapshot via REST API
curl -X POST 'http://localhost:6333/collections/grepai/snapshots'

Restore Snapshot
# Restore from snapshot
curl -X PUT 'http://localhost:6333/collections/grepai/snapshots/recover' \
  -H 'Content-Type: application/json' \
  -d '{"location": "/path/to/snapshot"}'

Migrating from GOB
Start Qdrant:
docker run -d --name qdrant -p 6333:6333 -p 6334:6334 qdrant/qdrant

Update configuration:
store:
  backend: qdrant
  qdrant:
    endpoint: localhost
    port: 6334

Delete old index:
rm .grepai/index.gob

Re-index:
grepai watch

Migrating from PostgreSQL
Start Qdrant
Update configuration to use Qdrant
Re-index (embeddings must be regenerated)
Common Issues

❌ Problem: Connection refused ✅ Solution: Ensure Qdrant is running:

docker ps | grep qdrant
docker start grepai-qdrant


❌ Problem: gRPC connection failed ✅ Solution: Check port 6334 is exposed:

docker run -p 6334:6334 ...


❌ Problem: Authentication failed ✅ Solution: Check API key:

echo $QDRANT_API_KEY


❌ Problem: Out of memory ✅ Solutions:

Enable on-disk storage in Qdrant config
Increase Docker memory limit
Use Qdrant Cloud for managed scaling

❌ Problem: Slow initial indexing ✅ Solution: This is normal; Qdrant optimizes in background. Searches will be fast after indexing completes.

Qdrant vs PostgreSQL
Feature	Qdrant	PostgreSQL
Search speed	⚡⚡⚡	⚡⚡
Setup complexity	Easy (Docker)	Medium
SQL queries	❌	✅
Scalability	Excellent	Good
Memory efficiency	Excellent	Good
Team familiarity	Lower	Higher

Recommendation: Use Qdrant for large codebases or maximum performance. Use PostgreSQL if you need SQL integration or team is familiar with it.

Best Practices
Use persistent volume: Mount /qdrant/storage
Enable TLS in production: Set use_tls: true
Secure API key: Use environment variables
Monitor memory: Vector search is memory-intensive
Regular snapshots: Backup before major changes
Output Format

Qdrant storage status:

✅ Qdrant Storage Configured

   Backend: Qdrant
   Endpoint: localhost:6334
   TLS: disabled
   Collection: grepai

   Contents:
   - Files: 5,000
   - Vectors: 25,000
   - Dimensions: 768

   Performance:
   - Connection: OK
   - Indexed: Yes
   - Search latency: ~15ms

Weekly Installs
354
Repository
yoanbernabeu/gr…i-skills
GitHub Stars
16
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass