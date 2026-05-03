---
title: angular-testing
url: https://skills.sh/analogjs/angular-skills/angular-testing
---

# angular-testing

skills/analogjs/angular-skills/angular-testing
angular-testing
Installation
$ npx skills add https://github.com/analogjs/angular-skills --skill angular-testing
Summary

Unit and integration testing for Angular v20+ with Vitest or Jasmine, supporting signals and modern patterns.

Supports both Vitest (recommended) and Jasmine test runners with native Angular v20+ integration via @angular/build
Covers signal-based components, computed values, OnPush change detection, and input/output testing with modern APIs
Includes HTTP mocking via HttpTestingController, service injection with TestBed.inject(), and dependency mocking with Vitest
Provides patterns for async testing with fakeAsync and waitForAsync, HTTP resources, and component fixture workflows
SKILL.md
Angular Testing

Test Angular v20+ applications with Vitest (recommended) or Jasmine, focusing on signal-based components and modern patterns.

Vitest Setup (Angular v20+)

Angular v20+ has native Vitest support through the @angular/build package.

npm install -D vitest jsdom


Configure in angular.json:

{
  "projects": {
    "your-app": {
      "architect": {
        "test": {
          "builder": "@angular/build:unit-test",
          "options": {
            "tsConfig": "tsconfig.spec.json",
            "buildTarget": "your-app:build"
          }
        }
      }
    }
  }
}


Run tests:

ng test              # Run tests
ng test --watch      # Watch mode
ng test --code-coverage  # With coverage


For Vitest migration from Jasmine and advanced configuration, see references/vitest-migration.md.

Basic Component Test
import { describe, it, expect, beforeEach } from 'vitest';
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { Counter } from './counter.component';

describe('Counter', () => {
  let component: Counter;
  let fixture: ComponentFixture<Counter>;
  
  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Counter], // Standalone component
    }).compileComponents();
    
    fixture = TestBed.createComponent(Counter);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });
  
  it('should create', () => {
    expect(component).toBeTruthy();
  });
  
  it('should increment count', () => {
    expect(component.count()).toBe(0);
    component.increment();
    expect(component.count()).toBe(1);
  });
  
  it('should display count in template', () => {
    component.count.set(5);
    fixture.detectChanges();
    
    const element = fixture.nativeElement.querySelector('.count');
    expect(element.textContent).toContain('5');
  });
});

Testing Signals
Direct Signal Testing
import { signal, computed } from '@angular/core';

describe('Signal logic', () => {
  it('should update computed when signal changes', () => {
    const count = signal(0);
    const doubled = computed(() => count() * 2);
    
    expect(doubled()).toBe(0);
    
    count.set(5);
    expect(doubled()).toBe(10);
    
    count.update(c => c + 1);
    expect(doubled()).toBe(12);
  });
});

Testing Component Signals
@Component({
  selector: 'app-todo-list',
  template: `
    <ul>
      @for (todo of filteredTodos(); track todo.id) {
        <li>{{ todo.text }}</li>
      }
    </ul>
    <p>{{ remaining() }} remaining</p>
  `,
})
export class TodoList {
  todos = signal<Todo[]>([]);
  filter = signal<'all' | 'active' | 'done'>('all');
  
  filteredTodos = computed(() => {
    const todos = this.todos();
    switch (this.filter()) {
      case 'active': return todos.filter(t => !t.done);
      case 'done': return todos.filter(t => t.done);
      default: return todos;
    }
  });
  
  remaining = computed(() => this.todos().filter(t => !t.done).length);
}

describe('TodoList', () => {
  let component: TodoList;
  let fixture: ComponentFixture<TodoList>;
  
  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TodoList],
    }).compileComponents();
    
    fixture = TestBed.createComponent(TodoList);
    component = fixture.componentInstance;
  });
  
  it('should filter active todos', () => {
    component.todos.set([
      { id: '1', text: 'Task 1', done: false },
      { id: '2', text: 'Task 2', done: true },
      { id: '3', text: 'Task 3', done: false },
    ]);
    
    component.filter.set('active');
    
    expect(component.filteredTodos().length).toBe(2);
    expect(component.remaining()).toBe(2);
  });
});

Testing OnPush Components

OnPush components require explicit change detection:

@Component({
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `<span>{{ data().name }}</span>`,
})
export class OnPushCmpt {
  data = input.required<{ name: string }>();
}

describe('OnPushCmpt', () => {
  it('should update when input signal changes', () => {
    const fixture = TestBed.createComponent(OnPushCmpt);
    
    // Set input using setInput (for signal inputs)
    fixture.componentRef.setInput('data', { name: 'Initial' });
    fixture.detectChanges();
    
    expect(fixture.nativeElement.textContent).toContain('Initial');
    
    // Update input
    fixture.componentRef.setInput('data', { name: 'Updated' });
    fixture.detectChanges();
    
    expect(fixture.nativeElement.textContent).toContain('Updated');
  });
});

Testing Services
Basic Service Test
@Injectable({ providedIn: 'root' })
export class CounterService {
  private _count = signal(0);
  readonly count = this._count.asReadonly();
  
  increment() { this._count.update(c => c + 1); }
  reset() { this._count.set(0); }
}

describe('CounterService', () => {
  let service: CounterService;
  
  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CounterService);
  });
  
  it('should increment count', () => {
    expect(service.count()).toBe(0);
    service.increment();
    expect(service.count()).toBe(1);
  });
});

Service with HTTP
import { HttpTestingController, provideHttpClientTesting } from '@angular/common/http/testing';
import { provideHttpClient } from '@angular/common/http';

describe('UserService', () => {
  let service: UserService;
  let httpMock: HttpTestingController;
  
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [
        provideHttpClient(),
        provideHttpClientTesting(),
      ],
    });
    
    service = TestBed.inject(UserService);
    httpMock = TestBed.inject(HttpTestingController);
  });
  
  afterEach(() => {
    httpMock.verify(); // Verify no outstanding requests
  });
  
  it('should fetch user by id', () => {
    const mockUser = { id: '1', name: 'Test User' };
    
    service.getUser('1').subscribe(user => {
      expect(user).toEqual(mockUser);
    });
    
    const req = httpMock.expectOne('/api/users/1');
    expect(req.request.method).toBe('GET');
    req.flush(mockUser);
  });
});

Mocking Dependencies
Using Vitest Mocks
import { describe, it, expect, vi, beforeEach } from 'vitest';

describe('UserProfile', () => {
  const mockUserService = {
    getUser: vi.fn(),
    updateUser: vi.fn(),
    user: signal<User | null>(null),
  };
  
  beforeEach(async () => {
    vi.clearAllMocks();
    mockUserService.getUser.mockReturnValue(of({ id: '1', name: 'Test' }));
    
    await TestBed.configureTestingModule({
      imports: [UserProfile],
      providers: [
        { provide: UserService, useValue: mockUserService },
      ],
    }).compileComponents();
  });
  
  it('should call getUser on init', () => {
    const fixture = TestBed.createComponent(UserProfile);
    fixture.detectChanges();
    
    expect(mockUserService.getUser).toHaveBeenCalledWith('1');
  });
});

Mock Signal-Based Service
const mockAuth = {
  user: signal<User | null>(null),
  isAuthenticated: computed(() => mockAuth.user() !== null),
  login: vi.fn(),
  logout: vi.fn(),
};

beforeEach(async () => {
  await TestBed.configureTestingModule({
    imports: [ProtectedPage],
    providers: [
      { provide: AuthService, useValue: mockAuth },
    ],
  }).compileComponents();
});

it('should show content when authenticated', () => {
  mockAuth.user.set({ id: '1', name: 'Test User' });
  
  const fixture = TestBed.createComponent(ProtectedPage);
  fixture.detectChanges();
  
  expect(fixture.nativeElement.querySelector('.protected-content')).toBeTruthy();
});

Testing Inputs and Outputs
@Component({
  selector: 'app-item',
  template: `<div (click)="select()">{{ item().name }}</div>`,
})
export class ItemCmpt {
  item = input.required<Item>();
  selected = output<Item>();
  
  select() {
    this.selected.emit(this.item());
  }
}

describe('ItemCmpt', () => {
  it('should emit selected event on click', () => {
    const fixture = TestBed.createComponent(ItemCmpt);
    const item: Item = { id: '1', name: 'Test Item' };
    
    fixture.componentRef.setInput('item', item);
    fixture.detectChanges();
    
    let emittedItem: Item | undefined;
    fixture.componentInstance.selected.subscribe(i => emittedItem = i);
    
    fixture.nativeElement.querySelector('div').click();
    
    expect(emittedItem).toEqual(item);
  });
});

Testing Async Operations
Using fakeAsync
import { fakeAsync, tick, flush } from '@angular/core/testing';

it('should debounce search', fakeAsync(() => {
  const fixture = TestBed.createComponent(SearchCmpt);
  fixture.detectChanges();
  
  fixture.componentInstance.query.set('test');
  
  tick(300); // Advance time for debounce
  fixture.detectChanges();
  
  expect(fixture.componentInstance.results().length).toBeGreaterThan(0);
  
  flush(); // Flush remaining timers
}));

Using waitForAsync
import { waitForAsync } from '@angular/core/testing';

it('should load data', waitForAsync(() => {
  const fixture = TestBed.createComponent(DataCmpt);
  fixture.detectChanges();
  
  fixture.whenStable().then(() => {
    fixture.detectChanges();
    expect(fixture.componentInstance.data()).toBeDefined();
  });
}));

Testing HTTP Resources
@Component({
  template: `
    @if (userResource.isLoading()) {
      <p>Loading...</p>
    } @else if (userResource.hasValue()) {
      <p>{{ userResource.value().name }}</p>
    }
  `,
})
export class UserCmpt {
  userId = signal('1');
  userResource = httpResource<User>(() => `/api/users/${this.userId()}`);
}

describe('UserCmpt', () => {
  let httpMock: HttpTestingController;
  
  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [UserCmpt],
      providers: [
        provideHttpClient(),
        provideHttpClientTesting(),
      ],
    }).compileComponents();
    
    httpMock = TestBed.inject(HttpTestingController);
  });
  
  it('should display user name after loading', () => {
    const fixture = TestBed.createComponent(UserCmpt);
    fixture.detectChanges();
    
    expect(fixture.nativeElement.textContent).toContain('Loading');
    
    const req = httpMock.expectOne('/api/users/1');
    req.flush({ id: '1', name: 'John Doe' });
    fixture.detectChanges();
    
    expect(fixture.nativeElement.textContent).toContain('John Doe');
  });
});


For advanced testing patterns including component harnesses, router testing, form testing, and directive testing, see references/testing-patterns.md.

For Vitest migration from Jasmine, see references/vitest-migration.md.

Weekly Installs
3.9K
Repository
analogjs/angular-skills
GitHub Stars
588
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass