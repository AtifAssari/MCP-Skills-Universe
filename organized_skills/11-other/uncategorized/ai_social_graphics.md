---
rating: ⭐⭐⭐
title: ai-social-graphics
url: https://skills.sh/anit-1to10x/10x-accountability-coach/ai-social-graphics
---

# ai-social-graphics

skills/anit-1to10x/10x-accountability-coach/ai-social-graphics
ai-social-graphics
Installation
$ npx skills add https://github.com/anit-1to10x/10x-accountability-coach --skill ai-social-graphics
SKILL.md
AI Social Graphics

This skill creates platform-optimized graphics for social media. Not generic images that happen to be the right size — graphics engineered for each platform's specific algorithm, user behavior, and visual language.

Use this skill when: You need graphics for specific social platforms or ads. Route here from: ai-creative-workflow when platform is specified.

Why This Skill Exists

The problem: Every platform has different:

Aspect ratios and safe zones
Visual languages that perform
Algorithm preferences
User attention patterns
Text overlay requirements

Generic "social media graphics" underperform because they ignore these differences.

The solution: Platform-specific knowledge built into prompt construction, so every graphic is optimized for where it will live.

Model

ALWAYS use Nano Banana Pro via Glif.

Model	Glif ID	Speed
🍌 Nano Banana Pro Text 2 Image	cmi7ne4p40000kz04yup2nxgh	~20sec

Exception: For text-heavy graphics (quote cards, announcement graphics), route to ai-typography which uses Recraft v3 or Ideogram v3 for superior text rendering.

Platform Specifications
Instagram
Placement	Ratio	Pixels	Safe Zone
Feed (Square)	1:1	1080×1080	Full frame
Feed (Portrait)	4:5	1080×1350	Best engagement
Stories	9:16	1080×1920	Avoid top 250px, bottom 200px
Reels Cover	9:16	1080×1920	Center content
Carousel	1:1 or 4:5	1080×1080/1350	Consistent across slides

Instagram Visual Language:

Bold, vibrant colors
High contrast
Clean compositions
Scroll-stopping first frame
Text minimal (algorithm prefers)
YouTube
Placement	Ratio	Pixels	Safe Zone
Thumbnail	16:9	1280×720	Right 1/3 for timestamp overlay
Channel Banner	16:9	2560×1440	Safe area: 1546×423 center
Community Post	1:1	1080×1080	Full frame

YouTube Thumbnail Formula:

FACE + EMOTION + BRIGHT COLOR + CONTRAST + TEXT SPACE


Thumbnails compete against dozens of others. Survival requires:

Human face with exaggerated expression (if relevant)
3 or fewer colors, extremely bold
Text readable at phone size
Contrast that pops in sidebar
LinkedIn
Placement	Ratio	Pixels	Safe Zone
Feed Post	1.91:1	1200×627	Full frame
Article Header	1.91:1	1200×627	Full frame
Profile Banner	4:1	1584×396	Center focal point
Square Post	1:1	1080×1080	Works well too

LinkedIn Visual Language:

Professional but not boring
Clean, sophisticated aesthetics
Thought leadership positioning
Data visualization performs well
Avoid overly casual/meme-y
Twitter/X
Placement	Ratio	Pixels	Safe Zone
Feed Image	16:9	1200×675	Optimal
Feed Image	1.91:1	1200×628	Also works
Feed Image	1:1	1080×1080	Square option
Header	3:1	1500×500	Safe area centered

Twitter Visual Language:

High contrast (dark mode dominant)
Bold, shareable visuals
Meme-adjacent aesthetics OK
Hot takes benefit from visual punch
Screenshots of text perform well
TikTok
Placement	Ratio	Pixels	Safe Zone
Video Cover	9:16	1080×1920	Avoid bottom 150px (UI)
Profile	1:1	200×200	Keep simple

TikTok Visual Language:

Native, not polished
"Shot on phone" aesthetic often wins
Bold text overlays
Faces perform
Trend-aware styling
Pinterest
Placement	Ratio	Pixels	Safe Zone
Standard Pin	2:3	1000×1500	Optimal
Long Pin	1:2.1	1000×2100	More real estate
Square Pin	1:1	1000×1000	Works but less optimal

Pinterest Visual Language:

Aspirational aesthetic
Warm, inviting tones
Clear text overlay (Pinterest users read)
Step-by-step works well
Lifestyle context
Facebook
Placement	Ratio	Pixels	Safe Zone
Feed Post	1.91:1	1200×630	Standard
Square Post	1:1	1080×1080	Also works
Story	9:16	1080×1920	Same as Instagram
Cover Photo	16:9	820×312 (desktop display)	Safe area center

Facebook Visual Language:

Broader demographic appeal
Less edgy than Twitter
Community/family vibes
Video thumbnails important
Event graphics common
Platform-Specific Prompt Templates
Instagram Feed (4:5 Portrait)
[Subject] for Instagram feed, bold vibrant colors,
clean minimal composition, scroll-stopping visual impact,
high contrast, lifestyle aesthetic, modern photography style,
portrait 4:5 composition, subject centered with breathing room,
professional quality, engaging immediate appeal


What makes it work:

"Bold vibrant colors" → Algorithm favors engagement
"Scroll-stopping" → Primes for thumb-pausing moment
"4:5 composition" → Optimal feed real estate
"Breathing room" → Space for engagement UI elements
Instagram Stories (9:16)
[Subject] for Instagram Stories, vertical 9:16 composition,
subject centered in middle third (avoiding top and bottom),
bold engaging visual, bright colors, clean composition,
space for text overlay or sticker placement,
story-native aesthetic, immediate visual impact


What makes it work:

"Middle third" → Avoids UI overlay zones
"Space for text/sticker" → Interactive element room
"Story-native" → Matches platform expectation
YouTube Thumbnail
YouTube thumbnail style, [subject/person] with [emotion] expression,
high contrast dramatic lighting, bold vibrant colors,
clean background for text overlay on [left/right] side,
click-worthy composition, face prominent in frame,
professional thumbnail aesthetic, extreme visual clarity


Emotion Modifiers:

Emotion	Prompt Addition
Surprise	"shocked expression, wide eyes, raised eyebrows, open mouth"
Excitement	"excited expression, big genuine smile, enthusiastic energy"
Curiosity	"intrigued expression, raised eyebrow, knowing look"
Confidence	"confident expression, slight smirk, assured posture"
Concern	"concerned expression, worried face, serious"

Color Psychology for Thumbnails:

Color	Best For	Why
Yellow	Most click-worthy	Highest attention in sidebar
Red	Urgency, drama	Hot takes, breaking news
Blue	Tech, education	Trust, authority
Green	Money, success	Finance, growth
Orange	Entertainment	Warm, inviting
Purple	Creative, unique	Stands out from typical
LinkedIn Professional
Professional LinkedIn graphic, [subject/concept],
clean sophisticated aesthetic, corporate-appropriate colors,
thought leadership positioning, business context,
modern professional photography style, confident tone,
1.91:1 landscape composition, space for headline overlay,
high-end professional quality


LinkedIn Variations:

Data/Insight: Add "data visualization style, clean infographic aesthetic"
Personal Brand: Add "executive portrait style, approachable authority"
Company: Add "brand-aligned color palette, corporate identity"
Twitter/X Post
Twitter-optimized graphic, [subject], high contrast for dark mode,
bold simple composition, shareable visual impact,
16:9 landscape, punchy immediate appeal,
conversation-starter aesthetic, timeline scroll-stopping,
clean professional quality with edge


Twitter Variations:

Hot Take: Add "provocative visual tension, bold statement energy"
Thread Intro: Add "curiosity-inducing, incomplete story visual"
Data/Stat: Add "stark data visualization, number prominent"
Pinterest Pin
Pinterest pin style, [subject] in aspirational setting,
vertical 2:3 composition, rich warm aesthetic,
inspirational lifestyle photography, save-worthy visual,
clear space at top for text overlay, beautiful staging,
high-quality editorial feel, dreamy aspirational mood


Pinterest Performs Best With:

Step-by-step previews
Before/after concepts
Lifestyle aspiration
How-to previews
Collection/roundup style
TikTok Cover
TikTok cover image, [subject/scene], vertical 9:16,
native authentic aesthetic (not over-produced),
bold engaging composition, face-forward if person,
content centered above bottom navigation area,
trend-aware styling, scroll-stopping thumbnail,
high contrast, clear at small size

Content Type Templates
Quote Graphics

Route to ai-typography for best results (text rendering critical)

If generating here:

Minimalist quote graphic for [platform], clean background,
space for text overlay center frame, sophisticated aesthetic,
[color palette], modern design, professional typography space,
[aspect ratio for platform]

Product Announcement
Product announcement graphic for [platform],
[product] hero shot, celebration/launch energy,
bold attention-grabbing composition, premium aesthetic,
space for headline and details, excitement visual,
[platform-specific aspect ratio], commercial quality

Event Promotion
Event promotion graphic for [platform], [event type] theme,
engaging inviting composition, date/time visual priority,
exciting anticipation mood, bold readable design,
[platform aspect ratio], event marketing aesthetic

Behind-the-Scenes
Behind-the-scenes content for [platform],
authentic candid aesthetic, real moment capture,
[subject/scene], genuine unpolished feel,
personality-forward composition, relatable vibe,
[platform aspect ratio], native platform aesthetic

Testimonial/Social Proof
Testimonial graphic for [platform], clean professional design,
space for quote text, trustworthy aesthetic,
person placeholder or abstract human element,
credibility-building composition, [brand colors],
[platform aspect ratio]

Style Exploration (Before Execution)

Critical insight from ai-creative-strategist: Don't lock into one style early. Generate multiple genuinely DIFFERENT visual directions first.

Why This Matters for Social Graphics

Social graphics live in noisy feeds. The "right" style isn't obvious — it depends on:

Platform visual language
Audience expectations
Competitive landscape
Brand positioning

One style = hope. Multiple styles = informed choice.

The Style Exploration Process
1. GENERATE 4-5 DIFFERENT STYLES
   → Not variations of one style
   → Genuinely different visual languages
   → Same subject, different aesthetic approaches

2. IDENTIFY WINNER
   → Which stops the scroll?
   → Which matches platform vibe?
   → Which feels most "brand"?

3. EXTRACT PRINCIPLES
   → What makes this style work?
   → Color palette?
   → Composition approach?
   → Lighting mood?

4. APPLY TO FORMATS
   → Same principles, different platforms
   → Build content SYSTEM
   → Repeatable, not one-off

Style Exploration Prompt Template

For any new social graphics project, generate these 5 directions:

Style 1 - Clean Minimal:
[Subject] for [platform], clean minimal aesthetic, white space,
single focal point, modern typography space, sophisticated restraint

Style 2 - Bold Vibrant:
[Subject] for [platform], bold vibrant colors, high contrast,
dynamic composition, energetic attention-grabbing

Style 3 - Warm Lifestyle:
[Subject] for [platform], warm lifestyle aesthetic, natural tones,
authentic feeling, relatable human-centered

Style 4 - Dark & Premium:
[Subject] for [platform], dark moody aesthetic, premium feel,
sophisticated lighting, luxury positioning

Style 5 - Playful Creative:
[Subject] for [platform], playful creative aesthetic, unexpected angles,
personality-forward, memorable differentiation

Style Decision Framework

After generating options:

Question	Guides Toward
Does brand feel established/premium?	Dark & Premium or Clean Minimal
Is brand approachable/friendly?	Warm Lifestyle or Playful Creative
Competing against boring competitors?	Bold Vibrant or Playful Creative
Professional B2B context?	Clean Minimal or Dark & Premium
Consumer/lifestyle product?	Warm Lifestyle or Bold Vibrant
Extract Principles Template

Once winner is identified, document:

## Winning Style: [Name]

**What makes it work:**
- Color palette: [specific colors]
- Composition: [approach]
- Lighting: [mood/direction]
- Typography space: [how handled]
- Mood: [feeling it creates]

**Apply to other platforms:**
- Instagram Feed: [how to adapt]
- LinkedIn: [how to adapt]
- Twitter: [how to adapt]
- etc.


This creates a repeatable SYSTEM, not just one graphic.

Execution Workflow
Step 1: Platform Requirements
□ Which platform?
□ Which placement? (feed/stories/cover/etc.)
□ Aspect ratio confirmed?
□ Safe zones understood?

Step 2: Content Type
□ What type of content? (announcement/quote/product/etc.)
□ Text overlay needed?
□ Brand colors required?
□ Specific elements must include?

Step 3: Construct Platform-Optimized Prompt

Use templates above, customize for specific need.

Step 4: Generate
Glif: 🍌 Nano Banana Pro Text 2 Image
ID: cmi7ne4p40000kz04yup2nxgh
Inputs: ["[platform-specific prompt]"]

Step 5: Platform-Specific Review

Check against platform requirements:

Correct ratio?
Safe zones respected?
Visual language matches platform?
Scroll-stopping quality?
Text space if needed?
Step 6: Iterate or Approve
Multi-Platform Scaling

When one concept needs multiple platforms:

Strategy: Generate Primary, Then Adapt
1. Generate for PRIMARY platform (where it matters most)
2. Approve composition and style
3. Generate variants for other platforms
   - Adjust aspect ratio
   - Adjust composition for different safe zones
   - Maintain visual consistency

Platform Adaptation Matrix
From → To	Composition Change
Instagram Feed → Stories	Recenter subject in middle third
YouTube Thumb → Twitter	Can often use as-is (both 16:9)
LinkedIn → Facebook	Minimal change (similar ratios)
Pinterest → Instagram	Square crop or reimagine
Any → Stories/TikTok	Full vertical recomposition needed
Batch Generation
For campaign "Product Launch":
├── Instagram Feed (4:5) - primary
├── Instagram Stories (9:16) - adapted
├── LinkedIn (1.91:1) - professional version
├── Twitter (16:9) - punchy version
└── Facebook (1.91:1) - broader appeal version

Quality Checklist
Technical
 Correct aspect ratio for platform
 Resolution sufficient (minimum specs met)
 Safe zones respected (no critical content in overlay areas)
Platform Fit
 Visual language matches platform
 Would scroll-stop on this platform specifically
 Appropriate for platform's audience
 Text (if any) readable at typical view size
Composition
 Subject clear and prominent
 Space for text overlay if needed
 Doesn't compete with platform UI elements
 Colors work on platform (dark mode consideration)
Brand
 Consistent with brand aesthetic
 Colors appropriate
 Tone matches brand voice
Common Issues & Solutions
Issue	Cause	Solution
Looks generic	Platform not specified	Use platform-specific template
Wrong vibe for platform	Cross-platform prompt	Rewrite for specific platform language
Content in unsafe zone	Template not followed	Specify safe zone in prompt
Too polished for TikTok	Wrong aesthetic	Add "native, authentic, not over-produced"
Too casual for LinkedIn	Wrong aesthetic	Add "professional, sophisticated, corporate-appropriate"
Won't scroll-stop	Lacks contrast/impact	Add "bold, high contrast, scroll-stopping"
Text unreadable	Bad text space	Specify "clear space for text overlay"
Wrong ratio	Default used	Explicitly state ratio in prompt
Platform-Specific Tips
Instagram
4:5 gets more real estate than 1:1 — default to portrait
Algorithm favors engagement — bold colors help
First frame of carousel is everything
Avoid heavy text (algorithm deprioritizes)
YouTube
Thumbnail is 50% of click decision
Face + emotion dramatically increases CTR
Test against actual competitors' thumbnails
Yellow genuinely outperforms other colors
LinkedIn
Thought leadership aesthetic wins
Data/insight graphics get shared
Avoid anything that looks like an ad
Professional ≠ boring
Twitter/X
Dark mode dominant — high contrast essential
Memes and screenshots perform
Hot take energy works
Ratio-able graphics (quotes) spread
Pinterest
Vertical wins — 2:3 or longer
Text on pin = good (users read)
Aspirational + actionable
Save-worthy > like-worthy
TikTok
Native aesthetic beats polished
Face-forward works
Match trending visual styles
Avoid looking like an ad
Output Format
## Social Graphic Generated

**Platform:** [platform]
**Placement:** [feed/stories/thumbnail/etc.]
**Aspect Ratio:** [ratio]

**Image URL:** [URL]

**Platform Optimization:**
- ✓ Correct ratio
- ✓ Safe zones respected
- ✓ Platform visual language
- ✓ Scroll-stopping quality

**Feedback?**
- Does it match platform vibe?
- Scroll-stopping enough?
- Text space adequate?
- Ready to approve or iterate?

**Multi-Platform?**
- [ ] Generate additional platform variants
- [ ] Specify platforms needed

Integration with Pipeline
SOCIAL GRAPHICS PIPELINE

┌─────────────────────────────────────────┐
│  Request with platform specified        │
│  → Or route from ai-creative-workflow   │
└─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────┐
│  ai-social-graphics (THIS SKILL)        │
│  → Identify platform requirements       │
│  → Apply platform-specific template     │
│  → Generate with Nano Banana Pro/Glif   │
│  → Review against platform checklist    │
└─────────────────────────────────────────┘
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
┌──────────────────┐   ┌──────────────────┐
│  Single Platform │   │  Multi-Platform  │
│  → Deliver       │   │  → Generate      │
│                  │   │    variants      │
└──────────────────┘   └──────────────────┘

Handoff Protocols
Receiving from ai-creative-workflow
Receive:
  platform: "Instagram"
  placement: "Feed"
  content_type: "Product announcement"
  subject: "[what to show]"
  brand_colors: "[if specified]"
  text_needed: true/false

Returning
Return:
  status: "complete"
  deliverables:
    - platform: "Instagram"
      placement: "Feed"
      aspect_ratio: "4:5"
      url: "[URL]"
  multi_platform_available: true
  additional_platforms_needed: "[list if requested]"

Tips from Experience
What Works
Platform-first thinking — Start with where it lives, not what it shows
Ratio is non-negotiable — Wrong ratio = wrong everything
Safe zones matter — Platform UI will cover content
Visual language matching — LinkedIn ≠ TikTok aesthetically
Bold beats subtle — Social is noisy, you need to pop
What Doesn't Work
One size fits all — Generic "social media" prompts
Ignoring platform culture — Too polished for TikTok, too casual for LinkedIn
Forgetting mobile — Most viewing is phone-sized
Text-heavy images — Most platforms deprioritize
Subtle visuals — Get lost in the scroll
The 80/20

80% of social graphic success comes from:

Correct aspect ratio
Platform-appropriate visual language
Scroll-stopping contrast/colors
Clear focal point

Get these four right and you'll outperform most content.

Weekly Installs
8
Repository
anit-1to10x/10x…ty-coach
GitHub Stars
9
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass