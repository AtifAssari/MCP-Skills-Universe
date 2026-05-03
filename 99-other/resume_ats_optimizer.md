---
rating: ⭐⭐⭐
title: resume ats optimizer
url: https://skills.sh/paramchoudhary/resumeskills/resume-ats-optimizer
---

# resume ats optimizer

skills/paramchoudhary/resumeskills/Resume ATS Optimizer
Resume ATS Optimizer
Installation
$ npx skills add https://github.com/paramchoudhary/resumeskills --skill 'Resume ATS Optimizer'
Summary

Resume optimization for Applicant Tracking Systems with keyword matching and compatibility analysis.

Parses resumes for ATS compatibility, identifies formatting issues (tables, headers/footers, non-standard fonts), and flags file format problems that break automated screening
Extracts and analyzes keywords from job descriptions across hard skills, soft skills, and industry terms, then calculates match scores between resume and posting
Provides structured compatibility reports with specific keyword placement recommendations, before/after examples, and estimated score improvements
Includes industry-specific guidance for tech, finance, healthcare, and marketing roles, plus strategies for career changers and recent graduates
SKILL.md
Resume ATS Optimizer
When to Use This Skill

Use this skill when the user wants to:

Optimize their resume for Applicant Tracking Systems (ATS)
Check if their resume will pass automated screening
Understand why their applications aren't getting responses
Mentions keywords like: "ATS", "not getting interviews", "resume not working", "optimize resume", "keyword optimization"

Also use when the user provides a resume file and mentions they're applying to jobs.

Core Capabilities
Parse resume and test ATS compatibility
Extract and analyze keywords against job descriptions
Identify formatting issues that break ATS parsers
Calculate match scores between resume and job postings
Suggest keyword additions and placements
Generate ATS-friendly formatting recommendations
The ATS Problem

75% of resumes are rejected by Applicant Tracking Systems before a human ever sees them. Companies use ATS to:

Filter out unqualified candidates automatically
Search for specific keywords from job requirements
Parse resumes into structured data
Rank candidates by keyword match percentage

Common reasons resumes fail ATS:

Poor formatting (tables, columns, headers/footers)
Missing keywords from job description
Inconsistent section headers
Non-standard fonts or special characters
Text embedded in images
Incorrect file format
ATS Compatibility Checklist
File Format
✅ Use .docx or .pdf (not .pages, .odt)
✅ PDF must be text-based, not scanned image
✅ File name: "FirstName_LastName_Resume.pdf"
Font & Formatting
✅ Standard fonts: Arial, Calibri, Georgia, Times New Roman
✅ Font size: 10-12pt for body, 14-16pt for headers
✅ No text boxes, tables, or columns
✅ No headers/footers (put contact info in body)
✅ No images, graphics, or charts
✅ Consistent date formats (MM/YYYY)
✅ Standard bullet points (•, -, *)
Section Headers

Use standard, recognizable headers:

✅ "Professional Experience" or "Work Experience" (not "Where I've Been")
✅ "Education" (not "Academic Background")
✅ "Skills" (not "Core Competencies")
✅ "Summary" or "Professional Summary"
Contact Information
John Smith
email@example.com | (555) 123-4567 | LinkedIn: linkedin.com/in/johnsmith
San Francisco, CA


NOT in header/footer, and avoid:

❌ Tables for contact info
❌ Special characters in email
❌ Multiple phone numbers
❌ Full mailing address (city/state is enough)
Keyword Optimization Process
Step 1: Extract Job Description Keywords

Identify three types of keywords:

Hard Skills (Technical)

Programming languages (Python, Java, SQL)
Tools and platforms (Salesforce, AWS, Excel)
Certifications (PMP, CPA, CFA)
Methodologies (Agile, Six Sigma, SDLC)

Soft Skills

Leadership, collaboration, communication
Problem-solving, analytical thinking
Project management, stakeholder management

Industry Terms

B2B, SaaS, e-commerce
Enterprise, SMB, mid-market
ARR, MRR, churn rate
Step 2: Match Analysis

For each keyword in job description:

Check if exact phrase appears in resume
Check for synonyms or variations
Count frequency of mention
Note location (summary, experience, skills)
Step 3: Calculate Match Score
Match Score = (Keywords Matched / Total Required Keywords) × 100

Example:
Job has 20 required keywords
Your resume has 15 of them
Match Score = 75%

Target: 80%+ for strong match

Step 4: Keyword Placement Strategy

Priority 1: Professional Summary (Top of Resume)

Include 5-8 most important keywords
Use naturally in 3-4 sentence paragraph
Example: "Data Scientist with 5+ years using Python, SQL, and machine learning to drive business insights..."

Priority 2: Skills Section

List keywords explicitly
Group by category if needed
Use exact phrasing from job description

Priority 3: Experience Bullets

Incorporate keywords into achievement statements
Don't force keywords unnaturally
Use variations throughout

Keyword Density Guidelines:

Critical keywords: Appear 2-4 times throughout resume
Important keywords: Appear 1-2 times
Don't keyword stuff - keep it natural
Vary phrasing (e.g., "led team" and "team leadership")
Analysis Output Format

When analyzing a resume, provide this structured report:

# ATS COMPATIBILITY REPORT

## Overall Score: [X]/100

### File Format Check ✅/❌
- Format: [DOCX/PDF]
- Text extraction: [Success/Failed]
- File size: [X KB/MB]

### Formatting Issues
✅ No tables or columns detected
❌ Contact info in header (move to body)
⚠️  Two different font sizes in skills section

### Keyword Analysis

JOB REQUIREMENTS vs YOUR RESUME:

**Critical Keywords (Must Have):**
✅ Project Management - Found 3x
✅ Agile/Scrum - Found 2x
❌ Stakeholder Management - MISSING (mentioned 5x in JD)
❌ Budget Management - MISSING (mentioned 3x in JD)

**Important Keywords:**
✅ Cross-functional teams - Found 1x
⚠️  "Risk management" - You have "risk mitigation" (close but not exact match)
✅ Process improvement - Found 2x

**Match Score: 65%**
Target: 80%+ recommended

### Recommended Changes

**1. Add Missing Keywords:**

In Professional Summary, change:
"Experienced project manager with proven track record..."

To:
"Experienced project manager with proven track record in stakeholder management and budget oversight..."

In Experience section, add bullet:
"Managed stakeholder communication across 3 departments and executive leadership team"
"Directed budget management for $2.5M project portfolio"

**2. Fix Formatting:**
- Move contact information from header to body of resume
- Make all skill section items same font size (currently 10pt and 11pt mixed)

**3. Strengthen Existing Keywords:**
Change "risk mitigation" to "risk management" for exact match

### Estimated New Match Score: 85%

Common ATS Failure Patterns
Pattern 1: Creative Formatting
❌ PROBLEM:
[Two-column layout with graphics]
[Skill bars and proficiency charts]
[Text in colored boxes]

✅ SOLUTION:
- Single column layout
- Text-only skills list
- Simple bullet points

Pattern 2: Unconventional Section Names
❌ PROBLEM:
"My Journey" (instead of Experience)
"What I Bring to the Table" (instead of Skills)
"Academic Pursuits" (instead of Education)

✅ SOLUTION:
Use standard headers ATS recognizes

Pattern 3: Missing Keywords
❌ PROBLEM:
Job requires: "Python, SQL, Data Visualization"
Resume says: "Programming, databases, making charts"

✅ SOLUTION:
Use exact terminology from job description

Pattern 4: Keyword Stuffing
❌ PROBLEM:
Skills: Python, Python programming, Python developer, Python expert, Python specialist, Advanced Python...

✅ SOLUTION:
Skills: Python, SQL, JavaScript, React, Node.js
(Then incorporate naturally in bullets)

Industry-Specific Considerations
Tech Resumes
Emphasize programming languages and frameworks
Include GitHub, portfolio links in Skills section (not header)
Certifications and courses matter highly
Business/Finance
Focus on software proficiency (Excel, SAP, Salesforce)
Certifications critical (CPA, CFA, PMP)
Industry keywords (P&L, ROI, KPI)
Healthcare
Licenses and certifications required
Specific systems (Epic, Cerner, MEDITECH)
Compliance keywords (HIPAA, Joint Commission)
Marketing
Platform expertise (HubSpot, Salesforce, Google Analytics)
Channel keywords (SEO, PPC, email marketing)
Metrics and results-driven language
Edge Cases & Special Situations
Career Changers
Focus on transferable skills
Use keywords from TARGET industry, not just current
May need two resume versions for ATS
Recent Graduates
Education section becomes priority for keywords
Include relevant coursework, projects
Internships count as experience - use those keywords
Executive Level
ATS still matters for senior roles
Focus on strategic keywords
Include board experience, P&L size, team size
Gaps in Employment
Use years only (not months) if it helps
Include freelance/consulting with keywords
Volunteer work can include relevant keywords
Implementation Checklist

When helping user optimize for ATS:

✅ Scan current resume for ATS compatibility issues
✅ Analyze job description for required keywords
✅ Calculate current match score
✅ Identify specific missing keywords
✅ Suggest exact placements for new keywords
✅ Flag formatting problems
✅ Provide before/after examples
✅ Re-score after suggested changes
✅ Verify file format and naming
✅ Test with ATS simulator if possible
Success Metrics

After optimization, the resume should:

Score 80%+ match for target job descriptions
Pass ATS parsing test (all sections recognized)
Have zero formatting errors
Include all critical keywords 2-4x each
Read naturally (not keyword-stuffed)
Be ready to submit immediately
Weekly Installs
–
Repository
paramchoudhary/…meskills
GitHub Stars
405
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn