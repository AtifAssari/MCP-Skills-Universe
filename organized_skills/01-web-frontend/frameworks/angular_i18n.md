---
rating: ⭐⭐
title: angular-i18n
url: https://skills.sh/oguzhan18/angular-ecosystem-skills/angular-i18n
---

# angular-i18n

skills/oguzhan18/angular-ecosystem-skills/angular-i18n
angular-i18n
Installation
$ npx skills add https://github.com/oguzhan18/angular-ecosystem-skills --skill angular-i18n
SKILL.md
Angular i18n

Version: Angular 21 (2025) Tags: i18n, Internationalization, Localization, Translations

References: i18n Guide • Angular Localize

API Changes

This section documents recent version-specific API changes.

NEW: @angular/localize — Built-in i18n support

NEW: $localize — Message extraction

NEW: Angular CLI i18n — Multiple language builds

NEW: Lazy-loaded translations — Runtime translation loading

Best Practices
Mark text for translation
@Component({
  template: `
    <h1 i18n="@@welcome">Welcome to our app!</h1>
    <p i18n="@@greeting">Hello, world!</p>
  `
})
export class HomeComponent {}

Use translations with placeholders
@Component({
  template: `
    <p i18n="@@userCount">
      There are { count, plural, =0 { no users } =1 { one user } other { {{ count }} users } } in the system.
    </p>
  `
})
export class UsersComponent {
  count = 5;
}

Use gender-specific translations
@Component({
  template: `
    <p i18n="@@message">
      { gender, select, male {He} female {She} other {They} } is attending.
    </p>
  `
})
export class MessageComponent {}

Extract messages
ng extract-i18n --output-path src/locale

Build for multiple locales
ng build --localize

Configure locales in angular.json
{
  "projects": {
    "my-app": {
      "i18n": {
        "locales": {
          "en": "src/locale/messages.en.xlf",
          "es": "src/locale/messages.es.xlf",
          "fr": "src/locale/messages.fr.xlf"
        }
      }
    }
  }
}

Use i18n attribute for elements
@Component({
  template: `
    <img i18n-title title="Logo" src="logo.png" />
    <a i18n-href href="/about" hreflang="es">About</a>
  `
})
export class HeaderComponent {}

Use @angular/localize for runtime translations
import { $localize } from '@angular/localize';

$localize`:@@greeting:Hello, ${name}:name:World!`;

Use ngx-translate for runtime translations
// Alternative: use @ngx-translate/core
import { TranslateModule } from '@ngx-translate/core';

@NgModule({
  imports: [TranslateModule.forRoot()]
})
export class AppModule {}

Lazy load translations
// Using @ngx-translate
this.translate.getTranslation('en').subscribe(translations => {
  // Load translations
});

Weekly Installs
122
Repository
oguzhan18/angul…m-skills
GitHub Stars
6
First Seen
7 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass