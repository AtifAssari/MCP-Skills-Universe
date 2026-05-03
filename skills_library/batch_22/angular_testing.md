---
title: angular-testing
url: https://skills.sh/oguzhan18/angular-ecosystem-skills/angular-testing
---

# angular-testing

skills/oguzhan18/angular-ecosystem-skills/angular-testing
angular-testing
Installation
$ npx skills add https://github.com/oguzhan18/angular-ecosystem-skills --skill angular-testing
SKILL.md
Angular Testing

Version: Angular 21 (2025) Tags: Testing, Jasmine, Karma, Vitest, Cypress, Jest

References: Testing Guide • Testing API • Angular Blog

API Changes

This section documents recent version-specific API changes.

NEW: Vitest as default — Angular 21+ uses Vitest instead of Jasmine/Karma source

NEW: Template coverage — Coverage reports now include HTML templates source

NEW: Component input testing — Test component inputs directly with Component输入

NEW: Functional interceptors for testing — Easier to test HTTP interceptors

DEPRECATED: Karma test runner — Migrate to Vitest for modern Angular

Best Practices
Use TestBed for component testing
import { TestBed } from '@angular/core/testing';
import { MyComponent } from './my.component';

describe('MyComponent', () => {
  let component: MyComponent;
  let fixture: ComponentFixture<MyComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MyComponent]
    }).compileComponents();

    fixture = TestBed.createComponent(MyComponent);
    component = fixture.componentInstance;
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

Use AAA pattern (Arrange-Act-Assert)
it('should calculate total correctly', () => {
  // Arrange
  const service = new CalculatorService();
  
  // Act
  const result = service.add(2, 3);
  
  // Assert
  expect(result).toBe(5);
});

Use fakeAsync and tick for async operations
import { fakeAsync, tick } from '@angular/core/testing';

it('should fetch data after delay', fakeAsync(() => {
  service.getData();
  tick(1000);
  expect(component.data).toBeTruthy();
}));

Use spies for mocking
it('should call service', () => {
  spyOn(service, 'getData').and.returnValue(of({ name: 'Test' }));
  
  component.loadData();
  
  expect(service.getData).toHaveBeenCalled();
});

Use by.css for querying DOM elements
import { By } from '@angular/platform-browser';

it('should display title', () => {
  fixture.detectChanges();
  const el = fixture.debugElement.query(By.css('.title'));
  expect(el.nativeElement.textContent).toBe('Hello');
});

Test behavior, not implementation
// ❌ Bad - tests implementation details
expect(component['privateMethod']).toHaveBeenCalled();

// ✅ Good - tests behavior
expect(fixture.nativeElement.querySelector('.result')).toContain('expected');

Use provideHttpClient for HTTP testing
TestBed.configureTestingModule({
  providers: [
    provideHttpClient(withInterceptors([authInterceptor]))
  ]
});

Use mock services for dependencies
const mockAuthService = {
  isAuthenticated: jasmine.createSpy().and.returnValue(true),
  getToken: jasmine.createSpy().and.returnValue('fake-token')
};

TestBed.configureTestingModule({
  providers: [{ provide: AuthService, useValue: mockAuthService }]
});

Test form validation
it('should show error for invalid email', () => {
  component.form.controls.email.setValue('invalid');
  component.form.controls.email.markAsTouched();
  
  fixture.detectChanges();
  
  expect(fixture.nativeElement.querySelector('.error')).toBeTruthy();
});

Use detectChanges appropriately
// After changing component properties
component.value = 'new value';
fixture.detectChanges();

// For async operations
fixture.detectChanges();
await fixture.whenStable();
fixture.detectChanges();

Weekly Installs
126
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