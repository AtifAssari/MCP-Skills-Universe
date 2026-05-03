---
rating: ⭐⭐
title: angular-components
url: https://skills.sh/oguzhan18/angular-ecosystem-skills/angular-components
---

# angular-components

skills/oguzhan18/angular-ecosystem-skills/angular-components
angular-components
Installation
$ npx skills add https://github.com/oguzhan18/angular-ecosystem-skills --skill angular-components
SKILL.md
Angular Components

Version: Angular 21 (2025) Tags: Components, @Component, Architecture

References: Components Guide • @Component API

Best Practices
Create standalone component
@Component({
  standalone: true,
  selector: 'app-my',
  imports: [CommonModule],
  template: `<p>Content</p>`
})
export class MyComponent {}

Use inputs with signals
@Component({})
export class MyComponent {
  data = input<string>('');
  required = input.required<User>();
  
  computed = computed(() => this.data()?.name);
}

Use outputs for events
@Component({})
export class MyComponent {
  data = output<string>();
  
  onClick() {
    this.data.emit('event');
  }
}

Use template reference variables
@Component({
  template: `
    <input #nameInput>
    <button (click)="onSubmit(nameInput.value)">Submit</button>
  `
})
export class MyComponent {}

Use content projection
@Component({
  selector: 'app-card',
  template: `
    <div class="header">
      <ng-content select="[header]"></ng-content>
    </div>
    <div class="body">
      <ng-content></ng-content>
    </div>
  `
})
export class CardComponent {}

Use change detection strategy
@Component({
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class OptimizedComponent {}

Use encapsulation
@Component({
  encapsulation: ViewEncapsulation.None // or Emulated, ShadowDom
})
export class StyledComponent {}

Use host binding
@Component({
  host: {
    '[class.active]': 'isActive',
    '(click)': 'onClick()'
  }
})
export class HostComponent {
  isActive = false;
}

Weekly Installs
122
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