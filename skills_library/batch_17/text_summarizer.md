---
title: text_summarizer
url: https://skills.sh/rscheiwe/open-skills/text_summarizer
---

# text_summarizer

skills/rscheiwe/open-skills/text_summarizer
text_summarizer
Installation
$ npx skills add https://github.com/rscheiwe/open-skills --skill text_summarizer
SKILL.md
Text Summarizer Skill

A more complex example that demonstrates text processing capabilities.

What it does

This skill takes a long piece of text and:

Analyzes the text (word count, sentence count, etc.)
Extracts key points
Creates a bullet-point summary
Generates a statistics report
Usage
Input
{
  "text": "Your long text here...",
  "max_points": 5
}

Output
{
  "summary": "• Point 1\n• Point 2\n• Point 3",
  "stats": {
    "word_count": 150,
    "sentence_count": 8,
    "avg_sentence_length": 18.75
  }
}

Artifacts
summary.md: Markdown file with the formatted summary
stats.json: JSON file with detailed statistics
Algorithm

This is a simple implementation that:

Splits text into sentences
Scores sentences by length and position
Selects top N sentences as summary points

Note: This is a demonstration. For production use, consider using NLP libraries like spaCy or transformers.

Weekly Installs
16
Repository
rscheiwe/open-skills
GitHub Stars
31
First Seen
Jan 24, 2026