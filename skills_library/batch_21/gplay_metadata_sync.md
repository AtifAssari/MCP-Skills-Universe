---
title: gplay-metadata-sync
url: https://skills.sh/tamtom/gplay-cli-skills/gplay-metadata-sync
---

# gplay-metadata-sync

skills/tamtom/gplay-cli-skills/gplay-metadata-sync
gplay-metadata-sync
Installation
$ npx skills add https://github.com/tamtom/gplay-cli-skills --skill gplay-metadata-sync
SKILL.md
Metadata Sync for Google Play

Use this skill when you need to update or sync Play Store metadata and localizations.

Fastlane Directory Structure
fastlane/metadata/android/
├── en-US/
│   ├── title.txt
│   ├── short_description.txt
│   ├── full_description.txt
│   ├── video.txt
│   └── images/
│       ├── phoneScreenshots/
│       │   ├── 1.png
│       │   └── 2.png
│       ├── sevenInchScreenshots/
│       ├── tenInchScreenshots/
│       ├── tvScreenshots/
│       ├── wearScreenshots/
│       ├── icon.png
│       └── featureGraphic.png
├── es-ES/
│   ├── title.txt
│   └── ...
└── fr-FR/
    └── ...

Export Metadata from Play Store
# Export all listings to Fastlane format
gplay sync export-listings \
  --package com.example.app \
  --dir ./fastlane/metadata/android

# Export images
gplay sync export-images \
  --package com.example.app \
  --dir ./fastlane/metadata/android

Import Metadata to Play Store
# Validate before importing (offline check)
gplay validate listing \
  --dir ./fastlane/metadata/android \
  --locale en-US

# Import all listings
gplay sync import-listings \
  --package com.example.app \
  --dir ./fastlane/metadata/android

# Import images
gplay sync import-images \
  --package com.example.app \
  --dir ./fastlane/metadata/android

Compare Local vs Remote
# See what would change
gplay sync diff-listings \
  --package com.example.app \
  --dir ./fastlane/metadata/android

Manual Metadata Management
List all listings
gplay listings list \
  --package com.example.app \
  --edit $EDIT_ID

Get specific locale
gplay listings get \
  --package com.example.app \
  --edit $EDIT_ID \
  --locale en-US

Update listing
gplay listings update \
  --package com.example.app \
  --edit $EDIT_ID \
  --locale en-US \
  --json @listing.json

listing.json format
{
  "title": "My Awesome App",
  "shortDescription": "A short description under 80 characters",
  "fullDescription": "A full description under 4000 characters...",
  "video": "https://www.youtube.com/watch?v=VIDEO_ID"
}

Image Management
Upload screenshots
gplay images upload \
  --package com.example.app \
  --edit $EDIT_ID \
  --locale en-US \
  --type phoneScreenshots \
  --file screenshot1.png

gplay images upload \
  --package com.example.app \
  --edit $EDIT_ID \
  --locale en-US \
  --type phoneScreenshots \
  --file screenshot2.png

Image types
phoneScreenshots - Phone screenshots (required)
sevenInchScreenshots - 7" tablet screenshots
tenInchScreenshots - 10" tablet screenshots
tvScreenshots - TV screenshots
wearScreenshots - Wear OS screenshots
icon - App icon
featureGraphic - Feature graphic (1024x500)
List images
gplay images list \
  --package com.example.app \
  --edit $EDIT_ID \
  --locale en-US \
  --type phoneScreenshots

Delete image
gplay images delete \
  --package com.example.app \
  --edit $EDIT_ID \
  --locale en-US \
  --type phoneScreenshots \
  --image-id IMAGE_ID \
  --confirm

App Details
Get app details
gplay details get \
  --package com.example.app \
  --edit $EDIT_ID

Update contact info
gplay details update \
  --package com.example.app \
  --edit $EDIT_ID \
  --contact-email support@example.com \
  --contact-phone "+1234567890" \
  --contact-website "https://example.com"

Character Limits

Validate against Google Play limits:

Field	Limit
Title	50 characters
Short Description	80 characters
Full Description	4000 characters
# Validate before upload
gplay validate listing \
  --dir ./fastlane/metadata/android \
  --locale en-US

Workflow Example

Complete metadata update workflow:

# 1. Export current metadata
gplay sync export-listings \
  --package com.example.app \
  --dir ./metadata

# 2. Edit files locally
vi ./metadata/en-US/full_description.txt

# 3. Validate changes
gplay validate listing \
  --dir ./metadata \
  --locale en-US

# 4. See what will change
gplay sync diff-listings \
  --package com.example.app \
  --dir ./metadata

# 5. Import changes
gplay sync import-listings \
  --package com.example.app \
  --dir ./metadata

Multi-Locale Management
Create new locale

Copy existing locale directory:

cp -r fastlane/metadata/android/en-US fastlane/metadata/android/es-ES


Translate all text files

Import:

gplay sync import-listings \
  --package com.example.app \
  --dir ./fastlane/metadata/android

Supported Locales

Use Play Console locale codes:

en-US - English (United States)
es-ES - Spanish (Spain)
fr-FR - French (France)
de-DE - German (Germany)
ja-JP - Japanese (Japan)
etc.
Best Practices
Keep metadata in version control - Track changes over time
Validate before importing - Catch character limit errors
Use consistent formatting - Follow style guide
Test on different devices - Screenshots should represent actual app
Update regularly - Keep descriptions current with features
Localize properly - Don't use machine translation without review
Weekly Installs
87
Repository
tamtom/gplay-cli-skills
GitHub Stars
33
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass