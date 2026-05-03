---
rating: ⭐⭐⭐
title: latchbio-integration
url: https://skills.sh/davila7/claude-code-templates/latchbio-integration
---

# latchbio-integration

skills/davila7/claude-code-templates/latchbio-integration
latchbio-integration
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill latchbio-integration
SKILL.md
LatchBio Integration
Overview

Latch is a Python framework for building and deploying bioinformatics workflows as serverless pipelines. Built on Flyte, create workflows with @workflow/@task decorators, manage cloud data with LatchFile/LatchDir, configure resources, and integrate Nextflow/Snakemake pipelines.

Core Capabilities

The Latch platform provides four main areas of functionality:

1. Workflow Creation and Deployment
Define serverless workflows using Python decorators
Support for native Python, Nextflow, and Snakemake pipelines
Automatic containerization with Docker
Auto-generated no-code user interfaces
Version control and reproducibility
2. Data Management
Cloud storage abstractions (LatchFile, LatchDir)
Structured data organization with Registry (Projects → Tables → Records)
Type-safe data operations with links and enums
Automatic file transfer between local and cloud
Glob pattern matching for file selection
3. Resource Configuration
Pre-configured task decorators (@small_task, @large_task, @small_gpu_task, @large_gpu_task)
Custom resource specifications (CPU, memory, GPU, storage)
GPU support (K80, V100, A100)
Timeout and storage configuration
Cost optimization strategies
4. Verified Workflows
Production-ready pre-built pipelines
Bulk RNA-seq, DESeq2, pathway analysis
AlphaFold and ColabFold for protein structure prediction
Single-cell tools (ArchR, scVelo, emptyDropsR)
CRISPR analysis, phylogenetics, and more
Quick Start
Installation and Setup
# Install Latch SDK
python3 -m uv pip install latch

# Login to Latch
latch login

# Initialize a new workflow
latch init my-workflow

# Register workflow to platform
latch register my-workflow


Prerequisites:

Docker installed and running
Latch account credentials
Python 3.8+
Basic Workflow Example
from latch import workflow, small_task
from latch.types import LatchFile

@small_task
def process_file(input_file: LatchFile) -> LatchFile:
    """Process a single file"""
    # Processing logic
    return output_file

@workflow
def my_workflow(input_file: LatchFile) -> LatchFile:
    """
    My bioinformatics workflow

    Args:
        input_file: Input data file
    """
    return process_file(input_file=input_file)

When to Use This Skill

This skill should be used when encountering any of the following scenarios:

Workflow Development:

"Create a Latch workflow for RNA-seq analysis"
"Deploy my pipeline to Latch"
"Convert my Nextflow pipeline to Latch"
"Add GPU support to my workflow"
Working with @workflow, @task decorators

Data Management:

"Organize my sequencing data in Latch Registry"
"How do I use LatchFile and LatchDir?"
"Set up sample tracking in Latch"
Working with latch:/// paths

Resource Configuration:

"Configure GPU for AlphaFold on Latch"
"My task is running out of memory"
"How do I optimize workflow costs?"
Working with task decorators

Verified Workflows:

"Run AlphaFold on Latch"
"Use DESeq2 for differential expression"
"Available pre-built workflows"
Using latch.verified module
Detailed Documentation

This skill includes comprehensive reference documentation organized by capability:

references/workflow-creation.md

Read this for:

Creating and registering workflows
Task definition and decorators
Supporting Python, Nextflow, Snakemake
Launch plans and conditional sections
Workflow execution (CLI and programmatic)
Multi-step and parallel pipelines
Troubleshooting registration issues

Key topics:

latch init and latch register commands
@workflow and @task decorators
LatchFile and LatchDir basics
Type annotations and docstrings
Launch plans with preset parameters
Conditional UI sections
references/data-management.md

Read this for:

Cloud storage with LatchFile and LatchDir
Registry system (Projects, Tables, Records)
Linked records and relationships
Enum and typed columns
Bulk operations and transactions
Integration with workflows
Account and workspace management

Key topics:

latch:/// path format
File transfer and glob patterns
Creating and querying Registry tables
Column types (string, number, file, link, enum)
Record CRUD operations
Workflow-Registry integration
references/resource-configuration.md

Read this for:

Task resource decorators
Custom CPU, memory, GPU configuration
GPU types (K80, V100, A100)
Timeout and storage settings
Resource optimization strategies
Cost-effective workflow design
Monitoring and debugging

Key topics:

@small_task, @large_task, @small_gpu_task, @large_gpu_task
@custom_task with precise specifications
Multi-GPU configuration
Resource selection by workload type
Platform limits and quotas
references/verified-workflows.md

Read this for:

Pre-built production workflows
Bulk RNA-seq and DESeq2
AlphaFold and ColabFold
Single-cell analysis (ArchR, scVelo)
CRISPR editing analysis
Pathway enrichment
Integration with custom workflows

Key topics:

latch.verified module imports
Available verified workflows
Workflow parameters and options
Combining verified and custom steps
Version management
Common Workflow Patterns
Complete RNA-seq Pipeline
from latch import workflow, small_task, large_task
from latch.types import LatchFile, LatchDir

@small_task
def quality_control(fastq: LatchFile) -> LatchFile:
    """Run FastQC"""
    return qc_output

@large_task
def alignment(fastq: LatchFile, genome: str) -> LatchFile:
    """STAR alignment"""
    return bam_output

@small_task
def quantification(bam: LatchFile) -> LatchFile:
    """featureCounts"""
    return counts

@workflow
def rnaseq_pipeline(
    input_fastq: LatchFile,
    genome: str,
    output_dir: LatchDir
) -> LatchFile:
    """RNA-seq analysis pipeline"""
    qc = quality_control(fastq=input_fastq)
    aligned = alignment(fastq=qc, genome=genome)
    return quantification(bam=aligned)

GPU-Accelerated Workflow
from latch import workflow, small_task, large_gpu_task
from latch.types import LatchFile

@small_task
def preprocess(input_file: LatchFile) -> LatchFile:
    """Prepare data"""
    return processed

@large_gpu_task
def gpu_computation(data: LatchFile) -> LatchFile:
    """GPU-accelerated analysis"""
    return results

@workflow
def gpu_pipeline(input_file: LatchFile) -> LatchFile:
    """Pipeline with GPU tasks"""
    preprocessed = preprocess(input_file=input_file)
    return gpu_computation(data=preprocessed)

Registry-Integrated Workflow
from latch import workflow, small_task
from latch.registry.table import Table
from latch.registry.record import Record
from latch.types import LatchFile

@small_task
def process_and_track(sample_id: str, table_id: str) -> str:
    """Process sample and update Registry"""
    # Get sample from registry
    table = Table.get(table_id=table_id)
    records = Record.list(table_id=table_id, filter={"sample_id": sample_id})
    sample = records[0]

    # Process
    input_file = sample.values["fastq_file"]
    output = process(input_file)

    # Update registry
    sample.update(values={"status": "completed", "result": output})
    return "Success"

@workflow
def registry_workflow(sample_id: str, table_id: str):
    """Workflow integrated with Registry"""
    return process_and_track(sample_id=sample_id, table_id=table_id)

Best Practices
Workflow Design
Use type annotations for all parameters
Write clear docstrings (appear in UI)
Start with standard task decorators, scale up if needed
Break complex workflows into modular tasks
Implement proper error handling
Data Management
Use consistent folder structures
Define Registry schemas before bulk entry
Use linked records for relationships
Store metadata in Registry for traceability
Resource Configuration
Right-size resources (don't over-allocate)
Use GPU only when algorithms support it
Monitor execution metrics and optimize
Design for parallel execution when possible
Development Workflow
Test locally with Docker before registration
Use version control for workflow code
Document resource requirements
Profile workflows to determine actual needs
Troubleshooting
Common Issues

Registration Failures:

Ensure Docker is running
Check authentication with latch login
Verify all dependencies in Dockerfile
Use --verbose flag for detailed logs

Resource Problems:

Out of memory: Increase memory in task decorator
Timeouts: Increase timeout parameter
Storage issues: Increase ephemeral storage_gib

Data Access:

Use correct latch:/// path format
Verify file exists in workspace
Check permissions for shared workspaces

Type Errors:

Add type annotations to all parameters
Use LatchFile/LatchDir for file/directory parameters
Ensure workflow return type matches actual return
Additional Resources
Official Documentation: https://docs.latch.bio
GitHub Repository: https://github.com/latchbio/latch
Slack Community: Join Latch SDK workspace
API Reference: https://docs.latch.bio/api/latch.html
Blog: https://blog.latch.bio
Support

For issues or questions:

Check documentation links above
Search GitHub issues
Ask in Slack community
Contact support@latch.bio
Weekly Installs
211
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass