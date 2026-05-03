---
title: frontend-design
url: https://skills.sh/stuartf303/sorcha/frontend-design
---

# frontend-design

skills/stuartf303/sorcha/frontend-design
frontend-design
Installation
$ npx skills add https://github.com/stuartf303/sorcha --skill frontend-design
SKILL.md
Frontend-design Skill

Sorcha uses MudBlazor 8.15.0 for Material Design components with CSS Isolation as the primary styling approach. The design system follows Material Design 3 with custom extensions for blockchain/workflow visualization.

Quick Start
Styling a New Component
@* MyComponent.razor *@
<MudPaper Elevation="1" Class="pa-4 mb-3">
    <MudText Typo="Typo.h6" Class="mb-2">Component Title</MudText>
    <MudText Typo="Typo.body2" Color="Color.Secondary">
        Description text
    </MudText>
</MudPaper>

Custom Component with CSS Isolation
@* MyCard.razor *@
<div class="custom-card @(IsSelected ? "selected" : "")">
    <div class="card-header">@Title</div>
    <div class="card-content">@ChildContent</div>
</div>

@code {
    [Parameter] public string Title { get; set; } = "";
    [Parameter] public RenderFragment? ChildContent { get; set; }
    [Parameter] public bool IsSelected { get; set; }
}

/* MyCard.razor.css */
.custom-card {
    background: white;
    border: 2px solid #1976d2;
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.12);
    transition: all 0.2s ease;
}

.custom-card:hover {
    box-shadow: 0 4px 12px rgba(0,0,0,0.18);
    transform: translateY(-2px);
}

.custom-card.selected {
    border-color: #0d47a1;
    border-width: 3px;
}

Key Concepts
Concept	Usage	Example
CSS Isolation	Component-scoped styles	Component.razor.css
MudBlazor Utility	Spacing, flex, alignment	Class="d-flex pa-4 mb-3"
Color System	Semantic colors	Color.Primary, Color.Error
Typography	Text hierarchy	Typo.h6, Typo.body2
Elevation	Shadow depth	Elevation="1" (0-24)
Breakpoint	Responsive	Breakpoint.Sm (641px)
Common Patterns
Flex Layout with Gap
<div class="d-flex align-center gap-2 mb-3">
    <MudIcon Icon="@Icons.Material.Filled.Settings" />
    <MudText Typo="Typo.body1">Settings</MudText>
    <MudSpacer />
    <MudChip T="string" Size="Size.Small" Color="Color.Info">Active</MudChip>
</div>

Panel with Header/Content Pattern
<MudPaper Elevation="1" Class="panel">
    <div class="panel-header">
        <MudText Typo="Typo.subtitle1">Panel Title</MudText>
    </div>
    <div class="panel-content">
        @* Content here *@
    </div>
</MudPaper>

See Also
aesthetics - Color system, typography, brand identity
components - MudBlazor component patterns
layouts - Page structure, responsive grids
motion - Transitions, hover effects
patterns - DO/DON'T design decisions
Related Skills
See the blazor skill for component lifecycle and state management
See the signalr skill for real-time UI updates
Weekly Installs
25
Repository
stuartf303/sorcha
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass