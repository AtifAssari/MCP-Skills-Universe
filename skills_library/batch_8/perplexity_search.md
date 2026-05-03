---
title: perplexity-search
url: https://skills.sh/davila7/claude-code-templates/perplexity-search
---

# perplexity-search

skills/davila7/claude-code-templates/perplexity-search
perplexity-search
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill perplexity-search
Summary

AI-powered web search with real-time information and source citations via Perplexity models.

Access five Perplexity models through a single OpenRouter API key, ranging from cost-effective Sonar to advanced Sonar Pro Search for complex multi-step analysis
Ideal for finding current information beyond model knowledge cutoff, recent scientific literature, clinical trials, and domain-specific research with peer-reviewed sources
Includes comprehensive query design guidance covering specificity, time constraints, domain terminology, and structured question formatting for high-quality results
Supports batch processing, programmatic access via Python module, and cost optimization strategies with token limits and spending controls
Built-in troubleshooting for API key setup, rate limiting, credit management, and integration patterns with other scientific research skills
SKILL.md
Perplexity Search
Overview

Perform AI-powered web searches using Perplexity models through LiteLLM and OpenRouter. Perplexity provides real-time, web-grounded answers with source citations, making it ideal for finding current information, recent scientific literature, and facts beyond the model's training data cutoff.

This skill provides access to all Perplexity models through OpenRouter, requiring only a single API key (no separate Perplexity account needed).

When to Use This Skill

Use this skill when:

Searching for current information or recent developments (2024 and beyond)
Finding latest scientific publications and research
Getting real-time answers grounded in web sources
Verifying facts with source citations
Conducting literature searches across multiple domains
Accessing information beyond the model's knowledge cutoff
Performing domain-specific research (biomedical, technical, clinical)
Comparing current approaches or technologies

Do not use for:

Simple calculations or logic problems (use directly)
Tasks requiring code execution (use standard tools)
Questions well within the model's training data (unless verification needed)
Quick Start
Setup (One-time)

Get OpenRouter API key:

Visit https://openrouter.ai/keys
Create account and generate API key
Add credits to account (minimum $5 recommended)

Configure environment:

# Set API key
export OPENROUTER_API_KEY='sk-or-v1-your-key-here'

# Or use setup script
python scripts/setup_env.py --api-key sk-or-v1-your-key-here


Install dependencies:

uv pip install litellm


Verify setup:

python scripts/perplexity_search.py --check-setup


See references/openrouter_setup.md for detailed setup instructions, troubleshooting, and security best practices.

Basic Usage

Simple search:

python scripts/perplexity_search.py "What are the latest developments in CRISPR gene editing?"


Save results:

python scripts/perplexity_search.py "Recent CAR-T therapy clinical trials" --output results.json


Use specific model:

python scripts/perplexity_search.py "Compare mRNA and viral vector vaccines" --model sonar-pro-search


Verbose output:

python scripts/perplexity_search.py "Quantum computing for drug discovery" --verbose

Available Models

Access models via --model parameter:

sonar-pro (default): General-purpose search, best balance of cost and quality
sonar-pro-search: Most advanced agentic search with multi-step reasoning
sonar: Basic model, most cost-effective for simple queries
sonar-reasoning-pro: Advanced reasoning with step-by-step analysis
sonar-reasoning: Basic reasoning capabilities

Model selection guide:

Default queries → sonar-pro
Complex multi-step analysis → sonar-pro-search
Explicit reasoning needed → sonar-reasoning-pro
Simple fact lookups → sonar
Cost-sensitive bulk queries → sonar

See references/model_comparison.md for detailed comparison, use cases, pricing, and performance characteristics.

Crafting Effective Queries
Be Specific and Detailed

Good examples:

"What are the latest clinical trial results for CAR-T cell therapy in treating B-cell lymphoma published in 2024?"
"Compare the efficacy and safety profiles of mRNA vaccines versus viral vector vaccines for COVID-19"
"Explain AlphaFold3 improvements over AlphaFold2 with specific accuracy metrics from 2023-2024 research"

Bad examples:

"Tell me about cancer treatment" (too broad)
"CRISPR" (too vague)
"vaccines" (lacks specificity)
Include Time Constraints

Perplexity searches real-time web data:

"What papers were published in Nature Medicine in 2024 about long COVID?"
"What are the latest developments (past 6 months) in large language model efficiency?"
"What was announced at NeurIPS 2023 regarding AI safety?"
Specify Domain and Sources

For high-quality results, mention source preferences:

"According to peer-reviewed publications in high-impact journals..."
"Based on FDA-approved treatments..."
"From clinical trial registries like clinicaltrials.gov..."
Structure Complex Queries

Break complex questions into clear components:

Topic: Main subject
Scope: Specific aspect of interest
Context: Time frame, domain, constraints
Output: Desired format or type of answer

Example: "What improvements does AlphaFold3 offer over AlphaFold2 for protein structure prediction, according to research published between 2023 and 2024? Include specific accuracy metrics and benchmarks."

See references/search_strategies.md for comprehensive guidance on query design, domain-specific patterns, and advanced techniques.

Common Use Cases
Scientific Literature Search
python scripts/perplexity_search.py \
  "What does recent research (2023-2024) say about the role of gut microbiome in Parkinson's disease? Focus on peer-reviewed studies and include specific bacterial species identified." \
  --model sonar-pro

Technical Documentation
python scripts/perplexity_search.py \
  "How to implement real-time data streaming from Kafka to PostgreSQL using Python? Include considerations for handling backpressure and ensuring exactly-once semantics." \
  --model sonar-reasoning-pro

Comparative Analysis
python scripts/perplexity_search.py \
  "Compare PyTorch versus TensorFlow for implementing transformer models in terms of ease of use, performance, and ecosystem support. Include benchmarks from recent studies." \
  --model sonar-pro-search

Clinical Research
python scripts/perplexity_search.py \
  "What is the evidence for intermittent fasting in managing type 2 diabetes in adults? Focus on randomized controlled trials and report HbA1c changes and weight loss outcomes." \
  --model sonar-pro

Trend Analysis
python scripts/perplexity_search.py \
  "What are the key trends in single-cell RNA sequencing technology over the past 5 years? Highlight improvements in throughput, cost, and resolution, with specific examples." \
  --model sonar-pro

Working with Results
Programmatic Access

Use perplexity_search.py as a module:

from scripts.perplexity_search import search_with_perplexity

result = search_with_perplexity(
    query="What are the latest CRISPR developments?",
    model="openrouter/perplexity/sonar-pro",
    max_tokens=4000,
    temperature=0.2,
    verbose=False
)

if result["success"]:
    print(result["answer"])
    print(f"Tokens used: {result['usage']['total_tokens']}")
else:
    print(f"Error: {result['error']}")

Save and Process Results
# Save to JSON
python scripts/perplexity_search.py "query" --output results.json

# Process with jq
cat results.json | jq '.answer'
cat results.json | jq '.usage'

Batch Processing

Create a script for multiple queries:

#!/bin/bash
queries=(
  "CRISPR developments 2024"
  "mRNA vaccine technology advances"
  "AlphaFold3 accuracy improvements"
)

for query in "${queries[@]}"; do
  echo "Searching: $query"
  python scripts/perplexity_search.py "$query" --output "results_$(echo $query | tr ' ' '_').json"
  sleep 2  # Rate limiting
done

Cost Management

Perplexity models have different pricing tiers:

Approximate costs per query:

Sonar: $0.001-0.002 (most cost-effective)
Sonar Pro: $0.002-0.005 (recommended default)
Sonar Reasoning Pro: $0.005-0.010
Sonar Pro Search: $0.020-0.050+ (most comprehensive)

Cost optimization strategies:

Use sonar for simple fact lookups
Default to sonar-pro for most queries
Reserve sonar-pro-search for complex analysis
Set --max-tokens to limit response length
Monitor usage at https://openrouter.ai/activity
Set spending limits in OpenRouter dashboard
Troubleshooting
API Key Not Set

Error: "OpenRouter API key not configured"

Solution:

export OPENROUTER_API_KEY='sk-or-v1-your-key-here'
# Or run setup script
python scripts/setup_env.py --api-key sk-or-v1-your-key-here

LiteLLM Not Installed

Error: "LiteLLM not installed"

Solution:

uv pip install litellm

Rate Limiting

Error: "Rate limit exceeded"

Solutions:

Wait a few seconds before retrying
Increase rate limit at https://openrouter.ai/keys
Add delays between requests in batch processing
Insufficient Credits

Error: "Insufficient credits"

Solution:

Add credits at https://openrouter.ai/account
Enable auto-recharge to prevent interruptions

See references/openrouter_setup.md for comprehensive troubleshooting guide.

Integration with Other Skills

This skill complements other scientific skills:

Literature Review

Use with literature-review skill:

Use Perplexity to find recent papers and preprints
Supplement PubMed searches with real-time web results
Verify citations and find related work
Discover latest developments post-database indexing
Scientific Writing

Use with scientific-writing skill:

Find recent references for introduction/discussion
Verify current state of the art
Check latest terminology and conventions
Identify recent competing approaches
Hypothesis Generation

Use with hypothesis-generation skill:

Search for latest research findings
Identify current gaps in knowledge
Find recent methodological advances
Discover emerging research directions
Critical Thinking

Use with scientific-critical-thinking skill:

Find evidence for and against hypotheses
Locate methodological critiques
Identify controversies in the field
Verify claims with current evidence
Best Practices
Query Design
Be specific: Include domain, time frame, and constraints
Use terminology: Domain-appropriate keywords and phrases
Specify sources: Mention preferred publication types or journals
Structure questions: Clear components with explicit context
Iterate: Refine based on initial results
Model Selection
Start with sonar-pro: Good default for most queries
Upgrade for complexity: Use sonar-pro-search for multi-step analysis
Downgrade for simplicity: Use sonar for basic facts
Use reasoning models: When step-by-step analysis needed
Cost Optimization
Choose appropriate models: Match model to query complexity
Set token limits: Use --max-tokens to control costs
Monitor usage: Check OpenRouter dashboard regularly
Batch efficiently: Combine related simple queries when possible
Cache results: Save and reuse results for repeated queries
Security
Protect API keys: Never commit to version control
Use environment variables: Keep keys separate from code
Set spending limits: Configure in OpenRouter dashboard
Monitor usage: Watch for unexpected activity
Rotate keys: Change keys periodically
Resources
Bundled Resources

Scripts:

scripts/perplexity_search.py: Main search script with CLI interface
scripts/setup_env.py: Environment setup and validation helper

References:

references/search_strategies.md: Comprehensive query design guide
references/model_comparison.md: Detailed model comparison and selection guide
references/openrouter_setup.md: Complete setup, troubleshooting, and security guide

Assets:

assets/.env.example: Example environment file template
External Resources

OpenRouter:

Dashboard: https://openrouter.ai/account
API Keys: https://openrouter.ai/keys
Perplexity Models: https://openrouter.ai/perplexity
Usage Monitoring: https://openrouter.ai/activity
Documentation: https://openrouter.ai/docs

LiteLLM:

Documentation: https://docs.litellm.ai/
OpenRouter Provider: https://docs.litellm.ai/docs/providers/openrouter
GitHub: https://github.com/BerriAI/litellm

Perplexity:

Official Docs: https://docs.perplexity.ai/
Dependencies
Required
# LiteLLM for API access
uv pip install litellm

Optional
# For .env file support
uv pip install python-dotenv

# For JSON processing (usually pre-installed)
uv pip install jq

Environment Variables

Required:

OPENROUTER_API_KEY: Your OpenRouter API key

Optional:

DEFAULT_MODEL: Default model to use (default: sonar-pro)
DEFAULT_MAX_TOKENS: Default max tokens (default: 4000)
DEFAULT_TEMPERATURE: Default temperature (default: 0.2)
Summary

This skill provides:

Real-time web search: Access current information beyond training data cutoff
Multiple models: From cost-effective Sonar to advanced Sonar Pro Search
Simple setup: Single OpenRouter API key, no separate Perplexity account
Comprehensive guidance: Detailed references for query design and model selection
Cost-effective: Pay-as-you-go pricing with usage monitoring
Scientific focus: Optimized for research, literature search, and technical queries
Easy integration: Works seamlessly with other scientific skills

Conduct AI-powered web searches to find current information, recent research, and grounded answers with source citations.

Weekly Installs
521
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail