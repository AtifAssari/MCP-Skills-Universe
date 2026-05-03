---
title: dna-assembly
url: https://skills.sh/letta-ai/skills/dna-assembly
---

# dna-assembly

skills/letta-ai/skills/dna-assembly
dna-assembly
Installation
$ npx skills add https://github.com/letta-ai/skills --skill dna-assembly
SKILL.md
DNA Assembly
Overview

This skill provides procedural knowledge for DNA assembly tasks, particularly Golden Gate assembly using Type IIS restriction enzymes. It addresses common pitfalls in primer design and provides verification strategies to ensure correct assembly designs.

Critical Requirements for Type IIS Restriction Enzyme Primers
Complete Primer Structure

When designing primers for Type IIS enzymes (BsaI, BsmBI, etc.), the complete structure must include ALL components:

[clamp ≥1bp]-[recognition site]-[spacer N]-[4bp overhang]-[binding region 15-45bp]


For BsaI-HFv2 specifically:

[clamp ≥1bp]-GGTCTC-N-[4bp overhang]-[binding region]


Critical: The clamp sequence is MANDATORY. Type IIS restriction enzymes require additional nucleotides flanking the recognition site for efficient binding and cutting. Primers starting directly with the recognition sequence (e.g., GGTCTC...) will fail validation.

Component Details
Component	Requirement	Purpose
Clamp	≥1 nucleotide (typically 2-6bp)	Enzyme binding efficiency
Recognition site	Enzyme-specific (e.g., GGTCTC for BsaI)	Enzyme targeting
Spacer (N)	1 nucleotide	Separates recognition from cut site
Overhang	4bp for Golden Gate	Determines assembly order
Binding region	15-45bp, Tm 50-65°C	Template specificity
Approach for DNA Assembly Tasks
Step 1: Verify External Requirements First

Before implementing any primer design:

Look up the specific enzyme requirements from the manufacturer (NEB, Thermo, etc.)
Document the complete primer structure explicitly
Verify clamp length requirements for the specific enzyme
Check for any special buffer or temperature requirements
Step 2: Parse and Validate Input Sequences

When working with input DNA sequences:

Parse FASTA/GenBank files correctly
Check for internal restriction sites that would interfere with assembly
Verify reading frames for fusion proteins (length divisible by 3)
Identify start/stop codons and determine if they need modification
Step 3: Design Overhangs Strategically

For ordered multi-fragment assembly:

Choose 4bp overhangs that are unique and non-complementary
Avoid palindromic sequences in overhangs
Ensure overhangs don't create internal recognition sites when joined
For fusion proteins, remove stop codons between fragments
Step 4: Calculate Binding Regions

For the template-binding portion of primers:

Target melting temperature (Tm) within specification (typically 50-65°C)
Use appropriate Tm calculation method (nearest-neighbor preferred)
Ensure binding region is 15-45 nucleotides
Check for secondary structures or primer dimers
Verification Strategies
Independent Validation Approach

Self-verification can encode the same incorrect assumptions. To avoid this:

Test against published examples: Find published Golden Gate primer sequences and verify the design logic produces the same structure
Use external tools: Validate primers with established tools (Benchling, SnapGene, NEB primer design tools)
Check component counts: Verify primers contain all required components by position
Verification Checklist
[ ] Clamp sequence present (≥1bp before recognition site)
[ ] Recognition site correct and complete
[ ] Spacer nucleotide present after recognition site
[ ] Overhang is exactly 4bp
[ ] Binding region Tm within specification
[ ] No internal restriction sites in inserts
[ ] Overhangs are unique and non-conflicting
[ ] Frame preserved for fusion proteins
[ ] Start/stop codons handled correctly

Programmatic Verification

When writing verification code:

Check primer structure by position, not just content
Verify the recognition site does NOT start at position 0
Confirm overhang sequences match expected assembly order
Calculate actual Tm using consistent method
Common Pitfalls
1. Missing Clamp Sequence

Error: Primer starts directly with recognition site

WRONG: GGTCTCAAAGC...  (GGTCTC at position 0)
RIGHT: GCGGTCTCAAAGC... (clamp 'GC' before GGTCTC)

2. Incomplete Requirements Verification

Error: Acknowledging the need to check enzyme requirements but not following through Solution: Always document the complete primer structure before writing any design code

3. Self-Verification Bias

Error: Creating verification scripts that encode the same assumptions as the design Solution: Use external references or published examples to validate design logic

4. Ignoring Manufacturer Specifications

Error: Using generic enzyme knowledge instead of specific product requirements Solution: Check manufacturer documentation for the specific enzyme variant (e.g., BsaI-HFv2 vs standard BsaI)

5. Overhang Conflicts

Error: Choosing overhangs that are complementary to each other or create unintended recognition sites Solution: Systematically verify all overhang pairs for compatibility

Reusable Code Patterns

When implementing DNA assembly tasks, consider creating reusable functions for:

FASTA/sequence parsing - Avoid rewriting parsing logic multiple times
Reverse complement calculation - Standard function used throughout
Melting temperature calculation - Consistent Tm method across all primers
Primer structure validation - Single source of truth for structure requirements
Reference Materials

For detailed enzyme specifications and protocols, consult:

references/golden_gate_primer_structure.md - Complete primer structure documentation
Manufacturer protocols (NEB, Thermo Fisher) for specific enzymes
Published Golden Gate assembly papers for validated examples
Weekly Installs
34
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