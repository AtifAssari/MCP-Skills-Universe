---
rating: ⭐⭐
title: gpui-focus-handle
url: https://skills.sh/longbridge/gpui-component/gpui-focus-handle
---

# gpui-focus-handle

skills/longbridge/gpui-component/gpui-focus-handle
gpui-focus-handle
Installation
$ npx skills add https://github.com/longbridge/gpui-component --skill gpui-focus-handle
SKILL.md
Overview

GPUI's focus system enables keyboard navigation and focus management.

Key Concepts:

FocusHandle: Reference to focusable element
Focus tracking: Current focused element
Keyboard navigation: Tab/Shift-Tab between elements
Focus events: on_focus, on_blur
Quick Start
Creating Focus Handles
struct FocusableComponent {
    focus_handle: FocusHandle,
}

impl FocusableComponent {
    fn new(cx: &mut Context<Self>) -> Self {
        Self {
            focus_handle: cx.focus_handle(),
        }
    }
}

Making Elements Focusable
impl Render for FocusableComponent {
    fn render(&mut self, _: &mut Window, cx: &mut Context<Self>) -> impl IntoElement {
        div()
            .track_focus(&self.focus_handle)
            .on_action(cx.listener(Self::on_enter))
            .child("Focusable content")
    }

    fn on_enter(&mut self, _: &Enter, cx: &mut Context<Self>) {
        // Handle Enter key when focused
        cx.notify();
    }
}

Focus Management
impl MyComponent {
    fn focus(&mut self, cx: &mut Context<Self>) {
        self.focus_handle.focus(cx);
    }

    fn is_focused(&self, cx: &App) -> bool {
        self.focus_handle.is_focused(cx)
    }

    fn blur(&mut self, cx: &mut Context<Self>) {
        cx.blur();
    }
}

Focus Events
Handling Focus Changes
impl Render for MyInput {
    fn render(&mut self, _: &mut Window, cx: &mut Context<Self>) -> impl IntoElement {
        let is_focused = self.focus_handle.is_focused(cx);

        div()
            .track_focus(&self.focus_handle)
            .on_focus(cx.listener(|this, _event, cx| {
                this.on_focus(cx);
            }))
            .on_blur(cx.listener(|this, _event, cx| {
                this.on_blur(cx);
            }))
            .when(is_focused, |el| {
                el.bg(cx.theme().focused_background)
            })
            .child(self.render_content())
    }
}

impl MyInput {
    fn on_focus(&mut self, cx: &mut Context<Self>) {
        // Handle focus gained
        cx.notify();
    }

    fn on_blur(&mut self, cx: &mut Context<Self>) {
        // Handle focus lost
        cx.notify();
    }
}

Keyboard Navigation
Tab Order

Elements with track_focus() automatically participate in Tab navigation.

div()
    .child(
        input1.track_focus(&focus1)  // Tab order: 1
    )
    .child(
        input2.track_focus(&focus2)  // Tab order: 2
    )
    .child(
        input3.track_focus(&focus3)  // Tab order: 3
    )

Focus Within Containers
impl Container {
    fn focus_first(&mut self, cx: &mut Context<Self>) {
        if let Some(first) = self.children.first() {
            first.update(cx, |child, cx| {
                child.focus_handle.focus(cx);
            });
        }
    }

    fn focus_next(&mut self, cx: &mut Context<Self>) {
        // Custom focus navigation logic
    }
}

Common Patterns
1. Auto-focus on Mount
impl MyDialog {
    fn new(cx: &mut Context<Self>) -> Self {
        let focus_handle = cx.focus_handle();

        // Focus when created
        focus_handle.focus(cx);

        Self { focus_handle }
    }
}

2. Focus Trap (Modal)
impl Modal {
    fn render(&mut self, _: &mut Window, cx: &mut Context<Self>) -> impl IntoElement {
        div()
            .track_focus(&self.focus_handle)
            .on_key_down(cx.listener(|this, event: &KeyDownEvent, cx| {
                if event.key == Key::Tab {
                    // Keep focus within modal
                    this.focus_next_in_modal(cx);
                    cx.stop_propagation();
                }
            }))
            .child(self.render_content())
    }
}

3. Conditional Focus
impl Searchable {
    fn render(&mut self, _: &mut Window, cx: &mut Context<Self>) -> impl IntoElement {
        div()
            .track_focus(&self.focus_handle)
            .when(self.search_active, |el| {
                el.on_mount(cx.listener(|this, _, cx| {
                    this.focus_handle.focus(cx);
                }))
            })
            .child(self.search_input())
    }
}

Best Practices
✅ Track Focus on Interactive Elements
// ✅ Good: Track focus for keyboard interaction
input()
    .track_focus(&self.focus_handle)
    .on_action(cx.listener(Self::on_enter))

✅ Provide Visual Focus Indicators
let is_focused = self.focus_handle.is_focused(cx);

div()
    .when(is_focused, |el| {
        el.border_color(cx.theme().focused_border)
    })

❌ Don't: Forget to Track Focus
// ❌ Bad: No track_focus, keyboard navigation won't work
div()
    .on_action(cx.listener(Self::on_enter))

Reference Documentation
API Reference: See api-reference.md
FocusHandle API, focus management
Events, keyboard navigation
Best practices
Weekly Installs
206
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