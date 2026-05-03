---
rating: ⭐⭐⭐
title: cpq-builder
url: https://skills.sh/customware-ai/skills/cpq-builder
---

# cpq-builder

skills/customware-ai/skills/cpq-builder
cpq-builder
Installation
$ npx skills add https://github.com/customware-ai/skills --skill cpq-builder
SKILL.md
CPQ Builder Skill
What This Skill Does

This skill defines how to build a Configure-Price-Quote tool — any system where users configure inputs, the system applies rules to calculate results, and the output is a formatted document that may require review/approval.

CPQ is NOT limited to product pricing. The same structural pattern covers:

Domain	"Configure"	"Price" (Calculate)	"Quote" (Output)
Equipment sales	Select product, pick options	Apply markup, calculate totals	Sales quote PDF
Legal calculators	Enter case details (income, duration)	Apply guideline formulas	Summary report with estimates
Insurance estimators	Enter coverage details	Apply rate tables	Premium estimate document
Loan qualification	Enter financial details	Apply lending criteria	Qualification letter
Benefits eligibility	Enter personal details	Apply eligibility rules	Benefits summary
Service proposals	Select services, set scope	Apply labor rates	Service proposal

The builder reads this skill, reads the DOMAIN.md for the specific domain terminology and rules, and generates a working prototype. The DOMAIN.md determines whether the tool is about crane quotes or divorce calculations — the skill defines the structure.

When to Use This Skill

The Builder Agent should select this skill when the customer's DOMAIN.md contains:

Classic CPQ signals:

Products or services that are quoted/priced for customers
Configuration options (sizes, models, variants, materials)
Dependencies between products (requires, recommends, excludes)
Markup or margin-based pricing (cost-plus, vendor list + percentage)
A quoting or proposal workflow (draft → review → approve → send)

Broader "configure-calculate-output" signals:

A calculator, estimator, or assessment tool
Guided intake forms where inputs drive calculated outputs
Multi-step data collection with rules applied to produce results
Output documents (reports, summaries, estimates, proposals)
A preparer/reviewer workflow (client fills in → professional reviews)
"Fill out this form based on these guidelines and get an estimate"

Classification signals from the Clarence transcript:

"quoting is a mess," "inconsistent pricing," "reps don't know what goes with what"
"calculator," "estimator," "guided form," "step-through guide"
"fill out fields and get a result," "apply the guidelines," "produce a report"
"client submits, then the [professional] reviews"
Products with accessories, parts, or services that must go together

Do NOT use this skill when the domain is primarily about inventory tracking (use ERP skill), ongoing project execution with field tracking and payments (use trades-builder), online product sales (use e-commerce skill), or customer relationship management (use CRM skill).

Template Contract

Before you start building, understand what the template gives you and what this skill adds. This is the contract:

The template (app/layouts/MainLayout.tsx) ships with:

SidebarProvider, Sidebar, SidebarContent, SidebarInset, SidebarTrigger — already wired
SidebarContent is empty — this is your landing zone
One brand slot in the header (logo placeholder + company name)
ModeToggle and user menu in the header's right cluster

This skill fills:

SidebarContent — with the vertical stepper and saved items (see Layout Pattern below)
The brand slot in the header — with the client's logo and company name from DOMAIN.md
The header's right cluster — adds a role switcher DropdownMenu before the existing user menu
The <Outlet /> in <main> — via route components for each of the four sections

This skill does NOT:

Add a second Sidebar component. There is one sidebar.
Put a brand tile inside SidebarContent. Brand lives in the header only.
Rewire SidebarProvider or replace the collapsible behavior. Use what's there.
Put the stepper as horizontal tabs in the main content area. The stepper is a vertical list inside SidebarContent.

If you find yourself wanting to restructure MainLayout.tsx, stop — the answer is almost always to fill SidebarContent instead.

Section Definitions

The CPQ application has three navigable sections plus a fourth output view. The Builder Agent uses these as-is.

Section count rationale: CPQ has FOUR sections, not five. The older "Preview" section has been removed — its job (showing subtotal, tax, total before approval) is already done by the always-on Live Summary panel in the right sidebar, which updates continuously as the user configures the quote. A dedicated Preview step would be redundant. If a review gate before approval is genuinely needed, it belongs as a confirmation dialog on the Approve action, not as its own stepper step.

{
  "sections": [
    {
      "id": "configure",
      "label": "Configure",
      "icon": "Settings2",
      "order": 1,
      "component": "selector",
      "componentConfig": {
        "itemLayout": "grid",
        "showPrice": true,
        "showDescription": true,
        "showOptions": true,
        "selectionMode": "add-to-list",
        "groupBy": "category",
        "capturePricing": true
      },
      "dataSource": "data.products",
      "actions": [
        { "label": "Add to Quote", "action": "addSelected", "variant": "primary" }
      ]
    },
    {
      "id": "quote",
      "label": "Build Quote",
      "icon": "FileText",
      "order": 2,
      "component": "data-table",
      "componentConfig": {
        "columns": [
          { "key": "product", "label": "Product", "width": "auto" },
          { "key": "options", "label": "Configuration", "width": "auto" },
          { "key": "quantity", "label": "Qty", "width": "80px", "editable": true },
          { "key": "unitPrice", "label": "Unit Price", "width": "120px", "format": "currency", "editable": true },
          { "key": "total", "label": "Total", "width": "120px", "format": "currency", "computed": true }
        ],
        "showRowActions": true,
        "rowActions": ["edit", "duplicate", "remove"],
        "showTotalsFooter": true
      },
      "dataSource": "data.lineItems",
      "actions": [
        { "label": "Continue to Approval", "action": "navigateTo:approve", "variant": "primary" },
        { "label": "Clear All", "action": "clearItems", "variant": "ghost", "confirm": true }
      ]
    },
    {
      "id": "approve",
      "label": "Approve",
      "icon": "CheckCircle",
      "order": 3,
      "component": "form",
      "componentConfig": {
        "fields": [
          { "key": "customerName", "label": "Customer Name", "type": "text", "required": true },
          { "key": "customerEmail", "label": "Customer Email", "type": "email" },
          { "key": "paymentTerms", "label": "Payment Terms", "type": "select", "default": "net30" },
          { "key": "notes", "label": "Notes", "type": "textarea" },
          { "key": "validUntil", "label": "Valid Until", "type": "date" }
        ],
        "confirmBeforeSubmit": true
      },
      "dataSource": "data.quoteSettings",
      "gated": {
        "requires": ["customerName", "hasLineItems", "hasPricing", "noErrors"],
        "message": "Complete these before approving: customer name, at least one product with unit price, no unresolved dependency errors."
      },
      "actions": [
        { "label": "Approve & Send", "action": "approveQuote", "variant": "primary", "confirm": true },
        { "label": "Save Draft", "action": "saveDraft", "variant": "secondary" }
      ]
    },
    {
      "id": "document",
      "label": "Quote Document",
      "icon": "FileOutput",
      "order": 4,
      "component": "quote-document",
      "componentConfig": {
        "readOnly": true,
        "printable": true,
        "showBrandHeader": true,
        "showLineItemsTable": true,
        "showTotalsBlock": true,
        "showTermsBlock": true
      },
      "dataSource": "data.currentQuote",
      "actions": [
        { "label": "Back to Approve", "action": "navigateTo:approve", "variant": "ghost" }
      ]
    }
  ],
  "navMode": "stepper"
}


Navigation mode is stepper — the sidebar shows all sections as sequential steps. All steps are clickable at any time (not a wizard). The Approve step shows gating indicators when requirements aren't met. The Quote Document step becomes clickable once a quote is approved or saved as draft.

Pricing Capture is Mandatory (Not Optional)

A CPQ tool without pricing is not CPQ — it is intake routing. The Builder Agent MUST capture pricing during the Configure or Build Quote step when the domain has any pricing information. This is a hard requirement, not a preference.

What triggers pricing capture:

DOMAIN.md Entity Registry notes mention prices, rates, or costs for any entity ("Example price: $15,000")
DOMAIN.md has an Approved Pricing Reference, rate card, or pricing table
DOMAIN.md Business Rules reference monetary thresholds or calculations ("discounts over 15% require approval")
The domain is clearly a pricing/quoting domain (customer mentioned currency, tax, payment terms, quotes, estimates, proposals)

What the build must include when pricing is triggered:

Unit price field in the Configure or Build Quote step — either as a number input (simple case) or as a product picker that loads the price from a pricing table (catalog case). Never as a hardcoded constant.
Quantity field in the Build Quote step line items — default to 1, editable.
Line total computation — unit price × quantity, displayed per line and as a footer subtotal.
Tax line — computed as a percentage of subtotal. The tax name (HST, GST, VAT, Sales Tax) and rate come from DOMAIN.md. If the rate isn't specified, default to the jurisdiction's standard (HST → 13% for Ontario, GST → 5% for Canada-wide, etc.) and note the assumption in the completion summary.
Grand total — subtotal + tax, displayed prominently.
Payment terms — from DOMAIN.md (Net 30, Net 45, etc.) captured in the Approve step.
Currency — from DOMAIN.md. Format all money displays with the currency symbol or code (e.g., "CA$15,000.00" or "$15,000.00 CAD").

When pricing info is partial or missing:

If the domain is clearly a pricing domain but DOMAIN.md doesn't have specific price values, do NOT skip pricing capture — still build the pricing UI with empty/editable fields so the user can fill them in. Then note the gap in the completion summary: "DOMAIN.md mentions pricing but does not specify unit prices. Pricing UI is present and editable; unit prices are empty and must be entered by the user."

Example values from DOMAIN.md are seed data, not constants:

If DOMAIN.md says "Example price: $15,000," that value should appear as a default/seed in localStorage pricing data — NOT hardcoded in the UI, NOT embedded in rule logic. The user can change it. This is consistent with the "examples are data points, not canonical rules" extraction rule in the Knowledge Agent.

Failure mode to avoid: A CPQ prototype that shows "Quote Document" with Customer, Product, Motor, Status, and Terms — but no price, no subtotal, no tax, no grand total. That is a routing workflow masquerading as a quote. If the domain has any pricing signal, that build is incomplete regardless of how clean the UI looks.

Layout Pattern

The CPQ application uses a three-panel layout with FOUR sections (not five). The builder MUST follow this layout — not a single scrolling page with all sections stacked.

The four sections are: Configure, Build Quote, Approve, Quote Document. The task description from the project agent may only list three stages — the Quote Document is always added as the fourth section by this skill regardless of what the task says. Do not skip it.

The older Preview step has been removed. Its role (showing subtotal + tax + total before approval) is fully covered by the always-visible Live Summary panel in the right sidebar, which updates as the user configures the quote. Do not re-introduce a Preview step.

Left sidebar (always visible, collapsible)

The template ships SidebarProvider, Sidebar, SidebarContent, and SidebarTrigger already wired in app/layouts/MainLayout.tsx. SidebarContent is empty — that's the slot this skill fills. Do not re-wire the sidebar, do not add a second Sidebar component, and do not put a brand tile inside it. Brand identity lives in the header only (see Template Contract above).

Sidebar heading: Use a contextual label like "Quote workflow" or "Business process" — not the company name. The heading describes what the navigation IS, not who it's for.

Component	Content
Stepper	A VERTICAL list of ALL FOUR CPQ sections inside SidebarContent: (1) Configure, (2) Build Quote, (3) Approve, (4) Quote Document. Each step shows: step number, label, subtitle, and completion state (pending / active / done with checkmark). Clicking a step navigates to that section's panel. This is a vertical stepper in the sidebar — NOT horizontal tabs in the main content area.
Saved items	List of saved records stored in localStorage. Each shows name + status badge (Draft / Awaiting Review / Approved). Clicking loads the record. "New" button at top. Pin this section to the bottom of the sidebar so it's always visible without scrolling — use flexbox with stepper taking available space and saved items fixed at the bottom. Double-click a name to rename inline. The label should match the domain: "Saved quotes" for product domains, "Saved submissions" for intake/calculator domains, or whatever DOMAIN.md calls them.

The role switcher is in the header bar as a dropdown — not in the left sidebar. See Layout Principles in the builder prompt.

Main content (center — changes per section)

Only the active section renders. Do NOT stack all four sections on one scrolling page. Do NOT render sections as side-by-side cards. Each stepper step shows its corresponding panel at FULL WIDTH of the main content area. All other panels are hidden.

Do NOT put the stepper as horizontal tabs at the top of the main content area. The stepper belongs in the sidebar as a vertical list. The template's SidebarContent is already empty and waiting — fill it there.

Implementation: use a currentStep state variable (0–3, not 0–4). Render only the panel that matches currentStep. When the user clicks a stepper step, update currentStep and only that panel appears.

// Correct: ALL FOUR panels, conditional rendering
{currentStep === 0 && <ConfigurePanel />}
{currentStep === 1 && <BuildQuotePanel />}
{currentStep === 2 && <ApprovePanel />}
{currentStep === 3 && <QuoteDocumentPanel />}


If you define a WorkflowStep type, it must include all four:

type WorkflowStep = "configure" | "build" | "approve" | "document";

// WRONG: all panels visible, scroll to find the right one
<ConfigurePanel />
<BuildQuotePanel />
<ApprovePanel />
<QuoteDocumentPanel />

Section	What renders
Configure	Input selection or data entry. For product domains: inline product/options selector with unit price fields — pricing capture is mandatory when the domain has pricing signals (see Pricing Capture is Mandatory above). For calculator/intake domains: guided form sections with input fields, dropdowns, and validation. The DOMAIN.md determines which pattern fits.
Build Quote	Results assembly and review. For product domains: line items table with editable quantities, editable unit prices, and computed line totals, plus a totals footer showing subtotal + tax + grand total. For calculator/intake domains: calculated results table showing inputs → applied rules → outputs. Editable where the domain allows adjustments.
Approve	Approval owner display, status badge (Pending / Approved / Rejected). Approve and reject buttons, gated by presence of pricing data (cannot approve a priceless quote when the domain is a pricing domain). Gated by role — only roles with approval permission can approve. Other roles see a message: "You are viewing as [Name]. Only [approver names] can approve." For intake domains: the reviewer (lawyer, underwriter, advisor) reviews the submission. Clicking Approve should show a confirmation dialog summarizing the final totals before committing, since the old Preview step has been removed.
Quote Document	The final formatted output — what you would send to the customer or print. For product domains: a proper sales quote with brand header, line items table, totals, and terms. For calculator/intake domains: a summary report with inputs, calculations, results, and any disclaimers. See "Quote Document" section below for the required layout.
Quote Document (final output view)

This is the polished, recipient-facing document. It renders as a clean, printable layout inside the main content area — styled as if it could be handed directly to the customer. This is the actual deliverable the CPQ tool produces. Treat it as such: it is not a summary card, it is a document.

Minimum quality bar: if you would be embarrassed to email this to North Shore Fabrication as "the quote," it is not done. If it omits price, line items, tax, or grand total on a pricing domain, it is not done.

Layout — top to bottom, each a distinct block:

1. Document header block — two columns:

Left: brand logo when available, the full company name, and company address (placeholder address if not in DOMAIN.md: "123 Main St, City, Province, Postal Code — update in settings").
Right: document title ("Quote"), document reference number (auto-generated, e.g., "Q-2026-0001"), document date, "Valid until" date (from Approve step).

Render logos robustly. If a logo URL is missing, broken, expired, relative, or blocked, fall back to a styled initials mark.

2. Prepared-for block — a labeled "Prepared for" section with the customer's name, contact email, and any customer company name captured during Configure. Give this block visual weight — it's the most important identity on the document.

3. Line items table — for product/pricing domains, a proper table with these columns:

Column	Content
#	Line number (1, 2, 3...)
Description	Product name + configuration details ("Single girder crane — Motor A")
Qty	Quantity
Unit Price	Per-unit price, formatted with currency
Line Total	Qty × Unit Price, formatted with currency

For calculator/intake domains: an inputs table (left column: input name, right column: value) instead of a line items table, followed by a results table (left: result name, right: computed value with formula note).

4. Totals block — right-aligned, structured as a stack:

Subtotal:                    $XX,XXX.00
HST (13%):                    $X,XXX.00
─────────────────────────────────────────
Total:                       $XX,XXX.00 CAD


The Total row should be visually prominent — larger font, bold, full currency label (e.g., "CAD", "USD").

5. Terms block — a clearly delimited section with:

Payment Terms (e.g., "Net 45")
Currency (e.g., "Canadian Dollars (CAD)")
Validity period (e.g., "This quote is valid for 30 days")
Any mandatory terms or disclaimers from DOMAIN.md (e.g., for legal calculators, the required "this is an estimate, not legal advice" language)

6. Status and approval block — status badge (Draft / Awaiting Review / Approved), approved-by name if applicable, approval date if applicable.

7. Footer — small print area for additional terms, contact info, or signature lines if the domain requires them.

This view is read-only. No edit controls anywhere on the document. The only action available is "Back to Approve" (which returns to the stepper). If the user wants to change something, they click back to Configure or Build Quote in the stepper. The Quote Document is the output, not a workspace.

Reference implementation (abbreviated):

<article className="bg-background border rounded-lg p-8 max-w-4xl mx-auto print:border-0 print:shadow-none">
  {/* 1. Header */}
  <header className="flex justify-between items-start pb-6 border-b">
    <div className="flex items-center gap-4">
      {BRAND_LOGO_URL ? (
        <img src={BRAND_LOGO_URL} alt={COMPANY_NAME} className="h-10 w-auto" />
      ) : (
        <div className="flex size-10 items-center justify-center rounded-md bg-primary/10 text-sm font-semibold text-primary">
          {COMPANY_INITIALS}
        </div>
      )}
      <div>
        <h1 className="text-xl font-bold">{COMPANY_NAME}</h1>
        <p className="text-sm text-muted-foreground">{COMPANY_ADDRESS}</p>
      </div>
    </div>
    <div className="text-right">
      <h2 className="text-2xl font-bold">Quote</h2>
      <p className="text-sm">{quote.ref}</p>
      <p className="text-sm text-muted-foreground">Date: {quote.date}</p>
      <p className="text-sm text-muted-foreground">Valid until: {quote.validUntil}</p>
    </div>
  </header>

  {/* 2. Prepared for */}
  <section className="py-6">
    <h3 className="text-sm font-semibold text-muted-foreground uppercase tracking-wide mb-2">
      Prepared for
    </h3>
    <p className="text-lg font-medium">{quote.customerName}</p>
    {quote.customerEmail && <p className="text-sm">{quote.customerEmail}</p>}
  </section>

  {/* 3. Line items */}
  <Table>
    <TableHeader>
      <TableRow>
        <TableHead className="w-12">#</TableHead>
        <TableHead>Description</TableHead>
        <TableHead className="w-20 text-right">Qty</TableHead>
        <TableHead className="w-32 text-right">Unit Price</TableHead>
        <TableHead className="w-32 text-right">Total</TableHead>
      </TableRow>
    </TableHeader>
    <TableBody>
      {quote.lineItems.map((item, i) => (
        <TableRow key={item.id}>
          <TableCell>{i + 1}</TableCell>
          <TableCell>
            <div className="font-medium">{item.product}</div>
            <div className="text-sm text-muted-foreground">{item.configuration}</div>
          </TableCell>
          <TableCell className="text-right">{item.quantity}</TableCell>
          <TableCell className="text-right">{formatCurrency(item.unitPrice, quote.currency)}</TableCell>
          <TableCell className="text-right">{formatCurrency(item.lineTotal, quote.currency)}</TableCell>
        </TableRow>
      ))}
    </TableBody>
  </Table>

  {/* 4. Totals */}
  <section className="flex justify-end py-6">
    <dl className="w-80 space-y-2">
      <div className="flex justify-between text-sm">
        <dt>Subtotal:</dt>
        <dd>{formatCurrency(quote.subtotal, quote.currency)}</dd>
      </div>
      <div className="flex justify-between text-sm">
        <dt>{quote.taxName} ({quote.taxRate}%):</dt>
        <dd>{formatCurrency(quote.taxAmount, quote.currency)}</dd>
      </div>
      <div className="flex justify-between text-lg font-bold pt-2 border-t">
        <dt>Total:</dt>
        <dd>{formatCurrency(quote.total, quote.currency)} {quote.currency}</dd>
      </div>
    </dl>
  </section>

  {/* 5. Terms */}
  <section className="py-6 border-t">
    <h3 className="text-sm font-semibold text-muted-foreground uppercase tracking-wide mb-2">
      Terms
    </h3>
    <dl className="grid grid-cols-2 gap-y-2 text-sm">
      <dt className="font-medium">Payment Terms:</dt>
      <dd>{quote.paymentTerms}</dd>
      <dt className="font-medium">Currency:</dt>
      <dd>{quote.currencyName}</dd>
      <dt className="font-medium">Validity:</dt>
      <dd>Valid until {quote.validUntil}</dd>
    </dl>
  </section>

  {/* 6. Status */}
  <footer className="pt-6 border-t flex justify-between items-center">
    <StatusBadge status={quote.status} />
    {quote.approvedBy && (
      <p className="text-sm text-muted-foreground">
        Approved by {quote.approvedBy} on {quote.approvedDate}
      </p>
    )}
  </footer>
</article>


What the document must NOT look like:

A 5-line key-value list showing "Customer: X, Product: Y, Motor: Z, Status: Awaiting Review, Terms: Net 45" inside a single card is not a Quote Document. It's a summary blurb. A customer receiving that would have no idea what they're being quoted, for how much, or what they're agreeing to. If your Quote Document would fit inside the Live Summary panel, you have not built a Quote Document.

Right sidebar (always visible)
Component	Content
Live summary	Live-updating sidebar summary: For product domains — selected product, chosen options, running subtotal, tax, total. For calculator domains — key inputs entered so far, preliminary results. Updates immediately when the user changes any input.
Workflow notes	Business rules and routing info from DOMAIN.md displayed as compact contextual notes. For calculator domains, this can include "Guidelines applied" or "Rules being used."
RBAC behavior
Seed localStorage with roles from DOMAIN.md User Roles or Stakeholder Map.
Role switcher is a single DropdownMenu dropdown in the header bar — not separate buttons for each role. The dropdown trigger shows the active role name and badge (e.g., "Jeff — Approver"). Clicking opens the menu listing all roles. Do NOT render each role as a separate button in the header row. One trigger, one dropdown menu. Selecting a new role updates the view immediately.
Approval gating: If DOMAIN.md says "only Andy or Jeff can approve," disable the Approve button when viewing as Dre or Manish. Show a clear message explaining why.
Routing visibility: If a role handles specific work types (e.g., "Dre handles maintenance"), show relevant routing info when that role is active.
Price and results visibility
For pricing domains: Show prices on EVERY screen where products or options appear. Option selection immediately updates the right sidebar Live Summary total. The Build Quote section shows subtotal + tax = total in a footer row. Use the tax type from DOMAIN.md (HST = 13%, GST = 5%). Currency from DOMAIN.md (CAD, USD) appears in all price displays. The Quote Document shows the full totals block as the recipient would see it.
For calculator/intake domains: Show calculated results as they become available. If partial results can be computed from the inputs entered so far, show them in the right sidebar Live Summary. The Build Quote section shows the full calculation results. Use the output format specified in DOMAIN.md (monetary amounts, percentages, ranges, scores). The Quote Document renders as a formal summary report.
shadcn/ui component mapping

Use these shadcn/ui components for each CPQ element. Do not build custom equivalents when an existing component does the job. Import from ~/components/ui/*.

Treat cards as an exception, not the default layout primitive. Inline content into the page body whenever possible. Use cards only when something truly needs emphasis, separation, repetition, or dialog/detail framing. Do not build card-heavy dashboards, cards inside cards, or generic grids of floating panels.

CPQ Element	Component	Source	Usage Notes
Product/options selector	RadioGroup, Checkbox, Select, Table	shadcn	Show product name, description, base price, and configuration fields inline. Use a card only if an item genuinely needs visual emphasis.
Motor / option selection	RadioGroup, RadioGroupItem	shadcn	Mutually exclusive options. Show price next to each label. Keep options inline or in a compact list.
Optional items (installation)	Checkbox with label	shadcn	Toggle on/off. Show description below the label.
Status badges	Badge	shadcn	Use variant="outline" for Draft, variant="default" for Awaiting Approval, variant="secondary" for Approved. Apply semantic colors via className.
Role badges	Badge	shadcn	variant="outline" for Staff, variant="default" for Approver, variant="secondary" for View only.
Line items table	Table, TableHeader, TableRow, TableCell	shadcn	Clean header row, right-align price columns. Use TableFooter for subtotal row.
Saved quotes list	Custom list with Badge	shadcn	Each item is a clickable row with Badge for status. Use ScrollArea if the list could overflow.
Form inputs	Input, Label	shadcn	Quote name, customer name, notes. Stack label above input.
Dropdowns	Select, SelectContent, SelectItem	shadcn	Lead source, assigned-to, motor selection (alternative to RadioGroup for compact layouts).
Action buttons	Button	shadcn	Primary: variant="default" with brand accent. Secondary: variant="outline". Destructive: variant="destructive".
Section dividers	Separator	shadcn	Between sections within a panel. Horizontal, subtle.
Stepper navigation	Custom (no library component)	—	Build as a vertical list of clickable items inside SidebarContent. Use cn() for active/done/pending states. Step number in a circle, label, subtitle, completion checkmark.
Role switcher	DropdownMenu	shadcn	In the header. Shows active role name and badge. Dropdown lists all roles.
Quote summary sidebar	Inline stacked label/value rows	shadcn primitives	Labels are text-muted-foreground text-sm. Values are font-medium. Total row is text-lg font-semibold.
Workflow notes sidebar	Compact muted note block	shadcn primitives	Reference material, not primary content. Small text, muted colors.
Confirmation dialogs	AlertDialog	shadcn	For destructive actions (delete quote, reject quote).
Toast notifications	Sonner / toast()	shadcn	After save, approve, reject, delete. Brief confirmation messages.
Quote document header	Header block with robust logo fallback + company name	shadcn primitives	Brand logo from domain.md assets. Placeholder address below.
Quote document pricing table	Table with TableFooter	shadcn	Clean itemized rows. Footer shows subtotal. Totals block below with large bold total.
Quote notes	Textarea	shadcn	Plain text editing for internal notes.
Config Schema

See references/config-schema.md for full TypeScript interfaces. Summary:

config
├── app                    ← Branding, theme (from brandfetch)
├── sections[]             ← Fixed (from this skill, above)
├── data
│   ├── products[]         ← Catalog of available products with options
│   ├── lineItems[]        ← Current quote contents (starts empty)
│   └── quoteSettings      ← Currency, tax, terms, markup
├── rules[]                ← Business rules (dependencies, validations)
└── roles[]                ← User roles and permissions

Deterministic Mapping Rules

The Builder Agent follows these rules mechanically to transform DOMAIN.md into config.json. No reasoning, no interpretation — execute the rules.

Entity → Configurable Item Mapping
FOR EACH entity in DOMAIN.md Entity Registry:

  — PRODUCT DOMAINS (entities have prices, options, accessories):
  WHERE entity description suggests a sellable product, equipment, service, or part:
    → CREATE config.data.products[] entry
    → SET id = slugify(entity name)
    → SET name = entity name (exact, from DOMAIN.md)
    → SET category = entity parent grouping or category (from Entity Registry or Relationship Map)
    → SET basePrice = entity price if stated (number, no currency symbol)
    → SET pricingSource = determine from context:
        IF "price list" or "vendor list" or "catalog price" → "catalog"
        IF "get a quote from vendor" or "depends on specs" → "vendor_rfq"
        IF "we know our cost and mark it up" → "cost_plus"
        IF no pricing discussed → "tbd"
    → SET options[] = from entity's "what varies" attributes:
        FOR EACH variation mentioned (size, model, capacity, material, type):
          → CREATE option entry with id, label, type, choices

  — CALCULATOR / INTAKE DOMAINS (entities are input fields with rules):
  WHERE entity description suggests an input field, data point, or parameter:
    → CREATE config.data.inputSections[] entry
    → GROUP related inputs into sections (e.g., "Personal details," "Financial details")
    → SET field.id = slugify(field name)
    → SET field.label = field name (exact, from DOMAIN.md)
    → SET field.type = infer from context:
        IF enumerated values → "select" with options
        IF yes/no → "checkbox"
        IF date → "date"
        IF number (income, amount, duration) → "number"
        IF free text → "text"
    → SET field.required = true if DOMAIN.md marks it as mandatory
    → SET field.validation = from business rules (min/max, format, constraints)

  WHERE entity has NO price, NO options, NO input role, and is NOT referenced:
    → SKIP — it's probably not configurable
    → ADD to Open Questions: "Is [entity] an input or a quotable item?"

Relationship → Rule Mapping
FOR EACH relationship in DOMAIN.md Relationship Map:

  IF relationship type = "requires":
    → CREATE config.rules[] entry
    → SET type = "requires"
    → SET severity = "error"
    → SET trigger = "addItem"
    → SET condition = { "item.category": [source entity category] }
    → SET action = { "suggest": [target entity id] }
    → IF relationship mentions size/model matching:
        → SET action.matchField = the matching attribute
    → SET message = relationship rationale from DOMAIN.md (the "because")
    → IF no rationale captured:
        → SET message = "[source] requires [target] — rationale not captured"

  IF relationship type = "recommends":
    → CREATE config.rules[] entry
    → SET type = "recommends"
    → SET severity = "warning"
    → SET trigger = "addItem"
    → SET condition = { "item.category": [source entity category] }
    → SET action = { "suggest": [target entity id] }
    → SET message = relationship rationale from DOMAIN.md

  IF relationship type = "excludes":
    → CREATE config.rules[] entry
    → SET type = "excludes"
    → SET severity = "error"
    → SET trigger = "addItem"
    → SET condition = { "item.category": [source entity category] }
    → SET action = { "block": [target entity id] }
    → SET message = relationship rationale from DOMAIN.md

Business Rule → Validation Mapping
FOR EACH rule in DOMAIN.md Business Rules:

  IF rule mentions "approval" or "requires authorization":
    → CREATE config.rules[] entry
    → SET type = "validates"
    → SET trigger = the action being gated (e.g., "setTerms", "approveQuote")
    → SET condition = the triggering condition
    → SET action = { "requireApproval": [role] }
    → SET severity = "warning"
    → SET message = rule rationale

  IF rule mentions "cannot" or "must not" or "not allowed":
    → CREATE config.rules[] entry
    → SET type = "validates"
    → SET trigger = the blocked action
    → SET condition = the triggering condition
    → SET action = { "block": true }
    → SET severity = "error"
    → SET message = rule rationale

  IF rule mentions pricing constraint (markup, margin, discount limit):
    → CREATE config.rules[] entry
    → SET type = "computes"
    → SET trigger = "priceCalculation"
    → SET condition = the pricing formula or constraint
    → SET action = { "compute": [formula description] }
    → SET message = rule rationale

State Model → Quote Settings Mapping
IF DOMAIN.md State Models contains payment terms or approval statuses:
  → MAP to config.data.quoteSettings.availableTerms[]
  → SET config.data.quoteSettings.defaultTerms = the default mentioned

IF DOMAIN.md State Models contains quote statuses:
  → MAP to section gating logic
  → The CPQ skill handles this through the fixed section definitions (Configure → Quote → Approve → Quote Document)

Branding → Theme Mapping
→ SET config.app.companyName = DOMAIN.md Project Overview company name
→ SET config.app.theme.primaryColor = from brandfetch (or fallback "#1a1a2e")
→ SET config.app.theme.accentColor = from brandfetch (or fallback "#3b82f6")
→ SET config.app.theme.logoUrl = from brandfetch
→ SET config.app.theme.mode = "light"

Quote Settings Mapping
→ SET config.data.quoteSettings.currency = from DOMAIN.md (or default "USD")
→ SET config.data.quoteSettings.taxEnabled = true/false based on DOMAIN.md
→ SET config.data.quoteSettings.taxLabel = from DOMAIN.md (e.g., "HST", "GST", "Sales Tax")
→ SET config.data.quoteSettings.taxRate = from DOMAIN.md (decimal, e.g., 0.13 for 13%)
→ SET config.data.quoteSettings.defaultTerms = from DOMAIN.md (e.g., "net30")
→ SET config.data.quoteSettings.markup = from DOMAIN.md (decimal, e.g., 0.375 for 37.5%)
→ SET config.data.quoteSettings.quoteFormat = "itemized" (default, unless DOMAIN.md says otherwise)

Role Mapping
FOR EACH role in DOMAIN.md User Roles:
  → CREATE config.roles[] entry
  → SET id = slugify(role name)
  → SET label = role name (exact, from DOMAIN.md)
  → SET permissions = infer from DOMAIN.md role description:
      IF role creates quotes → ["createQuote", "editQuote", "selectProducts"]
      IF role approves → ["approveQuote", "approveTerms", "viewReports"]
      IF role manages catalog → ["editCatalog", "editPricing"]
      IF role is view-only → ["viewQuotes"]
  → IF permissions cannot be inferred → SET permissions = ["createQuote", "editQuote"] (safe default)

Edge Cases
→ IF entity has no price → SET pricingSource = "tbd", ADD to config metadata openQuestions
→ IF relationship rationale is missing → SET message = "[source] [relationship] [target] — rationale not captured"
→ IF entity cannot be classified as a product → SKIP, ADD to config metadata openQuestions
→ IF DOMAIN.md has Open Questions → COPY to config.metadata.openQuestions for reference
→ IF no roles are defined in DOMAIN.md → CREATE one default role: { id: "user", label: "User", permissions: ["createQuote", "editQuote", "selectProducts"] }
→ IF no pricing information at all → SET quoteSettings.markup = 0, quoteSettings.currency = "USD", ADD note to openQuestions

Business Rule Templates

Common CPQ rule patterns the Builder Agent can use when DOMAIN.md describes rules in natural language:

Product Dependency (hard)
{
  "id": "BR-XXX",
  "type": "requires",
  "trigger": "addItem",
  "condition": { "item.category": "[source_category]" },
  "action": { "suggest": "[target_product_id]", "matchField": "[matching_attribute]" },
  "message": "[rationale from DOMAIN.md]",
  "severity": "error"
}

Product Recommendation (soft)
{
  "id": "BR-XXX",
  "type": "recommends",
  "trigger": "addItem",
  "condition": { "item.category": "[source_category]" },
  "action": { "suggest": "[target_product_id]" },
  "message": "[rationale from DOMAIN.md]",
  "severity": "warning"
}

Product Exclusion
{
  "id": "BR-XXX",
  "type": "excludes",
  "trigger": "addItem",
  "condition": { "item.category": "[source_category]" },
  "action": { "block": "[target_product_id]" },
  "message": "[rationale from DOMAIN.md]",
  "severity": "error"
}

Approval Gate
{
  "id": "BR-XXX",
  "type": "validates",
  "trigger": "[gated_action]",
  "condition": { "[field]": { "$ne": "[default_value]" } },
  "action": { "requireApproval": "[role_id]" },
  "message": "[rationale from DOMAIN.md]",
  "severity": "warning"
}

Price Computation
{
  "id": "BR-XXX",
  "type": "computes",
  "trigger": "priceCalculation",
  "condition": { "item.pricingSource": "cost_plus" },
  "action": { "compute": "sellingPrice = cost * (1 + markup)" },
  "message": "Cost-plus pricing: [markup]% markup applied",
  "severity": "info"
}

Vertical Presets

See references/vertical-presets.md for full details. Summary:

Vertical	"Configure" Inputs	Calculation Model	Key Rule Pattern	Output Style
Manufacturing / BOM	Products with options, accessories	Cost-plus or vendor RFQ	Equipment requires parts/installation	Itemized quote with scope of work
Wholesale / Distribution	Catalog items, bulk goods	Price list with volume tiers	Product bundles, case/pallet quantities	Itemized quote with quantity breaks
Services / Integrator	Equipment + installation + PM	Mixed (catalog + labor rates)	Equipment requires service, service includes consumables	Itemized quote with service schedule
Legal / Compliance	Case details, personal/financial data	Guideline formulas, statutory tables	Input dependencies (field X required when Y = Z)	Summary report with calculations + disclaimer
Financial / Insurance	Coverage details, risk factors	Rate tables, actuarial formulas	Eligibility rules, coverage limits	Estimate document with ranges + terms
Assessment / Eligibility	Personal/business details	Scoring models, threshold rules	Pass/fail criteria, tiered outcomes	Assessment report with recommendations

The Builder Agent uses the vertical preset as a starting point, then overrides with specifics from DOMAIN.md. For product domains, "Configure" means product selection. For calculator/intake domains, "Configure" means guided data entry.

Mapping Log

After executing the mapping rules, the Builder Agent should produce a brief mapping log as an audit trail:

## Mapping Log

**Skill:** cpq-builder v4.2
**DOMAIN.md:** [company name]
**Vertical preset:** [manufacturing / wholesale / services / legal / financial / assessment / none]

### Products mapped: [N]
- [entity name] → config.data.products[0] ([pricingSource], [N] options)
- [entity name] → config.data.products[1] ([pricingSource], [N] options)

### Rules mapped: [N]
- BR-001: [source] requires [target] → severity: error
- BR-002: [source] recommends [target] → severity: warning

### Skipped entities: [N]
- [entity name] — not a quotable product (added to openQuestions)

### Open questions carried forward: [N]
- [question from DOMAIN.md]


This log is NOT part of the config. It's a separate output that can be reviewed if the config seems wrong.

Reference Files
references/config-schema.md — Full TypeScript interfaces for the CPQ config shape
references/vertical-presets.md — Detailed presets for Manufacturing, Wholesale, and Services
references/example-config.json — Fully populated Total Water example config
Weekly Installs
372
Repository
customware-ai/skills
GitHub Stars
1
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass