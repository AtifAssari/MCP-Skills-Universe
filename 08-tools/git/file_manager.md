---
title: file-manager
url: https://skills.sh/ninehills/skills/file-manager
---

# file-manager

skills/ninehills/skills/file-manager
file-manager
Installation
$ npx skills add https://github.com/ninehills/skills --skill file-manager
SKILL.md
File Manager Skill

Help users find and organize files on their computer.

Find Files
# By name (case-insensitive)
find ~/Desktop ~/Documents ~/Downloads -iname "*report*" -type f 2>/dev/null

# By extension
find ~/Downloads -name "*.pdf" -type f

# By size (larger than 100MB)
find ~ -size +100M -type f 2>/dev/null | head -20

# Recently modified (last 7 days)
find ~/Documents -mtime -7 -type f | head -20

# Duplicates by size (potential dupes)
find ~/Downloads -type f -exec ls -la {} + | sort -k5 -n | uniq -d -f4

Organize
# Move all PDFs from Downloads to Documents
mv ~/Downloads/*.pdf ~/Documents/

# Create dated folder and move files
mkdir -p ~/Documents/$(date +%Y-%m-%d)

# Rename files (pattern)
for f in *.jpeg; do mv "$f" "${f%.jpeg}.jpg"; done

Cleanup
# Show large files in Downloads
du -sh ~/Downloads/* | sort -rh | head -20

# Empty trash (macOS)
rm -rf ~/.Trash/*

# Clear old downloads (older than 30 days)
find ~/Downloads -mtime +30 -type f

Compress/Extract
# Create zip
zip -r archive.zip folder/

# Create tar.gz
tar czf archive.tar.gz folder/

# Extract
unzip archive.zip
tar xzf archive.tar.gz

Tips
Always use trash over rm when available (recoverable)
Preview file lists before bulk operations
Ask before deleting — show what would be affected first
Weekly Installs
125
Repository
ninehills/skills
GitHub Stars
267
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass