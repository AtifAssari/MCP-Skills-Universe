---
title: pdf-best-practices
url: https://skills.sh/pdfnoodle/pdf-best-practices/pdf-best-practices
---

# pdf-best-practices

skills/pdfnoodle/pdf-best-practices/pdf-best-practices
pdf-best-practices
Installation
$ npx skills add https://github.com/pdfnoodle/pdf-best-practices --skill pdf-best-practices
SKILL.md
PDF Best Practices Skill

Comprehensive guidelines for creating HTML that renders perfectly as PDF documents.

┌─────────────────────────────────────────────────────────────────────────────┐
│                         HTML to PDF Pipeline                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌──────────┐    ┌──────────────┐    ┌─────────────┐    ┌──────────────┐  │
│   │  HTML    │───▶│  PDF Engine  │───▶│  Pagination │───▶│  Final PDF   │  │
│   │ Content  │    │  (Puppeteer) │    │  & Layout   │    │  Document    │  │
│   └──────────┘    └──────────────┘    └─────────────┘    └──────────────┘  │
│        │                                     │                              │
│        ▼                                     ▼                              │
│   ┌──────────┐                        ┌─────────────┐                       │
│   │  CSS     │                        │ Page Breaks │                       │
│   │  Styles  │                        │  & Margins  │                       │
│   └──────────┘                        └─────────────┘                       │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘

Quick Reference
I want to...	Read this
Set up document structure correctly	Document Setup
Control page breaks	Page Breaks
Format tables for PDF	Tables
Handle images properly	Images
Optimize content density	Content Density
Set up colors and backgrounds	Colors & Backgrounds
Add headers, footers, page numbers	Headers & Footers
Create specific document types	Document Types
Start Here
Building a new PDF document?
Start with Document Setup for the HTML structure
Review Page Breaks to prevent awkward splits
Check Content Density to avoid sparse pages
Working with data tables?
Read Tables for formatting and header repetition
Apply Page Breaks to prevent row splitting
Document has images?
Follow Images for sizing and positioning
Use Page Breaks to keep images with captions
Creating a specific document type?
Check Document Types for type-specific guidelines
Available types: Invoice, Report, Certificate, Letter, Table-heavy, Image-heavy
Default Configuration

When generating PDFs, use these recommended parameters:

{
  "format": "A4",
  "margin": {
    "top": "40px",
    "right": "40px",
    "bottom": "40px",
    "left": "40px"
  },
  "printBackground": true
}

Quick Checklist

Before generating any PDF:

 Complete HTML structure with DOCTYPE, html, head, body
 CSS includes @page rule with A4 size
 Body has -webkit-print-color-adjust: exact
 All images have explicit width/height
 Tables use thead/tbody structure
 page-break-inside: avoid on logical content blocks
 Headings have page-break-after: avoid
 No excessive whitespace or sparse pages
 Font sizes are 9pt or larger
 Colors have sufficient contrast
 pdfParams includes format, margins, and printBackground: true
Weekly Installs
78
Repository
pdfnoodle/pdf-b…ractices
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass