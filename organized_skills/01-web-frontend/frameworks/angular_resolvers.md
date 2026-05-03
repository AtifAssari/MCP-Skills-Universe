---
rating: ⭐⭐
title: angular-resolvers
url: https://skills.sh/oguzhan18/angular-ecosystem-skills/angular-resolvers
---

# angular-resolvers

skills/oguzhan18/angular-ecosystem-skills/angular-resolvers
angular-resolvers
Installation
$ npx skills add https://github.com/oguzhan18/angular-ecosystem-skills --skill angular-resolvers
SKILL.md
Angular Route Resolvers

Version: Angular 21 (2025) Tags: Resolvers, Routing, Data Loading

References: Resolvers Guide

Best Practices
Create functional resolver
export const userResolver: ResolveFn<User> = (route, state) => {
  const userService = inject(UserService);
  const userId = route.paramMap.get('id');
  return userService.getUser(userId!);
};

Use resolver in route
const routes: Routes = [
  {
    path: 'user/:id',
    resolve: { user: userResolver },
    component: UserComponent
  }
];

Get resolved data in component
@Component({})
export class UserComponent {
  private route = inject(ActivatedRoute);
  
  user = this.route.snapshot.data['user'];
  
  // Or with input binding (Angular 17+)
  userId = input<string>();
}

Handle resolver errors
export const dataResolver: ResolveFn<Data> = (route, state) => {
  const service = inject(DataService);
  return service.getData().pipe(
    catchError(() => of(null))
  );
};

Use multiple resolvers
const routes: Routes = [
  {
    path: 'dashboard',
    resolve: {
      user: userResolver,
      settings: settingsResolver
    },
    component: DashboardComponent
  }
];

Weekly Installs
122
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