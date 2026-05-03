---
rating: ⭐⭐
title: angular-resource
url: https://skills.sh/oguzhan18/angular-ecosystem-skills/angular-resource
---

# angular-resource

skills/oguzhan18/angular-ecosystem-skills/angular-resource
angular-resource
Installation
$ npx skills add https://github.com/oguzhan18/angular-ecosystem-skills --skill angular-resource
SKILL.md
Angular Resource

Version: Angular 19+ (2025) Tags: Resource, Async, Signals

References: Resource API

Best Practices
Use resource for async data
import { resource } from '@angular/core/rxjs-interop';

@Component({})
export class MyComponent {
  private http = inject(HttpClient);
  
  users = resource({
    loader: () => this.http.get<User[]>('/api/users').toPromise()
  });
}

Use with request
id = signal<string>('');

user = resource({
  request: () => ({ id: this.id() }),
  loader: ({ request }) => this.http.getUser(request.id).toPromise()
});

Weekly Installs
121
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