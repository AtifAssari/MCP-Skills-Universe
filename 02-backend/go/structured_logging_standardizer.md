---
title: structured-logging-standardizer
url: https://skills.sh/patricio0312rev/skills/structured-logging-standardizer
---

# structured-logging-standardizer

skills/patricio0312rev/skills/structured-logging-standardizer
structured-logging-standardizer
Installation
$ npx skills add https://github.com/patricio0312rev/skills --skill structured-logging-standardizer
SKILL.md
Structured Logging Standardizer

Implement consistent, queryable, correlated logs.

Log Schema
interface LogEntry {
  timestamp: string; // ISO 8601
  level: "debug" | "info" | "warn" | "error" | "fatal";
  message: string;
  service: string;
  environment: string;

  // Request context
  requestId?: string;
  traceId?: string;
  userId?: string;

  // Additional context
  [key: string]: any;
}

Request ID Middleware
import { v4 as uuidv4 } from "uuid";

app.use((req, res, next) => {
  // Generate or use existing request ID
  req.id = req.headers["x-request-id"] || uuidv4();

  // Add to response headers
  res.setHeader("x-request-id", req.id);

  // Store in async local storage
  asyncLocalStorage.run(new Map(), () => {
    asyncLocalStorage.getStore()?.set("requestId", req.id);
    next();
  });
});

// Logger with request context
const logger = pino({
  mixin() {
    return {
      requestId: asyncLocalStorage.getStore()?.get("requestId"),
    };
  },
});

Standardized Logger
class StandardLogger {
  private logger = pino();

  info(message: string, context?: Record<string, any>) {
    this.logger.info(
      {
        ...this.getContext(),
        ...context,
      },
      message
    );
  }

  error(message: string, error?: Error, context?: Record<string, any>) {
    this.logger.error(
      {
        ...this.getContext(),
        ...context,
        error: {
          message: error?.message,
          stack: error?.stack,
          name: error?.name,
        },
      },
      message
    );
  }

  private getContext() {
    return {
      requestId: asyncLocalStorage.getStore()?.get("requestId"),
      userId: asyncLocalStorage.getStore()?.get("userId"),
    };
  }
}

Best Practices
// ✅ DO: Structured fields
logger.info({ userId: '123', action: 'purchase', amount: 99.99 }, 'Purchase completed');

// ❌ DON'T: String interpolation
logger.info(\`User 123 purchased for $99.99\`);

// ✅ DO: Consistent field names
logger.info({ duration_ms: 150 }, 'Request completed');

// ❌ DON'T: Inconsistent naming
logger.info({ durationMs: 150 }, 'Request done');

Output Checklist
 Request ID middleware
 Structured log schema
 Correlation IDs
 Standardized logger
 Best practices documented ENDFILE
Weekly Installs
92
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