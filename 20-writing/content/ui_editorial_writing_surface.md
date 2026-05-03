---
title: ui-editorial-writing-surface
url: https://skills.sh/ajrlewis/ai-skills/ui-editorial-writing-surface
---

# ui-editorial-writing-surface

skills/ajrlewis/ai-skills/ui-editorial-writing-surface
ui-editorial-writing-surface
Installation
$ npx skills add https://github.com/ajrlewis/ai-skills --skill ui-editorial-writing-surface
SKILL.md
UI: Editorial Writing Surface

Use this skill when an app needs a text-first long-form writing surface with strong typography and clean authoring workflow.

Compatibility
Best with architect-nextjs-bun-app.
Recommended with addon-domain-semantic-adaptation for domain vocabulary in writing/publish UX. Common pairings:
addon-nostr-client-nextjs
addon-nostr-key-custody
addon-nostr-nip23-longform
addon-llm-ancient-greek-translation
Inputs

Collect:

VISUAL_DIRECTION: minimal | serif-classic | high-contrast.
CONTENT_MODE: journal | essay | notes.
STYLE_INSPIRATION: short natural-language descriptor from user prompt.
ENABLE_SPLIT_VIEW: yes | no (default yes).
Integration Workflow
Add files:
src/app/journal/page.tsx
src/app/journal/journal.css
src/components/journal/journal-shell.tsx
src/components/journal/editor-pane.tsx
src/components/journal/translation-pane.tsx
src/components/journal/publish-controls.tsx

Import ./journal.css from src/app/journal/page.tsx.
UI contract:
Typography-first layout with generous line height and restrained palette.
Long-form editor with title + body and clear content hierarchy.
Optional translation/preview pane when translation add-on is present.
Publish controls that integrate with selected protocol add-ons.
Integrate add-ons:
Translation pane reads from Ancient Greek translation route.
Publish controls call long-form publish flow.
Posting remains disabled until signer is unlocked/authenticated.
Required UI Contract
Mobile: single column flow.
Desktop: editor and translation split view (when enabled).
Distinct states: draft, translating, ready-to-publish, publish-error.
Explicit signer status (locked/unlocked, signer kind).
Internal navigation uses next/link.
Design Guardrails
Avoid noisy cards or social-feed chrome.
Keep visual hierarchy driven by type scale and spacing, not heavy borders.
Maintain comfortable reading measure for long text.
Ensure focus styles are visible on keyboard navigation.
Apply prompt-provided tone/style at implementation time instead of creating one-off UI skills.
Validation Checklist
Confirm generated code includes required docstrings/JSDoc and rationale comments for non-obvious logic.
# Use the project's package manager (examples):
bun run lint
bun run build
pnpm run lint
pnpm run build


Fallback (offline-smoke):

test -f src/app/journal/page.tsx
test -f src/app/journal/journal.css
rg -n "next/link" src/components/journal || true

Manual checks:
Drafting and translation preview are both usable on mobile and desktop.
Publish controls remain disabled until key auth/signing is available.
Decision Justification Rule
Every non-trivial decision must include a concrete justification.
Capture the alternatives considered and why they were rejected.
State tradeoffs and residual risks for the chosen option.
If justification is missing, treat the task as incomplete and surface it as a blocker.
Weekly Installs
9
Repository
ajrlewis/ai-skills
First Seen
Mar 2, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass