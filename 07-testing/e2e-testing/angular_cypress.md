---
rating: ⭐⭐
title: angular-cypress
url: https://skills.sh/oguzhan18/angular-ecosystem-skills/angular-cypress
---

# angular-cypress

skills/oguzhan18/angular-ecosystem-skills/angular-cypress
angular-cypress
Installation
$ npx skills add https://github.com/oguzhan18/angular-ecosystem-skills --skill angular-cypress
SKILL.md
Angular + Cypress

Version: Cypress 13.x (2025) Tags: Cypress, E2E, Testing, Component Tests

References: Cypress • Cypress Angular

Best Practices
Install Cypress
npm install -D cypress @cypress/angular cypress-visual-regression
npx cypress open

Write E2E test
describe('My First Test', () => {
  it('visits the kitchen sink', () => {
    cy.visit('/');
    cy.contains('type').click();
    cy.get('.action-email').type('fake@email.com');
    cy.get('.action-email').should('have.value', 'fake@email.com');
  });
});

Write component test
import { mount } from 'cypress/angular';
import { ButtonComponent } from './button.component';

describe('ButtonComponent', () => {
  it('renders button with text', () => {
    mount(ButtonComponent, { 
      componentProperties: { 
        label: 'Click me' 
      } 
    });
    cy.get('button').should('contain.text', 'Click me');
  });
});

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