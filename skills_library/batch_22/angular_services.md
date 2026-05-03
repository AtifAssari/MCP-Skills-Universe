---
title: angular-services
url: https://skills.sh/oguzhan18/angular-ecosystem-skills/angular-services
---

# angular-services

skills/oguzhan18/angular-ecosystem-skills/angular-services
angular-services
Installation
$ npx skills add https://github.com/oguzhan18/angular-ecosystem-skills --skill angular-services
SKILL.md
Angular Services

Version: Angular 21 (2025) Tags: Services, @Injectable, DI

References: Services Guide • @Injectable API

Best Practices
Create service with providedIn
@Injectable({ providedIn: 'root' })
export class DataService {
  getData() {
    return this.http.get('/api/data');
  }
}

Use inject() function
@Injectable({ providedIn: 'root' })
export class UserService {
  private http = inject(HttpClient);
  
  getUsers() {
    return this.http.get<User[]>('/api/users');
  }
}

Use factory providers
@Injectable({
  providedIn: 'root',
  useFactory: () => new LoggerService(environment.production)
})
export class LoggerService {
  constructor(private isProduction: boolean) {}
}

Use providedIn: 'any' for lazy services
@Injectable({ providedIn: 'any' })
export class LazyService {}

Use service in component
@Component({})
export class MyComponent {
  private dataService = inject(DataService);
  
  data$ = this.dataService.getData();
}

Use multiple services
@Component({})
export class MyComponent {
  private auth = inject(AuthService);
  private http = inject(HttpClient);
  private router = inject(Router);
}

Use service for shared state
@Injectable({ providedIn: 'root' })
export class CartService {
  private items = signal<Item[]>([]);
  
  cartItems = this.items.asReadonly();
  
  addItem(item: Item) {
    this.items.update(items => [...items, item]);
  }
}

Weekly Installs
124
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