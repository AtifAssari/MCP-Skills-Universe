---
rating: ⭐⭐
title: bankr x402 sdk - job management
url: https://skills.sh/bankrbot/claude-plugins/bankr-x402-sdk---job-management
---

# bankr x402 sdk - job management

skills/bankrbot/claude-plugins/Bankr x402 SDK - Job Management
Bankr x402 SDK - Job Management
Installation
$ npx skills add https://github.com/bankrbot/claude-plugins --skill 'Bankr x402 SDK - Job Management'
SKILL.md
SDK Job Management

Manage asynchronous jobs: submit, poll, check status, cancel, and batch operations.

SDK Methods
Method	Description	Use Case
promptAndWait()	Submit and wait for result	Recommended for most cases
prompt()	Submit, return immediately	Background processing
pollJob()	Poll until job completes	Manual job tracking
getJobStatus()	Check status once	Custom polling logic
cancelJob()	Cancel pending/processing job	Stop unwanted jobs
Job Lifecycle
pending → processing → completed
                    ↘ failed
                    ↘ cancelled

State	Cancellable	Description
pending	Yes	Awaiting processing
processing	Yes	Actively processing
completed	No	Finished successfully
failed	No	Encountered error
cancelled	No	Cancelled by user
Usage Examples
Recommended: promptAndWait
const result = await client.promptAndWait({
  prompt: "Swap 0.1 ETH to USDC",
  timeout: 60000,
});

if (result.status === "completed") {
  console.log(result.response);
}

Manual Job Control
// Submit without waiting
const { jobId } = await client.prompt({ prompt: "What are trending tokens?" });

// Check status later
const status = await client.getJobStatus(jobId);

// Or poll until complete
const result = await client.pollJob({ jobId, timeout: 60000 });

Cancel Job
const { jobId } = await client.prompt({ prompt: "..." });
await client.cancelJob(jobId);

Batch Processing
const prompts = ["Price of ETH", "Price of BTC", "Price of SOL"];

// Submit all in parallel
const jobs = await Promise.all(
  prompts.map(prompt => client.prompt({ prompt }))
);

// Wait for all to complete
const results = await Promise.all(
  jobs.map(job => client.pollJob({ jobId: job.jobId }))
);

Timing Guidelines
Operation	Typical Time	Recommended Timeout
Price queries	2-5s	15s
Balance checks	2-5s	15s
Token swaps	5-15s	60s
Cross-chain bridges	10-30s	120s
NFT operations	5-15s	60s
Related Skills
sdk-wallet-operations: Client setup and configuration
sdk-capabilities: Full list of supported operations
Weekly Installs
–
Repository
bankrbot/claude-plugins
GitHub Stars
72
First Seen
–