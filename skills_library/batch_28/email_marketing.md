---
title: email-marketing
url: https://skills.sh/nexu-io/open-design/email-marketing
---

# email-marketing

skills/nexu-io/open-design/email-marketing
email-marketing
Installation
$ npx skills add https://github.com/nexu-io/open-design --skill email-marketing
SKILL.md
Email Marketing Skill

Produce a single HTML email — centered, single column, no chrome around the email body. Treat it like a marketing artifact: one big idea, one CTA.

Workflow
Read the active DESIGN.md (injected above). Email leans on the display font more than any other surface — pick the loudest type token in the DS for the headline lockup.
Pick the brand + product from the brief. Generate a real wordmark, a real product name, and one real benefit sentence — no placeholders.
Layout, in order, all centered inside a 600–680px column on a tinted page background (so the email body looks like an email, not the page):
Masthead — wordmark on the left + 3 short nav links (SHOP, JOURNAL, MEMBERS) on the right. Thin underline.
Hero block — a 16:9 product image placeholder. Use a DS-tinted gradient or a stylized SVG silhouette of the product (shoe, bottle, headphones, whatever the brief implies). Add a tiny brand stamp on the top-left and a colorway tag on the bottom-left.
Eyebrow — small caps, accent color, separated by · characters (e.g. "NEW · MAX-CUSHION TRAINER · EMBER FLARE").
Headline lockup — 2–3 line headline using the display font, all caps, extra-tight tracking. Apply a slight skew (transform: skew(-6deg)) on one accent word to give it a sporty parallelogram feel.
Body — 2–3 sentence paragraph, left-aligned, body font.
Primary CTA — solid pill or block button. One only.
Specs grid — 2×2 grid of (big number + unit + label) callouts using the display font for the numbers.
Footer — wordmark, address line, unsubscribe + view-in-browser links.
Write a single HTML document:
<!doctype html> through </html>, CSS inline.
Center the column with margin: 0 auto. Set body { background: <tint> } so the email-on-page metaphor reads.
No external images — use inline SVG or DS-tinted gradient blocks for the product photo.
data-od-id on the masthead, hero, headline, CTA, specs.
Self-check:
Email reads top to bottom in 8–10 seconds.
One CTA. Accent appears at most twice (eyebrow + CTA, or headline word).
Looks legible on a 480px window (column reflows, type drops one step).
Output contract

Emit between <artifact> tags:

<artifact identifier="email-slug" type="text/html" title="Email — Subject Line">
<!doctype html>
<html>...</html>
</artifact>


One sentence before the artifact, nothing after.

Weekly Installs
64
Repository
nexu-io/open-design
GitHub Stars
14.2K
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass