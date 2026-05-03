---
rating: ⭐⭐⭐
title: create-command
url: https://skills.sh/antinomyhq/forge/create-command
---

# create-command

skills/antinomyhq/forge/create-command
create-command
Installation
$ npx skills add https://github.com/antinomyhq/forge --skill create-command
SKILL.md
Create Commands

Create and manage commands for the code-forge application. Commands are modular workflows that can be invoked to perform specific tasks.

File Location

CRITICAL: All command files must be created in the <cwd>/.forge/commands directory, where <cwd> is the current working directory of your code-forge project.

Directory: <cwd>/.forge/commands
File format: {command-name}.md
Example: If your project is at /home/user/my-project, commands go in /home/user/my-project/.forge/commands/

This is the only location where forge will discover and load custom commands.

Command File Structure

Every command file must have:

YAML Frontmatter (required):

name: Command identifier (use hyphens for multi-word names)
description: What the command does

Command Body (required):

List of steps to execute
Special tags for automated workflows
Clear instructions for each step
Example Command File
---
name: check
description: Checks if the code is ready to be committed
---

- Run the `lint` and `test` commands and verify if everything is fine.
  <lint>cargo +nightly fmt --all; cargo +nightly clippy --fix --allow-staged --allow-dirty --workspace</lint>
  <test>cargo insta test --accept --unreferenced=delete</test>
- Fix every issue found in the process

Complete Sample Command

This sample demonstrates all three tag types:

---
name: sample-command
description: Sample command demonstrating the command file structure
---

This is a sample command that demonstrates the structure of command files.

- First step: Perform an initial action
  <lint>echo "Running linting..."</lint>
- Second step: Execute tests
  <test>echo "Running tests..."</test>
- Third step: Complete the workflow
  <shell>echo "Workflow complete!"</shell>
- Final step: Verify everything worked correctly

Creating a New Command
Step 1: Determine Command Purpose

Identify what the command should accomplish:

What task will it perform?
What steps are involved?
Are there automated checks or tests needed?
What should the user do with the results?
Step 2: Choose Command Name

Use verb-based names with hyphens for multi-word commands:

Good: check, fixme, pr-description, run-tests
Bad: checker, fixing, PRdescription
Step 3: Write the Command File

Create the file in the <cwd>/.forge/commands directory with the format: {command-name}.md

IMPORTANT: The file MUST be in <cwd>/.forge/commands where <cwd> is your current working directory. Commands placed anywhere else will not be discovered by forge.

Frontmatter
---
name: your-command-name
description: Clear, concise description of what this command does
---

Command Body

Use markdown lists for steps. Each step should:

Start with a clear action verb
Be specific and actionable
Include context about what to do
Special Command Tags

Use these tags for automated workflows:

<lint> Tag

For linting/formatting commands:

<lint>cargo +nightly fmt --all; cargo +nightly clippy --fix --allow-staged --allow-dirty --workspace</lint>

<test> Tag

For testing commands:

<test>cargo insta test --accept --unreferenced=delete</test>

<shell> Tag

For general shell commands (not linting or testing):

<shell>rm -rf target/debug</shell>

Using Tags

Tags should be placed on their own line after the step description:

- Run linting and testing
  <lint>your-lint-command</lint>
  <test>your-test-command</test>

Command Types
Simple Commands

Single-step or instruction-only commands:

---
name: fixme
description: Looks for all the fixme comments in the code and attempts to fix them
---

Find all the FIXME comments in source-code files and attempt to fix them.

Multi-Step Commands

Commands with multiple sequential steps:

---
name: pr-description
description: Updates the description of the PR
---

- I have created a Pull Request with all the accepted changes
- Understand the current PR deeply using the GH CLI and update the PR title and description
- Make sure the title follows conventional commits standard
- Top-level summary should contain 2-3 lines about the core functionality improvements

Automated Workflow Commands

Commands that include automated checks:

---
name: check
description: Checks if the code is ready to be committed
---

- Run the `lint` and `test` commands and verify if everything is fine.
  <lint>cargo +nightly fmt --all; cargo +nightly clippy --fix --allow-staged --allow-dirty --workspace</lint>
  <test>cargo insta test --accept --unreferenced=delete</test>
- Fix every issue found in the process

Command Templates
Simple Command Template
---
name: simple-command
description: Does one specific thing
---

Single clear instruction or description.

Automated Workflow Template
---
name: automated-workflow
description: Runs automated checks and performs follow-up actions
---

- Run automated checks
  <lint>your-lint-command</lint>
  <test>your-test-command</test>
- Review and fix any issues found
- Complete the workflow

Multi-Step Workflow Template
---
name: multi-step-workflow
description: Performs multiple sequential steps
---

- First step with clear action
- Second step with context
- Third step with specific requirements
- Final step with verification

Git Workflow Template
---
name: git-workflow
description: Performs git operations
---

- Stage changes
  <shell>git add .</shell>
- Run pre-commit checks
  <lint>cargo fmt --all</lint>
  <test>cargo test</test>
- Commit with message
  <shell>git commit -m "your commit message"</shell>
- Push to remote
  <shell>git push</shell>

Best Practices
Naming
Use lowercase letters
Use hyphens to separate words
Use verb-based names (imperative form)
Keep names short but descriptive
Descriptions
Be clear and concise
Describe what the command does, not how
Include the main purpose and key outcomes
Avoid implementation details
Command Steps
Use numbered lists for sequential steps
Start each step with an action verb
Be specific about what to do
Include context for complex steps
Use present tense
Special Tags
Place tags on their own line after the step
Only use <lint>, <test>, and <shell> tags
Include complete commands that can be executed
Use appropriate flags for your workflow
Common Patterns
Git Workflow Commands
---
name: commit-check
description: Verifies code is ready to commit
---

- Run linting and tests
  <lint>cargo fmt --all; cargo clippy --fix --allow-staged</lint>
  <test>cargo test</test>
- Review and fix any issues
- Stage all changes

Documentation Commands
---
name: update-docs
description: Updates documentation for recent changes
---

- Review recent code changes
- Identify functions or modules that need documentation
- Update inline documentation comments
- Regenerate any auto-generated docs
- Verify documentation builds successfully

Cleanup Commands
---
name: cleanup
description: Cleans up temporary files and artifacts
---

- Remove build artifacts
  <shell>rm -rf target/debug</shell>
- Remove temporary files
  <shell>find . -name "*.tmp" -delete</shell>
- Clean up dependency caches if needed
- Verify the project still builds

Build and Deploy Commands
---
name: build-deploy
description: Builds the project and deploys to staging
---

- Build the project in release mode
  <shell>cargo build --release</shell>
- Run integration tests
  <test>cargo test --test integration</test>
- Build Docker image
  <shell>docker build -t myapp:latest .</shell>
- Tag image for staging
  <shell>docker tag myapp:latest myapp:staging</shell>
- Push to registry
  <shell>docker push myapp:staging</shell>
- Deploy to staging environment
  <shell>kubectl set image deployment/myapp myapp=myapp:staging</shell>

Validation Checklist

Use this checklist to verify your command is complete and correct:

File Structure
 File is in the <cwd>/.forge/commands directory (CRITICAL)
 Filename matches command name (e.g., check.md for name: check)
 File has .md extension
 YAML frontmatter uses --- delimiters
Frontmatter
 name field is present
 name uses lowercase letters
 name uses hyphens for multi-word names
 name is verb-based (imperative form)
 description field is present
 description is clear and concise
 description describes what, not how
Command Body
 At least one step is defined
 Steps use bullet points (-)
 Each step starts with action verb
 Steps are specific and actionable
 Complex steps include context
 Steps are in logical order
Special Tags
 Tags are on their own line after step description
 Only valid tags are used (<lint>, <test>, <shell>)
 Tag commands are complete and executable
 Tag commands use appropriate flags
 Tag commands are properly formatted
Content Quality
 Command name is descriptive
 Steps are clear and unambiguous
 No redundant or duplicate steps
 Steps follow logical sequence
 Special requirements are documented
 Error handling is considered
Testing
 Command can be executed successfully
 All steps complete as expected
 Special tags work correctly
 Output is as expected
 Edge cases are handled
 Command is recognized by forge: Run forge list command --custom (or forge list cmd) and verify your command appears in the list
Common Mistakes to Avoid
Frontmatter Mistakes

Bad: Wrong delimiter:

---
name: my-command
description: My command


(Missing closing ---)

Good: Correct:

---
name: my-command
description: My command
---


Bad: Missing required field:

---
name: my-command
---


(Missing description)

Good: Correct:

---
name: my-command
description: Does something useful
---

Naming Mistakes

Bad: CamelCase name:

---
name: myCommand
description: Does something
---


Good: Correct:

---
name: my-command
description: Does something
---


Bad: Noun instead of verb:

---
name: checker
description: Checks something
---


Good: Correct:

---
name: check
description: Checks something
---

Step Mistakes

Bad: No action verb:

---
name: test
description: Runs tests
---

- The tests
- The code


Good: Correct:

---
name: test
description: Runs tests
---

- Run all tests
- Verify code quality


Bad: Vague steps:

---
name: deploy
description: Deploys application
---

- Do the deployment
- Make sure it works


Good: Correct:

---
name: deploy
description: Deploys application to production
---

- Build the Docker image
  <shell>docker build -t myapp:latest .</shell>
- Push to registry
  <shell>docker push myapp:latest</shell>
- Deploy to production
  <shell>kubectl set image deployment/myapp myapp=myapp:latest</shell>
- Verify deployment is healthy

Tag Mistakes

Bad: Tag on same line:

- Run tests <test>cargo test</test>


Good: Correct:

- Run tests
  <test>cargo test</test>


Bad: Invalid tag:

- Run checks
  <check>cargo clippy</check>


Good: Correct:

- Run checks
  <lint>cargo clippy</lint>


Bad: Incomplete command:

- Format code
  <lint>cargo fmt</lint>


(Missing --all flag)

Good: Correct:

- Format code
  <lint>cargo fmt --all</lint>

Quick Reference
File Location
Directory: <cwd>/.forge/commands (where <cwd> is current working directory)
Format: {command-name}.md
CRITICAL: Commands MUST be in this exact location to be discovered by forge
Valid Tags
<lint> - For linting/formatting commands
<test> - For testing commands
<shell> - For general shell commands
Naming Rules
Lowercase only
Hyphens for multi-word names
Verb-based (imperative form)
Keep it short but descriptive
Step Guidelines
Start with action verb
Be specific
Include context for complex steps
Use present tense
Keep steps focused
When to Use Tags
Use <lint> when running formatters or linters
Use <test> when running test suites
Use <shell> for other shell commands
Place tags on their own line after step description
Don't use tags if the step is just an instruction
Testing Your Command

After creating a command, test it by:

Syntax Check: Verify YAML is valid

# If you have yamllint installed
yamllint path/to/your-command.md


Manual Review: Read through the command

Does each step make sense?
Is the order logical?
Are all commands complete?

Execution Test: Run the command

Does each step execute successfully?
Is the output as expected?
Are there any errors?

Forge Recognition Test: Verify the command is recognized by forge

# Option 1: List all commands (custom commands marked as type: custom)
forge list command

# Option 2: List only custom commands
forge list cmd

# Option 3: List only custom commands (newer versions)
forge list command --custom

Does your command appear in the list?
Is the name correct?
Is the description correct?

Edge Cases: Consider unusual scenarios

What happens if a step fails?
What if the environment is different?
What if files are missing?
Verification

After creating a command:

Verify the file location: Ensure the file is in <cwd>/.forge/commands directory (CRITICAL - commands anywhere else will not be found)

Check YAML frontmatter is valid (use --- delimiters)

Ensure the command name matches the filename (without .md)

Verify the command is recognized by forge:

# Option 1: List all commands (custom commands marked as type: custom)
forge list command

# Option 2: List only custom commands
forge list cmd

# Option 3: List only custom commands (newer versions)
forge list command --custom


Your new command should appear in the list with its name and description

Test the command to ensure it works as expected

Verify special tags are properly formatted

If your command doesn't appear in the list, check:

File location: File MUST be in <cwd>/.forge/commands directory (this is the most common issue)
Filename matches the name field in frontmatter
YAML frontmatter is properly formatted with --- delimiters
Both name and description fields are present
Getting Help

If you're unsure about something:

Review the examples in this skill
Follow the validation checklist
Test your command before finalizing
Weekly Installs
43
Repository
antinomyhq/forge
GitHub Stars
7.1K
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass