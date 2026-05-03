---
title: angular-animations
url: https://skills.sh/oguzhan18/angular-ecosystem-skills/angular-animations
---

# angular-animations

skills/oguzhan18/angular-ecosystem-skills/angular-animations
angular-animations
Installation
$ npx skills add https://github.com/oguzhan18/angular-ecosystem-skills --skill angular-animations
SKILL.md
@angular/animations

Version: Angular 21 (2025) Tags: Animations, UI, Transitions, Motion

References: Animations Guide • API • npm

API Changes

This section documents recent version-specific API changes.

NEW: Modern animation API — Use animateEnter and animateLeave over deprecated :enter/:leave

NEW: CSS-based animations — Angular team recommends CSS for better performance

NEW: View transitions API — Support for browser View Transitions API

DEPRECATED: :enter and :leave — Use animateEnter and animateLeave instead

Best Practices
Enable animations module
import { provideAnimations } from '@angular/platform-browser/animations';

export const appConfig: ApplicationConfig = {
  providers: [
    provideAnimations()
  ]
};

Use triggers for state-based animations
import { trigger, state, style, transition, animate } from '@angular/animations';

@Component({
  animations: [
    trigger('fadeInOut', [
      state('hidden', style({ opacity: 0 })),
      state('visible', style({ opacity: 1 })),
      transition('hidden <=> visible', animate(500))
    ])
  ]
})
export class FadeComponent {
  isVisible = signal(false);
}

Use enter/leave animations
@Component({
  animations: [
    trigger('slideIn', [
      transition(':enter', [
        style({ transform: 'translateX(-100%)' }),
        animate('300ms ease-in', style({ transform: 'translateX(0%)' }))
      ]),
      transition(':leave', [
        animate('300ms ease-out', style({ transform: 'translateX(-100%)' }))
      ])
    ])
  ]
})
export class SlideComponent {}

Use wildcard states for any transition
trigger('expand', [
  transition('* => expanded', [
    style({ height: '*' }),
    animate('300ms ease-out', style({ height: '200px' }))
  ]),
  transition('expanded => *', [
    animate('300ms ease-in', style({ height: '*' }))
  ])
])

Use query and stagger for list animations
trigger('listAnimation', [
  transition('* => *', [
    query(':enter', [
      style({ opacity: 0 }),
      stagger(100, [
        animate('300ms', style({ opacity: 1 }))
      ])
    ], { optional: true })
  ])
])

Use animation callbacks
@Component({
  template: `
    <div [@fade]="state" 
         (@fade.start)="onAnimationStart()"
         (@fade.done)="onAnimationDone()">
    </div>
  `
})
export class AnimComponent {
  onAnimationStart() { console.log('Start'); }
  onAnimationDone() { console.log('Done'); }
}

Use reusable triggers
// animations.ts
export const fadeAnimation = trigger('fade', [
  transition(':enter', [
    style({ opacity: 0 }),
    animate('300ms', style({ opacity: 1 }))
  ]),
  transition(':leave', [
    animate('300ms', style({ opacity: 0 }))
  ])
]);

Use functional animations (Angular 17+)
@Component({
  animations: [
    trigger('expanded', [
      transition(':expanded', [
        animate('300ms cubic-bezier(0.4, 0, 0.2, 1)')
      ])
    ])
  ]
})
export class ExpandComponent {}

Optimize for performance
// Prefer transform and opacity
transition('* => *', [
  animate('200ms', style({ 
    transform: 'translateX(10px)',
    opacity: 0.5 
  }))
])

// Avoid expensive properties
// ❌ Don't animate: width, height, margin, top
// ✅ Do animate: transform, opacity

Provide reduced motion for accessibility
@Component({
  animations: [
    trigger('slide', [
      transition('* => *', [
        style({ '@.disabled': '' }), // Disable for reduced motion
        animate('300ms')
      ])
    ])
  ]
})

Weekly Installs
134
Repository
oguzhan18/angul…m-skills
GitHub Stars
6
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass