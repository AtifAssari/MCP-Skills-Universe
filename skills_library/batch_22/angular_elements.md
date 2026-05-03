---
title: angular-elements
url: https://skills.sh/oguzhan18/angular-ecosystem-skills/angular-elements
---

# angular-elements

skills/oguzhan18/angular-ecosystem-skills/angular-elements
angular-elements
Installation
$ npx skills add https://github.com/oguzhan18/angular-ecosystem-skills --skill angular-elements
SKILL.md
@angular/elements

Version: Angular 21 (2025) Tags: Web Components, Custom Elements, Micro-frontends

References: Elements Guide • API

API Changes

This section documents recent version-specific API changes.

NEW: createCustomElement API — Package Angular components as custom elements

NEW: NgElementConfig — Configure custom element behavior

NEW: Input/Output mapping — Map Angular inputs/outputs to web component attributes

NEW: Standalone elements — Build standalone elements without NgModule

Best Practices
Install @angular/elements
npm install @angular/elements

Create custom element from component
import { createCustomElement } from '@angular/elements';

@Injectable()
export class ElementRegistrar {
  constructor(private injector: Injector) {}

  register() {
    const element = createCustomElement(MyComponent, { injector: this.injector });
    customElements.define('my-element', element);
  }
}

Use in main.ts
import { createApplication } from '@angular/platform-browser';
import { createCustomElement } from '@angular/elements';

bootstrapApplication(AppComponent).then(appRef => {
  const element = createCustomElement(MyComponent, { injector: appRef.injector });
  customElements.define('my-component', element);
});

Map inputs and outputs
const element = createCustomElement(MyComponent, {
  injector: this.injector,
  events: ['myEvent'],
  attributes: ['myInput']
});

Use CUSTOM_ELEMENTS_SCHEMA
// To use custom elements in Angular
import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';

@NgModule({
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class AppModule {}

Build as web component
// angular.json
{
  "build": {
    "options": {
      "outputPath": "dist",
      "singleBundle": true
    }
  }
}

Use input() and output() for web component data
@Component({
  selector: 'my-element',
  standalone: true
})
export class MyElementComponent {
  data = input<string>('');
  output = output<string>();

  onClick() {
    this.output.emit('event-data');
  }
}

Handle content projection
@Component({
  selector: 'my-element',
  template: `
    <div class="header">
      <ng-content select="[header]"></ng-content>
    </div>
    <div class="body">
      <ng-content></ng-content>
    </div>
  `
})
export class MyElementComponent {}

Use for micro-frontends
// Register multiple elements
const elements = [ButtonComponent, CardComponent, InputComponent];
elements.forEach(comp => {
  const el = createCustomElement(comp, { injector });
  customElements.define(comp.selector, el);
});

Weekly Installs
121
Repository
oguzhan18/angul…m-skills
GitHub Stars
6
First Seen
6 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass