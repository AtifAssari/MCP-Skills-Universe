---
title: fact-checker
url: https://skills.sh/nicepkg/ai-workflow/fact-checker
---

# fact-checker

skills/nicepkg/ai-workflow/fact-checker
fact-checker
Installation
$ npx skills add https://github.com/nicepkg/ai-workflow --skill fact-checker
SKILL.md
Fact Checker

Verify factual claims in documents and propose corrections backed by authoritative sources.

When to use

Trigger when users request:

"Fact-check this document"
"Verify these AI model specifications"
"Check if this information is still accurate"
"Update outdated data in this file"
"Validate the claims in this section"
Workflow

Copy this checklist to track progress:

Fact-checking Progress:
- [ ] Step 1: Identify factual claims
- [ ] Step 2: Search authoritative sources
- [ ] Step 3: Compare claims against sources
- [ ] Step 4: Generate correction report
- [ ] Step 5: Apply corrections with user approval

Step 1: Identify factual claims

Scan the document for verifiable statements:

Target claim types:

Technical specifications (context windows, pricing, features)
Version numbers and release dates
Statistical data and metrics
API capabilities and limitations
Benchmark scores and performance data

Skip subjective content:

Opinions and recommendations
Explanatory prose
Tutorial instructions
Architectural discussions
Step 2: Search authoritative sources

For each claim, search official sources:

AI models:

Official announcement pages (anthropic.com/news, openai.com/index, blog.google)
API documentation (platform.claude.com/docs, platform.openai.com/docs)
Developer guides and release notes

Technical libraries:

Official documentation sites
GitHub repositories (releases, README)
Package registries (npm, PyPI, crates.io)

General claims:

Academic papers and research
Government statistics
Industry standards bodies

Search strategy:

Use model names + specification (e.g., "Claude Opus 4.5 context window")
Include current year for recent information
Verify from multiple sources when possible
Step 3: Compare claims against sources

Create a comparison table:

Claim in Document	Source Information	Status	Authoritative Source
Claude 3.5 Sonnet: 200K tokens	Claude Sonnet 4.5: 200K tokens	❌ Outdated model name	platform.claude.com/docs
GPT-4o: 128K tokens	GPT-5.2: 400K tokens	❌ Incorrect version & spec	openai.com/index/gpt-5-2

Status codes:

✅ Accurate - claim matches sources
❌ Incorrect - claim contradicts sources
⚠️ Outdated - claim was true but superseded
❓ Unverifiable - no authoritative source found
Step 4: Generate correction report

Present findings in structured format:

## Fact-Check Report

### Summary
- Total claims checked: X
- Accurate: Y
- Issues found: Z

### Issues Requiring Correction

#### Issue 1: Outdated AI Model Reference
**Location:** Line 77-80 in docs/file.md
**Current claim:** "Claude 3.5 Sonnet: 200K tokens"
**Correction:** "Claude Sonnet 4.5: 200K tokens"
**Source:** https://platform.claude.com/docs/en/build-with-claude/context-windows
**Rationale:** Claude 3.5 Sonnet has been superseded by Claude Sonnet 4.5 (released Sept 2025)

#### Issue 2: Incorrect Context Window
**Location:** Line 79 in docs/file.md
**Current claim:** "GPT-4o: 128K tokens"
**Correction:** "GPT-5.2: 400K tokens"
**Source:** https://openai.com/index/introducing-gpt-5-2/
**Rationale:** 128K was output limit; context window is 400K. Model also updated to GPT-5.2

Step 5: Apply corrections with user approval

Before making changes:

Show the correction report to the user
Wait for explicit approval: "Should I apply these corrections?"
Only proceed after confirmation

When applying corrections:

# Use Edit tool to update document
# Example:
Edit(
    file_path="docs/03-写作规范/AI辅助写书方法论.md",
    old_string="- Claude 3.5 Sonnet: 200K tokens（约 15 万汉字）",
    new_string="- Claude Sonnet 4.5: 200K tokens（约 15 万汉字）"
)


After corrections:

Verify all edits were applied successfully
Note the correction summary (e.g., "Updated 4 claims in section 2.1")
Remind user to commit changes
Search best practices
Query construction

Good queries (specific, current):

"Claude Opus 4.5 context window 2026"
"GPT-5.2 official release announcement"
"Gemini 3 Pro token limit specifications"

Poor queries (vague, generic):

"Claude context"
"AI models"
"Latest version"
Source evaluation

Prefer official sources:

Product official pages (highest authority)
API documentation
Official blog announcements
GitHub releases (for open source)

Use with caution:

Third-party aggregators (llm-stats.com, etc.) - verify against official sources
Blog posts and articles - cross-reference claims
Social media - only for announcements, verify elsewhere

Avoid:

Outdated documentation
Unofficial wikis without citations
Speculation and rumors
Handling ambiguity

When sources conflict:

Prioritize most recent official documentation
Note the discrepancy in the report
Present both sources to the user
Recommend contacting vendor if critical

When no source found:

Mark as ❓ Unverifiable
Suggest alternative phrasing: "According to [Source] as of [Date]..."
Recommend adding qualification: "approximately", "reported as"
Special considerations
Time-sensitive information

Always include temporal context:

Good corrections:

"截至 2026 年 1 月" (As of January 2026)
"Claude Sonnet 4.5 (released September 2025)"

Poor corrections:

"Latest version" (becomes outdated)
"Current model" (ambiguous timeframe)
Numerical precision

Match precision to source:

Source says: "approximately 1 million tokens" Write: "1M tokens (approximately)"

Source says: "200,000 token context window" Write: "200K tokens" (exact)

Citation format

Include citations in corrections:

> **注**：具体上下文窗口以模型官方文档为准，本书写作时使用 Claude Sonnet 4.5 为主要工具。


Link to sources when possible.

Examples
Example 1: Technical specification update

User request: "Fact-check the AI model context windows in section 2.1"

Process:

Identify claims: Claude 3.5 Sonnet (200K), GPT-4o (128K), Gemini 1.5 Pro (2M)
Search official docs for current models
Find: Claude Sonnet 4.5, GPT-5.2, Gemini 3 Pro
Generate report showing discrepancies
Apply corrections after approval
Example 2: Statistical data verification

User request: "Verify the benchmark scores in chapter 5"

Process:

Extract numerical claims
Search for official benchmark publications
Compare reported vs. source values
Flag any discrepancies with source links
Update with verified figures
Example 3: Version number validation

User request: "Check if these library versions are still current"

Process:

List all version numbers mentioned
Check package registries (npm, PyPI, etc.)
Identify outdated versions
Suggest updates with changelog references
Update after user confirms
Quality checklist

Before completing fact-check:

 All factual claims identified and categorized
 Each claim verified against official sources
 Sources are authoritative and current
 Correction report is clear and actionable
 Temporal context included where relevant
 User approval obtained before changes
 All edits verified successful
 Summary provided to user
Limitations

This skill cannot:

Verify subjective opinions or judgments
Access paywalled or restricted sources
Determine "truth" in disputed claims
Predict future specifications or features

For such cases:

Note the limitation in the report
Suggest qualification language
Recommend user research or expert consultation
Weekly Installs
49
Repository
nicepkg/ai-workflow
GitHub Stars
176
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn