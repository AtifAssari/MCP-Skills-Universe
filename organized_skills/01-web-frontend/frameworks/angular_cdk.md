---
rating: ⭐⭐
title: angular-cdk
url: https://skills.sh/oguzhan18/angular-ecosystem-skills/angular-cdk
---

# angular-cdk

skills/oguzhan18/angular-ecosystem-skills/angular-cdk
angular-cdk
Installation
$ npx skills add https://github.com/oguzhan18/angular-ecosystem-skills --skill angular-cdk
SKILL.md
@angular/cdk (Component Dev Kit)

Version: 21.0.3 (Feb 2026) Tags: Accessibility, Drag & Drop, Overlay, Virtual Scroll, Portal

References: Docs — official CDK documentation • GitHub • API

API Changes

This section documents recent version-specific API changes.

NEW: CDK overlays now use browser's built-in popovers for improved accessibility source

NEW: Angular 19 signal-based APIs — Modern signal integration for CDK components

NEW: Improved focus management — Better cdkTrapFocus and cdkFocusRegion support

NEW: Drag & Drop improvements — Enhanced item copying between lists

DEPRECATED: Legacy overlay strategies — Prefer scroll strategy configuration over deprecated approaches

Best Practices
Use CDK for custom UI components — Build your own components without Material styling
import { OverlayModule } from '@angular/cdk/overlay';
import { PortalModule } from '@angular/cdk/portal';

@Component({
  standalone: true,
  imports: [OverlayModule, PortalModule],
  // ...
})
export class CustomDropdownComponent {}

Use Overlay for floating panels — Tooltips, dropdowns, modals
import { OverlayRef, Overlay } from '@angular/cdk/overlay';

export class TooltipService {
  private overlayRef: OverlayRef;

  constructor(private overlay: Overlay) {
    this.overlayRef = this.overlay.create({
      hasBackdrop: true,
      positionStrategy: this.overlay.position()
        .connectedTo(origin, { originX: 'center', originY: 'bottom' })
        .withOffsetX(0)
        .withOffsetY(8)
    });
  }
}

Use Drag & Drop for sortable lists
import { CdkDragDrop, moveItemInArray, transferArrayItem } from '@angular/cdk/drag-drop';

drop(event: CdkDragDrop<string[]>) {
  if (event.previousContainer === event.container) {
    moveItemInArray(event.container.data, event.previousIndex, event.currentIndex);
  } else {
    transferArrayItem(
      event.previousContainer.data,
      event.container.data,
      event.previousIndex,
      event.currentIndex
    );
  }
}

Use Virtual Scroll for large lists
import { ScrollingModule } from '@angular/cdk/scrolling';

@Component({
  standalone: true,
  imports: [ScrollingModule],
  template: `
    <cdk-virtual-scroll-viewport itemSize="50" class="viewport">
      <div *cdkVirtualFor="let item of items">{{item.name}}</div>
    </cdk-virtual-scroll-viewport>
  `
})
export class ListComponent {}

Use Portal for dynamic content
import { DomPortalOutlet, TemplatePortal } from '@angular/cdk/portal';

@Component({ template: `<ng-template #dialogTemplate>Content</ng-template>` })
export class DialogComponent {
  @ViewChild('dialogTemplate') dialogTemplate!: TemplatePortal;

  attach() {
    const portalOutlet = new DomPortalOutlet(this.document.body);
    portalOutlet.attach(this.dialogTemplate);
  }
}

Use A11y utilities for accessibility
import { A11yModule, CdkTrapFocus, LiveAnnouncer } from '@angular/cdk/a11y';

@Component({
  standalone: true,
  imports: [A11yModule],
  template: `
    <div cdkTrapFocus>
      <button cdkFocusInitial>First</button>
      <button>Second</button>
    </div>
  `
})
export class AccessibleComponent {
  constructor(private liveAnnouncer: LiveAnnouncer) {
    this.liveAnnouncer.announce('Message for screen readers');
  }
}

Use Layout for responsive breakpoints
import { LayoutModule } from '@angular/cdk/layout';

@Component({
  standalone: true,
  imports: [LayoutModule],
  template: `
    <div *ngIf="isHandset$ | async">
      Mobile content
    </div>
  `
})
export class ResponsiveComponent {
  isHandset$ = this.breakpointObserver.observe('(max-width: 599px)');
}

Weekly Installs
124
Repository
oguzhan18/angul…m-skills
GitHub Stars
6
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass