---
title: write-notes
url: https://skills.sh/p-2411/write-notes/write-notes
---

# write-notes

skills/p-2411/write-notes/write-notes
write-notes
Installation
$ npx skills add https://github.com/p-2411/write-notes --skill write-notes
SKILL.md
Writing Lecture Notes from Slide PDFs

Turn lecture PDFs into a linked concept graph inside an Obsidian vault — one topic folder per lecture, one markdown file per concept, plus a positioned .canvas view.

Core principles
The PDF is the only source of concepts. If a concept is not explicitly named or clearly introduced in the pdftotext output, it does NOT become a note — no matter how canonical, standard, or "obviously related" it is to the lecture topic. See Do not invent concepts below.
General knowledge is for explaining, not extending. You may use your own knowledge to flesh out an explanation, add an illustrative example, or phrase a definition clearly — but only for concepts the PDF already introduces.
One concept per note. Never dump a whole lecture into one file.
Group notes by lecture topic. Every concept from a lecture goes inside a folder named after that lecture's hub concept — never at the course root. See the path convention below.
Link aggressively — within the verified set. Use [[wikilinks]] for every concept that has (or should have) its own note, but never wikilink to a concept the PDF doesn't mention. Forward-links to future lectures are fine only if the current PDF explicitly names the future concept.
Stay within the course. Do not link across course folders.
Merge, don't overwrite. If a note exists, integrate new material and preserve existing structure.
Cite the PDF, not slide numbers. E.g. CS101 Lecture — 03_DesignByContract.pdf.
Ask before you assume inputs. If the user didn't specify a PDF path, a vault location, or a canvas file, ask — do not invent defaults. See Inputs below.
Do not invent concepts

Completeness means what the lecture covered, not what the topic canonically includes.

Lectures are deliberately narrower than textbooks. If a microservices lecture skips Circuit Breaker / Saga / Bulkhead, those concepts are not examinable and must not appear in the notes. Adding them pollutes the vault with material the student hasn't been taught and may contradict the lecturer's framing.

Rationalizations to reject
Excuse	Reality
"This concept is standard for this topic."	PDF is the source of truth, not the field's canon.
"Adding it makes the graph more complete."	Completeness = the lecture's scope, not the topic's scope.
"The concept is implied even if not named."	Implied ≠ covered. Do not create the note.
"It's only one extra concept."	One hallucinated concept invites ten more. Zero tolerance.
"The PDF mentions it once in a diagram / example."	A passing mention is not an introduction. Only create a note if the PDF names and describes the concept.
"The student will want to know this eventually."	Then they'll get it in the lecture that covers it, or add it themselves.
"I can mark it as 'extension material'."	No. Unverified concepts are excluded entirely.
Red flags — STOP if you catch yourself thinking any of these
"What are the standard sub-topics under X?"
"To be complete I should add…"
"This lecture briefly mentioned Y, and Y is usually explained alongside Z, so Z should have a note too."
Writing a note whose body relies on details the PDF doesn't contain.
Adding a wikilink to a concept name that never appeared in the pdftotext output.
When to use
User gives one or more PDF paths and asks for notes.
User references lecture slides in the vault and wants them processed.
User asks for "study notes from these slides" or similar.
Inputs

Gather these before any work:

Input	Required?	Default
PDF source	Yes	—
Vault root	Yes	—
Course name	No	Infer from PDF folder name or ask
Canvas path	No	<Vault>/<Course>.canvas (create if missing)
PDF source

Accept either:

A file path (one PDF).
A directory path — list every .pdf inside, show the user the list, and confirm the processing order before starting.
A glob (e.g. ~/slides/*.pdf).

If the user invokes this skill without specifying any PDF, ask:

Which lecture PDF(s) should I process? Give me a file path, a directory containing PDFs, or a glob.

Do not process "whatever's in the current directory" as a default. Do not silently skip PDFs that didn't parse.

Vault root

The Obsidian vault's root. If unspecified:

If the current working directory contains .obsidian/, offer it as a suggestion.
Otherwise ask: "Which Obsidian vault should I add notes to?"

Never create a brand-new vault without explicit permission.

Canvas path
If the user provides an existing canvas (e.g. architecture-map.canvas), use that file — load, mutate, save.
Otherwise default to <Vault>/<Course>.canvas. Create if absent, as an empty {"nodes":[],"edges":[]}.

Do not write canvas data into a file you weren't told to touch.

Never assume inputs you weren't given

If any required input is missing, ASK BEFORE PROCEEDING. Rationalizations to reject:

Excuse	Reality
"The obvious PDF is in ~/Desktop."	Ask — don't guess the user's filesystem.
"I'll just use the cwd as the vault."	Cwd ≠ vault. Confirm first.
"The course name is obvious from the folder."	Confirm; do not assume the folder name equals the course.
Execution mode

Pick one based on batch size:

1–3 PDFs → single-agent mode. The main agent does everything. Simpler; keeps full context for cross-lecture linking.
4+ PDFs → subagent-per-PDF mode. For each PDF, dispatch a subagent (via the Agent tool) to do steps 1–4 only: survey, plan, extract visuals, draft note contents. The subagent returns a compact structured result — do NOT have it write files or touch the canvas. The main agent then performs the merge into existing notes (step 4 write) and the canvas update (step 5) serially, so shared state (existing notes, canvas positions) stays consistent.

Subagent output schema (JSON in the final message):

{
  "course": "CS101",
  "topic": "Design by Contract",
  "concepts": [
    {
      "name": "Preconditions",
      "path": "CS101/Content/Design by Contract/Preconditions.md",
      "tier_hint": "leaf",
      "parents": ["Design by Contract"],
      "wikilinks": ["Design by Contract", "Assertions"],
      "pdf_evidence": "A pre-condition must be true before the method executes — the caller's obligation.",
      "body": "<full markdown body, including ## References footer>"
    }
  ],
  "pdf_filename": "03_DesignByContract.pdf"
}


pdf_evidence is mandatory. It must be a verbatim snippet from the pdftotext output that names and introduces the concept. No evidence = no note. The main agent rejects any concept without a plausible evidence quote.

The main agent then: validates every returned concept has a pdf_evidence string, spot-checks 2–3 of the evidence quotes against the pdftotext output, rejects and sends back any concept that fails, checks each concept's path, merges or creates, updates the canvas using the full set of verified concepts across all subagent returns.

If the subagent returns more than ~8 concepts from a single short lecture (≤25 slides), treat it as a hallucination warning sign and re-run grep-verification on every concept before proceeding.

Workflow

Process lectures one PDF at a time (even in subagent mode — dispatch sequentially, merging each before the next, so later subagents can be told which notes already exist). Do not parallelise across PDFs — each one needs its own survey → plan → write cycle so concept maps stay coherent.

1. Survey (cheap text pass)

Run pdftotext <path> - to get the full lecture text. Save the output — you will grep against it in step 1.5. From the text, identify:

Course (confirmed with the user, or inferred from the PDF path — e.g. CS101)
Lecture topic (hub concept, e.g. "Design by Contract") — this becomes both the hub note name AND the topic folder name.
Candidate concepts — distinct ideas the PDF explicitly names or introduces. For each, record a short verbatim quote from the pdftotext output that introduces the concept. This becomes the pdf_evidence field.
Slide ranges where each concept lives (for the next step)

Do not add concepts you merely expect the topic to include. If the PDF doesn't mention it, it isn't a candidate.

1.5. Grep-verify the candidate list (mandatory)

For every candidate concept, run a case-insensitive grep against the pdftotext output:

pdftotext <path> - | grep -iE "concept name|obvious paraphrase"


Rules:

Zero hits and no obvious paraphrase present → delete the candidate. It is hallucinated.
One passing mention inside an example/diagram caption → not enough. The PDF must introduce the concept (define, describe, list as a bullet, or give it a section heading). Delete the candidate if it only appears inside a worked example's body.
Multiple references, clearly introduced → keep.

Record the grep results you relied on. The pdf_evidence in the subagent's JSON output must cite a specific hit from this step.

If you find yourself grepping for synonyms to "rescue" a candidate you wanted to include — stop. That is the rationalization described in Do not invent concepts. The only legitimate paraphrase is one the PDF itself uses (e.g. "pre-condition" vs "precondition").

2. Plan

Build a concept tree using only the grep-verified candidates: hub → direct sub-concepts → recursive sub-concepts.

Path convention (topic folder per lecture)

Every note goes inside a topic folder named after the lecture's hub concept:

<Vault>/<Course>/Content/<Topic>/<Concept>.md


Example — a "Design by Contract" lecture produces:

<Vault>/CS101/Content/Design by Contract/Design by Contract.md ← hub
<Vault>/CS101/Content/Design by Contract/Preconditions.md
<Vault>/CS101/Content/Design by Contract/Postconditions.md
<Vault>/CS101/Content/Design by Contract/Class Invariants.md

Do not flatten concepts directly into <Course>/ or into <Course>/Content/. Topic folders scope each lecture's notes so the vault stays browsable as it grows.

If the user's vault already uses a different structure (e.g. flat), confirm the deviation explicitly before following it. Don't silently mirror what's there — ask.

Existing-note check

For each concept, check whether a note already exists at the expected path. Also search the whole course folder in case the topic folder is named slightly differently (e.g. "DbC" vs "Design by Contract"). Mark each node create or merge.

3. Targeted visual extraction

For slides containing diagrams, code, worked examples, or tables worth preserving, use the Read tool directly on the PDF with the pages parameter for just those pages. Don't read the whole PDF as images — it's wasteful.

4. Write notes

Follow the existing vault style exactly. Example structure:

A **pre-condition** is a condition or predicate that must always be true just **prior** to the execution of some section of code — it is the caller's obligation in a [[Design by Contract]] specification.

## Key points

- If a precondition is **violated**, the effect becomes **undefined**.
- ...

## Example

```java
// code from the slide, cleaned up

References
CS101 Lecture — 03_DesignByContract.pdf

Style rules:

- Opening sentence defines the concept and wikilinks to parent/related ideas.
- Use `**bold**` for emphasis on key terms.
- Section headings (`##`) are topical (`Key points`, `Example`, `In inheritance`, etc.) — do NOT include slide numbers.
- Code blocks use fenced syntax with the right language.
- Footer is a `## References` section naming the PDF file only.
- Every concept name that has (or could have) its own note — **and is present in the verified concept list for this or a previous lecture** — becomes a `[[wikilink]]`. Never wikilink to a concept that no PDF has introduced.

**Using general knowledge for explanation (allowed):**

- Fleshing out a definition the PDF states tersely.
- Providing an extra illustrative example that matches the lecture's framing.
- Rephrasing for clarity while preserving the PDF's meaning.

**Using general knowledge for extension (forbidden):**

- Introducing related sub-concepts the PDF doesn't name (even as a sub-bullet).
- Adding a `##` section about a topic the PDF doesn't cover.
- Citing mechanisms, patterns, or examples that pull in new terminology not in the PDF.
- Expanding a brief slide into a multi-section deep dive that goes beyond what was taught.

If a `##` section in your draft can't be traced back to specific PDF content, delete it.

**Merging:** when a note exists, read it first. Add new bullets/sections at the natural place, add missing wikilinks, extend the `## References` footer with the new PDF if different. Preserve the author's existing wording. The same no-extension rule applies to merges — new material must come from the current PDF.

### 5. Update canvas

#### Resolve the canvas path

1. **User-provided canvas path** — use it directly. Read, mutate, save.
2. **Otherwise** — use `<Vault>/<Course>.canvas`.
3. **If the file doesn't exist** — create it, initialised as `{"nodes":[],"edges":[]}`.

Always read the current canvas before writing so you preserve existing nodes and edges.

Canvas JSON schema:

```json
{
  "nodes": [
    {"id": "<16-hex>", "type": "file", "file": "<Course>/Content/<Topic>/<Name>.md",
     "x": 0, "y": 0, "width": 400, "height": 400, "color": "5"}
  ],
  "edges": [
    {"id": "<16-hex>", "fromNode": "<id>", "fromSide": "top",
     "toNode": "<id>", "toSide": "bottom"}
  ]
}


Rules:

Preserve existing node positions. Only place/resize new nodes; never move existing ones.
Generate id as a random 16-char hex string.
Write valid JSON (Obsidian is strict — no trailing commas, no comments).

Importance tiers — before placing, count each concept's degree (how many other concepts link to/from it). Assign a tier:

Tier	When	Size	Color
Hub	Lecture topic, or degree ≥ 6	680×420	"5"
Core	Degree 3–5 (dense branching)	520×360	"4"
Leaf	Degree 1–2	400×280	(omit color)

A concept with many outgoing arrows is a "core" node — make it visibly bigger and coloured even if it isn't the lecture's top-level hub. Recompute tiers each run so a node promoted by new lectures gets resized.

Layout philosophy: aim for an organic, flowing graph — not a rigid ring or grid. Think of concepts drifting outward from their parent like branches of a tree, with some asymmetry. Perfect symmetry looks sterile; slight irregularity reads as natural.

Layout algorithm:

Place the hub at its existing position, or ≥1200 px from the nearest existing hub if new.
For a parent's children, pick a broad angular region (e.g. 120°–180° arc) on the side facing away from the rest of the graph. Within that arc, distribute children at varied radii (roughly 700–1000 px for core nodes, 450–650 px for leaves off a core) and uneven angular gaps — don't snap to equal spacing. Small jitter (±10–15%) is better than clockwork.
Follow the natural branching: a core node's leaves should fan out beyond it, continuing the flow outward rather than curling back toward the hub.
Minimum spacing: 120 px gap between any two node bounding boxes. If a candidate position overlaps, nudge outward or sideways until clear — keep the nudge small so the flow isn't disrupted.
Arrow routing: pick fromSide/toSide based on relative position:
child above parent → fromSide: "top", toSide: "bottom"
child below → "bottom" / "top"
child left/right → "left"/"right" symmetrically Choose whichever axis (horizontal vs vertical) has the greater displacement. This prevents arrows cutting diagonally across nodes.
Add edges: parent hub → each direct sub-concept, plus edges between already-placed concepts wherever wikilinks exist between them.
6. Next PDF

Only after the current PDF is fully written (notes + canvas updated), move to the next. Report progress to the user between PDFs.

Quick reference
Task	Tool
Survey PDF text	Bash: pdftotext <path> -
Grep-verify a candidate concept	Bash: pdftotext <path> - | grep -iE "name|paraphrase"
Extract diagrams/code from specific slides	Read with pages: "N-M"
Read existing note before merging	Read
Create new note	Write
Merge into existing note	Edit
Update canvas	Read then Write (parse JSON, mutate, re-serialise)
Common mistakes
Hallucinating canonical concepts not in the PDF. The #1 failure mode. If you're adding standard topic-X concepts because "lectures on X usually cover them", STOP — grep the pdftotext output, confirm zero hits, delete the concept. Applies to every topic.
Deep-diving a concept the PDF only names briefly. A one-line slide mention doesn't justify a multi-section note. Match the note's depth to the PDF's depth; use general knowledge only for phrasing and one short illustrative example.
Wikilinking to concepts the PDF doesn't mention. Forward-links to future-lecture concepts are allowed only if the current PDF explicitly names them (e.g. a slide listing upcoming lectures).
Dumping every concept at the course root. Every lecture's concepts belong inside a topic folder named after the lecture — never <Course>/Concept.md. See Step 2.
Processing PDFs you weren't given. If the user didn't specify which files to process, ask — don't glob the current directory.
Writing to a canvas you weren't asked to touch. Use the user-provided canvas if given; otherwise the course default. Don't pick a third file.
Writing one giant note per lecture. Split by concept.
Citing slide numbers. PDF filename only.
Linking across courses. Stay within the course folder.
Overwriting existing notes. Always merge.
Processing all PDFs in parallel. Go one at a time.
Reading the whole PDF as images. Use pdftotext first, then targeted page reads.
Dropping existing canvas nodes or moving them. Only add/position new ones.
Invalid canvas JSON (trailing commas, missing id). Obsidian silently fails to load.
Uniform node sizes. A concept that ten others link to should look different from a leaf — resize and recolour by degree.
Arrows slicing through nodes. Pick fromSide/toSide from relative position (step 5). If an arrow still crosses a node, nudge the new child further out.
Clustering new nodes on one side. Distribute around the parent — but in a flowing arc, not a strict ring.
Over-regular layout. Equal spacing and matched radii look mechanical. Vary distances and angles slightly so the graph reads as organic.
Baseline failure on record

In the development of this skill, a subagent was pointed at a 24-slide architecture lecture without these guardrails. It returned 25 notes; 13 were hallucinated — canonical topics from the wider literature that the slides never taught (resilience patterns, sagas, eventual consistency, service discovery, bounded contexts, and several service-infrastructure concepts). A pdftotext … | grep -i check confirmed zero hits for any of the distinctive terms. These concepts exist in the textbook the course references, but the lecturer chose not to teach them, so they polluted the vault with non-examinable material. The grep-verify step exists specifically to catch this pattern — pressure to "be complete" pulls the subagent toward topic-canonical completeness rather than lecture-specific fidelity.

Weekly Installs
8
Repository
p-2411/write-notes
First Seen
4 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail