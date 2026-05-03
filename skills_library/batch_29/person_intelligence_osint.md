---
title: person-intelligence-osint
url: https://skills.sh/andy160675/sovereign-skills-season1/person-intelligence-osint
---

# person-intelligence-osint

skills/andy160675/sovereign-skills-season1/person-intelligence-osint
person-intelligence-osint
Installation
$ npx skills add https://github.com/andy160675/sovereign-skills-season1 --skill person-intelligence-osint
SKILL.md
Person Intelligence OSINT

Conduct a comprehensive, LinkedIn-friendly, open-source intelligence investigation on any individual. The process starts with professional network reconnaissance, expands to broad-spectrum public sources, and produces a structured intelligence dossier.

Inputs

Three inputs are required. If any are missing, ask the user before proceeding.

Input	Description	Example
Person Name	Full name of the subject	Jane Smith
Job Title	Current or most recent known role	Chief Technology Officer
Company Name	Primary company the subject is associated with	Acme Corp
Workflow

Execute sequentially. Do not skip steps.

Step 1: Acknowledge and Scope

Confirm the target details with the user. Create a working directory:

mkdir -p /home/ubuntu/osint/{{person_name_slug}}


Create osint_notes.md inside this directory to accumulate raw findings throughout the process.

Step 2: LinkedIn Reconnaissance

This is the foundational data source. The goal is to locate and extract the subject's canonical professional profile.

Use search tool (type: info) with these query patterns:

"{{person_name}}" "{{company_name}}" site:linkedin.com
"{{person_name}}" "{{job_title}}" LinkedIn
"{{person_name}}" "{{company_name}}" LinkedIn profile

Use browser_navigate to visit the identified LinkedIn URL. Extract:

Full name, headline, location
Career history (all roles, companies, dates)
Education
Skills, endorsements, recommendations count
Connection count and notable mutual connections
Any posts or articles authored

Save all extracted data to osint_notes.md immediately.

Step 3: Corporate Intelligence

Investigate the subject's company and any other associated entities.

Use search tool with:

"{{company_name}}" Companies House (UK) or "{{company_name}}" SEC filing (US)
"{{company_name}}" corporate registration
"{{person_name}}" director OR officer "{{company_name}}"

For UK companies, navigate to https://find-and-update.company-information.service.gov.uk/ and search for the company. Extract:

Company number, status, incorporation date
Registered address
Directors and officers (confirm subject's role)
Filing history (recent accounts, confirmation statements)

Append findings to osint_notes.md.

Step 4: Media & Public Presence

Expand to news, social media, and other public mentions.

Use search tool (type: news) with:

"{{person_name}}" "{{company_name}}"
"{{person_name}}" interview OR announcement OR appointed

Use search tool (type: info) with:

"{{person_name}}" site:twitter.com OR site:x.com
"{{person_name}}" site:facebook.com
"{{person_name}}" site:github.com (if technical role)
"{{person_name}}" "{{company_name}}" conference OR speaker OR panel

For each significant result, use browser_navigate to read the full content. Save key excerpts and URLs to osint_notes.md.

Step 5: Domain & Technical Intelligence (Conditional)

Execute this step only if the subject has a technical or digital role (CTO, developer, engineer, etc.).

Search for personal websites, blogs, or portfolios.
Search for GitHub profiles, open-source contributions, or academic papers.
Search for domain registrations (WHOIS) if a personal domain is found.
Append findings to osint_notes.md.
Step 6: Connected Systems Check (Conditional)

If the user has Gmail or Slack MCP integrations enabled, search those systems for any prior correspondence or mentions of the subject.

Gmail: Use gmail_search_messages with queries for the person's name and company.
Slack: Use slack_search_public_and_private with the person's name.
Append any findings to osint_notes.md.
Step 7: Synthesize and Generate Dossier
Read the dossier template: /home/ubuntu/skills/person-intelligence-osint/templates/dossier_template.md
Create the final report file: Dossier_{{person_name_slug}}.md
Populate the template with synthesized intelligence from osint_notes.md.
Ensure all sections are written in complete paragraphs, not bullet lists.
Include a References section with numbered citations and source URLs.
Include a table for career history and a table for the identity profile.
Step 8: Deliver
Review the dossier for completeness.
Use message tool (type: result) to deliver the Markdown dossier as an attachment.
Provide a concise summary of key findings in the message text.
Optionally, sync to Google Drive if the user has integration enabled.
Output Format

The final dossier MUST use the template at templates/dossier_template.md. Key requirements:

Professional Markdown formatting
Identity table at the top
Career history table
Complete paragraphs (not bullet-point lists) for analysis sections
Numbered inline citations with a References section
All source URLs documented
Example Usage

User says: "Research John Smith, VP Engineering at TechCorp"

Skill triggers with:

Person Name: John Smith
Job Title: VP Engineering
Company Name: TechCorp

Output: A structured Markdown dossier covering LinkedIn profile, corporate filings, news mentions, social media presence, and any connected system references.

Weekly Installs
8
Repository
andy160675/sove…-season1
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail