---
title: searching-media
url: https://skills.sh/forcedotcom/afv-library/searching-media
---

# searching-media

skills/forcedotcom/afv-library/searching-media
searching-media
Installation
$ npx skills add https://github.com/forcedotcom/afv-library --skill searching-media
SKILL.md
Media Search

Universal routing skill for searching and retrieving existing images and media.

Scope

This skill is for SEARCHING FOR existing media, not CREATING new media.

Use this skill when the user wants to:

Search for images in Salesforce CMS, Data Cloud
Find existing visual assets to use in their app
Retrieve media from connected sources
Browse available images for their project
Locate specific photos or graphics

DO NOT use this skill when the user wants to:

Generate new images with AI (use image generation tools)
Create graphics or designs from scratch
Edit or modify existing images
Build custom visuals or diagrams
Before You Search

CRITICAL: This is a routing skill, not a direct search skill.

When a user requests to find an image:

Your first action MUST use the ask_followup_question tool to present search sources.

Use ask_followup_question to present available search sources as options
Receive the user's selection from the tool response
Then call the appropriate search tool based on their choice

Example of what NOT to do:

❌ Calling ANY tool before the user picks a source (MCP tools, file reads, descriptor checks, etc.)
❌ "Checking which MCP tools are available" — do not probe or discover tools via tool calls
❌ Immediately calling search_electronic_media or search_media_cms_channels
❌ Reading MCP tool descriptors or schemas to see what's available
❌ Deciding which search source to use without asking

Example of what TO do:

✅ Respond with ONLY text — a numbered list of search sources
✅ Ask: "Which option would you like to use?"
✅ Wait for user to reply with their choice
✅ Then (and only then) call the tool they selected

Your first response when this skill triggers MUST be a text-only message presenting search sources. No tool calls. No exceptions.

Workflow Overview

The user MUST choose the search source. You CANNOT skip this step.

Copy this checklist and track your progress:

Media Search Progress:
- [ ] Step 1: Check your own tool list for available search tools (no tool calls — just inspect what's in your context)
- [ ] Step 2: Present only the available options to the user as a numbered list (plain text, no tool calls)
- [ ] Step 3: Wait for the user to reply with their selection
- [ ] Step 4: Execute the selected search method (this is the first tool call)
- [ ] Step 5: Present all results to user for selection
- [ ] Step 6: Apply selected image to code


If you call any tool before step 4, you are not following this skill correctly.

Presenting Search Sources (First Response)

DO NOT call any tool, read any MCP descriptor, or make any external request to determine available tools.

Your tools are already loaded into your context. Look at the tool names you already have access to — this is introspection, not a tool call.

Step 1: Check your own tool list (no tool calls)

Look at the tools already in your context and check for these names:

search_media_cms_channels → If present, include "Search using keywords"
search_electronic_media → If present, include "Search using Data 360 hybrid search"
Always include "Other" as the last option

Step 2: Build your response

Include ONLY the sources whose tools you actually have. Number them sequentially.

I can help you find that image. Where would you like to search?

[NUMBER]. [SEARCH SOURCE NAME] — [Brief description]
...
[NUMBER]. Other — Provide your own URL or path

Which option would you like to use?


Step 3: Stop and wait

After presenting the list, STOP. Do not call any tool. Do not proceed. Wait for the user to reply with their choice.

Examples

Both tools available:

I can help you find that image. Where would you like to search?

1. Search using Data 360 hybrid search — Semantic search across Salesforce CMS and connected DAMs
2. Search using keywords — Search Salesforce CMS by keywords and taxonomies
3. Other — Provide your own URL or path

Which option would you like to use?


Only search_media_cms_channels available:

I can help you find that image. Where would you like to search?

1. Search using keywords — Search Salesforce CMS by keywords and taxonomies
2. Other — Provide your own URL or path

Which option would you like to use?


Only search_electronic_media available:

I can help you find that image. Where would you like to search?

1. Search using Data 360 hybrid search — Semantic search across Salesforce CMS and connected DAMs
2. Other — Provide your own URL or path

Which option would you like to use?


Neither tool available:

No automated media search sources are currently configured. Please provide a direct URL or asset library path.


Wait for the user to select before proceeding.

Executing the Selected Search Method

⚠️ ONLY reach this step if the user has explicitly selected an option from your numbered list.

If you haven't shown options yet, go back to the "Presenting Search Sources" section first.

After the user selects an option, execute the corresponding search method below.

Search using keywords

Tool: search_media_cms_channels

Process:

Analyze the query — Understand what the user is searching for (subject, attributes, domain)

Extract keywords — Concrete nouns that would appear in image metadata

Use domain-specific synonyms
Maximum 10 terms
Examples:
"luxury apartments" → apartment, villa, penthouse, residence, condo
"company logo" → logo, emblem, corporate logo
"bright room" → (empty if no concrete nouns)

Extract taxonomies — Descriptive qualities, styles, moods, categories

Only adjectives and attributes
Examples:
"luxury apartment with river view" → Luxury, Premium, Waterfront, Riverside, Panoramic
"bright spacious room" → Bright, Spacious, Open, Airy, Light
"car" → (empty if no descriptive terms)

Determine locale — Use format en_US, es_MX, fr_FR (default: en_US)

Build the JSON payload — Construct this exact structure:

{
  "inputs": [{
    "searchKeyword": "keyword1 OR keyword2 OR keyword3",
    "taxonomyExpression": "{\"OR\": [\"Taxonomy1\", \"Taxonomy2\"]}",
    "searchLanguage": "en_US",
    "channelIds": "",
    "channelType": "PublicUnauthenticated",
    "contentTypeFqn": "sfdc_cms__image",
    "pageOffset": 0,
    "searchLimit": 5
  }]
}


Field rules:

searchKeyword: Join keywords with OR (space-OR-space). Use empty string if no keywords.
taxonomyExpression: Stringify JSON object {"OR": ["term1", "term2"]}. Use "{}" if no taxonomies.
searchLanguage: Locale with underscore (e.g., en_US)
channelIds: Always empty string
channelType: Always "PublicUnauthenticated"
contentTypeFqn: Always "sfdc_cms__image"
pageOffset: Start at 0, increment by searchLimit for pagination
searchLimit: Default 5, adjust if user requests more

Examples:

Query: "luxury apartment with river view"

{
  "inputs": [{
    "searchKeyword": "apartment OR villa OR penthouse OR residence",
    "taxonomyExpression": "{\"OR\": [\"Luxury\", \"Premium\", \"Waterfront\", \"Riverside\"]}",
    "searchLanguage": "en_US",
    "channelIds": "",
    "channelType": "PublicUnauthenticated",
    "contentTypeFqn": "sfdc_cms__image",
    "pageOffset": 0,
    "searchLimit": 5
  }]
}


Query: "bright spacious room" (no concrete nouns)

{
  "inputs": [{
    "searchKeyword": "",
    "taxonomyExpression": "{\"OR\": [\"Bright\", \"Spacious\", \"Open\", \"Airy\"]}",
    "searchLanguage": "en_US",
    "channelIds": "",
    "channelType": "PublicUnauthenticated",
    "contentTypeFqn": "sfdc_cms__image",
    "pageOffset": 0,
    "searchLimit": 5
  }]
}


Query: "car images" (no descriptive terms)

{
  "inputs": [{
    "searchKeyword": "car OR automobile OR vehicle OR auto",
    "taxonomyExpression": "{}",
    "searchLanguage": "en_US",
    "channelIds": "",
    "channelType": "PublicUnauthenticated",
    "contentTypeFqn": "sfdc_cms__image",
    "pageOffset": 0,
    "searchLimit": 5
  }]
}

Call the tool with the exact JSON payload
Search using Data 360 hybrid search

Tool: search_electronic_media

Process:

Use the user's query as-is — no keyword extraction or transformation needed
Call search_electronic_media
Pass the query to the tool's searchQuery parameter

Example:

User query: "modern luxury apartment with natural lighting"
Tool call: search_electronic_media(searchQuery="modern luxury apartment with natural lighting")
Other (User-Provided URL)

Ask the user to provide:

Direct URL to the image
Asset library path
Specific system/location to check
Presenting Search Results

Your action MUST use the ask_followup_question tool to present search results as options.

Parse the tool response — Extract all image results (title and source)
Use ask_followup_question to present ALL results as selectable options. Show the image title only — do not display the URL.
Receive the user's selection from the tool response
Then apply the selected image
I found 4 images. Which one would you like to use?

1. Luxury Apartment Exterior
   Source: Salesforce CMS

2. Modern High-Rise Building
   Source: Salesforce CMS

3. Waterfront Residence
   Source: Salesforce CMS

4. Premium Condominium
   Source: Salesforce CMS


Never auto-select an image. Always wait for user choice.

Applying the Selected Image

After the user chooses:

Confirm the selection with image name and URL
Use the complete URL returned by the tool, including all query parameters. CMS and DAM URLs rely on query parameters for authentication, resizing, and CDN routing — dropping them breaks the image. For example, a URL like https://cms.example.com/media/img.jpg?oid=00D&refid=0EM&v=2 must be used in full.
Apply the URL to the user's code/component
Show what was changed (file path and line number)
Error Handling
Error	Response
Tool unavailable	"The [source name] tool is unavailable. Would you like to try a different source?"
Tool returns error	Show error message, offer retry with different terms or alternative source
No results found	"No results found. Try broader keywords, removing descriptive terms, or a different source."
Invalid user selection	Re-display options and ask again

Never silently fail. Always inform the user and offer alternatives.

Search Behavior Notes

Search using keywords:

Both keyword and taxonomy → results match keyword OR (keyword + taxonomy)
Empty keyword → search by taxonomy only
Empty taxonomy → search by keyword only
Use pageOffset for pagination (increment by searchLimit)

Search using Data 360 hybrid search:

Handles natural language queries
Semantic similarity matching
Searches across multiple connected systems
Key Principles
First response is always text-only — Present search sources without calling any tool
Only show configured sources — Check your own tool list (introspection, not tool calls) and only present sources whose tools you have
Wait for user selection — Never auto-select a source or image
Show all results — Let the user choose the best match
Confirm before applying — Verify the selection before modifying code
Handle errors gracefully — Provide clear feedback and alternatives
Weekly Installs
426
Repository
forcedotcom/afv-library
GitHub Stars
242
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail