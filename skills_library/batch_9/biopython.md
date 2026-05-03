---
title: biopython
url: https://skills.sh/davila7/claude-code-templates/biopython
---

# biopython

skills/davila7/claude-code-templates/biopython
biopython
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill biopython
SKILL.md
Biopython: Computational Molecular Biology in Python
Overview

Biopython is a comprehensive set of freely available Python tools for biological computation. It provides functionality for sequence manipulation, file I/O, database access, structural bioinformatics, phylogenetics, and many other bioinformatics tasks. The current version is Biopython 1.85 (released January 2025), which supports Python 3 and requires NumPy.

When to Use This Skill

Use this skill when:

Working with biological sequences (DNA, RNA, or protein)
Reading, writing, or converting biological file formats (FASTA, GenBank, FASTQ, PDB, mmCIF, etc.)
Accessing NCBI databases (GenBank, PubMed, Protein, Gene, etc.) via Entrez
Running BLAST searches or parsing BLAST results
Performing sequence alignments (pairwise or multiple sequence alignments)
Analyzing protein structures from PDB files
Creating, manipulating, or visualizing phylogenetic trees
Finding sequence motifs or analyzing motif patterns
Calculating sequence statistics (GC content, molecular weight, melting temperature, etc.)
Performing structural bioinformatics tasks
Working with population genetics data
Any other computational molecular biology task
Core Capabilities

Biopython is organized into modular sub-packages, each addressing specific bioinformatics domains:

Sequence Handling - Bio.Seq and Bio.SeqIO for sequence manipulation and file I/O
Alignment Analysis - Bio.Align and Bio.AlignIO for pairwise and multiple sequence alignments
Database Access - Bio.Entrez for programmatic access to NCBI databases
BLAST Operations - Bio.Blast for running and parsing BLAST searches
Structural Bioinformatics - Bio.PDB for working with 3D protein structures
Phylogenetics - Bio.Phylo for phylogenetic tree manipulation and visualization
Advanced Features - Motifs, population genetics, sequence utilities, and more
Installation and Setup

Install Biopython using pip (requires Python 3 and NumPy):

uv pip install biopython


For NCBI database access, always set your email address (required by NCBI):

from Bio import Entrez
Entrez.email = "your.email@example.com"

# Optional: API key for higher rate limits (10 req/s instead of 3 req/s)
Entrez.api_key = "your_api_key_here"

Using This Skill

This skill provides comprehensive documentation organized by functionality area. When working on a task, consult the relevant reference documentation:

1. Sequence Handling (Bio.Seq & Bio.SeqIO)

Reference: references/sequence_io.md

Use for:

Creating and manipulating biological sequences
Reading and writing sequence files (FASTA, GenBank, FASTQ, etc.)
Converting between file formats
Extracting sequences from large files
Sequence translation, transcription, and reverse complement
Working with SeqRecord objects

Quick example:

from Bio import SeqIO

# Read sequences from FASTA file
for record in SeqIO.parse("sequences.fasta", "fasta"):
    print(f"{record.id}: {len(record.seq)} bp")

# Convert GenBank to FASTA
SeqIO.convert("input.gb", "genbank", "output.fasta", "fasta")

2. Alignment Analysis (Bio.Align & Bio.AlignIO)

Reference: references/alignment.md

Use for:

Pairwise sequence alignment (global and local)
Reading and writing multiple sequence alignments
Using substitution matrices (BLOSUM, PAM)
Calculating alignment statistics
Customizing alignment parameters

Quick example:

from Bio import Align

# Pairwise alignment
aligner = Align.PairwiseAligner()
aligner.mode = 'global'
alignments = aligner.align("ACCGGT", "ACGGT")
print(alignments[0])

3. Database Access (Bio.Entrez)

Reference: references/databases.md

Use for:

Searching NCBI databases (PubMed, GenBank, Protein, Gene, etc.)
Downloading sequences and records
Fetching publication information
Finding related records across databases
Batch downloading with proper rate limiting

Quick example:

from Bio import Entrez
Entrez.email = "your.email@example.com"

# Search PubMed
handle = Entrez.esearch(db="pubmed", term="biopython", retmax=10)
results = Entrez.read(handle)
handle.close()
print(f"Found {results['Count']} results")

4. BLAST Operations (Bio.Blast)

Reference: references/blast.md

Use for:

Running BLAST searches via NCBI web services
Running local BLAST searches
Parsing BLAST XML output
Filtering results by E-value or identity
Extracting hit sequences

Quick example:

from Bio.Blast import NCBIWWW, NCBIXML

# Run BLAST search
result_handle = NCBIWWW.qblast("blastn", "nt", "ATCGATCGATCG")
blast_record = NCBIXML.read(result_handle)

# Display top hits
for alignment in blast_record.alignments[:5]:
    print(f"{alignment.title}: E-value={alignment.hsps[0].expect}")

5. Structural Bioinformatics (Bio.PDB)

Reference: references/structure.md

Use for:

Parsing PDB and mmCIF structure files
Navigating protein structure hierarchy (SMCRA: Structure/Model/Chain/Residue/Atom)
Calculating distances, angles, and dihedrals
Secondary structure assignment (DSSP)
Structure superimposition and RMSD calculation
Extracting sequences from structures

Quick example:

from Bio.PDB import PDBParser

# Parse structure
parser = PDBParser(QUIET=True)
structure = parser.get_structure("1crn", "1crn.pdb")

# Calculate distance between alpha carbons
chain = structure[0]["A"]
distance = chain[10]["CA"] - chain[20]["CA"]
print(f"Distance: {distance:.2f} Å")

6. Phylogenetics (Bio.Phylo)

Reference: references/phylogenetics.md

Use for:

Reading and writing phylogenetic trees (Newick, NEXUS, phyloXML)
Building trees from distance matrices or alignments
Tree manipulation (pruning, rerooting, ladderizing)
Calculating phylogenetic distances
Creating consensus trees
Visualizing trees

Quick example:

from Bio import Phylo

# Read and visualize tree
tree = Phylo.read("tree.nwk", "newick")
Phylo.draw_ascii(tree)

# Calculate distance
distance = tree.distance("Species_A", "Species_B")
print(f"Distance: {distance:.3f}")

7. Advanced Features

Reference: references/advanced.md

Use for:

Sequence motifs (Bio.motifs) - Finding and analyzing motif patterns
Population genetics (Bio.PopGen) - GenePop files, Fst calculations, Hardy-Weinberg tests
Sequence utilities (Bio.SeqUtils) - GC content, melting temperature, molecular weight, protein analysis
Restriction analysis (Bio.Restriction) - Finding restriction enzyme sites
Clustering (Bio.Cluster) - K-means and hierarchical clustering
Genome diagrams (GenomeDiagram) - Visualizing genomic features

Quick example:

from Bio.SeqUtils import gc_fraction, molecular_weight
from Bio.Seq import Seq

seq = Seq("ATCGATCGATCG")
print(f"GC content: {gc_fraction(seq):.2%}")
print(f"Molecular weight: {molecular_weight(seq, seq_type='DNA'):.2f} g/mol")

General Workflow Guidelines
Reading Documentation

When a user asks about a specific Biopython task:

Identify the relevant module based on the task description
Read the appropriate reference file using the Read tool
Extract relevant code patterns and adapt them to the user's specific needs
Combine multiple modules when the task requires it

Example search patterns for reference files:

# Find information about specific functions
grep -n "SeqIO.parse" references/sequence_io.md

# Find examples of specific tasks
grep -n "BLAST" references/blast.md

# Find information about specific concepts
grep -n "alignment" references/alignment.md

Writing Biopython Code

Follow these principles when writing Biopython code:

Import modules explicitly

from Bio import SeqIO, Entrez
from Bio.Seq import Seq


Set Entrez email when using NCBI databases

Entrez.email = "your.email@example.com"


Use appropriate file formats - Check which format best suits the task

# Common formats: "fasta", "genbank", "fastq", "clustal", "phylip"


Handle files properly - Close handles after use or use context managers

with open("file.fasta") as handle:
    records = SeqIO.parse(handle, "fasta")


Use iterators for large files - Avoid loading everything into memory

for record in SeqIO.parse("large_file.fasta", "fasta"):
    # Process one record at a time


Handle errors gracefully - Network operations and file parsing can fail

try:
    handle = Entrez.efetch(db="nucleotide", id=accession)
except HTTPError as e:
    print(f"Error: {e}")

Common Patterns
Pattern 1: Fetch Sequence from GenBank
from Bio import Entrez, SeqIO

Entrez.email = "your.email@example.com"

# Fetch sequence
handle = Entrez.efetch(db="nucleotide", id="EU490707", rettype="gb", retmode="text")
record = SeqIO.read(handle, "genbank")
handle.close()

print(f"Description: {record.description}")
print(f"Sequence length: {len(record.seq)}")

Pattern 2: Sequence Analysis Pipeline
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

for record in SeqIO.parse("sequences.fasta", "fasta"):
    # Calculate statistics
    gc = gc_fraction(record.seq)
    length = len(record.seq)

    # Find ORFs, translate, etc.
    protein = record.seq.translate()

    print(f"{record.id}: {length} bp, GC={gc:.2%}")

Pattern 3: BLAST and Fetch Top Hits
from Bio.Blast import NCBIWWW, NCBIXML
from Bio import Entrez, SeqIO

Entrez.email = "your.email@example.com"

# Run BLAST
result_handle = NCBIWWW.qblast("blastn", "nt", sequence)
blast_record = NCBIXML.read(result_handle)

# Get top hit accessions
accessions = [aln.accession for aln in blast_record.alignments[:5]]

# Fetch sequences
for acc in accessions:
    handle = Entrez.efetch(db="nucleotide", id=acc, rettype="fasta", retmode="text")
    record = SeqIO.read(handle, "fasta")
    handle.close()
    print(f">{record.description}")

Pattern 4: Build Phylogenetic Tree from Sequences
from Bio import AlignIO, Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

# Read alignment
alignment = AlignIO.read("alignment.fasta", "fasta")

# Calculate distances
calculator = DistanceCalculator("identity")
dm = calculator.get_distance(alignment)

# Build tree
constructor = DistanceTreeConstructor()
tree = constructor.nj(dm)

# Visualize
Phylo.draw_ascii(tree)

Best Practices
Always read relevant reference documentation before writing code
Use grep to search reference files for specific functions or examples
Validate file formats before parsing
Handle missing data gracefully - Not all records have all fields
Cache downloaded data - Don't repeatedly download the same sequences
Respect NCBI rate limits - Use API keys and proper delays
Test with small datasets before processing large files
Keep Biopython updated to get latest features and bug fixes
Use appropriate genetic code tables for translation
Document analysis parameters for reproducibility
Troubleshooting Common Issues
Issue: "No handlers could be found for logger 'Bio.Entrez'"

Solution: This is just a warning. Set Entrez.email to suppress it.

Issue: "HTTP Error 400" from NCBI

Solution: Check that IDs/accessions are valid and properly formatted.

Issue: "ValueError: EOF" when parsing files

Solution: Verify file format matches the specified format string.

Issue: Alignment fails with "sequences are not the same length"

Solution: Ensure sequences are aligned before using AlignIO or MultipleSeqAlignment.

Issue: BLAST searches are slow

Solution: Use local BLAST for large-scale searches, or cache results.

Issue: PDB parser warnings

Solution: Use PDBParser(QUIET=True) to suppress warnings, or investigate structure quality.

Additional Resources
Official Documentation: https://biopython.org/docs/latest/
Tutorial: https://biopython.org/docs/latest/Tutorial/
Cookbook: https://biopython.org/docs/latest/Tutorial/ (advanced examples)
GitHub: https://github.com/biopython/biopython
Mailing List: biopython@biopython.org
Quick Reference

To locate information in reference files, use these search patterns:

# Search for specific functions
grep -n "function_name" references/*.md

# Find examples of specific tasks
grep -n "example" references/sequence_io.md

# Find all occurrences of a module
grep -n "Bio.Seq" references/*.md

Summary

Biopython provides comprehensive tools for computational molecular biology. When using this skill:

Identify the task domain (sequences, alignments, databases, BLAST, structures, phylogenetics, or advanced)
Consult the appropriate reference file in the references/ directory
Adapt code examples to the specific use case
Combine multiple modules when needed for complex workflows
Follow best practices for file handling, error checking, and data management

The modular reference documentation ensures detailed, searchable information for every major Biopython capability.

Weekly Installs
277
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn