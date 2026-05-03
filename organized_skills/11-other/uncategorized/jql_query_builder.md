---
rating: ⭐⭐
title: jql query builder
url: https://skills.sh/sethdford/claude-plugins/jql-query-builder
---

# jql query builder

skills/sethdford/claude-plugins/JQL Query Builder
JQL Query Builder
Installation
$ npx skills add https://github.com/sethdford/claude-plugins --skill 'JQL Query Builder'
SKILL.md
JQL Query Builder

Expert assistance for constructing JQL (Jira Query Language) queries to search and filter Jira issues efficiently.

When to Use This Skill
User wants to search for specific issues
User needs to filter issues by multiple criteria
User mentions JQL or queries
User wants to find bugs, features, or tasks matching certain conditions
User needs help understanding JQL syntax
JQL Basics
Field Operators
Operator	Description	Example
=	Equals	status = "In Progress"
!=	Not equals	priority != Low
>, <	Greater/less than	created > -7d
>=, <=	Greater/less or equal	priority >= High
~	Contains text	summary ~ "login"
IN	Matches any value	status IN (Open, "In Progress")
NOT IN	Doesn't match	priority NOT IN (Low)
IS EMPTY	Field is empty	assignee IS EMPTY
IS NOT EMPTY	Field has value	dueDate IS NOT EMPTY
Common Fields
project: Project key (e.g., project = PROJ)
status: Issue status (e.g., status = "In Progress")
priority: Priority level (e.g., priority = High)
assignee: Assigned user (e.g., assignee = currentUser())
reporter: Who created it (e.g., reporter = currentUser())
created: Creation date (e.g., created >= -30d)
updated: Last update (e.g., updated > -7d)
type: Issue type (e.g., type = Bug)
labels: Labels (e.g., labels = urgent)
summary: Title text (e.g., summary ~ "authentication")
description: Description text (e.g., description ~ "error")
Date Functions
-1d, -7d, -30d: Relative dates (days ago)
-1w, -4w: Weeks ago
startOfDay(), endOfDay(): Day boundaries
startOfWeek(), endOfWeek(): Week boundaries
User Functions
currentUser(): The logged-in user
membersOf("group-name"): Users in a group
Logical Operators
AND: Both conditions must be true
OR: Either condition must be true
NOT: Negate a condition
Common Query Patterns
My Open Issues
assignee = currentUser() AND status != Done

Recently Updated Bugs
type = Bug AND updated >= -7d ORDER BY updated DESC

High Priority Unassigned Issues
priority = High AND assignee IS EMPTY AND status != Done

Issues Created This Sprint
project = PROJ AND created >= -14d AND type IN (Story, Task)

Overdue Issues
dueDate < now() AND status != Done ORDER BY dueDate ASC

Issues Mentioning Specific Feature
(summary ~ "authentication" OR description ~ "authentication") AND status != Done

Team's Work This Week
assignee IN membersOf("dev-team") AND updated >= startOfWeek()

Epics Without Stories
type = Epic AND issueFunction NOT IN linkedIssuesOf("type = Story")

Building Complex Queries
Step-by-Step Approach

Start with project:

project = PROJ


Add status filter:

project = PROJ AND status IN ("To Do", "In Progress")


Add assignee:

project = PROJ AND status IN ("To Do", "In Progress") AND assignee = currentUser()


Add time filter:

project = PROJ AND status IN ("To Do", "In Progress") AND assignee = currentUser() AND created >= -30d


Add sorting:

project = PROJ AND status IN ("To Do", "In Progress") AND assignee = currentUser() AND created >= -30d ORDER BY priority DESC, updated DESC

Optimization Tips
Use Specific Fields

❌ Slow: text ~ "bug" ✅ Fast: summary ~ "bug" OR description ~ "bug"

Limit Date Ranges

❌ Slow: created <= now() ✅ Fast: created >= -90d

Use IN Instead of Multiple OR

❌ Verbose: status = "To Do" OR status = "In Progress" OR status = "Review" ✅ Clean: status IN ("To Do", "In Progress", "Review")

Order Matters for AND

Put most restrictive conditions first:

assignee = currentUser() AND status != Done AND type = Bug

Testing Queries

When I build a query for you, I'll:

Explain the logic: Break down what each part does
Test it: Use /jira-search to verify results
Refine: Adjust based on results
Optimize: Suggest improvements for performance
Common Use Cases
Sprint Planning
project = PROJ AND status = "To Do" AND sprint IS EMPTY ORDER BY priority DESC

Bug Triage
type = Bug AND status = "To Do" AND priority IS EMPTY ORDER BY created DESC

Release Readiness
fixVersion = "v2.0" AND status != Done

Stale Issues
status = "In Progress" AND updated <= -30d

Blocked Work
status = Blocked OR labels = blocked ORDER BY priority DESC

Advanced Patterns
Find Issues Without Estimates
project = PROJ AND "Story Points" IS EMPTY AND type IN (Story, Task)

Parent Issues with Incomplete Subtasks
issueFunction IN parentsOf("status != Done")

Issues Mentioned in Comments
comment ~ "needs review"

Cross-Project Search
project IN (PROJ1, PROJ2, PROJ3) AND assignee = currentUser()

How I'll Help

When you need a JQL query, I will:

Understand your requirements: What are you trying to find?
Build the query: Construct JQL step-by-step
Explain each part: Help you understand the syntax
Test it: Run the query using /jira-search
Refine: Adjust based on results
Save for reuse: Document the query for future use
Example Interaction

You: "Find all high-priority bugs assigned to me that were updated in the last week"

Me: "I'll build a JQL query for that:

type = Bug AND priority = High AND assignee = currentUser() AND updated >= -7d ORDER BY updated DESC


Breaking it down:

type = Bug: Only bugs
priority = High: High priority only
assignee = currentUser(): Assigned to you
updated >= -7d: Updated in last 7 days
ORDER BY updated DESC: Newest first

Let me search for these issues using /jira-search..."

References

For more JQL details:

Jira Query Language documentation: https://support.atlassian.com/jira-service-management-cloud/docs/use-advanced-search-with-jira-query-language-jql/
JQL functions: https://support.atlassian.com/jira-software-cloud/docs/jql-functions/
JQL operators: https://support.atlassian.com/jira-software-cloud/docs/jql-operators/
Weekly Installs
–
Repository
sethdford/claude-plugins
GitHub Stars
2
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass