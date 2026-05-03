---
title: angular-query
url: https://skills.sh/oguzhan18/angular-ecosystem-skills/angular-query
---

# angular-query

skills/oguzhan18/angular-ecosystem-skills/angular-query
angular-query
Installation
$ npx skills add https://github.com/oguzhan18/angular-ecosystem-skills --skill angular-query
SKILL.md
@tanstack/angular-query-experimental

Version: 5.x (2025) Tags: Data Fetching, Server State, Caching, TanStack Query

References: Docs • GitHub • npm

API Changes

This section documents version-specific API changes.

NEW: Angular Query v5 — Signal-based API for TanStack Query source

NEW: injectQuery — Signal-based query injection

NEW: injectMutation — Signal-based mutation injection

NEW: Query options pattern — Service-based query configuration

NEW: DevTools integration — Angular Query DevTools for debugging

Best Practices
Install and setup
npm install @tanstack/angular-query-experimental

import { provideHttpClient } from '@angular/common/http';
import { provideTanStackQuery } from '@tanstack/angular-query-experimental';
import { QueryClient } from '@tanstack/query-core';

export const appConfig: ApplicationConfig = {
  providers: [
    provideHttpClient(),
    provideTanStackQuery(new QueryClient())
  ]
};

Use injectQuery for data fetching
import { injectQuery } from '@tanstack/angular-query-experimental';

@Component({})
export class TodosComponent {
  private http = inject(HttpClient);
  
  query = injectQuery(() => ({
    queryKey: ['todos'],
    queryFn: () => lastValueFrom(this.http.get<Todo[]>('/api/todos'))
  }));
}

Use in templates with signals
@Component({
  template: `
    @if (query.isPending()) {
      Loading...
    } @else if (query.isError()) {
      Error: {{ query.error().message }}
    } @else {
      @for (todo of query.data(); track todo.id) {
        {{ todo.title }}
      }
    }
  `
})
export class TodosComponent {
  query = injectQuery(() => ({ ... }));
}

Use mutations for data modification
import { injectMutation, injectQueryClient } from '@tanstack/angular-query-experimental';

@Component({})
export class AddTodoComponent {
  private http = inject(HttpClient);
  private queryClient = injectQueryClient();
  
  mutation = injectMutation(() => ({
    mutationFn: (newTodo: string) => 
      lastValueFrom(this.http.post('/api/todos', { title: newTodo })),
    onSuccess: () => {
      this.queryClient.invalidateQueries({ queryKey: ['todos'] });
    }
  }));
  
  addTodo(title: string) {
    this.mutation.mutate(title);
  }
}

Use query options for reusable queries
@Injectable({ providedIn: 'root' })
export class TodoService {
  private http = inject(HttpClient);
  
  getTodoOptions = (id: number) => queryOptions({
    queryKey: ['todo', id],
    queryFn: () => lastValueFrom(this.http.get(`/api/todos/${id}`))
  });
}

@Component({})
export class TodoComponent {
  private todoService = inject(TodoService);
  
  todo = this.todoService.getTodoOptions(1);
}

Handle loading and error states
query = injectQuery(() => ({
  queryKey: ['todos'],
  queryFn: () => fetchTodos(),
  retry: 3,
  staleTime: 1000 * 60 * 5, // 5 minutes
  refetchOnWindowFocus: false
}));

Use invalidation for cache updates
mutation = injectMutation(() => ({
  mutationFn: createTodo,
  onSuccess: () => {
    queryClient.invalidateQueries({ queryKey: ['todos'] });
  }
}));

Use optimistic updates
mutation = injectMutation(() => ({
  mutationFn: updateTodo,
  onMutate: async (newTodo) => {
    await queryClient.cancelQueries({ queryKey: ['todos'] });
    const previousTodos = queryClient.getQueryData(['todos']);
    queryClient.setQueryData(['todos'], (old: Todo[]) => [...old, newTodo]);
    return { previousTodos };
  },
  onError: (err, newTodo, context) => {
    queryClient.setQueryData(['todos'], context.previousTodos);
  }
}));

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