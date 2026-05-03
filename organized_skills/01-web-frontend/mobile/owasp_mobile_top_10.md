---
rating: ⭐⭐
title: owasp-mobile-top-10
url: https://skills.sh/yariv1025/skills/owasp-mobile-top-10
---

# owasp-mobile-top-10

skills/yariv1025/skills/owasp-mobile-top-10
owasp-mobile-top-10
Installation
$ npx skills add https://github.com/yariv1025/skills --skill owasp-mobile-top-10
SKILL.md
OWASP Mobile Top 10

This skill encodes the OWASP Mobile Top 10 for secure mobile app design and review. References are loaded per risk (progressive disclosure). Based on OWASP Mobile Top 10 2024.

When to Read Which Reference
Risk	Read
M1 Improper Credential Usage	references/m1-improper-credential-usage.md
M2 Inadequate Supply Chain Security	references/m2-supply-chain-security.md
M3 Insecure Authentication/Authorization	references/m3-insecure-auth.md
M4 Insufficient Input/Output Validation	references/m4-input-output-validation.md
M5 Insecure Communication	references/m5-insecure-communication.md
M6 Inadequate Privacy Controls	references/m6-privacy-controls.md
M7 Insufficient Binary Protections	references/m7-binary-protections.md
M8 Security Misconfiguration	references/m8-security-misconfiguration.md
M9 Insecure Data Storage	references/m9-insecure-data-storage.md
M10 Insufficient Cryptography	references/m10-insufficient-cryptography.md
Quick Patterns
Store credentials and API keys in secure storage (keychain/Keystore); never hardcode. Validate all inputs and encode outputs.
Use certificate pinning and TLS for communication; enforce privacy controls and minimal data collection.
Harden binary (obfuscation, integrity); use secure defaults and encrypt sensitive data at rest.
Quick Reference / Examples
Task	Approach
Store credentials	Use iOS Keychain or Android Keystore; never hardcode. See M1.
Secure network calls	Use TLS 1.2+, implement certificate pinning. See M5.
Validate input	Sanitize all user/external input before use. See M4.
Protect local data	Encrypt with platform APIs (EncryptedSharedPreferences, Data Protection). See M9.

Safe - Android Keystore for credentials:

val keyStore = KeyStore.getInstance("AndroidKeyStore")
keyStore.load(null)
val secretKey = keyStore.getKey("my_key_alias", null) as SecretKey


Unsafe - hardcoded API key:

val API_KEY = "sk-12345abcdef"  // NEVER do this - extract from APK


Certificate pinning (OkHttp):

val certificatePinner = CertificatePinner.Builder()
    .add("api.example.com", "sha256/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=")
    .build()

Workflow

Load the reference for the risk you are addressing (e.g. credential handling → M1; network → M5; local storage → M9). See OWASP Mobile Top 10 for the official list.

Weekly Installs
16
Repository
yariv1025/skills
GitHub Stars
1
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass