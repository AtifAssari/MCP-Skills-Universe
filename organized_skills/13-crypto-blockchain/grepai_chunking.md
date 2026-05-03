---
rating: ⭐⭐⭐
title: grepai-chunking
url: https://skills.sh/yoanbernabeu/grepai-skills/grepai-chunking
---

# grepai-chunking

skills/yoanbernabeu/grepai-skills/grepai-chunking
grepai-chunking
Installation
$ npx skills add https://github.com/yoanbernabeu/grepai-skills --skill grepai-chunking
SKILL.md
GrepAI Chunking Configuration

This skill covers how GrepAI splits code files into chunks for embedding, and how to optimize chunking for your codebase.

When to Use This Skill
Optimizing search accuracy
Adjusting for code style (verbose vs. concise)
Troubleshooting search results
Understanding how indexing works
What is Chunking?

Chunking is the process of splitting source files into smaller segments for embedding:

┌─────────────────────────────────────┐
│         Large Source File           │
│         (1000+ tokens)              │
└─────────────────────────────────────┘
                  ↓
┌─────────┐ ┌─────────┐ ┌─────────┐
│ Chunk 1 │ │ Chunk 2 │ │ Chunk 3 │
│ ~512    │ │ ~512    │ │ ~512    │
│ tokens  │ │ tokens  │ │ tokens  │
└─────────┘ └─────────┘ └─────────┘
                  ↓
          Each chunk gets
          its own embedding

Why Chunking Matters

Embedding models have optimal input sizes:

Too large chunks: Less precise search results
Too small chunks: Lost context, fragmented results
Just right: Good balance of precision and context
Configuration
Basic Settings
# .grepai/config.yaml
chunking:
  size: 512      # Tokens per chunk
  overlap: 50    # Overlap between chunks

Understanding Parameters
Chunk Size

The target number of tokens per chunk.

Size	Effect
256	More precise, less context
512	Balanced (default)
1024	More context, less precise
Overlap

Tokens shared between adjacent chunks. Preserves context at boundaries.

Overlap	Effect
0	No overlap, may lose context at boundaries
50	Standard overlap (default)
100	More context, larger index
Visualization

With size=512 and overlap=50:

File: auth.go (1000 tokens)

Chunk 1: tokens 1-512
         ┌────────────────────────────────────┐
         │ func Login(user, pass)...          │
         └────────────────────────────────────┘
                                    ↘
                              50 token overlap
                                    ↙
Chunk 2: tokens 463-974
         ┌────────────────────────────────────┐
         │ ...validate credentials...         │
         └────────────────────────────────────┘
                                    ↘
                              50 token overlap
                                    ↙
Chunk 3: tokens 925-1000
         ┌──────────────┐
         │ ...return    │
         └──────────────┘

Recommended Settings by Language
Verbose Languages (Java, C#)
chunking:
  size: 768    # Larger to capture full methods
  overlap: 75

Concise Languages (Go, Python)
chunking:
  size: 512    # Standard size
  overlap: 50

Very Concise (Rust, Zig)
chunking:
  size: 384    # Smaller for precise results
  overlap: 40

Recommended Settings by Codebase
Small Functions (Microservices)
chunking:
  size: 384    # Capture individual functions
  overlap: 40

Large Classes (Monolith)
chunking:
  size: 768    # Capture more context
  overlap: 100

Mixed Codebase
chunking:
  size: 512    # Balanced default
  overlap: 50

How Tokens are Counted

GrepAI uses approximate token counting:

~4 characters = 1 token (for English text)
Code varies based on identifiers and syntax

Example:

func calculateTotal(items []Item) float64 {
    total := 0.0
    for _, item := range items {
        total += item.Price * float64(item.Quantity)
    }
    return total
}


≈ 45 tokens

Impact on Index Size

Larger overlap = more chunks = larger index:

Size	Overlap	Chunks per 10K tokens	Index Impact
512	0	~20	Smallest
512	50	~22	Standard
512	100	~24	+10%
256	50	~44	+100%
Impact on Search Quality
Too Small Chunks (size: 128)
Query: "authentication middleware"

Result: "...c.AbortWithStatus(401)..."
        (Fragment, missing context)

Just Right (size: 512)
Query: "authentication middleware"

Result: "func AuthMiddleware() gin.HandlerFunc {
            return func(c *gin.Context) {
                token := c.GetHeader("Authorization")
                if token == "" {
                    c.AbortWithStatus(401)
                    return
                }
                // validate token...
            }
        }"
        (Complete function with context)

Too Large Chunks (size: 2048)
Query: "authentication middleware"

Result: "// Multiple unrelated functions...
        func AuthMiddleware()... (your match)
        func LoggingMiddleware()...
        func CORSMiddleware()..."
        (Too much noise)

Experimentation
Testing Different Settings
Try smaller chunks for more precise results:
chunking:
  size: 384
  overlap: 40

Re-index:
rm .grepai/index.gob
grepai watch

Test with searches:
grepai search "your query"

Adjust and repeat until satisfied.
Comparing Results

Before changing settings, save a search result:

grepai search "authentication" > before.txt


After changing settings and re-indexing:

grepai search "authentication" > after.txt
diff before.txt after.txt

Chunk Boundaries

GrepAI tries to split at logical boundaries:

Empty lines (function/class boundaries)
Closing braces
Statement ends

This means actual chunk sizes may vary slightly from the target.

Best Practices
Start with defaults: 512/50 works well for most codebases
Adjust based on code style: Verbose = larger, concise = smaller
Test with real queries: See what your searches return
Re-index after changes: Must regenerate embeddings
Consider overlap: Don't set to 0 unless index size is critical
Common Issues

❌ Problem: Search results are too fragmented ✅ Solution: Increase chunk size:

chunking:
  size: 768


❌ Problem: Search results have too much irrelevant context ✅ Solution: Decrease chunk size:

chunking:
  size: 384


❌ Problem: Results miss related code at function boundaries ✅ Solution: Increase overlap:

chunking:
  overlap: 100


❌ Problem: Index is too large ✅ Solutions:

Decrease overlap
Increase chunk size
Add more ignore patterns
Output Format

Chunking status:

✅ Chunking Configuration

   Size: 512 tokens
   Overlap: 50 tokens

   Index Statistics:
   - Total files: 245
   - Total chunks: 1,234
   - Avg chunks/file: 5.0
   - Avg chunk size: 478 tokens

   Recommendations:
   - Current settings are balanced
   - Consider size: 384 for more precise results
   - Consider size: 768 for more context

Weekly Installs
419
Repository
yoanbernabeu/gr…i-skills
GitHub Stars
16
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass