---
title: pgvector-setup
url: https://skills.sh/vanman2024/ai-dev-marketplace/pgvector-setup
---

# pgvector-setup

skills/vanman2024/ai-dev-marketplace/pgvector-setup
pgvector-setup
Installation
$ npx skills add https://github.com/vanman2024/ai-dev-marketplace --skill pgvector-setup
SKILL.md
pgvector-setup
Instructions

This skill provides complete pgvector setup for Supabase databases, enabling vector search capabilities for AI applications, RAG systems, and semantic search.

Phase 1: Enable pgvector Extension

Run the setup script to enable pgvector:

bash scripts/setup-pgvector.sh [SUPABASE_DB_URL]


This creates the pgvector extension and sets up basic embedding tables.

Choose your embedding dimensions based on your model:

OpenAI text-embedding-3-small: 1536 dimensions
OpenAI text-embedding-3-large: 3072 dimensions
Cohere embed-english-v3.0: 1024 dimensions
Custom models: Check model documentation
Phase 2: Create Embedding Tables

Use the embedding table template:

# Copy template and customize for your use case
cat templates/embedding-table-schema.sql


Customize the schema:

Adjust vector dimensions to match your model
Add metadata columns (tags, timestamps, user_id, etc.)
Configure RLS policies for security

Apply the schema:

psql $SUPABASE_DB_URL < templates/embedding-table-schema.sql

Phase 3: Create Vector Indexes

Choose index type based on your data size:

HNSW (Recommended for most cases):

Best for: < 1M vectors, high recall requirements
Pros: Fast queries, good recall, works well with small-medium datasets
Cons: Slower inserts, higher memory usage
Run: bash scripts/create-indexes.sh hnsw [TABLE_NAME] [DIMENSION]

IVFFlat:

Best for: > 1M vectors, write-heavy workloads
Pros: Faster inserts, lower memory
Cons: Requires training, lower recall
Run: bash scripts/create-indexes.sh ivfflat [TABLE_NAME] [DIMENSION]

Performance Tuning:

HNSW m parameter (default 16): Higher = better recall, more memory
HNSW ef_construction (default 64): Higher = better quality, slower builds
IVFFlat lists (default sqrt(rows)): More lists = faster queries, lower recall
Phase 4: Implement Semantic Search

Create the match function:

-- See templates/match-function.sql for complete example
create or replace function match_documents(
  query_embedding vector(1536)
  match_threshold float
  match_count int
) returns setof documents ...


Query from application:

const { data } = await supabase.rpc('match_documents', {
  query_embedding: embedding
  match_threshold: 0.78
  match_count: 10
});

Phase 5: Setup Hybrid Search (Optional)

For combining keyword and semantic search:

Run hybrid search setup:

bash scripts/setup-hybrid-search.sh [TABLE_NAME]


This configures:

Full-text search with tsvector and GIN indexes
Vector search with HNSW indexes
RRF (Reciprocal Rank Fusion) for combining results
Weighted scoring for tuning keyword vs semantic importance

Use the hybrid search function:

select * from hybrid_search(
  'search query text'
  query_embedding
  match_count := 10
  full_text_weight := 1.0
  semantic_weight := 1.0
);

Phase 6: Test and Validate

Run validation tests:

bash scripts/test-vector-search.sh [TABLE_NAME]


This verifies:

pgvector extension is enabled
Tables have correct vector dimensions
Indexes are created and being used
Query performance is acceptable
Similarity functions return correct results
Key Decisions

Distance Metric Selection:

Cosine distance (<=>): Safe default, handles varying vector magnitudes
Inner product (<#>): Faster for normalized vectors (OpenAI embeddings)
Euclidean distance (<->): Use when absolute distances matter

Index Choice:

Start with HNSW for most applications
Switch to IVFFlat only if:
You have > 1M vectors
Insert performance is critical
You can tolerate lower recall

Dimension Size:

Higher dimensions = better semantic understanding
Lower dimensions = faster queries, less storage
Match your embedding model exactly (never truncate)
Common Patterns

Pattern 1: Document Search

Store document chunks with metadata
Use HNSW index for semantic search
Add full-text for hybrid search
See: examples/document-search-pattern.md

Pattern 2: User Preference Matching

Store user profile embeddings
Use cosine similarity for matching
Update embeddings as preferences change
See: examples/preference-matching-pattern.md

Pattern 3: Product Recommendations

Store product feature embeddings
Use hybrid search (keywords + semantic)
Weight by popularity or ratings
See: examples/product-recommendations-pattern.md
Troubleshooting

Slow queries (> 100ms):

Check if index is being used: EXPLAIN ANALYZE
Increase HNSW ef_search parameter
Consider reducing result limit
Add WHERE clauses to reduce search space

Poor recall (missing relevant results):

Increase match_count
Lower match_threshold
For HNSW: increase m and ef_construction
For IVFFlat: increase lists parameter

High memory usage:

HNSW uses ~10KB per vector
Reduce m parameter (quality tradeoff)
Consider IVFFlat for large datasets
Use partial indexes if possible

Insert performance issues:

HNSW is slow for bulk inserts
Disable index during bulk load, rebuild after
Use IVFFlat for write-heavy workloads
Batch inserts when possible
Security Considerations

Row Level Security (RLS):

Enable RLS on all embedding tables
Filter by user_id or organization_id
Prevent embedding leakage between users
See templates for RLS policy examples

API Key Protection:

Never expose embedding API keys
Use Supabase Edge Functions for embedding generation
Store keys in Supabase secrets
Rate limit embedding requests
Files Reference

Scripts:

scripts/setup-pgvector.sh - Enable extension and create base tables
scripts/create-indexes.sh - Create HNSW or IVFFlat indexes
scripts/setup-hybrid-search.sh - Configure hybrid search
scripts/test-vector-search.sh - Validate setup

Templates:

templates/embedding-table-schema.sql - Table structure with metadata
templates/hnsw-index-config.sql - HNSW index with tuning
templates/ivfflat-index-config.sql - IVFFlat index configuration
templates/hybrid-search-function.sql - Hybrid search with RRF
templates/match-function.sql - Basic semantic search function

Examples:

examples/embedding-strategies.md - Index selection guide
examples/vector-search-examples.md - Common search patterns
examples/document-search-pattern.md - Full document search implementation
examples/preference-matching-pattern.md - User matching system
examples/product-recommendations-pattern.md - Recommendation engine

Plugin: supabase Version: 1.0.0 Last Updated: 2025-10-26

Weekly Installs
10
Repository
vanman2024/ai-d…ketplace
GitHub Stars
10
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn