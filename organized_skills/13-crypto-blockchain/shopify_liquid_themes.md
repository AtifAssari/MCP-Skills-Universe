---
rating: ⭐⭐⭐
title: shopify-liquid-themes
url: https://skills.sh/shopify/liquid-skills/shopify-liquid-themes
---

# shopify-liquid-themes

skills/shopify/liquid-skills/shopify-liquid-themes
shopify-liquid-themes
Installation
$ npx skills add https://github.com/shopify/liquid-skills --skill shopify-liquid-themes
SKILL.md
Shopify Liquid Themes
Theme Architecture
.
├── sections/    # Full-width page modules with {% schema %} — hero, product grid, testimonials
├── blocks/      # Nestable components with {% schema %} — slides, feature items, text blocks
├── snippets/    # Reusable fragments via {% render %} — buttons, icons, image helpers
├── layout/      # Page wrappers (must include {{ content_for_header }} and {{ content_for_layout }})
├── templates/   # JSON files defining which sections appear on each page type
├── config/      # Global theme settings (settings_schema.json, settings_data.json)
├── locales/     # Translation files (en.default.json, fr.json, etc.)
└── assets/      # Static CSS, JS, images (prefer {% stylesheet %}/{% javascript %} instead)

When to use what
Need	Use	Why
Full-width customizable module	Section	Has {% schema %}, appears in editor, renders blocks
Small nestable component with editor settings	Block	Has {% schema %}, can nest inside sections/blocks
Reusable logic, not editable by merchant	Snippet	No schema, rendered via {% render %}, takes params
Logic shared across blocks/snippets	Snippet	Blocks can't {% render %} other blocks
Liquid Syntax
Delimiters
{{ ... }} — Output (prints a value)
{{- ... -}} — Output with whitespace trimming
{% ... %} — Logic tag (if, for, assign) — prints nothing
{%- ... -%} — Logic tag with whitespace trimming
Operators

Comparison: ==, !=, >, <, >=, <= Logical: and, or, contains

Critical Gotchas
No parentheses in conditions — use nested {% if %} instead
No ternary — always use {% if cond %}value{% else %}other{% endif %}
for loops max 50 iterations — use {% paginate %} for larger arrays
contains only works with strings — can't check objects in arrays
{% stylesheet %}/{% javascript %} don't render Liquid — no Liquid inside them
Snippets can't access outer-scope variables — pass them as render params
include is deprecated — always use {% render 'snippet_name' %}
{% liquid %} tag — multi-line logic without delimiters; use echo for output
Variables
{% assign my_var = 'value' %}
{% capture my_var %}computed {{ value }}{% endcapture %}
{% increment counter %}
{% decrement counter %}

Filter Quick Reference

Filters are chained with |. Output type of one filter feeds input of next.

Array: compact, concat, find, find_index, first, has, join, last, map, reject, reverse, size, sort, sort_natural, sum, uniq, where String: append, capitalize, downcase, escape, handleize, lstrip, newline_to_br, prepend, remove, replace, rstrip, slice, split, strip, strip_html, truncate, truncatewords, upcase, url_decode, url_encode Math: abs, at_least, at_most, ceil, divided_by, floor, minus, modulo, plus, round, times Money: money, money_with_currency, money_without_currency, money_without_trailing_zeros Color: color_brightness, color_darken, color_lighten, color_mix, color_modify, color_saturate, color_desaturate, color_to_hex, color_to_hsl, color_to_rgb Media: image_url, image_tag, video_tag, external_video_tag, media_tag, model_viewer_tag URL: asset_url, asset_img_url, file_url, shopify_asset_url HTML: link_to, script_tag, stylesheet_tag, time_tag, placeholder_svg_tag Localization: t (translate), format_address, currency_selector Other: date, default, json, structured_data, font_face, font_url, payment_button

Full details: language filters, HTML/media filters, commerce filters

Tags Quick Reference
Category	Tags
Theme	content_for, layout, section, sections, schema, stylesheet, javascript, style
Control	if, elsif, else, unless, case, when
Iteration	for, break, continue, cycle, tablerow, paginate
Variable	assign, capture, increment, decrement, echo
HTML	form, render, raw, comment, liquid
Documentation	doc

Full details with syntax and parameters: references/tags.md

Objects Quick Reference
Global objects (available everywhere)

cart, collections, customer, localization, pages, request, routes, settings, shop, template, theme, linklists, images, blogs, articles, all_products, metaobjects, canonical_url, content_for_header, content_for_layout, page_title, page_description, handle, current_page

Page-specific objects
Template	Objects
/product	product, remote_product
/collection	collection, current_tags
/cart	cart
/article	article, blog
/blog	blog, current_tags
/page	page
/search	search
/customers/*	customer, order

Full reference: commerce objects, content objects, tier 2, tier 3

Schema Tag

Sections and blocks require {% schema %} with a valid JSON object. Sections use section.settings.*, blocks use block.settings.*.

Section schema structure
{
  "name": "t:sections.hero.name",
  "tag": "section",
  "class": "hero-section",
  "limit": 1,
  "settings": [],
  "max_blocks": 16,
  "blocks": [{ "type": "@theme" }],
  "presets": [{ "name": "t:sections.hero.name" }],
  "enabled_on": { "templates": ["index"] },
  "disabled_on": { "templates": ["password"] }
}

Block schema structure
{
  "name": "t:blocks.slide.name",
  "tag": "div",
  "class": "slide",
  "settings": [],
  "blocks": [{ "type": "@theme" }],
  "presets": [{ "name": "t:blocks.slide.name" }]
}

Setting type decision table
Need	Setting Type	Key Fields
On/off toggle	checkbox	default: true/false
Short text	text	placeholder
Long text	textarea	placeholder
Rich text (with <p>)	richtext	—
Inline rich text (no <p>)	inline_richtext	—
Number input	number	placeholder
Slider	range	min, max, default (all required), step, unit
Dropdown/segmented	select	options: [{value, label}]
Radio buttons	radio	options: [{value, label}]
Text alignment	text_alignment	default: "left"/"center"/"right"
Color picker	color	default: "#000000"
Image upload	image_picker	—
Video upload	video	—
External video URL	video_url	accept: ["youtube", "vimeo"]
Product picker	product	—
Collection picker	collection	—
Page picker	page	—
Blog picker	blog	—
Article picker	article	—
URL entry	url	—
Menu picker	link_list	—
Font picker	font_picker	default (required)
Editor header	header	content (no id needed)
Editor description	paragraph	content (no id needed)
visible_if pattern
{
  "visible_if": "{{ block.settings.layout == 'vertical' }}",
  "type": "select",
  "id": "alignment",
  "label": "t:labels.alignment",
  "options": [...]
}


Conditionally shows/hides a setting in the editor based on other setting values.

Block entry types
{ "type": "@theme" } — Accept any theme block
{ "type": "@app" } — Accept app blocks
{ "type": "slide" } — Accept only the slide block type

Full schema details and all 33 setting types: references/schema-and-settings.md

CSS & JavaScript
Per-component styles and scripts

Use {% stylesheet %} and {% javascript %} in sections, blocks, and snippets:

{% stylesheet %}
  .my-component { display: flex; }
{% endstylesheet %}

{% javascript %}
  console.log('loaded');
{% endjavascript %}

One tag each per file — multiple {% stylesheet %} tags will error
No Liquid inside — these tags don't process Liquid; use CSS variables or classes instead
Only supported in sections/, blocks/, and snippets/
{% style %} tag (Liquid-aware CSS)

For dynamic CSS that needs Liquid (e.g., color settings that live-update in editor):

{% style %}
  .section-{{ section.id }} {
    background: {{ section.settings.bg_color }};
  }
{% endstyle %}

CSS patterns for settings

Single CSS property — use CSS variables:

<div style="--gap: {{ block.settings.gap }}px">


Multiple CSS properties — use CSS classes as select values:

<div class="{{ block.settings.layout }}">

LiquidDoc ({% doc %})

Required for: snippets (always), blocks (when statically rendered via {% content_for 'block' %})

{% doc %}
  Brief description of what this file renders.

  @param {type} name - Description of required parameter
  @param {type} [name] - Description of optional parameter (brackets = optional)

  @example
  {% render 'snippet-name', name: value %}
{% enddoc %}


Param types: string, number, boolean, image, object, array

Translations
Every user-facing string must use the t filter
<!-- Correct -->
<h2>{{ 'sections.hero.heading' | t }}</h2>
<button>{{ 'products.add_to_cart' | t }}</button>

<!-- Wrong — never hardcode strings -->
<h2>Welcome to our store</h2>

Variable interpolation
{{ 'products.price_range' | t: min: product.price_min | money, max: product.price_max | money }}


Locale file:

{
  "products": {
    "price_range": "From {{ min }} to {{ max }}"
  }
}

Locale file structure
locales/
├── en.default.json          # English translations (required)
├── en.default.schema.json   # Editor setting translations (required)
├── fr.json                  # French translations
└── fr.schema.json           # French editor translations

Key naming conventions
Use snake_case and hierarchical keys (max 3 levels)
Use sentence case for all text (capitalize first word only)
Schema labels use t: prefix: "label": "t:labels.heading"
Group by component: sections.hero.heading, blocks.slide.title
References
Filters: language (77), HTML/media (45), commerce (30)
Tag reference (30 tags)
Objects: commerce (5), content (10), tier 2 (69), tier 3 (53)
Schema & settings reference (33 types)
Complete examples (snippet, block, section)
Weekly Installs
31
Repository
shopify/liquid-skills
GitHub Stars
11
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass