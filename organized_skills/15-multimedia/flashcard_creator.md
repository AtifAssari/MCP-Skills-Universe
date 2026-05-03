---
rating: ⭐⭐⭐
title: flashcard-creator
url: https://skills.sh/szeyu/vibe-study-skills/flashcard-creator
---

# flashcard-creator

skills/szeyu/vibe-study-skills/flashcard-creator
flashcard-creator
Installation
$ npx skills add https://github.com/szeyu/vibe-study-skills --skill flashcard-creator
SKILL.md
Flashcard Creator

Generate effective flashcards optimized for spaced repetition learning systems like Anki.

Workflow
flowchart LR
    A[Source Material] --> B[Identify Key Facts]
    B --> C[Choose Card Type]
    C --> D[Create Cards]
    D --> E[Add Mnemonics]
    E --> F[Format for Export]

Step 1: Card Design Principles
The 20 Rules of Formulating Knowledge (Summary)
Understand before memorizing - Never create cards for things you don't understand
Minimum information - Keep each card focused on ONE fact
Use cloze deletion - More effective than Q&A for many concepts
Avoid sets/lists - Break lists into individual cards or use mnemonics
Use imagery - Visual memory is powerful
Use mnemonic techniques - Acronyms, stories, memory palaces
Step 2: Card Types
Basic Card (Front → Back)
Front: What is the powerhouse of the cell?
Back: Mitochondria


Anki Format:

What is the powerhouse of the cell?	Mitochondria

Reversed Card (Both Directions)
Front: Mitochondria
Back: The powerhouse of the cell - produces ATP through cellular respiration


Anki Format (with tag):

Mitochondria	The powerhouse of the cell - produces ATP	reversed

Cloze Deletion
Text: The {{c1::mitochondria}} is the powerhouse of the cell, producing {{c2::ATP}}.


Anki Format:

The {{c1::mitochondria}} is the powerhouse of the cell, producing {{c2::ATP}}.

Step 3: Card Templates by Subject
Vocabulary/Terminology
Front: [Term]
Back: 
- Definition: [Clear definition]
- Example: [Usage in context]
- Related: [Connected terms]

Formulas
Front: Formula for [concept]?
Back: 
[Formula]
Where:
- [Variable] = [meaning]

Processes/Sequences
Front: What are the steps of [process]?
Back:
1. [Step 1]
2. [Step 2]
3. [Step 3]
Mnemonic: [Memory aid]

Dates/Events
Front: [Year]: What happened?
Back: [Event and significance]


OR

Front: When did [event] occur?
Back: [Year] - [Brief context]

Step 4: Mnemonic Techniques
Acronyms
Front: Order of operations in math?
Back: PEMDAS - Parentheses, Exponents, Multiplication, Division, Addition, Subtraction

Visual Association
Front: What is the symbol for Iron on the periodic table?
Back: Fe (think: "Fe"rris wheel made of iron)

Story Method
Front: Stages of mitosis in order?
Back: PMAT - "Please Make Another Taco"
Prophase → Metaphase → Anaphase → Telophase

Step 5: Anki Export Format
Tab-Separated Format (.txt)
Front Text<TAB>Back Text
Question 1	Answer 1
Question 2	Answer 2

With Tags
Front Text	Back Text	tag1 tag2
What is DNA?	Deoxyribonucleic acid - carries genetic information	biology genetics

Cloze Format
{{c1::Answer hidden}}
The {{c1::mitochondria}} produces ATP.

Step 6: Batch Generation Template

When creating multiple cards from a topic:

# [Topic] Flashcards

**Total Cards:** [Number]
**Deck Name:** [Subject]::[Topic]
**Tags:** [tag1] [tag2]

---

## Cards

### Card 1
**Front:** [Question/Prompt]
**Back:** [Answer/Information]

### Card 2
**Front:** [Question/Prompt]  
**Back:** [Answer/Information]

[Continue...]

---

## Anki Import Ready

[Tab-separated plain text version]

Quality Checklist
 Each card tests ONE piece of information
 Cards can be answered in <10 seconds
 No ambiguous questions with multiple valid answers
 Mnemonics added for difficult items
 Cards are context-independent (understandable alone)
 Cloze deletions used where appropriate
Weekly Installs
123
Repository
szeyu/vibe-study-skills
GitHub Stars
10
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass