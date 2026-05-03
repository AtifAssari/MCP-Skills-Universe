---
title: tooluniverse-sequence-retrieval
url: https://skills.sh/mims-harvard/tooluniverse/tooluniverse-sequence-retrieval
---

# tooluniverse-sequence-retrieval

skills/mims-harvard/tooluniverse/tooluniverse-sequence-retrieval
tooluniverse-sequence-retrieval
Installation
$ npx skills add https://github.com/mims-harvard/tooluniverse --skill tooluniverse-sequence-retrieval
Summary

Retrieve DNA, RNA, and protein sequences from NCBI and ENA with automatic gene disambiguation and cross-database handling.

Searches NCBI Nucleotide by organism, gene name, strain, and sequence type; automatically disambiguates genes across species and resolves accession prefixes to the correct database
Handles RefSeq (NC_, NM_, NP_) and GenBank accessions with intelligent fallback between NCBI and ENA; never attempts ENA queries on RefSeq-only accessions
Returns detailed sequence profiles including metadata, GC content, annotation summaries, curation levels, and alternative sequences ranked by relevance
Supports FASTA and GenBank formats with full annotation extraction; provides cross-database references and download instructions for each sequence
SKILL.md
Biological Sequence Retrieval

Retrieve DNA, RNA, and protein sequences with proper disambiguation and cross-database handling.

IMPORTANT: Always use English terms in tool calls. Only try original-language terms as fallback. Respond in the user's language.

LOOK UP DON'T GUESS: Never assume accession numbers or sequence versions. Always retrieve and verify from NCBI or ENA.

Domain Reasoning

Sequence quality hierarchy: RefSeq (NM_/NP_ = curated) > RefSeq predicted (XM_/XP_) > GenBank (submitted). Prefer the MANE Select transcript for human canonical isoforms. Check version numbers -- annotations improve across versions.

Workflow
Phase 0: Clarify (if needed) → Phase 1: Disambiguate Gene/Organism → Phase 2: Search & Retrieve → Phase 3: Report

Phase 0: Clarification (When Needed)

Ask ONLY if: gene exists in multiple organisms, sequence type unclear, or strain matters. Skip for: specific accessions, clear organism+gene combos, complete genome requests with organism.

Phase 1: Gene/Organism Disambiguation
Accession Type Decision Tree
Prefix	Type	Use With
NC_/NM_/NR_/NP_/XM_	RefSeq	NCBI only
U*/M*/K*/X*/CP*/NZ_	GenBank	NCBI or ENA
EMBL format	EMBL	ENA preferred

CRITICAL: Never try ENA tools with RefSeq accessions -- they return 404.

Identity Checklist
Organism confirmed (scientific name)
Gene symbol/name identified
Sequence type determined (genomic/mRNA/protein)
Accession prefix identified for tool selection
Phase 2: Data Retrieval (Internal)

Retrieve silently. Do NOT narrate the search process.

# Search NCBI Nucleotide
result = tu.tools.NCBI_search_nucleotide(
    operation="search", organism=organism, gene=gene,
    strain=strain, keywords=keywords, seq_type=seq_type, limit=10
)

# Get accessions from UIDs
accessions = tu.tools.NCBI_fetch_accessions(operation="fetch_accession", uids=result["data"]["uids"])

# Retrieve sequence (FASTA or GenBank format)
sequence = tu.tools.NCBI_get_sequence(operation="fetch_sequence", accession=accession, format="fasta")

# ENA alternative (non-RefSeq accessions only)
entry = tu.tools.ena_get_entry(accession=accession)
fasta = tu.tools.ena_get_sequence_fasta(accession=accession)

Fallback Chains
Primary	Fallback	Notes
NCBI_get_sequence	ENA (if GenBank format)	NCBI unavailable
ENA_get_entry	NCBI_get_sequence	ENA doesn't have RefSeq
NCBI_search_nucleotide	Try broader keywords	No results
Phase 3: Report Sequence Profile

Present as a Sequence Profile Report. Hide search process. Include:

Search Summary: query, database, result count
Primary Sequence: accession, type (RefSeq/GenBank), organism, strain, length, molecule, topology, curation level
Sequence Preview: first lines of FASTA (truncated)
Annotations Summary: CDS/tRNA/rRNA/regulatory feature counts (from GenBank format)
Alternative Sequences: ranked by relevance and curation, with ENA compatibility
Cross-Database References: RefSeq, GenBank, ENA/EMBL, BioProject, BioSample
Download Options: FASTA (for BLAST/alignment), GenBank (for annotation)
Curation Level Tiers
Tier	Prefix	Description
RefSeq Reference (best)	NC_, NM_, NP_	NCBI-curated, gold standard
RefSeq Predicted	XM_, XP_, XR_	Computationally predicted
GenBank Validated	Various	Submitted, some curation
GenBank Direct	Various	Direct submission
Third Party	TPA_	Third-party annotation
Reasoning Framework

Sequence quality: Prefer RefSeq over GenBank. Check version numbers. Sequences with "PREDICTED" in definition are not experimentally validated.

Accession guidance: RefSeq = NCBI-only. GenBank = mirrored in ENA/EMBL. Default to RefSeq mRNA (NM_) for human/model organisms; most complete genome assembly for microbial queries.

Cross-database reconciliation: Same sequence may have different accessions (e.g., GenBank U00096 = RefSeq NC_000913 for E. coli K-12). Always report both when available. Discrepancies between GenBank/RefSeq typically indicate RefSeq curation corrected submission errors.

Synthesis Questions
What is the highest-quality accession available?
Are there alternative accessions in other databases?
What is the annotation completeness?
Is the sequence from the expected organism/strain?
What download format suits the user's downstream analysis?
Error Handling
Error	Response
"No search criteria provided"	Add organism, gene, or keywords
"ENA 404 error"	Likely RefSeq -- use NCBI only
"No results found"	Broaden search, check spelling, try synonyms
"Sequence too large"	Note size, provide download link instead
Tool Reference

NCBI Tools: NCBI_search_nucleotide (search), NCBI_fetch_accessions (UID→accession), NCBI_get_sequence (retrieve) ENA Tools (GenBank/EMBL only): ena_get_entry (metadata), ena_get_sequence_fasta (FASTA), ena_get_entry_summary (summary)

Search Parameters Reference

NCBI_search_nucleotide: operation="search", organism (scientific name), gene (symbol), strain, keywords, seq_type (complete_genome/mrna/refseq), limit

NCBI_get_sequence: operation="fetch_sequence", accession, format (fasta/genbank)

Weekly Installs
1.3K
Repository
mims-harvard/to…universe
GitHub Stars
1.3K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn