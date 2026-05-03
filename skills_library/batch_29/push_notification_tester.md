---
title: push-notification-tester
url: https://skills.sh/team-telnyx/skills/push-notification-tester
---

# push-notification-tester

skills/team-telnyx/skills/push-notification-tester
push-notification-tester
Installation
$ npx skills add https://github.com/team-telnyx/skills --skill push-notification-tester
SKILL.md
Push Notification Tester

Send test VoIP push notifications to iOS (APNs) and Android (FCM) devices.

iOS (APNs)
node {baseDir}/scripts/send-ios-push.js \
  --token=<device_token> \
  --bundle-id=<bundle_id> \
  --cert=<path/to/cert.pem> \
  --key=<path/to/key.pem> \
  [--env=sandbox|production] \
  [--caller-name="Test Caller"] \
  [--caller-number="+1234567890"]

Required args
--token — 64-char hex APNs device token
--bundle-id — App bundle ID (e.g. com.telnyx.webrtc)
--cert — Path to certificate PEM file
--key — Path to private key PEM file
Optional args
--env — sandbox (default) or production
--caller-name — Display name (default: "Test Caller")
--caller-number — Phone number (default: "+1234567890")
Android (FCM)
node {baseDir}/scripts/send-android-push.js \
  --token=<fcm_token> \
  --project-id=<firebase_project_id> \
  --service-account=<path/to/service-account.json> \
  [--caller-name="Test Caller"] \
  [--caller-number="+1234567890"]

Required args
--token — FCM device token
--project-id — Firebase project ID
--service-account — Path to service account JSON file
Optional args
--caller-name — Display name (default: "Test Caller")
--caller-number — Phone number (default: "+1234567890")
Output

Both scripts output JSON to stdout:

{"success": true, "message": "Push notification sent successfully", "details": {...}}

{"success": false, "error": "Description of what went wrong"}


Exit code 0 on success, 1 on failure.

Dependencies

Run npm install in the scripts/ directory, or the scripts will auto-install on first run.

@parse/node-apn — APNs client for iOS
google-auth-library — Google OAuth for FCM
axios — HTTP client for FCM API
Weekly Installs
30
Repository
team-telnyx/skills
GitHub Stars
171
First Seen
Feb 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn