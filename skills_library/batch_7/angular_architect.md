---
title: angular-architect
url: https://skills.sh/jeffallan/claude-skills/angular-architect
---

# angular-architect

skills/jeffallan/claude-skills/angular-architect
angular-architect
Installation
$ npx skills add https://github.com/jeffallan/claude-skills --skill angular-architect
Summary

Angular 17+ standalone components, signals, NgRx state management, and enterprise application architecture.

Generates standalone components with OnPush change detection, signals for reactive state, and computed properties; includes RxJS subscription management with takeUntilDestroyed
Configures NgRx store with actions, reducers, selectors, and effects; verifies store hydration and action flow via Redux DevTools
Implements advanced routing with lazy loading, guards, and resolvers for complex application flows
Applies performance optimization including bundle size verification with production builds and trackBy functions in loops
Delivers code with unit and integration tests targeting >85% coverage using TestBed
SKILL.md
Angular Architect

Senior Angular architect specializing in Angular 17+ with standalone components, signals, and enterprise-grade application development.

Core Workflow
Analyze requirements - Identify components, state needs, routing architecture
Design architecture - Plan standalone components, signal usage, state flow
Implement features - Build components with OnPush strategy and reactive patterns
Manage state - Setup NgRx store, effects, selectors as needed; verify store hydration and action flow with Redux DevTools before proceeding
Optimize - Apply performance best practices and bundle optimization; run ng build --configuration production to verify bundle size and flag regressions
Test - Write unit and integration tests with TestBed; verify >85% coverage threshold is met
Reference Guide

Load detailed guidance based on context:

Topic	Reference	Load When
Components	references/components.md	Standalone components, signals, input/output
RxJS	references/rxjs.md	Observables, operators, subjects, error handling
NgRx	references/ngrx.md	Store, effects, selectors, entity adapter
Routing	references/routing.md	Router config, guards, lazy loading, resolvers
Testing	references/testing.md	TestBed, component tests, service tests
Key Patterns
Standalone Component with OnPush and Signals
import { ChangeDetectionStrategy, Component, computed, input, output, signal } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-user-card',
  standalone: true,
  imports: [CommonModule],
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `
    <div class="user-card">
      <h2>{{ fullName() }}</h2>
      <button (click)="onSelect()">Select</button>
    </div>
  `,
})
export class UserCardComponent {
  firstName = input.required<string>();
  lastName = input.required<string>();
  selected = output<string>();

  fullName = computed(() => `${this.firstName()} ${this.lastName()}`);

  onSelect(): void {
    this.selected.emit(this.fullName());
  }
}

RxJS Subscription Management with takeUntilDestroyed
import { Component, OnInit, inject } from '@angular/core';
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';
import { UserService } from './user.service';

@Component({ selector: 'app-users', standalone: true, template: `...` })
export class UsersComponent implements OnInit {
  private userService = inject(UserService);
  // DestroyRef is captured at construction time for use in ngOnInit
  private destroyRef = inject(DestroyRef);

  ngOnInit(): void {
    this.userService.getUsers()
      .pipe(takeUntilDestroyed(this.destroyRef))
      .subscribe({
        next: (users) => { /* handle */ },
        error: (err) => console.error('Failed to load users', err),
      });
  }
}

NgRx Action / Reducer / Selector
// actions
export const loadUsers = createAction('[Users] Load Users');
export const loadUsersSuccess = createAction('[Users] Load Users Success', props<{ users: User[] }>());
export const loadUsersFailure = createAction('[Users] Load Users Failure', props<{ error: string }>());

// reducer
export interface UsersState { users: User[]; loading: boolean; error: string | null; }
const initialState: UsersState = { users: [], loading: false, error: null };

export const usersReducer = createReducer(
  initialState,
  on(loadUsers, (state) => ({ ...state, loading: true, error: null })),
  on(loadUsersSuccess, (state, { users }) => ({ ...state, users, loading: false })),
  on(loadUsersFailure, (state, { error }) => ({ ...state, error, loading: false })),
);

// selectors
export const selectUsersState = createFeatureSelector<UsersState>('users');
export const selectAllUsers = createSelector(selectUsersState, (s) => s.users);
export const selectUsersLoading = createSelector(selectUsersState, (s) => s.loading);

Constraints
MUST DO
Use standalone components (Angular 17+ default)
Use signals for reactive state where appropriate
Use OnPush change detection strategy
Use strict TypeScript configuration
Implement proper error handling in RxJS streams
Use trackBy functions in *ngFor loops
Write tests with >85% coverage
Follow Angular style guide
MUST NOT DO
Use NgModule-based components (except when required for compatibility)
Forget to unsubscribe from observables (use takeUntilDestroyed or async pipe)
Use async operations without proper error handling
Skip accessibility attributes
Expose sensitive data in client-side code
Use any type without justification
Mutate state directly in NgRx
Skip unit tests for critical logic
Output Templates

When implementing Angular features, provide:

Component file with standalone configuration
Service file if business logic is involved
State management files if using NgRx
Test file with comprehensive test cases
Brief explanation of architectural decisions

Documentation

Weekly Installs
1.9K
Repository
jeffallan/claude-skills
GitHub Stars
8.7K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass