---
title: query-examples
url: https://skills.sh/posthog/ai-plugin/query-examples
---

# query-examples

skills/posthog/ai-plugin/query-examples
query-examples
Installation
$ npx skills add https://github.com/posthog/ai-plugin --skill query-examples
SKILL.md
Querying data in PostHog

If the MCP server haven't provided instructions on querying data in PostHog, read the guidelines.

Data Schema

Schema reference for PostHog's core system models, organized by domain:

Activity logs
Actions
Alerts
Annotations
Batch exports
Early Access Features
Cohorts & Persons
Dashboards, Tiles & Insights
Data Warehouse
Data Modeling Endpoints
Error Tracking
Flags & Experiments
Hog Flows
Hog Functions
Integrations
Logs
Notebooks
Session Recording Playlists
Session Recordings
Support Tickets
Surveys
SQL Variables
Skipped events in the read-data-schema tool
Dynamic person and event properties — patterns like $survey_dismissed/{id}, $feature/{key} that don't appear in tool results
HogQL References
Person property modes (event-time vs query-time). Read when working with person.properties.* to understand if values are historical or current.
Sparkline, SemVer, Session replays, Actions, Translation, HTML tags and links, Text effects, and more
SQL variables.
Available functions in HogQL. IMPORTANT: the list is long, so read data using bash commands like grep.
Analytics Query Examples

Use the examples below to create optimized analytical queries.

Trends (unique users, specific time range, single series)
Trends (total count with multiple breakdowns)
Funnel (two steps, aggregated by unique users, broken down by the person's role, sequential, 14-day conversion window)
Conversion trends (funnel, two steps, aggregated by unique groups, 1-day conversion window)
Retention (unique users, returned to perform an event in the next 12 weeks, recurring)
User paths (pageviews, three steps, applied path cleaning and filters, maximum 50 paths)
Lifecycle (unique users by pageviews)
Stickiness (counted by pageviews from unique users, defined by at least one event for the interval, non-cumulative)
LLM trace (generations, spans, embeddings, human feedback, captured AI metrics)
LLM traces list (searching and listing traces with property filters, two-phase query)
Web path stats (paths, visitors, views, bounce rate)
Web traffic channels (direct, organic search, etc)
Web views by devices
Web overview
Error tracking (search for a value in an error and filtering by custom properties)
Logs (filtering by severity and searching for a term)
Sessions (listing sessions with duration, pageviews, and bounce rate)
Session replay (listing recordings with activity filters)
Team taxonomy (top events by count, paginated)
Event taxonomy (properties of an event, with sample values)
Person property taxonomy (sample values for person properties)
Weekly Installs
42
Repository
posthog/ai-plugin
GitHub Stars
28
First Seen
Mar 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass