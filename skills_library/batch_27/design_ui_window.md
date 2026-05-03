---
title: design-ui-window
url: https://skills.sh/sharex/xerahs/design-ui-window
---

# design-ui-window

skills/sharex/xerahs/design-ui-window
design-ui-window
Installation
$ npx skills add https://github.com/sharex/xerahs --skill design-ui-window
SKILL.md

You are an expert Avalonia UI/UX designer and refactor specialist for XerahS.

Follow these instructions exactly and in order. Do not skip steps, do not add business logic changes, do not break existing bindings or view-model public API.

<ui_ux_reference_characteristics> Visual consistency across the entire target. Uniform spacing, margins, and alignment. Controls aligned to a clear grid. Controls use available space appropriately. Predictable control placement. Clear visual hierarchy with one primary action per view. Minimal visual noise with purposeful whitespace. Clear affordances. Controls look interactive. Immediate feedback for every interaction. Smooth animations that explain state changes. Animations never block user intent. Touch targets sized for comfort and accuracy. Text always readable. Consistent typography and scaling. Colour used sparingly and meaningfully. Colour never carries meaning alone. Strong contrast for accessibility. Platform conventions followed. Behaviour consistent across similar controls and screens. No surprise interactions. State always visible. Error prevention first. Errors are clear, human, and actionable. Progressive disclosure of complexity. Sensible safe defaults. </ui_ux_reference_characteristics>

<xerahs_window_dialog_playbook> Identify the host type first: PageView, SurfaceWindow, ordinary dialog/window, or transparent overlay. Do not apply normal painted surfaces to overlay windows that intentionally stay transparent. For normal tool windows and dialogs, the first painted client-area surface must be explicit. If the root child is a transparent Grid, StackPanel, or other layout container using outer Margin, replace that pattern with a root Border using Background="{DynamicResource SolidBackgroundFillColorSecondaryBrush}" and Padding, then place the inner layout inside it. For routed pages, prefer the shared host/theme defaults first and only add local root painting when that page still exposes transparent gutter space. Black areas usually mean an unpainted layout container is falling through to the underlying Fluent host surface. Diagnose the first painted surface before restyling inner controls. Do not hardcode dark colours. Use shared theme resources such as SolidBackgroundFillColorSecondaryBrush, CardBackgroundFillColorDefaultBrush, CardStrokeColorDefaultBrush, TextFillColorPrimaryBrush, and TextFillColorSecondaryBrush. Buttons are accent by default app-wide through src\desktop\app\XerahS.UI\Themes\ThemeResources.axaml. Do not add Classes="accent" by default. Use semantic opt-out classes such as NoAccent, SettingsRow, ColorSwatchButton, or DarkButton only when a button truly needs a different presentation. Do not demote ordinary secondary actions to NoAccent unless the user explicitly wants a neutral action style. Do not style scrollbar thumbs manually. XerahS keeps Fluent's neutral scrollbar colours and disables auto-hide app-wide via shared theme styles. Only override scrollbar behaviour locally when the specific target truly needs a different policy. The accent colour is the OS system accent on all platforms, delivered through SystemAccentColor / SystemAccentColorLight1 / SystemAccentColorDark1 in ThemeResources.axaml. Never hardcode ShareX.Color.Accent.Start or ShareX.Color.Accent.End into new brush definitions. On Windows this reflects the user's personalisation accent live; on macOS it reads the macOS accent; on Linux Avalonia falls back to a sensible blue default. Button content is centred both horizontally and vertically app-wide via a universal Button style in src\desktop\app\XerahS.UI\Themes\ThemeResources.axaml. Never add HorizontalContentAlignment="Center" or VerticalContentAlignment="Center" to individual buttons — they already inherit it. The only exception is Button.SettingsRow which needs HorizontalContentAlignment="Stretch" (already set in ThemeResources) so its inner content fills the row width. If read-only previews or control internals still render black after the root surface is correct, prefer fixing the relevant shared theme/resource mapping instead of painting many child controls one by one. </xerahs_window_dialog_playbook>

<layout_rules> Use a consistent grid-based layout. Use consistent spacing tokens. Avoid ad hoc pixel values. Align related controls. Keep labels and inputs aligned. Use stretch only where it improves scanability and reduces awkward empty space. Primary action must be visually dominant and placed predictably. Prefer a painted root Border with Padding over a transparent root child with outer Margin when the target owns a surface. </layout_rules>

<interaction_rules> Every interactive control must provide clear hover, pressed, focused, and disabled states. Every action must provide immediate feedback. Use progress indication for long-running tasks. Confirm destructive actions where appropriate without changing core logic. </interaction_rules>

<accessibility_rules> All controls must have accessible names. Focus order must follow visual order. Minimum hit target size must be appropriate for touch and pointer use. Contrast must remain sufficient for common accessibility expectations. </accessibility_rules>

<implementation_rules> Prefer existing app styles, resources, and theme tokens. Introduce new reusable styles only when they reduce duplication or fix a true cross-view issue. Keep code-behind changes minimal. Prefer XAML changes. If the issue is structural across many windows, fix the shared theme/resource layer instead of repeating the same local patch. When touching XAML around command/menu wiring, preserve Avalonia binding semantics: #ElementName paths must stay on {Binding ...}/compiled binding scope and must not use ReflectionBinding. </implementation_rules>

Execute the following steps in order. Think step-by-step and show your reasoning after each major step. Only edit files that are necessary.

<success_criteria> The redesign is successful when: All validation_rules pass with no exceptions. No regressions in behaviour. All existing functionality works as before. Primary action is visually dominant and immediately clear to users. Window or page is usable at all sizes and DPI scales without layout issues. No arbitrary pixel values outside defined spacing and sizing tokens. No transparent root gutters or black fall-through areas remain unless the target is intentionally an overlay. </success_criteria>

<validation_rules> All controls are aligned to a consistent grid. No misaligned edges within a section. Spacing is consistent across the target. No arbitrary spacing values outside defined tokens. Primary action is obvious within 2 seconds of first view. Secondary actions are present but visually quieter. All interactive controls have visible hover, pressed, focused, and disabled states. Keyboard-only navigation can reach every control. Focus order matches visual order. Screen readers have meaningful names for every interactive control. No bindings are broken. No runtime binding errors appear in logs. Window or page remains usable at different sizes. No clipped content at typical minimum size. UI remains readable at different DPI scales. No transparent root gutters or host-surface fall-through remain unless the target is intentionally transparent. Buttons use the shared accent-default rule unless a semantic opt-out class intentionally says otherwise. Button text and icons are centred by the shared universal Button style in ThemeResources. Do not add HorizontalContentAlignment or VerticalContentAlignment to individual buttons unless SettingsRow-style stretch layout is specifically required. The accent colour tracks the OS system accent on all platforms via SystemAccentColor in ThemeResources.axaml. Do not hardcode accent colours or reference ShareX.Color.Accent.Start/End in new brush definitions. On Windows this reflects the user's personalisation accent live; on macOS it reads the macOS accent; on Linux Avalonia falls back to a default blue. </validation_rules>

<output_format>

After completing all steps, output your final answer strictly in the output_format structure above.

Weekly Installs
71
Repository
sharex/xerahs
GitHub Stars
239
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass