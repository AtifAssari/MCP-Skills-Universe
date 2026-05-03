---
rating: ⭐⭐⭐
title: code_tools
url: https://skills.sh/tao3k/omni-dev-fusion/code_tools
---

# code_tools

skills/tao3k/omni-dev-fusion/code_tools
code_tools
Installation
$ npx skills add https://github.com/tao3k/omni-dev-fusion --skill code_tools
SKILL.md
Code Tools Skill

You have loaded the Code Tools Skill - The unified entry point for all code operations.

Primary Command
code_search - Unified Search Interface

This is the ONLY search tool you should use.

# Structure search (finds class/function definitions)
code_search("class User")
code_search("def authenticate")

# Semantic search (finds conceptually related code)
code_search("how does authentication work")
code_search("user validation logic")

# Text search (finds exact matches)
code_search("TODO: fix")
code_search("FIXME: memory leak")


Returns XML-formatted results optimized for LLM consumption.

Search Strategy Selection

The tool automatically selects the best strategy:

Query Type	Strategy	Example
class Foo	AST	Structural definition search
def foo()	AST	Function signature search
Questions	Vector	Semantic/conceptual search
TODO, FIXME	Grep	Exact text match
Workflow
1. SEARCH
   code_search("...")  # Unified entry point
   ↓
2. INTERPRET XML RESULTS
   - <item> for focused results
   - <search_interaction> for refinement suggestions
   ↓
3. REFINE (if needed)
   code_search("class ClassName")  # More specific
   ↓
4. READ FILE (for implementation details)
   read_file("path/to/file.py")

Best Practices
Always use code_search for all code discovery tasks
Be specific: code_search("class UserAuth") > code_search("auth")
Check XML guidance: If results are too broad, the XML will suggest refinements
Read files for details: Use read_file after finding the right file
Search Engines
Engine	Use Case	Examples
AST	Class/function definitions	class Foo, def bar
Vector	Conceptual queries	"how does auth work"
Grep	Exact text	TODO, "error message"
Weekly Installs
16
Repository
tao3k/omni-dev-fusion
GitHub Stars
9
First Seen
Jan 24, 2026