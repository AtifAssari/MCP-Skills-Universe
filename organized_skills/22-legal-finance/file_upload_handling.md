---
rating: ⭐⭐⭐
title: file-upload-handling
url: https://skills.sh/aj-geddes/useful-ai-prompts/file-upload-handling
---

# file-upload-handling

skills/aj-geddes/useful-ai-prompts/file-upload-handling
file-upload-handling
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill file-upload-handling
SKILL.md
File Upload Handling
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Build secure and robust file upload systems with validation, sanitization, virus scanning, efficient storage management, CDN integration, and proper file serving mechanisms across different backend frameworks.

When to Use
Implementing file upload features
Managing user-uploaded documents
Storing and serving media files
Implementing profile picture uploads
Building document management systems
Handling bulk file imports
Quick Start

Minimal working example:

# config.py
import os

class Config:
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 50 MB
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'docx', 'doc'}
    UPLOAD_DIRECTORY = os.path.join(os.path.dirname(__file__), UPLOAD_FOLDER)

# file_service.py
import os
import mimetypes
import hashlib
import secrets
from werkzeug.utils import secure_filename
from datetime import datetime
import magic
import aiofiles

class FileUploadService:
    def __init__(self, upload_dir, allowed_extensions, max_size=50*1024*1024):
        self.upload_dir = upload_dir
        self.allowed_extensions = allowed_extensions
        self.max_size = max_size
        self.mime = magic.Magic(mime=True)
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Python/Flask File Upload	Python/Flask File Upload
Node.js Express File Upload with Multer	Node.js Express File Upload with Multer
FastAPI File Upload	FastAPI File Upload
S3/Cloud Storage Integration	S3/Cloud Storage Integration
Best Practices
✅ DO
Validate file extensions and MIME types
Check file size before processing
Use secure filenames to prevent directory traversal
Store files outside web root
Implement virus scanning
Use CDN for file delivery
Generate signed URLs for direct access
Log file upload/download events
Implement access control checks
Clean up temporary files
❌ DON'T
Trust user-provided filenames
Store files in web-accessible directories
Allow arbitrary file types
Skip virus scanning for uploaded files
Expose absolute file paths
Allow unlimited file sizes
Ignore access control
Use predictable file paths
Store sensitive metadata in filenames
Forget to validate file content
Weekly Installs
294
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass