---
title: timeout-prevention
url: https://skills.sh/jackspace/claudeskillz/timeout-prevention
---

# timeout-prevention

skills/jackspace/claudeskillz/timeout-prevention
timeout-prevention
Installation
$ npx skills add https://github.com/jackspace/claudeskillz --skill timeout-prevention
SKILL.md
Timeout Prevention Skill

Expert strategies for preventing request timeouts in Claude Code by breaking down long operations into manageable chunks with progress tracking and recovery mechanisms.

When to Use This Skill

Use when:

Performing bulk operations (100+ files, repos, etc.)
Running long commands (>60 seconds)
Processing large datasets
Downloading multiple files sequentially
Executing complex multi-step workflows
Working with slow external APIs
Any operation that risks timing out
Understanding Timeout Limits
Claude Code Timeout Behavior
Default Tool Timeout: 120 seconds (2 minutes)
Request Timeout: Entire response cycle
What Causes Timeouts:
Long-running bash commands
Large file operations
Sequential processing of many items
Network operations without proper timeout settings
Blocking operations without progress
Core Prevention Strategies
1. Task Chunking

Break large operations into smaller batches:

# ❌ BAD: Process all 1000 files at once
for file in $(find . -name "*.txt"); do
    process_file "$file"
done

# ✅ GOOD: Process in batches of 10
find . -name "*.txt" | head -10 | while read file; do
    process_file "$file"
done
# Then process next 10, etc.

2. Progress Checkpoints

Save progress to resume if interrupted:

# Create checkpoint file
CHECKPOINT_FILE="progress.txt"

# Save completed items
echo "completed_item_1" >> "$CHECKPOINT_FILE"

# Skip already completed items
if grep -q "completed_item_1" "$CHECKPOINT_FILE"; then
    echo "Skipping already processed item"
fi

3. Background Processes

Run long operations in background:

# Start long-running process in background
long_command > output.log 2>&1 &
echo $! > pid.txt

# Check status later
if ps -p $(cat pid.txt) > /dev/null; then
    echo "Still running"
else
    echo "Completed"
    cat output.log
fi

4. Incremental Processing

Process and report incrementally:

# Process items one at a time with status updates
TOTAL=100
for i in $(seq 1 10); do  # First 10 of 100
    process_item $i
    echo "Progress: $i/$TOTAL"
done
# Continue with next 10 in subsequent calls

5. Timeout Configuration

Set explicit timeouts for commands:

# Use timeout command
timeout 60s long_command || echo "Command timed out"

# Set timeout in tool calls
yt-dlp --socket-timeout 30 "URL"
git clone --depth 1 --timeout 60 "URL"

Practical Patterns
Pattern 1: Batch File Processing
# Define batch size
BATCH_SIZE=10
OFFSET=${1:-0}  # Accept offset as parameter

# Process batch
find . -name "*.jpg" | tail -n +$((OFFSET + 1)) | head -$BATCH_SIZE | while read file; do
    convert "$file" -resize 800x600 "thumbnails/$(basename $file)"
    echo "Processed: $file"
done

# Report next offset
NEXT_OFFSET=$((OFFSET + BATCH_SIZE))
echo "Next batch: Run with offset $NEXT_OFFSET"


Usage:

# First batch
./process.sh 0

# Next batch
./process.sh 10

# Continue...
./process.sh 20

Pattern 2: Repository Cloning with Checkpoints
#!/bin/bash
REPOS_FILE="repos.txt"
CHECKPOINT="downloaded.txt"

# Read repos, skip already downloaded
while read repo; do
    # Check if already downloaded
    if grep -q "$repo" "$CHECKPOINT" 2>/dev/null; then
        echo "✓ Skipping $repo (already downloaded)"
        continue
    fi

    # Clone with timeout
    echo "Downloading $repo..."
    if timeout 60s git clone --depth 1 "$repo" 2>/dev/null; then
        echo "$repo" >> "$CHECKPOINT"
        echo "✓ Downloaded $repo"
    else
        echo "✗ Failed: $repo"
    fi
done < <(head -5 "$REPOS_FILE")  # Only 5 at a time

echo "Processed 5 repos. Check $CHECKPOINT for status."

Pattern 3: Progress-Tracked Downloads
#!/bin/bash
URLS_FILE="urls.txt"
PROGRESS_FILE="download_progress.json"

# Initialize progress
[ ! -f "$PROGRESS_FILE" ] && echo '{"completed": 0, "total": 0}' > "$PROGRESS_FILE"

# Get current progress
COMPLETED=$(jq -r '.completed' "$PROGRESS_FILE")
TOTAL=$(wc -l < "$URLS_FILE")

# Download next batch (5 at a time)
BATCH_SIZE=5
tail -n +$((COMPLETED + 1)) "$URLS_FILE" | head -$BATCH_SIZE | while read url; do
    echo "Downloading: $url"
    if yt-dlp --socket-timeout 30 "$url"; then
        COMPLETED=$((COMPLETED + 1))
        echo "{\"completed\": $COMPLETED, \"total\": $TOTAL}" > "$PROGRESS_FILE"
    fi
done

# Report progress
COMPLETED=$(jq -r '.completed' "$PROGRESS_FILE")
echo "Progress: $COMPLETED/$TOTAL"
[ $COMPLETED -lt $TOTAL ] && echo "Run again to continue."

Pattern 4: Parallel Execution with Rate Limiting
#!/bin/bash
MAX_PARALLEL=3
COUNT=0

for item in $(seq 1 15); do
    # Start background job
    (
        process_item $item
        echo "Completed: $item"
    ) &

    COUNT=$((COUNT + 1))

    # Wait when reaching max parallel
    if [ $COUNT -ge $MAX_PARALLEL ]; then
        wait -n  # Wait for any job to finish
        COUNT=$((COUNT - 1))
    fi

    # Rate limiting
    sleep 0.5
done

# Wait for remaining jobs
wait
echo "All items processed"

Pattern 5: Resumable State Machine
#!/bin/bash
STATE_FILE="workflow_state.txt"

# Read current state (default: START)
STATE=$(cat "$STATE_FILE" 2>/dev/null || echo "START")

case $STATE in
    START)
        echo "Phase 1: Initialization"
        initialize_project
        echo "PHASE1" > "$STATE_FILE"
        echo "Run again to continue to Phase 2"
        ;;
    PHASE1)
        echo "Phase 2: Processing (Batch 1 of 3)"
        process_batch_1
        echo "PHASE2" > "$STATE_FILE"
        echo "Run again for Phase 3"
        ;;
    PHASE2)
        echo "Phase 3: Processing (Batch 2 of 3)"
        process_batch_2
        echo "PHASE3" > "$STATE_FILE"
        echo "Run again for Phase 4"
        ;;
    PHASE3)
        echo "Phase 4: Processing (Batch 3 of 3)"
        process_batch_3
        echo "PHASE4" > "$STATE_FILE"
        echo "Run again for finalization"
        ;;
    PHASE4)
        echo "Phase 5: Finalization"
        finalize_project
        echo "COMPLETE" > "$STATE_FILE"
        echo "Workflow complete!"
        ;;
    COMPLETE)
        echo "Workflow already completed"
        ;;
esac

Command Optimization
Optimize Bash Commands
# ❌ SLOW: Multiple commands sequentially
git clone repo1
git clone repo2
git clone repo3

# ✅ FAST: Parallel with wait
git clone repo1 &
git clone repo2 &
git clone repo3 &
wait

Optimize File Operations
# ❌ SLOW: Process one file at a time
for file in *.txt; do
    cat "$file" | process > "output/$file"
done

# ✅ FAST: Parallel processing
for file in *.txt; do
    cat "$file" | process > "output/$file" &
done
wait

Optimize Network Calls
# ❌ SLOW: Sequential API calls
for id in {1..100}; do
    curl "https://api.example.com/item/$id"
done

# ✅ FAST: Batch API call
curl "https://api.example.com/items?ids=1,2,3,4,5"

Claude Code Integration
Strategy 1: Multi-Turn Workflow

Instead of one long operation, break into multiple turns:

Turn 1:

Process first 10 repositories and report progress


Turn 2:

Process next 10 repositories (11-20)


Turn 3:

Process final batch and generate report

Strategy 2: Status Check Pattern
# Turn 1: Start background process
./long_operation.sh > output.log 2>&1 &
echo $! > pid.txt
echo "Started background process"

# Turn 2: Check status
if ps -p $(cat pid.txt) > /dev/null; then
    echo "Still running... Check again"
    tail -20 output.log
else
    echo "Completed!"
    cat output.log
fi

Strategy 3: Incremental Results

Report partial results as you go:

echo "=== Batch 1 Results ==="
process_batch_1
echo ""
echo "=== Batch 2 Results ==="
process_batch_2

Error Handling
Graceful Degradation
# Try operation with timeout, fallback if fails
if timeout 30s expensive_operation; then
    echo "Operation completed"
else
    echo "Operation timed out, using cached result"
    cat cached_result.txt
fi

Retry Logic
MAX_RETRIES=3
RETRY_COUNT=0

while [ $RETRY_COUNT -lt $MAX_RETRIES ]; do
    if timeout 60s risky_operation; then
        echo "Success!"
        break
    else
        RETRY_COUNT=$((RETRY_COUNT + 1))
        echo "Attempt $RETRY_COUNT failed, retrying..."
        sleep 5
    fi
done

Best Practices
✅ DO
Chunk Large Operations: Process 5-10 items at a time
Save Progress: Use checkpoint files
Report Incrementally: Show results as you go
Use Timeouts: Set explicit timeout values
Parallelize Wisely: 3-5 concurrent operations max
Enable Resume: Make operations resumable
Monitor Progress: Show completion percentage
Background Long Tasks: Use & for async operations
❌ DON'T
Don't Process Everything: Batch large datasets
Don't Block Forever: Always set timeouts
Don't Ignore State: Save progress between runs
Don't Go Silent: Report progress regularly
Don't Retry Infinitely: Limit retry attempts
Don't Over-Parallelize: Limit concurrent operations
Don't Assume Success: Always check return codes
Don't Skip Cleanup: Clean up temp files
Common Scenarios
Scenario 1: Downloading 100 YouTube Videos
# DON'T do this (will timeout)
yt-dlp -a urls.txt  # 100 URLs

# DO this instead
head -5 urls.txt | yt-dlp -a -
# Then process next 5 in another turn

Scenario 2: Cloning 50 Repositories
# DON'T
for repo in $(cat repos.txt); do
    git clone $repo
done

# DO
head -5 repos.txt | while read repo; do
    timeout 60s git clone --depth 1 $repo
done
# Continue with tail -n +6 in next turn

Scenario 3: Processing 1000 Images
# DON'T
for img in *.jpg; do
    convert $img processed/$img
done

# DO
find . -name "*.jpg" | head -20 | xargs -P 4 -I {} convert {} processed/{}
# Process next 20 in subsequent turn

Monitoring and Debugging
Track Execution Time
start_time=$(date +%s)
# ... operations ...
end_time=$(date +%s)
duration=$((end_time - start_time))
echo "Duration: ${duration}s"

Log Everything
LOG_FILE="operation.log"
{
    echo "Started at $(date)"
    perform_operations
    echo "Completed at $(date)"
} | tee -a "$LOG_FILE"

Progress Indicators
TOTAL=100
for i in $(seq 1 10); do
    process_item $i
    echo -ne "Progress: $i/$TOTAL\r"
done
echo ""

Recovery Strategies
Checkpoint-Based Recovery
# Check last successful checkpoint
LAST_CHECKPOINT=$(cat .checkpoint 2>/dev/null || echo 0)
echo "Resuming from item $LAST_CHECKPOINT"

# Continue from checkpoint
for i in $(seq $((LAST_CHECKPOINT + 1)) $((LAST_CHECKPOINT + 10))); do
    process_item $i && echo $i > .checkpoint
done

Transaction-Like Operations
# Create temporary workspace
TEMP_DIR=$(mktemp -d)
trap "rm -rf $TEMP_DIR" EXIT

# Work in temp, only commit on success
cd $TEMP_DIR
perform_operations
if [ $? -eq 0 ]; then
    mv $TEMP_DIR/results ~/final/
fi


Version: 1.0.0 Last Updated: 2025-11-07 Key Principle: Break long operations into manageable chunks with progress tracking and resumability

Weekly Installs
48
Repository
jackspace/claudeskillz
GitHub Stars
14
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn