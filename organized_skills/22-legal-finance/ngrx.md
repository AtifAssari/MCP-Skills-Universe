---
rating: ⭐⭐
title: ngrx
url: https://skills.sh/claude-dev-suite/claude-dev-suite/ngrx
---

# ngrx

skills/claude-dev-suite/claude-dev-suite/ngrx
ngrx
Installation
$ npx skills add https://github.com/claude-dev-suite/claude-dev-suite --skill ngrx
SKILL.md
NgRx State Management - Quick Reference

Deep Knowledge: Use mcp__documentation__fetch_docs with technology: angular for NgRx patterns.

Store Setup
// app.config.ts
import { provideStore } from '@ngrx/store';
import { provideEffects } from '@ngrx/effects';
import { provideStoreDevtools } from '@ngrx/store-devtools';

export const appConfig: ApplicationConfig = {
  providers: [
    provideStore({ users: usersReducer }),
    provideEffects([UsersEffects]),
    provideStoreDevtools({ maxAge: 25, logOnly: !isDevMode() }),
  ]
};

Actions
import { createActionGroup, emptyProps, props } from '@ngrx/store';

export const UsersActions = createActionGroup({
  source: 'Users',
  events: {
    'Load Users': emptyProps(),
    'Load Users Success': props<{ users: User[] }>(),
    'Load Users Failure': props<{ error: string }>(),
    'Add User': props<{ user: User }>(),
    'Remove User': props<{ id: number }>(),
  },
});

Reducer with createFeature
import { createFeature, createReducer, on } from '@ngrx/store';

export interface UsersState {
  users: User[];
  loading: boolean;
  error: string | null;
}

const initialState: UsersState = {
  users: [],
  loading: false,
  error: null,
};

export const usersFeature = createFeature({
  name: 'users',
  reducer: createReducer(
    initialState,
    on(UsersActions.loadUsers, (state) => ({ ...state, loading: true, error: null })),
    on(UsersActions.loadUsersSuccess, (state, { users }) => ({
      ...state, users, loading: false,
    })),
    on(UsersActions.loadUsersFailure, (state, { error }) => ({
      ...state, error, loading: false,
    })),
    on(UsersActions.addUser, (state, { user }) => ({
      ...state, users: [...state.users, user],
    })),
    on(UsersActions.removeUser, (state, { id }) => ({
      ...state, users: state.users.filter(u => u.id !== id),
    })),
  ),
});

export const { selectUsers, selectLoading, selectError } = usersFeature;

Effects
import { inject } from '@angular/core';
import { Actions, createEffect, ofType } from '@ngrx/effects';
import { catchError, exhaustMap, map, of } from 'rxjs';

export class UsersEffects {
  private actions$ = inject(Actions);
  private userService = inject(UserService);

  loadUsers$ = createEffect(() =>
    this.actions$.pipe(
      ofType(UsersActions.loadUsers),
      exhaustMap(() =>
        this.userService.getUsers().pipe(
          map(users => UsersActions.loadUsersSuccess({ users })),
          catchError(error => of(UsersActions.loadUsersFailure({ error: error.message }))),
        )
      )
    )
  );
}

Component Integration with Signals
import { Component, inject } from '@angular/core';
import { Store } from '@ngrx/store';
import { selectUsers, selectLoading } from './users.reducer';
import { UsersActions } from './users.actions';

@Component({
  standalone: true,
  template: `
    @if (loading()) {
      <app-spinner />
    }
    @for (user of users(); track user.id) {
      <app-user-card [user]="user" (delete)="remove(user.id)" />
    }
  `
})
export class UsersComponent {
  private store = inject(Store);
  users = this.store.selectSignal(selectUsers);
  loading = this.store.selectSignal(selectLoading);

  constructor() {
    this.store.dispatch(UsersActions.loadUsers());
  }

  remove(id: number) {
    this.store.dispatch(UsersActions.removeUser({ id }));
  }
}

ComponentStore (Lightweight Alternative)
import { Injectable } from '@angular/core';
import { ComponentStore } from '@ngrx/component-store';
import { tapResponse } from '@ngrx/operators';
import { switchMap } from 'rxjs';

interface UsersState {
  users: User[];
  loading: boolean;
}

@Injectable()
export class UsersStore extends ComponentStore<UsersState> {
  constructor(private userService: UserService) {
    super({ users: [], loading: false });
  }

  readonly users = this.selectSignal(state => state.users);
  readonly loading = this.selectSignal(state => state.loading);

  readonly loadUsers = this.effect<void>(trigger$ =>
    trigger$.pipe(
      switchMap(() => {
        this.patchState({ loading: true });
        return this.userService.getUsers().pipe(
          tapResponse(
            users => this.patchState({ users, loading: false }),
            () => this.patchState({ loading: false }),
          )
        );
      })
    )
  );
}

Anti-Patterns
Anti-Pattern	Why It's Bad	Correct Approach
Store for local component state	Over-engineering	Use signals or ComponentStore
Dispatching in effects	Infinite loops	Return actions from effects
Not using createActionGroup	Verbose action creators	Use createActionGroup
Subscribing to store in components	Memory leaks	Use selectSignal()
Quick Troubleshooting
Issue	Likely Cause	Solution
State not updating	Immutability violation	Return new object in reducer
Effect not triggering	Wrong action type	Check ofType() matches
DevTools not showing	Missing provider	Add provideStoreDevtools()
Selector returning undefined	Feature not registered	Add to provideStore()
Weekly Installs
24
Repository
claude-dev-suit…ev-suite
GitHub Stars
12
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass