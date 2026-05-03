---
title: update-markdown-file-index
url: https://skills.sh/github/awesome-copilot/update-markdown-file-index
---

# update-markdown-file-index

skills/github/awesome-copilot/update-markdown-file-index
update-markdown-file-index
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill update-markdown-file-index
Summary

Generate and maintain file indexes in markdown documents by scanning folders and updating or creating organized file listings.

Scans target markdown files and discovers files matching specified patterns in designated folders
Generates three table format options: simple lists with descriptions, detailed tables with type/size metadata, or categorized sections grouped by file type
Automatically identifies existing index sections by heading patterns ("index", "files", "contents") and updates them while preserving document structure
Extracts file metadata including name, type, description from comments or headers, size, and modification date for comprehensive indexing
Uses relative paths for all file links and sorts results alphabetically by default
SKILL.md
Update Markdown File Index

Update markdown file ${file} with an index/table of files from folder ${input:folder}.

Process
Scan: Read the target markdown file ${file} to understand existing structure
Discover: List all files in the specified folder ${input:folder} matching pattern ${input:pattern}
Analyze: Identify if an existing table/index section exists to update, or create new structure
Structure: Generate appropriate table/list format based on file types and existing content
Update: Replace existing section or add new section with file index
Validate: Ensure markdown syntax is valid and formatting is consistent
File Analysis

For each discovered file, extract:

Name: Filename with or without extension based on context
Type: File extension and category (e.g., .md, .js, .py)
Description: First line comment, header, or inferred purpose
Size: File size for reference (optional)
Modified: Last modified date (optional)
Table Structure Options

Choose format based on file types and existing content:

Option 1: Simple List
## Files in ${folder}

- [filename.ext](path/to/filename.ext) - Description
- [filename2.ext](path/to/filename2.ext) - Description

Option 2: Detailed Table
File	Type	Description
filename.ext	Extension	Description
filename2.ext	Extension	Description
Option 3: Categorized Sections

Group files by type/category with separate sections or sub-tables.

Update Strategy
🔄 Update existing: If table/index section exists, replace content while preserving structure
➕ Add new: If no existing section, create new section using best-fit format
📋 Preserve: Maintain existing markdown formatting, heading levels, and document flow
🔗 Links: Use relative paths for file links within the repository
Section Identification

Look for existing sections with these patterns:

Headings containing: "index", "files", "contents", "directory", "list"
Tables with file-related columns
Lists with file links
HTML comments marking file index sections
Requirements
Preserve existing markdown structure and formatting
Use relative paths for file links
Include file descriptions when available
Sort files alphabetically by default
Handle special characters in filenames
Validate all generated markdown syntax
Weekly Installs
8.4K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass