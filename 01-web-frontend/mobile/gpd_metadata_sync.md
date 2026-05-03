---
title: gpd-metadata-sync
url: https://skills.sh/rudrankriyam/app-store-connect-cli-skills/gpd-metadata-sync
---

# gpd-metadata-sync

skills/rudrankriyam/app-store-connect-cli-skills/gpd-metadata-sync
gpd-metadata-sync
Installation
$ npx skills add https://github.com/rudrankriyam/app-store-connect-cli-skills --skill gpd-metadata-sync
SKILL.md
GPD Metadata Sync

Use this skill to keep local metadata in sync with Google Play.

Store listing fields
gpd publish listing get --package com.example.app
gpd publish listing update --package com.example.app --locale en-US --title "My App"
gpd publish details get --package com.example.app
gpd publish details update --package com.example.app --contact-email support@example.com

Images and assets
gpd publish images list phoneScreenshots --package com.example.app --locale en-US
gpd publish images upload icon icon.png --package com.example.app --locale en-US
gpd publish images delete phoneScreenshots IMAGE_ID --package com.example.app --locale en-US
gpd publish images deleteall featureGraphic --package com.example.app --locale en-US
gpd publish assets upload ./assets --package com.example.app
gpd publish assets spec

Fastlane metadata workflow
Export current state
gpd migrate fastlane export --package com.example.app --output fastlane/metadata/android

Validate local files
gpd migrate fastlane validate --dir fastlane/metadata/android

Import updates
gpd migrate fastlane import --package com.example.app --dir fastlane/metadata/android

Import with options
gpd migrate fastlane import --package com.example.app --dir fastlane/metadata/android --replace-images
gpd migrate fastlane import --package com.example.app --dir fastlane/metadata/android --skip-images --dry-run

Multi-language workflow
Export localizations:
gpd migrate fastlane export --package com.example.app --output fastlane/metadata/android


Translate files in fastlane/metadata/android.

Import all at once:

gpd migrate fastlane import --package com.example.app --dir fastlane/metadata/android

Notes
Use gpd migrate fastlane validate before import to catch missing fields.
Use --dry-run when available before overwriting assets.
Weekly Installs
216
Repository
rudrankriyam/ap…i-skills
GitHub Stars
776
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn