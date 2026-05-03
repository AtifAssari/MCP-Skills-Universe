---
title: firebase-auth-basics
url: https://skills.sh/firebase/skills/firebase-auth-basics
---

# firebase-auth-basics

skills/firebase/skills/firebase-auth-basics
firebase-auth-basics
Originally fromfirebase/agent-skills
Installation
$ npx skills add https://github.com/firebase/skills --skill firebase-auth-basics
Summary

Set up Firebase Authentication with multiple identity providers and secure data access.

Supports email/password, phone number, anonymous, federated providers (Google, Facebook, Twitter, GitHub, Microsoft, Apple), and custom auth integration
Users are identified by unique UIDs with optional properties including email, display name, photo URL, and email verification status
Authentication via CLI enables Google Sign In, anonymous auth, and email/password; other providers require Firebase Console configuration
Issues short-lived ID tokens (JWTs) for service requests and long-lived refresh tokens for token renewal
Secure data access through Firestore and Cloud Storage rules using request.auth for permission enforcement
SKILL.md
Prerequisites
Firebase Project: Created via npx -y firebase-tools@latest projects:create (see firebase-basics).
Firebase CLI: Installed and logged in (see firebase-basics).
Core Concepts

Firebase Authentication provides backend services, easy-to-use SDKs, and ready-made UI libraries to authenticate users to your app.

Users

A user is an entity that can sign in to your app. Each user is identified by a unique ID (uid) which is guaranteed to be unique across all providers. User properties include:

uid: Unique identifier.
email: User's email address (if available).
displayName: User's display name (if available).
photoURL: URL to user's photo (if available).
emailVerified: Boolean indicating if the email is verified.
Identity Providers

Firebase Auth supports multiple ways to sign in:

Email/Password: Basic email and password authentication.
Federated Identity Providers: Google, Facebook, Twitter, GitHub, Microsoft, Apple, etc.
Phone Number: SMS-based authentication.
Anonymous: Temporary guest accounts that can be linked to permanent accounts later.
Custom Auth: Integrate with your existing auth system.

Google Sign In is recommended as a good and secure default provider.

Tokens

When a user signs in, they receive an ID Token (JWT). This token is used to identify the user when making requests to Firebase services (Realtime Database, Cloud Storage, Firestore) or your own backend.

ID Token: Short-lived (1 hour), verifies identity.
Refresh Token: Long-lived, used to get new ID tokens.
Workflow
1. Provisioning
Option 1. Enabling Authentication via CLI

Only Google Sign In, anonymous auth, and email/password auth can be enabled via CLI. For other providers, use the Firebase Console.

Configure Firebase Authentication in firebase.json by adding an 'auth' block:

{
  "auth": {
    "providers": {
      "anonymous": true,
      "emailPassword": true,
      "googleSignIn": {
        "oAuthBrandDisplayName": "Your Brand Name",
        "supportEmail": "support@example.com",
        "authorizedRedirectUris": ["https://example.com"]
      }
    }
  }
}


CRITICAL: After configuring firebase.json, you MUST deploy the auth configuration to the Firebase backend for the changes to take effect. This is essential for auth providers like Google Sign-In, email/password, etc. to auto-generate the necessary OAuth clients for your app platforms. Run:

npx -y firebase-tools@latest deploy --only auth

Option 2. Enabling Authentication in Console

Enable other providers in the Firebase Console.

Go to the https://console.firebase.google.com/project/_/authentication/providers
Select your project.
Enable the desired Sign-in providers (e.g., Email/Password, Google).
2. Client Setup & Usage

Web See references/client_sdk_web.md.

Flutter See references/flutter_setup.md. Android (Kotlin) See references/client_sdk_android.md.

3. Security Rules

Secure your data using request.auth in Firestore/Storage rules.

See references/security_rules.md.

Weekly Installs
673
Repository
firebase/skills
GitHub Stars
264
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass