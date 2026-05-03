---
title: pytest-coverage
url: https://skills.sh/github/awesome-copilot/pytest-coverage
---

# pytest-coverage

skills/github/awesome-copilot/pytest-coverage
pytest-coverage
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill pytest-coverage
Summary

Run pytest with coverage reporting to identify and eliminate untested code lines.

Generates annotated source files in cov_annotate/ directory, with ! markers indicating uncovered lines
Supports module-specific coverage checks via --cov=module_name and targeted test runs on specific test files
Workflow: run coverage, review annotated files for uncovered lines, write tests to cover gaps, repeat until 100% coverage achieved
SKILL.md

The goal is for the tests to cover all lines of code.

Generate a coverage report with:

pytest --cov --cov-report=annotate:cov_annotate

If you are checking for coverage of a specific module, you can specify it like this:

pytest --cov=your_module_name --cov-report=annotate:cov_annotate

You can also specify specific tests to run, for example:

pytest tests/test_your_module.py --cov=your_module_name --cov-report=annotate:cov_annotate

Open the cov_annotate directory to view the annotated source code. There will be one file per source file. If a file has 100% source coverage, it means all lines are covered by tests, so you do not need to open the file.

For each file that has less than 100% test coverage, find the matching file in cov_annotate and review the file.

If a line starts with a ! (exclamation mark), it means that the line is not covered by tests. Add tests to cover the missing lines.

Keep running the tests and improving coverage until all lines are covered.

Weekly Installs
9.7K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass