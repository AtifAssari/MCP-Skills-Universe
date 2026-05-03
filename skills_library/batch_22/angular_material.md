---
title: angular-material
url: https://skills.sh/oguzhan18/angular-ecosystem-skills/angular-material
---

# angular-material

skills/oguzhan18/angular-ecosystem-skills/angular-material
angular-material
Installation
$ npx skills add https://github.com/oguzhan18/angular-ecosystem-skills --skill angular-material
SKILL.md
@angular/material & @angular/cdk

Version: 21.0.3 (Feb 2026) Tags: Material Design, CDK, Components, UI Library

References: Docs — components, guides • CDK Docs • GitHub Issues • Changelog

API Changes

This section documents recent version-specific API changes.

NEW: Angular Aria — New low-level component library for accessible, headless components that can be styled custom source

NEW: CDK overlays now use browser's built-in popovers for improved accessibility source

NEW: Material Design system tokens — Use utility classes to apply Material tokens directly in templates source

NEW: CDK Drag & Drop improvements — Allow copying items between lists source

NEW: Angular v21 — Full support for new Angular features including zoneless change detection

Best Practices
Use standalone components — Import Material components directly without NgModule
import { Component } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';

@Component({
  standalone: true,
  imports: [MatButtonModule, MatCardModule],
  // ...
})
export class ExampleComponent {}


Use CDK for custom components — Use CDK (Component Dev Kit) for behavior primitives like drag-drop, overlays, menus without Material styling

Use CDK Virtual Scroll for large lists — Improve performance with cdkVirtualScrollViewport instead of rendering all items

<cdk-virtual-scroll-viewport itemSize="50" class="viewport">
  <div *cdkVirtualFor="let item of items">{{item.name}}</div>
</cdk-virtual-scroll-viewport>


Use trackBy with ngFor — Prevent unnecessary DOM re-renders

Customize themes with SCSS — Use Material's theming system for custom colors and typography

Use ChangeDetectionStrategy.OnPush — Improve performance with default change detection strategy

Follow accessibility guidelines — Use ARIA labels, keyboard navigation, and focus management provided by CDK components

Weekly Installs
129
Repository
oguzhan18/angul…m-skills
GitHub Stars
6
First Seen
11 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass