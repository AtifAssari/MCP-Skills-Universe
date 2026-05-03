---
title: run-acceptance-tests
url: https://skills.sh/hashicorp/agent-skills/run-acceptance-tests
---

# run-acceptance-tests

skills/hashicorp/agent-skills/run-acceptance-tests
run-acceptance-tests
Installation
$ npx skills add https://github.com/hashicorp/agent-skills --skill run-acceptance-tests
Summary

Execute and diagnose Go acceptance tests for Terraform providers with structured troubleshooting.

Run focused acceptance tests using go test -run=TestAccFeatureHappyPath with TF_ACC=1 environment variable
Diagnose failures progressively: retry with -count=1, enable verbose output with -v, activate debug logging via TF_LOG=debug, and persist Terraform workspace with TF_ACC_WORKING_DIR_PERSIST=1
Validate test reliability by intentionally breaking a TestCheckFunc, re-running the test to confirm it fails, then reverting the change
Handle provider-specific environment variables by detecting missing variables in test output and guiding secure setup
SKILL.md

An acceptance test is a Go test function with the prefix TestAcc.

To run a focussed acceptance test named TestAccFeatureHappyPath:

Run go test -run=TestAccFeatureHappyPath with the following environment variables:

TF_ACC=1

Default to non-verbose test output.

The acceptance tests may require additional environment variables for specific providers. If the test output indicates missing environment variables, then suggest how to set up these environment variables securely.

To diagnose a failing acceptance test, use these options, in order. These options are cumulative: each option includes all the options above it.

Run the test again. Use the -count=1 option to ensure that go test does not use a cached result.
Offer verbose go test output. Use the -v option.
Offer debug-level logging. Enable debug-level logging with the environment variable TF_LOG=debug.
Offer to persist the acceptance test's Terraform workspace. Enable persistance with the environment variable TF_ACC_WORKING_DIR_PERSIST=1.

A passing acceptance test may be a false negative. To "flip" a passing acceptance test named TestAccFeatureHappyPath:

Edit the value of one of the TestCheckFuncs in one of the TestSteps in the TestCase.
Run the acceptance test. Expect the test to fail.
If the test fails, then undo the edit and report a successful flip. Else, keep the edit and report an unsuccessful flip.
Weekly Installs
1.1K
Repository
hashicorp/agent-skills
GitHub Stars
595
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail