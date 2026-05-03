---
rating: ⭐⭐
title: cv-generator
url: https://skills.sh/aalvaaro/skills/cv-generator
---

# cv-generator

skills/aalvaaro/skills/cv-generator
cv-generator
Installation
$ npx skills add https://github.com/aalvaaro/skills --skill cv-generator
SKILL.md
Resume / CV Builder

Build professional, deployable web resumes from any source material. The skill acts as an expert recruiter — not just a template filler — researching the target industry, advising on content strategy, and producing a polished result.

Step 0: Input Collection

Accept one or more sources. The user might provide several files at once (e.g., an old resume PDF + a LinkedIn URL + a Notion page with projects). Collect everything before parsing.

Supported formats and how to read them:

Format	Method
PDF	Read tool (built-in PDF support)
TXT, MD, HTML	Read tool
DOCX, DOC	Bash: textutil -convert txt <file> -stdout (macOS built-in)
URL (website/portfolio)	FirecrawlScrapeTool — scrape and extract relevant content
LinkedIn URL	FirecrawlScrapeTool — scrape public profile. May have limited access; if blocked, ask user to paste/export their LinkedIn data
Notion page	notion-search to find the page → notion-fetch to pull content. If user provides a Notion URL, extract the page ID and fetch directly

If the user provides multiple sources, read them all in parallel using subagents or parallel tool calls.

If no sources are provided, go directly to Step 1 and gather information through the interview.

Step 1: Information Extraction & Summary

Parse all sources and merge into a unified profile. Extract:

Contact info: name, email, phone, location, LinkedIn, portfolio URL, GitHub
Professional summary / objective (if present)
Work experience: company, role, dates, descriptions
Education: institution, degree, dates, honors
Skills: technical and soft skills
Languages: spoken languages and proficiency levels
Other: certifications, projects, publications, volunteer work, awards

Present the extracted information as a clean summary to the user. Highlight:

Any gaps or unclear items ("I found two different job titles at Company X — which is correct?")
Missing sections that would strengthen the resume ("I didn't find any skills listed — should we add those?")
Duplicates or contradictions across sources

Ask the user to confirm, correct, or fill in the gaps before proceeding.

Step 2: Target Role & Industry Research

Ask the user:

What role are you targeting? (job title, seniority level)

What industry or sector? (tech, finance, healthcare, creative, etc.)

Target company (optional but valuable) — accept any combination of:

Company name
Website URL
LinkedIn company page URL
Job posting URL
Any other link (Glassdoor, Crunchbase, etc.)

If the user only gives a name, search for the rest yourself using PerplexitySonarSearchTool ("[company name] website linkedin").

Then research in parallel:

Industry research — use PerplexitySonarSearchTool with 2-3 queries:

"[role] skills in demand [current year]"
"[industry] hiring trends what recruiters look for"
"[role] resume best practices"

Company research (if provided) — gather as much context as possible:

Website: FirecrawlMapTool to discover pages → FirecrawlScrapeTool on careers, about, team, and culture pages. Extract:

Mission, values, and culture
Tech stack or tools they use
How they describe ideal candidates (job listings are gold)
Language and tone (formal? startup-casual? mission-driven?)
Company size, stage, and industry positioning

LinkedIn: FirecrawlScrapeTool on the company LinkedIn URL. Extract:

Company description and specialties
Employee count and growth signals
Recent posts (what they're proud of, what they're hiring for)

Job posting (if provided): FirecrawlScrapeTool to extract the exact requirements, responsibilities, and keywords. This is the most valuable source — the resume should speak directly to what this posting asks for.

Other links (Glassdoor, Crunchbase, etc.): FirecrawlScrapeTool to pull reviews, funding info, or any relevant context.

Synthesis: PerplexitySonarSearchTool with "[company name] culture work environment what is it like to work at" for additional context.

The goal is to understand the target company well enough to tailor the resume's language, emphasis, and keywords to what this specific company values. A resume targeting a scrappy 20-person startup should read differently from one targeting a Fortune 500.

Save the research findings — they inform the recruiter advice in the next step.

Step 3: Recruiter Interview

This is where the skill earns its keep. Based on the extracted information AND the research, act as a senior recruiter specialized in the user's target industry. Walk through these areas:

Content Strategy
What to highlight: Based on the target role, identify which experiences and skills are most relevant. "For a Senior Frontend role, your React migration project at Company X is your strongest card — let's lead with that."
What to reword: Suggest action-verb, achievement-oriented rewording. Don't just say "use action verbs" — rewrite the actual bullet points. "Instead of 'Responsible for managing a team', try 'Led a 12-person engineering team that shipped 3 major products in 6 months'."
What to cut: If something doesn't serve the target role, suggest removing it. Be diplomatic but direct.
What's missing: Based on research, suggest skills or keywords the user should add if they genuinely have them. "Companies hiring for this role frequently mention Kubernetes — do you have experience with that?"
Section Order

Recommend the optimal order based on the user's strongest assets:

Strong experience → Experience first, then Skills, then Education
Recent graduate → Education first, then Projects, then Skills
Career changer → Summary first (framing the transition), then transferable Skills, then Experience
Professional Summary

Draft a 2-3 sentence summary tailored to the target role. Present it for the user to approve or adjust.

Present all suggestions and wait for user confirmation before proceeding. The user might want to discuss or push back — that's expected and healthy.

Step 4: Photo Handling

Ask: "Do you have a photo you'd like to use for your resume? You can share the file path."

If the user provides a photo:

Read the photo with the Read tool to see what we're working with

Determine the appropriate style based on the target industry:

Corporate / Finance / Law: Formal — professional attire, neutral background, clean lighting
Tech / Startup: Smart casual — friendly expression, modern but approachable
Creative / Design / Marketing: Expressive — can be more dynamic, show personality
Academic / Research: Professional but warm — approachable, scholarly

Generate a professional headshot using the reference photo:

Option 1 — infsh CLI (check with which infsh):

infsh app run falai/flux-dev-lora --input '{
  "prompt": "professional headshot portrait, [industry-appropriate description], clean background, studio lighting, high quality, photorealistic",
  "image_url": "[path-to-user-photo]"
}'


Option 2 — HiggsfieldImageTool (Social Toolkit MCP): Use the soul model for portrait generation with an industry-appropriate prompt.

Option 3 — Use original photo as-is: If AI generation isn't available or the user prefers their actual photo, apply CSS treatment: circular crop, subtle shadow, slight desaturation for a polished look.

If no photo provided: skip the photo section in the resume, or offer a tasteful initials avatar via CSS.

Suggest the style to the user and let them choose: "Since you're targeting tech roles, I'd suggest a friendly, smart-casual headshot. Want to go with that, or prefer something more formal?"

Step 5: Visual Style Selection

Present the available styles with a recommendation based on the target industry:

Minimalist

Clean lines, generous whitespace, single accent color, modern sans-serif typography.

Fonts: Outfit + Source Serif 4
Palette: White/light gray base, one bold accent (teal, coral, or slate)
Best for: Design, consulting, product management, UX
Corporate

Traditional structure, authoritative palette, clear hierarchy, serif headings.

Fonts: Playfair Display + Source Sans 3
Palette: Navy, charcoal, white with gold or burgundy accent
Best for: Finance, law, management, enterprise, consulting
Tech

Modern, optional dark mode, monospace accents, subtle code-inspired elements.

Fonts: Space Grotesk + IBM Plex Sans (monospace accents: JetBrains Mono)
Palette: Dark slate or pure white base, electric blue or green accent
Best for: Software engineering, data science, DevOps, IT
Creative

Bold colors, distinctive layout, asymmetric elements, expressive typography.

Fonts: Syne + DM Sans
Palette: Vibrant — deep purple with coral, or midnight with electric yellow
Best for: Marketing, media, arts, advertising, content creation
Academic

Clean, scholarly, reading-focused, structured with subtle refinement.

Fonts: Cormorant Garamond + Libre Franklin
Palette: Warm white, deep blue or forest green accent, warm gray text
Best for: Research, education, healthcare, science

Say something like: "For a Senior Frontend Engineer targeting tech companies, I'd recommend the Tech style — it signals you're in the right world. But if you prefer something cleaner, Minimalist also works well. Which one appeals to you?"

Let the user pick. If they want something custom, adapt.

Step 6: Content Finalization

Apply all the agreed-upon changes from Step 3:

Rewrite bullet points with action verbs and quantified achievements
Reorder sections per the agreed strategy
Insert the professional summary
Add any skills or keywords discussed
Set the final section list

Present the final content outline one more time for sign-off: section order, key bullet points, summary. This is the last checkpoint before building.

Step 7: HTML Generation

Generate a single self-contained index.html file with:

Structure
<project-dir>/
  index.html          ← complete resume (inline CSS + JS)
  images/
    headshot.jpg       ← professional photo (if generated)
  wrangler.jsonc       ← Cloudflare deployment config

Technical Requirements

HTML/CSS:

All CSS inline in a <style> block — no external stylesheets except Google Fonts
Google Fonts loaded via <link> tags
CSS variables for theming (colors, fonts, spacing) so the user can easily tweak later
Fully responsive: mobile (375px), tablet (768px), desktop (1280px+)
Semantic HTML: <header>, <main>, <section>, <article>, <footer>
Print-friendly styles via @media print — hide the download button, clean margins, black text
Subtle micro-interactions: section reveals on scroll, skill bar animations, smooth hover states
Clean, professional — avoid flashy animations that distract from the content

PDF Download Button: Include a floating download button that generates a PDF of the resume. Use html2pdf.js via CDN:

<script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.2/html2pdf.bundle.min.js"></script>


The button should:

Float in the bottom-right corner (or top-right, matching the style)
Hide itself during PDF generation (so it doesn't appear in the PDF)
Use the @media print styles for clean output
Name the file [FirstName]-[LastName]-Resume.pdf
function downloadPDF() {
  const button = document.getElementById('download-btn');
  button.style.display = 'none';
  const element = document.getElementById('resume');
  const opt = {
    margin: 0.5,
    filename: '[Name]-Resume.pdf',
    image: { type: 'jpeg', quality: 0.98 },
    html2canvas: { scale: 2, useCORS: true },
    jsPDF: { unit: 'in', format: 'letter', orientation: 'portrait' }
  };
  html2pdf().set(opt).from(element).save().then(() => {
    button.style.display = '';
  });
}


Photo display:

Circular crop with subtle border/shadow
Sized appropriately for the style (120-160px diameter)
Responsive — scales down on mobile
alt text: "[Name] — Professional headshot"
If no photo: show a tasteful CSS initials circle using the person's initials

Content sections to render (based on what was agreed in Step 6):

Header: name, title, contact info (email, phone, location, LinkedIn, GitHub/portfolio)
Professional summary
Work experience (company, role, dates, achievement bullets)
Education
Skills (grouped by category if applicable — e.g., Languages, Frameworks, Tools)
Languages (if applicable)
Any additional sections agreed upon

Design execution: Apply the chosen visual style from Step 5. Use the exact font pairings and color palettes defined there. The resume should look like it was designed by a professional — distinctive typography, intentional spacing, a clear visual hierarchy that guides the reader's eye from name → summary → experience → skills.

Image Generation for Design Elements (optional)

If the style benefits from subtle design elements (background texture, header pattern), generate them:

Check which infsh — use FLUX for abstract/textural images
Fallback to HiggsfieldImageTool
Final fallback: CSS-only effects (gradients, noise via SVG filters, geometric patterns)

Keep design elements subtle — the content is the star.

Step 8: Deployment

Create wrangler.jsonc in the project directory:

{
  "name": "<firstname-lastname>-resume",
  "compatibility_date": "2025-04-01",
  "assets": {
    "directory": "./"
  }
}


Deploy:

cd <project-dir> && wrangler deploy


Share the live URL with the user. Also open the local file so they can preview:

open <project-dir>/index.html

Behavior Notes
Be a recruiter, not a form filler. The value of this skill is the advice. Anyone can put text in an HTML template. What makes this special is understanding what recruiters in the target industry actually look for and tailoring the resume accordingly.
Research before advising. Don't give generic resume advice. Research the specific industry and role first, then give targeted, informed suggestions based on real data.
Rewrite, don't just suggest. When recommending changes to bullet points or summaries, write the actual new version. "Use action verbs" is unhelpful. "Led a cross-functional team of 8 engineers to deliver a payment processing system handling $2M daily" is useful.
Respect the user's voice. The resume should sound like a polished version of the user, not a generic template. If they have a casual tone, keep it conversational but professional. If they're formal, maintain that.
One page is king (usually). For most roles under 15 years of experience, aim for content that fits one page. For senior/academic roles, two pages is fine. Mention this to the user and let them decide.
Quantify everything possible. Numbers make achievements concrete. "Improved performance" → "Reduced API response time by 40% (from 850ms to 510ms)". Always ask the user for numbers if they're missing.
Handle multiple languages naturally. If the user communicates in Spanish, write the resume in Spanish (unless they ask for English). Research queries should match the target job market's language.
Show your work before building. Present research findings, content suggestions, and the final outline before generating HTML. The user should never be surprised by the output.
Don't invent achievements. Everything in the resume must come from the user's actual experience. Reword and polish, but never fabricate.
Weekly Installs
10
Repository
aalvaaro/skills
First Seen
Mar 25, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykWarn