---
rating: ⭐⭐⭐
title: python:temporal
url: https://skills.sh/martinffx/claude-code-atelier/python:temporal
---

# python:temporal

skills/martinffx/claude-code-atelier/python:temporal
python:temporal
Installation
$ npx skills add https://github.com/martinffx/claude-code-atelier --skill python:temporal
SKILL.md
Temporal Workflow Orchestration

Temporal SDK patterns for building durable, distributed workflows in Python.

Worker Setup
from temporalio.client import Client
from temporalio.worker import Worker

async def main():
    client = await Client.connect("localhost:7233")

    worker = Worker(
        client,
        task_queue="my-task-queue",
        workflows=[MyWorkflow],
        activities=[my_activity],
    )

    await worker.run()

Workflow Definition
from temporalio import workflow
from datetime import timedelta

@workflow.defn
class MyWorkflow:
    @workflow.run
    async def run(self, name: str) -> str:
        """Workflow run method"""
        # Execute activity
        result = await workflow.execute_activity(
            my_activity,
            name,
            start_to_close_timeout=timedelta(seconds=30),
        )

        return f"Hello {result}"

Activity Implementation
from temporalio import activity

@activity.defn
async def my_activity(name: str) -> str:
    """Activity - can fail and retry"""
    # Do work (database, API, etc.)
    return name.upper()

Starting Workflows
from temporalio.client import Client

async def start_workflow():
    client = await Client.connect("localhost:7233")

    handle = await client.start_workflow(
        MyWorkflow.run,
        "World",
        id="my-workflow-id",
        task_queue="my-task-queue",
    )

    result = await handle.result()
    print(result)  # "Hello WORLD"

Error Handling
from temporalio.exceptions import ActivityError

@workflow.defn
class MyWorkflow:
    @workflow.run
    async def run(self) -> str:
        try:
            result = await workflow.execute_activity(
                risky_activity,
                start_to_close_timeout=timedelta(seconds=30),
                retry_policy=RetryPolicy(maximum_attempts=3),
            )
        except ActivityError as e:
            # Handle failure after retries exhausted
            return "Failed"

        return result

Signals and Queries
@workflow.defn
class OrderWorkflow:
    def __init__(self):
        self.status = "pending"

    @workflow.run
    async def run(self, order_id: str) -> str:
        await workflow.wait_condition(lambda: self.status == "approved")
        return "Order processed"

    @workflow.signal
    def approve(self):
        """Signal to approve order"""
        self.status = "approved"

    @workflow.query
    def get_status(self) -> str:
        """Query current status"""
        return self.status


See references/ for testing patterns and common workflow patterns.

Weekly Installs
9
Repository
martinffx/claud…-atelier
GitHub Stars
20
First Seen
Feb 16, 2026