---
rating: ⭐⭐⭐
title: author-profile
url: https://skills.sh/mwguerra/claude-code-plugins/author-profile
---

# author-profile

skills/mwguerra/claude-code-plugins/author-profile
author-profile
Installation
$ npx skills add https://github.com/mwguerra/claude-code-plugins --skill author-profile
SKILL.md
Author Profile

Create and maintain consistent author voice across all articles.

Profile Location

Stored in: .article_writer/article_writer.db (authors table)

Schema: .article_writer/schemas/authors.schema.json

Two Ways to Create an Author
Option 1: Manual Questionnaire

Ask questions in conversational groups (2-3 at a time):

Identity
What name/identifier for this author? (e.g., "mwguerra")
Display name? (e.g., "MW Guerra")
Professional role(s)?
Years/areas of experience?
Expertise areas?
Languages
Primary writing language? (e.g., pt_BR, en_US)
Translation target languages?
Tone (1-10)
Casual (1) vs Formal (10)?
Neutral (1) vs Opinionated (10)?
Vocabulary
Terms readers know (use freely)?
Terms to always explain?
Style
Signature phrases?
Phrases to avoid?
Positions
Strong technology opinions?
Topics to stay neutral on?
Example
Write 2-3 sentences in your voice as example.
Option 2: Extract from Transcripts

Use Skill(voice-extractor) for transcript analysis.

If the author has recordings (podcasts, interviews, videos, meetings):

Prepare transcripts - Get transcription files with speaker labels
Run analysis:
bun run "${CLAUDE_PLUGIN_ROOT}"/scripts/voice-extractor.ts --speaker "Name" transcripts/*.txt

Review extracted data - Communication style, phrases, vocabulary
Add identity info - Name, role, expertise, languages (manual)
Merge - Combine extracted + manual data
Option 3: Combined Approach (Recommended)

Best results come from combining both:

Extract voice patterns from transcripts
Add identity/expertise info manually
Review and refine the merged profile
Author JSON Structure
{
  "id": "author-slug",
  "name": "Display Name",
  "languages": ["pt_BR", "en_US"],
  "role": "Senior Developer",
  "experience": "10+ years",
  "expertise": ["Laravel", "PHP", "Architecture"],
  "tone": {
    "formality": 4,
    "opinionated": 7
  },
  "vocabulary": {
    "use_freely": ["Controllers", "Middleware", "API"],
    "always_explain": ["DDD", "CQRS", "Event Sourcing"]
  },
  "phrases": {
    "signature": ["Na prática...", "Vamos direto ao ponto:"],
    "avoid": ["Simplesmente", "É só fazer..."]
  },
  "opinions": {
    "strong_positions": ["Tests are essential", "Fat models are bad"],
    "stay_neutral": ["Tabs vs spaces", "IDE preferences"]
  },
  "example_voice": "Sample paragraph in author's voice...",
  "voice_analysis": {
    "extracted_from": ["podcast_ep1.txt", "interview.txt"],
    "sample_count": 156,
    "total_words": 12450,
    "sentence_structure": {
      "avg_length": 14.5,
      "variety": "moderate length, conversational",
      "question_ratio": 12.3
    },
    "communication_style": [
      { "trait": "enthusiasm", "percentage": 28.5 },
      { "trait": "analytical", "percentage": 24.1 }
    ],
    "characteristic_expressions": ["you know", "the thing is"],
    "sentence_starters": ["I think", "So the"],
    "signature_vocabulary": ["approach", "strategy", "implementation"],
    "analyzed_at": "2025-01-15T10:00:00Z"
  },
  "notes": "Additional style notes..."
}

Voice Analysis Fields

When transcripts are analyzed, these fields are populated:

Field	Description
extracted_from	Transcript files analyzed
sample_count	Speaking turns analyzed
total_words	Total words in analysis
sentence_structure	Length, variety, question frequency
communication_style	Traits: enthusiasm, hedging, directness, etc.
characteristic_expressions	Frequently used phrases/fillers
sentence_starters	Common ways to start sentences
signature_vocabulary	Words that characterize the speaker
Using Voice Analysis When Writing

When writing articles, use voice_analysis data:

Sentence structure: Match avg_length and variety
Tone: Follow communication_style traits
Natural speech: Sprinkle characteristic_expressions naturally
Vocabulary: Prefer words from signature_vocabulary
Sentence starters: Use patterns from sentence_starters
Multi-Language Workflow
Article written in author's primary language (first in array)
After completion, translated to other languages
Each file named: {slug}.{language}.md

Example for author with ["pt_BR", "en_US"]:

content/articles/2025_01_15_rate-limiting/
├── rate-limiting.pt_BR.md    # Primary (written first)
└── rate-limiting.en_US.md    # Translation

Default Author

If article task doesn't specify author:

Author with lowest sort_order in the database is used
Their language settings apply
Their voice/tone is followed
Updating Authors
Add More Transcript Data
# Analyze new transcripts for existing author
bun run "${CLAUDE_PLUGIN_ROOT}"/scripts/voice-extractor.ts \
  --speaker "Name" \
  --author-json \
  new_podcast.txt > new_analysis.json

# Merge into existing profile (manually or via command)

When to Update
New transcript data available
Writing style evolves
Feedback indicates tone mismatch
New expertise develops
Weekly Installs
20
Repository
mwguerra/claude…-plugins
GitHub Stars
29
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass