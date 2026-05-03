---
title: address-pr-comments
url: https://skills.sh/morphet81/cheat-sheets/address-pr-comments
---

# address-pr-comments

skills/morphet81/cheat-sheets/address-pr-comments
address-pr-comments
Installation
$ npx skills add https://github.com/morphet81/cheat-sheets --skill address-pr-comments
SKILL.md

Retrieve unresolved review comments and general conversation comments from the current branch's PR, explain each issue to the developer with a proposed fix, allow the developer to discuss and amend proposals, then spawn a coordinated team of developers to implement the fixes. After committing, reply to each comment on GitHub with details on how it was addressed.

Usage:

/address-pr-comments — Fetch and address unresolved PR comments for the current branch

Instructions:

Verify prerequisites:

Run gh auth status via the Bash tool to verify the GitHub CLI is installed and authenticated
If gh is not available or not authenticated, display the following and STOP:
GitHub CLI (gh) is not installed or not authenticated.
Please install gh and run `gh auth login` before using /address-pr-comments.


Identify the PR for the current branch:

Run git branch --show-current to get the current branch name
Run gh pr view --json number,title,url,state,baseRefName,author to find the PR associated with the current branch and record the PR author's login (author.login) for step 3b
If no PR exists, display the following and STOP:
No pull request found for branch "<current-branch>".
Please create a PR first, then run /address-pr-comments.

If the PR is closed or merged, warn the developer:
PR #<number> is <state>. Comments may no longer be actionable.

Use AskUserQuestion to ask if they want to continue anyway.

Retrieve all PR comments (review comments + general comments):

a) Retrieve unresolved review comments:

Use the GitHub GraphQL API to fetch all review threads and their resolution status:
gh api graphql -f query='
  query($owner: String!, $repo: String!, $pr: Int!) {
    repository(owner: $owner, name: $repo) {
      pullRequest(number: $pr) {
        reviewThreads(first: 100) {
          nodes {
            id
            isResolved
            comments(first: 20) {
              nodes {
                id
                databaseId
                body
                path
                line
                author { login }
                createdAt
                url
              }
            }
          }
        }
      }
    }
  }
' -f owner='{owner}' -f repo='{repo}' -F pr={pr_number}

Collect only unresolved threads. For each, record:
Thread ID (for replying later)
File path and line number
Full comment thread (original comment + all replies)
Author(s)
The URL of the first comment in the thread (for linking in replies)
Within each thread, ignore replies whose body ends with [Agent response] — these are prior agent responses, not reviewer comments to address. However, the thread itself still needs to be addressed if it remains unresolved.

b) Retrieve review body comments (global review comments):

When a reviewer submits a review (Approve, Request Changes, or Comment), they can include a top-level body comment that is NOT attached to any specific line. These are "global" review comments.
Fetch all reviews using the GraphQL API:
gh api graphql -f query='
  query($owner: String!, $repo: String!, $pr: Int!) {
    repository(owner: $owner, name: $repo) {
      pullRequest(number: $pr) {
        reviews(first: 100) {
          nodes {
            id
            databaseId
            body
            state
            author { login }
            createdAt
            url
          }
        }
      }
    }
  }
' -f owner='{owner}' -f repo='{repo}' -F pr={pr_number}

Filter: Only include reviews where:
body is non-empty (reviews with no body text have nothing to address)
body does NOT end with [Agent response] (prior agent responses)
state is CHANGES_REQUESTED or COMMENTED (skip APPROVED reviews with body text that is purely congratulatory, e.g., "Looks great!", "LGTM". If an APPROVED review has a substantive body with actionable content, include it)
Author is not a bot
For each remaining review body comment, record:
Review ID (databaseId — for replying later)
Review state (CHANGES_REQUESTED, COMMENTED, APPROVED)
Author
Comment body
Created date
The url of the review (for linking in replies)
Note: These comments do not have file/line references. They are top-level feedback about the PR as a whole.

c) Retrieve general conversation comments:

Fetch general PR comments (issue comments) using the REST API:
gh api repos/{owner}/{repo}/issues/{pr_number}/comments --paginate

Filter out comments that should NOT be addressed:
Comments by bots (author type is "Bot", or login ends with [bot])
Comments whose body ends with [Agent response] (prior agent responses — not new comments to address)
Comments that are purely approval/acknowledgement (e.g., "LGTM", "Looks good", ":+1:")
PR author comments: Do not exclude the PR author by default. Authors often leave actionable conversation notes for collaborators or automation (e.g. re-run CI, regenerate visual snapshots, "please review X"). Include those.
Optional skip for author noise: If the comment's user.login matches the PR author's author.login from step 2 and the body is clearly non-actionable, skip it — e.g. only a commit URL, only "Done" / "Fixed" / "Pushed" with no remaining ask, or empty/emoji-only.
For each remaining general comment, record:
Comment ID (for replying later — id field)
Author
Comment body
Created date
The html_url of the comment (for linking in replies)
Note: General comments do not have file/line references and have no resolution status. Include all that pass the filters above.

d) Combine and check:

Merge all three lists into a single ordered list, sorted chronologically by creation date
Tag each entry with its source: review (from step 3a), review-body (from step 3b), or general (from step 3c)
If there are no comments from either source, display the following and STOP:
No unresolved review comments or actionable general comments on PR #<number>. Nothing to address!


Analyze each comment and propose fixes:

For each comment (review or general), present the issue to the developer with a clear explanation and a proposed approach.

For review comments (attached to code), use this format:

## Comment <N>/<total> — [Review] `<file>:<line>` — @<author>

### Reviewer said:
> <full comment body>

### Context:
<Read the referenced file and surrounding code. Explain the relevant code context
so the developer understands the issue without having to look it up.>

### Analysis:
<Explain what the reviewer is asking for and why. Categorize as one of:>
- **Code change** — specific modifications needed
- **Question** — reviewer asks for clarification; may not need a code change
- **Suggestion** — an optional improvement worth considering
- **Concern** — a potential issue that needs investigation

### Proposed fix:
<Describe the concrete approach to address this comment. If it's a code change,
describe exactly what will change and where. If it's a question, draft the reply.
If no fix is needed, explain why.>


For review body comments (global review feedback, not attached to a line), use this format:

## Comment <N>/<total> — [Review Body] <state> — @<author>

### Reviewer said:
> <full review body>

### Context:
<Identify what the reviewer is commenting on. Review body comments often address the PR
as a whole — architecture, approach, missing considerations, or cross-cutting concerns.
Read the PR diff and relevant files to understand the context.>

### Analysis:
<Explain what the reviewer is asking for and why. Categorize as one of:>
- **Code change** — specific modifications needed
- **Question** — reviewer asks for clarification; may not need a code change
- **Suggestion** — an optional improvement worth considering
- **Concern** — a potential issue that needs investigation
- **Discussion** — a broader topic about approach or architecture

### Proposed fix:
<Describe the concrete approach to address this comment. If it requires code changes,
identify the files and describe exactly what will change. If it's a question or discussion,
draft the reply. If no action is needed, explain why.>


For general comments (PR conversation), use this format:

## Comment <N>/<total> — [General] — @<author>

### Comment:
> <full comment body>

### Context:
<Identify any files, functions, or areas of the codebase the comment refers to.
If the comment mentions specific code, read the relevant files. If the comment is
about the PR overall (architecture, approach, etc.), summarize the relevant changes.>

### Analysis:
<Explain what the reviewer is asking for and why. Categorize as one of:>
- **Code change** — specific modifications needed
- **Question** — reviewer asks for clarification; may not need a code change
- **Suggestion** — an optional improvement worth considering
- **Concern** — a potential issue that needs investigation
- **Discussion** — a broader topic about approach or architecture

### Proposed fix:
<Describe the concrete approach to address this comment. If it requires code changes,
identify the files and describe exactly what will change. If it's a question or discussion,
draft the reply. If no action is needed, explain why.>


For comments that appear already addressed or invalid:

If the issue described in the comment has already been fixed in the current code, categorize as Already addressed and note the existing code that resolves it
If the comment is invalid (references outdated code, misunderstands the implementation, etc.), categorize as Invalid and explain why
These comments still require a response on GitHub (step 10) — the response should acknowledge the comment and explain why no further action is needed

After presenting all comments, use AskUserQuestion to ask:

I've presented all unresolved comments with proposed fixes. You can:

Ask questions about any specific comment (e.g., "tell me more about comment 3")
Request amendments to a proposed fix (e.g., "for comment 2, do X instead of Y")
Approve all and proceed to implementation

What would you like to do?

Interactive discussion:

The developer may:

Ask clarifying questions about any comment or proposed fix
Request changes to a proposed approach
Disagree with a fix and propose an alternative
Decide that a comment doesn't need a code fix (just a reply)

Continue the discussion until the developer explicitly approves the plan by saying something like "go ahead", "approve", "looks good", "implement", etc.

Keep a running record of the final approved approach for each comment:

Comment #N: <approved fix description> or <reply only — no code change>

Create the developer team:

Once the developer approves, set up a coordinated team to implement the fixes.

a) Create the team:

Use TeamCreate with name pr-comments-<pr-number> (e.g., pr-comments-142)

b) Create a shared task list:

Use TaskCreate to create one task per comment that requires a code change, plus one coordination task:
"Fix comment #N: " for each code change
"Coordination: verify no conflicts between fixes" as a tracking task

c) Determine team size:

Count the number of comments requiring code changes
Spawn 2 to 4 developers based on the number:
1–3 comments → 2 developers
4–6 comments → 3 developers
7+ comments → 4 developers

d) Divide work across developers:

Group comments so that comments touching the same file or closely related files are assigned to the same developer to avoid conflicts
Each developer should have a roughly balanced workload
Document the assignment clearly (which developer handles which comments)

e) Spawn developers using the Task tool (subagent_type: general-purpose) with run_in_background: true:

Give each developer the team name so they can communicate with each other
Each developer's prompt must include:
The team name for inter-agent communication
Their assigned comment(s) with the full approved fix description
The relevant file paths and current code context
Coordination instructions:

You are Developer on team <team-name>. You are responsible for fixing comment(s) . Other developers on this team are working on other comments in parallel.

Before making changes:

Read the latest version of any file you plan to edit (another developer may have already modified it)
Check team messages via SendMessage for any coordination notes from other developers

After making changes:

Send a message to the team describing exactly which files and line ranges you modified
Format: "Developer completed: edited lines - for comment #"
If you notice your changes overlap with or affect another developer's assignment, send an alert immediately

Do NOT commit. Only make the code changes. The team lead will handle committing. Mark your task(s) as completed via TaskUpdate when done.

Monitor and coordinate:

Wait for all developers to complete their tasks
After all developers finish, review the combined changes:
Run git diff to see all modifications
Check for conflicts: two developers editing the same lines or introducing contradictory changes
If conflicts are found, resolve them (or ask the developer for guidance if the resolution is ambiguous)
Run a final sanity check: read each modified file to confirm the changes are coherent

Present changes and wait for confirmation:

Present the combined changes to the developer:

## Fixes Implemented

### Comment #1 — `<file>:<line>` — @<author>
**Fix:** <description of what was changed>
**Files modified:** `<file>` (lines <start>-<end>)

### Comment #2 — `<file>:<line>` — @<author>
**Fix:** <description> (or "Reply only — no code change")

...

### Files Modified
- `path/to/file.ts`
- `path/to/other.ts`


Then display:

All fixes have been implemented. Please review the changes and confirm when ready to commit. You can also ask me to adjust any fix before committing.

Wait for the developer to explicitly confirm before committing. Do not commit automatically.

Commit the changes:

Once the developer confirms:

Stage only the files that were modified as part of the fixes (use git add <file1> <file2> ..., not git add -A)
Create a commit with a message following the repo's existing style. Suggested format:
Address PR #<number> review comments

- <Comment #1 short description>
- <Comment #2 short description>
- ...

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>


Respond to comments on GitHub:

After committing, reply to each comment on GitHub using the gh CLI.

a) For review comments — if a code fix was made:

Reply to the review comment thread with details on how it was addressed
Include the fixing code if it's short (under ~20 lines) as a fenced code block
If the fix is longer, reference the file path and line numbers:

Fixed in <file> (lines –).

Use the gh api command to reply:
gh api repos/{owner}/{repo}/pulls/{pr_number}/comments -f body='<reply>' -f in_reply_to=<comment_id>


b) For review comments — if no code fix was needed (question/reply-only):

Post the approved reply explaining why no code change was necessary
Be specific: reference the existing code, design decisions, or documentation that addresses the reviewer's concern

c) For review body comments — reply to the review:

Post a comment on the review using the REST API:
gh api repos/{owner}/{repo}/pulls/{pr_number}/reviews/{review_id}/comments -f body='<reply>'

Format the reply to address the reviewer's top-level feedback:

Regarding your review:

If a code fix was made, include the same details as inline review comment replies (file paths, line numbers, or short code blocks)

d) For general comments — reply on the PR conversation:

Post a new issue comment replying to the original. Quote the original comment for context:
gh api repos/{owner}/{repo}/issues/{pr_number}/comments -f body='<reply>'

Format the reply to reference the original author and comment:

Regarding @'s comment:

If a code fix was made, include the same details as review comment replies (file paths, line numbers, or short code blocks)

e) Reply format (all comment types):

Keep replies professional and concise
Start with a brief summary (e.g., "Fixed — ...", "Good catch — ...", "No change needed — ...")
Include code references with line numbers when relevant
Always append [Agent response] on a new line at the end of every reply. This tag identifies automated responses and allows future runs to skip already-handled comments
For already-addressed comments, reply explaining that the issue was already resolved (reference the relevant code or commit)
For invalid comments, reply respectfully explaining why the comment does not apply

Clean up and report:

Shut down the developer team:
Send a shutdown_request to each teammate via SendMessage
Once all have confirmed, call TeamDelete
Present a final summary:
## PR Comments Addressed

**PR:** #<number> — <title>
**Comments addressed:** <N>
**Commit:** <short SHA>

### Fixes
- Comment #1 (`<file>:<line>`) — <brief description> — replied on GitHub
- Comment #2 (`<file>:<line>`) — <brief description> — replied on GitHub
...

### Next Steps
- Push the commit: `git push`
- Verify CI passes
- Request re-review if needed


Handle edge cases:

If a comment references a file that no longer exists, note it in the analysis and propose replying to the reviewer explaining the file was removed (and why, if determinable from git history)
If a comment references lines that have changed since the review, read the current file and adapt the fix to the current code
If two comments conflict with each other, flag the conflict during step 4 and ask the developer to decide
If a comment is ambiguous or unclear, present your best interpretation and ask the developer to confirm during step 5
If the developer rejects all proposed fixes, skip implementation and optionally post replies explaining the decisions
If a developer agent fails or produces incorrect changes, attempt the fix directly or ask the developer for guidance
If a general comment is vague or doesn't clearly reference any code (e.g., "Can we discuss the approach?"), categorize it as Discussion and propose a reply addressing the concern based on the PR's changes
If a general comment has already been answered by another comment in the thread (someone else replied), skip it and note it as already addressed
If a PR author comment is workflow-only (e.g. update snapshots, re-run visual tests, trigger CI), treat it as Code change or Suggestion depending on the repo: propose the exact commands or test targets (e.g. Playwright --update-snapshots, Percy, etc.) after checking package.json / CI config
Weekly Installs
64
Repository
morphet81/cheat-sheets
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn