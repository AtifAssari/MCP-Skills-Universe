---
rating: ⭐⭐⭐
title: gplay-signing-setup
url: https://skills.sh/tamtom/gplay-cli-skills/gplay-signing-setup
---

# gplay-signing-setup

skills/tamtom/gplay-cli-skills/gplay-signing-setup
gplay-signing-setup
Installation
$ npx skills add https://github.com/tamtom/gplay-cli-skills --skill gplay-signing-setup
SKILL.md
Android App Signing Setup

Use this skill when you need to set up or manage app signing for Google Play.

Understanding Android App Signing

Android apps must be signed with a certificate before upload. Two signing approaches:

App Signing by Google Play (Recommended) - Google manages your signing key
Manual Signing (Legacy) - You manage your signing key
Create a New Keystore
Generate keystore
keytool -genkey -v \
  -keystore release.keystore \
  -alias my-app-key \
  -keyalg RSA \
  -keysize 2048 \
  -validity 10000


You'll be prompted for:

Keystore password (store securely!)
Key password (can be same as keystore password)
Your name/organization details
Keystore file location
Development: Keep locally, never commit to git
Production: Store in secure location (password manager, secrets vault)
CI/CD: Use encrypted secrets
Configure Gradle Signing
gradle.properties (gitignored)
KEYSTORE_FILE=/path/to/release.keystore
KEYSTORE_PASSWORD=your_keystore_password
KEY_ALIAS=my-app-key
KEY_PASSWORD=your_key_password

app/build.gradle
android {
    signingConfigs {
        release {
            storeFile file(project.property('KEYSTORE_FILE'))
            storePassword project.property('KEYSTORE_PASSWORD')
            keyAlias project.property('KEY_ALIAS')
            keyPassword project.property('KEY_PASSWORD')
        }
    }

    buildTypes {
        release {
            signingConfig signingConfigs.release
        }
    }
}

Using environment variables (CI/CD)
android {
    signingConfigs {
        release {
            storeFile file(System.getenv("KEYSTORE_FILE") ?: "release.keystore")
            storePassword System.getenv("KEYSTORE_PASSWORD")
            keyAlias System.getenv("KEY_ALIAS")
            keyPassword System.getenv("KEY_PASSWORD")
        }
    }
}

Play App Signing Setup
Enable Play App Signing (New App)

Build and sign AAB with upload key:

./gradlew bundleRelease


Upload AAB to Play Console:

gplay release \
  --package com.example.app \
  --track internal \
  --bundle app-release.aab


Google Play generates app signing key automatically

Download upload certificate:

Go to Play Console → App → Setup → App signing
Download "Upload certificate" (will be used for future uploads)
Migrate Existing App to Play App Signing

If your app uses manual signing:

Export upload key:

keytool -export -rfc \
  -keystore release.keystore \
  -alias my-app-key \
  -file upload_cert.pem


Encrypt private key (required by Google):

# Generate password for encryption
openssl rand -base64 32 > encryption_password.txt

# Export and encrypt private key
keytool -importkeystore \
  -srckeystore release.keystore \
  -destkeystore encrypted.p12 \
  -deststoretype PKCS12 \
  -srcalias my-app-key \
  -deststorepass $(cat encryption_password.txt)


Upload to Play Console:

Go to Play Console → App → Setup → App signing
Choose "Export and upload a key"
Upload encrypted.p12 and encryption_password.txt

Download new upload key:

After migration, download new upload certificate
Use this for all future uploads
Verify Keystore
List keys in keystore
keytool -list -v -keystore release.keystore

Check certificate validity
keytool -list -v \
  -keystore release.keystore \
  -alias my-app-key \
  | grep Valid

Extract certificate fingerprint
# SHA-256 (for Firebase, etc.)
keytool -list -v \
  -keystore release.keystore \
  -alias my-app-key \
  | grep SHA256

Verify APK/AAB Signature
Check AAB signature
jarsigner -verify -verbose -certs app-release.aab

Check APK signature
jarsigner -verify -verbose -certs app-release.apk

CI/CD Signing
GitHub Actions Example
- name: Decode keystore
  run: |
    echo "${{ secrets.KEYSTORE_BASE64 }}" | base64 -d > release.keystore

- name: Build signed AAB
  env:
    KEYSTORE_FILE: release.keystore
    KEYSTORE_PASSWORD: ${{ secrets.KEYSTORE_PASSWORD }}
    KEY_ALIAS: ${{ secrets.KEY_ALIAS }}
    KEY_PASSWORD: ${{ secrets.KEY_PASSWORD }}
  run: |
    ./gradlew bundleRelease

- name: Clean up keystore
  if: always()
  run: rm -f release.keystore

Store keystore as base64
# Encode keystore to base64
base64 -i release.keystore -o keystore_base64.txt

# Add to GitHub Secrets as KEYSTORE_BASE64

Upload Certificate Management
Register upload certificate for existing app

If you lose your upload key:

Generate new keystore (as shown above)

Export certificate:

keytool -export -rfc \
  -keystore new-upload.keystore \
  -alias my-app-key \
  -file new_upload_cert.pem


Contact Google Play support to reset upload key:

Go to Play Console → Help
Request upload certificate reset
Provide new_upload_cert.pem
Security Best Practices
DO:
✅ Use strong passwords (16+ characters)
✅ Store keystore in multiple secure locations
✅ Use different keys for different apps
✅ Enable Play App Signing
✅ Keep upload key separate from production
✅ Document key details securely (not passwords!)
✅ Set calendar reminder for key expiration (10-25 years)
DON'T:
❌ Commit keystores to git
❌ Share keystores via email/chat
❌ Use weak or obvious passwords
❌ Store passwords in code
❌ Forget to backup keystores
❌ Use same key for debug and release
Keystore Backup Strategy
What to backup:
Keystore file (release.keystore)
Key alias name
Keystore password (in password manager)
Key password (in password manager)
Where to backup:
Password manager (1Password, LastPass, etc.)
Encrypted cloud storage
Company secrets vault
Physical secure storage (for enterprise)
Test restore process:
# Verify you can use the backup
keytool -list -v -keystore backup/release.keystore

Troubleshooting
"jarsigner: unable to sign jar"
Check keystore password is correct
Verify keystore file path
Ensure keystore alias exists
"Failed to read key from keystore"
Key alias might be wrong
Key password might be wrong
Keystore might be corrupted
"Upload certificate doesn't match"
You're using wrong keystore
Keystore was regenerated (contact support)
Using app signing key instead of upload key
Lost keystore?
If using Play App Signing: Contact Google to reset upload key
If not using Play App Signing: Cannot recover, must publish new app
Multiple Apps, Multiple Keys
Organize multiple keystores
~/keystores/
├── app1-release.keystore
├── app2-release.keystore
└── app3-release.keystore

Use different gradle.properties per app
# app1/gradle.properties
KEYSTORE_FILE=~/keystores/app1-release.keystore
KEY_ALIAS=app1-key

# app2/gradle.properties
KEYSTORE_FILE=~/keystores/app2-release.keystore
KEY_ALIAS=app2-key

Key Rotation

Android apps are typically signed with long-lived keys (10-25 years), but if you need to rotate:

Only possible with Play App Signing enabled
Contact Google Play Support to rotate app signing key
Upload new upload certificate when prompted
All future builds must use new upload key
Documentation Template

Keep this info in your password manager:

App Name: My Awesome App
Package: com.example.app
Keystore File: release.keystore (backed up in Dropbox)
Keystore Password: [IN PASSWORD MANAGER]
Key Alias: my-app-key
Key Password: [IN PASSWORD MANAGER]
Certificate Validity: Valid until 2035-02-05
SHA-256 Fingerprint: AB:CD:EF:12:...
Play App Signing: Enabled
Notes: Upload key only, Google manages app signing key

Weekly Installs
85
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