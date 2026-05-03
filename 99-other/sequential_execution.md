---
title: sequential-execution
url: https://skills.sh/squirrel289/pax/sequential-execution
---

# sequential-execution

skills/squirrel289/pax/sequential-execution
sequential-execution
Installation
$ npx skills add https://github.com/squirrel289/pax --skill sequential-execution
SKILL.md
Sequential Execution

Execute tasks in order when dependencies exist between steps.

When to Use

Use sequential execution when:

Tasks have dependencies (Task B needs Task A's output)
Order matters for correctness
Tasks modify shared state or files
Workflow has clear sequential stages (e.g., commit → push → PR)
Later tasks need results from earlier tasks
Parameters
tasks: Ordered list of task descriptions
dependencies: Map of task dependencies (which tasks depend on which outputs)
How Sequential Execution Works
Step 1: Identify Dependencies

Map out which tasks depend on others:

Task A produces output X
Task B needs input X to proceed
Task C needs output from Task B
Step 2: Execute in Order

Execute tasks one at a time, passing outputs forward:

Execute Task A, store output
Execute Task B with output from A
Execute Task C with output from B
Step 3: Track Progress

Use todo list to track sequential progress:

Mark current task as in-progress
Mark completed tasks as completed
Keep upcoming tasks as not-started
Sequential Patterns
Pattern 1: Linear Pipeline

A → B → C → D

Each task depends on the previous task's output.

Pattern 2: Staged Workflow

Stage 1: Setup → Stage 2: Processing → Stage 3: Cleanup

Clear phases that must happen in order.

Pattern 3: Conditional Sequencing

A → (if success) → B → (if failure) → C

Execution path depends on previous results.

Pattern 4: Accumulator Pattern

Start with initial state, each task transforms and passes to next:

Task 1: Initialize state
Task 2: Transform state
Task 3: Enhance state
Task 4: Finalize state
When to Use Sequential vs Parallel
Scenario	Execution Type	Reason
B needs A's output	Sequential	Dependency
Multiple independent analyses	Parallel	No dependencies
Commit → Push → PR	Sequential	Order matters
Analyze multiple files	Parallel	Independent
Build → Test → Deploy	Sequential	Must happen in order
Review multiple perspectives	Parallel	Independent views
TodoList Integration

Track sequential progress clearly:

{
  "todos": [
    { "id": 1, "title": "Fetch PR details", "status": "completed" },
    { "id": 2, "title": "Run tests", "status": "in-progress" },
    { "id": 3, "title": "Review comments", "status": "not-started" },
    { "id": 4, "title": "Merge PR", "status": "not-started" }
  ]
}

Common Sequential Workflows
Git Workflow
Make changes → 2. Commit → 3. Push → 4. Create PR → 5. Merge
PR Processing
Fetch PR → 2. Analyze → 3. Address comments → 4. Run checks → 5. Merge
Build Pipeline
Install dependencies → 2. Build → 3. Test → 4. Package → 5. Deploy
Code Review
Read code → 2. Identify issues → 3. Write comments → 4. Submit review
Error Handling

In sequential execution:

If step N fails, steps N+1 onwards cannot proceed
Decide whether to:
Retry failed step
Skip to error handling flow
Abort entire sequence
Continue with partial results
Best Practices
Make dependencies explicit: Clearly document what each task needs
Pass data forward: Each task receives output from previous task
Track progress: Update todo list after each step
Handle errors: Plan for failures at each stage
Validate inputs: Ensure each task has what it needs before starting
Log intermediate results: Useful for debugging and resuming
Quick Reference
WHEN TO USE:
✓ Tasks have dependencies
✓ Order matters
✓ Shared state modifications
✓ Must wait for previous results

PATTERNS:
Linear: A → B → C → D
Staged: Setup → Process → Cleanup
Conditional: A → (check) → B or C
Accumulator: Transform state through stages

TODOLIST:

- Mark current step as in-progress
- Keep future steps as not-started
- Mark completed steps as completed

ERROR HANDLING:

- Stop on failure
- Retry step
- Fallback flow
- Abort sequence

Weekly Installs
10
Repository
squirrel289/pax
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass