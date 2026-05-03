---
title: form-filling
url: https://skills.sh/site/cbskills.xcloudzen.com/form-filling
---

# form-filling

skills/cbskills.xcloudzen.com/form-filling
form-filling
$ npx skills add https://cbskills.xcloudzen.com
SKILL.md
Form Filling — Detect, Fill, Submit, Verify

Works on login forms, contact forms, registration, checkout, search, multi-step wizards. Read chrome-bridge first.

Workflow
Discover — enumerate fields
Build selector strategy — pick the most stable handle per field
Fill — dom_fill for plain inputs, dom_type for rich editors, execute_script for everything else
Verify — read back the values before submitting
Submit — click the submit button (or fallback to form.submit())
Confirm — check URL change or success message after submit
Reusable scripts

Each capability has a focused JS file under scripts/. To use one:

Read the script file to load it as a string.
Pass the contents as the code argument to mcp__chrome-bridge__execute_script.
Many scripts have selector / value placeholders embedded — edit before passing.
Task	When	Script	Notes
Discover all forms + fields	Step 1	scripts/discover_fields.js	Returns every form with field types, names, ids, placeholders, labels, required flags, select options, submit text.
Verify values before submit	Step 4	scripts/form_values_dump.js	Reads back values from the first form on the page.
Set a radio button	Step 3	scripts/radio_set.js	Edit the name/value selector inline.
Toggle a checkbox	Step 3	scripts/checkbox_set.js	Edit the name selector inline. Uses .click() to fire full event chain.
Set a <input type="date">	Step 3	scripts/date_input_set.js	Edit the YYYY-MM-DD value inline. Native-setter pattern for React/Vue/Angular.
Native-setter text fill (React/Vue rescue)	Step 3	scripts/native_setter_input.js	Use when dom_fill sets the value but validation still fails or submit stays disabled.
CAPTCHA detection	Anywhere	scripts/captcha_detect.js	If detected, STOP. Never try to solve programmatically.
Step 1: Discover fields
execute_script(code=<contents of scripts/discover_fields.js>)

Step 2: Pick selectors

Priority order when choosing a handle per field:

#id — most reliable if the field has an id
[name="fieldname"] — reliable for named fields
[type="email"], [type="tel"], [type="password"] — reliable for typed inputs when the form has one per type
[placeholder="..."] — fallback for unnamed fields
[aria-label="..."] — accessible forms
Positional (form:nth-of-type(1) input:nth-of-type(2)) — last resort
Step 3: Fill
Plain inputs, textareas, selects
dom_fill('#email', 'user@example.com')
dom_fill('[name="password"]', 'hunter2')
dom_fill('textarea[name="message"]', 'Hello...')
dom_fill('select[name="country"]', 'MY')   # matches by value

Rich text editors (ProseMirror, TipTap, Draft.js, contentEditable)
dom_type('[role="textbox"][aria-label*="comment" i]', 'Thanks for sharing!')


dom_fill silently fails on these editors. They listen to real keystroke events, not .value assignment or input events. dom_type simulates actual CDP Input.dispatchKeyEvent — it's the only thing that works on LinkedIn, Threads, Notion, Slack, and most comment boxes on modern sites.

Radio buttons
# Edit name+value in scripts/radio_set.js, then:
execute_script(code=<contents of scripts/radio_set.js>)

Checkboxes
# Edit name in scripts/checkbox_set.js, then:
execute_script(code=<contents of scripts/checkbox_set.js>)

Date pickers (native <input type="date">)
# Edit value in scripts/date_input_set.js, then:
execute_script(code=<contents of scripts/date_input_set.js>)

Autocomplete fields
# Type character-by-character to trigger the suggestion list:
dom_type('input[name="location"]', 'Kuala Lumpur')
# Wait 1-2s for suggestions, then click the one you want:
dom_click('[role="option"]:first-child')

Step 4: Verify before submit
execute_script(code=<contents of scripts/form_values_dump.js>)

Step 5: Submit
dom_click('button[type="submit"]')


If there's no submit button or click does nothing:

execute_script(code="(function(){ document.forms[0].submit(); return 'submitted'; })()")

Step 6: Confirm
# wait 3s for the response
execute_script(code="(()=>location.href)()")  # did we redirect to a success page?
page_text()                                    # is there a "Thank you" / "Success" / error message?

React/Vue framework edge case

If dom_fill appears to work (value is set) but form validation still fails or the submit button stays disabled, the framework state didn't update. Use the native setter pattern:

# Edit selector + value in scripts/native_setter_input.js, then:
execute_script(code=<contents of scripts/native_setter_input.js>)

Multi-step wizards
# 1. Detect current step
execute_script(code="(function(){ return document.querySelector('.wizard-step.active')?.dataset.step || '?'; })()")
# 2. Fill this step's fields (discover → fill → verify)
# 3. Click Next
dom_click('button.next')   # or use execute_script to match by innerText if class varies
# 4. Wait for the next step to render, then repeat until you hit the final submit

CAPTCHA handling
execute_script(code=<contents of scripts/captcha_detect.js>)


If present, stop and tell the user to solve it manually. Never try to solve CAPTCHAs programmatically.

Common failures
Signal	Cause	Fix
dom_fill sets value but form fails validation	React/Vue state not updated	Use scripts/native_setter_input.js
Rich-text comment editor stays empty	.value assignment ignored	Use dom_type
Submit button stays disabled	Required field missed, or events didn't fire	Re-run scripts/discover_fields.js; ensure every input/change dispatched
dom_click on button[type="submit"] fails	Attribute selector escaping quirk	Use a narrower parent, or execute_script to click by innerText
Submit redirects to login	Session expired mid-flow	Ask the user to re-authenticate; don't try to auto-login
Checkbox "checked" but form ignores it	Bare .checked = true doesn't fire events on some frameworks	Use scripts/checkbox_set.js (.click() fires the full event chain)
Weekly Installs
9
Source
cbskills.xcloudzen.com
First Seen
8 days ago