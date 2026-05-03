---
title: angular-reactive
url: https://skills.sh/oguzhan18/angular-ecosystem-skills/angular-reactive
---

# angular-reactive

skills/oguzhan18/angular-ecosystem-skills/angular-reactive
angular-reactive
Installation
$ npx skills add https://github.com/oguzhan18/angular-ecosystem-skills --skill angular-reactive
SKILL.md
Angular Reactive Programming

Version: Angular 21 (2025) Tags: Reactive, Observables, RxJS, BehaviorSubject

References: Reactive Guide • RxJS

Best Practices
Use BehaviorSubject for state
@Injectable({ providedIn: 'root' })
export class StateService {
  private state = new BehaviorSubject<State>(initialState);
  state$ = this.state.asObservable();
  
  updateState(newState: Partial<State>) {
    this.state.next({ ...this.state.value, ...newState });
  }
}

Use Observable in services
@Injectable({ providedIn: 'root' })
export class DataService {
  private http = inject(HttpClient);
  
  getData(): Observable<Data[]> {
    return this.http.get<Data[]>('/api/data');
  }
}

Use async pipe
@Component({
  template: `
    @if (data$ | async; as data) {
      {{ data.name }}
    }
  `
})
export class MyComponent {
  data$ = this.service.getData();
}

Use shareReplay for caching
data$ = this.http.get('/api/data').pipe(
  shareReplay(1)
);

Use takeUntil for cleanup
@Component({})
export class MyComponent implements OnDestroy {
  private destroy$ = new Subject<void>();
  
  ngOnInit() {
    this.data$.pipe(takeUntil(this.destroy$)).subscribe();
  }
  
  ngOnDestroy() {
    this.destroy$.next();
    this.destroy$.complete();
  }
}

Weekly Installs
123
Repository
oguzhan18/angul…m-skills
GitHub Stars
6
First Seen
6 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass