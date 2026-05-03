---
rating: ⭐⭐⭐
title: hyperframes-captions
url: https://skills.sh/heygen-com/hyperframes/hyperframes-captions
---

# hyperframes-captions

skills/heygen-com/hyperframes/hyperframes-captions
hyperframes-captions
Installation
$ npx skills add https://github.com/heygen-com/hyperframes --skill hyperframes-captions
SKILL.md
Captions
Language Rule (Non-Negotiable)

Never use .en models unless the user explicitly states the audio is English. .en models (small.en, medium.en) TRANSLATE non-English audio into English instead of transcribing it. This silently destroys the original language.

When transcribing:

If the user says the language → use --model small --language <code> (no .en suffix)
If the user says it's English → use --model small.en
If the language is unknown → use --model small (no .en, no --language) — whisper auto-detects

Default model is small (not small.en). Only add .en when explicitly told the audio is English.

Analyze the spoken content to determine caption style. If the user specifies a style, use that. Otherwise, detect tone from the transcript.

Transcript Source

The project's transcript.json contains a normalized word array with word-level timestamps:

[
  { "text": "Hello", "start": 0.0, "end": 0.5 },
  { "text": "world.", "start": 0.6, "end": 1.2 }
]


This is the only format the captions composition consumes. Use it directly:

const words = JSON.parse(transcriptJson); // [{ text, start, end }]


For transcription commands, whisper model selection, external APIs (OpenAI, Groq), and supported input formats, see transcript-guide.md.

Style Detection (Default — When No Style Is Specified)

Read the full transcript before choosing a style. The style comes from the content, not a template.

Four Dimensions

1. Visual feel — the overall aesthetic personality:

Corporate/professional scripts → clean, minimal, restrained
Energetic/marketing scripts → bold, punchy, high-impact
Storytelling/narrative scripts → elegant, warm, cinematic
Technical/educational scripts → precise, high-contrast, structured
Social media/casual scripts → playful, dynamic, friendly

2. Color palette — driven by the content's mood:

Dark backgrounds with bright accents for high energy
Muted/neutral tones for professional or calm content
High contrast (white on black, black on white) for clarity
One accent color for emphasis — not multiple

3. Font mood — typography character, not specific font names:

Heavy/condensed for impact and energy
Clean sans-serif for modern and professional
Rounded for friendly and approachable
Serif for elegance and storytelling

4. Animation character — how words enter and exit:

Scale-pop/slam for punchy energy
Gentle fade/slide for calm or professional
Word-by-word reveal for emphasis
Typewriter for technical or narrative pacing
Per-Word Styling

Scan the script for words that deserve distinct visual treatment. Not every word is equal — some carry the message.

What to Detect
Brand names / product names — larger size, unique color, distinct entrance
ALL CAPS words — the author emphasized them intentionally. Scale boost, flash, or accent color.
Numbers / statistics — bold weight, accent color. Numbers are the payload in data-driven content.
Emotional keywords — "incredible", "insane", "amazing", "revolutionary" → exaggerated animation (overshoot, bounce)
Proper nouns — names of people, places, events → distinct accent or italic
Call-to-action phrases — "sign up", "get started", "try it now" → highlight, underline, or color pop
How to Apply

For each detected word, specify:

Font size multiplier (e.g., 1.3x for emphasis, 1.5x for hero moments)
Color override (specific hex value)
Weight/style change (bolder, italic)
Animation variant (overshoot entrance, glow pulse, scale pop)
Marker highlight mode — for visual emphasis beyond color/scale, add a marker-style effect: highlight sweep behind the word, hand-drawn circle around it, burst lines radiating from it, or scribble underline beneath it. See the /marker-highlight skill for patterns and the energy-to-mode mapping table.
Script-to-Style Mapping
Script tone	Font mood	Animation	Color	Size
Hype/launch	Heavy condensed, 800-900 weight	Scale-pop, back.out(1.7), fast 0.1-0.2s	Bright accent on dark (cyan, yellow, lime)	Large 72-96px
Corporate/pitch	Clean sans-serif, 600-700 weight	Fade + slide-up, power3.out, 0.3s	White/neutral on dark, single muted accent	Medium 56-72px
Tutorial/educational	Mono or clean sans, 500-600 weight	Typewriter or gentle fade, 0.4-0.5s	High contrast, minimal color	Medium 48-64px
Storytelling/brand	Serif or elegant sans, 400-500 weight	Slow fade, power2.out, 0.5-0.6s	Warm muted tones, low opacity (0.85-0.9)	Smaller 44-56px
Social/casual	Rounded sans, 700-800 weight	Bounce, elastic.out, word-by-word	Playful colors, colored backgrounds on pills	Medium-large 56-80px
Word Grouping by Tone

Group size affects pacing. Fast content needs fast caption turnover.

High energy: 2-3 words per group. Quick turnover matches rapid delivery.
Conversational: 3-5 words per group. Natural phrase length.
Measured/calm: 4-6 words per group. Longer groups match slower pace.

Break groups on sentence boundaries (period, question mark, exclamation), pauses (150ms+ gap), or max word count — whichever comes first.

Positioning
Landscape (1920x1080): Bottom 80-120px, centered
Portrait (1080x1920): Lower middle ~600-700px from bottom, centered
Never cover the subject's face
Use position: absolute — never relative (causes overflow)
One caption group visible at a time

Caption layer structure: Use a full-width container with margins instead of left: 50%; transform: translateX(-50%). The transform-centered approach collapses to content width, causing clipping at composition edges when text is wide or words are scaled.

/* ✓ Full-width with margins — safe for scaled words */
#caption-layer {
  position: absolute;
  bottom: 80px;
  left: 80px;
  right: 80px;
  text-align: center;
  overflow: visible;
}

/* ✗ Collapsed width — clips at edges */
#caption-layer {
  left: 50%;
  transform: translateX(-50%);
}

Text Overflow Prevention

Use window.__hyperframes.fitTextFontSize() to measure actual rendered text width and compute the correct font size. This replaces character-count heuristics with pixel-accurate measurement powered by pretext.

GROUPS.forEach(function (group, gi) {
  var result = window.__hyperframes.fitTextFontSize(group.text.toUpperCase(), {
    fontFamily: "Outfit",
    fontWeight: 900,
    maxWidth: 1600,
  });
  wordEls.forEach(function (el) {
    el.style.fontSize = result.fontSize + "px";
  });
});

Option	Default	Description
maxWidth	1600	Container width in px (1600 landscape, 900 portrait)
baseFontSize	78	Starting font size — used when text fits
minFontSize	42	Floor — never shrink below this
fontWeight	900	Must match the CSS font-weight
fontFamily	"Outfit"	Must match the CSS font-family
step	2	Decrement step in px per iteration

fontWeight and fontFamily must match the CSS applied to the text elements exactly, or measurements will be inaccurate.

Scale headroom for emphasis words: If per-word styling scales words above 1.0x (e.g., scale: 1.3 on "GOLDEN"), the scaled word occupies more width than fitTextFontSize measured. Reduce maxWidth to compensate: maxWidth = safeWidth / maxScale. For example, with max scale 1.3x on a 1920px composition with 80px margins: maxWidth = 1760 / 1.3 ≈ 1350.

Safety nets (still required in CSS):

max-width on caption container (reduced from composition width to account for emphasis scale)
overflow: visible — not overflow: hidden. Hidden clips scaled emphasis words and their glow effects. Rely on fitTextFontSize with reduced maxWidth instead.
position: absolute on all caption elements
Explicit height on caption container (e.g., 200px)
Caption Exit Guarantee

Captions that stick on screen are the most common caption bug. Every caption group must have a hard kill after its exit animation.

// Animate exit (soft — can fail if tweens conflict)
tl.to(groupEl, { opacity: 0, scale: 0.95, duration: 0.12, ease: "power2.in" }, group.end - 0.12);

// Hard kill at group.end (deterministic — guarantees invisible)
tl.set(groupEl, { opacity: 0, visibility: "hidden" }, group.end);


Why both? The tl.to exit can fail to fully hide a group when karaoke word-level tweens conflict with the parent exit tween, fromTo entrance tweens lock values that override later tweens, or timeline scrubbing lands between the exit start and end. The tl.set at group.end is a deterministic kill — it fires at an exact time, doesn't animate, and can't be overridden.

Self-lint rule: After building the timeline, verify every caption group has a hard kill:

GROUPS.forEach(function (group, gi) {
  var el = document.getElementById("cg-" + gi);
  if (!el) return;
  tl.seek(group.end + 0.01);
  var computed = window.getComputedStyle(el);
  if (computed.opacity !== "0" && computed.visibility !== "hidden") {
    console.warn(
      "[caption-lint] group " + gi + " still visible at t=" + (group.end + 0.01).toFixed(2) + "s",
    );
  }
});
tl.seek(0);


Place this before window.__timelines[id] = tl so it runs at composition init.

References

For dynamic animation techniques (karaoke, clip-path reveals, slam words, scatter exits, elastic entrances, 3D rotation, audio-reactive captions, pretext-based positioning and grouping), see dynamic-techniques.md.

For animated text emphasis (highlight sweeps, hand-drawn circles, burst lines, scribble underlines, sketchout effects) that pairs with per-word styling, see the /marker-highlight skill.

For transcription commands, whisper models, external APIs, and troubleshooting, see transcript-guide.md.

Constraints
Deterministic. No Math.random(), no Date.now().
Sync to transcript timestamps. Words appear when spoken.
One group visible at a time. No overlapping caption groups.
Every caption group must have a hard tl.set kill at group.end. Exit animations alone are not sufficient.
Check project root for font files before defaulting to Google Fonts.
Weekly Installs
46
Repository
heygen-com/hyperframes
GitHub Stars
13.7K
First Seen
Mar 28, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass