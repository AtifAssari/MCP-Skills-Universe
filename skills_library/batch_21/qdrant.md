---
title: qdrant
url: https://skills.sh/vm0-ai/vm0-skills/qdrant
---

# qdrant

skills/vm0-ai/vm0-skills/qdrant
qdrant
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill qdrant
SKILL.md
Troubleshooting

If requests fail, run zero doctor check-connector --env-name QDRANT_TOKEN or zero doctor check-connector --url https://your-cluster.cloud.qdrant.io/collections --method GET

How to Use

All examples below assume you have QDRANT_BASE_URL and QDRANT_TOKEN set.

1. Check Server Status

Verify connection to Qdrant:

curl -s -X GET "$QDRANT_BASE_URL" --header "api-key: $QDRANT_TOKEN"

2. List Collections

Get all collections:

curl -s -X GET "$QDRANT_BASE_URL/collections" --header "api-key: $QDRANT_TOKEN"

3. Create a Collection

Create a collection for storing vectors:

Write to /tmp/qdrant_request.json:

{
  "vectors": {
    "size": 1536,
    "distance": "Cosine"
  }
}


Then run:

curl -s -X PUT "$QDRANT_BASE_URL/collections/my_collection" --header "api-key: $QDRANT_TOKEN" --header "Content-Type: application/json" -d @/tmp/qdrant_request.json


Distance metrics:

Cosine - Cosine similarity (recommended for normalized vectors)
Dot - Dot product
Euclid - Euclidean distance
Manhattan - Manhattan distance

Common vector sizes:

OpenAI text-embedding-3-small: 1536
OpenAI text-embedding-3-large: 3072
Cohere: 1024
4. Get Collection Info

Get details about a collection:

curl -s -X GET "$QDRANT_BASE_URL/collections/my_collection" --header "api-key: $QDRANT_TOKEN"

5. Upsert Points (Insert/Update Vectors)

Add vectors with payload (metadata):

Write to /tmp/qdrant_request.json:

{
  "points": [
    {
      "id": 1,
      "vector": [0.05, 0.61, 0.76, 0.74],
      "payload": {"text": "Hello world", "source": "doc1"}
    },
    {
      "id": 2,
      "vector": [0.19, 0.81, 0.75, 0.11],
      "payload": {"text": "Goodbye world", "source": "doc2"}
    }
  ]
}


Then run:

curl -s -X PUT "$QDRANT_BASE_URL/collections/my_collection/points" --header "api-key: $QDRANT_TOKEN" --header "Content-Type: application/json" -d @/tmp/qdrant_request.json

6. Search Similar Vectors

Find vectors similar to a query vector:

Write to /tmp/qdrant_request.json:

{
  "query": [0.05, 0.61, 0.76, 0.74],
  "limit": 5,
  "with_payload": true
}


Then run:

curl -s -X POST "$QDRANT_BASE_URL/collections/my_collection/points/query" --header "api-key: $QDRANT_TOKEN" --header "Content-Type: application/json" -d @/tmp/qdrant_request.json


Response:

{
  "result": {
  "points": [
  {"id": 1, "score": 0.99, "payload": {"text": "Hello world"}}
  ]
  }
}

7. Search with Filters

Filter results by payload fields:

Write to /tmp/qdrant_request.json:

{
  "query": [0.05, 0.61, 0.76, 0.74],
  "limit": 5,
  "filter": {
    "must": [
      {"key": "source", "match": {"value": "doc1"}}
    ]
  },
  "with_payload": true
}


Then run:

curl -s -X POST "$QDRANT_BASE_URL/collections/my_collection/points/query" --header "api-key: $QDRANT_TOKEN" --header "Content-Type: application/json" -d @/tmp/qdrant_request.json


Filter operators:

must - All conditions must match (AND)
should - At least one must match (OR)
must_not - None should match (NOT)
8. Get Points by ID

Retrieve specific points:

Write to /tmp/qdrant_request.json:

{
  "ids": [1, 2],
  "with_payload": true,
  "with_vector": true
}


Then run:

curl -s -X POST "$QDRANT_BASE_URL/collections/my_collection/points" --header "api-key: $QDRANT_TOKEN" --header "Content-Type: application/json" -d @/tmp/qdrant_request.json

9. Delete Points

Delete by IDs:

Write to /tmp/qdrant_request.json:

{
  "points": [1, 2]
}


Then run:

curl -s -X POST "$QDRANT_BASE_URL/collections/my_collection/points/delete" --header "api-key: $QDRANT_TOKEN" --header "Content-Type: application/json" -d @/tmp/qdrant_request.json


Delete by filter:

Write to /tmp/qdrant_request.json:

{
  "filter": {
    "must": [
      {"key": "source", "match": {"value": "doc1"}}
    ]
  }
}


Then run:

curl -s -X POST "$QDRANT_BASE_URL/collections/my_collection/points/delete" --header "api-key: $QDRANT_TOKEN" --header "Content-Type: application/json" -d @/tmp/qdrant_request.json

10. Delete Collection

Remove a collection entirely:

curl -s -X DELETE "$QDRANT_BASE_URL/collections/my_collection" --header "api-key: $QDRANT_TOKEN"

11. Count Points

Get total count or filtered count:

Write to /tmp/qdrant_request.json:

{
  "exact": true
}


Then run:

curl -s -X POST "$QDRANT_BASE_URL/collections/my_collection/points/count" --header "api-key: $QDRANT_TOKEN" --header "Content-Type: application/json" -d @/tmp/qdrant_request.json

Filter Syntax

Common filter conditions:

{
  "filter": {
  "must": [
  {"key": "city", "match": {"value": "London"}},
  {"key": "price", "range": {"gte": 100, "lte": 500}},
  {"key": "tags", "match": {"any": ["electronics", "sale"]}}
  ]
  }
}


Match types:

match.value - Exact match
match.any - Match any in list
match.except - Match none in list
range - Numeric range (gt, gte, lt, lte)
Guidelines
Match vector size: Collection vector size must match your embedding model output
Use Cosine for normalized vectors: Most embedding models output normalized vectors
Add payload for filtering: Store metadata with vectors for filtered searches
Batch upserts: Insert multiple points in one request for efficiency
Use score_threshold: Filter out low-similarity results in search
Weekly Installs
75
Repository
vm0-ai/vm0-skills
GitHub Stars
57
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass