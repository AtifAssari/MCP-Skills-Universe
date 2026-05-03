---
rating: ⭐⭐⭐
title: large-document-processing
url: https://skills.sh/findinfinitelabs/chuuk/large-document-processing
---

# large-document-processing

skills/findinfinitelabs/chuuk/large-document-processing
large-document-processing
Installation
$ npx skills add https://github.com/findinfinitelabs/chuuk --skill large-document-processing
SKILL.md
Large Document Processing & Intelligent Text Chunking
Overview

Two tightly related concerns combined here:

Large document parsing — DOCX/PDF/EPUB ingestion with structure preservation
Intelligent text chunking — splitting parsed text into semantically coherent pieces for AI training or RAG
Source Files
File	Purpose
src/utils/nwt_epub_parser.py	EPUB parser for NWT Bible (English + Chuukese)
scripts/extract_jwpub.py	Extract JW publication .jwpub archives
scripts/setup_large_document_processing.py	One-time document pipeline setup
output/processed_document/	Output directory for processed content
Document Processing
Supported Formats
DOCX via python-docx
PDF via PyMuPDF (import as fitz) — note: fitz==0.0.1.dev2 is NOT in requirements; use PyMuPDF only
EPUB via ebooklib + NWTEpubParser
Plain text / CSV — direct read
EPUB Pattern (NWT Bible)
from src.utils.nwt_epub_parser import NWTEpubParser

parser = NWTEpubParser('data/bible/nwt_E.epub')
verse_text = parser.get_verse('John', 3, 16)
chapter_verses = parser.get_chapter('Genesis', 1)

PDF/DOCX Pattern
import fitz  # PyMuPDF — installed as PyMuPDF, exposed as fitz

doc = fitz.open('large_document.pdf')
for page_num, page in enumerate(doc):
    text = page.get_text()
    # process text...

Intelligent Text Chunking
Strategy Selection
Strategy	Use case
Semantic	AI training data — respect topic/paragraph boundaries
Structural	Documents with clear headings/sections
Fixed-size	RAG systems needing predictable chunk sizes
Sliding window	QA tasks needing context overlap
Implementation Pattern
# Sentence-boundary-aware chunking
def chunk_text(text: str, max_chars: int = 1024, overlap: int = 100) -> list[str]:
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks, current = [], ''
    for sent in sentences:
        if len(current) + len(sent) > max_chars and current:
            chunks.append(current.strip())
            current = current[-overlap:] + ' ' + sent  # overlap
        else:
            current += ' ' + sent
    if current.strip():
        chunks.append(current.strip())
    return chunks

Chuukese-aware chunking
# Chuukese uses the same sentence terminators as English
SENTENCE_ENDINGS = re.compile(r'(?<=[.!?])\s+')

def detect_language(text: str) -> str:
    has_accents = bool(re.search(r'[áéíóú]', text))
    return 'chuukese' if has_accents else 'english'

Memory Efficiency
Process large PDFs page-by-page, not loading the full DOM into memory
Stream EPUB chapters — do not load the entire book at once
Write chunk output incrementally to JSONL files rather than accumulating in RAM
Output Formats
JSONL: one JSON object per line — best for large training datasets
JSON array: for smaller batches consumed by the frontend
Plain text: cleaned extracted text for inspection
Dependencies
PyMuPDF==1.23.8 — PDF processing (do NOT add fitz==0.0.1.dev2)
python-docx>=1.2.0
ebooklib>=0.18
beautifulsoup4>=4.12.0
Weekly Installs
26
Repository
findinfinitelabs/chuuk
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass