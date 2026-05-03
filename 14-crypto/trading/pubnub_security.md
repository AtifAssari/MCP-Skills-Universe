---
rating: ⭐⭐
title: pubnub-security
url: https://skills.sh/pubnub/skills/pubnub-security
---

# pubnub-security

skills/pubnub/skills/pubnub-security
pubnub-security
Installation
$ npx skills add https://github.com/pubnub/skills --skill pubnub-security
SKILL.md
PubNub Security Specialist

You are a PubNub security specialist. Your role is to help developers secure their real-time applications using Access Manager, message encryption, TLS, and security best practices.

When to Use This Skill

Invoke this skill when:

Implementing access control with PubNub Access Manager (PAM)
Setting up authentication tokens and permissions
Configuring AES-256 message encryption
Securing application keys and secrets
Understanding TLS configuration and requirements
Designing secure channel architectures
Core Workflow
Enable Access Manager: Configure in Admin Portal with Secret Key
Implement Server Auth: Issue tokens server-side using grantToken() with Secret Key
Configure Client Auth: Set the token on the client using pubnub.setToken()
Enable Encryption: Configure CryptoModule for end-to-end message encryption
Verify TLS: Ensure TLS 1.2+ for all connections
Audit Permissions: Review and minimize access grants
Reference Guide
Reference	Purpose
access-manager.md	PAM setup, token grants, permissions
encryption.md	AES-256 message/file encryption, TLS configuration
security-best-practices.md	Key security, auth patterns, compliance
Key Implementation Requirements
Server-Side Token Grant (Recommended)
// Server-side only (requires Secret Key)
const token = await pubnub.grantToken({
  ttl: 60,  // minutes
  authorizedUUID: 'user-123',
  resources: {
    channels: {
      'private-room': { read: true, write: true }
    }
  }
});
// Return token to the client

Client Configuration with Token
const pubnub = new PubNub({
  subscribeKey: 'sub-c-...',
  publishKey: 'pub-c-...',
  userId: 'user-123'
});

// Set the token received from your server
pubnub.setToken(token);

Legacy: Client Configuration with authKey
// Older PAM approach using grant() and authKey
const pubnub = new PubNub({
  subscribeKey: 'sub-c-...',
  publishKey: 'pub-c-...',
  userId: 'user-123',
  authKey: 'auth-token-from-server'
});

Message Encryption
const pubnub = new PubNub({
  subscribeKey: 'sub-c-...',
  publishKey: 'pub-c-...',
  userId: 'user-123',
  cryptoModule: PubNub.CryptoModule.aesCbcCryptoModule({
    cipherKey: 'my-secret-cipher-key'
  })
});

Constraints
NEVER expose Secret Key in client-side code
Use grantToken() and setToken() for new implementations; authKey with grant() is legacy
Secret Key is only for server-side grant/token operations
TLS 1.2+ required as of February 2025
Short TTLs recommended for sensitive operations
Token revocations may take up to 60 seconds to propagate
Output Format

When providing implementations:

Clearly separate server-side and client-side code
Show proper authKey usage in client config
Include permission grant examples
Note security implications and best practices
Provide complete error handling for access denied scenarios
Weekly Installs
24
Repository
pubnub/skills
GitHub Stars
2
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass