---
rating: ⭐⭐⭐
title: settlement-analysis-expert
url: https://skills.sh/reggiechan74/vp-real-estate/settlement-analysis-expert
---

# settlement-analysis-expert

skills/reggiechan74/vp-real-estate/settlement-analysis-expert
settlement-analysis-expert
Installation
$ npx skills add https://github.com/reggiechan74/vp-real-estate --skill settlement-analysis-expert
SKILL.md

You are an expert in settlement scenario analysis vs. expropriation hearing risk, providing decision-focused guidance using probability-weighted expected value, BATNA/ZOPA calculations, and strategic negotiation planning.

Settlement Analysis Expert

Expert in settlement scenario analysis vs. expropriation hearing risk with probability-weighted outcomes, BATNA/ZOPA calculations, and strategic negotiation planning.

When to Use This Skill

Use this skill when:

Analyzing settlement offers vs. proceeding to expropriation hearing
Calculating BATNA (Best Alternative to Negotiated Agreement)
Evaluating ZOPA (Zone of Possible Agreement)
Assessing owner holdout risk and litigation probability
Developing concession strategies for settlement negotiations
Quantifying expected value of hearing outcomes with uncertainty
Comparing multiple settlement scenarios with probability weighting
What This Skill Provides
Core Analysis Capabilities

Settlement vs. Hearing Analysis

Probability-weighted expected value of hearing outcomes
Settlement scenario comparison (current offer, counteroffer, midpoint)
Net benefit calculation with risk adjustment
Breakeven settlement determination

BATNA Calculation

Expected award calculation across low/mid/high scenarios
Total hearing costs (legal fees, expert fees, time costs)
Net BATNA (total expected cost to buyer)
Uncertainty analysis (standard deviation, coefficient of variation)

ZOPA Analysis

Zone of possible agreement identification
Optimal settlement range recommendations
Opening offer, target, and walkaway points
Negotiation leverage assessment

Risk Assessment

Owner holdout risk scoring (0-30 scale)
Litigation probability estimation
Expected hearing duration and cost ranges
Risk factor identification and mitigation strategies

Strategic Planning

Concession strategy with diminishing increments
Negotiation rounds planning
Timeline and action items
Decision confidence levels
Key Metrics Calculated
Expected Hearing Cost: Probability-weighted award + legal/expert fees
Net Benefit: Settlement savings vs. hearing
Holdout Risk Score: 0-30 scale (motivation + sophistication + alternatives)
Litigation Probability: 0-100% based on valuation gap, owner profile, case complexity
ZOPA Range: Lower bound (seller min) to upper bound (buyer max)
Optimal Settlement: Target, floor, ceiling within ZOPA
Risk-Adjusted Benefit: Net benefit minus uncertainty premium
Calculator: settlement_analyzer.py

Location: .claude/skills/settlement-analysis-expert/settlement_analyzer.py

Purpose: Analyze settlement scenarios vs. hearing risk with probability-weighted outcomes

Architecture: Modular design following Issue #21 requirements

Thin orchestration layer (main calculator)
Separate modules for validation, calculations, analysis, output formatting
Shared utilities integration (negotiation_utils, risk_utils, financial_utils, report_utils)
Modules

validators.py

Input validation against JSON schema
Probability distribution validation (must sum to 1.0)
Owner profile and case factors validation
Award amount ordering validation (low <= mid <= high)

calculations.py

Settlement scenario calculations
Hearing expected value (BATNA)
Net benefit and savings analysis
Scenario comparison with probability weighting

analysis.py

Settlement vs. hearing decision analysis
ZOPA and optimal range calculation
Concession strategy generation
Owner holdout risk assessment
Litigation risk assessment
Sensitivity analysis

output_formatters.py

Comprehensive markdown reports
Executive summaries
Scenario comparison tables
Financial summaries
Usage
# Basic usage (markdown report to stdout)
python settlement_analyzer.py samples/sample_1_transmission_easement.json

# Generate report to file
python settlement_analyzer.py samples/sample_1_transmission_easement.json --output report.md

# JSON output for programmatic use
python settlement_analyzer.py samples/sample_1_transmission_easement.json --json > results.json

Input Schema

Required Fields:

case_id: Case identifier
settlement_offer: Current settlement offer amount
hearing_probabilities: {low_award, mid_award, high_award} (must sum to 1.0)
hearing_costs: {low/mid/high_award_amount, legal_fees, expert_fees, time_cost}

Optional Fields:

counteroffer: Owner's counteroffer
buyer_max_settlement: Maximum buyer willing to pay (defaults to BATNA)
settlement_costs: {legal_fees_to_settle, settlement_risk}
owner_profile: {motivation, sophistication, alternatives}
case_factors: {valuation_gap, property_value, legal_complexity, precedent_clarity, jurisdiction_history}
discount_rate: Annual discount rate for NPV (default 5%)

Full Schema: See settlement_input_schema.json (JSON Schema Draft 2020-12)

Sample Input
{
  "case_id": "HYDRO-2025-001",
  "property_description": "Transmission line easement across 50-acre farm",
  "settlement_offer": 180000,
  "counteroffer": 220000,
  "hearing_probabilities": {
    "low_award": 0.2,
    "mid_award": 0.5,
    "high_award": 0.3
  },
  "hearing_costs": {
    "low_award_amount": 150000,
    "mid_award_amount": 185000,
    "high_award_amount": 230000,
    "legal_fees": 50000,
    "expert_fees": 30000,
    "time_cost": 10000
  },
  "settlement_costs": {
    "legal_fees_to_settle": 5000,
    "settlement_risk": 0.1
  },
  "owner_profile": {
    "motivation": {
      "financial_need": "low",
      "emotional_attachment": "high",
      "business_impact": "moderate"
    },
    "sophistication": {
      "real_estate_experience": "medium",
      "legal_representation": true,
      "previous_negotiations": 1
    },
    "alternatives": {
      "relocation_options": "some",
      "financial_flexibility": "medium",
      "timeline_pressure": "low"
    }
  },
  "case_factors": {
    "valuation_gap": 40000,
    "property_value": 200000,
    "legal_complexity": "medium",
    "precedent_clarity": "mixed",
    "jurisdiction_history": "neutral"
  }
}

Output Report

The calculator generates a comprehensive markdown report with:

Executive Summary

Recommendation (SETTLE / PROCEED TO HEARING / NEUTRAL)
Rationale and confidence level
Financial impact

Financial Summary

Settlement total cost vs. hearing total cost
Net benefit and savings percentage
Breakeven settlement amount

Hearing Risk Analysis

Expected award with probability distribution
Total costs breakdown (legal, expert, time)
Award range (low/mid/high scenarios)
Uncertainty metrics (standard deviation, coefficient of variation)

Settlement Scenarios

Scenario comparison table (current offer, counteroffer, midpoint)
Probability-weighted costs
Scenario descriptions

ZOPA Analysis (if counteroffer provided)

ZOPA existence and range
Optimal settlement range (opening, target, walkaway)
Negotiation room and leverage

Owner Holdout Risk Assessment (if owner profile provided)

Risk level (LOW/MEDIUM/HIGH/CRITICAL)
Holdout probability
Score breakdown (motivation, sophistication, alternatives)
Key risk factors and mitigation strategies

Litigation Risk Assessment (if case factors provided)

Litigation probability
Expected duration (months) and cost
Risk factors
Shared Utilities Used

negotiation_utils.py:

calculate_batna(): Calculate hearing expected value
calculate_zopa(): Identify zone of possible agreement
probability_weighted_ev(): Probability-weighted scenario comparison
hearing_cost_benefit(): Cost-benefit analysis settlement vs. hearing
optimal_settlement_range(): Calculate optimal negotiation range
calculate_concession_strategy(): Generate diminishing concession pattern

risk_utils.py:

assess_holdout_risk(): Owner holdout risk scoring (0-30)
litigation_risk_assessment(): Litigation probability and duration
sensitivity_analysis(): Impact of variable changes

financial_utils.py:

npv(): Net present value calculations
safe_divide(): Division with zero handling

report_utils.py:

generate_executive_summary(): Decision-focused summaries
format_markdown_table(): Scenario comparison tables
eastern_timestamp(): Report timestamps
generate_document_header(): Standard headers
format_number(): Currency/percentage formatting
Decision Framework
Recommendation Thresholds

SETTLE (High Confidence):

Net benefit > $10,000
Settlement saves material amount vs. hearing
Low hearing uncertainty acceptable

SETTLE (Medium Confidence):

Net benefit $0 - $10,000
Settlement saves small amount vs. hearing
Uncertainty may be concerning

NEUTRAL (Continue Negotiations):

Net benefit between -$10,000 and $0
Costs roughly equivalent
Room for negotiation exists within ZOPA

PROCEED TO HEARING:

Net benefit < -$10,000
Hearing expected to save material amount vs. settlement
Settlement offer insufficient
Risk Adjustment

Hearing Uncertainty Premium:

Calculate standard deviation of hearing outcomes
Apply risk premium = std_dev × 0.5 (risk aversion factor)
Risk-adjusted benefit = net_benefit - risk_premium

Holdout Risk Scoring (0-30 scale):

0-9: LOW risk (15% holdout probability)
10-14: MEDIUM risk (30% holdout probability)
15-19: HIGH risk (50% holdout probability)
20-30: CRITICAL risk (70% holdout probability)

Litigation Probability Factors:

Valuation gap percentage
Owner risk profile
Legal complexity
Precedent clarity
Jurisdiction history
Workflow Integration
Typical Use Cases

1. Initial Settlement Evaluation

# Evaluate initial settlement offer vs. hearing
python settlement_analyzer.py case_data.json --output initial_analysis.md


2. Counteroffer Analysis

# Update JSON with counteroffer, recalculate ZOPA
python settlement_analyzer.py case_data_with_counter.json --output counter_analysis.md


3. Negotiation Strategy Development

# Generate concession strategy based on ZOPA
python settlement_analyzer.py case_data.json --json | jq '.concession_strategy'


4. Board Approval Package

# Comprehensive report for executive decision
python settlement_analyzer.py case_data.json --output board_memo.md

Integration with Other Skills

Combines with:

expropriation-compensation-entitlement-analysis: Legal entitlement framework for hearing scenarios
injurious-affection-assessment: Quantify damages for hearing cost estimates
agricultural-easement-negotiation-frameworks: Farm-specific negotiation strategies
negotiation-expert: Evidence-based persuasion and calibrated questions
Key Terms
BATNA: Best Alternative to Negotiated Agreement (hearing outcome)
ZOPA: Zone of Possible Agreement (overlap between buyer max and seller min)
Holdout Risk: Probability owner refuses settlement and forces hearing
Litigation Probability: Likelihood of proceeding to expropriation hearing
Net Benefit: Settlement savings vs. hearing (positive = settle, negative = hearing better)
Expected Award: Probability-weighted hearing compensation
Optimal Settlement Range: Opening offer, target, and walkaway points
Concession Strategy: Diminishing increments from opening to target
Risk-Adjusted Benefit: Net benefit minus uncertainty premium
Expert Guidance
When Settlement Makes Sense
Certainty Value: Settlement eliminates hearing uncertainty
Cost Savings: Avoid legal fees, expert fees, time delays
Relationship Preservation: Maintain goodwill for future dealings
Timeline Advantage: Faster resolution enables project progress
Risk Mitigation: Avoid worst-case hearing outcomes
When Hearing Makes Sense
Insufficient Offer: Settlement offer materially below expected hearing award
Precedent Setting: Need hearing decision for future similar cases
Owner Unreasonable: Counteroffer far exceeds fair value
Strong Case: High confidence in favorable hearing outcome
ZOPA Absent: No overlap between buyer max and seller min
Negotiation Best Practices
Start with BATNA: Know your walkaway point before negotiating
Calculate ZOPA: Identify settlement range where both parties benefit
Use Diminishing Concessions: Signal approaching limit
Anchor High/Low: Buyer starts low, seller starts high, meet in middle
Justify Movements: Each concession tied to new information or reciprocity
Monitor Owner Risk: Adjust strategy based on holdout probability
Document Everything: Create audit trail for decision rationale
References

Ontario Expropriations Act:

s.13: Market value determination
s.14: Basis of compensation
s.18: Disturbance damages
s.20: Interest on compensation

Negotiation Theory:

Fisher & Ury, "Getting to Yes" (BATNA/ZOPA framework)
Kahneman & Tversky, Prospect Theory (risk aversion, loss aversion)
Raiffa, "The Art and Science of Negotiation" (optimal settlement ranges)

Real Estate Valuation:

USPAP Standard 1: Real Property Appraisal (hearing award estimation)
CUSPAP: Canadian Uniform Standards of Professional Appraisal Practice
Weekly Installs
12
Repository
reggiechan74/vp…l-estate
GitHub Stars
16
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass