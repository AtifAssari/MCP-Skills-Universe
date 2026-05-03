---
title: session-timeout-handler
url: https://skills.sh/jackspace/claudeskillz/session-timeout-handler
---

# session-timeout-handler

skills/jackspace/claudeskillz/session-timeout-handler
session-timeout-handler
Installation
$ npx skills add https://github.com/jackspace/claudeskillz --skill session-timeout-handler
SKILL.md
Session Timeout Handler

Build resilient workflows that gracefully handle Claude Code's 2-minute timeout constraints.

Overview

Claude Code has a 120-second (2-minute) default tool timeout. This skill provides proven patterns for building workflows that work within this constraint while accomplishing complex, long-running tasks through intelligent chunking, checkpoints, and resumability.

When to Use

Use this skill when:

Processing 50+ items in a loop
Running commands that take >60 seconds
Downloading multiple large files
Performing bulk API calls
Processing large datasets
Running database migrations
Building large projects
Cloning multiple repositories
Any operation risking timeout
Core Strategies
Strategy 1: Batch Processing
#!/bin/bash
# Process items in small batches

ITEMS_FILE="items.txt"
BATCH_SIZE=10
OFFSET=${1:-0}

# Process one batch
tail -n +$((OFFSET + 1)) "$ITEMS_FILE" | head -$BATCH_SIZE | while read item; do
    process_item "$item"
    echo "✓ Processed: $item"
done

# Calculate next offset
NEXT_OFFSET=$((OFFSET + BATCH_SIZE))
TOTAL=$(wc -l < "$ITEMS_FILE")

if [ $NEXT_OFFSET -lt $TOTAL ]; then
    echo ""
    echo "Progress: $NEXT_OFFSET/$TOTAL"
    echo "Run: ./script.sh $NEXT_OFFSET"
else
    echo "✓ All items processed!"
fi

Strategy 2: Checkpoint Resume
#!/bin/bash
# Checkpoint-based workflow

CHECKPOINT_FILE=".progress"
ITEMS=("item1" "item2" "item3" ... "item100")

# Load last checkpoint
LAST_COMPLETED=$(cat "$CHECKPOINT_FILE" 2>/dev/null || echo "-1")
START_INDEX=$((LAST_COMPLETED + 1))

# Process next batch (10 items)
END_INDEX=$((START_INDEX + 10))
[ $END_INDEX -gt ${#ITEMS[@]} ] && END_INDEX=${#ITEMS[@]}

for i in $(seq $START_INDEX $END_INDEX); do
    process "${ITEMS[$i]}"

    # Save checkpoint after each item
    echo "$i" > "$CHECKPOINT_FILE"
    echo "✓ Completed $i/${#ITEMS[@]}"
done

# Check if finished
if [ $END_INDEX -eq ${#ITEMS[@]} ]; then
    echo "🎉 All items complete!"
    rm "$CHECKPOINT_FILE"
else
    echo "📋 Run again to continue from item $((END_INDEX + 1))"
fi

Strategy 3: State Machine
#!/bin/bash
# Multi-phase state machine workflow

STATE_FILE=".workflow_state"
STATE=$(cat "$STATE_FILE" 2>/dev/null || echo "INIT")

case $STATE in
    INIT)
        echo "Phase 1: Initialization"
        setup_environment
        echo "DOWNLOAD" > "$STATE_FILE"
        echo "✓ Phase 1 complete. Run again for Phase 2."
        ;;

    DOWNLOAD)
        echo "Phase 2: Download (batch 1/5)"
        download_batch_1
        echo "PROCESS_1" > "$STATE_FILE"
        echo "✓ Phase 2 complete. Run again for Phase 3."
        ;;

    PROCESS_1)
        echo "Phase 3: Process (batch 1/3)"
        process_batch_1
        echo "PROCESS_2" > "$STATE_FILE"
        echo "✓ Phase 3 complete. Run again for Phase 4."
        ;;

    PROCESS_2)
        echo "Phase 4: Process (batch 2/3)"
        process_batch_2
        echo "PROCESS_3" > "$STATE_FILE"
        echo "✓ Phase 4 complete. Run again for Phase 5."
        ;;

    PROCESS_3)
        echo "Phase 5: Process (batch 3/3)"
        process_batch_3
        echo "FINALIZE" > "$STATE_FILE"
        echo "✓ Phase 5 complete. Run again to finalize."
        ;;

    FINALIZE)
        echo "Phase 6: Finalization"
        cleanup_and_report
        echo "COMPLETE" > "$STATE_FILE"
        echo "🎉 Workflow complete!"
        ;;

    COMPLETE)
        echo "Workflow already completed."
        cat results.txt
        ;;
esac

Strategy 4: Progress Tracking
#!/bin/bash
# Detailed progress tracking with JSON

PROGRESS_FILE="progress.json"

# Initialize progress
init_progress() {
    cat > "$PROGRESS_FILE" << EOF
{
  "total": $1,
  "completed": 0,
  "failed": 0,
  "last_updated": "$(date -Iseconds)",
  "completed_items": []
}
EOF
}

# Update progress
update_progress() {
    local item="$1"
    local status="$2"  # "success" or "failed"

    # Read current progress
    local completed=$(jq -r '.completed' "$PROGRESS_FILE")
    local failed=$(jq -r '.failed' "$PROGRESS_FILE")

    if [ "$status" = "success" ]; then
        completed=$((completed + 1))
    else
        failed=$((failed + 1))
    fi

    # Update JSON
    jq --arg item "$item" \
       --arg status "$status" \
       --arg timestamp "$(date -Iseconds)" \
       --argjson completed "$completed" \
       --argjson failed "$failed" \
       '.completed = $completed |
        .failed = $failed |
        .last_updated = $timestamp |
        .completed_items += [{item: $item, status: $status, timestamp: $timestamp}]' \
       "$PROGRESS_FILE" > "$PROGRESS_FILE.tmp"

    mv "$PROGRESS_FILE.tmp" "$PROGRESS_FILE"
}

# Show progress
show_progress() {
    jq -r '"Progress: \(.completed)/\(.total) completed, \(.failed) failed"' "$PROGRESS_FILE"
}

# Example usage
init_progress 100

for item in $(seq 1 10); do  # Process 10 at a time
    if process_item "$item"; then
        update_progress "item-$item" "success"
    else
        update_progress "item-$item" "failed"
    fi
done

show_progress

Timeout-Safe Patterns
Pattern: Parallel with Rate Limiting
#!/bin/bash
# Process items in parallel with limits

MAX_PARALLEL=3
ACTIVE_JOBS=0

process_with_limit() {
    local item="$1"

    # Wait if at max parallel
    while [ $ACTIVE_JOBS -ge $MAX_PARALLEL ]; do
        wait -n  # Wait for any job to finish
        ACTIVE_JOBS=$((ACTIVE_JOBS - 1))
    done

    # Start background job
    (
        process_item "$item"
        echo "✓ $item"
    ) &

    ACTIVE_JOBS=$((ACTIVE_JOBS + 1))

    # Rate limiting
    sleep 0.5
}

# Process items
for item in $(seq 1 15); do
    process_with_limit "item-$item"
done

# Wait for remaining
wait
echo "✓ All processing complete"

Pattern: Timeout with Fallback
#!/bin/bash
# Try with timeout, fallback to cached/partial result

OPERATION_TIMEOUT=90  # 90 seconds, leave buffer

if timeout ${OPERATION_TIMEOUT}s expensive_operation > result.txt 2>&1; then
    echo "✓ Operation completed"
    cat result.txt
else
    EXIT_CODE=$?

    if [ $EXIT_CODE -eq 124 ]; then
        echo "⚠️  Operation timed out after ${OPERATION_TIMEOUT}s"

        # Use cached result if available
        if [ -f "cached_result.txt" ]; then
            echo "Using cached result from $(stat -c %y cached_result.txt)"
            cat cached_result.txt
        else
            echo "Partial result:"
            cat result.txt
            echo ""
            echo "Run again to continue processing"
        fi
    else
        echo "✗ Operation failed with code $EXIT_CODE"
    fi
fi

Pattern: Incremental Build
#!/bin/bash
# Incremental build with caching

BUILD_CACHE=".build_cache"
SOURCE_DIR="src"

# Track what needs rebuilding
mkdir -p "$BUILD_CACHE"

# Find changed files
find "$SOURCE_DIR" -type f -newer "$BUILD_CACHE/last_build" 2>/dev/null > changed_files.txt

if [ ! -s changed_files.txt ]; then
    echo "✓ No changes detected, using cached build"
    exit 0
fi

# Build only changed files (in batches)
head -10 changed_files.txt | while read file; do
    echo "Building: $file"
    build_file "$file"
done

# Update timestamp
touch "$BUILD_CACHE/last_build"

REMAINING=$(tail -n +11 changed_files.txt | wc -l)
if [ $REMAINING -gt 0 ]; then
    echo ""
    echo "⚠️  $REMAINING files remaining. Run again to continue."
else
    echo "✓ Build complete!"
fi

Real-World Examples
Example 1: Bulk Repository Cloning
#!/bin/bash
# Clone 50 repos without timing out

REPOS_FILE="repos.txt"
CHECKPOINT="cloned.txt"
BATCH_SIZE=5

# Skip already cloned
while read repo_url; do
    # Check checkpoint
    if grep -qF "$repo_url" "$CHECKPOINT" 2>/dev/null; then
        echo "✓ Skip: $repo_url (already cloned)"
        continue
    fi

    REPO_NAME=$(basename "$repo_url" .git)

    # Clone with timeout
    if timeout 60s git clone --depth 1 "$repo_url" "$REPO_NAME" 2>/dev/null; then
        echo "$repo_url" >> "$CHECKPOINT"
        echo "✓ Cloned: $REPO_NAME"
    else
        echo "✗ Failed: $REPO_NAME"
    fi
done < <(head -$BATCH_SIZE "$REPOS_FILE")

# Progress
CLONED=$(wc -l < "$CHECKPOINT" 2>/dev/null || echo 0)
TOTAL=$(wc -l < "$REPOS_FILE")
echo ""
echo "Progress: $CLONED/$TOTAL repositories"
[ $CLONED -lt $TOTAL ] && echo "Run again to continue"

Example 2: Large Dataset Processing
#!/bin/bash
# Process 1000 data files in batches

DATA_DIR="data"
OUTPUT_DIR="processed"
BATCH_NUM=${1:-1}
BATCH_SIZE=20

mkdir -p "$OUTPUT_DIR"

# Calculate offset
OFFSET=$(( (BATCH_NUM - 1) * BATCH_SIZE ))

# Process batch
find "$DATA_DIR" -name "*.csv" | sort | tail -n +$((OFFSET + 1)) | head -$BATCH_SIZE | while read file; do
    FILENAME=$(basename "$file")
    OUTPUT="$OUTPUT_DIR/${FILENAME%.csv}.json"

    echo "Processing: $FILENAME"
    process_csv_to_json "$file" > "$OUTPUT"
    echo "✓ Created: $OUTPUT"
done

# Report progress
TOTAL=$(find "$DATA_DIR" -name "*.csv" | wc -l)
PROCESSED=$(find "$OUTPUT_DIR" -name "*.json" | wc -l)

echo ""
echo "Batch $BATCH_NUM complete"
echo "Progress: $PROCESSED/$TOTAL files"

if [ $PROCESSED -lt $TOTAL ]; then
    NEXT_BATCH=$((BATCH_NUM + 1))
    echo "Next: ./script.sh $NEXT_BATCH"
else
    echo "🎉 All files processed!"
fi

Example 3: API Rate-Limited Scraping
#!/bin/bash
# Scrape API with rate limits and timeouts

API_IDS="ids.txt"
OUTPUT_DIR="api_data"
CHECKPOINT=".api_checkpoint"

mkdir -p "$OUTPUT_DIR"

# Load last checkpoint
LAST_ID=$(cat "$CHECKPOINT" 2>/dev/null || echo "0")

# Process next 10 IDs
grep -A 10 "^$LAST_ID$" "$API_IDS" | tail -n +2 | head -10 | while read id; do
    echo "Fetching ID: $id"

    # API call with timeout
    if timeout 30s curl -s "https://api.example.com/data/$id" > "$OUTPUT_DIR/$id.json"; then
        echo "$id" > "$CHECKPOINT"
        echo "✓ Saved: $id.json"
    else
        echo "✗ Failed: $id"
    fi

    # Rate limiting (100ms between requests)
    sleep 0.1
done

# Progress
TOTAL=$(wc -l < "$API_IDS")
COMPLETED=$(find "$OUTPUT_DIR" -name "*.json" | wc -l)

echo ""
echo "Progress: $COMPLETED/$TOTAL IDs"
[ $COMPLETED -lt $TOTAL ] && echo "Run again to continue"

Integration with Claude Code
Multi-Turn Workflow

Instead of one long operation, break into multiple Claude Code turns:

Turn 1:

Process first batch of 10 items and save checkpoint


Turn 2:

Resume from checkpoint and process next 10 items


Turn 3:

Complete processing and generate final report

Status Check Pattern
# Turn 1: Start background job
./long_operation.sh > output.log 2>&1 &
echo $! > pid.txt
echo "Started background job (PID: $(cat pid.txt))"

# Turn 2: Check status
if ps -p $(cat pid.txt) > /dev/null 2>&1; then
    echo "Still running..."
    echo "Recent output:"
    tail -20 output.log
else
    echo "✓ Complete!"
    cat output.log
    rm pid.txt
fi

Best Practices
✅ DO
Chunk operations into 5-10 item batches
Save checkpoints after each item or batch
Use timeouts on individual operations (60-90s max)
Report progress clearly and frequently
Enable resume from any checkpoint
Parallelize smartly (3-5 concurrent max)
Track failures separately from successes
Clean up checkpoint files when complete
❌ DON'T
Don't process everything in one go (>50 items)
Don't skip checkpoints on long workflows
Don't ignore timeout signals (handle EXIT 124)
Don't block indefinitely without progress
Don't over-parallelize (causes resource issues)
Don't lose progress due to missing state
Don't retry infinitely (limit to 3-4 attempts)
Don't forget cleanup of temp files
Quick Reference
# Batch processing
tail -n +$OFFSET file.txt | head -$BATCH_SIZE | while read item; do process; done

# Checkpoint resume
LAST=$(cat .checkpoint || echo 0); process_from $LAST

# State machine
case $(cat .state) in PHASE1) step1 ;; PHASE2) step2 ;; esac

# Progress tracking
echo "Progress: $COMPLETED/$TOTAL ($((COMPLETED * 100 / TOTAL))%)"

# Timeout with fallback
timeout 90s operation || use_cached_result

# Parallel with limit
for i in items; do process &; jobs=$(jobs -r | wc -l); [ $jobs -ge $MAX ] && wait -n; done


Version: 1.0.0 Author: Harvested from timeout-prevention skill patterns Last Updated: 2025-11-18 License: MIT Key Principle: Never try to do everything at once – chunk, checkpoint, and resume.

Weekly Installs
37
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