---
rating: ⭐⭐⭐
title: development-assistant
url: https://skills.sh/robthepcguy/claude-patent-creator/development-assistant
---

# development-assistant

skills/robthepcguy/claude-patent-creator/development-assistant
development-assistant
Installation
$ npx skills add https://github.com/robthepcguy/claude-patent-creator --skill development-assistant
SKILL.md
Development Assistant Skill

Expert system for developing and extending the Claude Patent Creator. Guides through adding new MCP tools, analyzers, configuration options, and features while following best practices and existing patterns.

When to Use This Skill

Activate when adding MCP tools, analyzers, configuration options, BigQuery queries, slash commands, or implementing performance optimizations.

Development Workflow
Feature Request -> Planning -> Implementation (Code + Validation + Monitoring + Tests) -> Testing -> Documentation -> Integration

Adding New MCP Tools

Quick Start:

Define inputs, outputs, dependencies
Create Pydantic model in mcp_server/validation.py
Add tool function in mcp_server/server.py with decorators
Create test script in scripts/
Update CLAUDE.md

Key Decorators:

@mcp.tool()                    # Register as MCP tool
@validate_input(YourInput)     # Pydantic validation
@track_performance             # Performance monitoring


Template:

def your_tool(param: str, optional: int = 10) -> dict:
    """Comprehensive docstring (Claude sees this).

    Args:
        param: Description
        optional: Description with default

    Returns:
        Dictionary containing: key1, key2, key3
    """
    # Implementation
    return {"result": "data"}

Adding New Analyzers

Overview: Analyzers inherit from BaseAnalyzer and check USPTO compliance.

Minimal Example:

from mcp_server.analyzer_base import BaseAnalyzer

class YourAnalyzer(BaseAnalyzer):
    def __init__(self):
        super().__init__()
        self.mpep_sections = ["608", "2173"]

    def analyze(self, content: str) -> dict:
        issues = []
        if violation:
            issues.append({
                "type": "violation_name",
                "severity": "critical",
                "mpep_citation": "MPEP 608",
                "recommendation": "Fix description"
            })
        return {"compliant": len(issues) == 0, "issues": issues}

Adding Configuration Options

Use Pydantic settings in mcp_server/config.py:

# In config.py
class AppSettings(BaseSettings):
    enable_feature_x: bool = Field(default=False, description="Enable X")

# In your code
from mcp_server.config import get_settings
if get_settings().enable_feature_x:
    # Feature enabled

Adding Performance Monitoring
@track_performance
def your_function(data):
    with OperationTimer("step1"):
        result1 = step1(data)
    with OperationTimer("step2"):
        result2 = step2(result1)
    return result2

Modifying RAG Search Pipeline

Pipeline: Query -> HyDE -> Vector+BM25 -> RRF -> Reranking -> Results

Customization Points: Query expansion, custom scoring, filtering, reranking strategies

Adding New Slash Commands
Create .claude/commands/your-command.md
Add frontmatter: description, model
Write workflow instructions
Restart Claude Code

Template:

---
description: Brief command description
model: claude-sonnet-4-5-20250929
---

# Command Name

## When to Use
- Use case 1

## How It Works
Step 1: ...

Development Best Practices
Follow existing patterns
Use type hints
Write docstrings (Google style)
Handle errors gracefully
Validate inputs (Pydantic)
Log operations
Monitor performance
Common Development Tasks

Add BigQuery Query: Add method in mcp_server/bigquery_search.py

Add Validation Rule:

class YourInput(BaseModel):
    field: str

    @field_validator("field")
    @classmethod
    def validate_field(cls, v):
        if not meets_requirement(v):
            raise ValueError("Error message")
        return v


Add Logging:

from mcp_server.logging_config import get_logger
logger = get_logger()
logger.info("event_name", extra={"context": "data"})

Quick Reference: File Locations
Task	Primary File	Related Files
Add MCP tool	mcp_server/server.py	mcp_server/validation.py
Add analyzer	mcp_server/your_analyzer.py	mcp_server/analyzer_base.py
Add config	mcp_server/config.py	.env, CLAUDE.md
Add BigQuery query	mcp_server/bigquery_search.py	-
Add test	scripts/test_your_feature.py	-
Key Patterns

MCP Tool Pattern:

@mcp.tool()
@validate_input(InputModel)
@track_performance
def tool_name(param: type) -> dict:
    """Docstring visible to Claude."""
    from module import Component
    if invalid:
        return {"error": "message"}
    result = process(param)
    return {"key": "value"}


Analyzer Pattern:

class YourAnalyzer(BaseAnalyzer):
    def analyze(self, content: str) -> dict:
        issues = []
        issues.extend(self._check_x(content))
        return {
            "compliant": len(issues) == 0,
            "issues": issues,
            "recommendations": self._generate_recommendations(issues)
        }

Weekly Installs
21
Repository
robthepcguy/cla…-creator
GitHub Stars
97
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass