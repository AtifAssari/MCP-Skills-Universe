---
rating: ⭐⭐
title: nlp-engineer
url: https://skills.sh/404kidwiz/claude-supercode-skills/nlp-engineer
---

# nlp-engineer

skills/404kidwiz/claude-supercode-skills/nlp-engineer
nlp-engineer
Installation
$ npx skills add https://github.com/404kidwiz/claude-supercode-skills --skill nlp-engineer
SKILL.md
NLP Engineer
Purpose

Provides expertise in Natural Language Processing systems design and implementation. Specializes in text classification, named entity recognition, sentiment analysis, and integrating modern LLMs using frameworks like Hugging Face, spaCy, and LangChain.

When to Use
Building text classification systems
Implementing named entity recognition (NER)
Creating sentiment analysis pipelines
Fine-tuning transformer models
Designing LLM-powered features
Implementing text preprocessing pipelines
Building search and retrieval systems
Creating text generation applications
Quick Start

Invoke this skill when:

Building NLP pipelines (classification, NER, sentiment)
Fine-tuning transformer models
Implementing text preprocessing
Integrating LLMs for text tasks
Designing semantic search systems

Do NOT invoke when:

RAG architecture design → use /ai-engineer
LLM prompt optimization → use /prompt-engineer
ML model deployment → use /mlops-engineer
General data processing → use /data-engineer
Decision Framework
NLP Task Type?
├── Classification
│   ├── Simple → Fine-tuned BERT/DistilBERT
│   └── Zero-shot → LLM with prompting
├── NER
│   ├── Standard entities → spaCy
│   └── Custom entities → Fine-tuned model
├── Generation
│   └── LLM (GPT, Claude, Llama)
└── Semantic Search
    └── Embeddings + Vector store

Core Workflows
1. Text Classification Pipeline
Collect and label training data
Preprocess text (tokenization, cleaning)
Select base model (BERT, RoBERTa)
Fine-tune on labeled dataset
Evaluate with appropriate metrics
Deploy with inference optimization
2. NER System
Define entity types for domain
Create labeled training data
Choose framework (spaCy, Hugging Face)
Train custom NER model
Evaluate precision, recall, F1
Integrate with post-processing rules
3. Embedding-Based Search
Select embedding model (sentence-transformers)
Generate embeddings for corpus
Index in vector database
Implement query embedding
Add hybrid search (keyword + semantic)
Tune similarity thresholds
Best Practices
Start with pretrained models, fine-tune as needed
Use domain-specific preprocessing
Evaluate with task-appropriate metrics
Consider inference latency for production
Implement proper text cleaning pipelines
Use batching for efficient inference
Anti-Patterns
Anti-Pattern	Problem	Correct Approach
Training from scratch	Wastes data and compute	Fine-tune pretrained
No preprocessing	Noisy inputs hurt performance	Clean and normalize text
Wrong metrics	Misleading evaluation	Task-appropriate metrics
Ignoring class imbalance	Biased predictions	Balance or weight classes
Overfitting to eval set	Poor generalization	Proper train/val/test splits
Weekly Installs
134
Repository
404kidwiz/claud…e-skills
GitHub Stars
76
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass