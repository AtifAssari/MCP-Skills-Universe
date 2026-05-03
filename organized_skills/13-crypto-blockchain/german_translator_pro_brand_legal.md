---
rating: ⭐⭐⭐
title: german-translator-pro-brand-legal
url: https://skills.sh/slfmr1/german-translator-pro-brand-legal/german-translator-pro-brand-legal
---

# german-translator-pro-brand-legal

skills/slfmr1/german-translator-pro-brand-legal/german-translator-pro-brand-legal
german-translator-pro-brand-legal
Installation
$ npx skills add https://github.com/slfmr1/german-translator-pro-brand-legal --skill german-translator-pro-brand-legal
SKILL.md
German Translator Pro — Brand & Legal

Translate and validate English to Swiss-formal German (Hochdeutsch CH). Trained on real translation patterns crawled from 12+ top brands — not generic machine translation.

What makes this different

LLMs produce translationese — grammatically correct German that sounds translated, not written. This skill fixes that with curated reference files extracted from how top brands actually translate their websites, marketing, and legal pages.

Brands crawled: Swisscom, UBS, On Running, Logitech, IKEA CH, Stripe, Notion, Slack, Apple, Shopify, BMW, Vercel

What we extracted: 100+ real EN→DE pairs, 5 hero headline strategies, 15+ CTA patterns, Du/Sie industry split, 40+ glossary decisions (keep vs translate), 29 legal term translations, translationese traps, legal register patterns — all with brand evidence.

The agent reads these references before every translation, producing output that matches how these brands write German.

Install
npx skills add SLFMR1/german-translator-pro-brand-legal

When to Use
Translating UI strings (buttons, headings, CTAs, marketing copy) to German
Translating legal pages (privacy policy, terms of service, imprint) to German
QA-checking existing German translations against English source
Any EN → DE translation that needs Swiss conventions and natural phrasing
How It Works

The skill supports two text types and two actions:

	Brand / UI	Legal
Translate (EN → DE)	Natural, punchy Swiss-German that sounds written, not translated	Precise, formal German with DSGVO/DSG legal terminology
Validate (QA check)	Check for naturalness, accuracy, Swiss conventions	Check for legal precision, qualifier preservation, terminology
Key features
Anti-translationese — Restructures German thoughts fresh instead of mapping English sentence structures. Trained on how top brands actually write
Swiss (CH) or German (DE) locale — Swiss: ss not ß, 1'000, CHF. German: standard ß, 1.000, EUR. User chooses
Back-translation QA — Verifies meaning preservation by translating DE back to EN
Completeness checks — Catches untranslated strings AND accidentally germanized brand terms
Legal term precision — 25+ DSGVO/DSG terms with brand-confirmed translations and source fidelity rules
4-agent legal pipeline — Translator → Back-Translator → Validator → Refiner for legal documents
Configurable glossary — Keep-in-English terms, always-translate terms, split decisions — all with brand evidence
Workflow
Step 1: Determine Text Type, Action, Address Form, and Locale

Before doing any work, determine four things. If not clear from context, ask the user:

1. Text type?

UI — hero sections, CTAs, agent descriptions, navigation, headings, buttons, labels
LEGAL — privacy policy, terms of service, imprint, legal disclaimers

2. Action?

TRANSLATE — convert English to German
VALIDATE — QA-check existing German translation against English source

3. Address form?

Sie (formal) — B2B, corporate, legal, professional. Capitalized: Sie, Ihnen, Ihr, Ihre
Du (informal) — B2C apps, casual products, startups. Lowercase: du, dir, dein, deine

Default to Sie if unclear. Legal text always uses Sie regardless of user preference.

4. Locale?

Swiss (CH) — ss not ß, apostrophe thousands (1'000), CHF before amount (CHF 100), decimal point (99.90)
German (DE) — ß where standard, dot thousands (1.000), € after amount (100 €), decimal comma (99,90)

Default to Swiss (CH) if unclear.

Apply the chosen form and locale consistently throughout. Follow the matching section below.

Web research allowed. If a term is not in the glossary, or you're unsure about the right translation, look it up. Fetch the German version of a brand's website (e.g. apple.com/de, stripe.com/de, notion.so/de) to see how they actually translate it. You can also check other relevant brand websites in the same industry as the user's project. Real-world usage beats guessing.

Step 2: Multi-File Projects — Use Subagents

When translating or validating multiple files or pages, do NOT process them all in the main context. Instead, use the orchestrator/subagent pattern:

Orchestrator (main agent):

Determine the 4 settings above (text type, action, address form, locale)
List all files/pages to process
Spawn one subagent per file/page using the Agent tool
Collect results and report a summary

Each subagent:

Receives: the file path, text type, action, address form, locale
Reads the reference files (glossary, style guide, examples)
Translates or validates the single file
Self-validates against qa-checklist.md — runs the relevant checks for the text type
Fixes any CRITICAL issues found during self-validation
Reports back: the output file + a summary (PASS/FAIL, issue count, any unresolved warnings)

Why: Each subagent gets a clean context with full reference files loaded. No context blowup from processing 10+ files sequentially. Self-validation catches issues before they reach the orchestrator.

Single file? Skip this — just run the translation/validation directly.

TRANSLATE + UI

Natural, punchy Swiss-German for marketing and interface text.

Process
Read the English source JSON file completely
Read glossary.md for terms that must stay untranslated
Read swiss-german-style.md for tone, conventions, and translationese traps
Read examples.md — match this quality level
Translate every value. Never modify keys or {variable} placeholders
Self-check: Read each German value out loud. Would a Swiss product manager say this over coffee? If it sounds like a document, rewrite it
Back-translate check: For 5 random keys, mentally translate the German back to English. If the meaning shifted, fix it
Completeness check: Compare EN keys vs DE keys — zero missing. Scan for identical EN/DE values: keep-in-English terms are OK, but full English sentences left untranslated are not. Verify always-translate terms from glossary are actually translated (Products→Produkte, not "Products")
Length check: Compare character count of each DE value vs EN value. Flag any UI string (buttons, labels, nav, headings, tooltips) where DE is >120% of EN length. Shorten these — German must fit the same visual space
Output a complete JSON file with identical structure to the English source
Rules
Restructure, don't translate. Write the German thought fresh. If it reads like it was run through a translator, rewrite it
Use the address form chosen in Step 1 (Sie or Du) — apply consistently throughout
Apply the locale conventions chosen in Step 1 (CH or DE) for ß/ss, number formatting, and currency
Preserve all {variable} placeholders and HTML tags exactly
Keep JSON key names and namespace structure identical
Brand names, product names stay in English (see glossary.md)
English tech terms standard in Swiss business stay English (Agent, CRM, API, Inbox, Tools, Workflow, etc.)
Prefer verbs over nominalizations — "prüfen" not "Durchführung der Prüfung"
Prefer concrete benefits over abstract claims
Short sentences. If over 20 words, consider splitting
Length constraint (UI critical). German text expands ~20-30% vs English. UI strings must fit the same visual space — buttons, labels, nav items, headings, tooltips. If the German is noticeably longer than the English, shorten it. Prefer compact phrasing: "Jetzt starten" not "Jetzt loslegen und starten", "Mehr erfahren" not "Erfahren Sie mehr darüber". For buttons and nav: aim to match or stay within ~120% of the English character count
Output

Complete valid JSON. Same keys, same nesting, German values.

TRANSLATE + LEGAL

Precise, formal Swiss-German for legal documents. Accuracy over style.

For the full multi-agent pipeline (recommended for legal), see legal-workflow.md. It uses 4 agents: Translator → Back-Translator → Validator → Refiner. The instructions below are for the Translator agent (Agent 1).

Process
Read the English source JSON file completely
Read glossary.md for terms that must stay untranslated
Read swiss-german-style.md — apply the locale conventions (CH or DE) chosen in Step 1, but use formal legal register, not marketing tone
Translate every value with focus on legal precision and completeness
Self-check — 4 passes:
Pass 1: Back-translate every value to English. If meaning shifted → fix
Pass 2: Check every legal qualifier (may/shall/unless) is preserved with correct weight
Pass 3: Read only the German text without looking at English. Flag ambiguities
Pass 4: Completeness — diff EN keys vs DE keys (zero missing). Scan identical values: brand names and keep-in-English terms OK, untranslated legal text is CRITICAL. Verify legal section headings, consent language, and rights descriptions are all in German
Output two files:
The complete translated JSON (same structure as source)
A _review_notes.md file flagging sections that need professional legal review
Rules
Legal precision over natural flow. Accuracy of meaning is paramount. Do not rephrase for punchiness
Formal register. Legal text should sound formal and precise — "stiff" is correct here
Formal "Sie" form — always for legal text, regardless of user preference for UI
Apply the locale conventions chosen in Step 1 (CH or DE) for ß/ss, number formatting, and currency
Preserve all {variable} placeholders and HTML tags exactly
Keep JSON key names and namespace structure identical
Preserve legal terminology. Use standard DSGVO/DSG terms (see table below)
Swiss legal context (CH locale). Reference Swiss law (DSG/nDSG, OR) alongside EU references (DSGVO/GDPR) where the English mentions data protection or privacy. For DE locale, DSGVO references are sufficient
Do NOT simplify. Complex sentences keep their complexity. Legal meaning depends on precise wording
Do NOT drop qualifiers. "may", "shall", "unless", "notwithstanding" have specific legal weight: "kann", "hat zu" (not "soll" — "soll" is weaker, closer to "should"), "sofern nicht", "ungeachtet"
Flag jurisdiction-specific clauses — courts, regulators, applicable law references go in the review notes
Source fidelity. Translate what the source says, not what it should say. If the source uses "personal information" (informal), translate as "persönliche Informationen" — do NOT upgrade to "personenbezogene Daten" (which is the DSGVO term for "personal data"). Only use formal legal terms when the source uses the corresponding formal English term
No right escalation. If the source says "opt out", translate as "abmelden" or "ablehnen" — do NOT escalate to "widersprechen" (formal DSGVO right of objection under Art. 21). Match the weight of the source
Complete compound nouns. German compound truncation ("Rechts- oder Behörden...") must be grammatically complete. "Rechts- oder Behördenanfragen" is correct. "Rechts- oder Behörden" alone is not — the compound base word must appear at least once
Legal Term Translations
English	German	Notes
personal data	personenbezogene Daten	DSGVO standard
data processing	Datenverarbeitung	
data controller	Verantwortlicher	
data processor	Auftragsverarbeiter	
consent	Einwilligung	not "Zustimmung" in GDPR context
legitimate interest	berechtigtes Interesse	
data subject	betroffene Person	
right to erasure	Recht auf Löschung	
terms of service	Nutzungsbedingungen	or AGB
liability	Haftung	
indemnification	Freistellung / Schadloshaltung	
governing law	anwendbares Recht	
severability	Salvatorische Klausel	
intellectual property	geistiges Eigentum	
data protection	Datenschutz	
data retention	Datenaufbewahrung	
data transfer	Datenübermittlung	Apple, Stripe
legal basis	Rechtsgrundlage	Apple, Stripe
supervisory authority	Aufsichtsbehörde	Apple
Data Protection Officer	Datenschutzbeauftragter	Apple, Stripe
Standard Contractual Clauses	Standardvertragsklauseln	Apple, Stripe, Slack
right to access	Auskunftsrecht	Apple
right to rectification	Recht auf Berichtigung	Apple
right to object	Widerspruchsrecht	Logitech
right to data portability	Recht auf Datenübertragbarkeit	Logitech
GDPR	DSGVO (Datenschutz-Grundverordnung)	Always "DSGVO" in DE, never "GDPR"
FADP / Swiss DPA	DSG (Bundesgesetz über den Datenschutz)	Stripe, IKEA
FDPIC	EDÖB	Swiss federal data protection authority
as is / as available	wie besehen / wie verfügbar	Shopify — warranty disclaimer
Output

Two files:

Complete valid JSON — same keys, same nesting, German values
_review_notes.md:
# Legal Translation Review Notes: [filename]

## Sections Requiring Professional Legal Review
- [key.path]: Reason

## Translation Decisions
- [key.path]: "Chose X over Y because..."

## Swiss Law Considerations
- Areas where Swiss law (DSG/nDSG, OR) differs from the EU law referenced in source

VALIDATE + UI

QA-check German UI/marketing translations for naturalness, accuracy, and Swiss conventions.

Process
Read both the English source and German translation JSON files
Read glossary.md and swiss-german-style.md
Read examples.md — compare translations against these benchmarks
Read qa-checklist.md — run the Structural, Accuracy, Naturalness, Tone & Style (UI), Linguistic (UI), and Completeness sections
Back-translation check: For each DE value, mentally translate it back to English. Mismatch → CRITICAL (meaning error) or WARNING (nuance drift)
Naturalness check: Does this sound written in German or translated from English? Flag translationese as WARNING
Completeness check: Run the full Completeness routine from qa-checklist.md:
Identify all keys where EN value === DE value (identical-value scan)
For each, classify: keep-in-English term → OK, brand name → OK, URL/email/number → OK, actual untranslated text → CRITICAL
Cross-check against glossary: no accidentally translated keep-in-English terms, no English left for always-translate terms
Verify all navigation terms, CTAs, and common UI patterns are translated per brand-crawl evidence
Length check: Compare character count of each DE value vs EN value. Flag UI strings (buttons, labels, nav, headings, tooltips) where DE is >120% of EN length as WARNING — these may break layout
Web crosscheck: For any translation you're unsure about or that feels off, fetch the German version of a relevant brand website to verify how they translate it. Spot-check at least 5 key terms against real brand usage
Report findings grouped by severity
VALIDATE + LEGAL

QA-check German legal translations for precision, terminology, and legal correctness.

If a back-translation file is available (from the legal-workflow.md pipeline), use it in step 4 below. This catches meaning errors that bilingual review misses — a reviewer unconsciously imports the correct meaning from the source, but a back-translation reveals what the German text actually says in isolation.

Process
Read both the English source and German translation JSON files
Read glossary.md and swiss-german-style.md
Read qa-checklist.md — run the Structural, Accuracy, Tone & Style (Legal), Linguistic (Legal), Legal-Specific, and Completeness sections
Back-translation diff (if back-translation file provided): Compare original EN with back-translated EN, key by key. Flag divergences:
Meaning matches → OK
Slight nuance drift → WARNING
Material change (obligation→permission, condition dropped, scope changed) → CRITICAL
Blind read: Read ONLY the German text without looking at English. Flag anything unclear or ambiguous as a standalone German legal document
Precision check: Are legal qualifiers ("may", "shall", "unless") translated with full legal weight? Are complex conditions preserved without simplification?
Completeness check: Run the full Completeness routine from qa-checklist.md:
Identical-value scan: classify every key where EN === DE (keep-in-English → OK, brand name → OK, actual untranslated text → CRITICAL)
Cross-check against glossary: keep-in-English terms not accidentally translated, always-translate terms not left in English
Legal-specific: verify legal section headings, consent language, rights descriptions are all translated — never left in English
Web crosscheck: For any legal term or translation you're unsure about, fetch the German version of a relevant brand's legal pages (e.g. apple.com/de/privacy, stripe.com/de/legal) to verify standard usage. Spot-check at least 5 key legal terms against real brand usage
Report findings grouped by severity
Severity Levels (Both VALIDATE Modes)
CRITICAL: Missing keys, broken placeholders, broken JSON, meaning errors, legal inaccuracies
WARNING: Tone issues, phrasing problems, terminology inconsistencies, Bundesdeutsch instead of Swiss
INFO: Style suggestions, alternative phrasings, minor improvements
Output Format (Both VALIDATE Modes)
## Validation Report: [filename]
### Text type: [UI / LEGAL]

### CRITICAL (X issues)
- [key.path]: Description of issue

### WARNING (X issues)
- [key.path]: Description of issue | Suggestion: ...

### INFO (X suggestions)
- [key.path]: Suggestion

### Summary
X critical | X warnings | X info — [PASS/FAIL]


FAIL if any CRITICAL issues exist. PASS otherwise.

Resources
references/examples.md — Real EN→DE translation examples (UI + Legal quality benchmarks, common pitfalls)
references/glossary.md — Untranslatable terms (universal + project-specific)
references/swiss-german-style.md — Swiss-German conventions, translationese traps, Obvious Adams principles
references/qa-checklist.md — QA checklist with separate UI and Legal sections
references/legal-workflow.md — Full 4-agent pipeline for legal translation (Translator → Back-Translator → Validator → Refiner)
Weekly Installs
28
Repository
slfmr1/german-t…nd-legal
First Seen
Mar 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass