---
rating: ⭐⭐⭐
title: pydantic-evals
url: https://skills.sh/fuenfgeld/pydantic-ai-skills/pydantic-evals
---

# pydantic-evals

skills/fuenfgeld/pydantic-ai-skills/pydantic-evals
pydantic-evals
Installation
$ npx skills add https://github.com/fuenfgeld/pydantic-ai-skills --skill pydantic-evals
SKILL.md
Pydantic Evals
Overview

Pydantic Evals provides rigorous testing and evaluation for AI agents and LLM outputs using a code-first approach with Pydantic models. It enables "Evaluation-Driven Development" (EDD) where evaluation suites live alongside application code, subject to version control and CI/CD.

Core Concepts

Understand these key primitives:

Case

A single test scenario with inputs, optional expected output, and metadata.

from pydantic_evals import Case

case = Case(
    name="refund_request",
    inputs="What is your refund policy?",
    expected_output="30 days full refund",
    metadata={"category": "policy"}
)

Dataset

Collection of Cases with default evaluators. Generic over input/output types.

from pydantic_evals import Dataset

dataset = Dataset(
    cases=[case1, case2, case3],
    evaluators=[evaluator1, evaluator2]
)

Evaluator

Logic engine that assesses outputs. Returns bool (Pass/Fail), float/int (score), or str (label).

Experiment

Point-in-time performance capture when Dataset runs against a Task.

For detailed explanations, see references/core-concepts.md

Quick Start

Create and run a simple evaluation:

from pydantic_evals import Case, Dataset
from pydantic_evals.evaluators import Contains, LLMJudge

# Define cases
cases = [
    Case(
        name="greeting",
        inputs="Hello, who are you?",
        expected_output="I am an AI assistant."
    )
]

# Define evaluators
evaluators = [
    Contains(value="AI assistant"),
    LLMJudge(rubric="Is this response polite? Answer PASS or FAIL.")
]

# Create dataset
dataset = Dataset(cases=cases, evaluators=evaluators)

# Run evaluation
async def my_agent(query: str) -> str:
    # Your agent logic here
    return "I am an AI assistant."

report = dataset.evaluate_sync(my_agent)
report.print()

Evaluator Types

Pydantic Evals supports a "Pyramid of Evaluation" from fast/cheap to slow/expensive:

1. Deterministic Evaluators

Fast, free, code-based checks. Use as first line of defense.

Equals: Exact equality check
EqualsExpected: Compare to Case.expected_output
Contains: Substring/item presence
IsInstance: Type validation
MaxDuration: Latency SLA enforcement

Strategy: Always run deterministic checks before expensive LLM judges.

2. LLM-as-a-Judge

Use secondary LLM to score outputs based on natural language rubrics.

from pydantic_evals.evaluators import LLMJudge

judge = LLMJudge(
    rubric="Response must: 1) Answer the question, 2) Cite context, 3) Be professional",
    include_input=True,
    include_expected_output=True,
    model='openai:gpt-4o'
)


Using OpenRouter for LLMJudge:

from pydantic_evals.evaluators.llm_as_a_judge import set_default_judge_model
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

# Configure OpenRouter as judge model
provider = OpenAIProvider(
    api_key=os.getenv('OPENROUTER_API_KEY'),
    base_url='https://openrouter.ai/api/v1'
)
model = OpenAIChatModel(model_name='gpt-4o-mini', provider=provider)
set_default_judge_model(model)

# Or pass model directly to LLMJudge
judge = LLMJudge(rubric="Is this polite?", model=model)


Rubric best practices: Be specific and actionable, not vague.

3. Custom Evaluators

Implement arbitrary logic by inheriting from Evaluator.

from dataclasses import dataclass
from pydantic_evals.evaluators import Evaluator, EvaluatorContext

@dataclass
class ValidSQL(Evaluator):
    def evaluate(self, ctx: EvaluatorContext) -> bool:
        import sqlparse
        try:
            parsed = sqlparse.parse(ctx.output)
            return len(parsed) > 0
        except:
            return False

Custom Evaluators for Structured Output (Pydantic Models)

Important: Built-in evaluators like Contains, Equals work with strings/lists/dicts. They do NOT work with Pydantic model outputs. For agents with output_type=MyModel, create custom evaluators:

from dataclasses import dataclass
from pydantic_evals.evaluators import Evaluator, EvaluatorContext
from pydantic import BaseModel

class MyAgentResponse(BaseModel):
    message: str
    status: str
    complete: bool

@dataclass
class HasNonEmptyMessage(Evaluator[MyAgentResponse, None]):
    """Check that response has a non-empty message field."""
    min_length: int = 1

    def evaluate(self, ctx: EvaluatorContext[MyAgentResponse, None]) -> bool:
        if not isinstance(ctx.output, MyAgentResponse):
            return False
        return len(ctx.output.message) >= self.min_length

@dataclass
class StatusIsValid(Evaluator[MyAgentResponse, None]):
    """Check that status is one of allowed values."""
    allowed_values: tuple = ("pending", "complete", "error")

    def evaluate(self, ctx: EvaluatorContext[MyAgentResponse, None]) -> bool:
        return ctx.output.status in self.allowed_values

# Usage
evaluators = [
    IsInstance(type_name="MyAgentResponse"),  # Check type first
    HasNonEmptyMessage(min_length=10),
    StatusIsValid(),
]

4. Span-Based Evaluation

Inspect execution traces to verify internal agent behavior (tool calls, retrieval steps).

from pydantic_evals.evaluators import HasMatchingSpan
from pydantic_evals.otel import SpanQuery

# Verify agent called a specific tool
# NOTE: HasMatchingSpan takes a query parameter with SpanQuery
tool_check = HasMatchingSpan(
    query=SpanQuery(
        name_equals='running tool',
        has_attributes={'gen_ai.tool.name': 'calculator'}
    )
)


For detailed guide, see references/evaluator-types.md

Integration with Pydantic AI
Define Agent as Task

Wrap agent execution in a task function:

from pydantic_ai import Agent

agent = Agent('openai:gpt-4o-mini', system_prompt="You are helpful.")

async def run_agent(query: str) -> str:
    result = await agent.run(query)
    return result.output  # Use result.output, NOT result.data

Handle Dependencies

Use dependency injection for deterministic testing:

from dataclasses import dataclass

@dataclass
class Deps:
    api_key: str

# During testing, override with mocks
test_deps = Deps(api_key="test_key")


For integration guide, see references/integration.md

Logfire Observability

Enable automatic tracing for debugging:

import logfire

logfire.configure(send_to_logfire='if-token-present')
logfire.instrument_pydantic_ai()

# Evaluations now create rich traces viewable in Logfire dashboard


Benefits:

Trace every evaluation run
Visualize agent internal execution
Compare experiments side-by-side
Debug failures with full context
Dataset Management
Save/Load Datasets
# Save to YAML with schema
dataset.to_file('evals.yaml', fmt='yaml')

# Load from file
dataset = Dataset.from_file('evals.yaml')


Important: Use typed Dataset for proper serialization:

# Define typed dataset to avoid serialization warnings
dataset: Dataset[str, str, None] = Dataset(...)

# Or when loading from file with custom evaluators
from types import NoneType
dataset = Dataset[MyInputType, MyOutputType, NoneType].from_file(
    'evals.yaml',
    custom_evaluator_types=(MyCustomEvaluator,)
)

Generate Datasets with LLM
from pydantic_evals.generation import generate_dataset

dataset = await generate_dataset(
    dataset_type=Dataset[str, str, None],
    model='openai:o1',
    n_examples=10,
    extra_instructions="Generate diverse test cases for customer support agent"
)

Best Practices
Fail-fast: Run deterministic evaluators before LLM judges
Cost-latency trade-off:
Commit hooks: Deterministic only
PR merges: Small LLM judges on critical cases
Nightly builds: Full LLM judge suite
Concurrency: Use max_concurrency parameter to avoid rate limits
Versioning: Store datasets in Git alongside code
Regression testing: Compare experiments to detect degradation
Common Workflows
Workflow 1: Create Evaluation Suite
Define Cases with inputs and expected outputs
Choose evaluators based on requirements
Create Dataset with cases and evaluators
Save to YAML for version control
Workflow 2: Run Evaluations
Load Dataset from file
Define task function (agent wrapper)
Run dataset.evaluate_sync(task) or dataset.evaluate(task)
Analyze report with report.print() or Logfire

Accessing Results:

report = dataset.evaluate_sync(my_task)
report.print()

# Access individual case results
for case in report.cases:  # NOTE: Use .cases, NOT .case_results
    print(f"Case: {case.name}")
    print(f"Output: {case.output}")
    print(f"Passed: {case.passed}")

Workflow 3: Compare Models
Run same dataset against different models
Generate Experiments for each run
Compare metrics (pass rates, latency, scores)
Use Logfire comparison view
Examples

Complete example files demonstrating patterns:

references/examples/generate_dataset.py: Generate test cases with LLM
references/examples/custom_evaluators.py: Implement custom evaluation logic
references/examples/unit_testing.py: Run evaluations in CI/CD
references/examples/compare_models.py: Benchmark different models
Resources
references/
core-concepts.md: Detailed explanation of Case, Dataset, Evaluator, Experiment
evaluator-types.md: Deep dive into all evaluator types
integration.md: Pydantic AI and Logfire integration guide
examples/: Complete working examples
Weekly Installs
9
Repository
fuenfgeld/pydan…i-skills
GitHub Stars
7
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn