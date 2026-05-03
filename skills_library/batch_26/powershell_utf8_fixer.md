---
title: powershell-utf8-fixer
url: https://skills.sh/mineru98/skills-store/powershell-utf8-fixer
---

# powershell-utf8-fixer

skills/mineru98/skills-store/powershell-utf8-fixer
powershell-utf8-fixer
Installation
$ npx skills add https://github.com/mineru98/skills-store --skill powershell-utf8-fixer
SKILL.md
PowerShell UTF-8 Fixer
Problem

PowerShell on Windows requires UTF-8 with BOM encoding for scripts containing non-ASCII characters (Korean, Chinese, Japanese, emoji, etc.). Without the BOM (Byte Order Mark), PowerShell interprets the file using the system's default encoding (typically CP949 on Korean Windows), causing character display issues.

Symptoms:

Korean text appears as ??? or garbled characters
Emoji and special characters don't display correctly
Write-Host output shows corrupted text
One script works fine while another with identical code shows garbled text

Root cause: File encoding mismatch

✓ UTF-8 with BOM (EF BB BF): PowerShell reads correctly
✗ UTF-8 without BOM: PowerShell uses system default encoding → garbled text
Quick Fix

When encountering encoding issues in PowerShell scripts:

Check encoding:
node scripts/check_powershell_encoding.js <file_or_directory>
# Or with npm:
npm run check <file_or_directory>

Fix encoding:
node scripts/fix_powershell_encoding.js <file_or_directory>
# Or with npm:
npm run fix <file_or_directory>

Workflow
When Creating New PowerShell Scripts

After creating any .ps1 file with non-ASCII characters:

node scripts/fix_powershell_encoding.js script.ps1


This ensures the file is saved with UTF-8 BOM from the start.

When Diagnosing Display Issues

If a PowerShell script shows garbled text:

Check the encoding:
node scripts/check_powershell_encoding.js problematic_script.ps1

If it shows "UTF-8 without BOM", fix it:
node scripts/fix_powershell_encoding.js problematic_script.ps1

Test the script again - text should now display correctly
Batch Processing

To check/fix all PowerShell scripts in a directory:

# Check all scripts
node scripts/check_powershell_encoding.js scripts/windows/

# Fix all scripts that need it
node scripts/fix_powershell_encoding.js scripts/windows/

Prevention

To prevent encoding issues in the future:

Before committing: Run the checker on modified .ps1 files
In CI/CD: Add encoding validation to your pipeline
Editor settings: Configure your editor to save .ps1 files as UTF-8 with BOM
Editor Configuration Examples

VS Code (settings.json):

{
  "[powershell]": {
    "files.encoding": "utf8bom"
  }
}


Cursor (settings.json):

{
  "[powershell]": {
    "files.encoding": "utf8bom"
  }
}

Scripts
check_powershell_encoding.js

Diagnoses encoding issues without modifying files.

Usage:

node scripts/check_powershell_encoding.js <file_or_directory>


Output:

✓ UTF-8 with BOM: File is correctly encoded
⚠ UTF-8 without BOM: File needs fixing
⚠ UTF-16: File uses UTF-16 encoding
✗ Unknown: Unable to detect encoding

Exit codes:

0: All files have UTF-8 BOM
1: Some files need fixing or have errors
fix_powershell_encoding.js

Adds UTF-8 BOM to PowerShell files that don't have it.

Usage:

node scripts/fix_powershell_encoding.js <file_or_directory>


Behavior:

Reads file content as UTF-8
Writes back with UTF-8 BOM (utf-8-sig)
Skips files that already have UTF-8 BOM
Processes .ps1 files recursively in directories

Exit codes:

0: All files processed successfully
1: Errors occurred during processing
Technical Details

UTF-8 BOM: The byte sequence EF BB BF at the start of a file signals UTF-8 encoding to PowerShell and other Windows applications.

Why PowerShell needs BOM:

Without BOM, PowerShell uses [Console]::OutputEncoding (often CP949/CP1252)
With BOM, PowerShell correctly identifies the file as UTF-8
This is specific to Windows PowerShell's file reading behavior

Alternative workarounds (not recommended):

Adding encoding commands to each script (verbose, error-prone)
Using -Encoding UTF8 parameters (doesn't help with file reading)
Avoiding non-ASCII characters (limits usability)

The proper solution is to save files with UTF-8 BOM.

Weekly Installs
29
Repository
mineru98/skills-store
GitHub Stars
4
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass