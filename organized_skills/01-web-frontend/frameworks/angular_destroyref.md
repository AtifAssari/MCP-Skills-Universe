---
rating: ⭐⭐
title: angular-destroyref
url: https://skills.sh/oguzhan18/angular-ecosystem-skills/angular-destroyref
---

# angular-destroyref

skills/oguzhan18/angular-ecosystem-skills/angular-destroyref
angular-destroyref
Installation
$ npx skills add https://github.com/oguzhan18/angular-ecosystem-skills --skill angular-destroyref
SKILL.md
Angular DestroyRef

Version: Angular 16+ (2025) Tags: DestroyRef, Cleanup, takeUntilDestroyed

References: DestroyRef

Best Practices
Use takeUntilDestroyed
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';

@Component({})
export class MyComponent {
  private destroyRef = inject(DestroyRef);
  
  ngOnInit() {
    this.data$.pipe(
      takeUntilDestroyed(this.destroyRef)
    ).subscribe();
  }
}

Use in service
@Injectable({ providedIn: 'root' })
export class DataService {
  private destroyRef = inject(DestroyRef);
  
  getData() {
    return this.http.get('/api/data').pipe(
      takeUntilDestroyed(this.destroyRef)
    );
  }
}

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