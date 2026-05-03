---
title: sadd:judge
url: https://skills.sh/neolabhq/context-engineering-kit/sadd:judge
---

# sadd:judge

skills/neolabhq/context-engineering-kit/sadd:judge
sadd:judge
Installation
$ npx skills add https://github.com/neolabhq/context-engineering-kit --skill sadd:judge
SKILL.md
Judge Command
Your Workflow
Phase 1: Context Extraction

Before launching the evaluation pipeline, identify what needs evaluation:

Identify the work to evaluate:

Review conversation history for completed work
If arguments provided: Use them to focus on specific aspects
If unclear: Ask user "What work should I evaluate? (code changes, analysis, documentation, etc.)"

Extract evaluation context:

Original task or request that prompted the work
The actual output/result produced
Files created or modified (with brief descriptions)
Any constraints, requirements, or acceptance criteria mentioned
Artifact type (code, documentation, configuration, etc.)

Provide scope for user:

Evaluation Scope:
- Original request: [summary]
- Work produced: [description]
- Files involved: [list]
- Artifact type: [code | documentation | configuration | etc.]
- Evaluation focus: [from arguments or "general quality"]

Launching meta-judge to generate evaluation criteria...


IMPORTANT: Pass only the extracted context to the sub-agents - not the entire conversation. This prevents context pollution and enables focused assessment.

Phase 2: Dispatch Meta-Judge

Launch a meta-judge agent to generate an evaluation specification tailored to the specific work being evaluated. The meta-judge will return an evaluation specification YAML containing rubrics, checklists, and scoring criteria.

Meta-Judge Prompt:

## Task

Generate an evaluation specification yaml for the following evaluation task. You will produce rubrics, checklists, and scoring criteria that a judge agent will use to evaluate the work.

CLAUDE_PLUGIN_ROOT=`${CLAUDE_PLUGIN_ROOT}`

## User Prompt
{Original task or request that prompted the work}

## Context
{Any relevant context about the work being evaluated}
{Evaluation focus from arguments, or "General quality assessment"}

## Artifact Type
{code | documentation | configuration | etc.}

## Instructions
Return only the final evaluation specification YAML in your response.


Dispatch:

Use Task tool:
  - description: "Meta-judge: Generate evaluation criteria for {brief work summary}"
  - prompt: {meta-judge prompt}
  - model: opus
  - subagent_type: "sadd:meta-judge"


Wait for the meta-judge to complete before proceeding to Phase 3.

Phase 3: Dispatch Judge Agent

After the meta-judge completes, extract its evaluation specification YAML and dispatch the judge agent with both the work context and the specification.

CRITICAL: Provide to the judge the EXACT meta-judge evaluation specification YAML. Do not skip, add, modify, shorten, or summarize any text in it!

Judge Agent Prompt:

You are an Expert Judge evaluating the quality of work against an evaluation specification produced by the meta judge.

CLAUDE_PLUGIN_ROOT=`${CLAUDE_PLUGIN_ROOT}`

## Work Under Evaluation

[ORIGINAL TASK]
{paste the original request/task}
[/ORIGINAL TASK]

[WORK OUTPUT]
{summary of what was created/modified}
[/WORK OUTPUT]

[FILES INVOLVED]
{list of files with brief descriptions}
[/FILES INVOLVED]

## Evaluation Specification

```yaml
{meta-judge's evaluation specification YAML}

Instructions

Follow your full judge process as defined in your agent instructions!

CRITICAL: You must reply with this exact structured evaluation report format in YAML at the START of your response!


CRITICAL: NEVER provide score threshold to judges in any format. Judge MUST not know what threshold for score is, in order to not be biased!!!

**Dispatch:**



Use Task tool:

description: "Judge: Evaluate {brief work summary}"
prompt: {judge prompt with exact meta-judge specification YAML}
model: opus
subagent_type: "sadd:judge"

### Phase 4: Process and Present Results

After receiving the judge's evaluation:

1. **Validate the evaluation**:
   - Check that all criteria have scores in valid range (1-5)
   - Verify each score has supporting justification with evidence
   - Confirm weighted total calculation is correct
   - Check for contradictions between justification and score
   - Verify self-verification was completed with documented adjustments

2. **If validation fails**:
   - Note the specific issue
   - Request clarification or re-evaluation if needed

3. **Present results to user**:
   - Display the full evaluation report
   - Highlight the verdict and key findings
   - Offer follow-up options:
     - Address specific improvements
     - Request clarification on any judgment
     - Proceed with the work as-is

## Scoring Interpretation

| Score Range | Verdict | Interpretation | Recommendation |
|-------------|---------|----------------|----------------|
| 4.50 - 5.00 | EXCELLENT | Exceptional quality, exceeds expectations | Ready as-is |
| 4.00 - 4.49 | GOOD | Solid quality, meets professional standards | Minor improvements optional |
| 3.50 - 3.99 | ACCEPTABLE | Adequate but has room for improvement | Improvements recommended |
| 3.00 - 3.49 | NEEDS IMPROVEMENT | Below standard, requires work | Address issues before use |
| 1.00 - 2.99 | INSUFFICIENT | Does not meet basic requirements | Significant rework needed |

## Important Guidelines

1. **Meta-judge first**: Always generate evaluation specification before judging - never skip the meta-judge phase
2. **Include CLAUDE_PLUGIN_ROOT**: Both meta-judge and judge need the resolved plugin root path
3. **Meta-judge YAML**: Pass only the meta-judge YAML to the judge, do not modify it
4. **Context Isolation**: Pass only relevant context to sub-agents - not the entire conversation
5. **Justification First**: Always require evidence and reasoning BEFORE the score
6. **Evidence-Based**: Every score must cite specific evidence (file paths, line numbers, quotes)
7. **Bias Mitigation**: Explicitly warn against length bias, verbosity bias, and authority bias
8. **Be Objective**: Base assessments on evidence and rubric definitions, not preferences
9. **Be Specific**: Cite exact locations, not vague observations
10. **Be Constructive**: Frame criticism as opportunities for improvement with impact context
11. **Consider Context**: Account for stated constraints, complexity, and requirements
12. **Report Confidence**: Lower confidence when evidence is ambiguous or criteria unclear
13. **Single Judge**: This command uses one focused judge for context isolation

## Notes

- This is a **report-only** command - it evaluates but does not modify work
- The meta-judge generates criteria tailored to the specific artifact type and evaluation focus
- The judge operates with fresh context for unbiased assessment
- Scores are calibrated to professional development standards
- Low scores indicate improvement opportunities, not failures
- Use the evaluation to inform next steps and iterations
- Low confidence evaluations may warrant human review

Weekly Installs
447
Repository
neolabhq/contex…ring-kit
GitHub Stars
942
First Seen
Feb 23, 2026