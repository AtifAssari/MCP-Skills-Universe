---
title: diataxis
url: https://skills.sh/keithpatton/diataxis-agent-skill/diataxis
---

# diataxis

skills/keithpatton/diataxis-agent-skill/diataxis
diataxis
Installation
$ npx skills add https://github.com/keithpatton/diataxis-agent-skill --skill diataxis
SKILL.md
Diátaxis Documentation Governance

This skill enforces the Diátaxis framework for documentation. Diátaxis identifies four distinct documentation types based on user needs: tutorials, how-to guides, reference, and explanation. Each serves a different purpose and must be written differently.

Operating Modes

This skill operates in one of the following modes:

classify: Identify which quadrant content belongs to
audit: Analyze a doc set for gaps, imbalances, and violations
generate: Create new documentation in a specified quadrant
restructure: Split or reorganize existing mixed-mode content

The mode must be inferred from the user request or explicitly stated. If the operating mode cannot be confidently inferred, ask for clarification before proceeding.

Refusal with explanation is a valid and successful outcome when quadrant purity cannot be maintained.

Generate Mode Policy

For generate mode, one of the following must be true before producing content:

The user explicitly states the target quadrant ("write a How-to for X"), OR
The agent classifies the request, presents reasoning with confidence+evidence, and receives user confirmation
The Diátaxis Compass

Use this decision tree to classify content into exactly ONE quadrant:

If content...	...and serves user's...	...then it belongs to...
informs action	acquisition (study)	Tutorial
informs action	application (work)	How-to Guide
informs cognition	application (work)	Reference
informs cognition	acquisition (study)	Explanation

Two questions to ask:

Does this inform action (doing) or cognition (knowing)?
Does this serve acquisition (learning/study) or application (working)?
Quadrant Summary
Tutorial (learning-oriented)

A lesson that takes the learner through a practical experience. The instructor is responsible for the learner's success. Focus on doing, not explaining. Deliver results early and often. Minimize explanation. No choices or alternatives.

Form: Sequential lesson with concrete steps
Language: "We will...", "First, do X", "You'll notice that..."
Not: Teaching concepts, offering alternatives, explaining why
How-to Guide (goal-oriented)

Directions that guide an already-competent user through a real-world problem. Assumes the reader knows what they want to achieve. Focused on work, not study.

Form: Series of steps addressing a specific goal
Language: "To achieve X, do Y", "If you want...", conditional imperatives
Not: Teaching beginners, explaining concepts, describing machinery
Reference (information-oriented)

Technical description of the machinery. Austere, neutral, accurate. Structure mirrors the thing being described. The user consults it, not reads it.

Form: Structured descriptions, tables, specifications
Language: "X is...", "The options are...", factual statements
Not: Instructing, explaining why, narrative, opinions
Explanation (understanding-oriented)

Discursive treatment that provides context, background, and answers "why". Makes connections, admits opinion, circles around the subject.

Form: Prose discussion of a topic
Language: "The reason for X is...", "This is because...", "Consider..."
Not: Step-by-step procedures, technical specifications, teaching tasks
Core Workflow
For Classification
Read the content carefully
Apply the compass: action/cognition × acquisition/application
Identify the single quadrant
Report with confidence and evidence
For Generation
Confirm the target quadrant (stated or inferred with confirmation)
Apply quadrant constraints strictly
Refuse to blend quadrants; recommend splitting if needed
Validate output against quadrant characteristics
For Audit
Inventory all documentation
Classify each document
Identify gaps (missing quadrants)
Flag violations (mixed-mode, wrong quadrant)
Report imbalances (e.g., "reference-heavy, tutorial-poor")
For Restructure
Classify the existing content
Identify quadrant violations
Propose splits (one document per quadrant)
Present plan for user confirmation before changes
Output Requirements

When classifying or flagging violations, always provide:

Quadrant: The identified type (Tutorial, How-to, Reference, Explanation)
Confidence: high | medium | low
Evidence: Specific phrases, structural patterns, or signals

Example:

Classified as How-to (high confidence). Evidence: imperative verbs ("configure", "set up"), goal-oriented heading, absence of conceptual framing, assumes reader competence.

Violation Detection

Flag these anti-patterns:

Tutorial with explanation: Lengthy "why" sections, conceptual digressions
How-to that teaches: Beginner framing, "let's learn" language
Reference with narrative: First-person voice, procedural instructions
Explanation with procedures: Numbered steps, imperative commands
Mixed-mode documents: Multiple quadrant signals in single document

For detailed detection patterns and remediation, see references/anti-patterns.md.

Non-Goals

This skill does not:

Invent documentation strategy or information architecture
Decide product architecture or feature scope
Merge multiple Diátaxis quadrants into a single document
Override repository-specific documentation rules or style guides
Generate content without explicit quadrant classification
Additional Resources
Detailed quadrant characteristics: references/quadrants.md
Classification decision tree: references/compass.md
Anti-patterns and fixes: references/anti-patterns.md
Attribution

Diátaxis is the work of Daniele Procida. This skill encodes the Diátaxis framework for use by AI agents. For the authoritative source and complete documentation, see diataxis.fr.

Licensed under CC-BY-SA 4.0. Citation metadata available at the Diátaxis GitHub repository.

Weekly Installs
19
Repository
keithpatton/dia…nt-skill
GitHub Stars
8
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass