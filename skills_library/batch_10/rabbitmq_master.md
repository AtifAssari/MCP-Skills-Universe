---
title: rabbitmq-master
url: https://skills.sh/modra40/claude-codex-skills-directory/rabbitmq-master
---

# rabbitmq-master

skills/modra40/claude-codex-skills-directory/rabbitmq-master
rabbitmq-master
Installation
$ npx skills add https://github.com/modra40/claude-codex-skills-directory --skill rabbitmq-master
SKILL.md
RabbitMQ Master Skill

Expert-level RabbitMQ knowledge for building bulletproof messaging systems.

Quick Reference
Connection Best Practices
# WRONG - Connection per message (kills performance)
def send_bad(msg):
    conn = pika.BlockingConnection(params)  # 7-way TCP handshake + AMQP handshake
    ch = conn.channel()
    ch.basic_publish(...)
    conn.close()

# CORRECT - Connection pooling with heartbeat
import pika
from pika import ConnectionParameters, PlainCredentials

params = ConnectionParameters(
    host='rabbitmq.prod',
    port=5672,
    credentials=PlainCredentials('user', 'pass'),
    heartbeat=60,                    # Detect dead connections
    blocked_connection_timeout=300,  # Handle flow control
    connection_attempts=3,
    retry_delay=5,
    socket_timeout=10,
    stack_timeout=15,
    # CRITICAL: TCP keepalive untuk cloud/NAT environments
    tcp_options={'TCP_KEEPIDLE': 60, 'TCP_KEEPINTVL': 10, 'TCP_KEEPCNT': 3}
)

# Use connection pool - see scripts/connection_pool.py

Channel Best Practices
# Channels are NOT thread-safe - use 1 channel per thread
# Channels are cheap - create many, but not per message

# OPTIMAL: Dedicated channels per purpose
publish_channel = conn.channel()
publish_channel.confirm_delivery()  # Enable publisher confirms

consume_channel = conn.channel()
consume_channel.basic_qos(prefetch_count=50)  # Tuned prefetch

Core Patterns
1. Reliable Publishing (Publisher Confirms)
# Synchronous confirms (simple, slower)
channel.confirm_delivery()
try:
    channel.basic_publish(
        exchange='orders',
        routing_key='new',
        body=json.dumps(order),
        properties=pika.BasicProperties(
            delivery_mode=2,           # Persistent
            content_type='application/json',
            message_id=str(uuid4()),   # Idempotency key
            timestamp=int(time.time()),
            headers={'retry_count': 0}
        ),
        mandatory=True  # Return if unroutable
    )
except pika.exceptions.UnroutableError:
    handle_unroutable()
except pika.exceptions.NackError:
    handle_nack()

# Asynchronous confirms (complex, 10x faster) - see scripts/async_publisher.py

2. Reliable Consuming
def callback(ch, method, properties, body):
    try:
        # ALWAYS process idempotently using message_id
        if is_duplicate(properties.message_id):
            ch.basic_ack(method.delivery_tag)
            return
        
        process_message(body)
        mark_processed(properties.message_id)
        ch.basic_ack(method.delivery_tag)
        
    except RecoverableError as e:
        # Requeue with exponential backoff via DLX
        retry_count = (properties.headers or {}).get('retry_count', 0)
        if retry_count < MAX_RETRIES:
            republish_with_delay(ch, body, retry_count + 1)
            ch.basic_ack(method.delivery_tag)  # Ack original
        else:
            ch.basic_nack(method.delivery_tag, requeue=False)  # To DLQ
            
    except FatalError:
        # Permanent failure - dead letter immediately
        ch.basic_nack(method.delivery_tag, requeue=False)

channel.basic_qos(prefetch_count=50)  # CRITICAL - tune this!
channel.basic_consume(queue='orders', on_message_callback=callback)

3. Dead Letter Exchange Pattern
# DLX captures: rejected, expired, queue-full messages
channel.exchange_declare('dlx.exchange', 'direct', durable=True)
channel.queue_declare('dlq.orders', durable=True)
channel.queue_bind('dlq.orders', 'dlx.exchange', 'orders')

# Main queue with DLX
channel.queue_declare(
    'orders',
    durable=True,
    arguments={
        'x-dead-letter-exchange': 'dlx.exchange',
        'x-dead-letter-routing-key': 'orders',
        'x-message-ttl': 86400000,     # 24h max age
        'x-max-length': 1000000,       # Max 1M messages
        'x-overflow': 'reject-publish-dlx'  # DLX on overflow
    }
)

4. Delayed/Scheduled Messages
# Method 1: Plugin (rabbitmq_delayed_message_exchange)
channel.exchange_declare(
    'delayed.exchange',
    'x-delayed-message',
    arguments={'x-delayed-type': 'direct'}
)

channel.basic_publish(
    exchange='delayed.exchange',
    routing_key='scheduled',
    body=payload,
    properties=pika.BasicProperties(
        headers={'x-delay': 60000}  # 60 seconds delay
    )
)

# Method 2: TTL + DLX chain (no plugin needed) - see references/patterns.md

5. Priority Queues
# CAUTION: Priority queues have overhead, use sparingly
channel.queue_declare(
    'priority.orders',
    durable=True,
    arguments={
        'x-max-priority': 10,  # 1-10 priorities, keep low!
        'x-queue-type': 'classic'  # Not supported on quorum
    }
)

# Publishing with priority
channel.basic_publish(
    exchange='',
    routing_key='priority.orders',
    body=payload,
    properties=pika.BasicProperties(
        delivery_mode=2,
        priority=8  # Higher = more important
    )
)

High Availability
Quorum Queues (Recommended for HA)
# Raft-based replication - ALWAYS use for critical queues
channel.queue_declare(
    'orders.quorum',
    durable=True,
    arguments={
        'x-queue-type': 'quorum',
        'x-quorum-initial-group-size': 3,  # Replicas
        'x-delivery-limit': 5,             # Auto-DLQ after 5 redeliveries
        'x-dead-letter-exchange': 'dlx',
        'x-dead-letter-strategy': 'at-least-once'  # Safe DLQ
    }
)

Stream Queues (High-throughput, replay)
# Kafka-like streams in RabbitMQ 3.9+
channel.queue_declare(
    'events.stream',
    durable=True,
    arguments={
        'x-queue-type': 'stream',
        'x-max-length-bytes': 20_000_000_000,  # 20GB retention
        'x-max-age': '7D',                      # 7 days retention
        'x-stream-max-segment-size-bytes': 500_000_000
    }
)

# Consuming from offset
channel.basic_qos(prefetch_count=100)
channel.basic_consume(
    'events.stream',
    callback,
    arguments={
        'x-stream-offset': 'first'  # first|last|next|timestamp|offset
    }
)

Performance Tuning
Prefetch Optimization Formula
optimal_prefetch = (avg_processing_time_ms / avg_network_rtt_ms) * consumer_count * 1.5

Examples:
- Same datacenter (1ms RTT), 50ms processing, 1 consumer: (50/1) * 1 * 1.5 = 75
- Cross-region (50ms RTT), 50ms processing, 1 consumer: (50/50) * 1 * 1.5 = 2
- Batch processing (500ms), local: (500/1) * 1 * 1.5 = 750

Batch Publishing (10x throughput)
# Single publish: ~2000 msg/s
# Batch publish: ~20000+ msg/s

def batch_publish(channel, messages, batch_size=100):
    channel.confirm_delivery()
    
    for i in range(0, len(messages), batch_size):
        batch = messages[i:i+batch_size]
        for msg in batch:
            channel.basic_publish(
                exchange='batch.exchange',
                routing_key=msg['key'],
                body=msg['body'],
                properties=pika.BasicProperties(delivery_mode=2)
            )
        # Confirm entire batch
        channel.wait_for_confirms(timeout=30)

Memory Management
%% rabbitmq.conf - Production settings
vm_memory_high_watermark.relative = 0.6
vm_memory_high_watermark_paging_ratio = 0.75
disk_free_limit.absolute = 5GB

%% Queue memory limits
queue_index_embed_msgs_below = 4096
lazy_queue_explicit_gc_run_operation_threshold = 1000

%% Flow control tuning
credit_flow_default_credit = {400, 200}

Monitoring & Alerting
Critical Metrics
# Prometheus alerts - see references/monitoring.md for full config
- alert: RabbitMQHighMemory
  expr: rabbitmq_process_resident_memory_bytes / rabbitmq_resident_memory_limit_bytes > 0.8
  
- alert: RabbitMQQueueBacklog
  expr: rabbitmq_queue_messages_ready > 100000
  
- alert: RabbitMQConsumerUtilization
  expr: rabbitmq_queue_consumer_utilisation < 0.5  # Consumers idle = problem
  
- alert: RabbitMQUnackedMessages
  expr: rabbitmq_queue_messages_unacknowledged > 10000
  
- alert: RabbitMQDiskAlarm
  expr: rabbitmq_alarms_free_disk_space_watermark == 1

Health Check Script
# See scripts/health_check.sh for complete implementation
rabbitmqctl node_health_check
rabbitmqctl cluster_status
rabbitmq-diagnostics check_port_connectivity
rabbitmq-diagnostics check_running
rabbitmq-diagnostics check_local_alarms

Anti-Patterns to Avoid
Anti-Pattern	Problem	Solution
Connection per message	1000x overhead	Connection pool
No prefetch (unlimited)	Memory explosion	Tune prefetch_count
auto_ack=True	Message loss	Manual ack after processing
Classic queues for HA	Split-brain risk	Use Quorum queues
Polling with basic_get	CPU waste, latency	Use basic_consume
Giant messages (>128KB)	Memory pressure	External storage + reference
No message TTL	Queue bloat	Set x-message-ttl
Unbounded queue growth	Disk/memory full	x-max-length + overflow policy
File Reference
scripts/connection_pool.py - Production-grade connection pooling
scripts/async_publisher.py - High-throughput async publisher with confirms
scripts/consumer_template.py - Robust consumer with retry logic
scripts/health_check.sh - Comprehensive health check script
scripts/queue_migrate.py - Zero-downtime queue migration tool
scripts/dlq_processor.py - Dead letter queue reprocessing
references/patterns.md - Advanced messaging patterns deep-dive
references/clustering.md - HA clustering configuration
references/security.md - Security hardening guide
references/monitoring.md - Full monitoring setup
references/troubleshooting.md - Problem diagnosis guide
references/performance.md - Performance tuning deep-dive
assets/rabbitmq.conf - Production configuration template
assets/docker-compose.yml - Development cluster setup
assets/k8s/ - Kubernetes deployment manifests
Weekly Installs
33
Repository
modra40/claude-…irectory
GitHub Stars
5
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass