---
title: angular-jest
url: https://skills.sh/oguzhan18/angular-ecosystem-skills/angular-jest
---

# angular-jest

skills/oguzhan18/angular-ecosystem-skills/angular-jest
angular-jest
Installation
$ npx skills add https://github.com/oguzhan18/angular-ecosystem-skills --skill angular-jest
SKILL.md
Angular + Jest

Version: Jest 29.x (2025) Tags: Jest, Testing, Unit Tests

References: Jest • jest-preset-angular

Best Practices
Install Jest
npm install --save-dev jest @types/jest jest-preset-angular

Configure Jest
// jest.config.js
module.exports = {
  preset: 'jest-preset-angular',
  setupFilesAfterEnv: ['<rootDir>/setup-jest.ts'],
  testPathIgnorePatterns: ['<rootDir>/node_modules/'],
};

Write test
import { ComponentFixture, TestBed } from '@angular/core/testing';
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

Weekly Installs
125
Repository
oguzhan18/angul…m-skills
GitHub Stars
6
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass