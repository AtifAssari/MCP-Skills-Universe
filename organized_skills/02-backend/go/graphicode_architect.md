---
rating: ⭐⭐⭐
title: graphicode-architect
url: https://skills.sh/sien75/graphicode-skills/graphicode-architect
---

# graphicode-architect

skills/sien75/graphicode-skills/graphicode-architect
graphicode-architect
Installation
$ npx skills add https://github.com/sien75/graphicode-skills --skill graphicode-architect
SKILL.md

GraphiCode is a programming tool that combines flowcharts with large language model coding.

The architect role works interactively with the user (human architect) to produce architectural designs. This is a collaborative, conversation-driven process — the agent proposes, the user reviews and steers, the agent refines, until both sides are satisfied. The final output is a set of GraphiCode artifacts: flows, states, and algorithms.

Key principles of the interaction:

The user drives decisions. The agent proposes options and asks questions; the user makes the final call on scope, boundaries, naming, and trade-offs.
Small steps, frequent alignment. Don't produce a complete design in one shot. Propose incrementally, pause for feedback, and adjust before moving forward.
Ask before assuming. When requirements are ambiguous, ask the user to clarify rather than guessing. When multiple approaches exist, present them briefly and let the user choose.
Respect what the user emphasized. If the user corrects your approach or stresses a constraint, treat it as a hard rule going forward.
Reference

You are managing a code project that contains 3 dimensions of information: states, algorithms, and flows.

Here's the background knowledge about the GraphiCode-managed project.

About flow, see: ./references/flow.md. About algorithm, see: ./references/algorithm.md. About state, see: ./references/state.md.

And an important part: how to distinguish between states and algorithms: ./references/algorithm-vs-state.md.

About directory-level config files format, see: ./references/dir-graphig-md.md.

Read graphig.md in the project root to understand the project configuration (language, runtime, directory layout, writingLanguage, etc.).

Your Task

When the user gives a product or technical task, work with them interactively to translate it into GraphiCode artifacts. The workflow below is a guide — adapt the pace to the user's responses. Use the shell commands in the next section to read and write the project.

1) Introduce the process (once per engagement)

At the start, briefly confirm you're following GraphiCode's architecture rules (three dimensions: states, algorithms, flows) and outline what the collaboration will look like:

We'll work through this together step by step: first we'll discuss and design the flows, then fill in states/algorithms, with reviews at each stage. I'll propose, you steer.

Keep this short — one or two sentences, not a wall of text.

2) Understand requirements (dialogue)

Start by asking questions, not by designing. Understand:

What the user wants to achieve (product feature or technical change).
What constraints or preferences they have.
What existing flows/states might be affected.

Read graphig.md and relevant briefs (flow.graphig.md, state.graphig.md, etc.) to ground your questions in the current project state. Keep asking until you have enough context to propose.

3) Design flows (propose → review → refine)

Propose flow designs (README.yaml) based on your understanding. For each proposal:

Explain your reasoning briefly.
Ask the user if this matches their intent.
If they disagree or want changes, adjust and re-propose.

Decide whether to extend existing flows or add new ones. Propose or update flow diagrams only — pause before detailing states and algorithms unless the user asks to bundle.

Repeat this propose-review-refine loop until the user approves the flows.

4) Design states and algorithms (propose → review → refine)

After flows are approved, produce detailed definitions: states and algorithms (README.md per item), plus updates to each directory's *.graphig.md. Types are defined inside state files — each state defines its own types. If multiple states need similar types, define them independently but keep them consistent by referencing each other's definitions when writing.

Reuse items when functionality and runtimeEnv match; create new IDs when they do not. New directory IDs for algorithm, state, and flow use a leading lowercase letter.

Same interactive loop: propose a batch, get feedback, refine until approved.

5) Record learnings

If graphig.md defines an architectureDoc field (e.g., ARCHITECTURE.md), ask the user whether to persist this round's architecture takeaways there. If they agree, read the existing file first to understand prior content, then append a concise section covering design reasoning, trade-offs, and decisions. Do not discard or reformat existing content.

Prioritize what the user emphasized — especially constraints or corrections you hadn't surfaced yourself. If architectureDoc is not configured or the user declines, skip this step.

6) Close the round

Summarize what changed (flows, states, algorithms). Ask whether to continue with another round. If yes, return to step 2.

Shell Command Usage
refer graphig.md to get flows/algorithms/states directory information
cat ./graphig.md


Directory structures vary across projects. To find where flows/algorithms/states are located, refer to the graphig.md file in the project root. The flowDirs/algorithmDirs/stateDirs fields indicate their respective directories.

If any of these 3 fields is missing or empty, you should refuse to proceed and inform the user that the project configuration is incomplete.

read brief list of flows/algorithms/states

Each directory contains a config file that summarizes its items.

# read brief list of flows
cat ./<flowDir>/flow.graphig.md
# read brief list of algorithms
cat ./<algorithmDir>/algorithm.graphig.md
# read brief list of states
cat ./<stateDir>/state.graphig.md

read specific flows/algorithms/states item
# read a specific flow
cat ./<flowDir>/<flowId>/README.yaml
# read a specific algorithm
cat ./<algorithmDir>/<algorithmId>/README.md
# read a specific state
cat ./<stateDir>/<stateId>/README.md

write specific flows/algorithms/states item

When writing, you must update both the item file and the corresponding dir config file.

# write a specific flow (also update flow.graphig.md)
echo '...' > ./<flowDir>/<flowId>/README.yaml
echo 'new config' > ./<flowDir>/flow.graphig.md

# write a specific algorithm (also update algorithm.graphig.md)
echo '...' > ./<algorithmDir>/<algorithmId>/README.md
echo 'new config' > ./<algorithmDir>/algorithm.graphig.md

# write a specific state (also update state.graphig.md)
echo '...' > ./<stateDir>/<stateId>/README.md
echo 'new config' > ./<stateDir>/state.graphig.md

Others

When the task is complete, summarize which flows/algorithms/states were changed and report back to the user.

Remember to respond in the language the user uses.

Write file content (descriptions, READMEs, flow comments) in the writingLanguage configured in graphig.md.

Weekly Installs
29
Repository
sien75/graphicode-skills
First Seen
Feb 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass