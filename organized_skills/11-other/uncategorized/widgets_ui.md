---
rating: ⭐⭐⭐
title: widgets-ui
url: https://skills.sh/inference-sh/skills/widgets-ui
---

# widgets-ui

skills/inference-sh/skills/widgets-ui
widgets-ui
Installation
$ npx skills add https://github.com/inference-sh/skills --skill widgets-ui
SKILL.md
Widget Renderer

Declarative UI from JSON via ui.inference.sh.

Quick Start
npx shadcn@latest add https://ui.inference.sh/r/widgets.json

Basic Usage
import { WidgetRenderer } from "@/registry/blocks/widgets/widget-renderer"
import type { Widget, WidgetAction } from "@/registry/blocks/widgets/types"

const widget: Widget = {
  type: 'ui',
  title: 'My Widget',
  children: [
    { type: 'text', value: 'Hello World' },
    { type: 'button', label: 'Click me', onClickAction: { type: 'click' } },
  ],
}

<WidgetRenderer
  widget={widget}
  onAction={(action, formData) => console.log(action, formData)}
/>

Widget Types
Layout
{ "type": "row", "gap": 2, "children": [...] }
{ "type": "col", "gap": 2, "children": [...] }
{ "type": "box", "background": "gradient-ocean", "padding": 4, "radius": "lg", "children": [...] }

Typography
{ "type": "title", "value": "Heading", "size": "2xl", "weight": "bold" }
{ "type": "text", "value": "Body text", "variant": "bold" }
{ "type": "caption", "value": "Small text" }
{ "type": "label", "value": "Field label", "fieldName": "email" }

Interactive
{ "type": "button", "label": "Submit", "variant": "default", "onClickAction": { "type": "submit" } }
{ "type": "input", "name": "email", "placeholder": "Enter email" }
{ "type": "textarea", "name": "message", "placeholder": "Your message" }
{ "type": "select", "name": "plan", "options": [{ "value": "pro", "label": "Pro" }] }
{ "type": "checkbox", "name": "agree", "label": "I agree", "defaultChecked": false }

Display
{ "type": "badge", "label": "New", "variant": "secondary" }
{ "type": "icon", "iconName": "check", "size": "lg" }
{ "type": "image", "src": "https://...", "alt": "Image", "width": 100, "height": 100 }
{ "type": "divider" }

Example: Flight Card
const flightWidget: Widget = {
  type: 'ui',
  children: [
    {
      type: 'box', background: 'gradient-ocean', padding: 4, radius: 'lg', children: [
        {
          type: 'row', justify: 'between', children: [
            {
              type: 'col', gap: 1, children: [
                { type: 'caption', value: 'departure' },
                { type: 'title', value: 'SFO', size: '2xl', weight: 'bold' },
              ]
            },
            { type: 'icon', iconName: 'plane', size: 'lg' },
            {
              type: 'col', gap: 1, align: 'end', children: [
                { type: 'caption', value: 'arrival' },
                { type: 'title', value: 'JFK', size: '2xl', weight: 'bold' },
              ]
            },
          ]
        },
      ]
    },
  ],
}

Example: Form
const formWidget: Widget = {
  type: 'ui',
  title: 'Contact Form',
  asForm: true,
  children: [
    {
      type: 'col', gap: 3, children: [
        { type: 'input', name: 'name', placeholder: 'Your name' },
        { type: 'input', name: 'email', placeholder: 'Email address' },
        { type: 'textarea', name: 'message', placeholder: 'Message' },
        { type: 'button', label: 'Send', variant: 'default', onClickAction: { type: 'submit' } },
      ]
    },
  ],
}

Gradients
Name	Description
gradient-ocean	Blue teal gradient
gradient-sunset	Orange pink gradient
gradient-purple	Purple gradient
gradient-cool	Cool blue gradient
gradient-midnight	Dark blue gradient
Handling Actions
const handleAction = (action: WidgetAction, formData?: WidgetFormData) => {
  switch (action.type) {
    case 'submit':
      console.log('Form data:', formData)
      break
    case 'click':
      console.log('Button clicked')
      break
  }
}

Related Skills
# Full agent component
npx skills add inference-sh/skills@agent-ui

# Chat UI blocks
npx skills add inference-sh/skills@chat-ui

# Tool UI
npx skills add inference-sh/skills@tools-ui

Documentation
Widgets Overview - Understanding widgets
Widget Schema - Widget JSON structure
Agents That Generate UI - Building generative UIs

Component docs: ui.inference.sh/blocks/widgets

Weekly Installs
341
Repository
inference-sh/skills
GitHub Stars
395
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass