---
rating: ⭐⭐⭐
title: apply-job
url: https://skills.sh/theaayushstha1/job-applier-agent/apply-job
---

# apply-job

skills/theaayushstha1/job-applier-agent/apply-job
apply-job
Installation
$ npx skills add https://github.com/theaayushstha1/job-applier-agent --skill apply-job
SKILL.md
Job Application Agent

Automated job application system with multi-channel recruiter outreach.

Quick Start
/apply-job <url>              # Apply to specific job
/apply-job search <query>     # Search and batch apply
/apply-job outreach <url>     # Recruiter outreach only
/apply-job status             # View statistics
/apply-job score <url>        # Score job fit only

Setup Required

Before first use, ensure these files exist:

File	Purpose
$APPLIER_HOME/data/profile.json	Your personal info (from template)
$APPLIER_HOME/data/applications.json	Application tracking
$APPLIER_HOME/resume/master_resume.md	Your complete resume
$APPLIER_HOME/templates/cover_letter.md	Cover letter template
$APPLIER_HOME/templates/cold_email.md	Cold email template

$APPLIER_HOME = ~/job-applier-agent (cross-platform)

See SETUP.md for installation instructions.

Core Principles
AUTO-PROCEED Mode
DO NOT ask for confirmation at routine steps
JUST DO IT - proceed through entire workflow automatically
ONLY STOP for: login walls, CAPTCHA, critical errors, fit score < 5.0
⚠️ Outreach Order (CRITICAL)
1. Find recruiters on LinkedIn (names, titles, URLs)
2. Discover email addresses (WebSearch company email pattern)
3. Send cold emails via Gmail FIRST
4. THEN send LinkedIn connection requests
5. Track everything in applications.json


Email = PRIMARY (higher response rate). LinkedIn = SECONDARY.

Workflow: Apply to Job URL
Step 1: Extract Job Description
1. Navigate to job URL with Playwright
2. Capture page snapshot
3. Extract: title, company, location, requirements
4. Identify key skills/technologies

Step 2: Score Job Fit (0-10 each)
Technical Fit: Skills match percentage
Level Match: Appropriate for experience level
Location: Remote/local/relocation
Mission: Company alignment

Score >= 5.0 → AUTO-PROCEED | Score < 5.0 → Notify user

Step 3: Tailor Resume
1. Read $APPLIER_HOME/resume/master_resume.md
2. Reorder projects by relevance to JD
3. Emphasize matching skills (use JD keywords)
4. Save to $APPLIER_HOME/applications/<Company>/


Rules: Never add fake skills. Never fabricate metrics. Only reorder/emphasize.

Step 4: Generate Cover Letter
1. Read $APPLIER_HOME/templates/cover_letter.md
2. Research company (WebFetch)
3. Personalize for role + company
4. Keep to 250-350 words
5. Save to $APPLIER_HOME/applications/<Company>/

Step 5: Auto-Fill Application

Use Playwright to fill forms based on platform:

LinkedIn Easy Apply
Company career pages (Greenhouse, Lever, Workday, ADP, etc.)
Upload resume, add cover letter if field exists
Step 6: Track & Screenshot
1. Take confirmation screenshot
2. Update $APPLIER_HOME/data/applications.json
3. Update stats

Step 7: Recruiter Outreach

See WORKFLOWS.md for detailed outreach steps.

Summary:

Search LinkedIn for company recruiters (3+ people)
Discover emails via WebSearch (company email pattern)
Send cold emails via Gmail (use template)
Send LinkedIn connections (after emails)
Track all outreach in applications.json
Recruiter Contact Discovery

Use publicly available contact information only:

1. Check the recruiter's LinkedIn profile for contact info
2. Check the company careers page for recruiter contact details
3. Use the company's public contact form if no direct contact is available

Profile Configuration

All personal data comes from $APPLIER_HOME/data/profile.json:

{
  "personal": {
    "name": "Your Name",
    "email": "you@email.com",
    "phone": "123-456-7890",
    "location": "City, State"
  },
  "links": {
    "website": "https://yoursite.com",
    "linkedin": "linkedin.com/in/you",
    "github": "github.com/you"
  },
  "education": {
    "school": "University Name",
    "degree": "BS Computer Science",
    "gpa": "3.9",
    "graduation": "May 2026"
  },
  "headline": "Your professional headline",
  "top_skills": ["Python", "React", "AWS"],
  "flagship_project": {
    "name": "Project Name",
    "description": "Brief description",
    "users": "100+"
  },
  "work_auth": true,
  "willing_to_relocate": true,
  "location_preference": ["Remote", "NYC", "SF"]
}


See profile-template.json for full template.

Application Tracking

$APPLIER_HOME/data/applications.json schema:

{
  "applications": [{
    "id": "company-date-001",
    "company": "Company Name",
    "role": "Job Title",
    "url": "https://...",
    "platform": "linkedin|greenhouse|workday|adp",
    "applied_date": "2026-01-27",
    "status": "applied|interviewed|rejected|offer",
    "fit_score": 7.5,
    "cover_letter": true,
    "outreach": [{
      "name": "Recruiter Name",
      "title": "Technical Recruiter",
      "email": "recruiter@company.com",
      "linkedin": "linkedin.com/in/...",
      "email_sent": true,
      "connection_sent": true,
      "date": "2026-01-27"
    }]
  }],
  "stats": {
    "total": 0,
    "applied": 0,
    "interviewed": 0,
    "emailsSent": 0,
    "connectionsSent": 0
  }
}

Cold Email Template
Subject: Referral Request - [Role] Application | [School] [Major] Senior

Hi [First Name],

I just applied for the [Role] position at [Company] and wanted to reach out.

I'm a [Major] senior at [School] ([GPA] GPA) graduating [Graduation].
[Flagship project description with metrics].

[1-2 sentences about why THIS company excites you]

Would appreciate if you could review my application or put in a referral.

Thanks!
[Name]
[Website]
[Phone]


Rules: Under 150 words. Personalize company line. Include contact info.

Error Handling
Error	Action
Login required	Notify user, wait for "continue"
CAPTCHA	Notify user, wait
Rate limit	Wait 60s, retry once, skip if still blocked
Email failed	Log, continue with LinkedIn
Form field missing	Screenshot, ask user
Reference Files
File	Content
WORKFLOWS.md	Detailed step-by-step workflows
SETUP.md	Installation & configuration
profile-template.json	Profile data template
Path Variables
Variable	Default	Description
$APPLIER_HOME	~/job-applier-agent	Base directory
$APPLICATIONS_DIR	$APPLIER_HOME/applications	Per-company files

Cross-platform: Use ~/ which expands to home directory on all OS.

Best Practices
Email FIRST, LinkedIn SECOND - Always send emails before connections
AUTO-PROCEED - Don't ask, just do (except critical errors)
Track everything - Update applications.json after every action
Personalize - Reference specific company details in outreach
Screenshot - Capture confirmation for records
Be honest - Never fabricate skills or metrics

Line Count: ~280 (under 500 ✓) Cross-Platform: Yes (uses ~/ paths) ✓ User-Agnostic: Yes (data in profile.json) ✓

Weekly Installs
59
Repository
theaayushstha1/…er-agent
GitHub Stars
4
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn