---
title: sequential-thinking
url: https://skills.sh/mrgoonie/claudekit-skills/sequential-thinking
---

# sequential-thinking

skills/mrgoonie/claudekit-skills/sequential-thinking
sequential-thinking
Installation
$ npx skills add https://github.com/mrgoonie/claudekit-skills --skill sequential-thinking
Summary

Structured problem-solving through iterative reasoning with revision and branching capabilities.

Break complex problems into sequential thought steps with dynamic scope adjustment as understanding evolves
Revise previous conclusions and explore alternative reasoning paths from any point in the analysis
Maintains full reasoning chain context throughout multi-stage analysis, design planning, or problem decomposition
Ideal for tasks with initially unclear scope, interconnected reasoning requirements, or situations requiring backtracking
SKILL.md
Sequential Thinking

Enables structured problem-solving through iterative reasoning with revision and branching capabilities.

Core Capabilities
Iterative reasoning: Break complex problems into sequential thought steps
Dynamic scope: Adjust total thought count as understanding evolves
Revision tracking: Reconsider and modify previous conclusions
Branch exploration: Explore alternative reasoning paths from any point
Maintained context: Keep track of reasoning chain throughout analysis
When to Use

Use mcp__reasoning__sequentialthinking when:

Problem requires multiple interconnected reasoning steps
Initial scope or approach is uncertain
Need to filter through complexity to find core issues
May need to backtrack or revise earlier conclusions
Want to explore alternative solution paths

Don't use for: Simple queries, direct facts, or single-step tasks.

Basic Usage

The MCP tool mcp__reasoning__sequentialthinking accepts these parameters:

Required Parameters
thought (string): Current reasoning step
nextThoughtNeeded (boolean): Whether more reasoning is needed
thoughtNumber (integer): Current step number (starts at 1)
totalThoughts (integer): Estimated total steps needed
Optional Parameters
isRevision (boolean): Indicates this revises previous thinking
revisesThought (integer): Which thought number is being reconsidered
branchFromThought (integer): Thought number to branch from
branchId (string): Identifier for this reasoning branch
Workflow Pattern
1. Start with initial thought (thoughtNumber: 1)
2. For each step:
   - Express current reasoning in `thought`
   - Estimate remaining work via `totalThoughts` (adjust dynamically)
   - Set `nextThoughtNeeded: true` to continue
3. When reaching conclusion, set `nextThoughtNeeded: false`

Simple Example
// First thought
{
  thought: "Problem involves optimizing database queries. Need to identify bottlenecks first.",
  thoughtNumber: 1,
  totalThoughts: 5,
  nextThoughtNeeded: true
}

// Second thought
{
  thought: "Analyzing query patterns reveals N+1 problem in user fetches.",
  thoughtNumber: 2,
  totalThoughts: 6, // Adjusted scope
  nextThoughtNeeded: true
}

// ... continue until done

Advanced Features

For revision patterns, branching strategies, and complex workflows, see:

Advanced Usage - Revision and branching patterns
Examples - Real-world use cases
Tips
Start with rough estimate for totalThoughts, refine as you progress
Use revision when assumptions prove incorrect
Branch when multiple approaches seem viable
Express uncertainty explicitly in thoughts
Adjust scope freely - accuracy matters less than progress visibility
Weekly Installs
1.0K
Repository
mrgoonie/claude…t-skills
GitHub Stars
2.0K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass