---
rating: ⭐⭐⭐
title: wordpress-elementor
url: https://skills.sh/jezweb/claude-skills/wordpress-elementor
---

# wordpress-elementor

skills/jezweb/claude-skills/wordpress-elementor
wordpress-elementor
Installation
$ npx skills add https://github.com/jezweb/claude-skills --skill wordpress-elementor
Summary

Edit Elementor pages and manage templates on WordPress sites via WP-CLI or browser automation.

Choose WP-CLI for safe text and URL replacements within widgets; use browser automation for structural changes, styling, and template application
Workflow: identify the page, back up Elementor data, execute edits, flush CSS cache, and verify the live result
Supports template duplication, template library management, and page cloning via WP-CLI meta operations
Always clear Elementor's CSS cache after WP-CLI changes to ensure visual updates appear on the live site
SKILL.md
WordPress Elementor

Edit Elementor pages and manage templates on existing WordPress sites. Produces updated page content via browser automation (for visual/structural changes) or WP-CLI (for safe text replacements).

Prerequisites
Working WP-CLI connection or admin access (use wordpress-setup skill)
Elementor installed and active: wp @site plugin status elementor
Workflow
Step 1: Identify the Page
# List Elementor pages
wp @site post list --post_type=page --meta_key=_elementor_edit_mode --meta_value=builder \
  --fields=ID,post_title,post_name,post_status

# Editor URL format: https://example.com/wp-admin/post.php?post={ID}&action=elementor

Step 2: Choose Editing Method
Change Type	Method	Risk
Text content updates	WP-CLI search-replace	Low (with backup)
Image URL swaps	WP-CLI meta update	Low (with backup)
Widget styling	Browser automation	None
Add/remove sections	Browser automation	None
Layout changes	Browser automation	None
Template application	Browser automation	None

Rule of thumb: If you're only changing text or URLs within existing widgets, WP-CLI is faster. For anything structural, use the visual editor via browser.

Step 3a: Text Updates via WP-CLI

Always back up first:

wp @site post meta get {post_id} _elementor_data > /tmp/elementor-backup-{post_id}.json


Pre-flight checklist:

Back up the postmeta (above)
Dry run the replacement
Verify the dry run matches expectations (correct number of replacements)
Execute
Flush CSS cache
Verify visually

Simple text replacement:

# Dry run
wp @site search-replace "Old Heading Text" "New Heading Text" wp_postmeta \
  --include-columns=meta_value --dry-run --precise

# Execute (after confirming dry run looks correct)
wp @site search-replace "Old Heading Text" "New Heading Text" wp_postmeta \
  --include-columns=meta_value --precise


After updating, clear Elementor's CSS cache:

wp @site elementor flush-css


If the elementor WP-CLI command isn't available:

wp @site option delete _elementor_global_css
wp @site post meta delete-all _elementor_css


What's safe to replace:

Safe	Risky
Headings text	HTML structure
Paragraph text	Widget IDs
Button text and URLs	Section/column settings
Image URLs (same dimensions)	Layout properties
Phone numbers, emails	CSS classes
Addresses	Element ordering
Step 3b: Visual Editing via Browser Automation

For structural changes, use browser automation to interact with Elementor's visual editor.

Login flow (skip if already logged in via Chrome MCP):

Navigate to https://example.com/wp-admin/
Enter username and password
Click "Log In"
Wait for dashboard to load

Open the editor:

Navigate to https://example.com/wp-admin/post.php?post={ID}&action=elementor
Wait for Elementor loading overlay to disappear (can take 5-10 seconds)
Editor is ready when the left sidebar shows widget panels

Edit text content:

Click on the text element in the page preview (right panel)
The element becomes selected (blue border)
The left sidebar shows the element's settings
Under "Content" tab, edit the text in the editor field
Changes appear live in the preview
Click "Update" (green button, bottom left) or Ctrl+S

Edit heading:

Click the heading in the preview
Left sidebar > Content tab > "Title" field
Edit the text
Optionally adjust: HTML tag (H1-H6), alignment, link
Save

Change image:

Click the image widget in the preview
Left sidebar > Content tab > click the image thumbnail
Media Library opens
Select new image or upload
Click "Insert Media"
Save

Edit button:

Click the button in the preview
Left sidebar > Content tab: Text (label), Link (URL), Icon (optional)
Style tab: colours, typography, border, padding
Save

Using playwright-cli:

playwright-cli -s=wp-editor open "https://example.com/wp-admin/"
# Login first, then navigate to Elementor editor
playwright-cli -s=wp-editor navigate "https://example.com/wp-admin/post.php?post={ID}&action=elementor"


Or Chrome MCP if using the user's logged-in session.

Step 4: Manage Templates

List saved templates:

wp @site post list --post_type=elementor_library --fields=ID,post_title,post_status


Export a template (browser):

Navigate to: https://example.com/wp-admin/edit.php?post_type=elementor_library
Hover over the template > "Export Template"
Downloads as .json file

Import a template (browser):

Navigate to: https://example.com/wp-admin/edit.php?post_type=elementor_library
Click "Import Templates" at the top
Choose file > upload .json
Template appears in the library

Apply a template to a new page:

Create the page: wp @site post create --post_type=page --post_title="New Page" --post_status=draft
Open in Elementor via browser
Click the folder icon (Add Template)
Select from "My Templates" tab
Click "Insert"
Customise and save

Duplicate an existing page via WP-CLI:

# Get source page's Elementor data
SOURCE_DATA=$(wp @site post meta get {source_id} _elementor_data)
SOURCE_CSS=$(wp @site post meta get {source_id} _elementor_page_settings)

# Create new page
NEW_ID=$(wp @site post create --post_type=page --post_title="Duplicated Page" --post_status=draft --porcelain)

# Copy Elementor data
wp @site post meta update $NEW_ID _elementor_data "$SOURCE_DATA"
wp @site post meta update $NEW_ID _elementor_edit_mode "builder"
wp @site post meta update $NEW_ID _elementor_page_settings "$SOURCE_CSS"

# Regenerate CSS
wp @site elementor flush-css


Apply template between pages via WP-CLI:

# Get source data
SOURCE=$(wp @site post meta get {source_id} _elementor_data)
SETTINGS=$(wp @site post meta get {source_id} _elementor_page_settings)

# Apply to target
wp @site post meta update {target_id} _elementor_data "$SOURCE"
wp @site post meta update {target_id} _elementor_edit_mode "builder"
wp @site post meta update {target_id} _elementor_page_settings "$SETTINGS"

# Clear cache
wp @site elementor flush-css

Step 5: Verify
# Check the page status
wp @site post get {post_id} --fields=ID,post_title,post_status,guid

# Get live URL
wp @site post get {post_id} --field=guid


Take a screenshot to confirm visual changes:

playwright-cli -s=verify open "https://example.com/{page-slug}/"
playwright-cli -s=verify screenshot --filename=page-verify.png
playwright-cli -s=verify close

Critical Patterns
Elementor Data Format

Elementor stores page content as JSON in _elementor_data postmeta. The structure is:

Section > Column > Widget


Each element has an id, elType, widgetType, and settings object. Direct manipulation of this JSON is possible but fragile -- always back up first and prefer search-replace over manual JSON editing.

CSS Cache

After any WP-CLI change to Elementor data, you must flush the CSS cache. Elementor pre-generates CSS from widget settings. Stale cache = visual changes don't appear.

wp @site elementor flush-css
# OR if elementor CLI not available:
wp @site option delete _elementor_global_css
wp @site post meta delete-all _elementor_css

Global Widgets

Global widgets are shared across pages. Editing one updates all instances.

# List global widgets
wp @site post list --post_type=elementor_library --meta_key=_elementor_template_type \
  --meta_value=widget --fields=ID,post_title


Caution: Replacing text in a global widget's data affects every page that uses it.

Elementor Pro vs Free
Feature	Free	Pro
Basic widgets	Yes	Yes
Theme Builder	No	Yes
Custom fonts	No	Yes
Form widget	No	Yes
WooCommerce widgets	No	Yes
Dynamic content	No	Yes

Theme Builder templates (header, footer, archive) are stored as elementor_library post type with specific meta indicating their display conditions.

Common Elementor WP-CLI Commands

If the Elementor CLI extension is available:

wp @site elementor flush-css          # Clear CSS cache
wp @site elementor library sync       # Sync with template library
wp @site elementor update db          # Update database after version change

Weekly Installs
1.0K
Repository
jezweb/claude-skills
GitHub Stars
759
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn