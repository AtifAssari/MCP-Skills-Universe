---
title: zvec
url: https://skills.sh/zvec-ai/zvec-agent-skills/zvec
---

# zvec

skills/zvec-ai/zvec-agent-skills/zvec
zvec
Installation
$ npx skills add https://github.com/zvec-ai/zvec-agent-skills --skill zvec
SKILL.md
Usage Instructions
Before starting, understand the following:

Development Language: Python or Node.js?

Python: use pip install zvec
Node.js: use npm install @zvec/zvec

Use Cases:

RAG document retrieval system
Semantic search
Multimodal search (image + text)
Hybrid search (keywords + semantic)

Data Scale:

< 100k: use FLAT index (exact search)
100k-10M: use HNSW index (recommended default)

10M: use IVF index (memory optimized)

Decision Workflow
User needs vector search functionality
Choose development language (Python/Node.js)
Determine use case
RAG system → use single-vector search + document chunk management
E-commerce search → use hybrid search (vector + filter)
Multimodal → use multi-vector search + weighted ranking
Design Schema (vector fields + scalar fields)
Select index type (HNSW/FLAT/IVF)
Implement data synchronization strategy
Default Recommendations
Use create_and_open() / ZVecCreateAndOpen() to create Collection
Use cosine similarity (COSINE) as default distance metric
Use FP32 type for dense vectors
Create InvertIndexParam index for filter fields
Validation Checklist
Vector dimensions match Schema definition
Scalar field types are correct
Filter condition syntax is correct
Call optimize() after large batch writes
Quick Start

Python:

import zvec

# Create Collection
schema = zvec.CollectionSchema(
    name="my_collection",
    fields=[
        zvec.FieldSchema(name="title", data_type=zvec.DataType.STRING),
    ],
    vectors=[
        zvec.VectorSchema(
            name="embedding",
            data_type=zvec.DataType.VECTOR_FP32,
            dimension=768,
            index_param=zvec.HnswIndexParam(
                metric_type=zvec.MetricType.COSINE
            ),
        ),
    ],
)

collection = zvec.create_and_open("./my_data", schema)

# Insert document
collection.upsert(zvec.Doc(
    id="doc_1",
    vectors={"embedding": [0.1] * 768},
    fields={"title": "Hello World"},
))

# Search
results = collection.query(
    vectors=zvec.VectorQuery(
        field_name="embedding",
        vector=[0.1] * 768,
    ),
    topk=10,
)


Node.js:

import { ZVecCreateAndOpen, ZVecCollectionSchema, ZVecFieldSchema, ZVecVectorSchema, ZVecDataType, ZVecHnswIndexParams, ZVecMetricType } from "@zvec/zvec";

const schema = new ZVecCollectionSchema({
  name: "my_collection",
  fields: [new ZVecFieldSchema({ name: "title", dataType: ZVecDataType.STRING })],
  vectors: [new ZVecVectorSchema({
    name: "embedding",
    dataType: ZVecDataType.VECTOR_FP32,
    dimension: 768,
    indexParams: new ZVecHnswIndexParams({ metricType: ZVecMetricType.COSINE }),
  })],
});

const collection = ZVecCreateAndOpen("./my_data", schema);

Core Concepts
Data Model

Collection

Similar to a table in relational databases, a container for storing, organizing, and querying data
Each Collection has a Schema defining its structure
Each Collection is independently persisted in a dedicated directory on disk

Document

Basic unit of data storage, similar to a row in a relational table
Contains three core components:
id: unique string identifier
vectors: named vector collection (supports dense and sparse vectors)
fields: named scalar field collection

Schema

Dynamic Schema: scalar fields and vectors can be added or removed at any time
Strong type system: each field must declare a DataType
Vector Types

Dense Vector

Fixed-length real-valued embeddings
Types: VECTOR_FP16, VECTOR_FP32, VECTOR_INT8
Suitable for: semantic understanding, context capture

Sparse Vector

High-dimensional representation with only a few non-zero dimensions
Types: SPARSE_VECTOR_FP32, SPARSE_VECTOR_FP16
Suitable for: keyword matching, BM25 scoring
Index Types
Index Type	Characteristics	Use Case
FLAT	Brute force search, exact results	Small scale data (<100k)
HNSW	Approximate nearest neighbor, graph structure	Large scale data (recommended default)
IVF	Inverted file index	Very large scale data
Available Topics
Python
Quick Start - Quick start with Zvec Python API
Collection Management - Create, open, and manage Collections
Data Operations - Insert, update, and delete documents
Vector Search - Single-vector, multi-vector, and hybrid search
RAG System - Build document retrieval system
Hybrid Search - Vector similarity + scalar filtering
Multimodal Search - Image + text joint search
Node.js
Quick Start - Quick start with Zvec Node.js API
Collection Management - Create, open, and manage Collections
Data Operations - Insert, update, and delete documents
Vector Search - Single-vector, multi-vector, and hybrid search
RAG System - Build document retrieval system
Hybrid Search - Vector similarity + scalar filtering
Multimodal Search - Image + text joint search
General
Configuration - Global configuration and initialization
Data Model - Zvec data model overview
Embedding - Text embedding functions (Python only)
Reranker - Result reranking functions (Python only)
API Cheatsheet - Python & Node.js API quick reference
Troubleshooting - Common issues and solutions
Available Topics
Python
Collection Management
Data Operations
Hybrid Search
Multimodal Search
Quick Start
Rag System
Vector Search
Node.js
Collection Management
Data Operations
Hybrid Search
Multimodal Search
Quick Start
Rag System
Vector Search
General
Configuration
Data Model
Embedding
Reranker
Api Cheatsheet
Troubleshooting
Weekly Installs
14
Repository
zvec-ai/zvec-ag…t-skills
GitHub Stars
5
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass