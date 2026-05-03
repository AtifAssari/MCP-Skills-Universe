---
title: brand-analyzer
url: https://skills.sh/ailabs-393/ai-labs-claude-skills/brand-analyzer
---

# brand-analyzer

skills/ailabs-393/ai-labs-claude-skills/brand-analyzer
brand-analyzer
Installation
$ npx skills add https://github.com/ailabs-393/ai-labs-claude-skills --skill brand-analyzer
SKILL.md
Brand Analyzer
Overview

This skill enables comprehensive brand analysis and guidelines creation. It analyzes brand requirements, identifies brand personality and positioning, and generates professional brand guidelines documents. The skill uses established brand frameworks including Jung's 12 archetypes and industry-standard brand identity principles.

When to Use This Skill

Use this skill when the user requests:

Brand analysis or brand audit
Creation of brand guidelines or brand standards
Brand identity development or refinement
Brand consistency evaluation
Brand positioning and differentiation analysis
Brand archetype identification
Recommendations for brand improvements
Documentation of existing brand elements
Core Workflow
Step 1: Determine Analysis Type

Identify what type of brand work is needed:

A. New Brand Development

Starting from scratch or rebranding
Requires comprehensive brand identity creation
Output: Complete brand guidelines document

B. Existing Brand Analysis

Analyzing current brand state
Identifying inconsistencies and gaps
Output: Brand analysis report with recommendations

C. Quick Brand Audit

Fast assessment of brand health
Checking for consistency issues
Output: Quick audit checklist with scores

D. Brand Guidelines Creation

Documenting existing brand elements
Formalizing standards and rules
Output: Professional brand guidelines
Step 2: Gather Brand Information

Collect relevant information based on analysis type. Use the questions from references/brand_analysis_framework.md as a guide.

Essential Information:

Brand name and tagline
Mission and vision statements
Core values
Target audience details
Industry and competitive context
Existing brand materials (if any)

Visual Identity Information:

Logo and variations
Color palette (with codes)
Typography (font families)
Imagery style preferences
Design elements

Voice and Messaging:

Brand personality traits
Tone of voice
Key messages
Value proposition
Language preferences

Additional Context:

Brand history and evolution
Customer perception
Competitive positioning
Business goals
Brand touchpoints
Step 3: Analyze Brand Archetype

Identify the brand's personality using the 12 archetypes framework from references/brand_archetypes.md.

Analysis Process:

Review brand's core desire and goals
Assess personality traits and values
Consider target audience aspirations
Evaluate competitive positioning
Identify primary archetype (60-70% influence)
Identify secondary archetype (30-40% influence)

Archetypes Quick Reference:

Innocent: Happiness, optimism, simplicity
Sage: Knowledge, wisdom, expertise
Explorer: Freedom, adventure, discovery
Outlaw: Rebellion, disruption, change
Magician: Transformation, vision, innovation
Hero: Courage, achievement, mastery
Lover: Passion, intimacy, beauty
Jester: Fun, humor, enjoyment
Everyman: Belonging, authenticity, relatability
Caregiver: Nurturing, protection, support
Ruler: Control, leadership, success
Creator: Innovation, imagination, artistic expression

Load references/brand_archetypes.md for detailed characteristics, visual directions, and messaging patterns for each archetype.

Step 4: Conduct Brand Analysis

Perform comprehensive analysis using the framework from references/brand_analysis_framework.md.

Key Analysis Areas:

1. Brand Identity

Mission/vision clarity and alignment
Values authenticity and consistency
Personality definition and expression
Archetype fit and application

2. Visual Identity

Logo effectiveness and variations
Color palette appropriateness and accessibility
Typography hierarchy and readability
Imagery style consistency
Overall visual coherence

3. Voice and Messaging

Voice consistency across channels
Tone adaptation for contexts
Message clarity and relevance
Language effectiveness
Value proposition strength

4. Target Audience Alignment

Audience definition completeness
Brand-audience fit
Messaging resonance
Visual appeal to audience
Problem-solution alignment

5. Market Position

Competitive differentiation
Unique value proposition
Market positioning clarity
Brand promise delivery

6. Brand Consistency

Cross-channel consistency
Touchpoint alignment
Quality standards maintenance
Experience coherence
Step 5: Generate Output Document

Create the appropriate deliverable based on analysis type using templates from assets/.

Output Options:

A. Brand Guidelines Document (assets/brand_guidelines_template.md)

Complete, professional brand guidelines
Includes all identity elements
Usage rules and examples
Application across channels
Resource section

B. Brand Analysis Report (assets/brand_analysis_report_template.md)

Comprehensive analysis findings
Strengths and opportunities
Competitive positioning
Recommendations and roadmap
Success metrics

C. Quick Brand Audit (assets/quick_brand_audit_template.md)

Rapid assessment checklist
Health scores by category
Priority action items
Consistency check across channels

File Naming Convention:

Guidelines: brand-guidelines-BRANDNAME-YYYY-MM-DD.md
Analysis: brand-analysis-BRANDNAME-YYYY-MM-DD.md
Audit: brand-audit-BRANDNAME-YYYY-MM-DD.md

Storage Location: Create in project root or in brand-documents/ directory if multiple documents.

Step 6: Provide Recommendations

Based on analysis, provide actionable recommendations:

Prioritization Framework:

High Impact + Low Effort: Quick wins - do immediately
High Impact + High Effort: Strategic initiatives - plan carefully
Low Impact + Low Effort: Nice-to-haves - do when possible
Low Impact + High Effort: Avoid - not worth resources

Recommendation Categories:

Visual Identity Improvements: Logo refinements, color adjustments, typography updates
Voice and Messaging: Tone consistency, message clarification, language refinement
Documentation: Creating or updating guidelines, standards documentation
Consistency: Fixing inconsistencies across touchpoints
Strategic: Repositioning, rebranding, major initiatives
Step 7: Create Implementation Roadmap

Provide phased approach for implementing recommendations:

Phase 1: Immediate (0-30 days)

Critical fixes
Quick wins
Documentation updates
High-priority inconsistencies

Phase 2: Short-term (1-3 months)

Medium-priority improvements
Guideline development
Team training
Channel optimization

Phase 3: Long-term (3-6+ months)

Strategic initiatives
Major redesigns
Comprehensive rollouts
Measurement and refinement
Advanced Features
Competitive Brand Analysis

When comparing to competitors:

Identify 3-5 key competitors
Analyze their positioning and differentiation
Map brand attributes on positioning matrix
Identify gaps and opportunities
Recommend differentiation strategy
Brand Health Scoring

Provide quantitative assessments:

Visual Identity: Logo, colors, typography coherence
Brand Foundation: Mission, values, personality clarity
Voice & Messaging: Consistency and effectiveness
Consistency: Cross-channel alignment
Audience Alignment: Target fit and appeal
Differentiation: Competitive uniqueness
Documentation: Guidelines completeness

Scale: 1-10 for each category, with overall average.

Multi-Channel Audit

Assess brand consistency across touchpoints:

Website
Social media (platform-specific)
Email communications
Print materials
Packaging
Signage and environmental
Customer service
Product/service delivery
Usage Examples
Example 1: New Brand Guidelines

User Request: "Create comprehensive brand guidelines for our eco-friendly packaging startup called GreenWrap."

Execution:

Ask discovery questions about mission, values, target audience
Gather visual identity details (colors, fonts, logo variations)
Identify brand archetype (likely Explorer or Caregiver)
Reference references/brand_analysis_framework.md for structure
Use assets/brand_guidelines_template.md as base
Fill in all sections with specific details
Save as brand-guidelines-greenwrap-2025-03-15.md
Provide implementation recommendations
Example 2: Brand Audit

User Request: "Audit our existing brand for consistency issues."

Execution:

Request access to brand materials across channels
Use references/brand_analysis_framework.md audit checklist
Assess each brand element category
Score consistency across touchpoints
Identify gaps and inconsistencies
Use assets/quick_brand_audit_template.md
Complete all checklist items with findings
Provide prioritized action items
Save as brand-audit-[name]-[date].md
Example 3: Brand Analysis with Recommendations

User Request: "Analyze our tech startup brand and suggest improvements."

Execution:

Gather current brand information
Load references/brand_archetypes.md to identify archetype
Use references/brand_analysis_framework.md for analysis structure
Evaluate all brand elements (visual, voice, positioning)
Assess competitive differentiation
Identify strengths and opportunities
Use assets/brand_analysis_report_template.md
Complete comprehensive report with scores
Provide implementation roadmap
Save as brand-analysis-[name]-[date].md
Reference Files

This skill includes detailed reference documentation:

references/brand_analysis_framework.md

Comprehensive framework covering:

Core brand elements (identity, visual, voice, audience, position)
Discovery and analysis questions
Brand consistency checkpoints
Guideline categories and structure
Audit checklists
Output frameworks

When to load: For any brand analysis or guidelines creation to ensure comprehensive coverage.

references/brand_archetypes.md

Complete guide to Jung's 12 brand archetypes:

Detailed descriptions of each archetype
Core desires, goals, and strategies
Voice and visual characteristics
Example brands for each type
How to identify and apply archetypes
Mixed archetype strategies

When to load: When identifying brand personality or determining visual/voice direction.

Asset Templates

This skill includes three professional templates in assets/:

brand_guidelines_template.md

Complete brand guidelines document template with sections for:

Brand story and foundation
Visual identity (logo, colors, typography, imagery)
Voice and messaging
Brand applications (digital, print, environmental)
Usage examples and checklist
brand_analysis_report_template.md

Comprehensive analysis report template covering:

Executive summary and key findings
Detailed analysis of all brand elements
Competitive positioning
Touchpoint audit
Strengths and opportunities
Implementation roadmap with phases
Success metrics
quick_brand_audit_template.md

Rapid assessment checklist including:

Visual identity verification
Brand foundation check
Voice and messaging evaluation
Consistency across channels
Audience alignment assessment
Competitive position review
Health scores and priority actions
Best Practices
Discovery Phase
Ask open-ended questions to understand brand deeply
Review all existing materials before making recommendations
Understand business goals and how brand supports them
Consider customer perspective and perception
Analysis Phase
Use both references files for comprehensive framework
Be objective in assessments - identify both strengths and gaps
Provide specific examples when noting issues
Consider industry context and competitive landscape
Documentation Phase
Use clear, actionable language
Include specific measurements and standards
Provide both good and bad examples
Make guidelines accessible and easy to follow
Recommendation Phase
Prioritize based on impact and effort
Provide rationale for each recommendation
Include estimated timelines and resources
Connect recommendations to business goals
Follow-up
Suggest regular brand audits (quarterly or bi-annually)
Recommend brand guideline updates as brand evolves
Provide guidance on implementing changes
Offer to create supporting materials
Common Scenarios
Scenario 1: Inconsistent Brand

Symptoms: Different colors/fonts across channels, unclear messaging Approach: Quick audit → Identify inconsistencies → Prioritize fixes → Create guidelines Output: Quick audit + Brand guidelines document

Scenario 2: Undefined Brand

Symptoms: No clear values, personality, or visual standards Approach: Discovery → Define all elements → Document in guidelines Output: Complete brand guidelines document

Scenario 3: Rebranding

Symptoms: Old brand doesn't fit current direction Approach: Full analysis → Competitive positioning → New identity development Output: Brand analysis report + New brand guidelines

Scenario 4: Brand Expansion

Symptoms: Entering new market or launching new product line Approach: Review core brand → Adapt for new context → Extension guidelines Output: Brand guidelines with extension sections

Tips for Effective Brand Analysis
Start with Why: Understanding purpose drives better brand decisions
Think Long-term: Brand should be enduring, not trendy
Stay Authentic: Brand must reflect true organizational values
Be Consistent: Repetition builds recognition
Consider Context: Brand exists in competitive and cultural context
Measure Impact: Track brand health metrics over time
Evolve Thoughtfully: Brands should evolve, but deliberately
Empower Team: Guidelines should enable, not restrict creativity
Weekly Installs
640
Repository
ailabs-393/ai-l…e-skills
GitHub Stars
357
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass