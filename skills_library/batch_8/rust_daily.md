---
title: rust-daily
url: https://skills.sh/zhanghandong/rust-skills/rust-daily
---

# rust-daily

skills/zhanghandong/rust-skills/rust-daily
rust-daily
Installation
$ npx skills add https://github.com/zhanghandong/rust-skills --skill rust-daily
Summary

Aggregates Rust community news and updates from multiple sources, filtered by time range.

Fetches from five primary sources: Reddit r/rust, This Week in Rust, official Rust blog, Inside Rust, and Rust Foundation news/blog/events
Supports three time ranges (day, week, month) and category filtering (all, ecosystem, official, foundation)
Operates in two modes: agent-based (if rust-daily-reporter.md exists) or inline (direct source fetching via agent-browser, actionbook MCP, or WebFetch)
Combines results into a structured markdown report with scores, dates, titles, and summaries organized by source category
SKILL.md
Rust Daily Report

Version: 2.1.0 | Last Updated: 2025-01-27

Fetch Rust community updates, filtered by time range.

Data Sources
Category	Sources
Ecosystem	Reddit r/rust, This Week in Rust
Official	blog.rust-lang.org, Inside Rust
Foundation	rustfoundation.org (news, blog, events)
Parameters
time_range: day | week | month (default: week)
category: all | ecosystem | official | foundation
Execution Mode Detection

CRITICAL: Check agent file availability first to determine execution mode.

Try to read: ../../agents/rust-daily-reporter.md

Agent Mode (Plugin Install)

When ../../agents/rust-daily-reporter.md exists:

Workflow
1. Read: ../../agents/rust-daily-reporter.md
2. Task(subagent_type: "general-purpose", run_in_background: false, prompt: <agent content>)
3. Wait for result
4. Format and present to user

Inline Mode (Skills-only Install)

When agent file is NOT available, execute each source directly:

1. Reddit r/rust
# Using agent-browser CLI
agent-browser open "https://www.reddit.com/r/rust/hot/"
agent-browser get text ".Post" --limit 10
agent-browser close


Or with WebFetch fallback:

WebFetch("https://www.reddit.com/r/rust/hot/", "Extract top 10 posts with scores and titles")


Parse output into:

Score	Title	Link
2. This Week in Rust
# Check actionbook first
mcp__actionbook__search_actions("this week in rust")
mcp__actionbook__get_action_by_id(<action_id>)

# Then fetch
agent-browser open "https://this-week-in-rust.org/"
agent-browser get text "<selector_from_actionbook>"
agent-browser close


Parse output into:

Issue #{number} ({date}): highlights
3. Rust Blog (Official)
agent-browser open "https://blog.rust-lang.org/"
agent-browser get text "article" --limit 5
agent-browser close


Or with WebFetch fallback:

WebFetch("https://blog.rust-lang.org/", "Extract latest 5 blog posts with dates and titles")


Parse output into:

Date	Title	Summary
4. Inside Rust
agent-browser open "https://blog.rust-lang.org/inside-rust/"
agent-browser get text "article" --limit 3
agent-browser close


Or with WebFetch fallback:

WebFetch("https://blog.rust-lang.org/inside-rust/", "Extract latest 3 posts with dates and titles")

5. Rust Foundation
# News
agent-browser open "https://rustfoundation.org/media/category/news/"
agent-browser get text "article" --limit 3
agent-browser close

# Blog
agent-browser open "https://rustfoundation.org/media/category/blog/"
agent-browser get text "article" --limit 3
agent-browser close

# Events
agent-browser open "https://rustfoundation.org/events/"
agent-browser get text "article" --limit 3
agent-browser close

Time Filtering

After fetching all sources, filter by time range:

Range	Filter
day	Last 24 hours
week	Last 7 days
month	Last 30 days
Combining Results

After fetching all sources, combine into the output format below.

Tool Chain Priority

Both modes use the same tool chain order:

actionbook MCP - Check for cached/pre-fetched content first

mcp__actionbook__search_actions("rust news {date}")
mcp__actionbook__search_actions("this week in rust")
mcp__actionbook__search_actions("rust blog")


agent-browser CLI - For dynamic web content

agent-browser open "<url>"
agent-browser get text "<selector>"
agent-browser close


WebFetch - Fallback if agent-browser unavailable

Source	Primary Tool	Fallback
Reddit	agent-browser	WebFetch
TWIR	actionbook → agent-browser	WebFetch
Rust Blog	actionbook → WebFetch	-
Foundation	actionbook → WebFetch	-

DO NOT use:

Chrome MCP directly
WebSearch for fetching news pages
Output Format
# Rust {Weekly|Daily|Monthly} Report

**Time Range:** {start} - {end}

## Ecosystem

### Reddit r/rust
| Score | Title | Link |
|-------|-------|------|
| {score} | {title} | [link]({url}) |

### This Week in Rust
- Issue #{number} ({date}): highlights

## Official
| Date | Title | Summary |
|------|-------|---------|
| {date} | {title} | {summary} |

## Foundation
| Date | Title | Summary |
|------|-------|---------|
| {date} | {title} | {summary} |

Validation
Each source should have at least 1 result, otherwise mark "No updates"
On fetch failure, retry with alternative tool
Report reason if all tools fail for a source
Error Handling
Error	Cause	Solution
Agent file not found	Skills-only install	Use inline mode
agent-browser unavailable	CLI not installed	Use WebFetch
Site timeout	Network issues	Retry once, then skip source
Empty results	Selector mismatch	Report and use fallback
Weekly Installs
543
Repository
zhanghandong/rust-skills
GitHub Stars
1.1K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn