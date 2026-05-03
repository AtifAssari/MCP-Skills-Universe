---
rating: ⭐⭐⭐
title: sourcegraph-search
url: https://skills.sh/markus1189/nixos-config/sourcegraph-search
---

# sourcegraph-search

skills/markus1189/nixos-config/sourcegraph-search
sourcegraph-search
Installation
$ npx skills add https://github.com/markus1189/nixos-config --skill sourcegraph-search
SKILL.md
Sourcegraph Code Search Skill

This skill enables autonomous code searching across repositories using the Sourcegraph CLI (src command).

When to Invoke This Skill

Use this skill when you need to:

Research how features are implemented across codebases
Find examples of API usage, patterns, or libraries
Locate specific code patterns (functions, classes, imports)
Analyze code across repositories (not just local files)
Search commit history or diffs for changes
Find security issues or credential leaks
Understand architecture by searching for patterns
Answer "where is X used?" questions across projects

Do NOT use for local file searches - use Grep/Glob instead.

Reference Navigation

The reference files are comprehensive. To find specific topics quickly:

# Search reference.md sections
grep -n "^##" references/reference.md

# Find specific filter documentation
grep -n "^### \`repo:" references/reference.md
grep -n "^### \`file:" references/reference.md
grep -n "^### \`lang:" references/reference.md

# Find examples by use case
grep -n "^##" references/examples.md


See reference.md for complete syntax documentation. See examples.md for practical search patterns organized by use case.

Quick Start
Basic Search Syntax
src search 'PATTERN'              # Simple text search
src search -json 'PATTERN'        # JSON output for parsing
src search 'repo:REGEX PATTERN'   # Search specific repos
src search 'lang:go PATTERN'      # Search Go files only

Common Search Patterns

1. Find function/method implementations

src search 'lang:go func handleRequest'
src search 'lang:python def authenticate'


2. Search in specific repository

src search 'repo:github.com/org/repo$ TODO'
src search 'repo:sourcegraph/sourcegraph auth'


3. Search with multiple filters

src search 'repo:kubernetes lang:go file:test fmt.Errorf'
src search 'TODO -file:test -file:spec'


See examples.md for more patterns including file types, commit history, and boolean operators.

Workflow

When searching code:

Understand the goal - What pattern? Which repos/languages?
Construct the query - Start with pattern, add filters (repo:, lang:, file:), use operators (AND, OR, NOT)
Execute - Run src search 'query' or src search -json 'query' for programmatic parsing
Parse results - Extract matches, identify patterns, note files for investigation
Refine - Too many results? Add filters. Too few? Broaden search.
Key Filters

Most common filters: repo:, lang:, file:, type:, case:, - prefix for exclusion.

See reference.md for complete filter documentation and syntax.

Pattern Types

Sourcegraph supports three pattern types:

Literal (default): Exact text matching

src search 'func main('


Regexp: Use patternType:regexp for regex (RE2 syntax)

src search 'patternType:regexp func \w+Handler'


Structural: Use patternType:structural for syntax-aware matching

src search 'patternType:structural fmt.Sprintf(:[format], :[...])'


See reference.md for complete pattern syntax, regex reference, and structural search details.

CLI Flags
-json: Output results as JSON (for parsing)
-stream: Stream results as they arrive
-display N: Limit displayed results (with -stream)
--: Separate flags from query (for queries starting with -)
Important Notes
Negation in Queries

Queries starting with negation need -- separator:

src search -- '-repo:foo/bar error'


Use -json for programmatic parsing. Set NO_COLOR=t to disable colors or COLOR=t to force colors when piping.

Default search scope excludes forks and archived repos. Include with fork:yes or archived:yes.

Examples by Use Case
Finding Implementation Examples
# How do people handle authentication in Go?
src search 'lang:go repo:.*auth.* middleware'

# React hooks usage
src search 'lang:typescript repo:facebook/react use.*Hook'

Security Auditing
# Find hardcoded credentials
src search 'patternType:regexp (password|secret|api_key)\s*=\s*["\'][^"\']+["\']'

# Exposed private keys
src search 'type:diff BEGIN.*PRIVATE KEY'

API Research
# How is this library used?
src search 'lang:python import requests'

# Find all GraphQL mutations
src search 'file:\.graphql$ type Mutation'

Refactoring Research
# Find deprecated API usage
src search 'repo:myorg/ oldDeprecatedFunction'

# Find TODO comments in non-test files
src search 'TODO -file:test -file:spec'

Advanced Features

For comprehensive syntax reference, pattern types, and advanced operators, see reference.md.

For more practical examples and complex query patterns, see examples.md.

Troubleshooting

No results?

Check repository access/permissions
Verify repository is indexed by Sourcegraph
Try broader search terms
Remove restrictive filters

Too many results?

Add more specific filters
Use lang: to narrow by language
Use repo: with regex for specific repositories
Combine with file: for specific paths

Syntax errors?

Check regex syntax (RE2 format)
Quote the entire query
Use -- before queries starting with -
Verify filter names are correct
Integration with Other Tools

After finding results with Sourcegraph:

Use Read tool to examine specific files locally
Use Grep for more detailed local searching
Use Bash for git operations on repositories
Use WebFetch to access repository URLs
Best Practices
Start broad, then narrow: Begin with simple patterns, add filters incrementally
Use appropriate pattern types: Literal for exact matches, regexp for patterns
Combine filters effectively: repo: + lang: + file: for precision
Parse JSON for programmatic analysis: Use -json when processing results
Respect quotas and limits: Sourcegraph may have rate limits or result limits
Cache insights: Remember patterns that work for future searches
Performance Tips
Specific repo: filters are faster than broad searches
Language filters (lang:) significantly narrow scope
File filters (file:) reduce search surface
Use count: to limit results when you just need examples
Streaming (-stream) is better for large result sets
Reference Files
reference.md: Complete syntax documentation, all filters, operators, pattern types
examples.md: Practical search patterns organized by use case
Weekly Installs
22
Repository
markus1189/nixos-config
GitHub Stars
5
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail