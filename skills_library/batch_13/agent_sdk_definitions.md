---
title: agent-sdk-definitions
url: https://skills.sh/mgd34msu/goodvibes-plugin/agent-sdk-definitions
---

# agent-sdk-definitions

skills/mgd34msu/goodvibes-plugin/agent-sdk-definitions
agent-sdk-definitions
Installation
$ npx skills add https://github.com/mgd34msu/goodvibes-plugin --skill agent-sdk-definitions
SKILL.md
Agent SDK Definitions

For SDK-based applications, agents can be defined programmatically instead of as markdown files.

TypeScript Definition
import { query, ClaudeAgentOptions, AgentDefinition } from "@anthropic-ai/claude-agent-sdk";

const options: ClaudeAgentOptions = {
  // Parent agent needs Task tool to invoke subagents
  allowed_tools: ["Read", "Grep", "Glob", "Edit", "Write", "Bash", "Task"],

  agents: {
    "code-reviewer": {
      description: "Security-focused code reviewer. Use PROACTIVELY for auth code.",
      prompt: `You are a security code reviewer specializing in authentication
and authorization code. You identify vulnerabilities, suggest fixes,
and ensure best practices are followed.

## Focus Areas
- Authentication flows
- Session management
- Input validation
- Access control

## Output Format
Provide findings as:
1. Severity (Critical/High/Medium/Low)
2. Location (file:line)
3. Issue description
4. Recommended fix`,
      tools: ["Read", "Grep", "Glob"],  // Read-only access
      model: "opus"
    },

    "test-runner": {
      description: "Runs tests and analyzes failures. Use when tests need to be executed.",
      prompt: `You run test suites and analyze failures. You identify root causes
and suggest fixes for failing tests.`,
      // Omit tools to inherit all from parent
      model: "sonnet"
    }
  }
};

// Execute with agents
for await (const message of query({
  prompt: "Review the authentication module for security issues",
  options
})) {
  console.log(message);
}

Python Definition
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition

options = ClaudeAgentOptions(
    allowed_tools=["Read", "Grep", "Glob", "Edit", "Write", "Bash", "Task"],

    agents={
        "code-reviewer": AgentDefinition(
            description="Security-focused code reviewer. Use PROACTIVELY for auth code.",
            prompt="""You are a security code reviewer specializing in authentication
and authorization code. You identify vulnerabilities, suggest fixes,
and ensure best practices are followed.

## Focus Areas
- Authentication flows
- Session management
- Input validation
- Access control""",
            tools=["Read", "Grep", "Glob"],
            model="opus"
        ),

        "test-runner": AgentDefinition(
            description="Runs tests and analyzes failures. Use when tests need to be executed.",
            prompt="You run test suites and analyze failures.",
            # tools omitted = inherit all
            model="sonnet"
        )
    }
)

async def main():
    async for message in query(
        prompt="Review the authentication module",
        options=options
    ):
        print(message)

asyncio.run(main())

AgentDefinition Schema
type AgentDefinition = {
  description: string;   // Required: When to invoke (routing key)
  prompt: string;        // Required: System prompt content
  tools?: string[];      // Optional: Allowed tools (omit = inherit all)
  model?: 'sonnet' | 'opus' | 'haiku' | 'inherit';  // Optional: Model override
}

Key Differences from Filesystem Agents
Aspect	Filesystem (.claude/agents/)	SDK (programmatic)
Format	Markdown with YAML frontmatter	TypeScript/Python objects
Loading	Automatic from directory	Passed in options
Prompt	Markdown body	String in prompt field
Use case	Claude Code CLI	Custom SDK applications
When to Use SDK Format
Building custom agent harnesses
Programmatic agent orchestration
Dynamic agent creation at runtime
CI/CD pipelines with agent tasks
Applications embedding Claude agents
Providing Both Formats

When a user may use either approach, provide both:

Markdown file for .claude/agents/{name}.md
SDK definition for programmatic use

This ensures compatibility with both Claude Code CLI and custom SDK applications.

Weekly Installs
15
Repository
mgd34msu/goodvi…s-plugin
GitHub Stars
6
First Seen
Jan 21, 2026