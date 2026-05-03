---
title: prompt enhancer
url: https://skills.sh/catlog22/claude-code-workflow/prompt-enhancer
---

# prompt enhancer

skills/catlog22/claude-code-workflow/Prompt Enhancer
Prompt Enhancer
Installation
$ npx skills add https://github.com/catlog22/claude-code-workflow --skill 'Prompt Enhancer'
SKILL.md
Prompt Enhancer

Transform: Vague intent → Structured specification (Memory-based, Direct Output)

Languages: English + Chinese (中英文语义识别)

Process (Internal → Direct Output)

Internal Analysis: Intelligently extract session context, identify tech stack, and structure into actionable format.

Output: Direct structured prompt (no intermediate steps shown)

Output Format

Dynamic Structure: Adapt fields based on task type and context needs. Not all fields are required.

Core Fields (always present):

INTENT: One-sentence technical goal
ACTION: Concrete steps with technical details

Optional Fields (include when relevant):

TECH STACK: Relevant technologies (when tech-specific)
CONTEXT: Session memory findings (when context matters)
ATTENTION: Critical constraints (when risks/requirements exist)
SCOPE: Affected modules/files (for multi-module tasks)
METRICS: Success criteria (for optimization/performance tasks)
DEPENDENCIES: Related components (for integration tasks)

Example (Simple Task):

📋 ENHANCED PROMPT

INTENT: Fix authentication token validation in JWT middleware

ACTION:
1. Review token expiration logic in auth middleware
2. Add proper error handling for expired tokens
3. Test with valid/expired/malformed tokens


Example (Complex Task):

📋 ENHANCED PROMPT

INTENT: Optimize API performance with caching and database indexing

TECH STACK:
- Redis: Response caching
- PostgreSQL: Query optimization

CONTEXT:
- API response times >2s mentioned in previous conversation
- PostgreSQL slow query logs show N+1 problems

ACTION:
1. Profile endpoints to identify slow queries
2. Add PostgreSQL indexes on frequently queried columns
3. Implement Redis caching for read-heavy endpoints
4. Add cache invalidation on data updates

METRICS:
- Target: <500ms API response time
- Cache hit ratio: >80%

ATTENTION:
- Maintain backward compatibility with existing API contracts
- Handle cache invalidation correctly to avoid stale data

Workflow
Trigger (-e/--enhance) → Internal Analysis → Dynamic Output
         ↓                       ↓                  ↓
   User Input           Assess Task Type      Select Fields
                    Extract Memory Context    Structure Prompt

Detect: User input contains -e or --enhance
Analyze:
Determine task type (fix/optimize/implement/refactor)
Extract relevant session context
Identify tech stack and constraints
Structure:
Always include: INTENT + ACTION
Conditionally add: TECH STACK, CONTEXT, ATTENTION, METRICS, etc.
Output: Present dynamically structured prompt
Enhancement Guidelines (Internal)

Always Include:

Clear, actionable INTENT
Concrete ACTION steps with technical details

Add When Relevant:

TECH STACK: Task involves specific technologies
CONTEXT: Session memory provides useful background
ATTENTION: Security/compatibility/performance concerns exist
SCOPE: Multi-module or cross-component changes
METRICS: Performance/optimization goals need measurement
DEPENDENCIES: Integration points matter

Quality Checks:

Make vague intent explicit
Resolve ambiguous references
Add testing/validation steps
Include constraints from memory
Best Practices
✅ Trigger only on -e/--enhance flags
✅ Use dynamic field selection based on task type
✅ Extract memory context ONLY (no file reading)
✅ Always include INTENT + ACTION as core fields
✅ Add optional fields only when relevant to task
✅ Direct output (no intermediate steps shown)
❌ NO tool calls
❌ NO file operations (Bash, Read, Glob, Grep)
❌ NO fixed template - adapt to task needs
Weekly Installs
–
Repository
catlog22/claude…workflow
GitHub Stars
1.9K
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass