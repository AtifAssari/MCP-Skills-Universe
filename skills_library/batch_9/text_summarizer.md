---
title: text-summarizer
url: https://skills.sh/dkyazzentwatwa/chatgpt-skills/text-summarizer
---

# text-summarizer

skills/dkyazzentwatwa/chatgpt-skills/text-summarizer
text-summarizer
Installation
$ npx skills add https://github.com/dkyazzentwatwa/chatgpt-skills --skill text-summarizer
Summary

Extractive summarization from long documents with flexible length control and batch processing.

Supports three algorithms (TextRank, LSA, frequency-based) with configurable language support
Control summary length by ratio, sentence count, or word count; optionally preserve original sentence order
Extract key points as bullet-point summaries alongside full-text summaries
Batch process multiple documents or entire directories with consistent parameters
Available as Python API or CLI with file input/output options
SKILL.md
Text Summarizer

Create concise summaries from long text documents using extractive summarization. Identifies and extracts the most important sentences while preserving meaning.

Quick Start
from scripts.text_summarizer import TextSummarizer

# Summarize text
summarizer = TextSummarizer()
summary = summarizer.summarize(long_text, ratio=0.2)  # 20% of original
print(summary)

# Summarize file
summary = summarizer.summarize_file("article.txt", num_sentences=5)

Features
Extractive Summarization: Selects key sentences from original text
Length Control: By ratio, sentence count, or word count
Multiple Algorithms: TextRank, LSA, frequency-based
Key Points: Extract bullet-point summaries
Batch Processing: Summarize multiple documents
Preserve Structure: Maintains sentence order option
API Reference
Initialization
summarizer = TextSummarizer(
    method="textrank",    # textrank, lsa, frequency
    language="english"
)

Summarization
# By ratio (20% of original length)
summary = summarizer.summarize(text, ratio=0.2)

# By sentence count
summary = summarizer.summarize(text, num_sentences=5)

# By word count
summary = summarizer.summarize(text, max_words=100)

Key Points Extraction
# Get bullet points
points = summarizer.extract_key_points(text, num_points=5)
for point in points:
    print(f"• {point}")

Batch Processing
# Summarize multiple texts
texts = [text1, text2, text3]
summaries = summarizer.summarize_batch(texts, ratio=0.2)

# Summarize files in directory
summaries = summarizer.summarize_directory("./articles/", ratio=0.3)

Options
# Preserve original sentence order
summary = summarizer.summarize(text, preserve_order=True)

# Include title/first sentence
summary = summarizer.summarize(text, include_first=True)

# Minimum sentence length filter
summarizer.min_sentence_length = 10

CLI Usage
# Summarize text file
python text_summarizer.py --input article.txt --ratio 0.2

# Specific sentence count
python text_summarizer.py --input article.txt --sentences 5

# Extract key points
python text_summarizer.py --input article.txt --points 5

# Batch process
python text_summarizer.py --input-dir ./docs --output-dir ./summaries --ratio 0.3

# Output to file
python text_summarizer.py --input article.txt --output summary.txt --ratio 0.2

CLI Arguments
Argument	Description	Default
--input	Input file path	Required
--output	Output file path	stdout
--input-dir	Directory of files	-
--output-dir	Output directory	-
--ratio	Summary ratio (0.0-1.0)	0.2
--sentences	Number of sentences	-
--words	Maximum words	-
--points	Extract N key points	-
--method	Algorithm to use	textrank
--preserve-order	Keep sentence order	False
Examples
News Article Summary
summarizer = TextSummarizer()

article = """
[Long news article text...]
"""

# Get a 3-sentence summary
summary = summarizer.summarize(article, num_sentences=3)
print("Summary:")
print(summary)

# Get key points
points = summarizer.extract_key_points(article, num_points=5)
print("\nKey Points:")
for i, point in enumerate(points, 1):
    print(f"{i}. {point}")

Research Paper Abstract
summarizer = TextSummarizer(method="lsa")

paper = open("research_paper.txt").read()

# Create abstract-length summary
abstract = summarizer.summarize(paper, max_words=250)
print(abstract)

Meeting Notes Summary
summarizer = TextSummarizer()

notes = """
Meeting started at 2pm. John presented Q3 results showing 15% growth.
Sarah raised concerns about supply chain delays affecting Q4 projections.
The team discussed mitigation strategies including dual-sourcing.
Budget allocation for marketing was approved at $50k.
Next steps include vendor outreach by Friday.
Follow-up meeting scheduled for next Tuesday.
"""

summary = summarizer.summarize(notes, num_sentences=3)
points = summarizer.extract_key_points(notes, num_points=4)

print("Summary:", summary)
print("\nAction Items:")
for point in points:
    print(f"• {point}")

Batch Document Summarization
summarizer = TextSummarizer()

import os
for filename in os.listdir("./documents"):
    if filename.endswith(".txt"):
        text = open(f"./documents/{filename}").read()
        summary = summarizer.summarize(text, ratio=0.2)

        with open(f"./summaries/{filename}", "w") as f:
            f.write(summary)

        print(f"Summarized: {filename}")

Algorithm Comparison
Algorithm	Speed	Quality	Best For
TextRank	Medium	High	General text
LSA	Fast	Good	Technical docs
Frequency	Fast	Medium	Quick summaries
Dependencies
nltk>=3.8.0
numpy>=1.24.0
scikit-learn>=1.2.0

Limitations
Extractive only (doesn't paraphrase or generate new text)
Works best with well-structured text (paragraphs, clear sentences)
Very short texts may not summarize well
Doesn't understand context deeply (may miss nuance)
Weekly Installs
699
Repository
dkyazzentwatwa/…t-skills
GitHub Stars
53
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass