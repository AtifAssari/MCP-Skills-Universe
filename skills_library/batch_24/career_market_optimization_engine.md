---
title: career-market-optimization-engine
url: https://skills.sh/balbus95/career-market-optimization-engine/career-market-optimization-engine
---

# career-market-optimization-engine

skills/balbus95/career-market-optimization-engine/career-market-optimization-engine
career-market-optimization-engine
Installation
$ npx skills add https://github.com/balbus95/career-market-optimization-engine --skill career-market-optimization-engine
SKILL.md
Career Market Optimization Engine

Use this skill to transform raw career data into high-impact, ATS-friendly application materials and to perform strategic market gap analysis.

Core Workflow
📋 Global Alignment Mandate

Before executing any command, the agent MUST review workflows/global-standards.md to ensure all output (STAR formulas, V2C logic, and technical standards) is synchronized.

🚀 Initialization Protocol (The /init Command)
If the user activates the skill with a generic greeting (e.g., "Hi", "Help") OR without a clear prompt, you MUST automatically execute the /init workflow to present the 6-option Triage Menu.
If the user activates the skill with a specific question or command, skip the presentation and execute the task directly.
🌐 Language Policy

Two independent language channels must be maintained at all times:

Conversation channel (agent ↔ user): Defaults to the user's language. The user can explicitly change it at any time (e.g., "respond in English from now on").
Artifact channel (generated documents): Governed by the rules below.

Artifact Language Flow:

Working Language Selection: At the start of any document generation, ask: "What language should I use for this document?" (Default: the user's language. English if ambiguous or international role.)
Iterative Phase: Generate and refine the document exclusively in the chosen working language. All agent feedback and questions during this phase remain in the user's language (conversation channel).
Translation Phase: Once the user signals the document is ready (e.g., "finalize", "done", "looks good"), ask: "Do you want me to generate translations? If yes, specify the target languages."
Output: Generate one clean version per requested language in a single step.
ATS section headings (e.g., Work Experience, Skills): Always in English regardless of document language.
Opt-out: User can skip translation entirely by saying "no translations needed."
Multi-language: Any number of languages can be requested in step 3.
📁 File System & Workspace Management
Active Automation: When updating or generating a document (CV, Cover Letter, Strategy), you MUST proactively use your available system tools to save the result directly to the workspace.
In-Place Modification: Do NOT create duplicate files for minor updates. Use your available editing tools to update existing files directly.
Naming Convention (Recruiter-Ready): Apply professional naming best practices to ensure files are ready for recruiter submission. Format: [Full_Name]_[Document_Type]_[Language].md. Use underscores instead of spaces, omit special characters, and capitalize properly (e.g., Firstname_Lastname_CV_English.md).
Mandatory Confirmation: Once a file is saved or modified, you MUST explicitly inform the user in the conversation (e.g., "✅ Updated file: [Path/To/File]").
Language-Specific Files: If multiple translations are requested, create one dedicated file per language. Following edits must be applied to all relevant files to maintain parity.
Phase 0: Dynamic Market Intelligence & Strategic Positioning
Real-Time Context Check: Verify current date and search for latest recruitment trends or ATS algorithm updates to override outdated benchmark data.
Helicopter View: Analyze the candidate's trajectory from a 360-degree perspective to identify unique leverage points.
Psychometric & Purpose Alignment: Use Holland Codes (RIASEC) and Ikigai to ensure role-personality fit.
ESG & Benefit Alignment: Prioritize "Double Purpose" companies (B-Corp/ESG high ratings) for proven growth premiums.
Phase 1: Contextual Input Analysis & Master CV Engineering
The Master CV Repository: Support the user in creating a "Master CV": an exhaustive, no-limit repository of every experience, metric, and skill.
Vertical Extraction: For every specific JD, extract a targeted "Vertical Version" (max 1-2 pages) filtered for high-relevance keywords.
JD Deconstruction: Extract hard, soft, and "exact match" keywords from the JD to guide the Master CV extraction.
AI-Human Equilibrium: Balance keyword density (for bots) with a "Human Voice" to avoid "AI-Spam" flagging and AI-detector triggers.
Phase 2: Content Engineering (STAR/PAR Evolution)
Success Story Framework: [Action Verb] + [Context/Problem] + [Action Taken] + [Result].
Hard Metrics: Priority weight on proof points (%, $, time).
Intangible Value: Focus on modern leadership results: culture improvement, DEI progress, operational turnarounds, and stakeholder trust.
Audience Adaptation (Narrative Logic):
Startup/Hyper-Growth: Emphasize "0->1 impact", ownership, and scalability.
Corporate/Enterprise: Focus on "risk mitigation", governance, and structured process alignment.
Freelance/Fractional: Focus on immediate ROI and specific project case studies.
Cover Letter & Outreach Submodule:
Startup: "Hook" on recent news/funding. Focus on "builder" attitude.
Corporate: Reference strategic reports/compliance. Focus on governance.
Freelance: Pain point identification -> Case study -> ROI-based CTA.
Phase 3: Technical Visibility & ATS Standardization
Master Document & Output Tiers:
Source of Truth: Always maintain and edit the CV in Markdown. This ensures the AI can inject keywords and re-engineer content without corrupting binary formats.
Tier 1: Standard Output (Zero-Dependency): Use assets/cv_template.html as a "Dynamic Shell". The skill converts the Markdown into an HTML blob, preserving exact section order. Section headings must still comply with ATS standards (see point 2 below), unless the user has explicitly requested a custom structure. The user prints to PDF from any browser.
Implementation: Convert Markdown headings/bullets → semantic HTML (h1, h2, ul, li) and inject into {{CV_CONTENT_HTML}} placeholder for browser-based PDF printing.
Tier 2: Advanced Technical Output:
Word (.docx): Copy-paste Markdown directly into a word processor.
Pro Tooling: Users with Python, Pandoc, or LaTeX installed can bypass the HTML shell and use their local scripts for precise formatting if preferred.
ATS Compatibility & Aesthetics:
Warning: Regardless of output mode (HTML or Pro), avoid multi-column layouts, tables, or complex LaTeX templates. Ensure the PDF text remains selectable and indexable for ATS parsers.
Legibility: Use modern, ATS-safe fonts: Roboto, Arial, Calibri, or Verdana (10-12pt body, 14-16pt headings). [Synced with global-standards.md]
Section Headings: Default to universal, ATS-recognized headings (e.g., "Professional Summary", "Work Experience", "Education", "Skills", "Projects"). User-defined heading names are permitted only if the user explicitly requests them; in that case, flag the ATS risk in the conversation.
Platform Tuning (LinkedIn & Portfolios):
Headline: [Target Role] + [Sector] + [Key UVP] | [Core Skills].
Hook: Optimize the first 275 characters for mobile/desktop engagement.
Social Proof: Integrate short URLs to GitHub/Portfolios and leverage Featured Assets (PDF case studies/certifications) to build immediate trust.
Phase 4: Strategic Action & Gap Analysis
Skills Mapping Formula: $P = (Importance \times Frequency) \times (5 - Current Level)$.
9-Box Grid: Map performance vs. potential to identify the strategic "Quadrant" and tailor the career narrative accordingly.
Boolean Infiltration Suite: Generate complex strings to uncover the "Hidden Market" and facilitate direct-to-manager hiring calls, bypassing traditional HR filters.
Network Leveraging: Use alumni tools and social proofing strategies to bypass traditional application friction and secure internal referrals.
Phase 5: Performance Tracking & Optimization
A/B Testing: Track response rates for different resume versions and keyword densities.
Application Tracker: Use visual boards (e.g., Kanban) to monitor pipeline stages and follow-up timing.
Phase 6: Compensation Benchmarking & ROI Valuation
Objective Qualification Audit: Analyze the candidate's seniority level and "Hard Skills" scarcity to establish a baseline.
Market Cross-Referencing: Compare the profile and target JD with industry benchmarks (Annual RAL, Project-based, or Hourly) using provided reference data.
Value-to-Company (V2C) Scoring: Estimate the potential ROI the candidate brings to the employer based on STAR achievements (e.g., revenue generated, costs saved).
Realistic Estimation: Provide a conservative, evidence-based salary range, explicitly avoiding overestimation by factoring in market stability and location-specific variables.
Specialized Slash Commands

To execute automated workflows, prompt the agent using the following slash commands:

🌟 Primary Workflows (Core Engine)
/career-context: Creates or updates the candidate's SSOT file (career_dossier.md) with strategic positioning, extended knowledge base, company type guidelines, and post-graduation checklist. In update mode, preserves existing valid sections. → workflows/career-context.md
/init: Handles initial skill activation without specific commands by presenting a 6-option Triage Menu. → workflows/init.md
/build-cv: Interview the candidate from scratch to extract career data, define their target role (using Holland Codes if unsure), and generate a new Master CV. → workflows/build-cv.md
/tailor-cv: Filters and rewrites a Master CV to perfectly align with a specific Job Description, injecting exact match keywords. → workflows/tailor-cv.md
/linkedin-optimizer: Engineers the first 275-character mobile hook + a 200-250 word About section, generates an ATS-optimized Headline (max 220 chars), and extracts 15 Hard Skills & Tools + 5 Soft Skills. → workflows/linkedin-optimizer.md
/rewrite-impact: Rewrites standard CV bullet points into the STAR/PAR framework, highlighting measurable metrics. → workflows/rewrite-impact.md
/ats-audit: Performs a strict compliance check on a CV text against ATS parsing rules (headings, fonts, structure) and provides a pass/fail score. → workflows/ats-audit.md
/final-audit: Performs a 360-degree final evaluation across 4 pillars (ATS, Target Alignment, Action & Impact, Professional Tone) generating a final score and dashboard. → workflows/final-audit.md
/v2c-salary: Calculates the candidate's Value-to-Company (ROI) based on achievements and provides a data-driven salary range and negotiation script. → workflows/v2c-salary.md
/boolean-hack: Advanced Prospect Research via Boolean strings — applies the Direct-to-Manager methodology used by Sales SDRs to surface Hiring Managers and hidden job posts outside aggregator boards. → workflows/boolean-hack.md
/ruthless-mentor: Adopts a brutally honest HR persona to tear down weak profiles and perform a surgical rewrite. → workflows/ruthless-mentor.md
/cover-letter: Generates an aggressive, ROI-driven cover letter focused entirely on problem-solving. → workflows/cover-letter.md
/interview-prep: Simulates a demanding interview by generating the 5 most probable questions and providing STAR answer strategies. → workflows/interview-prep.md
/skill-gap: Performs a ruthless gap analysis between a CV and JD, identifying critical weaknesses and providing a prioritized mitigation strategy. → workflows/skill-gap.md
/job-hunt: Performs a live internet search to find active job postings perfectly matching the user's role, location (Remote/Hybrid), and constraints. → workflows/job-hunt.md
/career-pivot: Builds a full transition roadmap for candidates switching industries, including transferable skills mapping, gap analysis, narrative reframing, and a 90-day action plan. → workflows/career-pivot.md
🔋 Secondary Workflows (Power Tools)
/cold-outreach: Generates 3 variants of targeted, ROI-focused cold outreach messages for LinkedIn or Email to connect with Hiring Managers. → workflows/cold-outreach.md
/promo-pitch: Builds a data-driven internal business case (ROI-focused) to ask for a raise or promotion within the current company. → workflows/promo-pitch.md
/follow-up: Drafts strategic post-interview thank-you emails that reiterate the candidate's value and ability to solve specific pain points discussed. → workflows/follow-up.md
/case-study: Structures a complex professional project into a clear, business-focused Case Study (PAR method) for a portfolio or presentation. → workflows/case-study.md
/linkedin-post: Generates 3 high-engagement LinkedIn post variants (Short, Story, Data-Driven) to build passive recruiter visibility. → workflows/linkedin-post.md
/negotiation-counter: Generates a data-backed counter-offer strategy when an initial salary offer is below expectations, including a full email script and alternative levers. → workflows/negotiation-counter.md
/reference-check: Strategically selects professional references and generates briefing scripts to maximize offer conversion. → workflows/reference-check.md
/company-research: Performs live research on a target company before an interview, generating a full intelligence report with culture signals, pain points, and 5 tailored questions. → workflows/company-research.md
/offer-compare: Compares 2+ competing job offers across 5 dimensions (compensation, growth, alignment, stability, work-life fit), scoring each and providing a concrete recommendation. → workflows/offer-compare.md
/personal-brand-audit: Audits the candidate's full digital footprint (Google, LinkedIn, GitHub, portfolio, other platforms), flags inconsistencies, and provides a prioritized action plan for recruiter-facing visibility. → workflows/personal-brand-audit.md
Update Market Data / /update-market-data

See dedicated workflow: workflows/update-market-data.md

Reference Materials
market_data.md
Weekly Installs
21
Repository
balbus95/career…n-engine
GitHub Stars
1
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn