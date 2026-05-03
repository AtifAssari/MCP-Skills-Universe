---
title: senior-data-engineer
url: https://skills.sh/davila7/claude-code-templates/senior-data-engineer
---

# senior-data-engineer

skills/davila7/claude-code-templates/senior-data-engineer
senior-data-engineer
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill senior-data-engineer
Summary

Senior-level data engineering expertise for building scalable pipelines, ETL systems, and production data infrastructure.

Covers advanced patterns across data pipeline architecture, modeling, and DataOps with distributed computing frameworks (Spark, Airflow, dbt, Kafka) and modern data stack tools (Databricks, BigQuery, Snowflake)
Includes production deployment patterns for scalable data processing, ML model serving with low latency, and real-time inference with auto-scaling and monitoring
Provides best practices for development (TDD, code reviews), production (monitoring, canary deployments, feature flags), and team leadership including mentoring and cross-functional collaboration
Supports multiple languages (Python, SQL, R, Scala, Go) and integrates with ML frameworks (PyTorch, TensorFlow, XGBoost), LLM tools (LangChain, LlamaIndex), and observability platforms (MLflow, Prometheus, Weights & Biases)
SKILL.md
Senior Data Engineer

World-class senior data engineer skill for production-grade AI/ML/Data systems.

Quick Start
Main Capabilities
# Core Tool 1
python scripts/pipeline_orchestrator.py --input data/ --output results/

# Core Tool 2  
python scripts/data_quality_validator.py --target project/ --analyze

# Core Tool 3
python scripts/etl_performance_optimizer.py --config config.yaml --deploy

Core Expertise

This skill covers world-class capabilities in:

Advanced production patterns and architectures
Scalable system design and implementation
Performance optimization at scale
MLOps and DataOps best practices
Real-time processing and inference
Distributed computing frameworks
Model deployment and monitoring
Security and compliance
Cost optimization
Team leadership and mentoring
Tech Stack

Languages: Python, SQL, R, Scala, Go ML Frameworks: PyTorch, TensorFlow, Scikit-learn, XGBoost Data Tools: Spark, Airflow, dbt, Kafka, Databricks LLM Frameworks: LangChain, LlamaIndex, DSPy Deployment: Docker, Kubernetes, AWS/GCP/Azure Monitoring: MLflow, Weights & Biases, Prometheus Databases: PostgreSQL, BigQuery, Snowflake, Pinecone

Reference Documentation
1. Data Pipeline Architecture

Comprehensive guide available in references/data_pipeline_architecture.md covering:

Advanced patterns and best practices
Production implementation strategies
Performance optimization techniques
Scalability considerations
Security and compliance
Real-world case studies
2. Data Modeling Patterns

Complete workflow documentation in references/data_modeling_patterns.md including:

Step-by-step processes
Architecture design patterns
Tool integration guides
Performance tuning strategies
Troubleshooting procedures
3. Dataops Best Practices

Technical reference guide in references/dataops_best_practices.md with:

System design principles
Implementation examples
Configuration best practices
Deployment strategies
Monitoring and observability
Production Patterns
Pattern 1: Scalable Data Processing

Enterprise-scale data processing with distributed computing:

Horizontal scaling architecture
Fault-tolerant design
Real-time and batch processing
Data quality validation
Performance monitoring
Pattern 2: ML Model Deployment

Production ML system with high availability:

Model serving with low latency
A/B testing infrastructure
Feature store integration
Model monitoring and drift detection
Automated retraining pipelines
Pattern 3: Real-Time Inference

High-throughput inference system:

Batching and caching strategies
Load balancing
Auto-scaling
Latency optimization
Cost optimization
Best Practices
Development
Test-driven development
Code reviews and pair programming
Documentation as code
Version control everything
Continuous integration
Production
Monitor everything critical
Automate deployments
Feature flags for releases
Canary deployments
Comprehensive logging
Team Leadership
Mentor junior engineers
Drive technical decisions
Establish coding standards
Foster learning culture
Cross-functional collaboration
Performance Targets

Latency:

P50: < 50ms
P95: < 100ms
P99: < 200ms

Throughput:

Requests/second: > 1000
Concurrent users: > 10,000

Availability:

Uptime: 99.9%
Error rate: < 0.1%
Security & Compliance
Authentication & authorization
Data encryption (at rest & in transit)
PII handling and anonymization
GDPR/CCPA compliance
Regular security audits
Vulnerability management
Common Commands
# Development
python -m pytest tests/ -v --cov
python -m black src/
python -m pylint src/

# Training
python scripts/train.py --config prod.yaml
python scripts/evaluate.py --model best.pth

# Deployment
docker build -t service:v1 .
kubectl apply -f k8s/
helm upgrade service ./charts/

# Monitoring
kubectl logs -f deployment/service
python scripts/health_check.py

Resources
Advanced Patterns: references/data_pipeline_architecture.md
Implementation Guide: references/data_modeling_patterns.md
Technical Reference: references/dataops_best_practices.md
Automation Scripts: scripts/ directory
Senior-Level Responsibilities

As a world-class senior professional:

Technical Leadership

Drive architectural decisions
Mentor team members
Establish best practices
Ensure code quality

Strategic Thinking

Align with business goals
Evaluate trade-offs
Plan for scale
Manage technical debt

Collaboration

Work across teams
Communicate effectively
Build consensus
Share knowledge

Innovation

Stay current with research
Experiment with new approaches
Contribute to community
Drive continuous improvement

Production Excellence

Ensure high availability
Monitor proactively
Optimize performance
Respond to incidents
Weekly Installs
1.1K
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass