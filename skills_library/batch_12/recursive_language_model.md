---
title: recursive-language-model
url: https://skills.sh/viktor-ferenczi/skills/recursive-language-model
---

# recursive-language-model

skills/viktor-ferenczi/skills/recursive-language-model
recursive-language-model
Installation
$ npx skills add https://github.com/viktor-ferenczi/skills --skill recursive-language-model
SKILL.md
RLM (Recursive Language Model) Skill

This skill enables processing of arbitrarily long documents by treating them as an external environment and recursively calling sub-LLMs over chunks of the content.

Overview

The RLM pattern follows the architecture from the paper:

Root Agent: Main agent orchestrating the task
Sub-LLM (llm_query): Subordinate agent for chunk-level analysis
External Environment: Persistent Python REPL with document state
Requirements
Python 3.8+
An agentic harness with code execution and subordinate agent capabilities
File Structure
rlm_skill/
├── SKILL.md           # This file
├── rlm-subcall.md     # Subordinate agent prompt profile
└── scripts/
    └── rlm_repl.py    # Persistent Python REPL

Quick Start
Initialize the skill by loading it into your agent context
Load a context file using the REPL init command
Run the RLM workflow - chunk, delegate, synthesize
Detailed Usage
Step 1: Initialize the REPL with your context

Execute via your agent's code execution tool:

python3 /path/to/rlm_skill/scripts/rlm_repl.py init /path/to/your/context.txt

Step 2: Verify status
python3 /path/to/rlm_skill/scripts/rlm_repl.py status

Step 3: Scout the context
python3 /path/to/rlm_skill/scripts/rlm_repl.py exec -c 'print(peek(0, 3000))'

Step 4: Create chunks
python3 /path/to/rlm_skill/scripts/rlm_repl.py exec -c 'print("\\n".join(write_chunks("./rlm_chunks", size=200000, overlap=0)))'

Step 5: Delegate to sub-LLM

Use your agentic harness's subordinate agent capability with the rlm-subcall profile:

Subordinate Agent Query:
Profile: rlm-subcall
Message: Query: <user_question>

Chunk file: ./rlm_chunks/chunk_0000.txt

Extract relevant information from this chunk.

Step 6: Synthesize results

Combine sub-LLM outputs and provide the final answer in the main conversation.

REPL Helper Functions

The rlm_repl.py provides these injected functions:

peek(start=0, end=1000) - View portion of content
grep(pattern, max_matches=20, window=120, flags=0) - Search with context
chunk_indices(size=200000, overlap=0) - Get chunk boundaries
write_chunks(out_dir, size=200000, overlap=0, prefix='chunk') - Materialize chunks as files
add_buffer(text) - Store intermediate results
REPL Commands
init <context_path> - Load context file
status [--show-vars] - Show current state
exec [-c "code"] - Execute Python code (reads from stdin if no -c)
export-buffers <out_path> - Write buffers to file
reset - Delete state file
Best Practices
Don't paste large chunks into main chat - Use REPL and subordinates
Use grep() to locate relevant sections - Then peek() for details
Keep chunk outputs structured - Prefer JSON for sub-LLM responses
Synthesize in main conversation - After collecting evidence
Clean up state when done - Use reset to clear old contexts
Example Workflow
User: "Analyze this 500KB log file and find all error messages from service X"

Agent:
1. Init: python rlm_repl.py init /path/to/logs.txt
2. Scout: exec -c 'print(peek(0, 500))'
3. Search: exec -c 'print(grep("service X.*error", max_matches=10))'
4. Chunk: exec -c 'write_chunks("./chunks", size=100000)'
5. For each chunk, call subordinate with rlm-subcall profile
6. Synthesize findings and answer user

Limitations
State is stored locally via pickle (not distributed)
Context size limited by available memory
Sub-LLM calls are synchronous in this implementation
References
MIT paper: "Recursive Language Models"
Implementation: brainqub3/claude_code_RLM
Weekly Installs
9
Repository
viktor-ferenczi/skills
GitHub Stars
1
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass