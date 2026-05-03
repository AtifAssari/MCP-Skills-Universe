---
rating: ⭐⭐
title: angular-bootstrap
url: https://skills.sh/oguzhan18/angular-ecosystem-skills/angular-bootstrap
---

# angular-bootstrap

skills/oguzhan18/angular-ecosystem-skills/angular-bootstrap
angular-bootstrap
Installation
$ npx skills add https://github.com/oguzhan18/angular-ecosystem-skills --skill angular-bootstrap
SKILL.md
ng-bootstrap / Angular Bootstrap

Version: ng-bootstrap 17.x (2025) Tags: Bootstrap, UI Components, ng-bootstrap

References: ng-bootstrap • GitHub

API Changes

This section documents recent version-specific API changes.

NEW: Bootstrap 5 support — Full Bootstrap 5 integration

NEW: Standalone components — All components are standalone

NEW: Bootstrap icons support — Icon integration

NEW: Angular 17+ support — Full compatibility with modern Angular

Best Practices
Install ng-bootstrap
npm install @ng-bootstrap/ng-bootstrap @popperjs/core bootstrap

Import styles in angular.json
{
  "styles": ["node_modules/bootstrap/dist/css/bootstrap.min.css"]
}

Import NgbModule
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

@NgModule({
  imports: [NgbModule]
})
export class AppModule {}

Use standalone import
import { NgbCarouselModule } from '@ng-bootstrap/ng-bootstrap';

@Component({
  standalone: true,
  imports: [NgbCarouselModule],
  // ...
})
export class CarouselComponent {}

Use Modal
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';

@Component({})
export class ModalComponent {
  constructor(private modalService: NgbModal) {}

  open(content: TemplateRef<any>) {
    this.modalService.open(content);
  }
}

Use Dropdown
import { NgbDropdownModule } from '@ng-bootstrap/ng-bootstrap';

@Component({
  template: `
    <div ngbDropdown>
      <button ngbDropdownToggle>Menu</button>
      <div ngbDropdownMenu>
        <button ngbDropdownItem>Action</button>
      </div>
    </div>
  `
})
export class DropdownComponent {}

Use Accordion
import { NgbAccordionModule } from '@ng-bootstrap/ng-bootstrap';

@Component({
  template: `
    <ngb-accordion>
      <ngb-panel title="First">
        <ng-template ngbPanelContent>Content 1</ng-template>
      </ngb-panel>
    </ngb-accordion>
  `
})
export class AccordionComponent {}

Use Datepicker
import { NgbDatepickerModule } from '@ng-bootstrap/ng-bootstrap';

@Component({
  template: `
    <ngb-datepicker [(ngModel)]="date"></ngb-datepicker>
  `
})
export class DatePickerComponent {
  date: NgbDateStruct;
}

Use Toast
import { NgbToast } from '@ng-bootstrap/ng-bootstrap';

@Component({
  template: `
    @for (toast of toasts; track toast) {
      <ngb-toast>{{ toast }}</ngb-toast>
    }
  `
})
export class ToastComponent {}

Use Typeahead
import { NgbTypeaheadModule } from '@ng-bootstrap/ng-bootstrap';

@Component({
  template: `
    <input ngbTypeahead [ngModel]="value" [source]="search" />
  `
})
export class TypeaheadComponent {
  search = (text$: Observable<string>) => 
    text$.pipe(debounceTime(200), distinctUntilChanged());
}

Weekly Installs
127
Repository
oguzhan18/angul…m-skills
GitHub Stars
6
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass