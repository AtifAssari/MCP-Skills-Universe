---
title: analyzing-malicious-pdf-with-peepdf
url: https://skills.sh/mukul975/anthropic-cybersecurity-skills/analyzing-malicious-pdf-with-peepdf
---

# analyzing-malicious-pdf-with-peepdf

skills/mukul975/anthropic-cybersecurity-skills/analyzing-malicious-pdf-with-peepdf
analyzing-malicious-pdf-with-peepdf
Installation
$ npx skills add https://github.com/mukul975/anthropic-cybersecurity-skills --skill analyzing-malicious-pdf-with-peepdf
SKILL.md
Analyzing Malicious PDF with peepdf
When to Use
When triaging suspicious PDF attachments from phishing emails
During malware analysis of PDF-based exploit documents
When extracting embedded JavaScript, shellcode, or executables from PDFs
For forensic examination of weaponized document artifacts
When building detection signatures for PDF-based threats
Prerequisites
Python 3.8+ with peepdf-3 installed (pip install peepdf-3)
pdfid.py and pdf-parser.py from Didier Stevens suite
Isolated analysis environment (VM or sandbox)
Optional: PyV8 for JavaScript emulation within peepdf
Optional: Pylibemu for shellcode analysis
Workflow
Triage with pdfid: Scan PDF for suspicious keywords (/JS, /JavaScript, /OpenAction, /Launch, /EmbeddedFile).
Interactive Analysis: Open PDF in peepdf interactive mode to explore object structure.
Identify Suspicious Objects: Locate objects containing JavaScript, streams, or encoded data.
Extract Content: Dump suspicious streams and decode filters (FlateDecode, ASCIIHexDecode).
Deobfuscate JavaScript: Analyze extracted JS for shellcode, heap sprays, or exploit code.
Check VirusTotal: Use peepdf vtcheck to cross-reference file hash with AV detections.
Generate IOCs: Extract URLs, domains, hashes, and shellcode signatures.
Key Concepts
Concept	Description
/OpenAction	Automatic action executed when PDF is opened
/JavaScript /JS	Embedded JavaScript code in PDF objects
/Launch	Action that launches external applications
/EmbeddedFile	File embedded within the PDF structure
FlateDecode	zlib compression filter used to hide content
Object Streams	PDF objects stored in compressed streams
Tools & Systems
Tool	Purpose
peepdf / peepdf-3	Interactive PDF analysis with JS emulation
pdfid.py	Quick triage scanning for suspicious keywords
pdf-parser.py	Deep object-level PDF parsing
VirusTotal	Hash lookup and AV detection cross-reference
CyberChef	Decode and transform extracted payloads
Output Format
Analysis Report: PDF-MAL-[DATE]-[SEQ]
File: [filename.pdf]
SHA-256: [hash]
Suspicious Keywords: [/JS, /OpenAction, etc.]
Objects with JavaScript: [Object IDs]
Extracted URLs: [List]
Shellcode Detected: [Yes/No]
Embedded Files: [Count and types]
VirusTotal Detections: [X/Y engines]
Risk Level: [Critical/High/Medium/Low]

Weekly Installs
47
Repository
mukul975/anthro…y-skills
GitHub Stars
5.9K
First Seen
Mar 15, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass