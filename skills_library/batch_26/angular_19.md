---
title: angular-19
url: https://skills.sh/avvale/aurora-front/angular-19
---

# angular-19

skills/avvale/aurora-front/angular-19
angular-19
Installation
$ npx skills add https://github.com/avvale/aurora-front --skill angular-19
SKILL.md
When to Use
Implementing Angular components (detail, list, dialog)
Working with signals, resources, and reactive patterns
Creating custom pipes or directives
Setting up dependency injection
Configuring change detection strategies

Reference files (loaded on demand):

signals-api.md — Signals, inputs, outputs, model, linkedSignal, signal queries
resource-api.md — resource(), rxResource(), httpResource()
template-syntax.md — @let, @if/@for/@switch, @defer, hydration
Angular 19 Key Changes
Standalone by Default (BREAKING)

All components, directives, and pipes are standalone by default. No standalone: true needed.

// ✅ Angular 19: standalone is implicit
@Component({
    selector: 'app-example',
    templateUrl: './example.component.html',
    imports: [CommonModule, MatButtonModule],
})
export class ExampleComponent {}

// ❌ Only if you NEED NgModule (legacy)
@Component({ selector: 'app-legacy', standalone: false })
export class LegacyComponent {}

Signals (Stable in v19) — Quick Reference
import { signal, computed, effect } from '@angular/core';

count = signal(0);                                    // Writable
doubleCount = computed(() => this.count() * 2);       // Derived read-only

this.count.set(5);           // Replace
this.count.update(n => n + 1); // Update
const val = this.count();    // Read

// Effect — can set signals directly in v19 (no allowSignalWrites needed)
effect(() => {
    console.log('Count:', this.count());
    this.logCount.set(this.count()); // ✅ allowed in v19
});


For full signal API (inputs, outputs, model, linkedSignal, queries) → see signals-api.md

Dependency Injection (Modern)
export class MyComponent {
    // ✅ Preferred: inject() function
    private readonly http = inject(HttpClient);
    private readonly router = inject(Router);
    private readonly logger = inject(LoggerService, { optional: true });
    private readonly config = inject(CONFIG_TOKEN, { self: true });
}

// Tree-shakable singleton
@Injectable({ providedIn: 'root' })
export class UserService {}

// ✅ New in v19: provideAppInitializer
providers: [
    provideAppInitializer(() => {
        const config = inject(ConfigService);
        return config.load();
    }),
]

RxJS Interop
import { toSignal, toObservable } from '@angular/core/rxjs-interop';
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';

// Observable → Signal (with custom equality in v19)
arraySignal = toSignal(this.array$, {
    initialValue: [],
    equal: (a, b) => a.length === b.length && a.every((v, i) => v === b[i]),
});

// Signal → Observable
count$ = toObservable(this.count);

// Auto-unsubscribe on destroy
this.data$.pipe(takeUntilDestroyed()).subscribe(data => { /* ... */ });

Lifecycle & Rendering (v19)
import { afterRenderEffect, afterRender, afterNextRender } from '@angular/core';

// afterRenderEffect — tracks dependencies, reruns when they change
afterRenderEffect(() => {
    const el = this.chartEl().nativeElement;
    this.renderChart(el, this.data());
});

// afterRender — every render cycle
afterRender(() => this.updateScrollPosition());

// afterNextRender — once after next render
afterNextRender(() => this.initializeThirdPartyLib());

Pipes & Directives
// Pure Pipe (default)
@Pipe({ name: 'dateFormat' })
export class DateFormatPipe implements PipeTransform {
    transform(timestamp: string, format: string): string {
        return dateFromFormat(timestamp, 'YYYY-MM-DD HH:mm:ss').format(format);
    }
}

// Attribute Directive with signal input
@Directive({ selector: '[auFocus]' })
export class FocusDirective {
    private readonly elementRef = inject(ElementRef<HTMLElement>);
    focused = input(true, { alias: 'auFocus', transform: booleanAttribute });

    constructor() {
        effect(() => {
            if (this.focused()) this.elementRef.nativeElement.focus();
        });
    }
}

Anti-Patterns
Avoid	Do Instead
standalone: true (redundant in v19)	Omit (standalone by default)
@Input() decorator	input() / input.required()
@Output() decorator	output()
@ViewChild() decorator	viewChild() / viewChild.required()
allowSignalWrites in effect	Not needed in v19
Manual subscription cleanup	takeUntilDestroyed()
ChangeDetectionStrategy.Default	Use OnPush with signals
ngOnInit for async data	resource() / rxResource()
Constructor injection (verbose)	inject() function
APP_INITIALIZER token	provideAppInitializer()
Related Skills
Skill	When to Use Together
angular-material	Material components, CDK, theming
tailwind	Styling with Tailwind CSS
typescript	TypeScript patterns, generics, type safety
aurora-schema	When working with Aurora YAML schemas
Resources
Angular 19 Official Blog
Angular Signals Guide
Resource API Guide
Weekly Installs
17
Repository
avvale/aurora-front
First Seen
Jan 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass