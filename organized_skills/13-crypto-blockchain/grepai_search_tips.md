---
rating: ⭐⭐⭐
title: grepai-search-tips
url: https://skills.sh/yoanbernabeu/grepai-skills/grepai-search-tips
---

# grepai-search-tips

skills/yoanbernabeu/grepai-skills/grepai-search-tips
grepai-search-tips
Installation
$ npx skills add https://github.com/yoanbernabeu/grepai-skills --skill grepai-search-tips
SKILL.md
GrepAI Search Tips

This skill provides tips and best practices for writing effective semantic search queries.

When to Use This Skill
Improving search result quality
Learning semantic search techniques
Understanding how to phrase queries
Troubleshooting poor search results
Semantic Search Mindset

Think differently from text search:

Text Search (grep)	Semantic Search (GrepAI)
Search for exact text	Search for meaning/intent
"getUserById"	"retrieve user from database by ID"
Literal match	Conceptual match
Query Writing Principles
1. Describe Intent, Not Implementation

❌ Bad: getUserById ✅ Good: fetch user record from database using ID

❌ Bad: handleError ✅ Good: error handling and response to client

❌ Bad: validateInput ✅ Good: check if user input is valid and safe

2. Use Descriptive Language

❌ Bad: auth ✅ Good: user authentication and authorization

❌ Bad: db ✅ Good: database connection and queries

❌ Bad: config ✅ Good: application configuration loading

3. Be Specific About Context

❌ Bad: validation ✅ Good: validate email address format

❌ Bad: parse ✅ Good: parse JSON request body

❌ Bad: send ✅ Good: send email notification to user

4. Use 3-7 Words
Length	Example	Quality
Too short	"auth"	⚠️ Vague
Good	"user authentication middleware"	✅ Specific
Too long	"the code that handles user authentication and validates JWT tokens in the middleware layer"	⚠️ Verbose
5. Use English

Embedding models are trained primarily on English:

❌ authentification utilisateur (French) ✅ user authentication

Even if your code comments are in another language, English queries work best.

Query Patterns
Finding Code by Behavior
grepai search "validate user credentials before login"
grepai search "send notification when order is placed"
grepai search "calculate total price with discounts"
grepai search "retry failed HTTP requests"

Finding Code by Purpose
grepai search "middleware that checks authentication"
grepai search "function that formats dates"
grepai search "service that sends emails"
grepai search "handler for payment processing"

Finding Error Handling
grepai search "handle errors from API calls"
grepai search "catch and log exceptions"
grepai search "error response to client"
grepai search "validation error messages"

Finding Data Operations
grepai search "save user to database"
grepai search "query products by category"
grepai search "cache frequently accessed data"
grepai search "transform data before storage"

Finding Configuration
grepai search "load configuration from environment"
grepai search "database connection settings"
grepai search "API keys and secrets management"
grepai search "feature flags and toggles"

Finding Security Code
grepai search "password hashing and verification"
grepai search "input sanitization to prevent injection"
grepai search "rate limiting for API endpoints"
grepai search "CORS configuration"

Iterative Refinement

If results aren't good, iterate:

Start Broad
grepai search "authentication"
# Results too varied

Add Context
grepai search "JWT authentication"
# Better, but still broad

Be Specific
grepai search "JWT token validation middleware"
# Precise results

Using Synonyms

Semantic search understands synonyms. Try different phrasings:

# These may return similar results:
grepai search "user authentication"
grepai search "user login verification"
grepai search "credential validation"
grepai search "identity verification"

Domain-Specific Terms

Use your domain vocabulary:

# E-commerce
grepai search "shopping cart checkout process"
grepai search "inventory stock management"

# Finance
grepai search "transaction processing"
grepai search "payment reconciliation"

# Healthcare
grepai search "patient record retrieval"
grepai search "appointment scheduling"

Question-Style Queries

Natural questions work well:

grepai search "how are users authenticated"
grepai search "where is the database connection configured"
grepai search "what happens when a request fails"
grepai search "how are errors logged"

Avoiding Common Mistakes
❌ Don't Use Exact Function Names

If you know the exact name, use grep:

grep -r "getUserById" .  # Text search


GrepAI is for when you don't know the exact name:

grepai search "retrieve user from database"  # Semantic search

❌ Don't Be Too Abstract
# Too abstract
grepai search "business logic"

# More concrete
grepai search "calculate order total with tax"

❌ Don't Use Code Syntax
# Don't do this
grepai search "function() { return }"

# Do this
grepai search "function that returns early"

❌ Don't Over-Specify
# Over-specified (mentions irrelevant details)
grepai search "async function in TypeScript file that uses axios to fetch"

# Better
grepai search "fetch data from external API"

Interpreting Results
High Scores (0.85+)

Strong match. The code likely does what you described.

Medium Scores (0.70-0.84)

Related code. May be what you want, or adjacent functionality.

Low Scores (0.60-0.69)

Loosely related. Consider refining your query.

Very Low Scores (<0.60)

Weak match. The concept may not exist in the codebase, or query needs rework.

When GrepAI Doesn't Find Results
Check the index: grepai status
Verify files are indexed: Not in ignore patterns?
Try simpler query: Remove specificity
Try different words: Use synonyms
Check if code exists: Maybe it doesn't yet!
Quick Reference Card
Situation	Query Style
Know the behavior	"validates email format"
Know the domain	"payment processing flow"
Exploring	"how errors are handled"
Finding entry points	"main application startup"
Finding dependencies	"where database is connected"
Output Format

Tips summary:

📝 GrepAI Search Tips

✅ DO:
- Describe intent, not implementation
- Use 3-7 descriptive words
- Use English queries
- Iterate and refine

❌ DON'T:
- Use exact function names (use grep)
- Write too short queries ("auth")
- Write too long queries
- Use code syntax in queries

Example transformations:
  "auth"            → "user authentication and login"
  "getUserById"     → "fetch user by ID from database"
  "handleError"     → "error handling and logging"

Weekly Installs
496
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