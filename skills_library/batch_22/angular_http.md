---
title: angular-http
url: https://skills.sh/oguzhan18/angular-ecosystem-skills/angular-http
---

# angular-http

skills/oguzhan18/angular-ecosystem-skills/angular-http
angular-http
Installation
$ npx skills add https://github.com/oguzhan18/angular-ecosystem-skills --skill angular-http
SKILL.md
@angular/common/http

Version: Angular 21 (2025) Tags: HTTP, REST, API, Interceptors

References: HttpClient • API • Interceptors

API Changes

This section documents recent version-specific API changes.

NEW: Functional interceptors — Use provideHttpClient(withInterceptors([...])) for modern interceptor setup source

NEW: withFetch — Use native fetch API with HttpClient source

NEW: withInterceptorsFromDi — Legacy interceptor support with functional approach

NEW: HttpContext tokens — Per-request metadata using HttpContextToken

NEW: AbortSignal support — Request cancellation with timeout support

DEPRECATED: Class-based HttpInterceptor — Migrate to functional interceptors

Best Practices
Use functional interceptors
// ✅ Modern functional interceptor
export const authInterceptor: HttpInterceptorFn = (req, next) => {
  const authService = inject(AuthService);
  const token = authService.getToken();
  
  if (token) {
    const authReq = req.clone({
      setHeaders: { Authorization: `Bearer ${token}` }
    });
    return next(authReq);
  }
  return next(req);
};

// Register
export const appConfig: ApplicationConfig = {
  providers: [
    provideHttpClient(withInterceptors([authInterceptor]))
  ]
};

Use interceptors for cross-cutting concerns — Authentication, logging, error handling
// Error interceptor with retry
export const errorInterceptor: HttpInterceptorFn = (req, next) => {
  return next(req).pipe(
    catchError((error: HttpErrorResponse) => {
      if (error.status === 401) {
        inject(Router).navigate(['/login']);
      }
      return throwError(() => error);
    })
  );
};

Use retry with backoff for flaky networks
import { retry, delay, catchError } from 'rxjs/operators';

http.get('/api/data').pipe(
  retry({ count: 3, delay: 1000 })
);

Use HttpContext for per-request flags
const cacheToken = new HttpContextToken<boolean>(() => false);

export const cacheInterceptor: HttpInterceptorFn = (req, next) => {
  if (req.context.get(cacheToken)) {
    // Check cache
  }
  return next(req);
};

// Usage
http.get('/api/data', {
  context: new HttpContext().set(cacheToken, true)
});

Use proper typing for HTTP responses
interface User {
  id: number;
  name: string;
}

http.get<User>('/api/user/1').subscribe(user => {
  console.log(user.name); // TypeScript knows the type
});

Use observe: 'response' for full HTTP response
http.get('/api/data', { observe: 'response' }).subscribe(response => {
  console.log(response.headers);
  console.log(response.body);
});

Handle errors globally
@Injectable()
export class GlobalErrorHandler implements ErrorHandler {
  handleError(error: Error) {
    // Log to error tracking service
    console.error(error);
  }
}

// Register
provideErrorHandler(GlobalErrorHandler)

Use withCredentials for CORS requests
http.get('/api/data', { withCredentials: true });

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