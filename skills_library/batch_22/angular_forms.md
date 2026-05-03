---
title: angular-forms
url: https://skills.sh/oguzhan18/angular-ecosystem-skills/angular-forms
---

# angular-forms

skills/oguzhan18/angular-ecosystem-skills/angular-forms
angular-forms
Installation
$ npx skills add https://github.com/oguzhan18/angular-ecosystem-skills --skill angular-forms
SKILL.md
@angular/forms

Version: Angular 21 (2025) Tags: Forms, Validation, Reactive Forms, Template-Driven

References: Reactive Forms • Template-Driven • API

API Changes

This section documents recent version-specific API changes.

NEW: Signal-based form controls — Angular 19+ signal integration for form controls

NEW: Functional validators — Prefer functional validators over class-based validators

NEW: AbstractControl.markAllAsTouched() — New method to mark all controls as touched

NEW: nonNullable option — Create non-nullable FormControls

NEW: Typed forms — Full TypeScript support for form groups and arrays

DEPRECATED: Class-based validators — Migrate to functional validators

Best Practices
Use Reactive Forms for complex forms — Better structure, validation, and testability
import { FormBuilder, Validators, ReactiveFormsModule } from '@angular/forms';

@Component({
  standalone: true,
  imports: [ReactiveFormsModule],
  template: `
    <form [formGroup]="form" (ngSubmit)="onSubmit()">
      <input formControlName="email" />
      <div *ngIf="form.controls.email.invalid && form.controls.email.touched">
        Email is required
      </div>
    </form>
  `
})
export class LoginComponent {
  private fb = inject(FormBuilder);
  
  form = this.fb.nonNullable.group({
    email: ['', [Validators.required, Validators.email]],
    password: ['', [Validators.required, Validators.minLength(8)]]
  });

  onSubmit() {
    if (this.form.valid) {
      console.log(this.form.getRawValue());
    }
  }
}

Use FormBuilder for cleaner code
form = this.fb.group({
  name: ['', Validators.required],
  email: ['', [Validators.required, Validators.email]],
  address: this.fb.group({
    street: [''],
    city: ['']
  })
});

Use custom validators for complex logic
// Functional validator (preferred)
const forbiddenNameValidator = (control: AbstractControl): ValidationErrors | null => {
  const forbidden = ['admin', 'root', 'superuser'];
  return forbidden.includes(control.value) ? { forbiddenName: true } : null;
};

// Usage
name: ['', forbiddenNameValidator]

Use async validators for server-side validation
email: ['', 
  [Validators.email], 
  [asyncValidator, { debounceTime: 300 }]
]

Use FormArray for dynamic form fields
const form = this.fb.group({
  emails: this.fb.array([
    this.fb.control('')
  ])
});

get emails(): FormArray {
  return this.form.get('emails') as FormArray;
}

addEmail() {
  this.emails.push(this.fb.control(''));
}

Use updateOn option for performance
// Only validate on blur
email: ['', { updateOn: 'blur' }]

// Only validate on submit
password: ['', { updateOn: 'submit' }]

Show validation errors conditionally
<input formControlName="email" 
       [class.is-invalid]="email.invalid && (email.dirty || email.touched)" />

Use disable() for conditionally disabled fields
// Disable based on another control
this.form.statusChanges.subscribe(() => {
  if (this.form.value.isAdmin) {
    this.form.controls.permissions.enable();
  } else {
    this.form.controls.permissions.disable();
  }
});

Reset form properly
// Reset with default values
this.form.reset({ email: '', name: 'Default' });

// Reset and clear validators
this.form.reset();
this.form.clearValidators();

Weekly Installs
123
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