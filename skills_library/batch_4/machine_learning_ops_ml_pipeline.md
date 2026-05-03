---
title: machine-learning-ops-ml-pipeline
url: https://skills.sh/sickn33/antigravity-awesome-skills/machine-learning-ops-ml-pipeline
---

# machine-learning-ops-ml-pipeline

skills/sickn33/antigravity-awesome-skills/machine-learning-ops-ml-pipeline
machine-learning-ops-ml-pipeline
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill machine-learning-ops-ml-pipeline
SKILL.md
Machine Learning Pipeline - Multi-Agent MLOps Orchestration

Design and implement a complete ML pipeline for: $ARGUMENTS

Use this skill when
Working on machine learning pipeline - multi-agent mlops orchestration tasks or workflows
Needing guidance, best practices, or checklists for machine learning pipeline - multi-agent mlops orchestration
Do not use this skill when
The task is unrelated to machine learning pipeline - multi-agent mlops orchestration
You need a different domain or tool outside this scope
Instructions
Clarify goals, constraints, and required inputs.
Apply relevant best practices and validate outcomes.
Provide actionable steps and verification.
If detailed examples are required, open resources/implementation-playbook.md.
Thinking

This workflow orchestrates multiple specialized agents to build a production-ready ML pipeline following modern MLOps best practices. The approach emphasizes:

Phase-based coordination: Each phase builds upon previous outputs, with clear handoffs between agents
Modern tooling integration: MLflow/W&B for experiments, Feast/Tecton for features, KServe/Seldon for serving
Production-first mindset: Every component designed for scale, monitoring, and reliability
Reproducibility: Version control for data, models, and infrastructure
Continuous improvement: Automated retraining, A/B testing, and drift detection

The multi-agent approach ensures each aspect is handled by domain experts:

Data engineers handle ingestion and quality
Data scientists design features and experiments
ML engineers implement training pipelines
MLOps engineers handle production deployment
Observability engineers ensure monitoring
Phase 1: Data & Requirements Analysis

Deliverables:

Data source audit and ingestion strategy:

Source systems and connection patterns
Schema validation using Pydantic/Great Expectations
Data versioning with DVC or lakeFS
Incremental loading and CDC strategies

Data quality framework:

Profiling and statistics generation
Anomaly detection rules
Data lineage tracking
Quality gates and SLAs

Storage architecture:

Raw/processed/feature layers
Partitioning strategy
Retention policies
Cost optimization

Provide implementation code for critical components and integration patterns.

Deliverables:

Feature engineering pipeline:

Transformation specifications
Feature store schema (Feast/Tecton)
Statistical validation rules
Handling strategies for missing data/outliers

Model requirements:

Algorithm selection rationale
Performance metrics and baselines
Training data requirements
Evaluation criteria and thresholds

Experiment design:

Hypothesis and success metrics
A/B testing methodology
Sample size calculations
Bias detection approach

Include feature transformation code and statistical validation logic.

Phase 2: Model Development & Training

Build comprehensive training system:

Training pipeline implementation:

Modular training code with clear interfaces
Hyperparameter optimization (Optuna/Ray Tune)
Distributed training support (Horovod/PyTorch DDP)
Cross-validation and ensemble strategies

Experiment tracking setup:

MLflow/Weights & Biases integration
Metric logging and visualization
Artifact management (models, plots, data samples)
Experiment comparison and analysis tools

Model registry integration:

Version control and tagging strategy
Model metadata and lineage
Promotion workflows (dev -> staging -> prod)
Rollback procedures

Provide complete training code with configuration management.

Focus areas:

Code quality and structure:

Refactor for production standards
Add comprehensive error handling
Implement proper logging with structured formats
Create reusable components and utilities

Performance optimization:

Profile and optimize bottlenecks
Implement caching strategies
Optimize data loading and preprocessing
Memory management for large-scale training

Testing framework:

Unit tests for data transformations
Integration tests for pipeline components
Model quality tests (invariance, directional)
Performance regression tests

Deliver production-ready, maintainable code with full test coverage.

Phase 3: Production Deployment & Serving

Implementation requirements:

Model serving infrastructure:

REST/gRPC APIs with FastAPI/TorchServe
Batch prediction pipelines (Airflow/Kubeflow)
Stream processing (Kafka/Kinesis integration)
Model serving platforms (KServe/Seldon Core)

Deployment strategies:

Blue-green deployments for zero downtime
Canary releases with traffic splitting
Shadow deployments for validation
A/B testing infrastructure

CI/CD pipeline:

GitHub Actions/GitLab CI workflows
Automated testing gates
Model validation before deployment
ArgoCD for GitOps deployment

Infrastructure as Code:

Terraform modules for cloud resources
Helm charts for Kubernetes deployments
Docker multi-stage builds for optimization
Secret management with Vault/Secrets Manager

Provide complete deployment configuration and automation scripts.

Kubernetes-specific requirements:

Workload orchestration:

Training job scheduling with Kubeflow
GPU resource allocation and sharing
Spot/preemptible instance integration
Priority classes and resource quotas

Serving infrastructure:

HPA/VPA for autoscaling
KEDA for event-driven scaling
Istio service mesh for traffic management
Model caching and warm-up strategies

Storage and data access:

PVC strategies for training data
Model artifact storage with CSI drivers
Distributed storage for feature stores
Cache layers for inference optimization

Provide Kubernetes manifests and Helm charts for entire ML platform.

Phase 4: Monitoring & Continuous Improvement

Monitoring framework:

Model performance monitoring:

Prediction accuracy tracking
Latency and throughput metrics
Feature importance shifts
Business KPI correlation

Data and model drift detection:

Statistical drift detection (KS test, PSI)
Concept drift monitoring
Feature distribution tracking
Automated drift alerts and reports

System observability:

Prometheus metrics for all components
Grafana dashboards for visualization
Distributed tracing with Jaeger/Zipkin
Log aggregation with ELK/Loki

Alerting and automation:

PagerDuty/Opsgenie integration
Automated retraining triggers
Performance degradation workflows
Incident response runbooks

Cost tracking:

Resource utilization metrics
Cost allocation by model/experiment
Optimization recommendations
Budget alerts and controls

Deliver monitoring configuration, dashboards, and alert rules.

Configuration Options
experiment_tracking: mlflow | wandb | neptune | clearml
feature_store: feast | tecton | databricks | custom
serving_platform: kserve | seldon | torchserve | triton
orchestration: kubeflow | airflow | prefect | dagster
cloud_provider: aws | azure | gcp | multi-cloud
deployment_mode: realtime | batch | streaming | hybrid
monitoring_stack: prometheus | datadog | newrelic | custom
Success Criteria

Data Pipeline Success:

< 0.1% data quality issues in production
Automated data validation passing 99.9% of time
Complete data lineage tracking
Sub-second feature serving latency

Model Performance:

Meeting or exceeding baseline metrics
< 5% performance degradation before retraining
Successful A/B tests with statistical significance
No undetected model drift > 24 hours

Operational Excellence:

99.9% uptime for model serving
< 200ms p99 inference latency
Automated rollback within 5 minutes
Complete observability with < 1 minute alert time

Development Velocity:

< 1 hour from commit to production
Parallel experiment execution
Reproducible training runs
Self-service model deployment

Cost Efficiency:

< 20% infrastructure waste
Optimized resource allocation
Automatic scaling based on load
Spot instance utilization > 60%
Final Deliverables

Upon completion, the orchestrated pipeline will provide:

End-to-end ML pipeline with full automation
Comprehensive documentation and runbooks
Production-ready infrastructure as code
Complete monitoring and alerting system
CI/CD pipelines for continuous improvement
Cost optimization and scaling strategies
Disaster recovery and rollback procedures
Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
383
Repository
sickn33/antigra…e-skills
GitHub Stars
36.1K
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass