---
rating: ⭐⭐
title: cloud-native-patterns
url: https://skills.sh/dralgorhythm/claude-agentic-framework/cloud-native-patterns
---

# cloud-native-patterns

skills/dralgorhythm/claude-agentic-framework/cloud-native-patterns
cloud-native-patterns
Installation
$ npx skills add https://github.com/dralgorhythm/claude-agentic-framework --skill cloud-native-patterns
SKILL.md
Cloud-Native Patterns
Twelve-Factor App
Codebase: One codebase, many deploys
Dependencies: Explicitly declare and isolate
Config: Store in environment
Backing Services: Treat as attached resources
Build, Release, Run: Strictly separate stages
Processes: Execute as stateless processes
Port Binding: Export services via port
Concurrency: Scale out via process model
Disposability: Fast startup and graceful shutdown
Dev/Prod Parity: Keep environments similar
Logs: Treat as event streams
Admin Processes: Run as one-off processes
Resilience Patterns
Circuit Breaker

Prevent cascading failures by failing fast.

class CircuitBreaker {
  private failures = 0;
  private lastFailure?: Date;

  async call<T>(fn: () => Promise<T>): Promise<T> {
    if (this.isOpen()) {
      throw new Error('Circuit is open');
    }
    try {
      const result = await fn();
      this.reset();
      return result;
    } catch (error) {
      this.recordFailure();
      throw error;
    }
  }
}

Retry with Backoff
async function withRetry<T>(
  fn: () => Promise<T>,
  maxRetries = 3
): Promise<T> {
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await fn();
    } catch (error) {
      if (i === maxRetries - 1) throw error;
      await sleep(Math.pow(2, i) * 1000); // Exponential backoff
    }
  }
}

Bulkhead

Isolate failures to prevent system-wide impact.

Service Communication
Synchronous
REST/HTTP
gRPC
Asynchronous
Message queues (RabbitMQ, SQS)
Event streaming (Kafka)
Health Checks
app.get('/health', (req, res) => {
  res.json({ status: 'healthy' });
});

app.get('/ready', async (req, res) => {
  const dbHealthy = await checkDatabase();
  const cacheHealthy = await checkCache();

  if (dbHealthy && cacheHealthy) {
    res.json({ status: 'ready' });
  } else {
    res.status(503).json({ status: 'not ready' });
  }
});

Container Best Practices
One process per container
Use multi-stage builds
Run as non-root user
Use health checks
Keep images small
Weekly Installs
38
Repository
dralgorhythm/cl…ramework
GitHub Stars
76
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass