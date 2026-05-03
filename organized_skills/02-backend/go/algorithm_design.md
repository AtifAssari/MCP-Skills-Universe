---
rating: ⭐⭐
title: algorithm-design
url: https://skills.sh/lingzhi227/agent-research-skills/algorithm-design
---

# algorithm-design

skills/lingzhi227/agent-research-skills/algorithm-design
algorithm-design
Installation
$ npx skills add https://github.com/lingzhi227/agent-research-skills --skill algorithm-design
SKILL.md
Algorithm Design

Formalize methods into algorithm pseudocode and system architecture diagrams.

Input
$0 — Method description or implementation to formalize
References
Algorithm and diagram templates: ~/.claude/skills/algorithm-design/references/algorithm-templates.md
Workflow
Step 1: Formalize the Algorithm
Define clear inputs and outputs
Identify the main loop / recursive structure
Specify all parameters and their types
Write step-by-step pseudocode
Step 2: Generate LaTeX Pseudocode

Use algorithm + algpseudocode environments:

\begin{algorithm}[t]
\caption{Method Name}
\label{alg:method}
\begin{algorithmic}[1]
\Require Input $x$, parameters $\theta$
\Ensure Output $y$
\State Initialize ...
\For{$t = 1$ to $T$}
    \State $z_t \gets f(x_t; \theta)$
    \If{convergence criterion met}
        \State \textbf{break}
    \EndIf
\EndFor
\State \Return $y$
\end{algorithmic}
\end{algorithm}

Step 3: Generate UML Diagrams (Mermaid)
Class Diagram
classDiagram
    class Model {
        +forward(x: Tensor) Tensor
        +train_step(batch) float
    }

Sequence Diagram
sequenceDiagram
    participant M as Main
    participant D as DataLoader
    M->>D: load_data()
    D-->>M: batches

Step 4: Verify Consistency
Every pseudocode step must map to a code module
Every class in the UML must exist in the implementation
Parameter names must match between pseudocode and code
Rules
Use standard algorithmic notation (not code syntax)
Number lines for easy reference
Include complexity analysis as a comment or proposition
Use \Require / \Ensure for inputs/outputs
Keep pseudocode at the right abstraction level — not too detailed, not too vague
Related Skills
Upstream: atomic-decomposition, math-reasoning
Downstream: experiment-code, paper-writing-section
See also: symbolic-equation
Weekly Installs
146
Repository
lingzhi227/agen…h-skills
GitHub Stars
42
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass