---
rating: ⭐⭐
title: xapi specification
url: https://skills.sh/tim80411/ai-agent-extension/xapi-specification
---

# xapi specification

skills/tim80411/ai-agent-extension/xAPI Specification
xAPI Specification
Installation
$ npx skills add https://github.com/tim80411/ai-agent-extension --skill 'xAPI Specification'
SKILL.md
xAPI Specification Knowledge Base

Provide comprehensive guidance on xAPI (Experience API) specification for educational assessment and learning analytics.

Core Concepts
Statement Structure

An xAPI Statement follows the "Actor-Verb-Object" pattern with optional Result and Context:

{
  "actor": { },      // Who performed the action
  "verb": { },       // What action was performed
  "object": { },     // What was acted upon
  "result": { },     // Outcome of the action (optional)
  "context": { },    // Additional context (optional)
  "timestamp": "",   // When the action occurred
  "id": ""           // Unique statement identifier (UUID)
}

Required Fields
Actor - Agent or Group performing the action
Verb - Action taken (URI + display name)
Object - Activity, Agent, or Statement Reference
Actor Types

Agent (single learner):

{
  "objectType": "Agent",
  "name": "Learner Name",
  "mbox": "mailto:learner@example.com"
}


Account-based identification (recommended for LMS):

{
  "objectType": "Agent",
  "account": {
    "homePage": "https://lms.example.com",
    "name": "user123"
  }
}

Verb Structure

Define verbs with URI identifier and display text:

{
  "id": "http://adlnet.gov/expapi/verbs/answered",
  "display": {
    "en-US": "answered"
  }
}


Consult references/verbs.md for the complete ADL and cmi5 verb registry.

Object (Activity) Structure
{
  "objectType": "Activity",
  "id": "https://example.com/activities/quiz-123",
  "definition": {
    "name": { "en-US": "Quiz on xAPI Basics" },
    "description": { "en-US": "A quiz testing knowledge of xAPI" },
    "type": "http://adlnet.gov/expapi/activities/assessment"
  }
}

Result Structure

Capture assessment outcomes:

{
  "score": {
    "scaled": 0.85,
    "raw": 85,
    "min": 0,
    "max": 100
  },
  "success": true,
  "completion": true,
  "response": "choice-a",
  "duration": "PT30S"
}


Duration format: ISO 8601 duration (PT = Period Time, e.g., PT1H30M = 1 hour 30 minutes)

Context Structure

Provide additional information about the learning experience:

{
  "registration": "uuid-for-attempt",
  "contextActivities": {
    "parent": [{ "id": "https://example.com/course-123" }],
    "grouping": [{ "id": "https://example.com/program-abc" }],
    "category": [{ "id": "https://w3id.org/xapi/cmi5/context/categories/cmi5" }]
  },
  "platform": "Example LMS",
  "language": "en-US"
}

Interaction Types for Assessments

xAPI supports these interaction types for quiz questions:

Type	Description	Use Case
true-false	Binary choice	Yes/No, True/False questions
choice	Multiple choice	Single or multiple selection
fill-in	Text input	Short answer questions
long-fill-in	Long text	Essay questions
matching	Pair matching	Match items from two lists
performance	Task steps	Procedural tasks
sequencing	Order items	Arrange in correct sequence
likert	Scale rating	Survey/opinion questions
numeric	Number input	Mathematical answers

Consult references/interaction-types.md for detailed examples of each type.

Activity Types

Common activity types for educational contexts:

Category	Type URI	Use Case
Assessment	http://adlnet.gov/expapi/activities/assessment	Quizzes, exams
Question	http://adlnet.gov/expapi/activities/cmi.interaction	Individual questions
Course	http://adlnet.gov/expapi/activities/course	Course container
Module	http://adlnet.gov/expapi/activities/module	Course sections
Lesson	http://adlnet.gov/expapi/activities/lesson	Individual lessons

Consult references/activity-types.md for the complete registry.

cmi5 Profile

cmi5 is a standardized xAPI profile for e-learning. Key requirements:

Defined verbs: launched, initialized, completed, passed, failed, abandoned, waived, terminated
Mandatory context: registration, sessionId, masteryScore
Required extensions: sessionId, launchMode, launchURL

For cmi5-compliant statements, consult references/cmi5-profile.md.

Statement Generation Workflow

To generate a valid xAPI statement:

Identify the Actor (learner/user information)
Select appropriate Verb from ADL registry
Define the Object (activity being tracked)
Include Result for assessment outcomes
Add Context for hierarchical relationships
Generate UUID for statement ID
Add timestamp in ISO 8601 format
Validation Checklist

Validate statements against these criteria:

Structural validation:

 Actor has valid identifier (mbox, account, or openid)
 Verb has id (URI) and display (language map)
 Object has id and objectType

Vocabulary validation:

 Verb URI matches ADL/cmi5 registry
 Activity type URI is valid

cmi5 validation:

 Context includes registration UUID
 Context includes sessionId extension
 Correct verb sequence (launched → initialized → ... → terminated)

Interaction validation:

 interactionType matches response format
 correctResponsesPattern format matches interactionType
 choices/scale/source/target arrays are valid for type
Additional Resources
Reference Files

Detailed specifications and registries:

references/verbs.md - Complete ADL and cmi5 verb registry
references/activity-types.md - Activity type URIs and usage
references/interaction-types.md - Detailed interaction type examples
references/cmi5-profile.md - cmi5 requirements and extensions
External Resources
xAPI Specification
ADL Vocabulary
cmi5 Specification
Weekly Installs
–
Repository
tim80411/ai-age…xtension
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass