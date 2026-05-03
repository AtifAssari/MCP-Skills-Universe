---
rating: ⭐⭐
title: angular-lifecycle
url: https://skills.sh/oguzhan18/angular-ecosystem-skills/angular-lifecycle
---

# angular-lifecycle

skills/oguzhan18/angular-ecosystem-skills/angular-lifecycle
angular-lifecycle
Installation
$ npx skills add https://github.com/oguzhan18/angular-ecosystem-skills --skill angular-lifecycle
SKILL.md
Angular Lifecycle Hooks

Version: Angular 21 (2025) Tags: Lifecycle, Hooks, ngOnInit, ngOnChanges

References: Lifecycle Hooks • API

Best Practices
Use OnInit for initialization
import { OnInit } from '@angular/core';

@Component({})
export class MyComponent implements OnInit {
  ngOnInit() {
    // Initialize data, call services
    this.loadData();
  }
}

Use OnDestroy for cleanup
import { OnDestroy } from '@angular/core';

@Component({})
export class MyComponent implements OnDestroy {
  private destroy$ = new Subject<void>();
  
  ngOnDestroy() {
    this.destroy$.next();
    this.destroy$.complete();
  }
}

Use OnChanges for input changes
import { OnChanges, SimpleChanges } from '@angular/core';

@Component({})
export class MyComponent implements OnChanges {
  @Input() data: any;
  
  ngOnChanges(changes: SimpleChanges) {
    if (changes['data']) {
      console.log('Data changed:', this.data);
    }
  }
}

Use AfterViewInit for DOM manipulation
import { AfterViewInit, ViewChild, ElementRef } from '@angular/core';

@Component({})
export class MyComponent implements AfterViewInit {
  @ViewChild('el') el!: ElementRef;
  
  ngAfterViewInit() {
    this.el.nativeElement.focus();
  }
}

Use AfterContentInit for projected content
import { AfterContentInit, ContentChild } from '@angular/core';

@Component({})
export class MyComponent implements AfterContentInit {
  @ContentChild('header') header!: ElementRef;
  
  ngAfterContentInit() {
    // Access projected content
  }
}

Use DoCheck for custom change detection
import { DoCheck } from '@angular/core';

@Component({})
export class MyComponent implements DoCheck {
  ngDoCheck() {
    // Custom change detection
  }
}

Use OnPush with lifecycle
@Component({
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class MyComponent {
  @Input() data: any;
  
  ngOnChanges(changes: SimpleChanges) {
    // OnPush needs explicit change detection trigger
  }
}

Use constructor vs ngOnInit
// Constructor - for dependency injection only
constructor(private service: MyService) {}

// ngOnInit - for initialization logic
ngOnInit() {
  this.data = this.service.getData();
}

Weekly Installs
122
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