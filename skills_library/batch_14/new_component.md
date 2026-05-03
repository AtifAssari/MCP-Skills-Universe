---
title: new-component
url: https://skills.sh/longbridge/gpui-component/new-component
---

# new-component

skills/longbridge/gpui-component/new-component
new-component
Installation
$ npx skills add https://github.com/longbridge/gpui-component --skill new-component
SKILL.md
Instructions

When creating new GPUI components:

Follow existing patterns: Base implementation on components in crates/ui/src (examples: Button, Select, Dialog)
Style consistency: Follow existing component styles and Shadcn UI patterns
Component type decision:
Use stateless elements for simple components (like Button)
Use stateful elements for complex components with data (like Select and SelectState)
Use composition for components built on existing components (like AlertDialog based on Dialog)
API consistency: Maintain the same API style as other elements
Documentation: Create component documentation
Stories: Write component stories in the story folder
Registration: Add the component to crates/story/src/main.rs story list
Component Types
Stateless: Pure presentation components without internal state (e.g., Button)
Stateful: Components that manage their own state and data (e.g., Select)
Composite: Components built on top of existing components (e.g., AlertDialog based on Dialog)
Implementation Steps
1. Create Component File

Create a new file in crates/ui/src/ (e.g., alert_dialog.rs):

use gpui::{App, ClickEvent, Pixels, SharedString, Window, px};
use std::rc::Rc;

pub struct AlertDialog {
    pub(crate) variant: AlertVariant,
    pub(crate) title: SharedString,
    // ... other fields
}

impl AlertDialog {
    pub fn new(title: impl Into<SharedString>) -> Self {
        // implementation
    }

    // Builder methods
    pub fn description(mut self, desc: impl Into<SharedString>) -> Self {
        // implementation
    }
}

2. Register in lib.rs

Add the module to crates/ui/src/lib.rs:

pub mod alert_dialog;

3. Extend WindowExt (if needed)

For dialog-like components, add helper methods to window_ext.rs:

pub trait WindowExt {
    fn open_alert_dialog(&mut self, alert: AlertDialog, cx: &mut App);
}

4. Create Story

Create crates/story/src/stories/alert_dialog_story.rs:

pub struct AlertDialogStory {
    focus_handle: FocusHandle,
}

impl Story for AlertDialogStory {
    fn title() -> &'static str {
        "AlertDialog"
    }

    fn new_view(window: &mut Window, cx: &mut App) -> Entity<impl Render> {
        Self::view(window, cx)
    }
}

5. Register Story

Add to crates/story/src/stories/mod.rs:

mod alert_dialog_story;
pub use alert_dialog_story::AlertDialogStory;


Add to crates/story/src/main.rs in the stories list:

vec![
    StoryContainer::panel::<AlertStory>(window, cx),
    StoryContainer::panel::<AlertDialogStory>(window, cx),  // Add here
    // ...
]

Real Example: AlertDialog

AlertDialog is a composite component based on Dialog with these features:

Simpler API: Pre-configured for common alert scenarios
Center-aligned layout: All content (icon, title, description, buttons) is center-aligned
Vertical layout: Icon appears at the top, followed by title and description
Auto icons: Automatically shows icons based on variant (Info, Success, Warning, Error)
Convenience constructors: AlertDialog::info(), AlertDialog::warning(), etc.

Key Design Decisions:

description uses SharedString instead of AnyElement because the Dialog builder needs to be Fn (callable multiple times), and AnyElement cannot be cloned
Implementation is in window_ext.rs using Dialog as the base, not as a separate IntoElement component
Center-aligned layout: Icon is positioned at the top (not left), all text is center-aligned for a more focused alert appearance
Footer center-aligned: Buttons are centered, different from Dialog's default right-aligned footer

Usage:

window.open_alert_dialog(
    AlertDialog::warning("Unsaved Changes")
        .description("You have unsaved changes.")
        .show_cancel(true)
        .on_confirm(|_, window, cx| {
            window.push_notification("Confirmed", cx);
            true
        }),
    cx,
);

Common Patterns
Builder Pattern

All components use the builder pattern for configuration:

AlertDialog::new("Title")
    .description("Description")
    .width(px(500.))
    .on_confirm(|_, _, _| true)

Size Variants

Implement Sizable trait for components that support size variants (xs, sm, md, lg).

Variants

Use enums for visual variants (e.g., AlertVariant::Info, ButtonVariant::Primary).

Styled Trait Implementation

Components that render as a single container element should implement Styled to allow callers to customize styles. The pattern uses a StyleRefinement field and refine_style() from StyledExt:

use gpui::{AnyElement, App, IntoElement, ParentElement, RenderOnce, StyleRefinement, Styled, Window, div};
use crate::StyledExt as _;

#[derive(IntoElement)]
pub struct MyComponent {
    style: StyleRefinement,
    children: Vec<AnyElement>,
}

impl MyComponent {
    pub fn new() -> Self {
        Self {
            style: StyleRefinement::default(),
            children: Vec::new(),
        }
    }
}

impl ParentElement for MyComponent {
    fn extend(&mut self, elements: impl IntoIterator<Item = AnyElement>) {
        self.children.extend(elements);
    }
}

impl Styled for MyComponent {
    fn style(&mut self) -> &mut StyleRefinement {
        &mut self.style
    }
}

impl RenderOnce for MyComponent {
    fn render(self, _: &mut Window, _: &mut App) -> impl IntoElement {
        div()
            // ... component's default styles ...
            .refine_style(&self.style)  // Apply user's style overrides
            .children(self.children)
    }
}


Key points:

Add style: StyleRefinement field initialized with StyleRefinement::default()
Implement Styled trait returning &mut self.style
In render(), call .refine_style(&self.style) on the root div to merge user styles
Place .refine_style() after component defaults but before .children() so user styles override defaults
Reference: crates/ui/src/dialog/header.rs (DialogHeader), crates/ui/src/table/table.rs (Table and sub-components)
Callbacks

Use Rc<dyn Fn> for callbacks that may be called multiple times:

on_confirm: Option<Rc<dyn Fn(&ClickEvent, &mut Window, &mut App) -> bool + 'static>>

Weekly Installs
178
Repository
longbridge/gpui…omponent
GitHub Stars
11.3K
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass