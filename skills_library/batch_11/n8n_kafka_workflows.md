---
title: n8n-kafka-workflows
url: https://skills.sh/anton-abyzov/specweave/n8n-kafka-workflows
---

# n8n-kafka-workflows

skills/anton-abyzov/specweave/n8n-kafka-workflows
n8n-kafka-workflows
Installation
$ npx skills add https://github.com/anton-abyzov/specweave --skill n8n-kafka-workflows
SKILL.md
n8n Kafka Workflows Skill

Expert knowledge of integrating Apache Kafka with n8n workflow automation platform for no-code/low-code event-driven processing.

What I Know
n8n Kafka Nodes

Kafka Trigger Node (Event Consumer):

Triggers workflow on new Kafka messages
Supports consumer groups
Auto-commit or manual offset management
Multiple topic subscription
Message batching

Kafka Producer Node (Event Publisher):

Sends messages to Kafka topics
Supports key-based partitioning
Header support
Compression (gzip, snappy, lz4)
Batch sending

Configuration:

{
  "credentials": {
    "kafkaApi": {
      "brokers": "localhost:9092",
      "clientId": "n8n-workflow",
      "ssl": false,
      "sasl": {
        "mechanism": "plain",
        "username": "{{$env.KAFKA_USER}}",
        "password": "{{$env.KAFKA_PASSWORD}}"
      }
    }
  }
}

When to Use This Skill

Activate me when you need help with:

n8n Kafka setup ("Configure Kafka trigger in n8n")
Workflow patterns ("Event-driven automation with n8n")
Error handling ("Retry failed Kafka messages")
Integration patterns ("Enrich Kafka events with HTTP API")
Producer configuration ("Send messages to Kafka from n8n")
Consumer groups ("Process Kafka events in parallel")
Common Workflow Patterns
Pattern 1: Event-Driven Processing

Use Case: Process Kafka events with HTTP API enrichment

[Kafka Trigger] → [HTTP Request] → [Transform] → [Database]
     ↓
  orders topic
     ↓
  Get customer data
     ↓
  Merge order + customer
     ↓
  Save to PostgreSQL


n8n Workflow:

Kafka Trigger:

Topic: orders
Consumer Group: order-processor
Offset: latest

HTTP Request (Enrich):

URL: https://api.example.com/customers/{{$json.customerId}}
Method: GET
Headers: Authorization: Bearer {{$env.API_TOKEN}}

Set Node (Transform):

return {
  orderId: $json.order.id,
  customerId: $json.order.customerId,
  customerName: $json.customer.name,
  customerEmail: $json.customer.email,
  total: $json.order.total,
  timestamp: new Date().toISOString()
};


PostgreSQL (Save):

Operation: INSERT
Table: enriched_orders
Columns: Mapped from Set node
Pattern 2: Fan-Out (Publish to Multiple Topics)

Use Case: Single event triggers multiple downstream workflows

[Kafka Trigger] → [Switch] → [Kafka Producer] (topic: high-value-orders)
     ↓                ↓
  orders topic        └─→ [Kafka Producer] (topic: all-orders)
                           └─→ [Kafka Producer] (topic: analytics)


n8n Workflow:

Kafka Trigger: Consume orders
Switch Node: Route by total value
Route 1: total > 1000 → high-value-orders topic
Route 2: Always → all-orders topic
Route 3: Always → analytics topic
Kafka Producer (x3): Send to respective topics
Pattern 3: Retry with Dead Letter Queue (DLQ)

Use Case: Retry failed messages, send to DLQ after 3 attempts

[Kafka Trigger] → [Try/Catch] → [Success] → [Kafka Producer] (topic: processed)
     ↓                ↓
  input topic     [Catch Error]
                       ↓
                  [Increment Retry Count]
                       ↓
                  [If Retry < 3]
                       ↓ Yes
                  [Kafka Producer] (topic: input-retry)
                       ↓ No
                  [Kafka Producer] (topic: dlq)


n8n Workflow:

Kafka Trigger: input topic
Try Node: HTTP Request (may fail)
Catch Node (Error Handler):
Get retry count from message headers
Increment retry count
If retry < 3: Send to input-retry topic
Else: Send to dlq topic
Pattern 4: Batch Processing with Aggregation

Use Case: Aggregate 100 events, send batch to API

[Kafka Trigger] → [Aggregate] → [HTTP Request] → [Kafka Producer]
     ↓               ↓
  events topic   Buffer 100 msgs
                     ↓
                Send batch to API
                     ↓
                Publish results


n8n Workflow:

Kafka Trigger: Enable batching (100 messages)
Aggregate Node: Combine into array
HTTP Request: POST batch
Kafka Producer: Send results
Pattern 5: Change Data Capture (CDC) to Kafka

Use Case: Stream database changes to Kafka

[Cron Trigger] → [PostgreSQL] → [Compare] → [Kafka Producer]
     ↓               ↓              ↓
  Every 1 min    Get new rows   Find diffs
                                    ↓
                              Publish changes


n8n Workflow:

Cron: Every 1 minute
PostgreSQL: SELECT new rows (WHERE updated_at > last_run)
Function Node: Detect changes (INSERT/UPDATE/DELETE)
Kafka Producer: Send CDC events
Best Practices
1. Use Consumer Groups for Parallel Processing

✅ DO:

Workflow Instance 1:
  Consumer Group: order-processor
  Partition: 0, 1, 2

Workflow Instance 2:
  Consumer Group: order-processor
  Partition: 3, 4, 5


❌ DON'T:

// WRONG: No consumer group (all instances get all messages!)
Consumer Group: (empty)

2. Handle Errors with Try/Catch

✅ DO:

[Kafka Trigger]
  ↓
[Try] → [HTTP Request] → [Success Handler]
  ↓
[Catch] → [Error Handler] → [Kafka DLQ]


❌ DON'T:

// WRONG: No error handling (workflow crashes on failure!)
[Kafka Trigger] → [HTTP Request] → [Database]

3. Use Environment Variables for Credentials

✅ DO:

Kafka Brokers: {{$env.KAFKA_BROKERS}}
SASL Username: {{$env.KAFKA_USER}}
SASL Password: {{$env.KAFKA_PASSWORD}}


❌ DON'T:

// WRONG: Hardcoded credentials in workflow!
Kafka Brokers: "localhost:9092"
SASL Username: "admin"
SASL Password: "admin-secret"

4. Set Explicit Partitioning Keys

✅ DO:

Kafka Producer:
  Topic: orders
  Key: {{$json.customerId}}  // Partition by customer
  Message: {{$json}}


❌ DON'T:

// WRONG: No key (random partitioning!)
Kafka Producer:
  Topic: orders
  Message: {{$json}}

5. Monitor Consumer Lag

Setup Prometheus metrics export:

[Cron Trigger] → [Kafka Admin] → [Get Consumer Lag] → [Prometheus]
     ↓               ↓                   ↓
  Every 30s    List consumer groups   Calculate lag
                                           ↓
                                   Push to Pushgateway

Error Handling Strategies
Strategy 1: Exponential Backoff Retry
// Function Node (Calculate Backoff)
const retryCount = $json.headers?.['retry-count'] || 0;
const backoffMs = Math.min(1000 * Math.pow(2, retryCount), 60000); // Max 60 seconds

return {
  retryCount: retryCount + 1,
  backoffMs,
  nextRetryAt: new Date(Date.now() + backoffMs).toISOString()
};


Workflow:

Try processing
On failure: Calculate backoff
Wait (using Wait node)
Retry (send to retry topic)
If max retries reached: Send to DLQ
Strategy 2: Circuit Breaker
// Function Node (Check Failure Rate)
const failures = $json.metrics.failures || 0;
const total = $json.metrics.total || 1;
const failureRate = failures / total;

if (failureRate > 0.5) {
  // Circuit open (too many failures)
  return { circuitState: 'OPEN', skipProcessing: true };
}

return { circuitState: 'CLOSED', skipProcessing: false };


Workflow:

Track success/failure metrics
Calculate failure rate
If >50% failures: Open circuit (stop processing)
Wait 30 seconds
Try single request (half-open)
If success: Close circuit (resume)
Strategy 3: Idempotent Processing
// Function Node (Deduplication)
const messageId = $json.headers?.['message-id'];
const cache = $('Redis').get(messageId);

if (cache) {
  // Already processed, skip
  return { skip: true, reason: 'duplicate' };
}

// Process and cache
await $('Redis').set(messageId, 'processed', { ttl: 3600 });
return { skip: false };


Workflow:

Extract message ID
Check Redis cache
If exists: Skip processing
Process message
Store message ID in cache (1 hour TTL)
Performance Optimization
1. Batch Processing

Enable batching in Kafka Trigger:

Kafka Trigger:
  Batch Size: 100
  Batch Timeout: 5000ms  // Max wait 5 seconds


Process batch:

// Function Node (Batch Transform)
const events = $input.all();
const transformed = events.map(event => ({
  id: event.json.id,
  timestamp: event.json.timestamp,
  processed: true
}));

return transformed;

2. Parallel Processing with Split in Batches
[Kafka Trigger] → [Split in Batches] → [HTTP Request] → [Aggregate]
     ↓                  ↓                     ↓
  1000 events      100 at a time       Parallel API calls
                                            ↓
                                      Combine results

3. Use Compression

Kafka Producer:

Compression: lz4  // Or gzip, snappy
Batch Size: 1000  // Larger batches = better compression

Integration Patterns
Pattern 1: Kafka + HTTP API Enrichment
[Kafka Trigger] → [HTTP Request] → [Transform] → [Kafka Producer]
     ↓                 ↓                ↓
  Raw events      Enrich from API   Combine data
                                         ↓
                                  Publish enriched

Pattern 2: Kafka + Database Sync
[Kafka Trigger] → [PostgreSQL Upsert] → [Kafka Producer]
     ↓                   ↓                    ↓
  CDC events      Update database    Publish success/failure

Pattern 3: Kafka + Email Notifications
[Kafka Trigger] → [If Critical] → [Send Email] → [Kafka Producer]
     ↓                ↓                ↓
  Alerts        severity=critical  Notify admin
                                        ↓
                                   Publish alert sent

Pattern 4: Kafka + Slack Alerts
[Kafka Trigger] → [Transform] → [Slack] → [Kafka Producer]
     ↓               ↓            ↓
  Errors        Format message  Send to #alerts
                                     ↓
                                Publish notification

Testing n8n Workflows
Manual Testing

Test with Sample Data:

Right-click node → "Add Sample Data"
Execute workflow
Check outputs

Test Kafka Producer:

# Consume test topic
kcat -C -b localhost:9092 -t test-output -o beginning


Test Kafka Trigger:

# Produce test message
echo '{"test": "data"}' | kcat -P -b localhost:9092 -t test-input

Automated Testing

n8n CLI:

# Execute workflow with input
n8n execute workflow --file workflow.json --input data.json

# Export workflow
n8n export:workflow --id=123 --output=workflow.json

Common Issues & Solutions
Issue 1: Consumer Lag Building Up

Symptoms: Processing slower than message arrival

Solutions:

Increase consumer group size (parallel processing)
Enable batching (process 100 messages at once)
Optimize HTTP requests (use connection pooling)
Use Split in Batches for parallel processing
Issue 2: Duplicate Messages

Cause: At-least-once delivery, no deduplication

Solution: Add idempotency check:

// Check if message already processed
const messageId = $json.headers?.['message-id'];
const exists = await $('Redis').exists(messageId);

if (exists) {
  return { skip: true };
}

Issue 3: Workflow Execution Timeout

Cause: Long-running HTTP requests

Solution: Use async patterns:

[Kafka Trigger] → [Webhook] → [Wait for Webhook] → [Process Response]
     ↓               ↓
  Trigger job    Async callback
                     ↓
                 Continue workflow

References
n8n Kafka Trigger: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.kafkatrigger/
n8n Kafka Producer: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.kafka/
n8n Best Practices: https://docs.n8n.io/hosting/scaling/best-practices/
Workflow Examples: https://n8n.io/workflows

Invoke me when you need n8n Kafka integration, workflow automation, or event-driven no-code patterns!

Weekly Installs
25
Repository
anton-abyzov/specweave
GitHub Stars
134
First Seen
Jan 22, 2026