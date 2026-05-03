---
rating: ⭐⭐⭐
title: symbolic-equation
url: https://skills.sh/lingzhi227/agent-research-skills/symbolic-equation
---

# symbolic-equation

skills/lingzhi227/agent-research-skills/symbolic-equation
symbolic-equation
Installation
$ npx skills add https://github.com/lingzhi227/agent-research-skills --skill symbolic-equation
SKILL.md
Symbolic Equation Discovery

Discover interpretable scientific equations from data using LLM-guided evolutionary search.

Input
$0 — Dataset description, variable names, and physical context
References
LLM-SR patterns (prompts, evolution, sampling): ~/.claude/skills/symbolic-equation/references/llmsr-patterns.md
Workflow (from LLM-SR)
Step 1: Define Problem Specification

Create a specification with:

Input variables: Physical quantities with types (e.g., x: np.ndarray, v: np.ndarray)
Output variable: Target quantity to predict
Evaluation function: Fitness metric (typically negative MSE with parameter optimization)
Physical context: Domain knowledge to guide equation discovery
# Example specification
@equation.evolve
def equation(x: np.ndarray, v: np.ndarray, params: np.ndarray) -> np.ndarray:
    """Describe the acceleration of a damped nonlinear oscillator."""
    return params[0] * x

Step 2: Initialize Multi-Island Buffer
Create N islands (default: 10) for population diversity
Each island maintains independent clusters of equations
Clusters group equations by performance signature
Step 3: Evolutionary Search Loop

Repeat until convergence or max samples:

Select island: Random island selection
Build prompt: Sample top equations from clusters (softmax-weighted by score)
LLM proposes: Generate new equation as improved version
Evaluate: Execute on test data, compute fitness score
Register: Add to island's cluster if valid
Step 4: Prompt Construction

Present previous equations as versioned sequence:

def equation_v0(x, v, params):
    """Initial version."""
    return params[0] * x

def equation_v1(x, v, params):
    """Improved version of equation_v0."""
    return params[0] * x + params[1] * v

def equation_v2(x, v, params):
    """Improved version of equation_v1."""
    # LLM completes this

Step 5: Island Reset (Diversity Maintenance)

Periodically (default: every 4 hours):

Sort islands by best score
Reset bottom 50% of islands
Seed each reset island with best equation from a surviving island
Restart cluster sampling temperature
Step 6: Extract Best Equations

After search completes:

Collect best equation from each island
Rank by fitness score
Simplify if possible (algebraic simplification)
Report with physical interpretation
Cluster Sampling

Temperature-scheduled softmax over cluster scores:

temperature = T_init * (1 - (num_programs % period) / period)
probabilities = softmax(cluster_scores / temperature)

Higher temperature → more exploration
Lower temperature → more exploitation of best clusters
Within clusters: shorter programs are preferred (Occam's razor)
Rules
Equations must use only standard mathematical operations
Parameter optimization via scipy BFGS or Adam
Fitness = negative MSE (higher is better)
Timeout protection for equation evaluation
No recursive equations allowed
Physical interpretability is preferred over pure fit
Related Skills
Upstream: data-analysis, math-reasoning
Downstream: paper-writing-section
See also: algorithm-design
Weekly Installs
123
Repository
lingzhi227/agen…h-skills
GitHub Stars
42
First Seen
1 day ago
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass