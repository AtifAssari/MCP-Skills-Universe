---
rating: ⭐⭐⭐
title: dspy-custom-module-design
url: https://skills.sh/omidzamani/dspy-skills/dspy-custom-module-design
---

# dspy-custom-module-design

skills/omidzamani/dspy-skills/dspy-custom-module-design
dspy-custom-module-design
Installation
$ npx skills add https://github.com/omidzamani/dspy-skills --skill dspy-custom-module-design
SKILL.md
DSPy Custom Module Design
Goal

Design production-quality custom DSPy modules with proper architecture, state management, serialization, and testing patterns.

When to Use
Building reusable DSPy components
Complex logic beyond built-in modules
Need custom state management
Sharing modules across projects
Production deployment requirements
Related Skills
Module composition: dspy-advanced-module-composition
Signature design: dspy-signature-designer
Optimization: dspy-miprov2-optimizer
Inputs
Input	Type	Description
task_description	str	What the module should do
components	list	Sub-modules or predictors
state	dict	Stateful attributes
Outputs
Output	Type	Description
custom_module	dspy.Module	Production-ready module
Workflow
Phase 1: Basic Module Structure

All custom modules inherit from dspy.Module:

import dspy

class BasicQA(dspy.Module):
    """Simple question answering module."""

    def __init__(self):
        super().__init__()
        self.predictor = dspy.Predict("question -> answer")

    def forward(self, question):
        """Entry point for module execution."""
        return self.predictor(question=question)

# Usage
dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"))
qa = BasicQA()
result = qa(question="What is Python?")
print(result.answer)

Phase 2: Stateful Modules

Modules can maintain state across calls:

import dspy
import logging

logger = logging.getLogger(__name__)

class StatefulRAG(dspy.Module):
    """RAG with query caching."""

    def __init__(self, cache_size=100):
        super().__init__()
        self.retrieve = dspy.Retrieve(k=3)
        self.generate = dspy.ChainOfThought("context, question -> answer")
        self.cache = {}
        self.cache_size = cache_size

    def forward(self, question):
        # Check cache
        if question in self.cache:
            return self.cache[question]

        # Retrieve and generate
        passages = self.retrieve(question).passages
        result = self.generate(context=passages, question=question)

        # Update cache with size limit
        if len(self.cache) >= self.cache_size:
            self.cache.pop(next(iter(self.cache)))
        self.cache[question] = result

        return result

Phase 3: Error Handling and Validation

Production modules need robust error handling:

import dspy
from typing import Optional
import logging

logger = logging.getLogger(__name__)

class RobustClassifier(dspy.Module):
    """Classifier with validation."""

    def __init__(self, valid_labels: list[str]):
        super().__init__()
        self.valid_labels = set(valid_labels)
        self.classify = dspy.Predict("text -> label: str, confidence: float")

    def forward(self, text: str) -> dspy.Prediction:
        if not text or not text.strip():
            return dspy.Prediction(label="unknown", confidence=0.0, error="Empty input")

        try:
            result = self.classify(text=text)

            # Validate label
            if result.label not in self.valid_labels:
                result.label = "unknown"
                result.confidence = 0.0

            return result

        except Exception as e:
            logger.error(f"Classification failed: {e}")
            return dspy.Prediction(label="unknown", confidence=0.0, error=str(e))

Phase 4: Serialization

Modules support save/load:

import dspy

# Save module state
module = MyCustomModule()
module.save("my_module.json")

# Load requires creating instance first, then loading state
loaded = MyCustomModule()
loaded.load("my_module.json")

# For loading entire programs (dspy>=2.6.0)
module.save("./my_module/", save_program=True)
loaded = dspy.load("./my_module/")

Production Example
import dspy
from typing import List, Optional
import logging

logger = logging.getLogger(__name__)

class ProductionRAG(dspy.Module):
    """Production-ready RAG with all best practices."""

    def __init__(
        self,
        retriever_k: int = 5,
        cache_enabled: bool = True,
        cache_size: int = 1000
    ):
        super().__init__()

        # Configuration
        self.retriever_k = retriever_k
        self.cache_enabled = cache_enabled
        self.cache_size = cache_size

        # Components
        self.retrieve = dspy.Retrieve(k=retriever_k)
        self.generate = dspy.ChainOfThought("context, question -> answer")

        # State
        self.cache = {} if cache_enabled else None
        self.call_count = 0

    def forward(self, question: str) -> dspy.Prediction:
        """Execute RAG pipeline with caching."""
        self.call_count += 1

        # Validation
        if not question or not question.strip():
            return dspy.Prediction(
                answer="Please provide a valid question.",
                error="Invalid input"
            )

        # Cache check
        if self.cache_enabled and question in self.cache:
            logger.info(f"Cache hit (call #{self.call_count})")
            return self.cache[question]

        # Execute pipeline
        try:
            passages = self.retrieve(question).passages

            if not passages:
                logger.warning("No passages retrieved")
                return dspy.Prediction(
                    answer="No relevant information found.",
                    passages=[]
                )

            result = self.generate(context=passages, question=question)
            result.passages = passages

            # Update cache
            if self.cache_enabled:
                self._update_cache(question, result)

            return result

        except Exception as e:
            logger.error(f"RAG execution failed: {e}")
            return dspy.Prediction(
                answer="An error occurred while processing your question.",
                error=str(e)
            )

    def _update_cache(self, key: str, value: dspy.Prediction):
        """Manage cache with size limit."""
        if len(self.cache) >= self.cache_size:
            self.cache.pop(next(iter(self.cache)))
        self.cache[key] = value

    def clear_cache(self):
        """Clear cache."""
        if self.cache_enabled:
            self.cache.clear()

Best Practices
Single responsibility - Each module does one thing well
Validate inputs - Check for None, empty strings, invalid types
Handle errors - Return Predictions with error fields, never raise
Log important events - Cache hits, errors, validation failures
Test independently - Unit test modules before composition
Limitations
State increases memory usage (careful with large caches)
Serialization doesn't automatically save custom state
Module testing requires mocking LM calls
Deep module hierarchies can be hard to debug
Performance overhead from validation in hot paths
Official Documentation
DSPy Documentation: https://dspy.ai/
DSPy GitHub: https://github.com/stanfordnlp/dspy
Custom Modules Guide: https://dspy.ai/tutorials/custom_module/
Module API: https://dspy.ai/api/modules/
Weekly Installs
22
Repository
omidzamani/dspy-skills
GitHub Stars
74
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass