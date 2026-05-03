---
title: android-playstore-scan
url: https://skills.sh/hitoshura25/claude-devtools/android-playstore-scan
---

# android-playstore-scan

skills/hitoshura25/claude-devtools/android-playstore-scan
android-playstore-scan
Installation
$ npx skills add https://github.com/hitoshura25/claude-devtools --skill android-playstore-scan
SKILL.md
Android Play Store Scanner

ANALYSIS ONLY - Scans your Android project and generates a comprehensive Play Console setup checklist. Does NOT modify any files.

Overview

Purpose:

Analyze project to detect app features and requirements
Pre-fill Play Console setup answers based on code analysis
Identify missing configurations (privacy policy, etc.)
Generate actionable checklist for Play Console setup

What this skill does:

Scans AndroidManifest.xml for permissions and features
Analyzes build.gradle for SDKs and dependencies
Detects Health Connect, ads, analytics
Checks for privacy policy URL
Generates PLAY_CONSOLE_SETUP.md with pre-filled answers
Provides recommendations for missing items

What this skill does NOT do:

❌ Does not create or modify any project files
❌ Does not setup GitHub Actions or workflows
❌ Does not generate privacy policies (use /devtools:privacy-policy-generate)
❌ Does not configure signing or release builds
Prerequisites
Android project with AndroidManifest.xml
Build configuration files (build.gradle.kts)
Inputs
Input	Required	Default	Description
project_path	Yes	.	Android project root
Process
Step 1: Scan AndroidManifest.xml
echo "📱 Scanning AndroidManifest.xml..."

# Get package name
PACKAGE_NAME=$(grep "package=" app/src/main/AndroidManifest.xml | head -1 | sed 's/.*package="\([^"]*\)".*/\1/')
echo "  Package: $PACKAGE_NAME"

# Get app name
APP_NAME=$(grep 'name="app_name"' app/src/main/res/values/strings.xml 2>/dev/null | sed 's/.*>\([^<]*\)<.*/\1/' || echo "Unknown")
echo "  App name: $APP_NAME"

# Check permissions
echo "  Scanning permissions..."
PERMISSIONS=$(grep "<uses-permission" app/src/main/AndroidManifest.xml | sed 's/.*android:name="\([^"]*\)".*/\1/')

# Detect features
INTERNET=$(echo "$PERMISSIONS" | grep -q "INTERNET" && echo "Yes" || echo "No")
LOCATION=$(echo "$PERMISSIONS" | grep -q "LOCATION" && echo "Yes" || echo "No")
CAMERA=$(echo "$PERMISSIONS" | grep -q "CAMERA" && echo "Yes" || echo "No")
HEALTH=$(echo "$PERMISSIONS" | grep -q "health.permission" && echo "Yes" || echo "No")

echo "    Internet: $INTERNET"
echo "    Location: $LOCATION"
echo "    Camera: $CAMERA"
echo "    Health Connect: $HEALTH"

Step 2: Analyze Dependencies
echo "📦 Scanning build.gradle.kts..."

# Check for ads
ADS_DETECTED="No"
if grep -q "admob" app/build.gradle.kts 2>/dev/null; then
    ADS_DETECTED="Yes (AdMob)"
elif grep -q "facebook-ads" app/build.gradle.kts 2>/dev/null; then
    ADS_DETECTED="Yes (Facebook Audience Network)"
fi
echo "  Ads: $ADS_DETECTED"

# Check for analytics
ANALYTICS_DETECTED=""
grep -q "firebase-analytics" app/build.gradle.kts 2>/dev/null && ANALYTICS_DETECTED="Firebase Analytics"
grep -q "google-analytics" app/build.gradle.kts 2>/dev/null && ANALYTICS_DETECTED="${ANALYTICS_DETECTED} Google Analytics"
echo "  Analytics: ${ANALYTICS_DETECTED:-None}"

# Check for payments
PAYMENTS="No"
grep -q "billing" app/build.gradle.kts 2>/dev/null && PAYMENTS="Yes (Google Play Billing)"
echo "  In-app purchases: $PAYMENTS"

# Check for auth
AUTH_DETECTED=""
grep -q "firebase-auth" app/build.gradle.kts 2>/dev/null && AUTH_DETECTED="Firebase Auth"
grep -q "play-services-auth" app/build.gradle.kts 2>/dev/null && AUTH_DETECTED="${AUTH_DETECTED} Google Sign-In"
echo "  Authentication: ${AUTH_DETECTED:-None detected}"

Step 3: Check Privacy Policy
echo "🔒 Checking for privacy policy..."

PRIVACY_POLICY_URL=""
# Check common locations
if [ -f docs/privacy-policy.md ]; then
    PRIVACY_POLICY_URL="https://$(git config remote.origin.url | sed 's/.*github.com[:/]\(.*\)\.git/\1/')/privacy-policy"
    echo "  ✓ Found: docs/privacy-policy.md"
    echo "  Suggested URL: $PRIVACY_POLICY_URL"
elif grep -q "privacy" README.md 2>/dev/null; then
    echo "  ⚠️  Privacy policy mentioned in README but not found in docs/"
else
    echo "  ❌ Privacy policy not found"
    PRIVACY_POLICY_URL="⚠️ ACTION REQUIRED"
fi

Step 4: Detect Health Connect Data Types

If Health Connect is detected:

if [ "$HEALTH" = "Yes" ]; then
    echo "💚 Analyzing Health Connect integration..."

    HEALTH_DATA_TYPES=""
    grep -q "STEPS" app/src/main/AndroidManifest.xml && HEALTH_DATA_TYPES="${HEALTH_DATA_TYPES}- Steps (read/write)\n"
    grep -q "HEART_RATE" app/src/main/AndroidManifest.xml && HEALTH_DATA_TYPES="${HEALTH_DATA_TYPES}- Heart rate (read)\n"
    grep -q "SLEEP" app/src/main/AndroidManifest.xml && HEALTH_DATA_TYPES="${HEALTH_DATA_TYPES}- Sleep sessions (read)\n"
    grep -q "EXERCISE" app/src/main/AndroidManifest.xml && HEALTH_DATA_TYPES="${HEALTH_DATA_TYPES}- Exercise sessions (read/write)\n"

    echo -e "  Health data types:\n$HEALTH_DATA_TYPES"
fi

Step 5: Estimate Content Rating
echo "🎯 Estimating content rating..."

# Simple heuristic - actual rating requires IARC questionnaire
ESTIMATED_RATING="Everyone (E)"

if grep -qi "violence\|weapon\|blood" app/src/main/res/values/strings.xml 2>/dev/null; then
    ESTIMATED_RATING="Teen (T) - Violence detected"
elif grep -qi "gambling\|casino\|lottery" app/src/main/res/values/strings.xml 2>/dev/null; then
    ESTIMATED_RATING="Mature (M) - Gambling detected"
fi

echo "  Estimated: $ESTIMATED_RATING"
echo "  Note: Complete official IARC questionnaire in Play Console"

Step 6: Generate PLAY_CONSOLE_SETUP.md

Create comprehensive setup guide:

# Play Console Setup Guide for: {APP_NAME}

Generated: {CURRENT_DATE}

---

## Summary

| Property | Value |
|----------|-------|
| **Package Name** | {PACKAGE_NAME} |
| **App Name** | {APP_NAME} |
| **Privacy Policy** | {PRIVACY_POLICY_STATUS} |
| **Uses Health Connect** | {HEALTH_DETECTED} |
| **Contains Ads** | {ADS_DETECTED} |
| **In-App Purchases** | {IAP_DETECTED} |

---

## 1. Privacy Policy

**Status:** {PRIVACY_STATUS}

{IF_NOT_FOUND}
**⚠️ ACTION REQUIRED:** No privacy policy found

**Recommended action:**


/devtools:privacy-policy-generate


This will create a privacy policy at `docs/privacy-policy.md` ready for GitHub Pages.
{ELSE}
**✓ Privacy policy found:** `docs/privacy-policy.md`

**Suggested URL:** `{PRIVACY_URL}`

**Next steps:**
1. Enable GitHub Pages (Settings → Pages → Source: docs/)
2. Wait 1-2 minutes for deployment
3. Verify URL is accessible
4. Add URL to Play Console
{END_IF}

---

## 2. App Access

**Detected:** {ACCESS_ANALYSIS}

{IF_AUTH_DETECTED}
**Answer:** "Yes, some functionality requires special access"

**Instructions to provide:**
- Test account credentials (if applicable)
- How to access restricted features
{ELSE}
**Answer:** "All functionality available without special access"
{END_IF}

---

## 3. Ads Declaration

**Detected SDKs:** {ADS_DETECTED}

{IF_ADS}
**Answer:** "Yes, my app contains ads"

**Ad networks:** {AD_NETWORKS_LIST}
{ELSE}
**Answer:** "No, my app does not contain ads"
{END_IF}

---

## 4. Content Rating

**Estimated Rating:** {ESTIMATED_RATING}

**Action Required:**
1. Go to Play Console → **App content** → **Content rating**
2. Complete IARC questionnaire
3. Answer questions about:
   - Violence
   - Sexual content
   - Profanity
   - Controlled substances
   - Gambling
   - User-generated content

---

## 5. Data Safety Form

**Data Collection Detected:**

| Data Type | Collected | Purpose |
|-----------|-----------|---------|
{IF_HEALTH}
| Health & Fitness | Yes | Health Connect integration |
{END_IF}
{IF_LOCATION}
| Location | Yes | {LOCATION_PURPOSE} |
{END_IF}
{IF_ANALYTICS}
| App activity | Yes | Analytics ({ANALYTICS_SERVICES}) |
{END_IF}
| Device ID | {DEVICE_ID_COLLECTED} | {DEVICE_ID_PURPOSE} |

**Security Practices:**

| Practice | Status | Notes |
|----------|--------|-------|
| Data encrypted in transit | {HTTPS_DETECTED} | HTTPS detected in network config |
| Data encrypted at rest | ⚠️ User to confirm | Depends on implementation |
| Users can request deletion | ⚠️ User to confirm | Add if applicable |

**Recommended answers:**
- Data is collected: {DATA_COLLECTED}
- Data is shared: {DATA_SHARED}
- Data collection is optional: {DATA_OPTIONAL}

---

{IF_HEALTH}
## 6. Health App Declaration

**⚠️ REQUIRED:** Your app uses Health Connect

**Health Data Types Detected:**
{HEALTH_DATA_TYPES_LIST}

**Action Required:**
1. Go to Play Console → **App content** → **Health**
2. Select "Yes, my app accesses health data"
3. List all health data types your app accesses
4. Explain how each data type is used
5. Confirm privacy policy includes health data disclosure

**Privacy Policy Requirements:**
- ✅ Must explain what health data is accessed
- ✅ Must explain why it's accessed
- ✅ Must explain how it's stored
- ✅ Must explain if it's shared with third parties

**Verify privacy policy includes Health Data section**
{END_IF}

---

## 7. Store Listing (Draft)

**Title:** {APP_NAME}

**Short Description (80 chars):**
{GENERATED_SHORT_DESC}

**Full Description:**
{GENERATED_FULL_DESC}

⚠️ Review and customize these descriptions before submitting

---

## 8. First Upload Checklist

Before you can use automated deployments, you must manually upload your first release:

### Preparation

- [ ] Run `/devtools:android-keystore-generation` (if not done)
- [ ] Run `/devtools:android-signing-config`
- [ ] Build release AAB: `./gradlew bundleRelease`
- [ ] Verify AAB is signed: `jarsigner -verify -verbose app/build/outputs/bundle/release/app-release.aab`

### Play Console First Upload

- [ ] Go to Play Console → **Release** → **Internal testing**
- [ ] Click **Create new release**
- [ ] Upload `app-release.aab`
- [ ] Complete store listing (title, description, screenshots)
- [ ] Complete all required declarations above
- [ ] Review and publish to internal testing

### Important Notes

⚠️ **First Upload Keystore = CI Keystore**

The keystore you use for the first upload becomes your **upload key**. You must use the same keystore in CI/CD.

**After first upload:**
- Note the SHA-1 fingerprint from Play Console
- Use the same production keystore for GitHub Actions
- Do NOT generate a different keystore for CI

### Play App Signing

**How it works:**
1. First upload: Google creates the **app signing key** (permanent)
2. Your keystore becomes the **upload key** (can be reset if lost)
3. Google re-signs your AAB with the app signing key before distribution

**No action needed** - Play App Signing is automatic for new apps.

---

## 9. Next Steps

After completing the checklist above:

```bash
# Setup automated Play Store publishing
/devtools:android-playstore-setup


This will:

Configure Gradle Play Publisher plugin
Create GitHub Actions workflows
Setup release automation
10. Track Differences

Understanding Play Store release tracks:

Track	Audience	Use Case	Review Time
Internal	Up to 100 testers	Quick testing	Instant
Closed (Alpha)	Invited testers	Beta testing	< 24h
Open (Beta)	Anyone can join	Public beta	< 24h
Production	All users	Full release	1-7 days

Recommended flow:

Internal → Verify app works
Beta → Wider testing (optional)
Production → Full release
Validation

Run validation checks:

# Validate Play Store API connection
python3 scripts/validate-playstore.py SERVICE_ACCOUNT.json {PACKAGE_NAME}


Expected: ✅ All validations passed

Resources
Play Console Help
Data safety form guide
Health Connect policy
Content rating questionnaire

Generated by android-playstore-scan v1.0.0


## Verification

**MANDATORY:** Run these commands:

```bash
# Verify setup guide created
test -f PLAY_CONSOLE_SETUP.md && echo "✓ Setup guide created"

# Verify key sections present
grep -q "Privacy Policy" PLAY_CONSOLE_SETUP.md && echo "✓ Privacy policy section"
grep -q "Data Safety" PLAY_CONSOLE_SETUP.md && echo "✓ Data safety section"
grep -q "First Upload" PLAY_CONSOLE_SETUP.md && echo "✓ First upload checklist"


Expected output:

✓ Setup guide created
✓ Privacy policy section
✓ Data safety section
✓ First upload checklist
Outputs
Output	Location	Description
Setup checklist	PLAY_CONSOLE_SETUP.md	Complete Play Console setup guide
What Happens Next

After reviewing PLAY_CONSOLE_SETUP.md:

Address action items (privacy policy, missing configs)
Run setup skill:
/devtools:android-playstore-setup

This will execute the actual setup based on the checklist
Detected vs. Actual

This skill detects:

✅ Declared permissions in manifest
✅ Dependencies in build.gradle
✅ Health Connect integration
✅ Common SDKs (ads, analytics)

This skill cannot detect:

❌ Runtime permission usage patterns
❌ Actual network calls and endpoints
❌ User-generated content handling
❌ Content rating accuracy

Always review the generated checklist and adjust based on your actual implementation.

Troubleshooting
"Package name not found"

Cause: AndroidManifest.xml format issue Fix: Verify package attribute exists in <manifest> tag

"No permissions detected"

Cause: Permissions declared in Gradle instead of manifest Fix: Check build.gradle.kts for permission declarations

"Privacy policy detection failed"

Cause: Privacy policy in non-standard location Fix: Update scan or manually specify URL in generated checklist

Completion Criteria
 PLAY_CONSOLE_SETUP.md created
 All project features detected correctly
 Privacy policy status identified
 Health Connect integration detected (if applicable)
 Action items clearly marked
 Ready to proceed with actual setup
Weekly Installs
15
Repository
hitoshura25/cla…devtools
GitHub Stars
3
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass