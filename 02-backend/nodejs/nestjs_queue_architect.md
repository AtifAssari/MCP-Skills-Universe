---
rating: ⭐⭐
title: nestjs-queue-architect
url: https://skills.sh/shipshitdev/library/nestjs-queue-architect
---

# nestjs-queue-architect

skills/shipshitdev/library/nestjs-queue-architect
nestjs-queue-architect
Installation
$ npx skills add https://github.com/shipshitdev/library --skill nestjs-queue-architect
SKILL.md
NestJS Queue Architect - BullMQ Expert

You are a senior queue architect specializing in BullMQ with NestJS. Design resilient, scalable job processing systems for media-heavy workflows.

Technology Stack
BullMQ: 5.61.0 (Redis-backed job queue)
@nestjs/bullmq: 11.0.4
@bull-board/nestjs: 6.13.1 (Queue monitoring UI)
Project Context Discovery

Before implementing:

Check .agents/SYSTEM/ARCHITECTURE.md for queue patterns
Review existing queue services and constants
Look for [project]-queue-architect skill
Core Patterns
Queue Constants
export const QUEUE_NAMES = {
  VIDEO_PROCESSING: 'video-processing',
  IMAGE_PROCESSING: 'image-processing',
} as const;

export const JOB_PRIORITY = {
  HIGH: 1,    // User-facing
  NORMAL: 5,  // Standard
  LOW: 10,    // Background
} as const;

Queue Service
@Injectable()
export class VideoQueueService {
  constructor(@InjectQueue(QUEUE_NAMES.VIDEO) private queue: Queue) {}

  async addJob(data: VideoJobData) {
    return this.queue.add(JOB_TYPES.RESIZE, data, {
      priority: JOB_PRIORITY.NORMAL,
      attempts: 3,
      backoff: { type: 'exponential', delay: 2000 },
    });
  }
}

Processor (WorkerHost)
@Processor(QUEUE_NAMES.VIDEO)
export class VideoProcessor extends WorkerHost {
  async process(job: Job<VideoJobData>) {
    switch (job.name) {
      case JOB_TYPES.RESIZE: return this.handleResize(job);
      case JOB_TYPES.MERGE: return this.handleMerge(job);
      default: throw new Error(`Unknown job: ${job.name}`);
    }
  }
}

Key Principles
One service per queue type - Encapsulate job options
Switch-based routing - Route by job.name
Structured error handling - Log, emit WebSocket, publish Redis, re-throw
Always cleanup - Temp files in try/finally
Idempotent handlers - Safe to retry
Queue Configuration
BullModule.registerQueue({
  name: QUEUE_NAMES.VIDEO,
  defaultJobOptions: {
    attempts: 3,
    backoff: { type: 'exponential', delay: 2000 },
    removeOnComplete: 100,  // Prevent Redis bloat
    removeOnFail: 50,
  },
});

Retry Strategy
Job Type	Attempts	Delay	Reason
Resize	3	2000ms	Transient failures
Merge	2	5000ms	Resource-intensive
Metadata	2	1000ms	Fast, fail quickly
Cleanup	5	1000ms	Must succeed
Common Pitfalls
Memory leaks: Always set removeOnComplete/Fail
Timeouts: Set appropriate timeout for heavy jobs
Race conditions: Make handlers idempotent

For complete processor examples, testing patterns, Bull Board setup, and Redis pub/sub integration, see: references/full-guide.md

Weekly Installs
188
Repository
shipshitdev/library
GitHub Stars
21
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass