---
title: reshard-c4-data
url: https://skills.sh/letta-ai/skills/reshard-c4-data
---

# reshard-c4-data

skills/letta-ai/skills/reshard-c4-data
reshard-c4-data
Installation
$ npx skills add https://github.com/letta-ai/skills --skill reshard-c4-data
SKILL.md
Reshard C4 Data
Overview

This skill provides guidance for data resharding tasks where files must be reorganized across a directory structure while respecting constraints such as maximum file size limits and maximum items per directory. These tasks require careful consideration of how constraints apply recursively to all levels of the output structure.

Critical Concept: Recursive Constraint Application

When a constraint states "maximum N files or folders in each directory," this applies to ALL directories in the output structure, including:

The root output directory
Any intermediate grouping directories
The final shard/leaf directories

Common Mistake: Interpreting directory constraints as applying only to leaf directories while ignoring the root and intermediate levels.

Mathematical Validation

Before implementing, perform constraint arithmetic:

Calculate the total number of output items (files, shards, or groups)
If items exceed the per-directory limit, hierarchical nesting is required
Recursively apply this calculation at each level

Example: For 9,898 files with a 30-item-per-directory limit:

Files per shard: 30 → ~330 shards needed
Shards per group: 30 → ~11 groups needed
Groups in root: 11 → Compliant (under 30)

This yields a three-level hierarchy: output/group_XXXX/shard_XXXX/files

Approach for Resharding Tasks
Step 1: Analyze Input Data
Inventory all input files (count, sizes, directory structure)
Identify files exceeding size limits that require splitting
Calculate total storage requirements
Step 2: Validate Constraint Mathematics

For each constraint, verify compliance at all directory levels:

total_files = count(input_files) + count(split_chunks)
shards_needed = ceil(total_files / max_files_per_shard)

if shards_needed > max_items_per_directory:
    groups_needed = ceil(shards_needed / max_items_per_directory)
    # Continue nesting until root directory complies

Step 3: Design Hierarchical Output Structure

Create a directory hierarchy that satisfies constraints at every level:

output/
  .metadata.json          # Reconstruction metadata
  group_0000/
    shard_0000/
      file_001.txt
      file_002.txt
      ... (up to max_files_per_shard)
    shard_0001/
    ... (up to max_items_per_directory shards)
  group_0001/
  ... (up to max_items_per_directory groups)

Step 4: Implement File Distribution
Split oversized files into chunks that comply with size limits
Distribute files/chunks across shards evenly
Track original file mappings in metadata for reconstruction
Use checksums to verify data integrity
Step 5: Generate Reconstruction Metadata

Include metadata that enables reversing the resharding:

Original file paths and their shard locations
Split file chunk mappings
Checksums for integrity verification
Verification Strategies
Constraint Verification Checklist

Execute these checks before declaring success:

Root directory item count: ls <output_dir> | wc -l must be ≤ limit
All intermediate directories: Recursively verify each directory level
All leaf directories: Verify shard contents
File size limits: Check no single file exceeds the maximum
Data integrity: Verify checksums match originals
Automated Verification Script Pattern
def verify_directory_constraints(path, max_items):
    """Recursively verify all directories comply with item limit."""
    for root, dirs, files in os.walk(path):
        item_count = len(dirs) + len(files)
        if item_count > max_items:
            return False, f"{root} has {item_count} items (max: {max_items})"
    return True, "All directories compliant"

Common Verification Failures
Symptom	Likely Cause	Solution
Root directory exceeds limit	Flat shard structure	Add grouping hierarchy
Checksums don't match	File corruption during split	Re-implement split logic with verification
Missing files in reconstruction	Incomplete metadata	Audit metadata generation
Common Pitfalls
Pitfall 1: Partial Constraint Interpretation

Mistake: Applying "max N items per directory" only to leaf directories.

Prevention: Explicitly verify every directory level in the output structure.

Pitfall 2: Ignoring Metadata in Item Counts

Mistake: Forgetting that metadata files (e.g., .metadata.json) count toward directory limits.

Prevention: Include metadata files in constraint calculations.

Pitfall 3: False Confidence from Partial Testing

Mistake: Concluding success after verifying data integrity but not structural constraints.

Prevention: Create separate verification steps for each constraint type.

Pitfall 4: Underestimating Scale

Mistake: Testing with small datasets that don't trigger hierarchical nesting requirements.

Prevention: Calculate expected output structure mathematically before implementation.

Testing Recommendations
Unit test constraint logic with edge cases (exactly at limits, one over, etc.)
Test with representative scale that triggers all hierarchy levels
Verify round-trip integrity by reconstructing and comparing checksums
Check all constraint types independently before integration testing
Weekly Installs
32
Repository
letta-ai/skills
GitHub Stars
94
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass