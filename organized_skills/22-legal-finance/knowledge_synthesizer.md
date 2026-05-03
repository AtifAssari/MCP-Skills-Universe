---
rating: ⭐⭐
title: knowledge-synthesizer
url: https://skills.sh/404kidwiz/claude-supercode-skills/knowledge-synthesizer
---

# knowledge-synthesizer

skills/404kidwiz/claude-supercode-skills/knowledge-synthesizer
knowledge-synthesizer
Installation
$ npx skills add https://github.com/404kidwiz/claude-supercode-skills --skill knowledge-synthesizer
SKILL.md
Knowledge Synthesizer
Purpose

Provides expertise in aggregating information from multiple sources and synthesizing it into structured, actionable knowledge. Specializes in ontology building, knowledge graph design, and insight extraction for RAG and AI systems.

When to Use
Building knowledge graphs or ontologies
Designing GraphRAG or hybrid retrieval systems
Synthesizing information across multiple documents
Extracting entities and relationships from text
Creating structured knowledge bases
Developing taxonomy and classification systems
Implementing semantic search architectures
Connecting disparate data sources meaningfully
Quick Start

Invoke this skill when:

Building knowledge graphs or ontologies
Designing RAG systems with graph components
Synthesizing insights from multiple sources
Extracting structured knowledge from unstructured text
Creating taxonomies or classification schemes

Do NOT invoke when:

Vector database setup without graph needs → use /context-manager
General NLP tasks (NER, classification) → use /nlp-engineer
Database schema design → use /database-administrator
Document writing → use /technical-writer
Decision Framework
Knowledge Structure Needed?
├── Hierarchical (taxonomy)
│   └── Tree structure, parent-child relationships
├── Graph (connected entities)
│   └── Nodes + edges, property graphs
├── Hybrid (RAG + Graph)
│   └── Vector embeddings + knowledge graph
└── Flat (simple retrieval)
    └── Standard vector store sufficient

Core Workflows
1. Ontology Design
Identify domain scope and boundaries
Define core entity types (classes)
Map relationships between entities
Add properties and constraints
Validate with domain experts
Document with examples
2. Knowledge Graph Construction
Extract entities from source documents
Identify relationships between entities
Normalize and deduplicate entities
Build graph structure (nodes, edges)
Add metadata and provenance
Create query interfaces
3. Insight Synthesis
Gather sources and establish provenance
Extract key claims and facts
Identify contradictions and agreements
Synthesize into coherent narrative
Cite sources for traceability
Highlight confidence levels
Best Practices
Maintain provenance for all extracted knowledge
Use established ontology standards (OWL, SKOS) when applicable
Design for evolution—ontologies change over time
Validate extracted relationships with source context
Balance granularity with usability
Include confidence scores for extracted facts
Anti-Patterns
Anti-Pattern	Problem	Correct Approach
No provenance tracking	Cannot verify claims	Track source for every fact
Over-complex ontology	Hard to maintain and query	Start simple, evolve as needed
Ignoring contradictions	Inconsistent knowledge base	Flag and resolve conflicts
Static schema	Breaks with new domains	Design for extensibility
Blind extraction trust	Hallucinated relationships	Validate with confidence thresholds
Weekly Installs
126
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