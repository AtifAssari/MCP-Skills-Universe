---
rating: ⭐⭐
title: input-validation-sanitization-auditor
url: https://skills.sh/patricio0312rev/skills/input-validation-sanitization-auditor
---

# input-validation-sanitization-auditor

skills/patricio0312rev/skills/input-validation-sanitization-auditor
input-validation-sanitization-auditor
Installation
$ npx skills add https://github.com/patricio0312rev/skills --skill input-validation-sanitization-auditor
SKILL.md
Input Validation & Sanitization Auditor

Prevent injection attacks through proper input handling.

XSS Prevention
// ❌ DANGEROUS: Direct HTML injection
app.get("/search", (req, res) => {
  res.send(`<h1>Results for: ${req.query.q}</h1>`); // XSS!
});

// ✅ SAFE: Properly escaped
import { escape } from "html-escaper";

app.get("/search", (req, res) => {
  res.send(`<h1>Results for: ${escape(req.query.q)}</h1>`);
});

// ✅ BETTER: Template engine with auto-escaping
res.render("search", { query: req.query.q }); // EJS/Pug escape by default

SQL Injection Prevention
// ❌ DANGEROUS: String concatenation
const userId = req.params.id;
const query = `SELECT * FROM users WHERE id = '${userId}'`; // SQL Injection!
db.query(query);

// ✅ SAFE: Parameterized queries
db.query("SELECT * FROM users WHERE id = $1", [userId]);

// ✅ BEST: ORM (Prisma)
await prisma.user.findUnique({ where: { id: userId } });

Input Validation Schema
import { z } from "zod";

const userSchema = z.object({
  email: z.string().email().max(255),
  password: z.string().min(12).max(128),
  age: z.number().int().min(13).max(120),
  website: z.string().url().optional(),
});

app.post("/register", async (req, res) => {
  try {
    const validated = userSchema.parse(req.body);
    await createUser(validated);
    res.json({ success: true });
  } catch (error) {
    res.status(400).json({ error: error.errors });
  }
});

Output Checklist
 XSS prevention (escaping, CSP)
 SQL injection prevention (parameterized queries)
 Command injection prevention
 Input validation schemas
 Output encoding
 Sanitization libraries
 Security tests ENDFILE
Weekly Installs
98
Repository
patricio0312rev/skills
GitHub Stars
35
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass