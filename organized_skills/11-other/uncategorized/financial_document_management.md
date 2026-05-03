---
rating: ⭐⭐⭐
title: financial-document-management
url: https://skills.sh/qodex-ai/ai-agent-skills/financial-document-management
---

# financial-document-management

skills/qodex-ai/ai-agent-skills/financial-document-management
financial-document-management
Installation
$ npx skills add https://github.com/qodex-ai/ai-agent-skills --skill financial-document-management
SKILL.md
Invoice Organizer

This skill transforms chaotic folders of invoices, receipts, and financial documents into a clean, tax-ready filing system without manual effort.

When to Use This Skill
Preparing for tax season and need organized records
Managing business expenses across multiple vendors
Organizing receipts from a messy folder or email downloads
Setting up automated invoice filing for ongoing bookkeeping
Archiving financial records by year or category
Reconciling expenses for reimbursement
Preparing documentation for accountants
What This Skill Does

Reads Invoice Content: Extracts information from PDFs, images, and documents:

Vendor/company name
Invoice number
Date
Amount
Product or service description
Payment method

Renames Files Consistently: Creates standardized filenames:

Format: YYYY-MM-DD Vendor - Invoice - ProductOrService.pdf
Examples: 2024-03-15 Adobe - Invoice - Creative Cloud.pdf

Organizes by Category: Sorts into logical folders:

By vendor
By expense category (software, office, travel, etc.)
By time period (year, quarter, month)
By tax category (deductible, personal, etc.)

Handles Multiple Formats: Works with:

PDF invoices
Scanned receipts (JPG, PNG)
Email attachments
Screenshots
Bank statements

Maintains Originals: Preserves original files while organizing copies

How to Use
Basic Usage

Navigate to your messy invoice folder:

cd ~/Desktop/receipts-to-sort


Then ask Claude Code:

Organize these invoices for taxes


Or more specifically:

Read all invoices in this folder, rename them to 
"YYYY-MM-DD Vendor - Invoice - Product.pdf" format, 
and organize them by vendor

Advanced Organization
Organize these invoices:
1. Extract date, vendor, and description from each file
2. Rename to standard format
3. Sort into folders by expense category (Software, Office, Travel, etc.)
4. Create a CSV spreadsheet with all invoice details for my accountant

Instructions

When a user requests invoice organization:

Scan the Folder

Identify all invoice files:

# Find all invoice-related files
find . -type f \( -name "*.pdf" -o -name "*.jpg" -o -name "*.png" \) -print


Report findings:

Total number of files
File types
Date range (if discernible from names)
Current organization (or lack thereof)

Extract Information from Each File

For each invoice, extract:

From PDF invoices:

Use text extraction to read invoice content
Look for common patterns:
"Invoice Date:", "Date:", "Issued:"
"Invoice #:", "Invoice Number:"
Company name (usually at top)
"Amount Due:", "Total:", "Amount:"
"Description:", "Service:", "Product:"

From image receipts:

Read visible text from images
Identify vendor name (often at top)
Look for date (common formats)
Find total amount

Fallback for unclear files:

Use filename clues
Check file creation/modification date
Flag for manual review if critical info missing

Determine Organization Strategy

Ask user preference if not specified:

I found [X] invoices from [date range].

How would you like them organized?

1. **By Vendor** (Adobe/, Amazon/, Stripe/, etc.)
2. **By Category** (Software/, Office Supplies/, Travel/, etc.)
3. **By Date** (2024/Q1/, 2024/Q2/, etc.)
4. **By Tax Category** (Deductible/, Personal/, etc.)
5. **Custom** (describe your structure)

Or I can use a default structure: Year/Category/Vendor


Create Standardized Filename

For each invoice, create a filename following this pattern:

YYYY-MM-DD Vendor - Invoice - Description.ext


Examples:

2024-03-15 Adobe - Invoice - Creative Cloud.pdf
2024-01-10 Amazon - Receipt - Office Supplies.pdf
2023-12-01 Stripe - Invoice - Monthly Payment Processing.pdf

Filename Best Practices:

Remove special characters except hyphens
Capitalize vendor names properly
Keep descriptions concise but meaningful
Use consistent date format (YYYY-MM-DD) for sorting
Preserve original file extension

Execute Organization

Before moving files, show the plan:

# Organization Plan

## Proposed Structure


Invoices/ ├── 2023/ │ ├── Software/ │ │ ├── Adobe/ │ │ └── Microsoft/ │ ├── Services/ │ └── Office/ └── 2024/ ├── Software/ ├── Services/ └── Office/


## Sample Changes

Before: `invoice_adobe_march.pdf`
After: `2024-03-15 Adobe - Invoice - Creative Cloud.pdf`
Location: `Invoices/2024/Software/Adobe/`

Before: `IMG_2847.jpg`
After: `2024-02-10 Staples - Receipt - Office Supplies.jpg`
Location: `Invoices/2024/Office/Staples/`

Process [X] files? (yes/no)


After approval:

# Create folder structure
mkdir -p "Invoices/2024/Software/Adobe"

# Copy (don't move) to preserve originals
cp "original.pdf" "Invoices/2024/Software/Adobe/2024-03-15 Adobe - Invoice - Creative Cloud.pdf"

# Or move if user prefers
mv "original.pdf" "new/path/standardized-name.pdf"


Generate Summary Report

Create a CSV file with all invoice details:

Date,Vendor,Invoice Number,Description,Amount,Category,File Path
2024-03-15,Adobe,INV-12345,Creative Cloud,52.99,Software,Invoices/2024/Software/Adobe/2024-03-15 Adobe - Invoice - Creative Cloud.pdf
2024-03-10,Amazon,123-4567890-1234567,Office Supplies,127.45,Office,Invoices/2024/Office/Amazon/2024-03-10 Amazon - Receipt - Office Supplies.pdf
...


This CSV is useful for:

Importing into accounting software
Sharing with accountants
Expense tracking and reporting
Tax preparation

Provide Completion Summary

# Organization Complete! 📊

## Summary
- **Processed**: [X] invoices
- **Date range**: [earliest] to [latest]
- **Total amount**: $[sum] (if amounts extracted)
- **Vendors**: [Y] unique vendors

## New Structure


Invoices/ ├── 2024/ (45 files) │ ├── Software/ (23 files) │ ├── Services/ (12 files) │ └── Office/ (10 files) └── 2023/ (12 files)


## Files Created
- `/Invoices/` - Organized invoices
- `/Invoices/invoice-summary.csv` - Spreadsheet for accounting
- `/Invoices/originals/` - Original files (if copied)

## Files Needing Review
[List any files where information couldn't be extracted completely]

## Next Steps
1. Review the `invoice-summary.csv` file
2. Check files in "Needs Review" folder
3. Import CSV into your accounting software
4. Set up auto-organization for future invoices

Ready for tax season! 🎉

Examples
Example 1: Tax Preparation (From Martin Merschroth)

User: "I have a messy folder of invoices for taxes. Sort them and rename properly."

Process:

Scans folder: finds 147 PDFs and images
Reads each invoice to extract:
Date
Vendor name
Invoice number
Product/service description
Renames all files: YYYY-MM-DD Vendor - Invoice - Product.pdf
Organizes into: 2024/Software/, 2024/Travel/, etc.
Creates invoice-summary.csv for accountant
Result: Tax-ready organized invoices in minutes
Example 2: Monthly Expense Reconciliation

User: "Organize my business receipts from last month by category."

Output:

# March 2024 Receipts Organized

## By Category
- Software & Tools: $847.32 (12 invoices)
- Office Supplies: $234.18 (8 receipts)
- Travel & Meals: $1,456.90 (15 receipts)
- Professional Services: $2,500.00 (3 invoices)

Total: $5,038.40

All receipts renamed and filed in:
`Business-Receipts/2024/03-March/[Category]/`

CSV export: `march-2024-expenses.csv`

Example 3: Multi-Year Archive

User: "I have 3 years of random invoices. Organize them by year, then by vendor."

Output: Creates structure:

Invoices/
├── 2022/
│   ├── Adobe/
│   ├── Amazon/
│   └── ...
├── 2023/
│   ├── Adobe/
│   ├── Amazon/
│   └── ...
└── 2024/
    ├── Adobe/
    ├── Amazon/
    └── ...


Each file properly renamed with date and description.

Example 4: Email Downloads Cleanup

User: "I download invoices from Gmail. They're all named 'invoice.pdf', 'invoice(1).pdf', etc. Fix this mess."

Output:

Found 89 files all named "invoice*.pdf"

Reading each file to extract real information...

Renamed examples:
- invoice.pdf → 2024-03-15 Shopify - Invoice - Monthly Subscription.pdf
- invoice(1).pdf → 2024-03-14 Google - Invoice - Workspace.pdf
- invoice(2).pdf → 2024-03-10 Netlify - Invoice - Pro Plan.pdf

All files renamed and organized by vendor.

Common Organization Patterns
By Vendor (Simple)
Invoices/
├── Adobe/
├── Amazon/
├── Google/
└── Microsoft/

By Year and Category (Tax-Friendly)
Invoices/
├── 2023/
│   ├── Software/
│   ├── Hardware/
│   ├── Services/
│   └── Travel/
└── 2024/
    └── ...

By Quarter (Detailed Tracking)
Invoices/
├── 2024/
│   ├── Q1/
│   │   ├── Software/
│   │   ├── Office/
│   │   └── Travel/
│   └── Q2/
│       └── ...

By Tax Category (Accountant-Ready)
Invoices/
├── Deductible/
│   ├── Software/
│   ├── Office/
│   └── Professional-Services/
├── Partially-Deductible/
│   └── Meals-Travel/
└── Personal/

Automation Setup

For ongoing organization:

Create a script that watches my ~/Downloads/invoices folder 
and auto-organizes any new invoice files using our standard 
naming and folder structure.


This creates a persistent solution that organizes invoices as they arrive.

Pro Tips
Scan emails to PDF: Use Preview or similar to save email invoices as PDFs first
Consistent downloads: Save all invoices to one folder for batch processing
Monthly routine: Organize invoices monthly, not annually
Backup originals: Keep original files before reorganizing
Include amounts in CSV: Useful for budget tracking
Tag by deductibility: Note which expenses are tax-deductible
Keep receipts 7 years: Standard audit period
Handling Special Cases
Missing Information

If date/vendor can't be extracted:

Flag file for manual review
Use file modification date as fallback
Create "Needs-Review/" folder
Duplicate Invoices

If same invoice appears multiple times:

Compare file hashes
Keep highest quality version
Note duplicates in summary
Multi-Page Invoices

For invoices split across files:

Merge PDFs if needed
Use consistent naming for parts
Note in CSV if invoice is split
Non-Standard Formats

For unusual receipt formats:

Extract what's possible
Standardize what you can
Flag for review if critical info missing
Related Use Cases
Creating expense reports for reimbursement
Organizing bank statements
Managing vendor contracts
Archiving old financial records
Preparing for audits
Tracking subscription costs over time
Weekly Installs
92
Repository
qodex-ai/ai-agent-skills
GitHub Stars
6
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass