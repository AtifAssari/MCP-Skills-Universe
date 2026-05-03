---
rating: ⭐⭐
title: rxjs-implementation
url: https://skills.sh/pluginagentmarketplace/custom-plugin-angular/rxjs-implementation
---

# rxjs-implementation

skills/pluginagentmarketplace/custom-plugin-angular/rxjs-implementation
rxjs-implementation
Installation
$ npx skills add https://github.com/pluginagentmarketplace/custom-plugin-angular --skill rxjs-implementation
SKILL.md
RxJS Implementation Skill
Quick Start
Observable Basics
import { Observable } from 'rxjs';

// Create observable
const observable = new Observable((observer) => {
  observer.next(1);
  observer.next(2);
  observer.next(3);
  observer.complete();
});

// Subscribe
const subscription = observable.subscribe({
  next: (value) => console.log(value),
  error: (error) => console.error(error),
  complete: () => console.log('Done')
});

// Unsubscribe
subscription.unsubscribe();

Common Operators
import { map, filter, switchMap, takeUntil } from 'rxjs/operators';

// Transformation
data$.pipe(
  map(user => user.name),
  filter(name => name.length > 0)
).subscribe(name => console.log(name));

// Higher-order
userId$.pipe(
  switchMap(id => this.userService.getUser(id))
).subscribe(user => console.log(user));

Subjects
Subject Types
import { Subject, BehaviorSubject, ReplaySubject } from 'rxjs';

// Subject - No initial value
const subject = new Subject<string>();
subject.next('hello');

// BehaviorSubject - Has initial value
const behavior = new BehaviorSubject<string>('initial');
behavior.next('new value');

// ReplaySubject - Replays N values
const replay = new ReplaySubject<string>(3);
replay.next('one');
replay.next('two');

Service with Subject
@Injectable()
export class NotificationService {
  private messageSubject = new Subject<string>();
  public message$ = this.messageSubject.asObservable();

  notify(message: string) {
    this.messageSubject.next(message);
  }
}

// Usage
constructor(private notification: NotificationService) {
  this.notification.message$.subscribe(msg => {
    console.log('Notification:', msg);
  });
}

Transformation Operators
// map - Transform values
source$.pipe(
  map(user => user.name)
)

// switchMap - Switch to new observable (cancel previous)
userId$.pipe(
  switchMap(id => this.userService.getUser(id))
)

// mergeMap - Merge all results
fileIds$.pipe(
  mergeMap(id => this.downloadFile(id))
)

// concatMap - Sequential processing
tasks$.pipe(
  concatMap(task => this.processTask(task))
)

// exhaustMap - Ignore new while processing
clicks$.pipe(
  exhaustMap(() => this.longRequest())
)

Filtering Operators
// filter - Only pass matching values
data$.pipe(
  filter(item => item.active)
)

// first - Take first value
data$.pipe(first())

// take - Take N values
data$.pipe(take(5))

// takeUntil - Take until condition
data$.pipe(
  takeUntil(this.destroy$)
)

// distinct - Filter duplicates
data$.pipe(
  distinct(),
  distinctUntilChanged()
)

// debounceTime - Wait N ms
input$.pipe(
  debounceTime(300),
  distinctUntilChanged()
)

Combination Operators
import { combineLatest, merge, concat, zip } from 'rxjs';

// combineLatest - Latest from all
combineLatest([user$, settings$, theme$]).pipe(
  map(([user, settings, theme]) => ({ user, settings, theme }))
)

// merge - Values from any
merge(click$, hover$, input$)

// concat - Sequential
concat(request1$, request2$, request3$)

// zip - Wait for all
zip(form1$, form2$, form3$)

// withLatestFrom - Combine with latest
click$.pipe(
  withLatestFrom(user$),
  map(([click, user]) => ({ click, user }))
)

Error Handling
// catchError - Handle errors
data$.pipe(
  catchError(error => {
    console.error('Error:', error);
    return of(defaultValue);
  })
)

// retry - Retry on error
request$.pipe(
  retry(3),
  catchError(error => throwError(error))
)

// timeout - Timeout if no value
request$.pipe(
  timeout(5000),
  catchError(error => of(null))
)

Memory Leak Prevention
Unsubscribe Pattern
private destroy$ = new Subject<void>();

ngOnInit() {
  this.data$.pipe(
    takeUntil(this.destroy$)
  ).subscribe(data => {
    this.processData(data);
  });
}

ngOnDestroy() {
  this.destroy$.next();
  this.destroy$.complete();
}

Async Pipe (Preferred)
// Component
export class UserComponent {
  user$ = this.userService.getUser(1);

  constructor(private userService: UserService) {}
}

// Template - Async pipe handles unsubscribe
<div>{{ user$ | async as user }}
  <p>{{ user.name }}</p>
</div>

Advanced Patterns
Share Operator
// Hot observable - Share single subscription
readonly users$ = this.http.get('/api/users').pipe(
  shareReplay(1) // Cache last result
);

// Now multiple subscriptions use same HTTP request
this.users$.subscribe(users => {...});
this.users$.subscribe(users => {...}); // Reuses cached

Scan for State
// Accumulate state
const counter$ = clicks$.pipe(
  scan((count) => count + 1, 0)
)

// Complex state
const appState$ = actions$.pipe(
  scan((state, action) => {
    switch(action.type) {
      case 'ADD_USER': return { ...state, users: [...state.users, action.user] };
      case 'DELETE_USER': return { ...state, users: state.users.filter(u => u.id !== action.id) };
      default: return state;
    }
  }, initialState)
)

Forkjoin for Multiple Requests
// Parallel requests
forkJoin({
  users: this.userService.getUsers(),
  settings: this.settingService.getSettings(),
  themes: this.themeService.getThemes()
}).subscribe(({ users, settings, themes }) => {
  console.log('All loaded:', users, settings, themes);
})

Testing Observables
import { marbles } from 'rxjs-marbles';

it('should map values correctly', marbles((m) => {
  const source = m.hot('a-b-|', { a: 1, b: 2 });
  const expected = m.cold('x-y-|', { x: 2, y: 4 });

  const result = source.pipe(
    map(x => x * 2)
  );

  m.expect(result).toBeObservable(expected);
}));

Best Practices
Always unsubscribe: Use takeUntil or async pipe
Use higher-order operators: switchMap, mergeMap, etc.
Avoid nested subscriptions: Use operators instead
Share subscriptions: Use share/shareReplay for expensive operations
Handle errors: Always include catchError
Type your observables: Observable<User> not just Observable
Common Mistakes to Avoid
// ❌ Wrong - Creates multiple subscriptions
this.data$.subscribe(d => {
  this.data$.subscribe(d2 => {
    // nested subscriptions!
  });
});

// ✅ Correct - Use switchMap
this.data$.pipe(
  switchMap(d => this.otherService.fetch(d))
).subscribe(result => {
  // handled
});

// ❌ Wrong - Memory leak
ngOnInit() {
  this.data$.subscribe(data => this.data = data);
}

// ✅ Correct - Unsubscribe or async
ngOnInit() {
  this.data$ = this.service.getData();
}
// In template: {{ data$ | async }}

Resources
RxJS Documentation
Interactive Diagrams
RxJS Operators
Weekly Installs
31
Repository
pluginagentmark…-angular
GitHub Stars
5
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass