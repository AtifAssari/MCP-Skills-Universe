---
title: pdf processing pro
url: https://skills.sh/davila7/claude-code-templates/pdf-processing-pro
---

# pdf processing pro

skills/davila7/claude-code-templates/PDF Processing Pro
PDF Processing Pro
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill 'PDF Processing Pro'
Summary

Production-ready PDF processing with forms, tables, OCR, and batch operations.

Includes 10+ pre-built CLI scripts for form analysis, filling, table extraction, text extraction, PDF merging, splitting, and validation
All scripts feature comprehensive error handling with exit codes, input validation, type hints, and configurable logging for automation integration
Supports complex workflows: form field detection and filling with validation, multi-page table extraction to CSV/Excel, and OCR processing for scanned documents
Batch processing capabilities with performance optimization tips including parallel processing, streaming for large PDFs, and early validation to fail fast
SKILL.md
PDF Processing Pro

Production-ready PDF processing toolkit with pre-built scripts, comprehensive error handling, and support for complex workflows.

Quick start
Extract text from PDF
import pdfplumber

with pdfplumber.open("document.pdf") as pdf:
    text = pdf.pages[0].extract_text()
    print(text)

Analyze PDF form (using included script)
python scripts/analyze_form.py input.pdf --output fields.json
# Returns: JSON with all form fields, types, and positions

Fill PDF form with validation
python scripts/fill_form.py input.pdf data.json output.pdf
# Validates all fields before filling, includes error reporting

Extract tables from PDF
python scripts/extract_tables.py report.pdf --output tables.csv
# Extracts all tables with automatic column detection

Features
✅ Production-ready scripts

All scripts include:

Error handling: Graceful failures with detailed error messages
Validation: Input validation and type checking
Logging: Configurable logging with timestamps
Type hints: Full type annotations for IDE support
CLI interface: --help flag for all scripts
Exit codes: Proper exit codes for automation
✅ Comprehensive workflows
PDF Forms: Complete form processing pipeline
Table Extraction: Advanced table detection and extraction
OCR Processing: Scanned PDF text extraction
Batch Operations: Process multiple PDFs efficiently
Validation: Pre and post-processing validation
Advanced topics
PDF Form Processing

For complete form workflows including:

Field analysis and detection
Dynamic form filling
Validation rules
Multi-page forms
Checkbox and radio button handling

See FORMS.md

Table Extraction

For complex table extraction:

Multi-page tables
Merged cells
Nested tables
Custom table detection
Export to CSV/Excel

See TABLES.md

OCR Processing

For scanned PDFs and image-based documents:

Tesseract integration
Language support
Image preprocessing
Confidence scoring
Batch OCR

See OCR.md

Included scripts
Form processing

analyze_form.py - Extract form field information

python scripts/analyze_form.py input.pdf [--output fields.json] [--verbose]


fill_form.py - Fill PDF forms with data

python scripts/fill_form.py input.pdf data.json output.pdf [--validate]


validate_form.py - Validate form data before filling

python scripts/validate_form.py data.json schema.json

Table extraction

extract_tables.py - Extract tables to CSV/Excel

python scripts/extract_tables.py input.pdf [--output tables.csv] [--format csv|excel]

Text extraction

extract_text.py - Extract text with formatting preservation

python scripts/extract_text.py input.pdf [--output text.txt] [--preserve-formatting]

Utilities

merge_pdfs.py - Merge multiple PDFs

python scripts/merge_pdfs.py file1.pdf file2.pdf file3.pdf --output merged.pdf


split_pdf.py - Split PDF into individual pages

python scripts/split_pdf.py input.pdf --output-dir pages/


validate_pdf.py - Validate PDF integrity

python scripts/validate_pdf.py input.pdf

Common workflows
Workflow 1: Process form submissions
# 1. Analyze form structure
python scripts/analyze_form.py template.pdf --output schema.json

# 2. Validate submission data
python scripts/validate_form.py submission.json schema.json

# 3. Fill form
python scripts/fill_form.py template.pdf submission.json completed.pdf

# 4. Validate output
python scripts/validate_pdf.py completed.pdf

Workflow 2: Extract data from reports
# 1. Extract tables
python scripts/extract_tables.py monthly_report.pdf --output data.csv

# 2. Extract text for analysis
python scripts/extract_text.py monthly_report.pdf --output report.txt

Workflow 3: Batch processing
import glob
from pathlib import Path
import subprocess

# Process all PDFs in directory
for pdf_file in glob.glob("invoices/*.pdf"):
    output_file = Path("processed") / Path(pdf_file).name

    result = subprocess.run([
        "python", "scripts/extract_text.py",
        pdf_file,
        "--output", str(output_file)
    ], capture_output=True)

    if result.returncode == 0:
        print(f"✓ Processed: {pdf_file}")
    else:
        print(f"✗ Failed: {pdf_file} - {result.stderr}")

Error handling

All scripts follow consistent error patterns:

# Exit codes
# 0 - Success
# 1 - File not found
# 2 - Invalid input
# 3 - Processing error
# 4 - Validation error

# Example usage in automation
result = subprocess.run(["python", "scripts/fill_form.py", ...])

if result.returncode == 0:
    print("Success")
elif result.returncode == 4:
    print("Validation failed - check input data")
else:
    print(f"Error occurred: {result.returncode}")

Dependencies

All scripts require:

pip install pdfplumber pypdf pillow pytesseract pandas


Optional for OCR:

# Install tesseract-ocr system package
# macOS: brew install tesseract
# Ubuntu: apt-get install tesseract-ocr
# Windows: Download from GitHub releases

Performance tips
Use batch processing for multiple PDFs
Enable multiprocessing with --parallel flag (where supported)
Cache extracted data to avoid re-processing
Validate inputs early to fail fast
Use streaming for large PDFs (>50MB)
Best practices
Always validate inputs before processing
Use try-except in custom scripts
Log all operations for debugging
Test with sample PDFs before production
Set timeouts for long-running operations
Check exit codes in automation
Backup originals before modification
Troubleshooting
Common issues

"Module not found" errors:

pip install -r requirements.txt


Tesseract not found:

# Install tesseract system package (see Dependencies)


Memory errors with large PDFs:

# Process page by page instead of loading entire PDF
with pdfplumber.open("large.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        # Process page immediately


Permission errors:

chmod +x scripts/*.py

Getting help

All scripts support --help:

python scripts/analyze_form.py --help
python scripts/extract_tables.py --help


For detailed documentation on specific topics, see:

FORMS.md - Complete form processing guide
TABLES.md - Advanced table extraction
OCR.md - Scanned PDF processing
Weekly Installs
–
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass