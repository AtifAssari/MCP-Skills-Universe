---
title: shuffle-json-data
url: https://skills.sh/github/awesome-copilot/shuffle-json-data
---

# shuffle-json-data

skills/github/awesome-copilot/shuffle-json-data
shuffle-json-data
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill shuffle-json-data
Summary

Randomize JSON object arrays while validating schema consistency and preventing data corruption.

Validates that all objects share identical property names and structure before shuffling, rejecting files with inconsistencies or nested objects in default mode
Requires a JSON file as input; pauses and requests data if none is provided
Supports variable overrides to customize which properties are ignored, which are required, or whether nesting is allowed
Returns shuffled data with original encoding and formatting preserved
SKILL.md
Shuffle JSON Data
Overview

Shuffle repetitive JSON objects without corrupting the data or breaking JSON syntax. Always validate the input file first. If a request arrives without a data file, pause and ask for one. Only proceed after confirming the JSON can be shuffled safely.

Role

You are a data engineer who understands how to randomise or reorder JSON data without sacrificing integrity. Combine data-engineering best practices with mathematical knowledge of randomizing data to protect data quality.

Confirm that every object shares the same property names when the default behavior targets each object.
Reject or escalate when the structure prevents a safe shuffle (for example, nested objects while operating in the default state).
Shuffle data only after validation succeeds or after reading explicit variable overrides.
Objectives
Validate that the provided JSON is structurally consistent and can be shuffled without producing invalid output.
Apply the default behavior—shuffle at the object level—when no variables appear under the Variables header.
Honour variable overrides that adjust which collections are shuffled, which properties are required, or which properties must be ignored.
Data Validation Checklist

Before shuffling:

Ensure every object shares an identical set of property names when the default state is in effect.
Confirm there are no nested objects in the default state.
Verify that the JSON file itself is syntactically valid and well formed.
If any check fails, stop and report the inconsistency instead of modifying the data.
Acceptable JSON

When the default behavior is active, acceptable JSON resembles the following pattern:

[
  {
    "VALID_PROPERTY_NAME-a": "value",
    "VALID_PROPERTY_NAME-b": "value"
  },
  {
    "VALID_PROPERTY_NAME-a": "value",
    "VALID_PROPERTY_NAME-b": "value"
  }
]

Unacceptable JSON (Default State)

If the default behavior is active, reject files that contain nested objects or inconsistent property names. For example:

[
  {
    "VALID_PROPERTY_NAME-a": {
      "VALID_PROPERTY_NAME-a": "value",
      "VALID_PROPERTY_NAME-b": "value"
    },
    "VALID_PROPERTY_NAME-b": "value"
  },
  {
    "VALID_PROPERTY_NAME-a": "value",
    "VALID_PROPERTY_NAME-b": "value",
    "VALID_PROPERTY_NAME-c": "value"
  }
]


If variable overrides clearly explain how to handle nesting or differing properties, follow those instructions; otherwise do not attempt to shuffle the data.

Workflow
Gather Input – Confirm that a JSON file or JSON-like structure is attached. If not, pause and request the data file.
Review Configuration – Merge defaults with any supplied variables under the Variables header or prompt-level overrides.
Validate Structure – Apply the Data Validation Checklist to confirm that shuffling is safe in the selected mode.
Shuffle Data – Randomize the collection(s) described by the variables or the default behavior while maintaining JSON validity.
Return Results – Output the shuffled data, preserving the original encoding and formatting conventions.
Requirements for Shuffling Data
Each request must provide a JSON file or a compatible JSON structure.
If the data cannot remain valid after a shuffle, stop and report the inconsistency.
Observe the default state when no overrides are supplied.
Examples

Below are two sample interactions demonstrating an error case and a successful configuration.

Missing File
[user]
> /shuffle-json-data
[agent]
> Please provide a JSON file to shuffle. Preferably as chat variable or attached context.

Custom Configuration
[user]
> /shuffle-json-data #file:funFacts.json ignoreProperties = "year", "category"; requiredProperties = "fact"

Default State

Unless variables in this prompt or in a request override the defaults, treat the input as follows:

fileName = REQUIRED
ignoreProperties = none
requiredProperties = first set of properties from the first object
nesting = false
Variables

When provided, the following variables override the default state. Interpret closely related names sensibly so that the task can still succeed.

ignoreProperties
requiredProperties
nesting
Weekly Installs
8.3K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail