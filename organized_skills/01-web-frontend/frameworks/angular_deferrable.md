---
rating: ⭐⭐
title: angular-deferrable
url: https://skills.sh/oguzhan18/angular-ecosystem-skills/angular-deferrable
---

# angular-deferrable

skills/oguzhan18/angular-ecosystem-skills/angular-deferrable
angular-deferrable
Installation
$ npx skills add https://github.com/oguzhan18/angular-ecosystem-skills --skill angular-deferrable
SKILL.md
Angular Deferrable Views

Version: Angular 17+ (2025) Tags: @defer, Deferrable, Lazy Loading

References: Deferrable Views

Best Practices
Use @defer with on viewport
@Component({
  template: `
    @defer (on viewport) {
      <heavy-chart />
    } @placeholder {
      <div>Loading...</div>
    }
  `
})
export class DashboardComponent {}

Use @defer with on interaction
@Component({
  template: `
    <button (click)="showModal = true">Open</button>
    @defer (when showModal) {
      <modal-component />
    }
  `
})
export class MyComponent {}

Use @defer with on hover
@Component({
  template: `
    @defer (on hover) {
      <tooltip />
    }
  `
})
export class TooltipWrapper {}

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