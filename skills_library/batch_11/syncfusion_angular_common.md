---
title: syncfusion-angular-common
url: https://skills.sh/syncfusion/angular-ui-components-skills/syncfusion-angular-common
---

# syncfusion-angular-common

skills/syncfusion/angular-ui-components-skills/syncfusion-angular-common
syncfusion-angular-common
Installation
$ npx skills add https://github.com/syncfusion/angular-ui-components-skills --skill syncfusion-angular-common
SKILL.md
Common Features in Syncfusion Angular Components

Syncfusion Angular components include comprehensive common utilities and features that enhance user experience, ensure cross-cultural support, and provide foundational capabilities across all components. This skill covers installation setup, animations, globalization, state management, and security considerations for building robust Angular applications.

Table of Contents
Navigation Guide
Quick Start
Common Features
Documentation and Navigation Guide
Getting Started & Framework Setup

📄 Read: references/getting-started.md

Angular CLI installation and project creation
Standalone components vs. module-based configuration
npm package installation with ng add command
ASP.NET Core and ASP.NET MVC integration
Component initialization
Quick start examples
Globalization

📄 Read: references/globalization.md

Right-to-left (RTL) support for Arabic, Hebrew, Persian languages
Localization (l10n) for multi-language support
Internationalization (i18n) with CLDR data
Number and currency formatting
Date and time formatting
Advanced Features & Utilities

📄 Read: references/advanced-features.md

Animation effects (FadeIn, ZoomOut, SlideUp, etc.)
Animation timing (duration, delay, global settings)
Drag-and-drop interactions (Draggable, Droppable)
Template customization and optimization
State persistence with enablePersistence
Security best practices and HTML sanitization
Quick Start
Install Syncfusion Angular Package
ng add @syncfusion/ej2-angular-grids@latest


Note: The @syncfusion/ej2-base package is a dependency for all Syncfusion components and will be automatically installed when you install any Syncfusion Angular package. You don't need to explicitly add it to your package.json file.

Import Styles
@import "../node_modules/@syncfusion/ej2-base/styles/tailwind3.css";
@import "../node_modules/@syncfusion/ej2-buttons/styles/tailwind3.css";
@import "../node_modules/@syncfusion/ej2-calendars/styles/tailwind3.css";
@import "../node_modules/@syncfusion/ej2-dropdowns/styles/tailwind3.css";
@import "../node_modules/@syncfusion/ej2-inputs/styles/tailwind3.css";
@import "../node_modules/@syncfusion/ej2-navigations/styles/tailwind3.css";
@import "../node_modules/@syncfusion/ej2-popups/styles/tailwind3.css";
@import "../node_modules/@syncfusion/ej2-angular-grids/styles/tailwind3.css";

Register License Key

Step 1: Set the environment variable:

# Windows
setx SYNCFUSION_LICENSE "Your_License_Key_Here"

# Mac/Linux
export SYNCFUSION_LICENSE='Your_License_Key_Here'


Step 2: Activate the license using NPX command:

npx syncfusion-license activate


Note: For alternative license registration methods, kindly refer to the Syncfusion license key registration documentation.

Basic Component Setup
import { Component } from '@angular/core';
import { GridModule, PageService } from '@syncfusion/ej2-angular-grids';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [GridModule],
  providers: [PageService],
  template: `
    <ejs-grid [dataSource]="data" [allowPaging]="true">
      <e-columns>
        <e-column field="OrderID" width="100"></e-column>
        <e-column field="CustomerID" width="100"></e-column>
        <e-column field="Freight" width="100" format="C2"></e-column>
      </e-columns>
    </ejs-grid>
  `
})
export class AppComponent {
  data = [
    { OrderID: 10248, CustomerID: 'VINET', Freight: 32.38 },
    { OrderID: 10249, CustomerID: 'TOMSP', Freight: 11.61 }
  ];
}

Common Features
Enable State Persistence
<ejs-grid 
  id="persistGrid"
  [dataSource]="data" 
  [enablePersistence]="true"
>
  <!-- Component content -->
</ejs-grid>

Enable RTL Support
import { enableRtl } from '@syncfusion/ej2-base';

// Global RTL enablement
enableRtl(true);

// OR per-component
<ejs-grid [dataSource]="data" enableRtl="true"></ejs-grid>

Add Animation Effects
import { Component, ViewChild } from '@angular/core';
import { Animation } from '@syncfusion/ej2-base';

@Component({
  template: `<div #element class="box"></div>`
})
export class AnimationComponent {
  @ViewChild('element') element!: any;

  ngAfterViewInit() {
    const animation = new Animation({ duration: 5000, delay: 2000 });
    animation.animate(this.element.nativeElement, { name: 'FadeOut' });
  }
}

Implement Drag-and-Drop
import { Component, ViewChild } from '@angular/core';
import { Draggable, Droppable } from '@syncfusion/ej2-base';

@Component({
  template: `
    <div #draggable id="draggable">Drag me</div>
    <div #droppable id="droppable">Drop here</div>
  `
})
export class DragDropComponent {
  @ViewChild('draggable') draggable!: any;
  @ViewChild('droppable') droppable!: any;

  ngAfterViewInit() {
    new Draggable(this.draggable.nativeElement, { clone: false });
    
    new Droppable(this.droppable.nativeElement, {
      drop: (e) => {
        console.log('Dropped!', e.droppedElement);
      }
    });
  }
}

Weekly Installs
53
Repository
syncfusion/angu…s-skills
First Seen
Mar 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass