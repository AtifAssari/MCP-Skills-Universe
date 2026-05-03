---
rating: ⭐⭐
title: tooluniverse-gwas-snp-interpretation
url: https://skills.sh/mims-harvard/tooluniverse/tooluniverse-gwas-snp-interpretation
---

# tooluniverse-gwas-snp-interpretation

skills/mims-harvard/tooluniverse/tooluniverse-gwas-snp-interpretation
tooluniverse-gwas-snp-interpretation
Installation
$ npx skills add https://github.com/mims-harvard/tooluniverse --skill tooluniverse-gwas-snp-interpretation
SKILL.md
GWAS SNP Interpretation Skill

SNP interpretation: a GWAS hit is a REGION, not a single causal variant. The lead SNP may not be causal — it may be in LD with the causal variant. Always check LD structure and functional annotation before concluding a specific SNP is mechanistically responsible. Fine-mapping (SuSiE, FINEMAP credible sets) narrows the causal set but rarely identifies a single variant with certainty. L2G scores integrate eQTL, chromatin interaction, and distance data to predict the causal gene — a lead SNP mapping to gene A may actually regulate gene B 500 kb away via a distal enhancer.

LOOK UP DON'T GUESS: never assume a SNP's functional consequence, mapped gene, or population frequency — always call gwas_get_snp_by_id and OpenTargets_get_variant_info to retrieve current annotations.

Overview

Interpret genetic variants (SNPs) from GWAS studies by aggregating evidence from multiple sources to provide comprehensive clinical and biological context.

Use Cases:

"Interpret rs7903146" (TCF7L2 diabetes variant)
"What diseases is rs429358 associated with?" (APOE Alzheimer's variant)
"Clinical significance of rs1801133" (MTHFR variant)
"Is rs12913832 in any fine-mapped loci?" (Eye color variant)
What It Does

The skill provides a comprehensive interpretation of SNPs by:

SNP Annotation: Retrieves basic variant information including genomic coordinates, alleles, functional consequence, and mapped genes
Association Discovery: Finds all GWAS trait/disease associations with statistical significance
Fine-Mapping Evidence: Identifies credible sets the variant belongs to (fine-mapped causal loci)
Gene Mapping: Uses Locus-to-Gene (L2G) predictions to identify likely causal genes
Clinical Summary: Aggregates evidence into actionable clinical significance
Workflow
User Input: rs7903146
    ↓
[1] SNP Lookup
    → Get location, consequence, MAF
    → gwas_get_snp_by_id
    ↓
[2] Association Search
    → Find all trait/disease associations
    → gwas_get_associations_for_snp
    ↓
[3] Fine-Mapping (Optional)
    → Get credible set membership
    → OpenTargets_get_variant_credible_sets
    ↓
[4] Gene Predictions
    → Extract L2G scores for causal genes
    → (embedded in credible sets)
    ↓
[5] Clinical Summary
    → Aggregate evidence
    → Identify key traits and genes
    ↓
Output: Comprehensive Interpretation Report

Data Sources
GWAS Catalog (EMBL-EBI)
SNP annotations: Functional consequences, mapped genes, population frequencies
Associations: P-values, effect sizes, study metadata
Coverage: 350,000+ publications, 670,000+ associations
Open Targets Genetics
Fine-mapping: Statistical credible sets from SuSiE, FINEMAP methods
L2G predictions: Machine learning-based gene prioritization
Colocalization: QTL evidence for causal genes
Coverage: UK Biobank, FinnGen, and other large cohorts
Input Parameters
Required
rs_id (str): dbSNP rs identifier
Format: "rs" + number (e.g., "rs7903146")
Must be valid rsID in GWAS Catalog
Optional
include_credible_sets (bool, default=True): Query fine-mapping data
True: Complete interpretation (slower, ~10-30s)
False: Fast associations only (~2-5s)
p_threshold (float, default=5e-8): Genome-wide significance threshold
max_associations (int, default=100): Maximum associations to retrieve
Output Format

Returns SNPInterpretationReport containing:

1. SNP Basic Info
{
    'rs_id': 'rs7903146',
    'chromosome': '10',
    'position': 112998590,
    'ref_allele': 'C',
    'alt_allele': 'T',
    'consequence': 'intron_variant',
    'mapped_genes': ['TCF7L2'],
    'maf': 0.293
}

2. Trait Associations
[
    {
        'trait': 'Type 2 diabetes',
        'p_value': 1.2e-128,
        'beta': '0.28 unit increase',
        'study_id': 'GCST010555',
        'pubmed_id': '33536258',
        'effect_allele': 'T'
    },
    ...
]

3. Credible Sets (Fine-Mapping)
[
    {
        'study_id': 'GCST90476118',
        'trait': 'Renal failure',
        'finemapping_method': 'SuSiE-inf',
        'p_value': 3.5e-42,
        'predicted_genes': [
            {'gene': 'TCF7L2', 'score': 0.863}
        ],
        'region': '10:112950000-113050000'
    },
    ...
]

4. Clinical Significance
Genome-wide significant associations with 100 traits/diseases:
  - Type 2 diabetes
  - Diabetic retinopathy
  - HbA1c levels
  ...

Identified in 20 fine-mapped loci.
Predicted causal genes: TCF7L2

Example Usage

See QUICK_START.md for platform-specific examples.

Tools Used
GWAS Catalog Tools
gwas_get_snp_by_id: Get SNP annotation
gwas_get_associations_for_snp: Get all trait associations
Open Targets Tools
OpenTargets_get_variant_info: Get variant details with population frequencies
OpenTargets_get_variant_credible_sets: Get fine-mapping credible sets with L2G
Interpretation Guide
P-value Significance Levels
p < 5e-8: Genome-wide significant (strong evidence)
p < 5e-6: Suggestive (moderate evidence)
p < 0.05: Nominal (weak evidence)
L2G Score Interpretation
> 0.5: High confidence causal gene
0.1-0.5: Moderate confidence
< 0.1: Low confidence
Clinical Actionability
High: Multiple genome-wide significant associations + in credible sets + high L2G scores
Moderate: Genome-wide significant associations but limited fine-mapping
Low: Suggestive associations or limited replication
Limitations
Variant ID Conversion: OpenTargets requires chr_pos_ref_alt format, which may need allele lookup
Population Specificity: Associations may vary by ancestry
Effect Sizes: Beta values are study-dependent (different phenotype scales)
Causality: Associations don't prove causation; fine-mapping improves confidence
Currency: Data reflects published GWAS; latest studies may not be included
Best Practices
Use Full Interpretation: Enable include_credible_sets=True for clinical decisions
Check Multiple Variants: Look at other variants in the same locus
Validate Populations: Consider ancestry-specific effect sizes
Review Publications: Check original studies for context
Integrate Evidence: Combine with functional data, eQTLs, pQTLs
Technical Notes
Performance
Fast mode (no credible sets): 2-5 seconds
Full mode (with credible sets): 10-30 seconds
Bottleneck: OpenTargets GraphQL API rate limits
Error Handling
Invalid rs_id: Returns error message
No associations: Returns empty list with note
API failures: Graceful degradation (returns partial results)
Related Skills
Gene Function Analysis: Interpret predicted causal genes
Disease Ontology Lookup: Understand trait classifications
PubMed Literature Search: Find original GWAS publications
Variant Effect Prediction: Functional consequence analysis
References
GWAS Catalog: https://www.ebi.ac.uk/gwas/
Open Targets Genetics: https://genetics.opentargets.org/
GWAS Significance Thresholds: Fadista et al. 2016
L2G Method: Mountjoy et al. 2021 (Nature Genetics)
Version
Version: 1.0.0
Last Updated: 2026-02-13
ToolUniverse Version: >= 1.0.0
Tools Required: gwas_get_snp_by_id, gwas_get_associations_for_snp, OpenTargets_get_variant_credible_sets
Weekly Installs
185
Repository
mims-harvard/to…universe
GitHub Stars
1.3K
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn