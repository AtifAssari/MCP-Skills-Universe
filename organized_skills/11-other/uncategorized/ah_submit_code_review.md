---
rating: ⭐⭐⭐⭐⭐
title: ah-submit-code-review
url: https://skills.sh/arinhubcom/arinhub/ah-submit-code-review
---

# ah-submit-code-review

skills/arinhubcom/arinhub/ah-submit-code-review
ah-submit-code-review
Installation
$ npx skills add https://github.com/arinhubcom/arinhub --skill ah-submit-code-review
SKILL.md
Submit Code Review

Submit a structured code review with line-specific comments to a GitHub pull request. Identifies issues in the current chat session or review file, checks for duplicate comments, and submits the review.

Input
PR number or URL (required): The pull request identifier. Accepts:
Number: 123
Hash-prefixed: #123
Full URL: https://github.com/owner/repo/pull/123
Review file path (optional): Path to a review file produced by ah-review-code (e.g., ~/.agents/arinhub/code-reviews/code-review-pr-my-app-123.md). If provided, issues are extracted from this file instead of the current chat session.
Procedure
1. Resolve PR Identifier

Extract the PR number from the user input. Strip any # prefix or parse the number from a URL. Also resolve the repository owner and name for API calls.

PR_NUMBER=<extracted number>
REPO_OWNER=$(gh repo view --json owner -q '.owner.login')
REPO_NAME=$(basename -s .git "$(git remote get-url origin)")

2. Fetch PR Metadata

Gather PR details:

gh pr view $PR_NUMBER --json number,title,body,baseRefName,headRefName,files,url

3. Verify Requirements Coverage

Check whether requirements coverage data is already available:

Review file provided: If a review file path was given, check whether it contains a ## Requirements Coverage section. If yes, extract the coverage percentage and summary — no further action needed.
Current chat session: If no review file was provided, check the current chat session for output from a previous ah-verify-requirements-coverage invocation (sections starting with ## Requirements Coverage:). If found, use that data — no further action needed.
No coverage data available: If neither source contains requirements coverage, spawn a subagent to execute the /ah-verify-requirements-coverage skill:
Pass the PR number resolved in Step 1.
If a linked issue number is known (e.g., from the review file or PR body), pass it as well.
Store the resulting coverage report for use when composing the main review comment in Step 8.

If the subagent cannot find a linked issue (e.g., the PR body has no closing keywords and no explicit issue reference), proceed without coverage data — the main review comment will note that coverage data is unavailable.

4. Fetch Existing Review Comments

Retrieve all existing review comments to prevent duplication:

gh api repos/$REPO_OWNER/$REPO_NAME/pulls/$PR_NUMBER/comments --paginate --jq '.[] | {id, path, line, body, user: .user.login}'


Also fetch top-level review bodies:

gh api repos/$REPO_OWNER/$REPO_NAME/pulls/$PR_NUMBER/reviews --paginate --jq '.[] | {id, body, state, user: .user.login}'

5. Get Issue List

Get a list of issues from one of these sources (in priority order):

Review file: If a review file path is provided (e.g., from ah-review-code orchestrator), read the file and extract all issues from the ## Issues section.
Current chat session: If no review file is specified, collect issues identified during the code review in the current chat session.

For each issue found, record:

severity: One of High Priority, Medium Priority, or Low Priority
title: A short descriptive title for the issue (e.g., "Unvalidated user input passed to SQL query")
path: The relative file path
file_in_diff: Whether the file appears in the PR diff (true or false). Issues with file_in_diff: false cannot be posted as inline thread comments -- they are included in the main review body instead (see Step 8).
line: The specific line number in the new version of the file. For multi-line issues, this is the last line of the range.
start_line (optional): The first line of a multi-line range. Only set when the issue spans more than one line.
explanation: A concise, actionable comment explaining the issue (the "why", not just the "what")
suggestion (optional): Raw replacement code for a concrete fix. Only set for simple, contiguous changes (see Suggestion conversion rules). When set, this code replaces lines start_line (or line) through line verbatim. Do not include ```suggestion fences -- they are added automatically in Step 8. For complex suggestions (multiple diff blocks or non-contiguous changes), do not set this field; instead append the diff block(s) to explanation.
Parsing a review file

The review file from ah-review-code uses a different format than the submission API. Apply these transformations when extracting issues:

Review file field	Maps to	Transformation
**Severity:** High Priority	severity	Use the value directly (High Priority, Medium Priority, or Low Priority)
Issue heading (#### <text>)	title	Use the heading text as the title
**Source:** ...	(skip)	Informational only -- not used in submission
**File:** path/to/file.ts	path	Use the path directly. Strip any markdown link syntax (e.g., [`path:42`](/abs/path#L42) → path) and any :line or :line-line suffix
**File In Diff:** true or false	file_in_diff	Use the boolean value directly. If the field is missing, default to true
**Line(s):** 42	line: 42	Single line: set line only
**Line(s):** 42-50	start_line: 42, line: 50	Range: set start_line to the first number, line to the second
**Line(s):** 77, 324-325	Split into separate issues	Comma-separated values indicate multiple locations. Create one issue per segment (e.g., line: 77 and start_line: 324, line: 325), each sharing the same severity, title, path, file_in_diff, and explanation. Duplicate the suggestion only if it applies to each segment; otherwise omit suggestion from both and append the original diff block(s) to explanation instead.
**Description:** ...	explanation	Use as the explanation text
**Code:** ```...``` block	(skip)	Informational only -- not used in submission
**Suggestion:** ```diff ``` block	suggestion or explanation appendix	See Suggestion conversion rules below.
Suggestion conversion rules

A **Suggestion:** section in the review file may contain one or more ```diff ``` blocks. Apply these rules to decide how to handle it:

Convert to suggestion (simple case) -- when the suggestion contains exactly one diff block and all changed lines (+/- lines) form a contiguous group (no unchanged context lines between separate groups of changes):

Remove lines starting with - (deletions).
For lines starting with +, remove the leading + prefix. If a single space follows the +, remove that space as well (it is the diff marker separator, not part of the code). If no space follows the + (e.g., an empty added line), remove only the +.
The result is the raw replacement code -- store it in suggestion.

Example:

Review file:

- const result = unsafeOperation(input);
+ const result = safeOperation(sanitize(input));


Extracted suggestion (raw replacement code):

const result = safeOperation(sanitize(input));


Keep as markdown diff (complex case) -- when any of these conditions is true:

The suggestion contains multiple ```diff ``` blocks
The diff block contains non-contiguous changes (changed lines separated by unchanged context lines, indicating edits at distant locations within the file)

In this case:

Do not set the suggestion field.
Append the original ```diff ``` block(s) verbatim to the explanation text (separated by a blank line).
The comment will be posted as a pure observation (without a GitHub suggestion "Apply" button).

Example -- multiple diff blocks (keep as diff):

Review file:

```diff
- import { foo } from './utils';
+ import { foo, bar } from './utils';
```

```diff
- foo(data);
+ bar(foo(data));
```


Result: suggestion is not set. The two diff blocks are appended to explanation as-is.

Example -- non-contiguous changes within a single diff block (keep as diff):

Review file:

  function process(input) {
-   const raw = input;
+   const raw = sanitize(input);
    // ... many unchanged lines ...
    const config = loadConfig();
-   return execute(raw, config);
+   return executeSafely(raw, config);
  }


Result: suggestion is not set. The diff block is appended to explanation as-is.

6. Deduplicate Comments

For each issue identified in Step 5, compare against existing comments from Step 4:

Skip if an existing comment on the same path and line (or nearby range +/- 5 lines) already addresses the same concern
Skip if the issue is already mentioned in any top-level review body
Use semantic comparison, not exact string matching -- if the existing comment covers the same problem, even with different wording, skip the new comment
7. Decision Gate
If no new issues remain after deduplication (neither inline nor non-diff): Do not submit a review. Inform the user that no new issues were found beyond existing review comments.
If new issues exist (inline, non-diff, or both): Proceed to Step 8. A review with only non-diff issues is still submitted -- the issues appear in the main review body even though there are no inline thread comments.
8. Submit the Review

Submit a single review via the GitHub API. The review consists of one main review comment with individual thread comments that appear as conversation threads anchored to specific lines in the diff.

Main review comment (body): You MUST use the Read tool to read references/main-review-comment.md before composing the main review body. Follow its template and formatting exactly.

Thread comments (comments[].body): You MUST use the Read tool to read references/thread-comment.md before composing any thread comment. Follow its template and formatting exactly.

Separating inline vs. non-diff issues

Before building the payload, split the deduplicated issues into two groups:

Inline issues (file_in_diff: true): Posted as thread comments anchored to specific lines in the diff.
Non-diff issues (file_in_diff: false): Cannot be posted as thread comments (the API would reject them). Instead, these are appended to the main review body as a dedicated section. However, only include a non-diff issue if it is directly relevant to the PR body context (e.g., the change described in the PR description or the files/features the PR touches) or the requirements coverage context (e.g., a requirement from the linked issue that the PR should address). If a non-diff issue falls outside both of these contexts, drop it — do not include it in the review body. The issues table in Step 9 will still list all non-diff issues, but the "Reason" column will explain why any non-diff issue was excluded from the review body.
Determining event type
Use "REQUEST_CHANGES" if any issue (inline or non-diff) with severity High Priority or Medium Priority remains after deduplication.
Use "APPROVE" if all remaining issues (inline and non-diff) are Low Priority only.
Comment types

Each entry in comments uses one of two shapes depending on whether the issue targets a single line or a range of lines:

Single-line comment -- targets exactly one line in the diff:

{
  "path": "src/auth.ts",
  "line": 42,
  "side": "RIGHT",
  "body": "<thread-comment>"
}


Required fields: path, line, side.

Multi-line comment -- targets a range from start_line through line (both inclusive, both must be within the same diff hunk):

{
  "path": "src/utils.ts",
  "start_line": 10,
  "line": 14,
  "start_side": "RIGHT",
  "side": "RIGHT",
  "body": "<thread-comment>"
}


Required fields: path, start_line, line, start_side, side. The suggestion content replaces all lines from start_line through line verbatim.

Preflight validation

Run before submission:

Validate JSON payload syntax (e.g., pipe the heredoc through jq . >/dev/null)
Every comment has path, line, and side: "RIGHT"
Multi-line comments additionally have start_line and start_side: "RIGHT"
line (and start_line for ranges) falls inside the PR diff hunk for that file
Each body that includes a suggestion contains ```suggestion ``` fences wrapping the raw replacement code
Suggestion replacement code preserves indentation and exact intended final content
Empty suggestion block (```suggestion\n```) only when the intent is to delete the selected line(s)
Submit command

Build the JSON payload with all comments (single-line and multi-line mixed) and submit:

gh api repos/$REPO_OWNER/$REPO_NAME/pulls/$PR_NUMBER/reviews \
  --method POST \
  --input - <<'EOF'
{
  "event": "<APPROVE or REQUEST_CHANGES per 'Determining event type' above>",
  "body": "<main-review-comment>",
  "comments": [
    {
      "path": "src/auth.ts",
      "line": 42,
      "side": "RIGHT",
      "body": "<thread-comment>"
    },
    {
      "path": "src/utils.ts",
      "start_line": 10,
      "line": 14,
      "start_side": "RIGHT",
      "side": "RIGHT",
      "body": "<thread-comment>"
    }
  ]
}
EOF

Error handling

If the API returns an error (e.g., 422 Unprocessable Entity):

Parse the error response to identify which comment(s) failed (GitHub typically reports the index or the path/line that is invalid).
The most common cause is a line or start_line that falls outside the PR diff hunk. For each failing comment:
Re-fetch the diff hunk for that file (gh pr diff $PR_NUMBER and locate the @@ headers for the file).
Verify that the line value falls within one of the hunk ranges. If not, adjust the line to the nearest valid line within the hunk, or drop the comment if no valid line exists.
Remove or fix the failing comments and retry the submission once. If the retry also fails, report the error to the user with the full API response and the list of comments that could not be submitted.
9. Report Result

Present a summary of the review submission to the user, including:

The PR URL for reference
Number of review comments submitted vs. total issues found
Requirements coverage summary (percentage and any missing requirements from Step 3)
The Issues table below
Issues table

You MUST output a markdown table listing every issue from Step 5 with its submission status and reason. Never omit this table, even when all issues were skipped. Use the following format:

#	Severity	File	Line(s)	Title	Status	Reason
1	High Priority	src/auth.ts	42	Unvalidated input	Submitted	—
2	Medium Priority	src/utils.ts	10-14	Missing null check	Skipped	Duplicate of existing comment
3	Medium Priority	src/api.ts	88	Unused variable	Skipped	Line outside diff hunk
4	Medium Priority	src/db.ts	22	SQL injection risk	Failed	API error 422 — retry also failed
5	Low Priority	src/validators.ts	15-22	Shared helper duplicates logic	In review body	File not in diff

Status values:

Submitted — comment was successfully posted as an inline thread comment on the PR. Reason: —
In review body — the file is not part of the PR diff (file_in_diff: false), so the issue was included in the main review body under the "Additional issues outside the diff" section. Reason: File not in diff
Skipped (duplicate) — removed during deduplication (Step 6). Reason: describe which existing comment covers it
Skipped (no diff line) — the target line is not within any diff hunk and could not be adjusted. Reason: explain why
Failed — the API rejected the comment and the retry also failed. Reason: include the API error detail

If no review was submitted (Step 7), explain that no new issues were found beyond existing review comments and still show the table with all issues marked as skipped. List all issues in descending severity order (High → Medium → Low).

Important Notes
The line field in review comments must reference a line that appears in the diff -- comments on unchanged lines will be rejected by the API
For multi-line suggestions, use start_line and line together to define the range being replaced; both must be within the diff hunk
An empty suggestion block (```suggestion\n```) means "delete these lines"
The content inside ```suggestion ``` replaces the selected line(s) verbatim -- ensure correct indentation and formatting
Never fabricate issues -- only flag genuine concerns backed by evidence in the code
Weekly Installs
21
Repository
arinhubcom/arinhub
First Seen
Feb 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn