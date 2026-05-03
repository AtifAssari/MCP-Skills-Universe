---
rating: ⭐⭐⭐
title: karpathy-jobs-bls-visualizer
url: https://skills.sh/aradotso/trending-skills/karpathy-jobs-bls-visualizer
---

# karpathy-jobs-bls-visualizer

skills/aradotso/trending-skills/karpathy-jobs-bls-visualizer
karpathy-jobs-bls-visualizer
Installation
$ npx skills add https://github.com/aradotso/trending-skills --skill karpathy-jobs-bls-visualizer
SKILL.md
karpathy/jobs — BLS Job Market Visualizer

Skill by ara.so — Daily 2026 Skills collection.

A research tool for visually exploring Bureau of Labor Statistics Occupational Outlook Handbook data across 342 occupations. The interactive treemap colors rectangles by employment size (area) and any chosen metric (color): BLS growth outlook, median pay, education requirements, or LLM-scored AI exposure. The pipeline is fully forkable — write a new prompt, re-run scoring, get a new color layer.

Live demo: karpathy.ai/jobs

Installation & Setup
# Clone the repo
git clone https://github.com/karpathy/jobs
cd jobs

# Install dependencies (uses uv)
uv sync
uv run playwright install chromium


Create a .env file with your OpenRouter API key (required only for LLM scoring):

OPENROUTER_API_KEY=your_openrouter_key_here

Full Pipeline — Key Commands

Run these in order for a complete fresh build:

# 1. Scrape BLS pages (non-headless Playwright; BLS blocks bots)
#    Results cached in html/ — only needed once
uv run python scrape.py

# 2. Convert raw HTML → clean Markdown in pages/
uv run python process.py

# 3. Extract structured fields → occupations.csv
uv run python make_csv.py

# 4. Score AI exposure via LLM (uses OpenRouter API, saves scores.json)
uv run python score.py

# 5. Merge CSV + scores → site/data.json for the frontend
uv run python build_site_data.py

# 6. Serve the visualization locally
cd site && python -m http.server 8000
# Open http://localhost:8000

Key Files Reference
File	Description
occupations.json	Master list of 342 occupations (title, URL, category, slug)
occupations.csv	Summary stats: pay, education, job count, growth projections
scores.json	AI exposure scores (0–10) + rationales for all 342 occupations
prompt.md	All data in one ~45K-token file for pasting into an LLM
html/	Raw HTML pages from BLS (~40MB, source of truth)
pages/	Clean Markdown versions of each occupation page
site/index.html	The treemap visualization (single HTML file)
site/data.json	Compact merged data consumed by the frontend
score.py	LLM scoring pipeline — fork this to write custom prompts
Writing a Custom LLM Scoring Layer

The most powerful feature: write any scoring prompt, run score.py, get a new treemap color layer.

1. Edit the prompt in score.py
# score.py (simplified structure)
SYSTEM_PROMPT = """
You are evaluating occupations for exposure to humanoid robotics over the next 10 years.

Score each occupation from 0 to 10:
- 0 = no meaningful exposure (e.g., requires fine social judgment, non-physical)
- 5 = moderate exposure (some tasks automatable, but humans still central)
- 10 = high exposure (repetitive physical tasks, predictable environments)

Consider: physical task complexity, environment predictability, dexterity requirements,
cost of robot vs human, regulatory barriers.

Respond ONLY with JSON: {"score": <int 0-10>, "rationale": "<1-2 sentences>"}
"""

2. Run the scoring pipeline
# The pipeline reads each occupation's Markdown from pages/,
# sends it to the LLM, and writes results to scores.json

# scores.json structure:
{
  "software-developers": {
    "score": 1,
    "rationale": "Software development is digital and cognitive; humanoid robots provide no advantage."
  },
  "construction-laborers": {
    "score": 7,
    "rationale": "Physical, repetitive outdoor tasks are targets for humanoid robotics, though unstructured environments remain challenging."
  }
  // ... 342 occupations total
}

3. Rebuild site data
uv run python build_site_data.py
cd site && python -m http.server 8000

Data Structures
occupations.json entry
{
  "title": "Software Developers",
  "url": "https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm",
  "category": "Computer and Information Technology",
  "slug": "software-developers"
}

occupations.csv columns
slug, title, category, median_pay, education, job_count, growth_percent, growth_outlook


Example row:

software-developers, Software Developers, Computer and Information Technology,
130160, Bachelor's degree, 1847900, 17, Much faster than average

site/data.json entry (merged frontend data)
{
  "slug": "software-developers",
  "title": "Software Developers",
  "category": "Computer and Information Technology",
  "median_pay": 130160,
  "education": "Bachelor's degree",
  "job_count": 1847900,
  "growth_percent": 17,
  "growth_outlook": "Much faster than average",
  "ai_score": 9,
  "ai_rationale": "AI is deeply transforming software development workflows..."
}

Frontend Treemap (site/index.html)

The visualization is a single self-contained HTML file using D3.js.

Color layers (toggle in UI)
Layer	What it shows
BLS Outlook	BLS projected growth category (green = fast growth)
Median Pay	Annual median wage (color gradient)
Education	Minimum education required
Digital AI Exposure	LLM-scored 0–10 AI impact estimate
Adding a new color layer to the frontend
<!-- In site/index.html, find the layer toggle buttons -->
<button onclick="setLayer('ai_score')">Digital AI Exposure</button>

<!-- Add your new layer button -->
<button onclick="setLayer('robotics_score')">Humanoid Robotics</button>

// In the colorScale function, add a case for your new field:
function getColor(d, layer) {
  if (layer === 'robotics_score') {
    // scores 0-10, blue = low exposure, red = high
    return d3.interpolateRdYlBu(1 - d.robotics_score / 10);
  }
  // ... existing cases
}


Then update build_site_data.py to include your new score field in data.json.

Generating the LLM-Ready Prompt File

Package all 342 occupations + aggregate stats into a single file for LLM chat:

uv run python make_prompt.py
# Produces prompt.md (~45K tokens)
# Paste into Claude, GPT-4, Gemini, etc. for data-grounded conversation

Scraping Notes

The BLS blocks automated bots, so scrape.py uses non-headless Playwright (real visible browser window):

# scrape.py key behavior
browser = await p.chromium.launch(headless=False)  # Must be visible
# Pages saved to html/<slug>.html
# Already-scraped pages are skipped (cached)


If scraping fails or is rate-limited:

The html/ directory already contains cached pages in the repo
You can skip scraping entirely and run from process.py onward
If re-scraping, add delays between requests to avoid blocks
Common Patterns
Re-score only missing occupations
import json, os

with open("scores.json") as f:
    existing = json.load(f)

with open("occupations.json") as f:
    all_occupations = json.load(f)

# Find gaps
missing = [o for o in all_occupations if o["slug"] not in existing]
print(f"Missing scores: {len(missing)}")
# Then run score.py with a filter for missing slugs

Parse a single occupation page manually
from parse_detail import parse_occupation_page
from pathlib import Path

html = Path("html/software-developers.html").read_text()
data = parse_occupation_page(html)
print(data["median_pay"])     # e.g. 130160
print(data["job_count"])      # e.g. 1847900
print(data["growth_outlook"]) # e.g. "Much faster than average"

Load and query occupations.csv
import pandas as pd

df = pd.read_csv("occupations.csv")

# Top 10 highest paying occupations
top_pay = df.nlargest(10, "median_pay")[["title", "median_pay", "growth_outlook"]]
print(top_pay)

# Filter: fast growth + high pay
high_value = df[
    (df["growth_percent"] > 10) &
    (df["median_pay"] > 80000)
].sort_values("median_pay", ascending=False)

Combine CSV with AI scores for analysis
import pandas as pd, json

df = pd.read_csv("occupations.csv")

with open("scores.json") as f:
    scores = json.load(f)

df["ai_score"] = df["slug"].map(lambda s: scores.get(s, {}).get("score"))
df["ai_rationale"] = df["slug"].map(lambda s: scores.get(s, {}).get("rationale"))

# High AI exposure, high pay — reshaping, not disappearing
high_exposure_high_pay = df[
    (df["ai_score"] >= 8) &
    (df["median_pay"] > 100000)
][["title", "median_pay", "ai_score", "growth_outlook"]]
print(high_exposure_high_pay)

Troubleshooting

playwright install fails

uv run playwright install --with-deps chromium


BLS scraping blocked / returns empty pages

Ensure headless=False in scrape.py (already the default)
Add manual delays; do not run in CI
The cached html/ directory in the repo can be used directly

score.py OpenRouter errors

Verify OPENROUTER_API_KEY is set in .env
Check your OpenRouter account has credits
Default model is Gemini Flash — change model in score.py for a different LLM

site/data.json not updating after re-scoring

# Always rebuild site data after changing scores.json
uv run python build_site_data.py


Treemap shows blank / no data

Confirm site/data.json exists and is valid JSON
Serve with python -m http.server (not file:// — CORS blocks local JSON fetch)
Check browser console for fetch errors
Important Caveats (from the project)
AI Exposure ≠ job disappearance. A score of 9/10 means AI is transforming the work, not eliminating demand. Software developers score 9/10 but demand is growing.
Scores are rough LLM estimates (Gemini Flash via OpenRouter), not rigorous economic predictions.
The tool does not account for demand elasticity, latent demand, regulatory barriers, or social preferences for human workers.
This is a development/research tool, not an economic publication.
Weekly Installs
1.1K
Repository
aradotso/trending-skills
GitHub Stars
42
First Seen
Mar 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn