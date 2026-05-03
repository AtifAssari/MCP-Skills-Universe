---
title: write-issue
url: https://skills.sh/tldraw/tldraw/write-issue
---

# write-issue

skills/tldraw/tldraw/write-issue
write-issue
Installation
$ npx skills add https://github.com/tldraw/tldraw --skill write-issue
SKILL.md
Writing and maintaining GitHub issues

Standards for issues in tldraw/tldraw.

Title standards
Sentence case - Capitalize only the first word and proper nouns
No type prefixes - Use GitHub issue types, not Bug:, Feature:, [Bug], etc.
Imperative mood for enhancements - "Add padding option" not "Adding padding option"
Descriptive for bugs - Describe the symptom: "Arrow bindings break with rotated shapes"
Specific - Readable without opening the issue body
Good titles
Arrow bindings break with rotated shapes
Add padding option to zoomToFit method
Pinch zoom resets selection on Safari
Bad titles
Bug: arrow bug (prefix, vague)
[Feature] Add new feature (prefix, vague)
Not working (vague)
Title cleanup transformations
Remove prefixes: Bug: X → X
Fix capitalization: Add Padding Option → Add padding option
Use imperative: Adding feature X → Add feature X
Be specific: Problem → [Describe the actual problem]
Translate non-English titles to English
Issue types

Set via the GitHub GraphQL API after creating the issue (the --type flag is not reliably supported):

Type	Use for
Bug	Something isn't working as expected
Feature	New capability or improvement
Example	Request for a new SDK example
Task	Internal task or chore
Labels

Use sparingly (1-2 per issue) for metadata, not categorization.

Common labels
Label	Use for
good first issue	Well-scoped issues for newcomers
More Info Needed	Requires additional information
sdk	Affects the tldraw SDK
dotcom	Related to tldraw.com
a11y	Accessibility
performance	Performance improvement
api	API change
Automation labels (do not apply manually)

keep, stale, update-snapshots, publish-packages, major, minor, skip-release, deploy triggers

Issue body standards
Bug reports
Clear description of what's wrong
Steps to reproduce
Expected vs actual behavior
Environment details (browser, OS, version) when relevant
Screenshots/recordings when applicable
Feature requests
Problem statement - What problem does this solve?
Proposed solution - How should it work?
Alternatives considered
Use cases
Example requests
What API/pattern to demonstrate
Why it's useful
Suggested approach
Which example category it belongs to
Triage workflow
New issues
Verify sufficient information to act on
Set appropriate issue type
Clean up title if needed
Add More Info Needed label and comment if details missing
Add good first issue if appropriate
Stale issues
Review if still relevant
Close if no longer applicable
Add keep label if should remain open
Request updates if waiting on information
Important
Never include AI attribution unless the issue directly relates to AI tooling
Never use title case for descriptions - use sentence case
Weekly Installs
290
Repository
tldraw/tldraw
GitHub Stars
46.8K
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn