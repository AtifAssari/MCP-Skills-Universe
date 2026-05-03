---
rating: ⭐⭐⭐
title: background-job-processing
url: https://skills.sh/aj-geddes/useful-ai-prompts/background-job-processing
---

# background-job-processing

skills/aj-geddes/useful-ai-prompts/background-job-processing
background-job-processing
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill background-job-processing
SKILL.md
Background Job Processing
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Build robust background job processing systems with distributed task queues, worker pools, job scheduling, error handling, retry policies, and monitoring for efficient asynchronous task execution.

When to Use
Handling long-running operations asynchronously
Sending emails in background
Generating reports or exports
Processing large datasets
Scheduling recurring tasks
Distributing compute-intensive operations
Quick Start

Minimal working example:

# celery_app.py
from celery import Celery
from kombu import Exchange, Queue
import os

app = Celery('myapp')

# Configuration
app.conf.update(
    broker_url=os.getenv('REDIS_URL', 'redis://localhost:6379/0'),
    result_backend=os.getenv('REDIS_URL', 'redis://localhost:6379/0'),
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
    task_track_started=True,
    task_time_limit=30 * 60,  # 30 minutes
    task_soft_time_limit=25 * 60,  # 25 minutes
    broker_connection_retry_on_startup=True,
)

# Queue configuration
default_exchange = Exchange('tasks', type='direct')
app.conf.task_queues = (
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Python with Celery and Redis	Python with Celery and Redis
Node.js with Bull Queue	Node.js with Bull Queue
Ruby with Sidekiq	Ruby with Sidekiq
Job Retry and Error Handling	Job Retry and Error Handling
Monitoring and Observability	Monitoring and Observability
Best Practices
✅ DO
Use task timeouts to prevent hanging jobs
Implement retry logic with exponential backoff
Make tasks idempotent
Use job priorities for critical tasks
Monitor queue depths and job failures
Log job execution details
Clean up completed jobs
Set appropriate batch sizes for memory efficiency
Use dead-letter queues for failed jobs
Test jobs independently
❌ DON'T
Use synchronous operations in async tasks
Ignore job failures
Make tasks dependent on external state
Use unbounded retries
Store large objects in job data
Forget to handle timeouts
Run jobs without monitoring
Use blocking operations in queues
Forget to track job progress
Mix unrelated operations in one job
Weekly Installs
306
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass