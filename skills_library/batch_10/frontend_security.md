---
title: frontend-security
url: https://skills.sh/schalkneethling/webdev-agent-skills/frontend-security
---

# frontend-security

skills/schalkneethling/webdev-agent-skills/frontend-security
frontend-security
Installation
$ npx skills add https://github.com/schalkneethling/webdev-agent-skills --skill frontend-security
SKILL.md
Frontend Security Audit Skill

Perform comprehensive security audits of frontend codebases to identify vulnerabilities, bad practices, and missing protections.

Audit Process
Scan for dangerous patterns - Search codebase for known vulnerability indicators
Review framework-specific risks - Check for framework security bypass patterns
Validate defensive measures - Verify CSP, CSRF tokens, input validation
Check dependencies - Review npm/node dependencies for vulnerabilities
Report findings - Categorize by severity with remediation guidance
Critical Vulnerability Patterns to Search
XSS Indicators (Search Priority: HIGH)
# React dangerous patterns
grep -rn "dangerouslySetInnerHTML" --include="*.jsx" --include="*.tsx" --include="*.js"

# Direct DOM manipulation
grep -rn "\.innerHTML\s*=" --include="*.js" --include="*.ts" --include="*.jsx" --include="*.tsx"
grep -rn "\.outerHTML\s*=" --include="*.js" --include="*.ts"
grep -rn "document\.write" --include="*.js" --include="*.ts"

# URL-based injection
grep -rn "location\.href\s*=" --include="*.js" --include="*.ts"
grep -rn "location\.replace" --include="*.js" --include="*.ts"
grep -rn "window\.open" --include="*.js" --include="*.ts"

# Eval and code execution
grep -rn "eval\s*(" --include="*.js" --include="*.ts"
grep -rn "new Function\s*(" --include="*.js" --include="*.ts"
grep -rn "setTimeout\s*(\s*['\"]" --include="*.js" --include="*.ts"
grep -rn "setInterval\s*(\s*['\"]" --include="*.js" --include="*.ts"

# Twig unescaped output
grep -rn "|raw" --include="*.twig" --include="*.html.twig"
grep -rn "{% autoescape false %}" --include="*.twig"

CSRF Indicators
# Forms without CSRF tokens
grep -rn "<form" --include="*.html" --include="*.jsx" --include="*.tsx" --include="*.twig"

# State-changing requests without protection
grep -rn "fetch\s*(" --include="*.js" --include="*.ts" | grep -E "(POST|PUT|DELETE|PATCH)"
grep -rn "axios\.(post|put|delete|patch)" --include="*.js" --include="*.ts"

Sensitive Data Exposure
# localStorage/sessionStorage with sensitive data
grep -rn "localStorage\." --include="*.js" --include="*.ts"
grep -rn "sessionStorage\." --include="*.js" --include="*.ts"

# Hardcoded secrets
grep -rn "api[_-]?key\s*[:=]" --include="*.js" --include="*.ts" --include="*.env"
grep -rn "secret\s*[:=]" --include="*.js" --include="*.ts"
grep -rn "password\s*[:=]" --include="*.js" --include="*.ts"

Reference Documentation

Load these references based on findings:

XSS vulnerabilities found: See references/xss-prevention.md
CSRF concerns: See references/csrf-protection.md
DOM manipulation issues: See references/dom-security.md
CSP review needed: See references/csp-configuration.md
Input handling issues: See references/input-validation.md
Node.js/NPM audit: See references/nodejs-npm-security.md
Framework-specific patterns: See references/framework-patterns.md
File upload handling: See references/file-upload-security.md
JWT implementation: See references/jwt-security.md
Severity Classification

CRITICAL - Exploitable XSS, authentication bypass, secrets exposure HIGH - Missing CSRF protection, unsafe DOM manipulation, SQL injection vectors MEDIUM - Weak CSP, missing security headers, improper input validation LOW - Informational disclosure, deprecated functions, suboptimal practices

Report Format
## Security Audit Report

### Summary
- Critical: X findings
- High: X findings
- Medium: X findings
- Low: X findings

### Critical Findings

#### [CRITICAL-001] Title
- **Location**: file:line
- **Pattern**: Code snippet
- **Risk**: Description of the vulnerability
- **Remediation**: How to fix
- **Reference**: OWASP link

### High Findings
[...]

OWASP Reference Links

For comprehensive guidance, consult these OWASP cheatsheets directly:

XSS Prevention: https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html
DOM XSS Prevention: https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html
CSRF Prevention: https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html
CSP: https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html
Input Validation: https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html
HTML5 Security: https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html
DOM Clobbering: https://cheatsheetseries.owasp.org/cheatsheets/DOM_Clobbering_Prevention_Cheat_Sheet.html
Node.js Security: https://cheatsheetseries.owasp.org/cheatsheets/Nodejs_Security_Cheat_Sheet.html
NPM Security: https://cheatsheetseries.owasp.org/cheatsheets/NPM_Security_Cheat_Sheet.html
AJAX Security: https://cheatsheetseries.owasp.org/cheatsheets/AJAX_Security_Cheat_Sheet.html
File Upload: https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html
Error Handling: https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html
JWT Security: https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html
User Privacy: https://cheatsheetseries.owasp.org/cheatsheets/User_Privacy_Protection_Cheat_Sheet.html
gRPC Security: https://cheatsheetseries.owasp.org/cheatsheets/gRPC_Security_Cheat_Sheet.html
Weekly Installs
183
Repository
schalkneethling…t-skills
GitHub Stars
3
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail