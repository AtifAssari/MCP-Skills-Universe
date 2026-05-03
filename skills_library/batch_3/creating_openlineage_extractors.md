---
title: creating-openlineage-extractors
url: https://skills.sh/astronomer/agents/creating-openlineage-extractors
---

# creating-openlineage-extractors

skills/astronomer/agents/creating-openlineage-extractors
creating-openlineage-extractors
Installation
$ npx skills add https://github.com/astronomer/agents --skill creating-openlineage-extractors
Summary

Custom OpenLineage extractors for unsupported Airflow operators and complex lineage scenarios.

Two approaches: add OpenLineage methods directly to operators you own (recommended), or create custom extractors for third-party operators you cannot modify
Extractors intercept operator execution at three points: before execution for static lineage, after success for runtime-determined outputs, and optionally after failure for partial lineage
Register extractors via airflow.cfg or environment variable; on Astro, custom extractors are automatically picked up and lineage appears in the Lineage tab
Includes patterns for SQL operators, file transfers, and dynamic outputs determined at runtime; handle optional properties and avoid circular imports by importing inside methods
SKILL.md
Creating OpenLineage Extractors

This skill guides you through creating custom OpenLineage extractors to capture lineage from Airflow operators that don't have built-in support.

Reference: See the OpenLineage provider developer guide for the latest patterns and list of supported operators/hooks.

When to Use Each Approach
Scenario	Approach
Operator you own/maintain	OpenLineage Methods (recommended, simplest)
Third-party operator you can't modify	Custom Extractor
Need column-level lineage	OpenLineage Methods or Custom Extractor
Complex extraction logic	OpenLineage Methods or Custom Extractor
Simple table-level lineage	Inlets/Outlets (simplest, but lowest priority)

Important: Always prefer OpenLineage methods over custom extractors when possible. Extractors are harder to write, easier to diverge from operator behavior after changes, and harder to debug.

On Astro

Astro includes built-in OpenLineage integration — no additional transport configuration is needed. Lineage events are automatically collected and displayed in the Astro UI's Lineage tab. Custom extractors deployed to an Astro project are automatically picked up, so you only need to register them in airflow.cfg or via environment variable and deploy.

Two Approaches
1. OpenLineage Methods (Recommended)

Use when you can add methods directly to your custom operator. This is the go-to solution for operators you own.

2. Custom Extractors

Use when you need lineage from third-party or provider operators that you cannot modify.

Approach 1: OpenLineage Methods (Recommended)

When you own the operator, add OpenLineage methods directly:

from airflow.models import BaseOperator


class MyCustomOperator(BaseOperator):
    """Custom operator with built-in OpenLineage support."""

    def __init__(self, source_table: str, target_table: str, **kwargs):
        super().__init__(**kwargs)
        self.source_table = source_table
        self.target_table = target_table
        self._rows_processed = 0  # Set during execution

    def execute(self, context):
        # Do the actual work
        self._rows_processed = self._process_data()
        return self._rows_processed

    def get_openlineage_facets_on_start(self):
        """Called when task starts. Return known inputs/outputs."""
        # Import locally to avoid circular imports
        from openlineage.client.event_v2 import Dataset
        from airflow.providers.openlineage.extractors import OperatorLineage

        return OperatorLineage(
            inputs=[Dataset(namespace="postgres://db", name=self.source_table)],
            outputs=[Dataset(namespace="postgres://db", name=self.target_table)],
        )

    def get_openlineage_facets_on_complete(self, task_instance):
        """Called after success. Add runtime metadata."""
        from openlineage.client.event_v2 import Dataset
        from openlineage.client.facet_v2 import output_statistics_output_dataset
        from airflow.providers.openlineage.extractors import OperatorLineage

        return OperatorLineage(
            inputs=[Dataset(namespace="postgres://db", name=self.source_table)],
            outputs=[
                Dataset(
                    namespace="postgres://db",
                    name=self.target_table,
                    facets={
                        "outputStatistics": output_statistics_output_dataset.OutputStatisticsOutputDatasetFacet(
                            rowCount=self._rows_processed
                        )
                    },
                )
            ],
        )

    def get_openlineage_facets_on_failure(self, task_instance):
        """Called after failure. Optional - for partial lineage."""
        return None

OpenLineage Methods Reference
Method	When Called	Required
get_openlineage_facets_on_start()	Task enters RUNNING	No
get_openlineage_facets_on_complete(ti)	Task succeeds	No
get_openlineage_facets_on_failure(ti)	Task fails	No

Implement only the methods you need. Unimplemented methods fall through to Hook-Level Lineage or inlets/outlets.

Approach 2: Custom Extractors

Use this approach only when you cannot modify the operator (e.g., third-party or provider operators).

Basic Structure
from airflow.providers.openlineage.extractors.base import BaseExtractor, OperatorLineage
from openlineage.client.event_v2 import Dataset


class MyOperatorExtractor(BaseExtractor):
    """Extract lineage from MyCustomOperator."""

    @classmethod
    def get_operator_classnames(cls) -> list[str]:
        """Return operator class names this extractor handles."""
        return ["MyCustomOperator"]

    def _execute_extraction(self) -> OperatorLineage | None:
        """Called BEFORE operator executes. Use for known inputs/outputs."""
        # Access operator properties via self.operator
        source_table = self.operator.source_table
        target_table = self.operator.target_table

        return OperatorLineage(
            inputs=[
                Dataset(
                    namespace="postgres://mydb:5432",
                    name=f"public.{source_table}",
                )
            ],
            outputs=[
                Dataset(
                    namespace="postgres://mydb:5432",
                    name=f"public.{target_table}",
                )
            ],
        )

    def extract_on_complete(self, task_instance) -> OperatorLineage | None:
        """Called AFTER operator executes. Use for runtime-determined lineage."""
        # Access properties set during execution
        # Useful for operators that determine outputs at runtime
        return None

OperatorLineage Structure
from airflow.providers.openlineage.extractors.base import OperatorLineage
from openlineage.client.event_v2 import Dataset
from openlineage.client.facet_v2 import sql_job

lineage = OperatorLineage(
    inputs=[Dataset(namespace="...", name="...")],      # Input datasets
    outputs=[Dataset(namespace="...", name="...")],     # Output datasets
    run_facets={"sql": sql_job.SQLJobFacet(query="SELECT...")},  # Run metadata
    job_facets={},                                      # Job metadata
)

Extraction Methods
Method	When Called	Use For
_execute_extraction()	Before operator runs	Static/known lineage
extract_on_complete(task_instance)	After success	Runtime-determined lineage
extract_on_failure(task_instance)	After failure	Partial lineage on errors
Registering Extractors

Option 1: Configuration file (airflow.cfg)

[openlineage]
extractors = mypackage.extractors.MyOperatorExtractor;mypackage.extractors.AnotherExtractor


Option 2: Environment variable

AIRFLOW__OPENLINEAGE__EXTRACTORS='mypackage.extractors.MyOperatorExtractor;mypackage.extractors.AnotherExtractor'


Important: The path must be importable from the Airflow worker. Place extractors in your DAGs folder or installed package.

Common Patterns
SQL Operator Extractor
from airflow.providers.openlineage.extractors.base import BaseExtractor, OperatorLineage
from openlineage.client.event_v2 import Dataset
from openlineage.client.facet_v2 import sql_job


class MySqlOperatorExtractor(BaseExtractor):
    @classmethod
    def get_operator_classnames(cls) -> list[str]:
        return ["MySqlOperator"]

    def _execute_extraction(self) -> OperatorLineage | None:
        sql = self.operator.sql
        conn_id = self.operator.conn_id

        # Parse SQL to find tables (simplified example)
        # In practice, use a SQL parser like sqlglot
        inputs, outputs = self._parse_sql(sql)

        namespace = f"postgres://{conn_id}"

        return OperatorLineage(
            inputs=[Dataset(namespace=namespace, name=t) for t in inputs],
            outputs=[Dataset(namespace=namespace, name=t) for t in outputs],
            job_facets={
                "sql": sql_job.SQLJobFacet(query=sql)
            },
        )

    def _parse_sql(self, sql: str) -> tuple[list[str], list[str]]:
        """Parse SQL to extract table names. Use sqlglot for real parsing."""
        # Simplified example - use proper SQL parser in production
        inputs = []
        outputs = []
        # ... parsing logic ...
        return inputs, outputs

File Transfer Extractor
from airflow.providers.openlineage.extractors.base import BaseExtractor, OperatorLineage
from openlineage.client.event_v2 import Dataset


class S3ToSnowflakeExtractor(BaseExtractor):
    @classmethod
    def get_operator_classnames(cls) -> list[str]:
        return ["S3ToSnowflakeOperator"]

    def _execute_extraction(self) -> OperatorLineage | None:
        s3_bucket = self.operator.s3_bucket
        s3_key = self.operator.s3_key
        table = self.operator.table
        schema = self.operator.schema

        return OperatorLineage(
            inputs=[
                Dataset(
                    namespace=f"s3://{s3_bucket}",
                    name=s3_key,
                )
            ],
            outputs=[
                Dataset(
                    namespace="snowflake://myaccount.snowflakecomputing.com",
                    name=f"{schema}.{table}",
                )
            ],
        )

Dynamic Lineage from Execution
from openlineage.client.event_v2 import Dataset


class DynamicOutputExtractor(BaseExtractor):
    @classmethod
    def get_operator_classnames(cls) -> list[str]:
        return ["DynamicOutputOperator"]

    def _execute_extraction(self) -> OperatorLineage | None:
        # Only inputs known before execution
        return OperatorLineage(
            inputs=[Dataset(namespace="...", name=self.operator.source)],
        )

    def extract_on_complete(self, task_instance) -> OperatorLineage | None:
        # Outputs determined during execution
        # Access via operator properties set in execute()
        outputs = self.operator.created_tables  # Set during execute()

        return OperatorLineage(
            inputs=[Dataset(namespace="...", name=self.operator.source)],
            outputs=[Dataset(namespace="...", name=t) for t in outputs],
        )

Common Pitfalls
1. Circular Imports

Problem: Importing Airflow modules at the top level causes circular imports.

# ❌ BAD - can cause circular import issues
from airflow.models import TaskInstance
from openlineage.client.event_v2 import Dataset

class MyExtractor(BaseExtractor):
    ...

# ✅ GOOD - import inside methods
class MyExtractor(BaseExtractor):
    def _execute_extraction(self):
        from openlineage.client.event_v2 import Dataset
        # ...

2. Wrong Import Path

Problem: Extractor path doesn't match actual module location.

# ❌ Wrong - path doesn't exist
AIRFLOW__OPENLINEAGE__EXTRACTORS='extractors.MyExtractor'

# ✅ Correct - full importable path
AIRFLOW__OPENLINEAGE__EXTRACTORS='dags.extractors.my_extractor.MyExtractor'

3. Not Handling None

Problem: Extraction fails when operator properties are None.

# ✅ Handle optional properties
def _execute_extraction(self) -> OperatorLineage | None:
    if not self.operator.source_table:
        return None  # Skip extraction

    return OperatorLineage(...)

Testing Extractors
Unit Testing
import pytest
from unittest.mock import MagicMock
from mypackage.extractors import MyOperatorExtractor


def test_extractor():
    # Mock the operator
    operator = MagicMock()
    operator.source_table = "input_table"
    operator.target_table = "output_table"

    # Create extractor
    extractor = MyOperatorExtractor(operator)

    # Test extraction
    lineage = extractor._execute_extraction()

    assert len(lineage.inputs) == 1
    assert lineage.inputs[0].name == "input_table"
    assert len(lineage.outputs) == 1
    assert lineage.outputs[0].name == "output_table"

Precedence Rules

OpenLineage checks for lineage in this order:

Custom Extractors (highest priority)
OpenLineage Methods on operator
Hook-Level Lineage (from HookLineageCollector)
Inlets/Outlets (lowest priority)

If a custom extractor exists, it overrides built-in extraction and inlets/outlets.

Related Skills
annotating-task-lineage: For simple table-level lineage with inlets/outlets
tracing-upstream-lineage: Investigate data origins
tracing-downstream-lineage: Investigate data dependencies
Weekly Installs
559
Repository
astronomer/agents
GitHub Stars
354
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass