---
title: stdf-reader
url: https://skills.sh/showjim/chao-skills/stdf-reader
---

# stdf-reader

skills/showjim/chao-skills/stdf-reader
stdf-reader
Installation
$ npx skills add https://github.com/showjim/chao-skills --skill stdf-reader
SKILL.md
STDF Reader Skill

This skill provides access to the STDF Reader CLI tool for parsing and analyzing semiconductor STDF test data files.

Prerequisites

Install via pip (python version 3.9+):

pip install stdf-reader


Use the virtual environment for running any commands:

source .venv/bin/activate

Available Commands
1. Convert STDF to CSV (most common)

Parse one or more STDF files into a CSV log for analysis:

stdf-reader convert-csv <stdf_file(s)> [-o output_name]


Options:

--ignore-tnum — Ignore test number (match by name only)
--ignore-chnum — Ignore channel number in test name
--no-merge — Output separate CSV per file (default: merge into one)

Example:

stdf-reader convert-csv input.stdf
# Output: input.stdf_csv_log.csv

stdf-reader convert-csv lot1.stdf lot2.stdf -o merged_output
# Output: merged_output_csv_log.csv

2. Convert STDF to XLSX

Parse STDF file into a formatted Excel table (shows all record types):

stdf-reader convert-xlsx <stdf_file>

3. Convert Diagnosis STDF to ASCII

Convert STDF V4-2007.1 files with STR/PSR diagnosis records to ASCII CSV:

stdf-reader convert-diag <stdf_file>

4. Extract Single Record Type

Extract a specific STDF record type (DTR, GDR, TSR) to CSV:

stdf-reader extract-record <stdf_file> --type DTR

5. Generate Analysis Report

Generate comprehensive XLSX report from CSV (includes data statistics, bin summary, wafer map):

stdf-reader report <csv_file(s)> [-o output.xlsx]

6. Generate Correlation Report

Compare means across 2+ STDF files merged in a single CSV:

stdf-reader correlation <csv_file(s)> [-o output.xlsx]

7. Generate Site-to-Site Correlation

Compare test data across different test sites:

stdf-reader s2s <csv_file(s)> [-o output.xlsx] [--cherry-pick "1,3,5"]


Options:

--cherry-pick "1,3,5" — Site numbers to pick, comma-separated
8. Generate PDF Charts

Generate PDF with trendline + histogram charts for selected tests:

# By regex pattern
stdf-reader pdf <csv_file> --regex "IDD.*"

# All tests
stdf-reader pdf <csv_file> --all

# Specific tests
stdf-reader pdf <csv_file> --tests "210 - IDD_Static <> curr"


Options:

--no-limits — Don't plot failure limit lines
--group-by-file — Group trends by file instead of by site
9. Extract Sub-CSV

Extract only specific tests from a CSV file:

stdf-reader extract-tests <csv_file> --regex "VDD.*"

10. List Tests

List all test instances in a CSV file:

stdf-reader list-tests <csv_file>
stdf-reader list-tests <csv_file> --filter "IDD.*"

11. Transpose CSV

Swap rows and columns in a CSV file:

stdf-reader transpose <csv_file>

Typical Workflow
Convert STDF to CSV: convert-csv input.stdf
List available tests: list-tests input.stdf_csv_log.csv
Report: report input.stdf_csv_log.csv
PDF charts: pdf input.stdf_csv_log.csv --regex "pattern"
Output File Naming
convert-csv → {input}_csv_log.csv
convert-xlsx → {input}_excel.xlsx
convert-diag → {input}_diag_log.csv
extract-record → {input}_{TYPE}_Rec.csv
report → {base}_analysis_report_{timestamp}.xlsx
correlation → {base}_correlation_report_{timestamp}.xlsx
s2s → {base}_s2s_correlation_table{timestamp}.xlsx
pdf → {input}_results.pdf

All outputs default to the same directory as the input unless -o is specified.

Weekly Installs
13
Repository
showjim/chao-skills
GitHub Stars
1
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass