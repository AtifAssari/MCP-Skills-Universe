---
title: security-review
url: https://skills.sh/dralgorhythm/claude-agentic-framework/security-review
---

# security-review

skills/dralgorhythm/claude-agentic-framework/security-review
security-review
Installation
$ npx skills add https://github.com/dralgorhythm/claude-agentic-framework --skill security-review
SKILL.md
Security Review
Review Checklist
Authentication
 Strong password requirements enforced
 MFA implemented for sensitive operations
 Session tokens are cryptographically secure
 Session timeout is appropriate
 Logout properly invalidates session
Authorization
 Access controls checked server-side
 Least privilege principle applied
 Role-based access properly implemented
 Direct object references validated
Input Validation
 All input validated server-side
 Input type and length checked
 Special characters properly handled
 File uploads validated and restricted
Output Encoding
 HTML output properly encoded
 JSON responses use proper content type
 Error messages don't leak information
Cryptography
 Strong algorithms used (AES-256, RSA-2048+)
 No custom crypto implementations
 Keys properly managed
 TLS 1.2+ enforced
Error Handling
 Exceptions handled gracefully
 Error messages don't expose internals
 Failed operations logged
Logging
 Security events logged
 Sensitive data not logged
 Logs protected from tampering
Code Patterns to Flag
SQL Injection
// DANGER
db.query(`SELECT * FROM users WHERE id = ${id}`);

XSS
// DANGER
element.innerHTML = userInput;

Hardcoded Secrets
// DANGER
const API_KEY = "sk-abc123...";

Insecure Random
// DANGER
Math.random(); // For security purposes

Security Review Report
## Security Review: [Component]

### Summary
- Critical: [X]
- High: [X]
- Medium: [X]
- Low: [X]

### Findings

#### [CRITICAL] SQL Injection in UserService
**Location**: src/services/user.ts:47
**Description**: User input concatenated into SQL query
**Remediation**: Use parameterized queries
**Code**:
```typescript
// Current (vulnerable)
// Recommended fix

Weekly Installs
43
Repository
dralgorhythm/cl…ramework
GitHub Stars
76
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass