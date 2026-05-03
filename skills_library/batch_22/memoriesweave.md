---
title: memoriesweave
url: https://skills.sh/hero988/memoriesweave-skill/memoriesweave
---

# memoriesweave

skills/hero988/memoriesweave-skill/memoriesweave
memoriesweave
Installation
$ npx skills add https://github.com/hero988/memoriesweave-skill --skill memoriesweave
SKILL.md
MemoriesWeave API

Provides programmatic access to MemoriesWeave — a platform for creating photo memory collections with custom HTML layouts. The agent designs HTML layouts and pushes them to memories. The API provides photos, conversations, workspace context, and people data.

How to call the API

ALWAYS use curl via the Bash tool. Do not use WebFetch, fetch(), or any other HTTP client — they fail due to redirects and auth header stripping.

API="https://grandiose-loris-729.eu-west-1.convex.site/api/v1"
KEY="<user-provided-api-key>"

curl -s "$API/ENDPOINT" -H "Authorization: Bearer $KEY"


The user provides their API key (format: mw_sk_<32hex>) when requesting this skill.

Workflow: Creating or editing a memory

Follow these steps in order. Do not skip steps.

Step 1: Lock the memory FIRST

The VERY FIRST API call must be locking the memory. Do this before gathering context, before reading HTML, before anything else. This shows a loading animation on the user's screen immediately.

curl -s -X POST "$API/memories/{memoryId}/lock" -H "Authorization: Bearer $KEY"


If creating a new memory (no memory ID yet), lock it immediately after creation.

Step 2: Gather context
# Get workspace list
curl -s "$API/workspaces" -H "Authorization: Bearer $KEY"

# Get workspace context (who the people are, relationship info, instructions)
curl -s "$API/workspaces/{wsId}/context" -H "Authorization: Bearer $KEY"

# Get registered people (names, roles, descriptions)
curl -s "$API/workspaces/{wsId}/persons" -H "Authorization: Bearer $KEY"

Step 3: Save a "before" snapshot
curl -s -X POST "$API/memories/{memoryId}/snapshots" \
  -H "Authorization: Bearer $KEY" \
  -H "Content-Type: application/json" \
  -d '{"label": "Before edit — description of planned change"}'

Step 4: Select photos

Use tag filtering as a starting point, then verify with conversation context.

IMPORTANT: dateFrom and dateTo must be Unix timestamps in milliseconds, NOT date strings. Example: July 1, 2025 = 1751328000000, not 2025-07-01. Calculate with: new Date("2025-07-01").getTime()

# Filter by tag (e.g. couple, selfie, portrait, traveling)
curl -s "$API/workspaces/{wsId}/photos?tag=couple&limit=50" -H "Authorization: Bearer $KEY"

# Filter by date range (Unix ms timestamps)
curl -s "$API/workspaces/{wsId}/photos?dateFrom=1751328000000&dateTo=1754006400000&limit=50" -H "Authorization: Bearer $KEY"

# If user provides a photo ID, fetch it directly
curl -s "$API/photos/{photoId}" -H "Authorization: Bearer $KEY"

# Get conversation context around a photo (what was happening when it was shared)
curl -s "$API/workspaces/{wsId}/conversations/by-photo/{photoId}" -H "Authorization: Bearer $KEY"


Tags are AI-generated and may be inaccurate. Use them as a first filter, then verify with conversation context. Do not rely on tags alone.

Pagination: If a search doesn't return enough results, check meta.hasMore in the response. If true, use the cursor value to fetch the next batch:

# First request
curl -s "$API/workspaces/{wsId}/photos?tag=couple&limit=50" -H "Authorization: Bearer $KEY"
# Response includes: "meta": { "cursor": "abc123", "hasMore": true }

# Get next batch using cursor
curl -s "$API/workspaces/{wsId}/photos?tag=couple&limit=50&cursor=abc123" -H "Authorization: Bearer $KEY"


Keep paginating until you find what you need or hasMore is false.

Step 5: Choose the correct format
curl -s "$API/digital-formats" -H "Authorization: Bearer $KEY"


Common formats: Phone Wallpaper (1170x2532 iPhone 13, 1320x2868 iPhone 16 Pro Max), Desktop (3840x2160), Social Post (1080x1080).

Step 5b: VERIFY every photo before using it

Before including ANY photo in your design, you MUST verify it exists and get its actual data by calling:

curl -s "$API/photos/{photoId}" -H "Authorization: Bearer $KEY"


NEVER fabricate, guess, or construct photo URLs. Every photo URL must come from an actual API response (urls.original, urls.medium, or urls.thumbnail). If a photo search returns no results for a month, report that to the user — do not invent URLs.

Verification checklist for every photo:

You received the photo ID from the API (not made up)
You called GET /photos/{photoId} and got a valid response
The dateTaken field matches the month you're placing it on
The tags or photo content matches what you expect (couple/selfie/andrea etc.)
The urls.original URL is what you're putting in the HTML

If the API returns empty results for a time period, try different search strategies:

Search by tag=couple, tag=selfie, tag=andrea without date range
Then filter results by dateTaken in your code
Try broader date ranges
If truly no photos exist for a month, tell the user
Step 6: Design HTML and push

Note: Custom HTML is rendered inside a sandboxed iframe with DOMPurify sanitization. All <script> tags, <canvas>, <iframe>, and event handler attributes are stripped. Only CSS-based animations work (use @keyframes, animation-delay, and @supports (animation-timeline: view()) for scroll-driven effects). Do not rely on any JavaScript for interactivity or animations — it will be silently removed.

Design self-contained HTML with inline styles. For multi-page memories, wrap each page in <div data-mw-page="N">.

curl -s -X PATCH "$API/memories/{memoryId}" \
  -H "Authorization: Bearer $KEY" \
  -H "Content-Type: application/json" \
  -d '{"customHtml": "<div data-mw-page=\"1\" style=\"width:1170px;height:2532px;...\">...</div>"}'


When resizing, include digitalFormat in the same PATCH:

curl -s -X PATCH "$API/memories/{memoryId}" \
  -H "Authorization: Bearer $KEY" \
  -H "Content-Type: application/json" \
  -d '{"customHtml": "...", "digitalFormat": {"category": "phone_wallpaper", "widthPx": 1170, "heightPx": 2532, "outputFormat": "png"}}'

Step 7: Verify ALL images load, then screenshot

Before screenshotting, verify that every image URL in your HTML actually loads. Extract all image URLs from your HTML and spot-check at least 3 by fetching them:

curl -sI "https://pub-....r2.dev/photos/.../photo.jpg" | head -1
# Should return: HTTP/2 200 (not 404 or 403)


If any return 404, you used a fabricated or wrong URL — go back to Step 5b and fix it.

Then take screenshots to verify the design:

curl -s "https://www.memoriesweave.com/api/screenshot?memoryId={memoryId}&page=1" \
  -H "Authorization: Bearer $KEY"


Optional query params: widthPx and heightPx to override dimensions (useful for physical products where dimensions come from the product specs, not digitalFormat). Example: &widthPx=3772&heightPx=5250 for wall calendars.

Returns { "data": { "screenshotUrl": "https://..." } }. Download and view the screenshot. Check that:

All photos are visible (no broken image icons)
Photos show the correct people/content
No duplicate-looking photos on the same page
Text is readable and correctly positioned
Captions match the actual photo they appear under — you cannot determine which photo is in which position from HTML order alone. You MUST screenshot the page and visually confirm that each caption describes the photo it appears next to. Tags can be misleading (e.g. a "couple selfie on a bridge" might be tagged "coffee date" if they were near a cafe).

When editing captions: ALWAYS screenshot the page BEFORE changing any caption text. Look at the screenshot to understand which photo is in position 1, 2, and 3. Then match your caption to what you actually see in the screenshot.

Step 8: Save an "after" snapshot
curl -s -X POST "$API/memories/{memoryId}/snapshots" \
  -H "Authorization: Bearer $KEY" \
  -H "Content-Type: application/json" \
  -d '{"label": "After edit — description of what changed"}'

Step 9: Unlock the memory

This removes the loading animation from the user's screen.

curl -s -X POST "$API/memories/{memoryId}/unlock" -H "Authorization: Bearer $KEY"


Always unlock when done, even if an error occurred.

Creating physical product memories

To create a memory for a physical product (canvas print, poster, calendar, photo book, etc.):

Get the product list: GET /products
Create the memory with mode: "physical" and productId:
curl -s -X POST "$API/workspaces/{wsId}/memories" \
  -H "Authorization: Bearer $KEY" \
  -H "Content-Type: application/json" \
  -d '{"title": "My Canvas Print", "mode": "physical", "productId": "<product_id_from_products_list>"}'

The API automatically creates a pod design session with the correct product dimensions and print specs.
Push HTML with PATCH /memories/{id} using the product's pixel dimensions (e.g., 9000x7200 for canvas print, 3772x5250 for wall calendar, 3075x2475 for hardcover photo book).
The memory can then be ordered through the website's print flow.
Product response fields

Each product from GET /products includes:

provider — "printful", "blurb", or "gelato" (determines print fulfillment)
bleedMm — bleed margin in mm (5 for Printful, 3.175 for Blurb)
pageCountMin / pageCountMax — valid page range for variable-page products (null for fixed)
fileFormat — "png" for Printful products, "pdf" for Blurb photo books
variants[] — available size options with per-variant dimensions and pricing
Product-specific rules

Wall calendars MUST always have exactly 14 pages: cover + 12 months (Jan-Dec) + back page. Each month page needs a correct calendar grid with proper day-of-week starts. Dimensions: 3772x5250px. Never use duplicate photos across pages. Every photo on relationship months must show the people (not food, scenery, or screenshots).

Hardcover photo books (Blurb) have 20-240 pages. Dimensions: 3075x2475px (10×8" Standard Landscape with 3.175mm/0.125" bleed at 300 DPI). All pages are interior content pages. Users download the generated PDF and upload to Blurb via "PDF to Book" (blurb.co.uk/pdf-to-book), where they design the cover separately. When generating print files, the system automatically:

Assembles all pages into a sequential multi-page PDF (interior pages only)
Pads to even page count if needed (Blurb requirement)
Also provides individual PNG files + ZIP for proofing

Available sizes: 7×7" (18×18cm), 8×10" (20×25cm), 10×8" (25×20cm, default), 12×12" (30×30cm), 13×11" (33×28cm).

Paper: Premium Lustre 148gsm, ImageWrap hardcover, 300 DPI. Pricing in GBP (£28.00 base for 10×8", £0.34/extra page). Never use duplicate photos across pages. Each page should feature unique content and photos from different events.

Phone wallpapers support up to 10 pages. Each page is a standalone wallpaper at the device's resolution.

Bulk export endpoints

For large projects (e.g., 240-page photo books), use the export endpoints to get ALL data in one call.

CRITICAL — BANDWIDTH WARNING: Export endpoints read the ENTIRE workspace catalog from the database. Each call costs significant database bandwidth (~5-7 MB for photos, ~1 MB for conversations). You MUST:

Call each export endpoint AT MOST ONCE per session — never re-fetch what you already have
Cache the results in memory for the duration of your work — reference the cached data for all subsequent operations
Use dateFrom/dateTo filters when you only need a subset (e.g., a single month) to reduce bandwidth
Never call exports in a loop or retry — if the call succeeds, you have everything

Photo export — GET /workspaces/:wsId/photos/export?dateFrom=TS&dateTo=TS

Returns ALL photos (no pagination cap, no 100-item limit)
Each photo includes a persons[] array: [{id, name, confidence}] — who is in the photo
Use persons to prioritize photos (e.g., couple together > person alone > other)
Response: { data: [...], meta: { total: N } }
Call once, cache the result, reference from cache for all page designs

Conversation export — GET /workspaces/:wsId/conversations/export?dateFrom=TS&dateTo=TS

Returns ALL conversation chunks (no pagination cap)
Each chunk includes text (full inline message content) AND textUrl (fallback URL)
Response: { data: [...], meta: { total: N } }
Call once, cache the result, reference from cache for all page designs

Page HTML push — PATCH /memories/:id/pages/batch with {"pages": [{"pageNumber": N, "html": "..."}, ...]}

Push 1-50 pages at once. Even for a single page, always use the batch endpoint.
Each page is stored as its own ~5KB document in the database (no 1MB field limit)
Automatically wraps in <div data-mw-page="N"> if not present
Creates or replaces each page (upsert by memoryId + pageNumber)
Pages can be pushed in any order (not necessarily sequential)
Returns { pagesUpserted, totalPages }
After writing, automatically syncs the combined HTML to the design session
GET /memories/:id/html automatically concatenates all pages in order
Screenshots and print file generation load individual pages efficiently

Delete all pages — DELETE /memories/:id/pages

Removes all HTML pages for a memory (clean slate for redesigns)
Returns { deletedCount }

Set page count — PATCH /memories/:id with {"pageCount": N}

Sets the expected page count on the memory document
UI and print pipeline use this to know how many pages to expect without scanning
Photo selection rules
Always check conversation context around candidate photos before selecting them.
If user provides a photo ID, use it directly via GET /photos/{photoId}.
Prefer tags: couple, selfie, portrait, andrea, suliman, romantic, joyful, traveling.
Avoid tags: food, screenshot, meme, document, sticker, illustration (unless requested).
Prefer portrait orientation (height > width) for phone wallpapers.
Use urls.original for high-resolution output, urls.medium for web display.
No duplicate or visually similar photos on the same page or across pages. Check the fileName field — it contains a timestamp like 00013190-PHOTO-2025-09-27-19-46-12.jpg. If two photos have timestamps within 5 minutes of each other, they are from the same event/session and look nearly identical (e.g. two photobooth strips from the same booth, two selfies at the same spot). When placing multiple photos on the same page, ensure each photo is from a different date or different event (timestamps at least 1 hour apart).
Cover and back pages must use unique photos not used on any month page.
Each month's photos must be from that actual month. Check the dateTaken timestamp. Do not use April photos on the August page.
Use the earliest occurrence of a photo. Photos in WhatsApp are sometimes resent months later. The dateTaken field reflects when the photo was originally taken, NOT when it was shared in the chat. When filtering by date range, a photo taken in July may appear in a December conversation chunk because it was resent. Always use dateTaken to determine which month a photo belongs to — if dateTaken says July, it goes on the July page, never December, even if it was found in a December conversation search.
Photo URLs

Each photo has three variants:

urls.thumbnail — 300px wide WebP
urls.medium — 800px wide WebP
urls.original — Full resolution
Slideshow / Digital Frame Video Export

Render multi-page digital memories as MP4 videos with Ken Burns effects and transitions. Only available for digital memories (not physical products). The rendered video includes AI quality review via Gemini.

Workflow
Design a multi-page memory first (at least 2 pages with data-mw-page)
Configure the slideshow:
curl -s -X POST "$API/memories/{memoryId}/slideshow/render" \
  -H "Authorization: Bearer $KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "resolution": "1920x1080",
    "reviewModel": "google/gemini-3-flash-preview",
    "slides": [
      {"page": 1, "durationSeconds": 6, "kenBurns": {"direction": "zoom_in_center", "intensity": 0.3}, "transition": {"type": "crossfade", "durationSeconds": 1.5}},
      {"page": 2, "durationSeconds": 5, "kenBurns": {"direction": "pan_left", "intensity": 0.5}, "transition": {"type": "fade_black", "durationSeconds": 2.0}},
      {"page": 3, "durationSeconds": 7, "kenBurns": {"direction": "zoom_out_center", "intensity": 0.3}}
    ]
  }'

Poll for completion:
curl -s "$API/memories/{memoryId}/slideshow" -H "Authorization: Bearer $KEY"

When status is "completed", download the video from the videoUrl field
Read the reviewFeedback for quality assessment
If issues are identified, adjust the config and re-render
Ken Burns Directions
Direction	Description	Best for
zoom_in_center	Slow zoom into center	Portraits, close-ups
zoom_out_center	Start zoomed, pull out	Group shots, landscapes
pan_left	Pan from right to left	Wide scenes, landscapes
pan_right	Pan from left to right	Wide scenes
pan_up	Pan from bottom to top	Tall subjects
pan_down	Pan from top to bottom	Tall subjects
none	No motion (static)	Text-heavy slides
Transition Types
Type	FFmpeg Effect	Feel
crossfade	Dissolve	Classic, elegant
fade_black	Fade to black	Chapter break
fade_white	Fade to white	Dreamy
slide_left	Slide left	Timeline progression
slide_right	Slide right	Reverse timeline
circle_open	Circle reveal	Nostalgic, vintage
dissolve	Pixel dissolve	Soft, organic
wipe_right	Wipe right	Clean, modern
Resolutions
Resolution	Label	Best for
1920x1080	Full HD	Digital frames, Chromecast, most TVs
3840x2160	4K UHD	Samsung Frame TV, 4K displays
Pricing
Rendering: Free (compute only, no AI cost)
AI Review: Gemini Flash ~$0.04/review, Gemini Pro ~$0.10/review (credits deducted with 2x markup)
Endpoint reference
Account
Method	Endpoint	Description
GET	/me	User info and plan
GET	/me/credits	Credit balance
GET	/me/usage	Usage summary
Workspaces
Method	Endpoint	Description
GET	/workspaces	List workspaces
GET	/workspaces/:id	Workspace details
GET	/workspaces/:id/context	AI context (description, relationship, instructions)
GET	/workspaces/:id/persons	Registered people
Photos
Method	Endpoint	Description
GET	/workspaces/:wsId/photos	List photos. Params: cursor, limit, tag, dateFrom, dateTo
GET	/workspaces/:wsId/photos/export	Bulk export ALL photo metadata (no pagination cap). Includes persons[] array. Params: dateFrom, dateTo
GET	/photos/:id	Single photo details and URLs
PATCH	/photos/:id	Update caption or tags
Memories
Method	Endpoint	Description
GET	/workspaces/:wsId/memories	List memories
GET	/memories/:id	Memory details
POST	/workspaces/:wsId/memories	Create memory. Body: title, description, optional mode ("digital"|"physical"), optional productId (required if physical), optional digitalFormat
PATCH	/memories/:id	Update title, description, customHtml, or digitalFormat
DELETE	/memories/:id	Delete memory
GET	/memories/:id/html	Get rendered HTML
PATCH	/memories/:id/pages/batch	Push 1-50 pages. Body: {"pages": [{pageNumber, html}, ...]}. Returns {pagesUpserted, totalPages}. Syncs to design session automatically.
DELETE	/memories/:id/pages	Delete all HTML pages for a memory. Returns {deletedCount}
POST	/memories/:id/lock	Show AI working overlay on frontend
POST	/memories/:id/unlock	Remove AI working overlay
GET	/memories/:id/snapshots	List version history
POST	/memories/:id/snapshots	Create snapshot. Body: {"label": "..."}
POST	/memories/:id/snapshots/:snapId/restore	Restore a previous version
Conversations
Method	Endpoint	Description
GET	/workspaces/:wsId/conversations	List chat chunks
GET	/workspaces/:wsId/conversations/export	Bulk export ALL conversation chunks (no pagination cap). Includes textUrl for each chunk. Params: dateFrom, dateTo
GET	/workspaces/:wsId/conversations/search?start=TS&end=TS	Search by date range
GET	/workspaces/:wsId/conversations/by-photo/:photoId	Messages around a photo
Formats and products
Method	Endpoint	Description
GET	/digital-formats	All format presets with dimensions
GET	/products	Print product catalog
Conversation summaries
Method	Endpoint	Description
GET	/workspaces/:wsId/summaries	List summaries. Params: type (day|week|biweekly|month|year|custom), dateFrom (YYYY-MM-DD), dateTo (YYYY-MM-DD)
GET	/workspaces/:wsId/summaries/:periodKey	Get single summary by periodKey (e.g. day:2025-04-06)
GET	/workspaces/:wsId/summaries/export	Bulk export ALL summaries of a type (no pagination cap). Params: type (required)
GET	/workspaces/:wsId/summaries/volumes	List generation volumes (jobs). Returns volume number, period type, date range, status, stats
GET	/workspaces/:wsId/summaries/volumes/:volumeId	Get single volume details + all its summaries
GET	/workspaces/:wsId/summaries/date-range	Get min/max dates of available conversation data
GET	/workspaces/:wsId/summaries/counts	Count summaries by type: {day: N, week: N, month: N, ...}
Slideshow (digital memories only)
Method	Endpoint	Description
POST	/memories/:id/slideshow/render	Trigger slideshow video render with Ken Burns + transitions
GET	/memories/:id/slideshow	Get slideshow render status + video download URL
GET	/slideshow/presets	List available Ken Burns, transition, and resolution presets
Screenshot (uses website domain, not API domain)
Method	URL	Description
GET	https://www.memoriesweave.com/api/screenshot?memoryId=X&page=N	Render page to JPEG
Pricing
Free: All GET endpoints, CRUD operations, pushing HTML, snapshots, lock/unlock.
Credits: AI operations only (design chat, content generation, photo captioning via Trigger.dev pipeline). The agent designing HTML does not consume credits.
Rate limits
Plan	CRUD ops/min	AI ops/min
Free	60	2
Starter	120	5
Plus	300	10
Pro	600	20
Conversation Summaries

Warm, factual summaries of WhatsApp conversations at any granularity — by day, by month, by year, or for a custom date range. Suitable for scrapbooks, photo books, and memory collections.

Summary types
Type	User says	What it produces
Day summaries	"Create day summaries from April to January"	One summary per day — what happened that specific day
Month summaries	"Summarise each month from April to January"	One summary per month — the highlights, milestones, and themes of that month
Year summary	"Give me a year summary of our conversations"	One overall summary — the full story arc across the entire period
Custom range	"Summarise what happened between June 10 and June 20"	One summary covering that specific date range

Each summary has: title (2-3 words), titleLine2 (1-3 words), summary (length varies by type), startDate, endDate, periodKey, status.

Two options for getting summaries

The user chooses which approach they want:

Option A: Fetch existing summaries from the website (recommended)

If the user has already generated summaries on memoriesweave.com (via the website's + Generate button), fetch them directly from the API. This is faster, cheaper, and the summaries have already been AI-verified.

The user tells you which summaries to use by either:

Giving you a volume ID (copied from the website UI — e.g., vol:jd7a83kxyz...): "Use the summaries from this volume: vol:jd7a83kxyz..."
Specifying a type and date range: "Get my day summaries from April to June"
Saying "use existing summaries" or "fetch my summaries"

How to fetch:

# 1. Check what summaries exist
curl -s "$API/workspaces/{wsId}/summaries/counts" \
  -H "Authorization: Bearer $KEY"
# Returns: {"data": {"day": 25, "week": 0, "month": 3, "year": 1, ...}}

# 2. List volumes (generation batches) — shows what was generated and when
curl -s "$API/workspaces/{wsId}/summaries/volumes" \
  -H "Authorization: Bearer $KEY"
# Returns volumes with: volumeNumber, periodType, dateFrom, dateTo, status, completedPeriods, totalPeriods

# 3a. Get all summaries from a specific volume
curl -s "$API/workspaces/{wsId}/summaries/volumes/{volumeId}" \
  -H "Authorization: Bearer $KEY"
# Returns volume details + all its summaries

# 3b. OR list summaries by type + optional date range
curl -s "$API/workspaces/{wsId}/summaries?type=day&dateFrom=2025-04-06&dateTo=2025-04-30" \
  -H "Authorization: Bearer $KEY"
# Returns array of summaries matching the filter

# 3c. OR bulk export ALL summaries of a type
curl -s "$API/workspaces/{wsId}/summaries/export?type=day" \
  -H "Authorization: Bearer $KEY"
# Returns all summaries (no pagination cap) — best for large sets

# 4. Get a single summary by periodKey
curl -s "$API/workspaces/{wsId}/summaries/day:2025-04-06" \
  -H "Authorization: Bearer $KEY"
# Returns: {title, titleLine2, summary, startDate, endDate, status, ...}


Each summary object looks like:

{
  "periodKey": "day:2025-04-06",
  "periodType": "day",
  "startDate": "2025-04-06",
  "endDate": "2025-04-06",
  "title": "First Chats",
  "titleLine2": "Cat Cafe Plans",
  "summary": "Their very first conversation — both had never dated before...",
  "status": "verified",
  "messageCount": 163,
  "verificationPasses": 2
}

Option B: Generate summaries manually (agent does the work)

If the user hasn't generated summaries on the website yet, or wants the agent to create them from scratch by reading the raw conversations. This is slower but doesn't require any prior setup on the website.

The user says things like: "Create day summaries for me from April to January", "Write summaries yourself from the conversations"

Step 1: Export conversations to local .txt files

# Get all conversations with inline text
curl -s "$API/workspaces/{wsId}/conversations/export?dateFrom=TS&dateTo=TS" \
  -H "Authorization: Bearer $KEY" > convos_export.json


Then group by date into monthly .txt files for easy reading:

// Group conversation text by date, save as monthly .txt files
// Each date section starts with: ========== YYYY-MM-DD ==========
// Contains the FULL conversation text for that day (no truncation)


Save as convos_YYYY-MM.txt (e.g., convos_2025-04.txt). Include ALL message text — never truncate.

Step 2: Generate summaries by reading conversations

Read the actual conversation text and write summaries. Each summary has:

title: First line of a decorative title (2-3 words, e.g., "Sweet Mornings")
titleLine2: Second line (1-3 words, e.g., "& Missing You")
summary: Description of what ACTUALLY happened. Must be:
Written in third person (use actual names, not "I" or "you")
Specific — reference real places, events, quotes from the conversation
Factual — only include what is explicitly stated in messages
Warm and nostalgic — like a scrapbook caption looking back

For day summaries: Process one day at a time. Use parallel agents (one per 2 months) for speed. Each agent reads the .txt files and saves to a separate JSON file (e.g., summaries_apr_may.json). Summary length: 1-3 sentences.

For month summaries: Read ALL conversations for that month. Identify the key events, milestones, recurring themes, and emotional arc. Summary length: 3-5 sentences. Title should capture the month's main theme (e.g., "The Month We" / "Fell in Love" or "Exams &" / "Adventures").

For year summaries: Read conversations across the full period (or use the day/month summaries as input). Tell the complete story arc — how it started, key milestones, how the relationship evolved. Summary length: 5-10 sentences. Title should capture the overall journey (e.g., "Our Story" / "300 Days").

For custom range summaries: Read conversations in the specified range. Length proportional to the range — a few days gets 1-3 sentences, a few weeks gets 3-5.

Step 3: Verify summaries (CRITICAL — run at least 2 passes)

Launch verification agents that re-read each day's conversation and check every claim in the summary:

Is every fact directly supported by a message?
Is every event on the correct date? (Messages after midnight = next day)
Is anything fabricated, assumed, or embellished?
Is anything from an adjacent day bleeding in?
Who said what — correct attribution?
"Planned" vs "actually happened" accurately distinguished?

Common AI errors to watch for (from experience with 94 corrections across 5 passes):

Date bleeding (~30%): Messages after midnight attributed to wrong day
Fabricated details (~20%): AI inventing names, places, events not in text
Planned vs happened (~15%): Saying they did something they only discussed
Wrong attribution (~10%): Mixing up who said what
Adjacent day bleed (~10%): Details from wrong day
Embellishment (~10%): Adding unsupported adjectives/details
Wrong specifics (~5%): Incorrect amounts, times, place names

Run multiple verification passes until a pass comes back with 0-2 fixes. Minimum 2 passes recommended, 3-5 for print-quality output.

Step 4: Merge and save

Merge all per-month files into a single day_summaries.json. Generate a review HTML for the user to browse.

Step 5: Create review HTML

Build a browsable HTML file showing all summaries so the user can review before applying:

<!-- Each day shown as a card with date, title, and summary -->
<div class="day">
  <div class="day-date">2025-04-12</div>
  <div class="day-title">The First Date</div>
  <div class="day-summary">Their very first date! Both nervous, both excited...</div>
</div>

Using day summaries in photo books

When integrating summaries into photo book pages, render them as Polaroid Story Cards — a Polaroid-shaped card with:

Watercolor wash background (layered CSS radial gradients)
"this day was about" header in small Playfair Display caps
Big decorative title in Dancing Script (line 1 in espresso, line 2 in rose)
Gold divider (line + ✦ + line)
Summary text in Caveat cursive, centered
Handwritten caption at Polaroid bottom

For single-day pages: caption says "a day to remember" For multi-day pages: each day gets its own card with "our 3rd May" / "our 4th May" captions

Blurb BookWright Photo Book Export

When the user wants to convert a photo book memory HTML into a physical Blurb hardcover book, follow this automated pipeline. The user just says "make this into a photobook" and we handle everything.

Blurb Book Specifications (exact settings used for ordering)
Setting	Value
Cover type	Hardcover, ImageWrap
Size	Standard Landscape, 10×8 in (25×20 cm)
Paper	Premium Paper, lustre finish (148gsm Premium Lustre)
Cover finish	Matte
Blurb logo	Custom Logo Upgrade (remove Blurb logo page)
End sheets	Standard Mid-Grey
Page count	20-240 (must be even)
Page dimensions	3075×2475px (10.25×8.25" at 300 DPI, includes bleed)
SKU	PHBK-1000x0800-IW-PPRLS
Pricing	From £28.00 base + £0.34/extra page (before discounts)
Product page	https://www.blurb.co.uk/photo-books/imagewrap-hardcover-photo-book
Prerequisites
Node.js + Playwright (npx playwright install)
Python 3 (built-in sqlite3, Pillow for image processing)
Blurb BookWright desktop app installed (download from blurb.co.uk)
A BookWright project created with: Size 25×20cm, Premium Lustre, Matte, 20 pages starting count
Critical: Print Safe Zone

BookWright's autolayout="fill" crops 94px from each side of 3075px-wide images. The print trim removes additional margin. To prevent ANY content from being clipped, wrap all page content in a scale(0.91) transform before rendering:

# For each page div in the HTML, insert a wrapper after the opening tag:
wrapper = '<div style="position:absolute;inset:0;transform:scale(0.91);transform-origin:center center;">'
# Close the wrapper before the page's closing </div>


This scales all content to 91% and centers it, creating ~138px of safe margin on all edges. This is the ONLY reliable method — shifting individual CSS properties misses elements.

Automated Pipeline

Step 1: Fetch the HTML from the memory

# The API returns a URL to the HTML file, then download it
curl -s "$API/memories/{memoryId}/html" -H "Authorization: Bearer $KEY"
# Response: {"data":{"type":"url","url":"https://...convex.cloud/api/storage/..."}}
# Download the actual HTML from the storage URL
curl -s "STORAGE_URL" > photobook.html


Step 2: Apply print safe zone + upgrade image URLs

# 1. Wrap ALL page content in scale(0.91) wrapper for print safety
# 2. Replace -thumb.webp and -medium.webp with .jpg for print quality
# 3. If page 1 is a title page matching the cover, remove it (cover handles it)


Step 3: Pre-download all images locally

Images from the R2 CDN can timeout during rendering. Download ALL unique image URLs to a local folder first, then replace CDN URLs with file:// paths in the HTML:

// Extract all unique CDN URLs from HTML
// Download each to local-images/ folder (parallel batches of 20)
// IMPORTANT: Some -thumb.webp files don't have .jpg equivalents
// If a downloaded file is HTML (error page), re-download as original .webp format
// Replace all CDN URLs in HTML with file:// local paths


Step 4: Render each page as a high-quality JPEG (3075×2475px)

Use Playwright to screenshot each data-mw-page div:

Wrap the raw HTML in a <html> document with Google Fonts @import
Set viewport to 3075×2475, deviceScaleFactor 1
For each page: show only that page (CSS .active class), wait for images to load, screenshot as JPEG quality 95
Save to blurb-pages/page_001.jpg through page_NNN.jpg
Use 3-second timeout per image (local files load instantly)

Fonts to import: Dancing Script, Caveat, Nunito, Playfair Display, Patrick Hand, Lora.

Step 5: Build the .blurb SQLite file

The .blurb file is a SQLite database with two tables: ArchiveVersion (version=4) and Files (filepath, filecontent BLOB, filesize, filedate).

Image resolution chain (all three MUST match or images show as "Drag an image here"):

bbf2.xml:           <image src="{guid}.jpg"/>           ← GUID only, no path prefix
media_registry.xml: <media guid="{guid}" ext="jpg"/>    ← same GUID, use <media> NOT <image>
Files table:        filepath = "images/{guid}.jpg"      ← WITH "images/" prefix
                    filepath = "thumbnails/{guid}.jpg"   ← WITH "thumbnails/" prefix


Key values for the XML layout:

BookWright page: width=693, height=594 (points at 72 DPI)
SKU: PHBK-1000x0800-IW-PPRLS
Image fill scale: 594/2475 = 0.24
Image x-offset: -22.5 (centers the slightly-wider image)
Page count must be even (add blank page at end if odd)
Schema version: 2.11, Archive version: 4
Include .version file with content 4
Cover sections: SC, DJ, IW (keep default dimensions, BookWright recalculates for page count)

Step 6: Add cover images

Render front and back cover designs as JPEGs and add them to the IW coversheet in the XML. Add the cover image files to both images/ and thumbnails/ paths in the Files table, and register them in media_registry.xml.

Step 7: Open in BookWright, review, and order

Open the .blurb file in BookWright
BookWright recalculates cover/spine dimensions for the page count
Click Review & Upload — verify no clipping in the print preview
Upload and order (check blurb.co.uk/promo for discount codes — Blurb frequently runs 20-30% off)
Select: Qty 2, Custom Logo Upgrade (remove Blurb logo), Standard Mid-Grey End Sheets
Troubleshooting
Problem	Cause	Fix
"Drag an image here" on all pages	Image resolution chain broken	Ensure bbf2.xml src, media_registry.xml guid, and Files.filepath all use the same GUID
Content clipped in print preview	Elements in bleed zone	Apply scale(0.91) wrapper to ALL page content
Broken image icons (small white rectangles)	CDN images timed out during render	Pre-download ALL images locally, replace URLs with file:// paths
Some .jpg downloads are HTML error pages	Original was -thumb.webp with no .jpg equivalent	Re-download as .webp format instead
Empty space on pages	Changed page width from 3075 to smaller value	Keep pages at 3075px, use scale(0.91) wrapper instead
"You forgot to design a cover" warning	No cover images in IW coversheet	Add front/back cover JPEGs to the coversheet XML
Full implementation details

See docs/BLURB_BOOKWRIGHT_EXPORT.md for complete code examples and the .blurb file format specification.

Workflow: Period in Review

Creates a personalized, scrollable "Period in Review" digital memory — a beautiful dark-themed timeline page with month-by-month insights, real conversation quotes, photos, and highlights. Everything is fact-checked against the actual WhatsApp messages.

When to use

The user says things like:

"Create a review of our 10 months together"
"Make a period in review from April 2025 to January 2026"
"Create the full review for this workspace"
"Make a year in review" / "Make our story"
What the user must specify

The user must provide one of:

"Full period" / "everything" — use the workspace context's relationshipInfo to extract start/end dates automatically
Specific dates — e.g., "from 06/04/2025 to 30/01/2026" (parse as DD/MM/YYYY UK format)

If the user doesn't specify, ask them: "Would you like the full period review (covering your entire time together), or a review for specific dates?"

Step-by-step pipeline
1. Determine the date range
# Get workspace context to find relationship dates
curl -s "$API/workspaces/{wsId}/context" -H "Authorization: Bearer $KEY"
# Look at relationshipInfo field for start/end dates

# Get persons
curl -s "$API/workspaces/{wsId}/persons" -H "Authorization: Bearer $KEY"


Calculate:

Number of months covered (this becomes the hero number)
Number of days between dates (e.g., 299)
Unix millisecond timestamps for dateFrom/dateTo in API calls
Cities they visited TOGETHER (only cities confirmed from conversations — do not assume)
2. Create memory, lock it, save before-snapshot
curl -s -X POST "$API/workspaces/{wsId}/memories" \
  -H "Authorization: Bearer $KEY" \
  -H "Content-Type: application/json" \
  -d '{"title": "Our First N Months — Name1 & Name2", "mode": "digital"}'

curl -s -X POST "$API/memories/{memoryId}/lock" -H "Authorization: Bearer $KEY"

curl -s -X POST "$API/memories/{memoryId}/snapshots" \
  -H "Authorization: Bearer $KEY" -H "Content-Type: application/json" \
  -d '{"label": "Before — initial empty memory"}'

3. Export ALL data (call each ONCE, cache to disk)
# Photos — includes persons[] array showing who is in each photo
curl -s "$API/workspaces/{wsId}/photos/export?dateFrom={ts}&dateTo={ts}" \
  -H "Authorization: Bearer $KEY" > /tmp/photos.json

# Conversations — full message text inline
curl -s "$API/workspaces/{wsId}/conversations/export?dateFrom={ts}&dateTo={ts}" \
  -H "Authorization: Bearer $KEY" > /tmp/convos.json

# Day summaries (if any exist — check counts first)
curl -s "$API/workspaces/{wsId}/summaries/counts" -H "Authorization: Bearer $KEY"
# If day count > 0:
curl -s "$API/workspaces/{wsId}/summaries/export?type=day" -H "Authorization: Bearer $KEY" > /tmp/summaries.json


NEVER re-fetch exports. Cache locally and reference from cache for all subsequent operations.

4. Select best photos per month

Use parallel agents (one per task) for efficiency. For each month:

Scoring algorithm:

Criteria	Points
Both persons in persons[] array	+200
One person (primary)	+80
Tags: romantic, joyful, traveling, celebration	+15 each
Person confidence × 30	variable

Disqualifiers: tags food, screenshot, meme, document, sticker, illustration

Deduplication: Photos with dateTaken within 5 minutes = same event. Keep only one.

Select top 3 per month. Ensure variety (different dates/events).

5. Verify every selected photo
# For each photo ID selected:
curl -s "$API/photos/{photoId}" -H "Authorization: Bearer $KEY"


Confirm: exists, dateTaken matches intended month, extract urls.original.

NEVER use URLs from the export directly — always verify via individual GET.

6. Analyze conversations per month

Use parallel agents (one per 2-3 months). For each month, read 4-6 conversation chunks. Extract:

Field	Description
emoji	One emoji representing the month's theme
theme	2-4 word label (e.g., "Nervous beginnings bloom")
insight	1-2 sentence summary, third person, warm/nostalgic, specific
memorableMessage	EXACT quote from conversations (search for literal match)
messageSender	Who said it
totalMessages	Sum of messageCount across chunks
keyEvent	Most notable event that actually happened

Rules:

Only include REAL quotes — must be exact text from a message
Write insights in third person using actual names
Reference real places, events, dates
Distinguish "planned" vs "actually happened"
If someone retells a past story, do NOT present it as a current event
If day summaries exist for that month, prefer those over raw conversation reading
7. Fact-check EVERYTHING (mandatory — do not skip)

Launch verification agents that re-read conversation text and check EVERY claim:

Check	What to look for
Every quote	Search for exact text. Note if it's actually multiple messages merged
Every event	Did it actually happen, or was it just discussed?
Every date	Correct day? Messages after midnight = next day
Every place	Actually mentioned in messages?
Past vs present	Is an anecdote being retold, or did it happen this month?
Corrections	If someone says "30 min" then corrects to "20", use corrected value
Numbers	Calculate day counts mathematically. Don't round 299 to 300

Common fabrication patterns:

Date bleeding (~30%): wrong day attribution
Fabricated details (~20%): inventing names/places/events
Planned vs happened (~15%): saying they did something they only discussed
Past stories as current (~10%): retold anecdote framed as recent event

Minimum 2 verification passes. Fix all issues before building HTML.

7b. Gather extra quotes for decorative elements

Before building HTML, search conversations for 15-20 SHORT heartfelt quotes (under 25 words each) from both people, spread across all months. These fill the "dead space" between sections as floating quote strips, interludes, and quote mosaics — making the page feel rich and personal.

Look for: terms of endearment, "I miss you" variants, funny moments, inside jokes, declarations of love, short sweet messages.

8. Build the HTML

Self-contained HTML with only CSS — no JavaScript at all. Wrapped in <div data-mw-page="1">.

Design direction: "Cinematic Love Letter" — luxury magazine editorial crossed with a love letter. Rich, intimate, layered. NO dead space.

Page structure (8 sections):

Hero — Massive gold-gradient number (250px Playfair Display) with glow pulse animation, Dancing Script subtitle, tracked Nunito names, gold shimmer divider lines, row of 5 circular photos with individual float animations
Quote strip — Full-width glassmorphism strip with a beautiful quote, giant decorative open-quote watermark, breathe animation
Stats bar — 5 stats with gold gradient numbers in Playfair, staggered reveal animations, gold divider lines between
Month timeline — Vertical gold-gradient line with pulsing dots. Each month card has: large 220px featured photo (not a tiny thumbnail) with zoom-on-hover, mood-colored dot badge, italic Cormorant Garamond insight, dual message bubbles (rose-left, gold-right tints). 4 Memory Interludes between month groups — full-width photo + quote pairs in glassmorphic frames
Quote mosaic — 3x2 grid of 6 short quote cards with staggered reveal, decorative watermarks, different color tints per person
Highlights — 3 editorial cards: best message (chat bubble), journey numbers (stats table), best chapter (narrative + photo)
Closing photo mosaic — Creative asymmetric grid of 4 photos with staggered rotation reveals and caption overlay
Footer — Gradient cursive names + MemoriesWeave credit

Typography:

Cormorant Garamond — elegant serif for insights and body (more refined than Lora)
Dancing Script — romantic script accents
Playfair Display — bold serif for headings and the big number
Nunito — clean sans for UI labels

13+ CSS animations (all pure @keyframes, no JS): heroScale, glowPulse, floatPhoto1-5, shimmer, revealUp, breathe, timelinePulse, quoteReveal, fadeInScale, mosaicReveal1-4, goldLine, particleDrift

Plus @supports (animation-timeline: view()) for scroll-driven reveals on Chrome 115+.

CRITICAL DOMPurify rules (the iframe strips these — do NOT use):

NO <script> tags — ALL JavaScript is removed by DOMPurify
NO <canvas> — not in allowed tags
NO <defs>, <linearGradient>, <stop> — stripped. Use solid rgba() fills instead
NO id attributes — stripped. Use class only
NO data-sentiment or custom data-* — use CSS classes like mood-high, mood-mid, mood-low
NO preserveAspectRatio on SVG — stripped
SVG stroke properties must be in style="..." attribute
ONLY allowed tags: html, head, body, style, link, meta, div, span, p, h1-h6, img, a, section, article, header, footer, svg, path, circle, rect, table, tr, td, th, ul, ol, li, etc.
Google Fonts via @import in <style> tag, not <link> tags

CSS particles (replace canvas): Use ::before pseudo-element with radial-gradient dot pattern and particleDrift keyframe animation.

Responsive breakpoints: 1024px, 900px, 600px, 400px. Stats wrap, photos shrink, timeline stays single-column.

Full implementation details: See docs/PERIOD_IN_REVIEW_PIPELINE.md

9. Push, verify, finalize
# Push HTML
curl -s -X PATCH "$API/memories/{memoryId}/pages/batch" \
  -H "Authorization: Bearer $KEY" -H "Content-Type: application/json" \
  -d @/tmp/push_body.json

# Screenshot to verify
curl -s "https://www.memoriesweave.com/api/screenshot?memoryId={memoryId}&page=1" \
  -H "Authorization: Bearer $KEY"

# Save after-snapshot
curl -s -X POST "$API/memories/{memoryId}/snapshots" \
  -H "Authorization: Bearer $KEY" -H "Content-Type: application/json" \
  -d '{"label": "After — complete period review with verified content"}'

# Unlock
curl -s -X POST "$API/memories/{memoryId}/unlock" -H "Authorization: Bearer $KEY"

10. Give the user the link
https://www.memoriesweave.com/workspace/{wsId}/memories/{memoryId}

Full implementation details

See docs/PERIOD_IN_REVIEW_PIPELINE.md for complete CSS templates, JS code, HTML templates for every section, and all lessons learned.

Error codes
Code	Status	Meaning
bad_request	400	Invalid parameters
unauthorized	401	Missing or invalid API key
not_found	404	Resource not found
rate_limited	429	Too many requests
internal_error	500	Server error
Weekly Installs
19
Repository
hero988/memorie…ve-skill
First Seen
Mar 14, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykFail