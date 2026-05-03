---
title: doc-pipeline
url: https://skills.sh/claude-office-skills/skills/doc-pipeline
---

# doc-pipeline

skills/claude-office-skills/skills/doc-pipeline
doc-pipeline
Installation
$ npx skills add https://github.com/claude-office-skills/skills --skill doc-pipeline
SKILL.md
Doc Pipeline Skill
Overview

This skill enables building document processing pipelines - chain multiple operations (extract, transform, convert) into reusable workflows with data flowing between stages.

How to Use
Describe what you want to accomplish
Provide any required input data or files
I'll execute the appropriate operations

Example prompts:

"PDF → Extract Text → Translate → Generate DOCX"
"Image → OCR → Summarize → Create Report"
"Excel → Analyze → Generate Charts → Create PPT"
"Multiple inputs → Merge → Format → Output"
Domain Knowledge
Pipeline Architecture
Stage 1      Stage 2      Stage 3      Stage 4
┌──────┐    ┌──────┐    ┌──────┐    ┌──────┐
│Extract│ → │Transform│ → │ AI   │ → │Output│
│ PDF  │    │  Data  │    │Analyze│   │ DOCX │
└──────┘    └──────┘    └──────┘    └──────┘
     │           │           │           │
     └───────────┴───────────┴───────────┘
                 Data Flow

Pipeline DSL (Domain Specific Language)
# pipeline.yaml
name: contract-review-pipeline
description: Extract, analyze, and report on contracts

stages:
  - name: extract
    operation: pdf-extraction
    input: $input_file
    output: $extracted_text
    
  - name: analyze
    operation: ai-analyze
    input: $extracted_text
    prompt: "Review this contract for risks..."
    output: $analysis
    
  - name: report
    operation: docx-generation
    input: $analysis
    template: templates/review_report.docx
    output: $output_file

Python Implementation
from typing import Callable, Any
from dataclasses import dataclass

@dataclass
class Stage:
    name: str
    operation: Callable
    
class Pipeline:
    def __init__(self, name: str):
        self.name = name
        self.stages: list[Stage] = []
    
    def add_stage(self, name: str, operation: Callable):
        self.stages.append(Stage(name, operation))
        return self  # Fluent API
    
    def run(self, input_data: Any) -> Any:
        data = input_data
        for stage in self.stages:
            print(f"Running stage: {stage.name}")
            data = stage.operation(data)
        return data

# Example usage
pipeline = Pipeline("contract-review")
pipeline.add_stage("extract", extract_pdf_text)
pipeline.add_stage("analyze", analyze_with_ai)
pipeline.add_stage("generate", create_docx_report)

result = pipeline.run("/path/to/contract.pdf")

Advanced: Conditional Pipelines
class ConditionalPipeline(Pipeline):
    def add_conditional_stage(self, name: str, condition: Callable, 
                               if_true: Callable, if_false: Callable):
        def conditional_op(data):
            if condition(data):
                return if_true(data)
            return if_false(data)
        return self.add_stage(name, conditional_op)

# Usage
pipeline.add_conditional_stage(
    "ocr_if_needed",
    condition=lambda d: d.get("has_images"),
    if_true=run_ocr,
    if_false=lambda d: d
)

Best Practices
Keep stages focused (single responsibility)
Use intermediate outputs for debugging
Implement stage-level error handling
Make pipelines configurable via YAML/JSON
Installation
# Install required dependencies
pip install python-docx openpyxl python-pptx reportlab jinja2

Resources
Custom Repository
Claude Office Skills Hub
Weekly Installs
688
Repository
claude-office-s…s/skills
GitHub Stars
94
First Seen
Mar 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass