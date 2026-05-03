---
title: temporal-python-testing
url: https://skills.sh/wshobson/agents/temporal-python-testing
---

# temporal-python-testing

skills/wshobson/agents/temporal-python-testing
temporal-python-testing
Installation
$ npx skills add https://github.com/wshobson/agents --skill temporal-python-testing
Summary

Pytest-based testing strategies for Temporal workflows with time-skipping, mocking, and replay validation.

Covers unit testing (WorkflowEnvironment with time-skipping), integration testing (mocked activities), and replay testing for determinism validation
Time-skipping enables month-long workflows to execute in seconds; ActivityEnvironment isolates activity logic for fast feedback
Includes progressive disclosure resources for unit testing, integration testing, replay testing, and local Temporal server setup
Recommends ≥80% coverage targets and provides pytest fixtures, error injection patterns, and CI/CD integration guidance
SKILL.md
Temporal Python Testing Strategies

Comprehensive testing approaches for Temporal workflows using pytest, progressive disclosure resources for specific testing scenarios.

When to Use This Skill
Unit testing workflows - Fast tests with time-skipping
Integration testing - Workflows with mocked activities
Replay testing - Validate determinism against production histories
Local development - Set up Temporal server and pytest
CI/CD integration - Automated testing pipelines
Coverage strategies - Achieve ≥80% test coverage
Testing Philosophy

Recommended Approach (Source: docs.temporal.io/develop/python/testing-suite):

Write majority as integration tests
Use pytest with async fixtures
Time-skipping enables fast feedback (month-long workflows → seconds)
Mock activities to isolate workflow logic
Validate determinism with replay testing

Three Test Types:

Unit: Workflows with time-skipping, activities with ActivityEnvironment
Integration: Workers with mocked activities
End-to-end: Full Temporal server with real activities (use sparingly)
Available Resources

This skill provides detailed guidance through progressive disclosure. Load specific resources based on your testing needs:

Unit Testing Resources

File: resources/unit-testing.md When to load: Testing individual workflows or activities in isolation Contains:

WorkflowEnvironment with time-skipping
ActivityEnvironment for activity testing
Fast execution of long-running workflows
Manual time advancement patterns
pytest fixtures and patterns
Integration Testing Resources

File: resources/integration-testing.md When to load: Testing workflows with mocked external dependencies Contains:

Activity mocking strategies
Error injection patterns
Multi-activity workflow testing
Signal and query testing
Coverage strategies
Replay Testing Resources

File: resources/replay-testing.md When to load: Validating determinism or deploying workflow changes Contains:

Determinism validation
Production history replay
CI/CD integration patterns
Version compatibility testing
Local Development Resources

File: resources/local-setup.md When to load: Setting up development environment Contains:

Docker Compose configuration
pytest setup and configuration
Coverage tool integration
Development workflow
Quick Start Guide
Basic Workflow Test
import pytest
from temporalio.testing import WorkflowEnvironment
from temporalio.worker import Worker

@pytest.fixture
async def workflow_env():
    env = await WorkflowEnvironment.start_time_skipping()
    yield env
    await env.shutdown()

@pytest.mark.asyncio
async def test_workflow(workflow_env):
    async with Worker(
        workflow_env.client,
        task_queue="test-queue",
        workflows=[YourWorkflow],
        activities=[your_activity],
    ):
        result = await workflow_env.client.execute_workflow(
            YourWorkflow.run,
            args,
            id="test-wf-id",
            task_queue="test-queue",
        )
        assert result == expected

Basic Activity Test
from temporalio.testing import ActivityEnvironment

async def test_activity():
    env = ActivityEnvironment()
    result = await env.run(your_activity, "test-input")
    assert result == expected_output

Coverage Targets

Recommended Coverage (Source: docs.temporal.io best practices):

Workflows: ≥80% logic coverage
Activities: ≥80% logic coverage
Integration: Critical paths with mocked activities
Replay: All workflow versions before deployment
Key Testing Principles
Time-Skipping - Month-long workflows test in seconds
Mock Activities - Isolate workflow logic from external dependencies
Replay Testing - Validate determinism before deployment
High Coverage - ≥80% target for production workflows
Fast Feedback - Unit tests run in milliseconds
How to Use Resources

Load specific resource when needed:

"Show me unit testing patterns" → Load resources/unit-testing.md
"How do I mock activities?" → Load resources/integration-testing.md
"Setup local Temporal server" → Load resources/local-setup.md
"Validate determinism" → Load resources/replay-testing.md
Additional References
Python SDK Testing: docs.temporal.io/develop/python/testing-suite
Testing Patterns: github.com/temporalio/temporal/blob/main/docs/development/testing.md
Python Samples: github.com/temporalio/samples-python
Weekly Installs
5.8K
Repository
wshobson/agents
GitHub Stars
34.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn