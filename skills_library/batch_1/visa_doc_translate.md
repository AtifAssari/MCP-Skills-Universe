---
title: visa-doc-translate
url: https://skills.sh/affaan-m/everything-claude-code/visa-doc-translate
---

# visa-doc-translate

skills/affaan-m/everything-claude-code/visa-doc-translate
visa-doc-translate
Installation
$ npx skills add https://github.com/affaan-m/everything-claude-code --skill visa-doc-translate
Summary

Translate visa application documents to English and generate bilingual PDFs automatically.

Handles multiple document types: bank certificates, employment letters, retirement certificates, property documents, IDs, and passports
Automatically converts HEIC to PNG, detects and corrects image orientation via EXIF data, and extracts text using macOS Vision, EasyOCR, or Tesseract OCR
Translates extracted text professionally while preserving structure, proper names, dates, and amounts; uses pinyin for Chinese names
Generates a two-page PDF with the original image on page 1 and formatted English translation on page 2, suitable for official visa submissions
SKILL.md

You are helping translate visa application documents for visa applications.

Instructions

When the user provides an image file path, AUTOMATICALLY execute the following steps WITHOUT asking for confirmation:

Image Conversion: If the file is HEIC, convert it to PNG using sips -s format png <input> --out <output>

Image Rotation:

Check EXIF orientation data
Automatically rotate the image based on EXIF data
If EXIF orientation is 6, rotate 90 degrees counterclockwise
Apply additional rotation as needed (test 180 degrees if document appears upside down)

OCR Text Extraction:

Try multiple OCR methods automatically:
macOS Vision framework (preferred for macOS)
EasyOCR (cross-platform, no tesseract required)
Tesseract OCR (if available)
Extract all text information from the document
Identify document type (deposit certificate, employment certificate, retirement certificate, etc.)

Translation:

Translate all text content to English professionally
Maintain the original document structure and format
Use professional terminology appropriate for visa applications
Keep proper names in original language with English in parentheses
For Chinese names, use pinyin format (e.g., WU Zhengye)
Preserve all numbers, dates, and amounts accurately

PDF Generation:

Create a Python script using PIL and reportlab libraries
Page 1: Display the rotated original image, centered and scaled to fit A4 page
Page 2: Display the English translation with proper formatting:
Title centered and bold
Content left-aligned with appropriate spacing
Professional layout suitable for official documents
Add a note at the bottom: "This is a certified English translation of the original document"
Execute the script to generate the PDF

Output: Create a PDF file named <original_filename>_Translated.pdf in the same directory

Supported Documents
Bank deposit certificates (存款证明)
Income certificates (收入证明)
Employment certificates (在职证明)
Retirement certificates (退休证明)
Property certificates (房产证明)
Business licenses (营业执照)
ID cards and passports
Other official documents
Technical Implementation
OCR Methods (tried in order)

macOS Vision Framework (macOS only):

import Vision
from Foundation import NSURL


EasyOCR (cross-platform):

pip install easyocr


Tesseract OCR (if available):

brew install tesseract tesseract-lang
pip install pytesseract

Required Python Libraries
pip install pillow reportlab


For macOS Vision framework:

pip install pyobjc-framework-Vision pyobjc-framework-Quartz

Important Guidelines
DO NOT ask for user confirmation at each step
Automatically determine the best rotation angle
Try multiple OCR methods if one fails
Ensure all numbers, dates, and amounts are accurately translated
Use clean, professional formatting
Complete the entire process and report the final PDF location
Example Usage
/visa-doc-translate RetirementCertificate.PNG
/visa-doc-translate BankStatement.HEIC
/visa-doc-translate EmploymentLetter.jpg

Output Example

The skill will:

Extract text using available OCR method
Translate to professional English
Generate <filename>_Translated.pdf with:
Page 1: Original document image
Page 2: Professional English translation

Perfect for visa applications to Australia, USA, Canada, UK, and other countries requiring translated documents.

Weekly Installs
2.7K
Repository
affaan-m/everyt…ude-code
GitHub Stars
171.6K
First Seen
Today
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass