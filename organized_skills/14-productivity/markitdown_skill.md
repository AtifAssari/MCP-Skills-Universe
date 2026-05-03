---
rating: ⭐⭐⭐
title: markitdown-skill
url: https://skills.sh/julianobarbosa/claude-code-skills/markitdown-skill
---

# markitdown-skill

skills/julianobarbosa/claude-code-skills/markitdown-skill
markitdown-skill
Installation
$ npx skills add https://github.com/julianobarbosa/claude-code-skills --skill markitdown-skill
SKILL.md
MarkItDown Skill

Microsoft's Python utility for converting various file formats to Markdown for LLM and text analysis pipelines.

Overview

MarkItDown converts documents while preserving structure (headings, lists, tables, links). It's optimized for LLM consumption rather than human-readable output.

Supported Formats
Category	Formats
Documents	PDF, Word (DOCX), PowerPoint (PPTX), Excel (XLSX, XLS)
Media	Images (EXIF + OCR), Audio (WAV, MP3 transcription)
Web	HTML, YouTube URLs, Wikipedia, RSS/Atom feeds
Data	CSV, JSON, XML, Jupyter notebooks (.ipynb)
Archives	ZIP (iterates contents), EPub
Email	Outlook MSG files
Quick Start
Installation
# Full installation (recommended)
pip install 'markitdown[all]'

# Minimal with specific formats
pip install 'markitdown[pdf,docx,pptx]'

# Using uv
uv pip install 'markitdown[all]'

Optional Dependencies
Extra	Description
[all]	All optional dependencies
[pdf]	PDF file support
[docx]	Word documents
[pptx]	PowerPoint presentations
[xlsx]	Excel spreadsheets
[xls]	Legacy Excel files
[outlook]	Outlook MSG files
[az-doc-intel]	Azure Document Intelligence
[audio-transcription]	WAV/MP3 transcription
[youtube-transcription]	YouTube video transcripts
Command-Line Usage
# Basic conversion
markitdown document.pdf > output.md

# Specify output file
markitdown document.pdf -o output.md

# Pipe input
cat document.pdf | markitdown > output.md

# With Azure Document Intelligence
markitdown document.pdf -o output.md -d -e "<endpoint>"

Python API
from markitdown import MarkItDown

# Basic conversion
md = MarkItDown()
result = md.convert("document.xlsx")
print(result.text_content)

# With LLM for image descriptions
from openai import OpenAI

client = OpenAI()
md = MarkItDown(
    llm_client=client,
    llm_model="gpt-4o",
    llm_prompt="Describe this image in detail"
)
result = md.convert("image.jpg")
print(result.text_content)

# With Azure Document Intelligence
md = MarkItDown(docintel_endpoint="<your-endpoint>")
result = md.convert("complex-document.pdf")
print(result.text_content)

Common Use Cases
Batch Convert Directory
from markitdown import MarkItDown
from pathlib import Path

md = MarkItDown()
input_dir = Path("./documents")
output_dir = Path("./markdown")
output_dir.mkdir(exist_ok=True)

for file in input_dir.glob("*"):
    if file.is_file():
        try:
            result = md.convert(str(file))
            output_file = output_dir / f"{file.stem}.md"
            output_file.write_text(result.text_content)
            print(f"Converted: {file.name}")
        except Exception as e:
            print(f"Failed: {file.name} - {e}")

Process for LLM Context
from markitdown import MarkItDown

def prepare_for_llm(file_path: str) -> str:
    """Convert document to LLM-ready markdown."""
    md = MarkItDown()
    result = md.convert(file_path)

    # Add source reference
    content = f"# Source: {file_path}\n\n{result.text_content}"
    return content

# Use with your LLM
context = prepare_for_llm("report.pdf")

Extract YouTube Transcript
# CLI
markitdown "https://www.youtube.com/watch?v=VIDEO_ID" > transcript.md

# Python
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("https://www.youtube.com/watch?v=VIDEO_ID")
print(result.text_content)

Image OCR with AI Description
from markitdown import MarkItDown
from openai import OpenAI

# Initialize with LLM support
client = OpenAI()
md = MarkItDown(
    llm_client=client,
    llm_model="gpt-4o"
)

# Convert image with AI description
result = md.convert("screenshot.png")
print(result.text_content)

Convert Jupyter Notebook
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("analysis.ipynb")
print(result.text_content)  # Code cells, outputs, markdown

Extract Wikipedia Content
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("https://en.wikipedia.org/wiki/Python")
print(result.text_content)  # Main article content only

Parse RSS Feed
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("https://example.com/feed.xml")
print(result.text_content)  # Feed entries as markdown

Plugin System

MarkItDown supports third-party plugins for extended functionality.

# List installed plugins
markitdown --list-plugins

# Enable plugins during conversion
markitdown --use-plugins document.pdf

# Enable plugins in Python
md = MarkItDown(enable_plugins=True)
result = md.convert("document.pdf")


Search GitHub for #markitdown-plugin to find available plugins.

MCP Server Integration

MarkItDown offers an MCP (Model Context Protocol) server for integration with LLM applications like Claude Desktop.

# Install MCP server
pip install markitdown-mcp

# Or from source
git clone https://github.com/microsoft/markitdown.git
cd markitdown/packages/markitdown-mcp
pip install -e .


See markitdown-mcp for configuration details.

Docker Usage
# Build image
docker build -t markitdown:latest .

# Convert file
docker run --rm -i markitdown:latest < document.pdf > output.md

Troubleshooting
Issue	Solution
Missing dependencies	Install with pip install 'markitdown[all]'
PDF extraction fails	Try Azure Document Intelligence for complex PDFs
Image text not extracted	Ensure OCR dependencies installed or use LLM mode
Large file timeout	Process in chunks or use streaming
Plugin not found	Run markitdown --list-plugins to verify installation
Common Errors
# ModuleNotFoundError for specific format
pip install 'markitdown[pdf]'  # Install missing dependency

# Azure authentication
export AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT="<endpoint>"
export AZURE_DOCUMENT_INTELLIGENCE_KEY="<key>"

Requirements
Python >= 3.10
Virtual environment recommended
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

# Install
pip install 'markitdown[all]'

References
references/cli-reference.md - Complete CLI options
references/api-reference.md - Python API details
references/examples.md - Extended examples
references/advanced-features.md - Custom converters, URI handling
GitHub: https://github.com/microsoft/markitdown
PyPI: https://pypi.org/project/markitdown/
Weekly Installs
121
Repository
julianobarbosa/…e-skills
GitHub Stars
64
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn