---
title: sql-injection-prevention
url: https://skills.sh/aj-geddes/useful-ai-prompts/sql-injection-prevention
---

# sql-injection-prevention

skills/aj-geddes/useful-ai-prompts/sql-injection-prevention
sql-injection-prevention
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill sql-injection-prevention
SKILL.md
SQL Injection Prevention
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Implement comprehensive SQL injection prevention using prepared statements, parameterized queries, ORM best practices, and input validation.

When to Use
Database query development
Legacy code security review
Security audit remediation
API endpoint development
User input handling
Dynamic query generation
Quick Start

Minimal working example:

// secure-db.js
const { Pool } = require("pg");

class SecureDatabase {
  constructor() {
    this.pool = new Pool({
      host: process.env.DB_HOST,
      database: process.env.DB_NAME,
      user: process.env.DB_USER,
      password: process.env.DB_PASSWORD,
      max: 20,
      idleTimeoutMillis: 30000,
      connectionTimeoutMillis: 2000,
    });
  }

  /**
   * ✅ SECURE: Parameterized query
   */
  async getUserById(userId) {
    const query = "SELECT * FROM users WHERE id = $1";
    const values = [userId];

    try {
      const result = await this.pool.query(query, values);
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Node.js with PostgreSQL	Node.js with PostgreSQL
Python with SQLAlchemy ORM	Python with SQLAlchemy ORM
Java JDBC with Prepared Statements	Java JDBC with Prepared Statements
Input Validation & Sanitization	Input Validation & Sanitization
Best Practices
✅ DO
Use prepared statements ALWAYS
Use ORM frameworks properly
Validate all user inputs
Whitelist dynamic values
Use least privilege DB accounts
Enable query logging
Regular security audits
Use parameterized queries
❌ DON'T
Concatenate user input
Trust client-side validation
Use string formatting for queries
Allow dynamic table/column names
Grant excessive DB permissions
Skip input validation
Weekly Installs
308
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass