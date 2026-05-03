---
rating: ⭐⭐⭐
title: localise
url: https://skills.sh/morphet81/cheat-sheets/localise
---

# localise

skills/morphet81/cheat-sheets/localise
localise
Installation
$ npx skills add https://github.com/morphet81/cheat-sheets --skill localise
SKILL.md
Lokalise Translation Generator

Generate an interactive HTML translation page for pasting translations into Lokalise.

When to Use
User provides an English string (with or without plural forms) and wants translations for Lokalise
User mentions translating a key for the app's supported languages
User needs a quick translation reference with copy-to-clipboard functionality
Input

Parse $ARGUMENTS as the English text to translate. The format is <english singular> [| <english plural>].

If $ARGUMENTS contains a | separator, split into singular (before |) and plural (after |)
If $ARGUMENTS has no |, treat the entire string as the singular (other) form for all languages
If $ARGUMENTS is empty, use AskUserQuestion to ask the user for the English text

The user may also provide:

Key name (optional): e.g. tables::selected_count. If not given, derive from the English string.
Variables: Strings may contain %{variable_name} interpolation tokens. Preserve these exactly in all translations.
Target Languages (in this exact order)
#	Code	Name	Plural Forms (Lokalise)	RTL
1	en	English	one, other	no
2	ar	Arabic	zero, one, two, few, many, other	yes
3	zh-CN	Chinese (Simplified)	other	no
4	zh-TW	Chinese (Traditional)	other	no
5	nl	Dutch	one, other	no
6	fr	French	one, other	no
7	de	German	one, other	no
8	he	Hebrew	one, other	yes
9	hi	Hindi	one, other	no
10	id	Indonesian	other	no
11	it	Italian	one, other	no
12	ja	Japanese	other	no
13	km	Khmer	other	no
14	ko	Korean	other	no
15	lo	Lao	other	no
16	ms	Malay	other	no
17	pt	Portuguese	one, other	no
18	ru	Russian	one, few, many, other	no
19	es	Spanish	one, other	no
20	tl	Tagalog	zero, one, two, few, many, other	no
21	th	Thai	other	no
22	tr	Turkish	one, other	no
23	vi	Vietnamese	other	no
Translation Guidelines
Preserve all %{...} interpolation variables exactly as-is in every translation.
For languages with only other: provide a single translation (no plural distinction).
For languages with one/other: provide singular and plural forms where grammatically appropriate. If the language doesn't change the noun (e.g. Hindi, Turkish for some words), the forms may be identical — that's fine.
For Russian (one/few/many/other): follow Russian plural declension rules.
For Arabic (zero/one/two/few/many/other): follow Arabic plural rules. zero form can omit the count variable if natural (e.g. "No items selected").
For Tagalog (zero/one/two/few/many/other): follow Tagalog linker rules. zero form can omit the count variable.
RTL languages (Arabic, Hebrew) get the rtl CSS class on their translation rows.
Translations should sound natural in a restaurant/hospitality UI context (TableCheck product).
Output

Generate a single self-contained HTML file.

File Location

Save the file to: {working_directory}/.tmp/translations-{sanitized_key}.html

Where {sanitized_key} is the key name (or derived slug) with special characters replaced by hyphens.

After generating, open the file with the default system browser:

# macOS
open "{filepath}"
# Linux
xdg-open "{filepath}"
# Try open first, fall back to xdg-open
open "{filepath}" 2>/dev/null || xdg-open "{filepath}"

HTML Structure

The generated HTML MUST follow this exact structure. Copy the template below precisely, only changing the dynamic content (key name, translations).

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{KEY_NAME} — Plural Translations</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #0e1117;
    --surface: #161b22;
    --surface-2: #1c2129;
    --border: #2d333b;
    --border-light: #373e47;
    --text: #e6edf3;
    --text-muted: #8b949e;
    --accent: #58a6ff;
    --accent-dim: #1a3a5c;
    --green: #3fb950;
    --green-dim: #1a3524;
    --yellow: #d29922;
    --yellow-dim: #3d2e00;
    --purple: #bc8cff;
    --purple-dim: #2a1a4e;
    --orange: #f0883e;
    --red: #f85149;
    --code-bg: #1a1f27;
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'DM Sans', sans-serif;
    padding: 40px 32px;
    line-height: 1.6;
  }

  .container {
    max-width: 1360px;
    margin: 0 auto;
  }

  header { margin-bottom: 36px; }

  h1 {
    font-size: 22px;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 6px;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  h1 code {
    font-family: 'JetBrains Mono', monospace;
    font-size: 16px;
    background: var(--accent-dim);
    color: var(--accent);
    padding: 3px 10px;
    border-radius: 6px;
    font-weight: 500;
  }

  .subtitle { color: var(--text-muted); font-size: 14px; }

  .legend { display: flex; gap: 20px; margin-top: 14px; flex-wrap: wrap; }
  .legend-item { display: flex; align-items: center; gap: 6px; font-size: 12px; color: var(--text-muted); }
  .legend-dot { width: 10px; height: 10px; border-radius: 3px; }
  .legend-dot.one { background: var(--green); }
  .legend-dot.other { background: var(--accent); }
  .legend-dot.few { background: var(--yellow); }
  .legend-dot.many { background: var(--purple); }
  .legend-dot.two { background: var(--orange); }
  .legend-dot.zero { background: var(--red); }

  table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    border: 1px solid var(--border);
    border-radius: 10px;
    overflow: hidden;
    font-size: 14px;
  }

  thead th {
    background: var(--surface-2);
    color: var(--text-muted);
    font-weight: 600;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    padding: 12px 16px;
    text-align: left;
    border-bottom: 1px solid var(--border);
    position: sticky;
    top: 0;
    z-index: 2;
  }

  thead th:first-child { width: 50px; }
  thead th:nth-child(2) { width: 140px; }
  thead th:nth-child(3) { width: 100px; }

  tbody tr { transition: background 0.15s; }
  tbody tr:hover { background: var(--surface); }
  tbody tr:not(:last-child) td { border-bottom: 1px solid var(--border); }
  td { padding: 10px 16px; vertical-align: top; }

  .lang-code { font-family: 'JetBrains Mono', monospace; font-size: 13px; font-weight: 500; color: var(--accent); }
  .lang-name { font-weight: 500; color: var(--text); font-size: 13px; }
  .lang-name span { color: var(--text-muted); font-weight: 400; font-size: 12px; display: block; }

  .form-tag {
    display: inline-block;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    font-weight: 500;
    padding: 2px 8px;
    border-radius: 4px;
    min-width: 46px;
    text-align: center;
    flex-shrink: 0;
  }

  .form-tag.one { background: var(--green-dim); color: var(--green); }
  .form-tag.other { background: var(--accent-dim); color: var(--accent); }
  .form-tag.few { background: var(--yellow-dim); color: var(--yellow); }
  .form-tag.many { background: var(--purple-dim); color: var(--purple); }
  .form-tag.two { background: #3d1f00; color: var(--orange); }
  .form-tag.zero { background: #3d1116; color: var(--red); }

  .translation-cell { display: flex; flex-direction: column; gap: 6px; }

  .translation-row {
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .translation-text {
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    color: var(--text);
    flex: 1;
  }

  .translation-text .var { color: var(--yellow); }

  .copy-btn {
    flex-shrink: 0;
    background: var(--surface-2);
    border: 1px solid var(--border);
    color: var(--text-muted);
    font-family: 'DM Sans', sans-serif;
    font-size: 11px;
    font-weight: 500;
    padding: 4px 10px;
    border-radius: 5px;
    cursor: pointer;
    transition: all 0.15s;
    display: flex;
    align-items: center;
    gap: 4px;
    white-space: nowrap;
  }

  .copy-btn:hover {
    background: var(--border);
    color: var(--text);
    border-color: var(--border-light);
  }

  .copy-btn:active { transform: scale(0.96); }

  .copy-btn.copied {
    background: var(--green-dim);
    border-color: var(--green);
    color: var(--green);
  }

  .copy-btn svg { width: 13px; height: 13px; }

  .translation-row.handled {
    background: rgba(248, 81, 73, 0.2);
    border-radius: 4px;
    padding: 2px 6px;
    margin: -2px -6px;
  }

  .rtl .translation-text { direction: rtl; text-align: right; }

  footer {
    margin-top: 24px;
    padding: 16px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 10px;
    font-size: 12px;
    color: var(--text-muted);
    line-height: 1.8;
  }

  footer strong { color: var(--text); font-weight: 600; }
  footer code {
    font-family: 'JetBrains Mono', monospace;
    background: var(--code-bg);
    padding: 1px 5px;
    border-radius: 3px;
    font-size: 11px;
  }

  .toast {
    position: fixed;
    bottom: 24px;
    right: 24px;
    background: var(--green-dim);
    border: 1px solid var(--green);
    color: var(--green);
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
    font-weight: 500;
    padding: 10px 18px;
    border-radius: 8px;
    opacity: 0;
    transform: translateY(10px);
    transition: all 0.25s ease;
    pointer-events: none;
    z-index: 100;
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .toast.show { opacity: 1; transform: translateY(0); }
</style>
</head>
<body>
<div class="container">
  <header>
    <h1>Translations for <code>{KEY_NAME}</code></h1>
    <p class="subtitle">23 languages · CLDR plural rules · Variable: <code style="font-family:'JetBrains Mono',monospace;background:var(--yellow-dim);color:var(--yellow);padding:1px 6px;border-radius:4px;font-size:13px">%{count}</code></p>
    <div class="legend">
      <div class="legend-item"><div class="legend-dot one"></div> one</div>
      <div class="legend-item"><div class="legend-dot other"></div> other</div>
      <div class="legend-item"><div class="legend-dot few"></div> few</div>
      <div class="legend-item"><div class="legend-dot many"></div> many</div>
      <div class="legend-item"><div class="legend-dot two"></div> two</div>
      <div class="legend-item"><div class="legend-dot zero"></div> zero</div>
    </div>
  </header>

  <table>
    <thead>
      <tr>
        <th>#</th>
        <th>Language</th>
        <th>Forms</th>
        <th>Translations</th>
      </tr>
    </thead>
    <tbody>
      <!-- LANGUAGE ROWS GO HERE (see Row Templates below) -->
    </tbody>
  </table>

  <footer>
    <strong>Notes:</strong><br>
    • These translations should be reviewed by native speakers before production use.<br>
    • Plural forms follow CLDR plural rules as configured in Lokalise.<br>
    • RTL languages (Arabic, Hebrew) are displayed right-to-left.
  </footer>
</div>

<div class="toast" id="toast">
  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
  <span id="toast-text">Copied!</span>
</div>

<script>
  const COPY_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"/></svg>';
  const CHECK_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" width="13" height="13"><polyline points="20 6 9 17 4 12"/></svg>';
  let toastTimeout;

  function copyText(btn) {
    const row = btn.closest('.translation-row');
    const textEl = row.querySelector('.translation-text');
    const text = textEl.getAttribute('data-copy');

    navigator.clipboard.writeText(text).then(() => {
      showFeedback(btn, text);
    }).catch(() => {
      const ta = document.createElement('textarea');
      ta.value = text;
      ta.style.cssText = 'position:fixed;opacity:0';
      document.body.appendChild(ta);
      ta.select();
      document.execCommand('copy');
      document.body.removeChild(ta);
      showFeedback(btn, text);
    });
  }

  function showFeedback(btn, text) {
    const row = btn.closest('.translation-row');
    row.classList.add('handled');

    btn.classList.add('copied');
    btn.innerHTML = CHECK_ICON + 'Copied!';
    setTimeout(() => {
      btn.classList.remove('copied');
      btn.innerHTML = COPY_ICON + 'Copy';
    }, 1500);

    const toast = document.getElementById('toast');
    const toastText = document.getElementById('toast-text');
    const display = text.length > 45 ? text.substring(0, 45) + '…' : text;
    toastText.textContent = 'Copied: ' + display;
    clearTimeout(toastTimeout);
    toast.classList.add('show');
    toastTimeout = setTimeout(() => toast.classList.remove('show'), 2000);
  }
</script>
</body>
</html>

Row Templates

Use these templates to build each language row. Replace {N}, {LANG_NAME}, {LANG_CODE}, and translation text.

The copy button HTML (reused everywhere):

<button class="copy-btn" onclick="copyText(this)"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"/></svg>Copy</button>

Single form (other only)

For: zh-CN, zh-TW, id, ja, km, ko, lo, ms, th, vi

<tr>
  <td><span class="lang-code">{N}</span></td>
  <td><span class="lang-name">{LANG_NAME}<span>{LANG_CODE}</span></span></td>
  <td><span class="form-tag other">other</span></td>
  <td class="translation-cell">
    <div class="translation-row">
      <span class="translation-text" data-copy="{PLAIN_TEXT}">{DISPLAY_HTML}</span>
      {COPY_BUTTON}
    </div>
  </td>
</tr>

Two forms (one / other)

For: en, nl, fr, de, he, hi, it, pt, es, tr

<tr>
  <td><span class="lang-code">{N}</span></td>
  <td><span class="lang-name">{LANG_NAME}<span>{LANG_CODE}</span></span></td>
  <td><span class="form-tag one">one</span> <span class="form-tag other">other</span></td>
  <td class="translation-cell">
    <div class="translation-row{RTL_CLASS}">
      <span class="form-tag one">one</span>
      <span class="translation-text" data-copy="{PLAIN_ONE}">{DISPLAY_ONE}</span>
      {COPY_BUTTON}
    </div>
    <div class="translation-row{RTL_CLASS}">
      <span class="form-tag other">other</span>
      <span class="translation-text" data-copy="{PLAIN_OTHER}">{DISPLAY_OTHER}</span>
      {COPY_BUTTON}
    </div>
  </td>
</tr>

Four forms (one / few / many / other)

For: ru

<tr>
  <td><span class="lang-code">{N}</span></td>
  <td><span class="lang-name">Russian<span>ru</span></span></td>
  <td><span class="form-tag one">one</span> <span class="form-tag few">few</span> <span class="form-tag many">many</span> <span class="form-tag other">other</span></td>
  <td class="translation-cell">
    <div class="translation-row">
      <span class="form-tag one">one</span>
      <span class="translation-text" data-copy="{PLAIN}">{DISPLAY}</span>
      {COPY_BUTTON}
    </div>
    <div class="translation-row">
      <span class="form-tag few">few</span>
      <span class="translation-text" data-copy="{PLAIN}">{DISPLAY}</span>
      {COPY_BUTTON}
    </div>
    <div class="translation-row">
      <span class="form-tag many">many</span>
      <span class="translation-text" data-copy="{PLAIN}">{DISPLAY}</span>
      {COPY_BUTTON}
    </div>
    <div class="translation-row">
      <span class="form-tag other">other</span>
      <span class="translation-text" data-copy="{PLAIN}">{DISPLAY}</span>
      {COPY_BUTTON}
    </div>
  </td>
</tr>

Six forms (zero / one / two / few / many / other)

For: ar, tl

<tr>
  <td><span class="lang-code">{N}</span></td>
  <td><span class="lang-name">{LANG_NAME}<span>{LANG_CODE}</span></span></td>
  <td><span class="form-tag zero">zero</span> <span class="form-tag one">one</span> <span class="form-tag two">two</span> <span class="form-tag few">few</span> <span class="form-tag many">many</span> <span class="form-tag other">other</span></td>
  <td class="translation-cell">
    <!-- One div.translation-row per form: zero, one, two, few, many, other -->
    <!-- Add " rtl" to class for Arabic: class="translation-row rtl" -->
    <div class="translation-row{RTL_CLASS}">
      <span class="form-tag zero">zero</span>
      <span class="translation-text" data-copy="{PLAIN}">{DISPLAY}</span>
      {COPY_BUTTON}
    </div>
    <!-- ... repeat for one, two, few, many, other -->
  </td>
</tr>

Display HTML Formatting

In the {DISPLAY} content, wrap any %{variable} tokens with the yellow highlight span:

Plain text (for data-copy): %{count} tables selected
Display HTML (for visible content): <span class="var">%{count}</span> tables selected
Markdown File

In addition to the HTML file, generate a companion Markdown file containing all translations in a table format.

File Location

Save the file to: {working_directory}/.tmp/translations-{sanitized_key}.md

(Same directory and naming as the HTML file, but with .md extension.)

Markdown Structure

The file MUST follow this exact structure:

# Translations: `{KEY_NAME}`

| # | Language | Code | Form | Translation |
|---|----------|------|------|-------------|
| 1 | English | en | one | %{count} table selected |
| 1 | English | en | other | %{count} tables selected |
| 2 | Arabic | ar | zero | ... |
| 2 | Arabic | ar | one | ... |
| 2 | Arabic | ar | two | ... |
| 2 | Arabic | ar | few | ... |
| 2 | Arabic | ar | many | ... |
| 2 | Arabic | ar | other | ... |
| 3 | Chinese (Simplified) | zh-CN | other | ... |
...


Rules:

Languages appear in the same order as the HTML (1-23)
Each plural form gets its own row
The # column uses the same row number for all forms of a language (e.g., all Arabic forms are 2)
The Translation column contains plain text (with %{...} variables preserved, no HTML markup)
For languages with a single form (other only), there is one row
For languages with multiple forms, each form gets a separate row in the order: zero, one, two, few, many, other (only the forms that apply to that language)
Checklist Before Saving
All 23 languages present in the exact order specified
Correct plural forms per language (not generic CLDR — use the Lokalise forms table above)
%{...} variables preserved exactly in all translations
data-copy attributes contain plain text (no HTML)
Display content has <span class="var"> around variables
RTL class applied to Arabic and Hebrew rows
Row numbers sequential 1-23
Copy buttons on every translation row
Both HTML and Markdown files saved to .tmp/ folder
HTML file opened in default browser after generation
Weekly Installs
67
Repository
morphet81/cheat-sheets
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass