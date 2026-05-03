---
rating: ⭐⭐⭐
title: hf-model-inference
url: https://skills.sh/letta-ai/skills/hf-model-inference
---

# hf-model-inference

skills/letta-ai/skills/hf-model-inference
hf-model-inference
Installation
$ npx skills add https://github.com/letta-ai/skills --skill hf-model-inference
SKILL.md
HuggingFace Model Inference Service
Overview

This skill provides procedural guidance for setting up HuggingFace model inference services. It covers model downloading, caching strategies, Flask API creation, and service deployment patterns.

Workflow
Phase 1: Environment Setup

Verify package manager availability

Check for uv, pip, or conda before installing dependencies
Prefer uv for faster dependency resolution when available

Install required packages

Core: transformers, torch (or tensorflow)
API: flask for REST endpoints
Set appropriate timeouts for large package installations (300+ seconds)

Create model cache directory

Establish a dedicated directory for model storage (e.g., /app/model_cache/model_name)
Create parent directories as needed before downloading
Phase 2: Model Download

Download the model separately from API startup

Use a dedicated download script or inline download before starting the service
This prevents timeout issues during API initialization

Specify cache directory explicitly

from transformers import pipeline
model = pipeline("task-type", model="model-name", cache_dir="/path/to/cache")


Verification step (commonly missed)

After download, verify model files exist in the target directory
List directory contents to confirm successful download
Phase 3: API Creation

Flask application structure

from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
model = None  # Load at startup

@app.route('/predict', methods=['POST'])
def predict():
    # Handle inference
    pass


Input validation requirements

Check for required fields in request JSON
Validate field types (string, number, etc.)
Handle empty or whitespace-only inputs
Return descriptive error messages with appropriate HTTP status codes

Error response format

Use consistent JSON structure: {"error": "message"}
Return 400 for client errors, 500 for server errors
Phase 4: Service Deployment

Host and port configuration

Bind to 0.0.0.0 for external accessibility
Use specified port (commonly 5000)
Example: app.run(host='0.0.0.0', port=5000)

Background execution

Start Flask in background mode for testing
Allow startup time (2-3 seconds) before sending test requests
Verification Strategies
Model Download Verification
List cache directory contents after download
Confirm expected model files exist (config.json, model weights, tokenizer files)
API Functionality Testing

Test these scenarios in order:

Positive case: Valid input that should succeed

curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "valid input text"}'


Negative case: Different valid input to verify varied responses

curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "different input text"}'


Error case: Missing required field

curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{}'

Extended Edge Cases (Optional)
Empty string input
Very long text input
Non-JSON content type
Malformed JSON
Wrong field type (number instead of string)
Common Pitfalls
Installation Issues
Insufficient timeout: Large packages like torch require extended timeouts (5+ minutes)
Missing system dependencies: Some models require additional system packages
Model Loading Issues
Cold start timeout: Loading models at first request causes timeouts; load at startup instead
Memory constraints: Large models may exceed available RAM; check model requirements
API Issues
Development server warning: Flask development server is not suitable for production; acceptable for testing but note the limitation
No graceful shutdown: Consider signal handling for clean termination
No health check endpoint: Adding /health endpoint aids debugging
Process Management
Background process verification: After starting in background, verify the process is running
Port conflicts: Check if the specified port is already in use before starting
Task Planning Template

When approaching HuggingFace inference tasks, structure work as follows:

Environment verification (package manager, system requirements)
Dependency installation with appropriate timeouts
Cache directory creation
Model download with explicit cache path
Model download verification
API script creation with validation
Service startup in background
Functional testing (positive, negative, error cases)
Edge case testing (if time permits)
Weekly Installs
37
Repository
letta-ai/skills
GitHub Stars
93
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn