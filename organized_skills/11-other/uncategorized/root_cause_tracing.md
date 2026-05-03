---
rating: ⭐⭐
title: root-cause-tracing
url: https://skills.sh/secondsky/claude-skills/root-cause-tracing
---

# root-cause-tracing

skills/secondsky/claude-skills/root-cause-tracing
root-cause-tracing
Installation
$ npx skills add https://github.com/secondsky/claude-skills --skill root-cause-tracing
SKILL.md
Root Cause Tracing
Overview

Bugs often manifest deep in the call stack (git init in wrong directory, file created in wrong location, database opened with wrong path). Your instinct is to fix where the error appears, but that's treating a symptom.

Core principle: Trace backward through the call chain until you find the original trigger, then fix at the source.

When to Use

Use when:

Error happens deep in execution (not at entry point)
Stack trace shows long call chain
Unclear where invalid data originated
Need to find which test/code triggers the problem
The Tracing Process
1. Observe the Symptom
Error: git init failed in ~/project/packages/core

2. Find Immediate Cause

What code directly causes this?

await execFileAsync('git', ['init'], { cwd: projectDir });

3. Ask: What Called This?
WorktreeManager.createSessionWorktree(projectDir, sessionId)
  → called by Session.initializeWorkspace()
  → called by Session.create()
  → called by test at Project.create()

4. Keep Tracing Up

What value was passed?

projectDir = '' (empty string!)
Empty string as cwd resolves to process.cwd()
That's the source code directory!
5. Find Original Trigger

Where did empty string come from?

const context = setupCoreTest(); // Returns { tempDir: '' }
Project.create('name', context.tempDir); // Accessed before beforeEach!

Adding Stack Traces

When you can't trace manually, add instrumentation:

// Before the problematic operation
async function gitInit(directory: string) {
  const stack = new Error().stack;
  console.error('DEBUG git init:', {
    directory,
    cwd: process.cwd(),
    nodeEnv: process.env.NODE_ENV,
    stack,
  });

  await execFileAsync('git', ['init'], { cwd: directory });
}


Critical: Use console.error() in tests (not logger - may not show)

Run and capture:

bun test 2>&1 | grep 'DEBUG git init'


Analyze stack traces:

Look for test file names
Find the line number triggering the call
Identify the pattern (same test? same parameter?)
Finding Which Test Causes Pollution

If something appears during tests but you don't know which test:

Use the bisection script to run tests one-by-one:

# Example: find which test creates .git in wrong place
bun test --run --bail 2>&1 | tee test-output.log


Runs tests one-by-one, stops at first polluter.

Real Example: Empty projectDir

Symptom: .git created in packages/core/ (source code)

Trace chain:

git init runs in process.cwd() ← empty cwd parameter
WorktreeManager called with empty projectDir
Session.create() passed empty string
Test accessed context.tempDir before beforeEach
setupCoreTest() returns { tempDir: '' } initially

Root cause: Top-level variable initialization accessing empty value

Fix: Made tempDir a getter that throws if accessed before beforeEach

Also added defense-in-depth:

Layer 1: Project.create() validates directory
Layer 2: WorkspaceManager validates not empty
Layer 3: NODE_ENV guard refuses git init outside tmpdir
Layer 4: Stack trace logging before git init
Key Principle

NEVER fix just where the error appears. Trace back to find the original trigger.

Stack Trace Tips

In tests: Use console.error() not logger - logger may be suppressed Before operation: Log before the dangerous operation, not after it fails Include context: Directory, cwd, environment variables, timestamps Capture stack: new Error().stack shows complete call chain

Real-World Impact

From debugging session:

Found root cause through 5-level trace
Fixed at source (getter validation)
Added 4 layers of defense
1847 tests passed, zero pollution
Weekly Installs
178
Repository
secondsky/claude-skills
GitHub Stars
129
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass