---
title: init-repo
url: https://skills.sh/nathan13888/nice-skills/init-repo
---

# init-repo

skills/nathan13888/nice-skills/init-repo
init-repo
Installation
$ npx skills add https://github.com/nathan13888/nice-skills --skill init-repo
SKILL.md
Initializing Project

Scaffold a new project repository optimized for agentic development from a problem description -- or just set up ops tooling (git, precommits, gitignore, licensing, etc.) for an existing or empty project.

Quick Start

When invoked, follow the workflow below sequentially. After detecting the environment in Step 0, gather all preferences in a single Phase 1 intake form before executing any steps. This minimizes back-and-forth turns.

State Variables

Track these variables throughout the entire workflow. Once set, use the stored value -- never hardcode a branch name like main or master.

Variable	Set in	Description
{DEFAULT_BRANCH}	Step 0 (detected) or Phase 1	The repository's default branch name (e.g., main, master, develop). Every later step that references a branch MUST use this variable.
{PROJECT_KIND}	Phase 1	Whether the project is an Application (binary/executable) or Library (reusable code).
{INSTALLED_DEPS}	Step 5.5	List of recommended dependencies the user chose to install. Used in README (Step 10), CLAUDE.md (Step 11), and Summary (Step 12).
{LLVM_COV}	Phase 1	Whether LLVM coverage is enabled (yes/no). Only set for Rust projects with GitHub Actions CI.
{COV_THRESHOLD}	Phase 1	Minimum coverage percentage (e.g., 80), or empty if no threshold enforced.
{PACKAGES}	Phase 1	List of packages for multi-package projects. Each entry: {name, dir, lang, exts, format_fix_cmd, lint_fix_cmd, format_check_cmd, lint_check_cmd, test_cmd, coverage_cmd}. Only set when the project has multiple packages with different toolchains.
Workflow
Step 0: Detect Environment

Before anything else, check the current directory's state:

Run git rev-parse --is-inside-work-tree to see if the CWD is already inside a git repository (even if it has zero commits or is otherwise empty).
Run ls -A to check if the directory has any files/folders at all.
If it IS a git repo, note this -- we will NOT run git init later. Run git symbolic-ref --short HEAD to detect the current branch name. Store as {DETECTED_BRANCH}.
If it is NOT a git repo, note this -- we may need to initialize one later. Set {DETECTED_BRANCH} to main as the suggested default.

Report a brief one-line status note:

Detected: [git repo on branch {DETECTED_BRANCH} / no git repo], [empty / non-empty] directory at {CWD}.

Then proceed directly to Phase 1. Do NOT ask any questions here.

Phase 1: Project Intake

Call AskUserQuestion once with the comprehensive form below. Populate bracketed placeholders with values from Step 0 (e.g., {DETECTED_BRANCH}, {CWD}).

Let's set up your project. Fill in the fields below (skip sections that don't apply).

A. Project Basics

Problem description (what are you building? 1-2 sentences)

Project name (lowercase, kebab-case — leave blank to generate suggestions)

Location:

Here — use {CWD}
New subdirectory — name: ___

Scaffolding mode:

Full project — code + ops tooling
Ops only — git, .gitignore, license, CI, hooks, README, CLAUDE.md (no runtime/code)

B. Runtime & Language (skip if Ops only)

Choose one:

TypeScript (Bun) (Recommended for TypeScript) — fast runtime, built-in bundler/test runner
TypeScript (Node.js) — broader ecosystem compatibility
Python — data, ML/AI, scripting, automation
Rust — performance-critical, systems, CLI tools
Go — infrastructure, networking, microservices

TypeScript (Node.js) only:

Package manager: pnpm (default) / npm / yarn
Test runner: Vitest (default) / Jest / node:test

Python only:

Package manager: uv (default) / poetry / pip

Rust only:

Project kind: Application / Library

Go only:

Module path (e.g. github.com/username/project-name): ___

C. Code Quality (skip if Ops only)

Formatter/linter:

TypeScript: Biome (default) / ESLint+Prettier / ESLint flat config / oxlint
Python: Ruff (default) / Black+Flake8 / Black+Ruff
Rust: rustfmt+Clippy (only option)
Go: gofmt+go vet (default) / gofmt+golangci-lint

Task runner (Rust/Go only): just (default) / Makefile / neither

D. Project Kind (skip if Rust — already answered above; skip if Ops only)

Application — binary/executable (CLI, server, script, etc.)
Library — reusable code consumed by other projects

E. Dependencies (multi-select — check all to install; skip if Ops only)

TypeScript (Bun): [ ] zod — runtime type validation

TypeScript (Node.js): [ ] zod — runtime type validation [ ] dotenv — .env file loading

Python: [ ] pydantic — data validation [ ] python-dotenv — .env file loading [ ] httpx — async/sync HTTP client

Rust (universal — all projects): [ ] tracing — structured, async-aware logging [ ] thiserror — derive macro for std::error::Error [ ] serde + serde_json — serialization/deserialization

Rust (application only): [ ] eyre + color-eyre — flexible, colorful error reporting [ ] tokio (full) — async runtime

Go: [ ] github.com/rs/zerolog — high-performance structured logging

F. CI/CD

GitHub Actions (Recommended)
None
Other — system name: ___

Default branch name (pre-filled from detection: {DETECTED_BRANCH} — enter a different name to override): ___

G. Coverage (Rust + GitHub Actions only — leave blank if not applicable)

Coverage setup:

CI + pre-push hook (Recommended)
CI only
Hooks only
None / N/A

Minimum coverage threshold (percentage, e.g. 80 — leave blank for no threshold): ___

Coverage upload (CI only; ignored if hooks-only or none):

Artifact only (Recommended — works for all repos; uploads report as CI artifact with inline summary)
Codecov (open source only — requires CODECOV_TOKEN secret)
No upload

H. License

MIT (most common open-source)
Apache-2.0 (open source with patent protection)
GPL-3.0 (copyleft)
Dual (MIT + Apache-2.0) (Rust ecosystem standard)
Proprietary
None
Other — SPDX ID: ___ (for custom dual license, use SPDX-A+SPDX-B, e.g. MIT+GPL-3.0)

I. Extra .gitignore templates (multi-select — these supplement the primary runtime template)

[ ] macOS (.DS_Store, Spotlight index, Quarantine attrs) [ ] Linux (~backup files, .directory, .trash) [ ] Windows (Thumbs.db, Desktop.ini, ehthumbs.db) [ ] VSCode (.vscode/ folder, workspace settings) [ ] JetBrains *(.idea/, .iml, shelf/) [ ] Vim (swap, session, undo files) [ ] None of the above

(Ops only: also specify primary template — Node / Python / Rust / Go / None)

J. Git Hooks

Lefthook (Recommended — works with any runtime)
Native hooks (husky for TypeScript, pre-commit framework for Python, .git/hooks for Rust/Go)
None

Multi-package project?

No — single package (most projects)
Yes — list packages as name:dir:runtime pairs separated by commas: (e.g. api:api/:rust, web:web/:typescript-bun, worker:worker/:go) Valid runtime tokens: typescript-bun, typescript-node, python, rust, go Packages: ___

K. Docs

README.md:

Yes — concise README with overview and quick start (Recommended)
No

Agent context file:

AGENTS.md + CLAUDE.md symlink (Recommended for multi-agent setups)
CLAUDE.md only
No

Store all answers as state variables. Then apply these post-intake steps before proceeding to Step 1:

Post-intake: project name

If the project name was left blank, generate 2-3 kebab-case name suggestions derived from the problem description. Ask one follow-up AskUserQuestion:

Here are suggested project names based on your description:

{suggestion-1}
{suggestion-2}
{suggestion-3}
Enter my own: ___

Store the confirmed name and proceed to Step 1.

Post-intake: multi-package parsing

If multi-package was selected, parse the name:dir:runtime string into {PACKAGES}. For each entry, derive exts, format_fix_cmd, lint_fix_cmd, format_check_cmd, lint_check_cmd, test_cmd, and coverage_cmd from the runtime token. If any entry has an invalid format or unrecognized runtime token, report the parse error and ask one corrective follow-up before proceeding.

Post-intake: default branch

Store the confirmed (or detected) branch name as {DEFAULT_BRANCH}. This is used in every subsequent step that references a branch -- never re-ask.

Step 1: Understand the Problem

Use {PROBLEM_DESCRIPTION} from Phase 1. Summarize back your understanding before proceeding.

Step 1.5: Scaffolding Mode

Use {SCAFFOLDING_MODE} from Phase 1.

If the user picked Ops only, skip Steps 2-5.5 entirely and jump straight to Step 6 (CI/CD). The ops-only path still walks through CI, licensing, git setup, gitignore, precommits, README, and CLAUDE.md.

If the user picked Full project, continue with Step 2.

Step 2: Project Name

Use {PROJECT_NAME} from Phase 1 (confirmed in the post-intake step if it was left blank).

Naming rules:

Lowercase, kebab-case (my-project-name)
Short (1-3 words)
Descriptive of the solution, not the problem
Step 3: Runtime & Language

Use {RUNTIME} from Phase 1. Proceed with the appropriate section in Step 4.

Option	When to suggest
TypeScript (Bun)	Web apps, APIs, CLI tools, full-stack; fast runtime with built-in bundler/test runner
TypeScript (Node.js)	Web apps, APIs, CLI tools, full-stack; broader ecosystem compatibility
Python	Data, ML/AI, scripting, automation
Rust	Performance-critical, systems, CLI tools
Go	Infrastructure, networking, microservices
Step 4: Package Manager & Project Init

Based on {RUNTIME} from Phase 1, initialize the project:

TypeScript (Bun) (Recommended for TypeScript):

Run bun init
Update tsconfig.json with strict mode (Bun generates one; overwrite the compiler options to enable strict mode)
Refactor the generated entry point to export a testable function, and create a test file so bun test passes immediately and coverage tools report non-zero from the first commit:
// index.ts
export function greet(name: string): string {
  return `Hello, ${name}!`;
}

console.log(greet("world"));

// index.test.ts
import { expect, test } from "bun:test";
import { greet } from "./index";

test("greet returns greeting", () => {
  expect(greet("world")).toBe("Hello, world!");
});


TypeScript (Node.js):

Use {NODE_PKG_MANAGER} from Phase 1 (pnpm / npm / yarn)
Run the appropriate init command
Create tsconfig.json with strict mode
Use {NODE_TEST_RUNNER} from Phase 1 (Vitest / Jest / node --test). Install as a dev dependency (e.g., pnpm add -D vitest)
Create a testable entry point and test file so {test command} passes immediately:
Entry file (e.g., src/index.ts):
export function greet(name: string): string {
  return `Hello, ${name}!`;
}

Test file using the chosen runner. Vitest (src/index.test.ts):
import { expect, test } from "vitest";
import { greet } from "./index";

test("greet returns greeting", () => {
  expect(greet("world")).toBe("Hello, world!");
});

Jest (src/index.test.ts):
import { greet } from "./index";

test("greet returns greeting", () => {
  expect(greet("world")).toBe("Hello, world!");
});

node --test (src/index.test.ts):
import { strictEqual } from "node:assert";
import { test } from "node:test";
import { greet } from "./index.js";

test("greet returns greeting", () => {
  strictEqual(greet("world"), "Hello, world!");
});


Python:

Use {PYTHON_PKG_MANAGER} from Phase 1 (uv / poetry / pip)
Run the appropriate init command:
uv: uv init
poetry: poetry new {project-name} (or poetry init in an existing directory)
pip: There is no pip init. Create a minimal pyproject.toml manually:
[project]
name = "{project-name}"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = []

Set Python version (default to 3.12+): write requires-python = ">=3.12" in pyproject.toml and create a .python-version file with the pinned version (e.g., 3.12)
Install pytest as a dev dependency: uv add --dev pytest / poetry add --dev pytest / pip install pytest (and add to requirements-dev.txt)
Ensure the entry point exports a testable function and create a test so pytest passes immediately:
# src/{project_name}/main.py  (or the entry module uv/poetry generated)
def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("world"))

# tests/test_main.py
from {project_name}.main import greet

def test_greet() -> None:
    assert greet("world") == "Hello, world!"


Rust:

Use {PROJECT_KIND} from Phase 1 (Application or Library)
Run cargo init (for applications) or cargo init --lib (for libraries)
Create rust-toolchain.toml to pin the toolchain and ensure all contributors have formatting/linting/editor components:
[toolchain]
channel = "stable"
components = ["rustfmt", "clippy", "rust-analyzer"]

For applications (cargo init): refactor src/main.rs to extract a testable function so cargo test passes and cargo llvm-cov reports non-zero coverage from the first commit. Annotate fn main() with #[coverage(off)] so the entry-point boilerplate does not count against the threshold:
fn greeting() -> &'static str {
    "Hello, world!"
}

#[coverage(off)]
fn main() {
    println!("{}", greeting());
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_greeting() {
        assert_eq!(greeting(), "Hello, world!");
    }
}

For libraries (cargo init --lib): cargo init --lib already generates src/lib.rs with a passing it_works test -- no additional refactoring needed.

Go:

Use {GO_MODULE_PATH} from Phase 1 as the module path
Run go mod init
Create a testable entry point and test file so go test ./... passes immediately:
// main.go
package main

import "fmt"

// Greet returns a greeting string. Exported so it can be tested.
func Greet(name string) string {
	return fmt.Sprintf("Hello, %s!", name)
}

func main() {
	fmt.Println(Greet("world"))
}

// main_test.go
package main

import "testing"

func TestGreet(t *testing.T) {
	got := Greet("world")
	want := "Hello, world!"
	if got != want {
		t.Errorf("Greet() = %q, want %q", got, want)
	}
}

Step 5: Code Formatting & Linting

Use {FORMATTER_LINTER} from Phase 1. The user may have selected separate tools for formatting and linting, or a unified tool that handles both.

TypeScript / JavaScript:

Option	Type	Description
Biome (Recommended)	Formatter + Linter	Fast, unified tool, minimal config
ESLint + Prettier	Linter + Formatter	Most popular, huge plugin ecosystem
ESLint (flat config)	Linter only	If user wants linting without a formatter
oxlint	Linter	Extremely fast, Rust-based, drop-in ESLint alternative

Python:

Option	Type	Description
Ruff (Recommended)	Formatter + Linter	Extremely fast, replaces Black + Flake8 + isort
Black + Flake8	Formatter + Linter	Established, widely adopted
Black + Ruff	Formatter + Linter	Black formatting with Ruff linting

Rust:

Option	Type	Description
rustfmt + Clippy (Recommended)	Formatter + Linter	Standard Rust toolchain, no extra install

Go:

Option	Type	Description
gofmt + go vet (Recommended)	Formatter + Linter	Built into Go toolchain
gofmt + golangci-lint	Formatter + Linter	More comprehensive linting rules

After selection:

Install the chosen tools as dev dependencies

Create the appropriate config file(s):

Biome (biome.json): Run npx biome init to generate the config (biome is already installed from step 1). Then update the formatter section to use 2-space indentation:

"formatter": { "enabled": true, "indentStyle": "space", "indentWidth": 2 }


ESLint flat config (eslint.config.js) with TypeScript:

import tseslint from "typescript-eslint";
export default tseslint.config(tseslint.configs.recommended);


Ruff (ruff.toml):

line-length = 88
[lint]
select = ["E", "F", "I"]


rustfmt (rustfmt.toml): Can be empty to use defaults, or add:

edition = "2021"


golangci-lint (.golangci.yml):

linters:
  enable:
    - gofmt
    - govet
    - errcheck
    - staticcheck


Add format, lint, and lint:fix scripts to the project's task runner:

TypeScript (Bun/Node.js): package.json scripts
Python: Makefile targets (or pyproject.toml scripts if using uv run)
Rust: Use {TASK_RUNNER} from Phase 1 (just or Makefile)
Go: Use {TASK_RUNNER} from Phase 1 (just or Makefile — Makefile is idiomatic for Go)
Step 5.5: Recommended Dependencies

Use {PROJECT_KIND} from Phase 1. Use {SELECTED_DEPS} from Phase 1 as the list of dependencies to install. This step focuses on universal/foundational packages, NOT framework-specific choices.

Conditional logic

For Rust: if tracing is in {SELECTED_DEPS} and {PROJECT_KIND} is Application, automatically add tracing-subscriber to the install list if not already selected -- inform the user: "Adding tracing-subscriber since tracing needs a subscriber configured in the application to produce output."

For Library projects, eyre/color-eyre and tracing-subscriber should not be in {SELECTED_DEPS} -- these were not shown in the intake form for libraries. If they appear, skip them.

Dependency reference tables

Rust:

Dependency	Category	Description
tracing	Universal	Structured, async-aware diagnostic logging
thiserror	Universal	Derive macro for std::error::Error
serde (derive feature) + serde_json	Universal	Serialization/deserialization framework
eyre + color-eyre	Application only	Flexible, colorful error reporting for apps
tracing-subscriber	Application only	Configures tracing output for apps
tokio (full feature)	Application only	Async runtime

Install commands:

cargo add tracing
cargo add thiserror
cargo add serde --features derive and cargo add serde_json
cargo add eyre and cargo add color-eyre
cargo add tracing-subscriber
cargo add tokio --features full

TypeScript (Bun / Node.js):

Dependency	Category	Description
zod	Universal	Runtime type validation and schema declaration
dotenv	Universal	Load environment variables from .env files

Note: For Bun projects, skip dotenv -- Bun automatically loads .env files at startup via Bun.env. dotenv is only needed for Node.js.

Install (Bun): bun add {package} Install (Node.js): {npm install|yarn add|pnpm add} {package} (use {NODE_PKG_MANAGER} from Phase 1)

Python:

Dependency	Category	Description
pydantic	Universal	Data validation using Python type annotations
python-dotenv	Universal	Load environment variables from .env files
httpx	Universal	Modern async/sync HTTP client

Install:

uv: uv add {package}
poetry: poetry add {package}
pip: pip install {package} (and add to requirements.txt)

Go:

Go's standard library covers most foundational needs. Only suggest external dependencies when they provide substantial value over stdlib.

Dependency	Category	Description
github.com/rs/zerolog	Universal	High-performance structured logging

Install: go get {module_path}

Install selected dependencies

For each dependency in {SELECTED_DEPS}:

Run the appropriate install command (see tables above)
If a command fails, report the error and continue with the remaining dependencies -- do not abort the entire step
For crates/packages with feature flags, use the correct flags as noted in the tables

After all installations complete, summarize what was installed:

Installed dependencies:

{dep1} -- {description}
{dep2} -- {description}

Skipped / failed (if any):

{dep3} -- {reason}

Store the list of successfully installed dependencies as {INSTALLED_DEPS} for use in the README (Step 10), CLAUDE.md (Step 11), and Summary (Step 12).

Step 6: CI/CD

Use {CI_CD} from Phase 1.

Option	Description
GitHub Actions (Recommended)	Standard for GitHub repos
None	Skip CI/CD for now
Other	Use the name provided in Phase 1; help create a config file for that CI system, or skip and add a # TODO: add CI comment

Ops-only mode: If Steps 2-5.5 were skipped, there is no formatter, linter, or test runner configured. In this case, either skip CI entirely or create a minimal stub workflow with only actions/checkout@v4 and a # TODO: add format, lint, and test steps once tooling is set up comment. Inform the user that CI steps should be filled in after tooling is chosen.

If GitHub Actions is selected, create .github/workflows/ci.yml with:

Format check step (e.g., biome check, ruff format --check, cargo fmt --check)
Lint step (using the linter chosen in Step 5)
Test step (appropriate test runner for the chosen runtime) -- omit this step if no test framework has been installed
Triggered on push to {DEFAULT_BRANCH} and pull requests (use the exact branch name stored in {DEFAULT_BRANCH} -- do NOT hardcode main)

Note: The workflow file is created locally. The user must push the repository to GitHub and verify the workflow runs. Any required secrets (e.g., GITHUB_TOKEN, deployment keys) must be configured in the repository's Settings -> Secrets and variables -> Actions.

Step 6.5: LLVM Code Coverage (Rust only)

Skip this step unless the runtime is Rust AND GitHub Actions was selected in Step 6.

Use {LLVM_COV_MODE} from Phase 1. If any "Yes" option was selected, set {LLVM_COV} to yes.

Option	Description
Yes, CI + hooks (Recommended)	Add a coverage job to CI and a coverage check to the pre-push hook
Yes, CI only	Add a coverage job to GitHub Actions only
Yes, hooks only	Add a coverage check to the pre-push hook only
No	Skip code coverage

Use {COV_THRESHOLD} from Phase 1 (the minimum line coverage percentage, or empty for no threshold).

Use {COV_UPLOAD} from Phase 1 for coverage upload preference (Codecov / Artifact only / No upload).

Apply changes

Based on {LLVM_COV_MODE}, {COV_THRESHOLD}, and {COV_UPLOAD}, make the following modifications:

Install cargo-llvm-cov locally

Instruct the developer to install cargo-llvm-cov locally so hooks and task runner commands work:

cargo install cargo-llvm-cov  # or: cargo binstall cargo-llvm-cov (faster binary install)


Add this as a prerequisite note in the Summary (Step 12).

CI uses taiki-e/install-action@cargo-llvm-cov (pre-built binary). cargo install is only for local developer setup and should NOT be used in CI as it compiles from source and is significantly slower.

Update rust-toolchain.toml

Edit the components list to add llvm-tools-preview:

[toolchain]
channel = "stable"
components = ["rustfmt", "clippy", "rust-analyzer", "llvm-tools-preview"]

Update .github/workflows/ci.yml (if CI coverage was selected)

Add a coverage job to the workflow. Use taiki-e/install-action@cargo-llvm-cov for installation (pre-built binary -- do NOT use cargo install cargo-llvm-cov as it compiles from source and is slow):

  coverage:
    name: Coverage
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: dtolnay/rust-toolchain@stable
        with:
          components: llvm-tools-preview
      - uses: taiki-e/install-action@cargo-llvm-cov
      # If {COV_THRESHOLD} is set, combine report generation and threshold check into ONE step:
      - name: Generate coverage report
        run: cargo llvm-cov --lcov --output-path lcov.info --fail-under-lines {COV_THRESHOLD}
      # If NO threshold is set, omit --fail-under-lines:
      # - name: Generate coverage report
      #   run: cargo llvm-cov --lcov --output-path lcov.info
      # Include ONE of the following upload steps based on {COV_UPLOAD}:
      # Artifact only (default — works for all repos):
      - name: Generate coverage summary
        run: cargo llvm-cov report --summary-only
      - name: Upload coverage artifact
        uses: actions/upload-artifact@v4
        with:
          name: coverage-report
          path: lcov.info
      # Codecov (open source only — requires CODECOV_TOKEN secret):
      # - name: Upload to Codecov
      #   uses: codecov/codecov-action@v4
      #   with:
      #     files: lcov.info
      #     fail_ci_if_error: true
      #   env:
      #     CODECOV_TOKEN: ${{ secrets.CODECOV_TOKEN }}

Add coverage command to task runner (if a task runner was set up in Step 5)

If the project has a Makefile, Justfile, or similar task runner (set up in Step 5 alongside format, lint, and lint:fix), add a coverage recipe/target. This is what git hooks will call. CI does NOT use the task runner -- it runs cargo llvm-cov directly.

If {COV_THRESHOLD} is set, include --fail-under-lines {COV_THRESHOLD}. If not, omit it.

Example for a Justfile (with threshold):

coverage:
    cargo llvm-cov --fail-under-lines {COV_THRESHOLD}


Example for a Justfile (no threshold):

coverage:
    cargo llvm-cov


Example for a Makefile (with threshold):

coverage:
	cargo llvm-cov --fail-under-lines {COV_THRESHOLD}


Example for a Makefile (no threshold):

coverage:
	cargo llvm-cov


If no task runner exists, the git hooks (Step 9) will call cargo llvm-cov directly.

Coverage from day one: The scaffolded src/main.rs from Step 4 already includes a test covering greeting(), and fn main() is annotated with #[coverage(off)] so the entry-point boilerplate does not count against the threshold. This ensures cargo llvm-cov reports 100% coverage on the initial scaffold. Remind the user to annotate any future boilerplate entry points with #[coverage(off)] and raise the threshold as they add more code and tests.

Step 7: Licensing

Use {LICENSE} from Phase 1. If the user selected Other and specified a license SPDX ID, use that ID. If the ID contains a + separator (e.g., MIT+GPL-3.0), treat it as a custom dual-license.

CC license warning: If {LICENSE} is a CC license (CC-BY-*, CC-BY-SA-*), warn the user: "CC licenses are designed for creative works, not software. Creative Commons explicitly recommends against using CC licenses for software." Then ask one follow-up AskUserQuestion: "Confirm to proceed with {LICENSE}, or switch to: 1. MIT 2. Apache-2.0 3. Proceed anyway." This is the only license-related follow-up permitted.

Option	SPDX ID	Category	When to suggest
MIT	MIT	Permissive	Most common open-source license
Apache 2.0	Apache-2.0	Permissive	Open source with patent protection
GPL 3.0	GPL-3.0	Copyleft	Requires derivative works stay open
Dual License	(see below)	Permissive	Two licenses (e.g., MIT + Apache-2.0, Rust standard)
Proprietary	--	--	Private/commercial projects
None	--	--	Skip for now
Other	(see below)	--	Pick from expanded list

Proprietary: Create a LICENSE file containing: Copyright (c) {year} {copyright holder}. All rights reserved. No permissions are granted beyond reading the source code.

None: Skip license file creation entirely. Inform the user: "No license has been added. Without a license, the work is technically all rights reserved by default. Consider adding one before making the repository public."

Permissive: MIT . MIT-0 . Apache-2.0 . BSD-2-Clause . BSD-3-Clause . BSD-3-Clause-Clear . ISC . 0BSD . Unlicense . Zlib . CC0-1.0 . UPL-1.0

Copyleft: GPL-2.0 . GPL-3.0 . LGPL-2.1 . LGPL-3.0 . AGPL-3.0 . MPL-2.0 . EPL-1.0 . EPL-2.0 . EUPL-1.2 . OSL-3.0

Source-available: BSL-1.0

Other: CC-BY-4.0 . CC-BY-SA-4.0 . OFL-1.1 . MulanPSL-2.0 . WTFPL

Warning: CC licenses (CC-BY-*) are designed for creative works (art, documentation, data), not software. Creative Commons explicitly recommends against using CC licenses for software. If the user selects a CC license, warn them and suggest alternatives like MIT or Apache-2.0 instead. Proceed only if they confirm after the warning.

Fetching License Text

Fetch the license text using WebFetch from this skill's vendored license templates:

https://raw.githubusercontent.com/Nathan13888/nice-skills/master/data/licenses/{SPDX-ID}


After reading, replace placeholder fields with actual values:

<year> or [year] -> current year
<copyright holders> or [fullname] -> user's name from git config user.name (ask if not set)
Single License
Fetch the license text from the URL above
Replace placeholders
Write to LICENSE
Dual License

When {LICENSE} is a dual-license selection:

Identify the two licenses (pre-filled MIT + Apache-2.0, or the custom +-separated IDs from Phase 1)
Fetch both license texts in parallel via WebFetch
Replace placeholders in both
Create LICENSE-MIT and LICENSE-APACHE (pattern: LICENSE-{SHORT-NAME}). Use these short names for common licenses: MIT → MIT, Apache-2.0 → APACHE, GPL-3.0 → GPL3, GPL-2.0 → GPL2, LGPL-2.1 → LGPL, MPL-2.0 → MPL2. For unlisted licenses, use a short uppercase identifier derived from the SPDX ID.

Do NOT create a root LICENSE or LICENSE.md file for dual-licensed projects. GitHub's license detection cannot parse explanatory text and will show incorrect or confusing license information. The dual-license explanation belongs in the README's License section instead.

Step 8: Git Setup

Use the git repo status detected in Step 0 -- do NOT re-run the check.

If no repo was detected in Step 0:

Use {DEFAULT_BRANCH} from Phase 1 -- do NOT re-ask.
Run git init -b {DEFAULT_BRANCH} to initialize with that branch name.
Create .gitignore (see below)

Note: The initial commit is created at the end of Step 12 (after README, CLAUDE.md, and hooks have all been created). Do NOT commit here.

If a repo already exists (detected in Step 0):

Append new .gitignore content below a # === Added by init-repo === header rather than overwriting any existing .gitignore
If in Ops only mode, use {OPS_GITIGNORE_TEMPLATE} from Phase 1 as the primary template (Node / Python / Rust / Go / None)
Fetching .gitignore Templates

Fetch the primary .gitignore template for the chosen runtime using WebFetch:

Runtime	Template	URL
TypeScript (Bun/Node)	Node	https://raw.githubusercontent.com/github/gitignore/b4105e73e493bb7a20b5d7ea35efd5780ca44938/Node.gitignore
Python	Python	https://raw.githubusercontent.com/github/gitignore/b4105e73e493bb7a20b5d7ea35efd5780ca44938/Python.gitignore
Rust	Rust	https://raw.githubusercontent.com/github/gitignore/b4105e73e493bb7a20b5d7ea35efd5780ca44938/Rust.gitignore
Go	Go	https://raw.githubusercontent.com/github/gitignore/b4105e73e493bb7a20b5d7ea35efd5780ca44938/Go.gitignore

Bun projects: After fetching the Node template, append the following lines if not already present:

# === Bun ===
bun.lockb
bun.lock


(Bun v1.2+ uses bun.lock text format by default; older versions use binary bun.lockb. Include both to handle either.)

Use {EXTRA_GITIGNORE} from Phase 1 to determine which additional global ignores to append:

Option	Template Name
macOS	macOS
Linux	Linux
Windows	Windows
VSCode	VisualStudioCode
JetBrains	JetBrains
Vim	Vim
None of the above	(skip)

Global URL pattern: https://raw.githubusercontent.com/github/gitignore/b4105e73e493bb7a20b5d7ea35efd5780ca44938/Global/{Name}.gitignore

Combine templates into a single .gitignore with section headers:

# === Node ===
{fetched Node.gitignore content}

# === macOS ===
{fetched macOS.gitignore content}

Step 9: Git Hooks

Ops-only mode: If Steps 2-5.5 were skipped (no formatter, linter, or test runner configured), inform the user that hooks requiring those tools cannot be set up yet. Offer to either skip hooks entirely, or create a minimal commit-msg hook that checks for conventional commit format. Do NOT create hooks that reference format/lint/test commands that do not exist.

Use {GIT_HOOKS} from Phase 1. Use {IS_MULTI_PACKAGE} and {PACKAGES} from Phase 1.

Option	Description
Yes, with Lefthook (Recommended)	Universal git hooks manager; works with any language/runtime
Yes, with native hooks	Language-specific setup (husky, pre-commit framework, .git/hooks)
No	Skip git hooks

The hooks follow this convention:

Hook	Action
pre-commit	Auto-fix formatting and linting on staged files
pre-push	Check formatting and linting (no fix) + run tests

The rationale: pre-commit fixes what it can so the developer isn't blocked; pre-push is a final gate that catches anything unfixable and runs the full test suite before code reaches the remote.

Lefthook (universal, any runtime)

Lefthook is a fast, language-agnostic git hooks manager that works for any runtime.

Install lefthook (pick the method appropriate for the project):

TypeScript/Bun single-package projects: npm install --save-dev lefthook / bun add -d lefthook
Rust/Go/Python single-package projects (no npm): brew install lefthook (macOS/Linux via Homebrew) or download a binary release from GitHub
Go projects (alternative): go install github.com/evilmartians/lefthook@latest
Multi-package / mixed-runtime projects: Use brew install lefthook or the binary release regardless of which runtimes are present -- do NOT use a package manager install (e.g., npm install) as it would only be available within one package's scope

Use {IS_MULTI_PACKAGE} from Phase 1. If multi-package, use {PACKAGES} (parsed in the post-intake step) to get the list of packages with their names, directories, and runtimes.

Use the single-package template when {PACKAGES} has one entry; use the multi-package template when it has two or more.

Create lefthook.yml at the project root. Substitute the actual commands for the chosen runtime and formatter/linter:

Important: Pre-commit auto-fix commands must operate only on staged files to avoid silently modifying unstaged work. Use Lefthook's {staged_files} interpolation with a glob that matches the language's file extensions. For workspace-level tools like cargo fmt and cargo clippy that cannot be restricted to individual files, operating on the whole workspace is acceptable.

stage_fixed: true is required on format-fix and lint-fix commands. Without it, Lefthook modifies files in the working tree but those modifications are NOT re-staged, so the fixes never enter the commit. This would make auto-fix hooks silently useless.

Rust exception: cargo fmt and cargo clippy do NOT accept file arguments. For Rust, omit {staged_files} entirely -- the glob is used only to trigger the command when .rs files are staged, not to pass file names to the command. For all other languages, include {staged_files} in the run command.

Glob pattern must be recursive: Use "**/*.{ext}" (not "*.{ext}") to match files in all subdirectories (e.g., src/, lib/, tests/).

Single-package lefthook.yml
pre-commit:
  piped: true  # Runs command groups sequentially by priority; same-priority commands run in parallel
  commands:
    format-fix:
      priority: 1
      glob: "**/*.{ext}"  # replace {ext} with your language's extensions, e.g. ts,tsx,js,jsx or py
      stage_fixed: true   # REQUIRED: re-stages files modified by the fix command
      run: { format fix command } {staged_files} # e.g. biome format --write {staged_files}, ruff format {staged_files}
      # Rust: run: cargo fmt  (no {staged_files} -- cargo fmt operates on the whole workspace)
    lint-fix:
      priority: 2  # Runs AFTER format-fix completes (formatting can affect lint output)
      glob: "**/*.{ext}"
      stage_fixed: true   # REQUIRED: re-stages files modified by the fix command
      run: { lint fix command } {staged_files} # e.g. biome lint --fix {staged_files}, ruff check --fix {staged_files}
      # Rust: run: cargo clippy --fix --allow-dirty --allow-staged  (no {staged_files})

pre-push:
  commands:
    format-check:
      run: { format check command } # e.g. biome format --check, ruff format --check, cargo fmt --check
    lint-check:
      run: { lint check command } # e.g. biome lint, ruff check, cargo clippy -- -D warnings
    test:
      run: { test command } # e.g. bun test, pytest, cargo test, go test ./...
    # For Rust projects: include the following only if {LLVM_COV} is yes AND hooks coverage was selected:
    coverage:
      run: { just coverage | cargo llvm-cov [--fail-under-lines {COV_THRESHOLD}] } # use task runner command if available, otherwise raw cargo llvm-cov

Multi-package lefthook.yml

Use piped: true on pre-commit to enforce the format → lint ordering while running each phase's commands in parallel across packages. Use parallel: true on pre-push so all checks across all packages run concurrently (they are all read-only).

Command naming convention: {action}-{pkg.name} (e.g., format-fix-api, lint-check-web, test-worker).

The template below shows the pattern with placeholder package names. Generate one entry per package in {PACKAGES} — the actual names, paths, and commands are derived from the user's choices and may be 2, 3, 6, or more packages.

pre-commit:
  piped: true  # Commands run sequentially by priority; same-priority commands run in parallel
  commands:
    # --- Priority 1: format-fix (all packages run in parallel) ---
    # Repeat this block for each package, substituting {pkg.name}, {pkg.dir}, {pkg.exts}, and {pkg.format_fix_cmd}:
    format-fix-{pkg.name}:
      priority: 1
      root: "{pkg.dir}"
      glob: "{pkg.dir}**/*.{pkg.exts}"
      stage_fixed: true
      run: {pkg.format_fix_cmd} {staged_files}  # omit {staged_files} for Rust

    # --- Priority 2: lint-fix (all packages run in parallel, AFTER all format-fix completes) ---
    # Repeat this block for each package:
    lint-fix-{pkg.name}:
      priority: 2
      root: "{pkg.dir}"
      glob: "{pkg.dir}**/*.{pkg.exts}"
      stage_fixed: true
      run: {pkg.lint_fix_cmd} {staged_files}  # omit {staged_files} for Rust

pre-push:
  parallel: true  # All checks run concurrently (all are read-only)
  commands:
    # Repeat these blocks for each package:
    format-check-{pkg.name}:
      root: "{pkg.dir}"
      run: {pkg.format_check_cmd}
    lint-check-{pkg.name}:
      root: "{pkg.dir}"
      run: {pkg.lint_check_cmd}
    test-{pkg.name}:
      root: "{pkg.dir}"
      run: {pkg.test_cmd}
    # Include only if coverage is configured for this package:
    coverage-{pkg.name}:
      root: "{pkg.dir}"
      run: {pkg.coverage_cmd}


Concrete 3-package example (api in Rust, web in TypeScript/Bun, worker in Go):

pre-commit:
  piped: true
  commands:
    format-fix-api:
      priority: 1
      root: "api/"
      glob: "api/**/*.rs"
      stage_fixed: true
      run: cargo fmt
    format-fix-web:
      priority: 1
      root: "web/"
      glob: "web/**/*.{ts,tsx}"
      stage_fixed: true
      run: biome format --write {staged_files}
    format-fix-worker:
      priority: 1
      root: "worker/"
      glob: "worker/**/*.go"
      stage_fixed: true
      run: gofmt -w {staged_files}
    lint-fix-api:
      priority: 2
      root: "api/"
      glob: "api/**/*.rs"
      stage_fixed: true
      run: cargo clippy --fix --allow-dirty --allow-staged
    lint-fix-web:
      priority: 2
      root: "web/"
      glob: "web/**/*.{ts,tsx}"
      stage_fixed: true
      run: biome lint --fix {staged_files}
    lint-fix-worker:
      priority: 2
      root: "worker/"
      glob: "worker/**/*.go"
      stage_fixed: true
      run: golangci-lint run --fix ./...

pre-push:
  parallel: true
  commands:
    format-check-api:
      root: "api/"
      run: cargo fmt --check
    format-check-web:
      root: "web/"
      run: biome format --check .
    format-check-worker:
      root: "worker/"
      run: test -z "$(gofmt -l .)"
    lint-check-api:
      root: "api/"
      run: cargo clippy -- -D warnings
    lint-check-web:
      root: "web/"
      run: biome lint .
    lint-check-worker:
      root: "worker/"
      run: go vet ./...
    test-api:
      root: "api/"
      run: cargo test
    test-web:
      root: "web/"
      run: bun test
    test-worker:
      root: "worker/"
      run: go test ./...
    coverage-api:
      root: "api/"
      run: cargo llvm-cov --fail-under-lines 80

Run lefthook install to activate the hooks.
Native hooks (language-specific)

Multi-package projects: Native hooks do not support structured parallel execution across packages. If the project has multiple packages with different toolchains, strongly recommend Lefthook instead. Native hooks are only suitable for single-package projects.

If {GIT_HOOKS} is native hooks:

TypeScript (Bun/Node.js):

Install husky and lint-staged:

Bun: bun add -d husky lint-staged
npm/pnpm/yarn: {pkg manager} add -D husky lint-staged

Initialize husky: npx husky init (creates .husky/ directory and a sample pre-commit file)

Configure lint-staged in package.json:

"lint-staged": {
  "*.{ts,tsx,js,jsx}": [
    "{ format fix command }",
    "{ lint fix command }"
  ]
}


Write .husky/pre-commit:

#!/bin/sh
npx lint-staged


Write .husky/pre-push:

#!/bin/sh
{ format check command } && { lint check command } && { test command }


Add "prepare": "husky" to package.json scripts so hooks are installed automatically after npm install.

Python:

Install pre-commit framework
Create .pre-commit-config.yaml with:
Pre-commit stage hooks that fix (e.g., ruff format, ruff check --fix)
Pre-push stage hooks for format check, lint check, and pytest using stages: [pre-push]
Run pre-commit install --hook-type pre-commit --hook-type pre-push
Do NOT create a separate .git/hooks/pre-push script -- pre-commit install --hook-type pre-push already writes that file, and a manual script would overwrite the framework's hook

Rust:

Create .git/hooks/pre-commit: runs cargo fmt (fix) and cargo clippy --fix --allow-dirty --allow-staged (--allow-dirty --allow-staged is required because cargo fix refuses to run when files are staged, which is always the case in a pre-commit hook)
Create .git/hooks/pre-push: runs cargo fmt --check, cargo clippy -- -D warnings, and cargo test
If {LLVM_COV} is yes and hooks coverage was selected, also append a coverage step to .git/hooks/pre-push:
If a task runner exists: call just coverage (or the equivalent Make target)
Otherwise: call cargo llvm-cov directly (with --fail-under-lines {COV_THRESHOLD} if a threshold is set)
Make both scripts executable (chmod +x)

Go:

Create .git/hooks/pre-commit: fixes only staged .go files. Must guard against the empty-list case -- gofmt -w with no arguments reads from stdin and hangs forever if no .go files are staged. Use:
GO_FILES=$(git diff --cached --name-only --diff-filter=d | grep '\.go$' || true)
[ -n "$GO_FILES" ] && gofmt -w $GO_FILES

If golangci-lint is installed (command -v golangci-lint >/dev/null 2>&1), also run it. Note: golangci-lint run --fix operates on the entire module, not just staged files -- this is an acceptable exception (like cargo fmt) since golangci-lint has no per-file mode.
Create .git/hooks/pre-push: runs test -z "$(gofmt -l .)" (fails non-zero if any files are unformatted -- gofmt -l alone exits 0 and would not block the push), go vet ./..., and go test ./...
Make both scripts executable (chmod +x)
Step 10: README.md

Use {WANTS_README} from Phase 1.

First, check if a README.md already exists in the project directory. If it does, ask the user whether to overwrite or skip before proceeding.

If {WANTS_README} is Yes, create README.md using the appropriate template below. Fill in all placeholders with the values collected in earlier steps. Omit any section entirely if that feature was not set up (e.g., no Git Hooks section if the user skipped Step 9).

Full project template

The ## Prerequisites section lists each tool the developer must manually install. Use the reference table below to determine which lines to include. Omit the section entirely if no tools require manual installation.

# {Project Name}

{One-line problem description}

## Prerequisites

- [{runtime name}]({runtime url}) -- {runtime role}
- [{package manager}]({url}) -- package manager
- [just](https://github.com/casey/just) -- command runner
- [Lefthook](https://github.com/evilmartians/lefthook) -- git hooks manager
- [cargo-llvm-cov](https://github.com/taiki-e/cargo-llvm-cov) -- code coverage tool
- [golangci-lint](https://golangci-lint.run) -- Go linter

## Quick Start

\`\`\`bash
{install command}
{run/dev command}
\`\`\`

## Development

| Command              | Description          |
| -------------------- | -------------------- |
| `{install command}`  | Install dependencies |
| `{run/dev command}`  | Start development    |
| `{test command}`     | Run tests            |
| `{format command}`   | Format code          |
| `{lint fix command}` | Lint and auto-fix    |

## Tech Stack

- **Runtime:** {runtime}
- **Language:** {language}
- **Package Manager:** {package manager}
- **Formatter:** {formatter}
- **Linter:** {linter}
- **Key Dependencies:** {comma-separated list from {INSTALLED_DEPS}, or omit this line if none were installed}

## Git Hooks

This project uses {Lefthook/husky/pre-commit/native hooks}. Pre-commit hooks auto-fix formatting and linting on staged files. Pre-push hooks run format checks, lint checks, and tests.

## CI/CD

GitHub Actions runs format checks, linting, and tests on pushes to `{DEFAULT_BRANCH}` and pull requests.

## Code Coverage

<!-- Include this section only if {LLVM_COV} is yes -->

This project uses [`cargo-llvm-cov`](https://github.com/taiki-e/cargo-llvm-cov) for LLVM-based code coverage.{If COV_THRESHOLD is set: ` CI enforces a minimum of {COV_THRESHOLD}% line coverage.`}

\`\`\`bash
cargo llvm-cov
\`\`\`

## License

{License name} -- see [LICENSE](LICENSE) for details.


For dual-licensed projects, replace the License section with:

## License

Licensed under either of [{License A}](LICENSE-A) or [{License B}](LICENSE-B) at your option.

Ops-only template

When in ops-only mode (no runtime/language was chosen), use this shorter template. Use the directory name as the heading if no project name was set in Step 2. Omit any section entirely if that feature was not set up (e.g., no Git Hooks section if hooks were skipped, no CI/CD section if CI was skipped, no License section if licensing was skipped).

Omit the ## Prerequisites section entirely if no tools require manual installation (e.g., if hooks were skipped). For ops-only mode, typically only Lefthook needs to be listed.

# {Project Name or directory name}

{One-line problem description}

## Prerequisites

- [Lefthook](https://github.com/evilmartians/lefthook) -- git hooks manager

## Git Hooks

This project uses {Lefthook/native hooks}. Pre-commit hooks auto-fix formatting and linting on staged files. Pre-push hooks run format checks, lint checks, and tests.

## CI/CD

GitHub Actions runs format checks, linting, and tests on pushes to `{DEFAULT_BRANCH}` and pull requests.

## License

{License name} -- see [LICENSE](LICENSE) for details.


For dual-licensed projects, replace the License section with:

## License

Licensed under either of [{License A}](LICENSE-A) or [{License B}](LICENSE-B) at your option.


The README should be concise -- no badges, no Contributing section, no boilerplate. Its purpose is to give visitors a quick orientation and prevent AI agents from later generating verbose READMEs.

Prerequisites section reference

Use this table to determine which tools belong in the Prerequisites section. Include only tools that require manual installation -- dev dependencies auto-installed by bun install, npm install, cargo build, uv sync, etc. do not need to be listed.

Tool	URL	Include when
Bun	https://bun.sh	Runtime is TypeScript (Bun)
Node.js	https://nodejs.org	Runtime is TypeScript (Node.js)
pnpm	https://pnpm.io	Package manager is pnpm
Yarn	https://yarnpkg.com	Package manager is yarn
Python	https://python.org	Runtime is Python
uv	https://github.com/astral-sh/uv	Package manager is uv
Poetry	https://python-poetry.org	Package manager is poetry
Rust (rustup)	https://rustup.rs	Runtime is Rust
Go	https://go.dev	Runtime is Go
just	https://github.com/casey/just	Task runner is just
Lefthook	https://github.com/evilmartians/lefthook	Git hooks use Lefthook
cargo-llvm-cov	https://github.com/taiki-e/cargo-llvm-cov	{LLVM_COV} is yes
golangci-lint	https://golangci-lint.run	Linter is golangci-lint

Not included: Biome, ESLint, Prettier, Ruff, rustfmt, Clippy, golint, gofmt -- these are either bundled with the runtime toolchain or installed as dev dependencies by the package manager.

Step 11: CLAUDE.md

Use {CLAUDE_MD_FORMAT} from Phase 1 (AGENTS.md + symlink, CLAUDE.md only, or No).

If {CLAUDE_MD_FORMAT} is AGENTS.md + symlink, create the file as AGENTS.md and then run:

ln -s AGENTS.md CLAUDE.md


Use the appropriate template below based on the mode chosen in Step 1.5. Fill in all placeholders with values collected in earlier steps. Omit any section that was not set up (e.g., no Coverage section if {LLVM_COV} is not yes).

Full project template
# {Project Name}

{One-line problem description}

## Packages

<!-- Omit this section if no packages were installed ({INSTALLED_DEPS} is empty). For each installed package, state its intended use in this project -- not a generic description. -->

- **{dep}** -- {project-specific purpose, e.g., "structured logging for request tracing" not "a logging library"}

## Quality

Validate changes:

```bash
{test command}           # correctness
{format check command}   # formatting
{lint command}           # lint
```

<!-- Append this block only if {LLVM_COV} is yes: -->
```bash
{coverage command}       # coverage (minimum {COV_THRESHOLD}%)
```

<!-- Use the task runner command (e.g., `just test`) when a Justfile/Makefile was set up; otherwise use the raw tool command. -->

{Stack-specific code quality rules for this project. These are concrete, enforceable preferences -- not generic advice. Examples by stack:}
{- TypeScript: "No `any` types -- use `unknown` with type guards."}
{- Rust: "All `pub` items need doc comments. Mark fallible return types with `#[must_use]`."}
{- Python: "Type annotations required on all function signatures."}
{- Go: "Handle all errors explicitly -- no `_` for error returns."}

Ops-only template

Omit any section entirely if that feature was not set up (e.g., no Git Hooks section if hooks were skipped, no CI/CD section if CI was skipped, no License section if licensing was skipped).

# {Project Name or directory name}

{One-line problem description}

## Git Hooks

This project uses {Lefthook/native hooks}. Pre-commit hooks auto-fix formatting and linting on staged files. Pre-push hooks run format checks, lint checks, and tests.

## CI/CD

GitHub Actions runs checks on pushes to `{DEFAULT_BRANCH}` and pull requests.

## License

{License name} -- see [LICENSE](LICENSE) for details.


For dual-licensed projects, replace the License section with:

## License

Licensed under either of [{License A}](LICENSE-A) or [{License B}](LICENSE-B) at your option.

Step 12: Summary

For new repos (git was initialized in Step 8): Before printing the summary, create the initial commit now that all files (hooks, README, CLAUDE.md) exist, then push if a remote is configured (so pre-push hooks are verified immediately):

git add -A
git commit -m "chore: initialize project"
# Push if origin is already configured (e.g., user pre-created the remote):
git remote get-url origin 2>/dev/null && git push -u origin {DEFAULT_BRANCH}


If the user is on an existing repo and requested an initial commit (Step 8), do that now as well, then push if origin is configured.

Print a summary of everything that was created. Adapt the summary to the chosen mode:

Full project mode:


Project initialized: {name}
Location: {path}
Runtime: {runtime}
Package Manager: {pkg manager}
Formatter: {formatter}
Linter: {linter}
Dependencies: {count} installed ({comma-separated names from {INSTALLED_DEPS}}, or "none" if skipped)
License: {license(s)}
CI/CD: {ci/cd}
Coverage: {cargo-llvm-cov (threshold: {COV_THRESHOLD}%, upload: {artifact/Codecov/none}) | none}
Pre-commit: {yes/no}

Files created:
{list of files -- if AGENTS.md + symlink was chosen, show both AGENTS.md and CLAUDE.md -> AGENTS.md}

Next steps:

1. {install command}
2. Push to GitHub and verify GitHub Actions workflows run correctly
   - Configure any required secrets in Settings -> Secrets and variables -> Actions
   - {If Codecov upload was chosen: Configure `CODECOV_TOKEN` secret in Settings -> Secrets and variables -> Actions (note: Codecov is free for open-source repos only)}
3. Start building!



Ops only mode:


Ops tooling initialized
Location: {path}
License: {license(s)}
CI/CD: {ci/cd}
Pre-commit: {yes/no}

Files created:
{list of files -- if AGENTS.md + symlink was chosen, show both AGENTS.md and CLAUDE.md -> AGENTS.md}

Next steps:

1. Push to GitHub and verify GitHub Actions workflows run correctly
   - Configure any required secrets in Settings -> Secrets and variables -> Actions
2. Start building!



Reminder: GitHub Actions workflows only run once the repository is pushed to GitHub. If you haven't created the remote repository yet, do that first (gh repo create or via the GitHub UI), then add the remote and push:

git remote add origin {remote URL}
git push -u origin {DEFAULT_BRANCH}


Use the exact {DEFAULT_BRANCH} value confirmed/set earlier -- do NOT substitute main or any other name. The remote name origin is conventional; if the user has a different remote name, use that instead.

If the project was created in the current directory, do NOT include a cd step -- the user is already there.

Guidelines
Gather all preferences in Phase 1 before creating any files. Do not assume defaults -- if the user's Phase 1 response is ambiguous or missing a required field, ask one clarifying follow-up before proceeding.
Use AskUserQuestion with concrete options, not open-ended prompts. Outside of Phase 1, AskUserQuestion is permitted only for: (1) project name suggestions if left blank, (2) CC license warning confirmation, (3) multi-package input correction, and (4) overwrite confirmation if a README already exists.
Phase 1 must be completed in a single AskUserQuestion call. Do not split it across multiple calls.
If a tool is not installed (e.g., bun, uv), offer to install it or suggest an alternative
All files MUST be created in the chosen project directory (CWD or the user's subdirectory choice from Phase 1) -- never in a parent, sibling, or unrelated directory
Check if the target directory already exists before creating anything
Keep the initial project minimal -- don't over-scaffold
Respect the user's choice to skip code scaffolding -- ops-only mode is a first-class path, not a fallback
The CLAUDE.md should be practical and specific, not boilerplate
Detect git user.name and user.email from git config for license attribution
If the user provides a GitHub username, use it for module paths and license
Use WebFetch with prompt "Return the full file content exactly as-is" to get raw template text without summarization
If WebFetch fails for any URL, fall back to generating content from memory and inform the user
For dual-license, fetch both license texts in parallel to minimize latency
When adding LLVM coverage for Rust in CI, use taiki-e/install-action@cargo-llvm-cov (pre-built binary) -- do NOT use cargo install cargo-llvm-cov as it compiles from source and is significantly slower
Git hooks should call the task runner coverage command (e.g., just coverage) when a task runner is configured; CI always uses raw cargo llvm-cov commands directly
Annotate entry-point boilerplate with #[coverage(off)] (e.g., fn main()) so non-logic code does not count against coverage thresholds -- apply this in scaffolded templates and instruct users to do the same for any future entry-point code
Pre-commit hooks must only modify staged files -- use {staged_files} interpolation in Lefthook, lint-staged for TypeScript/Node.js native hooks, and file-list filtering in shell scripts; tools that only operate on the whole workspace (e.g., cargo fmt, cargo clippy --fix, golangci-lint run --fix) are acceptable exceptions because they have no per-file mode
cargo clippy --fix requires --allow-dirty --allow-staged in any git hook context -- without these flags it always fails when files are staged
Lefthook pre-commit fix commands must include stage_fixed: true -- without it, modifications made by the fix command stay in the working tree and are not included in the commit, making auto-fix hooks silently ineffective
The README Prerequisites section must list only tools that require manual installation -- do NOT list dev dependencies auto-installed by bun install, npm install, cargo build, uv sync, etc.
Scaffolded projects for all languages must include at least one meaningful test so {test command} passes and any coverage tool reports non-zero coverage from the first commit; use the greet/greeting function pattern from Step 4 as the initial test scaffold
For multi-package projects (monorepos or projects with multiple toolchains), use the multi-package Lefthook template with piped: true + priority for pre-commit and parallel: true for pre-push; package names and directories must always be derived from the user's choices -- never hardcode names like "frontend" or "backend"
Weekly Installs
23
Repository
nathan13888/nice-skills
GitHub Stars
5
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn