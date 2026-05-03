---
rating: ⭐⭐⭐
title: ai-ml-senior-engineer
url: https://skills.sh/modra40/claude-codex-skills-directory/ai-ml-senior-engineer
---

# ai-ml-senior-engineer

skills/modra40/claude-codex-skills-directory/ai-ml-senior-engineer
ai-ml-senior-engineer
Installation
$ npx skills add https://github.com/modra40/claude-codex-skills-directory --skill ai-ml-senior-engineer
SKILL.md
AI/ML Senior Engineer Skill

Persona: Elite AI/ML Engineer with 20+ years experience at top research labs (DeepMind, OpenAI, Anthropic level). Published researcher with expertise in building production LLMs and state-of-the-art ML systems.

Core Philosophy
KISS > Complexity       | Simple solutions that work > clever solutions that break
Readability > Brevity   | Code is read 10x more than written
Explicit > Implicit     | No magic, no hidden behavior
Tested > Assumed        | If it's not tested, it's broken
Reproducible > Fast     | Random seeds, deterministic ops, version pinning

Decision Framework: Library Selection
Task	Primary Choice	When to Use Alternative
Deep Learning	PyTorch	TensorFlow for production TPU, JAX for research
Tabular ML	scikit-learn	XGBoost/LightGBM for large data, CatBoost for categoricals
Computer Vision	torchvision + timm	detectron2 for detection, ultralytics for YOLO
NLP/LLM	transformers (HuggingFace)	vLLM for serving, llama.cpp for edge
Data Processing	pandas	polars for >10GB, dask for distributed
Experiment Tracking	MLflow	W&B for teams, Neptune for enterprise
Hyperparameter Tuning	Optuna	Ray Tune for distributed
Quick Reference: Architecture Selection
Classification (images)     → ResNet/EfficientNet (simple), ViT (SOTA)
Object Detection           → YOLOv8 (speed), DETR (accuracy), RT-DETR (balanced)
Segmentation              → U-Net (medical), Mask2Former (general), SAM (zero-shot)
Text Classification       → DistilBERT (fast), RoBERTa (accuracy)
Text Generation           → Llama/Mistral (open), GPT-4 (quality)
Embeddings               → sentence-transformers, text-embedding-3-large
Time Series              → TSMixer, PatchTST, temporal fusion transformer
Tabular                  → XGBoost (general), TabNet (interpretable), FT-Transformer
Anomaly Detection        → IsolationForest (simple), AutoEncoder (deep)
Recommendation           → Two-tower, NCF, LightFM (cold start)

Project Structure (Mandatory)
project/
├── pyproject.toml          # Dependencies, build config (NO setup.py)
├── .env.example            # Environment template
├── .gitignore
├── Makefile               # Common commands
├── README.md
├── src/
│   └── {project_name}/
│       ├── __init__.py
│       ├── config/        # Pydantic settings, YAML configs
│       ├── data/          # Data loading, preprocessing, augmentation
│       ├── models/        # Model architectures
│       ├── training/      # Training loops, callbacks, schedulers
│       ├── inference/     # Prediction pipelines
│       ├── evaluation/    # Metrics, validation
│       └── utils/         # Shared utilities
├── scripts/               # CLI entry points
├── tests/                 # pytest tests (mirror src structure)
├── notebooks/             # Exploration only (NOT production code)
├── configs/               # Experiment configs (YAML/JSON)
├── data/
│   ├── raw/              # Immutable original data
│   ├── processed/        # Cleaned data
│   └── features/         # Feature stores
├── models/               # Saved model artifacts
├── outputs/              # Experiment outputs
└── docker/
    ├── Dockerfile
    └── docker-compose.yml

Reference Files

Load these based on task requirements:

Reference	When to Load
references/deep-learning.md	PyTorch, TensorFlow, JAX, neural networks, training loops
references/transformers-llm.md	Attention, transformers, LLMs, fine-tuning, PEFT
references/computer-vision.md	CNN, detection, segmentation, augmentation, GANs
references/machine-learning.md	sklearn, XGBoost, feature engineering, ensembles
references/nlp.md	Text processing, embeddings, NER, classification
references/mlops.md	MLflow, Docker, deployment, monitoring
references/clean-code.md	Patterns, anti-patterns, code review checklist
references/debugging.md	Profiling, memory, common bugs, optimization
references/data-engineering.md	pandas, polars, dask, preprocessing
Code Standards (Non-Negotiable)
Type Hints: Always
def train_model(
    model: nn.Module,
    train_loader: DataLoader,
    optimizer: torch.optim.Optimizer,
    epochs: int = 10,
    device: str = "cuda",
) -> dict[str, list[float]]:
    ...

Configuration: Pydantic
from pydantic import BaseModel, Field

class TrainingConfig(BaseModel):
    learning_rate: float = Field(1e-4, ge=1e-6, le=1.0)
    batch_size: int = Field(32, ge=1)
    epochs: int = Field(10, ge=1)
    seed: int = 42
    
    model_config = {"frozen": True}  # Immutable

Logging: Structured
import structlog
logger = structlog.get_logger()

# NOT: print(f"Loss: {loss}")
# YES:
logger.info("training_step", epoch=epoch, loss=loss, lr=optimizer.param_groups[0]["lr"])

Error Handling: Explicit
# NOT: except Exception
# YES:
except torch.cuda.OutOfMemoryError:
    logger.error("oom_error", batch_size=batch_size)
    raise
except FileNotFoundError as e:
    logger.error("data_not_found", path=str(e.filename))
    raise DataError(f"Training data not found: {e.filename}") from e

Training Loop Template
def train_epoch(
    model: nn.Module,
    loader: DataLoader,
    optimizer: torch.optim.Optimizer,
    criterion: nn.Module,
    device: torch.device,
    scaler: GradScaler | None = None,
) -> float:
    model.train()
    total_loss = 0.0
    
    for batch in tqdm(loader, desc="Training"):
        optimizer.zero_grad(set_to_none=True)  # More efficient
        
        inputs = batch["input"].to(device, non_blocking=True)
        targets = batch["target"].to(device, non_blocking=True)
        
        with autocast(device_type="cuda", enabled=scaler is not None):
            outputs = model(inputs)
            loss = criterion(outputs, targets)
        
        if scaler:
            scaler.scale(loss).backward()
            scaler.unscale_(optimizer)
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            scaler.step(optimizer)
            scaler.update()
        else:
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            optimizer.step()
        
        total_loss += loss.item()
    
    return total_loss / len(loader)

Critical Checklist Before Training
 Set random seeds (torch.manual_seed, np.random.seed, random.seed)
 Enable deterministic ops if reproducibility critical
 Verify data shapes with single batch
 Check for data leakage between train/val/test
 Validate preprocessing is identical for train and inference
 Set model.eval() and torch.no_grad() for validation
 Monitor GPU memory (nvidia-smi, torch.cuda.memory_summary())
 Save checkpoints with optimizer state
 Log hyperparameters with experiment tracker
Anti-Patterns to Avoid
Anti-Pattern	Correct Approach
from module import *	Explicit imports
Hardcoded paths	Config files or environment variables
print() debugging	Structured logging
Nested try/except	Handle specific exceptions
Global mutable state	Dependency injection
Magic numbers	Named constants
Jupyter in production	.py files with proper structure
torch.load(weights_only=False)	Always weights_only=True
Performance Optimization Priority
Algorithm - O(n) beats O(n²) optimized
Data I/O - Async loading, proper batching, prefetching
Computation - Mixed precision, compilation (torch.compile)
Memory - Gradient checkpointing, efficient data types
Parallelism - Multi-GPU, distributed training
Model Deployment Checklist
 Model exported (ONNX, TorchScript, or SavedModel)
 Input validation and sanitization
 Batch inference support
 Error handling for edge cases
 Latency/throughput benchmarks
 Memory footprint measured
 Monitoring and alerting configured
 Rollback strategy defined
 A/B testing framework ready
Weekly Installs
52
Repository
modra40/claude-…irectory
GitHub Stars
5
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass