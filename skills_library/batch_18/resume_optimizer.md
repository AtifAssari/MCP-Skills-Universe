---
title: resume-optimizer
url: https://skills.sh/jackjin1997/clawforge/resume-optimizer
---

# resume-optimizer

skills/jackjin1997/clawforge/resume-optimizer
resume-optimizer
Installation
$ npx skills add https://github.com/jackjin1997/clawforge --skill resume-optimizer
SKILL.md
Resume Optimizer

Build professional, ATS-optimized resumes with PDF export capabilities.

Capabilities
Create Resumes - Build new resumes from user information with professional formatting
Customize Resumes - Tailor existing resumes for specific roles or per user requests
Analyze Resumes - Review resumes and provide actionable improvement recommendations
Export to PDF - Generate downloadable, ATS-friendly PDF documents
Workflow Decision Tree
Creating a New Resume
Gather user information (experience, education, skills, target role)
Select appropriate format (see format selection guide below)
Read references/templates.md for the chosen template
Build resume content following references/best-practices.md
Generate PDF using scripts/generate_resume_pdf.py
Customizing an Existing Resume
Review the provided resume content
Understand the target role/changes requested
Read references/ats-optimization.md for keyword integration
Apply modifications following best practices
Generate updated PDF
Analyzing a Resume
Parse the resume content
Check against criteria in references/analysis-checklist.md
Identify strengths and improvement areas
Provide specific, actionable recommendations
Optionally offer to implement changes
Format Selection Guide

Chronological (Most Common)

Use for: Consistent work history in same field, clear career progression
Best for: Most professionals staying in their field
Read: references/templates.md → Chronological Template section

Functional

Use for: Career changers, employment gaps, emphasizing transferable skills
Best for: Returning to workforce, diverse experience across fields
Read: references/templates.md → Functional Template section

Combination

Use for: Mid-career professionals balancing skills and progression
Best for: Diverse skill sets, career changers with relevant experience
Read: references/templates.md → Combination Template section
PDF Generation

Use the provided script to create professional PDFs:

python3 scripts/generate_resume_pdf.py \
  --input resume_content.json \
  --output resume.pdf \
  --format chronological


The script uses reportlab to create clean, ATS-compatible PDFs with:

Professional typography (Helvetica)
Proper margins and spacing (0.75" all sides)
Clean section headers
Bullet point formatting
Consistent visual hierarchy
Essential References

Before creating any resume, read:

references/best-practices.md - Core resume writing principles
references/ats-optimization.md - ATS compatibility requirements
references/templates.md - Format-specific templates

Before analyzing a resume, read:

references/analysis-checklist.md - Evaluation criteria and scoring
Quick Start Examples

Creating a resume:

User: "Help me build a resume. I have 5 years in marketing."

Steps:
1. Gather: Current role, key achievements, education, certifications
2. Format: Chronological (clear progression in same field)
3. Build: Use template from references/templates.md
4. Keywords: Integrate from job description per ats-optimization.md
5. Export: Generate PDF to /mnt/user-data/outputs/


Tailoring for a role:

User: "Tailor my resume for this job [job description]"

Steps:
1. Parse job description for required skills/keywords
2. Identify gaps between resume and requirements
3. Reorder bullets to lead with relevant achievements
4. Integrate keywords naturally throughout
5. Update summary to mirror key requirements
6. Generate updated PDF


Analyzing a resume:

User: "Review my resume and tell me how to improve it"

Steps:
1. Read references/analysis-checklist.md
2. Evaluate each section against criteria
3. Score: Content, Format, ATS-compatibility
4. Identify top 3-5 priority improvements
5. Provide specific rewrite examples
6. Offer to implement changes

Output Requirements

All generated resumes must:

Be saved to /mnt/user-data/outputs/ for user download
Use descriptive filenames: FirstName_LastName_Resume.pdf
Include a download link using computer:// protocol
Follow ATS-friendly formatting (no tables, text boxes, or graphics)
Code Style

When generating Python scripts for PDF creation:

Use reportlab for PDF generation
Keep code concise and functional
Handle errors gracefully
Test output before delivering to user
Weekly Installs
31
Repository
jackjin1997/clawforge
GitHub Stars
7
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass