---
rating: ⭐⭐
title: angular-viewchild
url: https://skills.sh/oguzhan18/angular-ecosystem-skills/angular-viewchild
---

# angular-viewchild

skills/oguzhan18/angular-ecosystem-skills/angular-viewchild
angular-viewchild
Installation
$ npx skills add https://github.com/oguzhan18/angular-ecosystem-skills --skill angular-viewchild
SKILL.md
Angular ViewChild / ContentChild

Version: Angular 21 (2025) Tags: ViewChild, ContentChild, DOM, Queries

References: ViewChild API • ContentChild API

Best Practices
Use ViewChild for element reference
import { ViewChild, ElementRef, AfterViewInit } from '@angular/core';

@Component({})
export class MyComponent implements AfterViewInit {
  @ViewChild('input') inputEl!: ElementRef<HTMLInputElement>;
  
  ngAfterViewInit() {
    this.inputEl.nativeElement.focus();
  }
}

Use static option
// Static - available in ngOnInit
@ViewChild('static', { static: true }) staticEl!: ElementRef;

// Dynamic - available in ngAfterViewInit
@ViewChild('dynamic', { static: false }) dynamicEl!: ElementRef;

Use ContentChild for projected content
import { ContentChild, TemplateRef } from '@angular/core';

@Component({
  selector: 'app-card',
  template: `
    <div class="card">
      <ng-content></ng-content>
    </div>
  `
})
export class CardComponent {
  @ContentChild(TemplateRef) headerTemplate!: TemplateRef<any>;
}

Use ViewChildren for multiple elements
import { ViewChildren, QueryList } from '@angular/core';

@Component({})
export class ListComponent {
  @ViewChildren('item') items!: QueryList<ElementRef>;
  
  ngAfterViewInit() {
    this.items.forEach(item => console.log(item));
  }
}

Use read option
@ViewChild('component', { read: ViewContainerRef }) container!: ViewContainerRef;

@ViewChild('template', { read: TemplateRef }) template!: TemplateRef<any>;

Access component instance
@ViewChild(ChildComponent) child!: ChildComponent;

ngAfterViewInit() {
  this.child.doSomething();
}

Use with signals
@ViewChild('el') el!: ElementRef<HTMLElement>;

ngAfterViewInit() {
  effect(() => {
    if (this.shouldFocus()) {
      this.el.nativeElement.focus();
    }
  });
}

Weekly Installs
121
Repository
oguzhan18/angul…m-skills
GitHub Stars
6
First Seen
7 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass