---
title: pii-redaction-logging-policy-builder
url: https://skills.sh/patricio0312rev/skills/pii-redaction-logging-policy-builder
---

# pii-redaction-logging-policy-builder

skills/patricio0312rev/skills/pii-redaction-logging-policy-builder
pii-redaction-logging-policy-builder
Installation
$ npx skills add https://github.com/patricio0312rev/skills --skill pii-redaction-logging-policy-builder
SKILL.md
PII Redaction & Logging Policy Builder

Protect user privacy in application logs.

PII Redaction
const PII_PATTERNS = {
  email: /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b/g,
  ssn: /\b\d{3}-\d{2}-\d{4}\b/g,
  phone: /\b\d{3}[-.]?\d{3}[-.]?\d{4}\b/g,
  creditCard: /\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b/g,
};

function redactPII(message: string): string {
  let redacted = message;
  Object.entries(PII_PATTERNS).forEach(([type, pattern]) => {
    redacted = redacted.replace(pattern, `[REDACTED_${type.toUpperCase()}]`);
  });
  return redacted;
}

// Safe logging
logger.info(redactPII(\`User registered: \${email}\`));
// Output: "User registered: [REDACTED_EMAIL]"

Logging Policy
# Logging Policy

## ✅ DO Log

- Request IDs
- User IDs (hashed)
- HTTP status codes
- Response times
- Error types
- Feature flags

## ❌ DON'T Log

- Passwords
- Credit card numbers
- SSNs
- API keys
- Full emails (hash first)
- Full names
- Addresses

Output Checklist
 Redaction rules defined
 Logging policy documented
 Safe logger wrapper
 Team trained
 Log monitoring ENDFILE
Weekly Installs
91
Repository
patricio0312rev/skills
GitHub Stars
35
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass