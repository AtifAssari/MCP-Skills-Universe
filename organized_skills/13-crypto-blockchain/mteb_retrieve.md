---
rating: ⭐⭐
title: mteb-retrieve
url: https://skills.sh/letta-ai/skills/mteb-retrieve
---

# mteb-retrieve

skills/letta-ai/skills/mteb-retrieve
mteb-retrieve
Installation
$ npx skills add https://github.com/letta-ai/skills --skill mteb-retrieve
SKILL.md
MTEB Retrieve
Overview

This skill provides guidance for text embedding retrieval tasks that involve encoding documents and queries using embedding models, computing similarity scores, and retrieving or ranking documents based on semantic similarity.

Workflow
Step 1: Inspect and Parse Data

Before writing any code, carefully inspect the raw data format:

Read the data file and examine actual line contents
Identify formatting artifacts such as:
Line number prefixes (e.g., 1→, 2→, 1., 1:)
Whitespace or tab characters
Quote characters or escape sequences
Header rows or metadata
Design parsing logic that strips all non-content artifacts

Common data format issues:

Files with line numbers prepended (e.g., 1→Document text here)
CSV/TSV files with headers
JSON files with nested structures
Files with trailing whitespace or newlines

Verification: Print 2-3 parsed documents to confirm they contain only the actual text content.

Step 2: Load the Embedding Model
Identify the model specified in the task (e.g., sentence-transformers/all-MiniLM-L6-v2)
Load the model using the appropriate library (typically sentence-transformers)
Verify model loading succeeded before proceeding
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('model-name')

Step 3: Encode Documents and Query
Encode all documents using the model's encode method
Encode the query using the same model
Ensure consistent encoding - same model and parameters for both
Step 4: Compute Similarities
Use cosine similarity (most common for embedding retrieval)
Compute similarity between query embedding and all document embeddings
Store similarities with corresponding document indices
from sklearn.metrics.pairwise import cosine_similarity
similarities = cosine_similarity([query_embedding], document_embeddings)[0]

Step 5: Rank and Retrieve
Sort documents by similarity score in descending order
Handle the ranking request (e.g., "5th most similar" means index 4 after sorting)
Extract the requested document(s)
Step 6: Validate Results

Critical verification steps before finalizing:

Print top 10 results with similarity scores and document text
Semantic sanity check: Do top results relate to the query?
If query is "terminal-bench", expect documents containing "terminal", "bench", or "benchmark"
If results seem unrelated, investigate data parsing or encoding issues
Check for anomalies:
Are similarity scores reasonable (typically 0.0 to 1.0)?
Are there unexpected ties in similarity values?
Do document texts look properly parsed?
Common Pitfalls
1. Data Format Parsing Errors

Problem: Document files often include line numbers, prefixes, or other formatting artifacts.

Example: A file might contain:

 1→Beyond the Imitation Game...
 2→MTEB: Massive Text Embedding Benchmark


If not properly parsed, embeddings are computed on 1→Beyond the Imitation Game... instead of just Beyond the Imitation Game....

Solution: Always inspect raw file contents and strip all formatting artifacts before encoding.

2. Skipping Validation

Problem: Accepting results without verification can lead to incorrect answers.

Solution: Always print intermediate results (top 10 documents with scores) and verify they make semantic sense given the query.

3. Off-by-One Errors in Ranking

Problem: Confusion between 0-indexed and 1-indexed rankings.

Example: "5th most similar" means:

Sort by similarity descending
Take index 4 (0-indexed) or position 5 (1-indexed)

Solution: Be explicit about indexing when retrieving ranked results.

4. Ignoring Semantic Reasonableness

Problem: Not questioning whether results make logical sense.

Example: If query is "terminal-bench" and the 5th result is "HumanEval: Benchmarking Python code generation", ask: Does this semantically relate to the query? If not, something may be wrong.

Solution: Apply domain knowledge to sanity-check results before finalizing.

Verification Checklist

Before submitting results, confirm:

 Data was inspected for formatting artifacts
 Documents were parsed to contain only actual text content
 Embedding model loaded successfully
 Query and documents encoded with same model
 Similarity computation used correct metric (cosine similarity)
 Top 10+ results printed and reviewed
 Top results semantically relate to the query
 Correct document extracted based on ranking request
Weekly Installs
35
Repository
letta-ai/skills
GitHub Stars
94
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass