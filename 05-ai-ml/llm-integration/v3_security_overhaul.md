---
rating: ⭐⭐
title: v3 security overhaul
url: https://skills.sh/ruvnet/ruflo/v3-security-overhaul
---

# v3 security overhaul

skills/ruvnet/ruflo/V3 Security Overhaul
V3 Security Overhaul
Installation
$ npx skills add https://github.com/ruvnet/ruflo --skill 'V3 Security Overhaul'
SKILL.md
V3 Security Overhaul
What This Skill Does

Orchestrates comprehensive security overhaul for claude-flow v3, addressing critical vulnerabilities and establishing security-first development practices using specialized v3 security agents.

Quick Start
# Initialize V3 security domain (parallel)
Task("Security architecture", "Design v3 threat model and security boundaries", "v3-security-architect")
Task("CVE remediation", "Fix CVE-1, CVE-2, CVE-3 critical vulnerabilities", "security-auditor")
Task("Security testing", "Implement TDD London School security framework", "test-architect")

Critical Security Fixes
CVE-1: Vulnerable Dependencies
npm update @anthropic-ai$claude-code@^2.0.31
npm audit --audit-level high

CVE-2: Weak Password Hashing
// ❌ Old: SHA-256 with hardcoded salt
const hash = crypto.createHash('sha256').update(password + salt).digest('hex');

// ✅ New: bcrypt with 12 rounds
import bcrypt from 'bcrypt';
const hash = await bcrypt.hash(password, 12);

CVE-3: Hardcoded Credentials
// ✅ Generate secure random credentials
const apiKey = crypto.randomBytes(32).toString('hex');

Security Patterns
Input Validation (Zod)
import { z } from 'zod';

const TaskSchema = z.object({
  taskId: z.string().uuid(),
  content: z.string().max(10000),
  agentType: z.enum(['security', 'core', 'integration'])
});

Path Sanitization
function securePath(userPath: string, allowedPrefix: string): string {
  const resolved = path.resolve(allowedPrefix, userPath);
  if (!resolved.startsWith(path.resolve(allowedPrefix))) {
    throw new SecurityError('Path traversal detected');
  }
  return resolved;
}

Safe Command Execution
import { execFile } from 'child_process';

// ✅ Safe: No shell interpretation
const { stdout } = await execFile('git', [userInput], { shell: false });

Success Metrics
Security Score: 90/100 (npm audit + custom scans)
CVE Resolution: 100% of critical vulnerabilities fixed
Test Coverage: >95% security-critical code
Implementation: All secure patterns documented and tested
Weekly Installs
–
Repository
ruvnet/ruflo
GitHub Stars
35.8K
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass