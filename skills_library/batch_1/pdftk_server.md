---
title: pdftk-server
url: https://skills.sh/github/awesome-copilot/pdftk-server
---

# pdftk-server

skills/github/awesome-copilot/pdftk-server
pdftk-server
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill pdftk-server
Summary

Command-line PDF manipulation covering merging, splitting, encryption, form filling, watermarking, and metadata extraction.

Supports 12+ operations including merge, split, rotate, encrypt/decrypt, burst, stamp, watermark, and repair
Fill PDF forms from FDF/XFDF data with optional flattening to lock filled fields
Extract and manipulate metadata, bookmarks, and embedded files; collate separately scanned pages
Cross-platform installation via package managers (Windows, macOS, Linux) with verification via pdftk --version
SKILL.md
PDFtk Server

PDFtk Server is a command-line tool for working with PDF documents. It can merge, split, rotate, encrypt, decrypt, watermark, stamp, fill forms, extract metadata, and manipulate PDFs in a variety of ways.

When to Use This Skill
Merging or joining multiple PDF files into one
Splitting or bursting a PDF into individual pages
Rotating PDF pages
Encrypting or decrypting PDF files
Filling PDF form fields from FDF/XFDF data
Applying background watermarks or foreground stamps
Extracting PDF metadata, bookmarks, or form field information
Repairing corrupted PDF files
Attaching or extracting files embedded in PDFs
Removing specific pages from a PDF
Collating separately scanned even/odd pages
Compressing or decompressing PDF page streams
Prerequisites
PDFtk Server must be installed on the system
Windows: winget install --id PDFLabs.PDFtk.Server
macOS: brew install pdftk-java
Linux (Debian/Ubuntu): sudo apt-get install pdftk
Linux (Red Hat/Fedora): sudo dnf install pdftk
Access to a terminal or command prompt
Verify installation by running pdftk --version
Step-by-Step Workflows
Merge Multiple PDFs
pdftk file1.pdf file2.pdf cat output merged.pdf


Using handles for more control:

pdftk A=file1.pdf B=file2.pdf cat A B output merged.pdf

Split a PDF into Individual Pages
pdftk input.pdf burst

Extract Specific Pages

Extract pages 1-5 and 10-15:

pdftk input.pdf cat 1-5 10-15 output extracted.pdf

Remove Specific Pages

Remove page 13:

pdftk input.pdf cat 1-12 14-end output output.pdf

Rotate Pages

Rotate all pages 90 degrees clockwise:

pdftk input.pdf cat 1-endeast output rotated.pdf

Encrypt a PDF

Set an owner password and a user password with 128-bit encryption (default):

pdftk input.pdf output secured.pdf owner_pw mypassword user_pw userpass

Decrypt a PDF

Remove encryption using the known password:

pdftk secured.pdf input_pw mypassword output unsecured.pdf

Fill a PDF Form

Populate form fields from an FDF file and flatten to prevent further edits:

pdftk form.pdf fill_form data.fdf output filled.pdf flatten

Apply a Background Watermark

Place a single-page PDF behind every page of the input (input should have transparency):

pdftk input.pdf background watermark.pdf output watermarked.pdf

Stamp an Overlay

Place a single-page PDF on top of every page of the input:

pdftk input.pdf stamp overlay.pdf output stamped.pdf

Extract Metadata

Export bookmarks, page metrics, and document information:

pdftk input.pdf dump_data output metadata.txt

Repair a Corrupted PDF

Pass a broken PDF through pdftk to attempt automatic repair:

pdftk broken.pdf output fixed.pdf

Collate Scanned Pages

Interleave separately scanned even and odd pages:

pdftk A=even.pdf B=odd.pdf shuffle A B output collated.pdf

Troubleshooting
Issue	Solution
pdftk command not found	Verify installation; check that pdftk is in your system PATH
Cannot decrypt PDF	Ensure you are providing the correct owner or user password via input_pw
Output file is empty or corrupt	Check input file integrity; try running pdftk input.pdf output repaired.pdf first
Form fields not visible after fill	Use the flatten flag to merge fields into the page content
Watermark not appearing	Ensure the input PDF has transparent regions; use stamp for opaque overlays
Permission denied errors	Check file permissions on input and output paths
References

Bundled reference documents in the references/ folder:

pdftk-man-page.md - Complete manual reference with all operations, options, and syntax
pdftk-cli-examples.md - Practical command-line examples for common tasks
download.md - Installation and download instructions for all platforms
pdftk-server-license.md - PDFtk Server licensing information
third-party-materials.md - Third-party library licenses
Weekly Installs
8.6K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykFail