---
rating: ⭐⭐
title: next-intl-i18n
url: https://skills.sh/canatufkansu/claude-skills/next-intl-i18n
---

# next-intl-i18n

skills/canatufkansu/claude-skills/next-intl-i18n
next-intl-i18n
Installation
$ npx skills add https://github.com/canatufkansu/claude-skills --skill next-intl-i18n
SKILL.md
next-intl i18n
Configuration
// i18n.config.ts
export const locales = ['pt-PT', 'en', 'tr', 'es', 'fr', 'de'] as const;
export type Locale = (typeof locales)[number];
export const defaultLocale: Locale = 'pt-PT';

// i18n/request.ts
import { getRequestConfig } from 'next-intl/server';
import { locales, type Locale } from '@/i18n.config';

export default getRequestConfig(async ({ requestLocale }) => {
  let locale = await requestLocale;
  
  if (!locale || !locales.includes(locale as Locale)) {
    locale = 'pt-PT';
  }

  return {
    locale,
    messages: (await import(`@/messages/${locale}.json`)).default,
  };
});

Middleware
// middleware.ts
import createMiddleware from 'next-intl/middleware';
import { locales, defaultLocale } from '@/i18n.config';

export default createMiddleware({
  locales,
  defaultLocale,
  localePrefix: 'always',
});

export const config = {
  matcher: ['/', '/(pt-PT|en|tr|es|fr|de)/:path*'],
};

Message Files Structure
messages/
├── pt-PT.json
├── en.json
├── tr.json
├── es.json
├── fr.json
└── de.json

// messages/en.json
{
  "nav": {
    "home": "Home",
    "about": "About",
    "services": "Services",
    "book": "Book a Session"
  },
  "hero": {
    "title": "Pilates & Yoga for strength and calm",
    "subtitle": "Transform your body and mind with personalized coaching",
    "cta": "Book Now"
  },
  "common": {
    "learnMore": "Learn More",
    "readMore": "Read More"
  },
  "form": {
    "name": "Name",
    "email": "Email",
    "message": "Message",
    "submit": "Submit",
    "errors": {
      "required": "This field is required",
      "email": "Please enter a valid email"
    }
  }
}

Server Components
// app/[locale]/page.tsx
import { getTranslations, setRequestLocale } from 'next-intl/server';

type Props = {
  params: Promise<{ locale: string }>;
};

export default async function HomePage({ params }: Props) {
  const { locale } = await params;
  setRequestLocale(locale); // Required for static rendering
  
  const t = await getTranslations('hero');
  
  return (
    <div>
      <h1>{t('title')}</h1>
      <p>{t('subtitle')}</p>
      <button>{t('cta')}</button>
    </div>
  );
}

Client Components
'use client';

import { useTranslations } from 'next-intl';

export function ContactForm() {
  const t = useTranslations('form');
  
  return (
    <form>
      <label>{t('name')}</label>
      <input placeholder={t('name')} />
      <button type="submit">{t('submit')}</button>
    </form>
  );
}

Interpolation & Plurals
// messages/en.json
{
  "greeting": "Hello, {name}!",
  "items": "You have {count, plural, =0 {no items} =1 {one item} other {# items}}",
  "date": "Last updated: {date, date, medium}"
}

const t = useTranslations();
t('greeting', { name: 'Maria' }); // "Hello, Maria!"
t('items', { count: 5 }); // "You have 5 items"

Language Switcher
'use client';

import { useLocale } from 'next-intl';
import { usePathname, useRouter } from 'next/navigation';
import { locales, type Locale } from '@/i18n.config';

const labels: Record<Locale, string> = {
  'pt-PT': 'PT',
  'en': 'EN',
  'tr': 'TR',
  'es': 'ES',
  'fr': 'FR',
  'de': 'DE',
};

export function LanguageSwitcher() {
  const locale = useLocale();
  const pathname = usePathname();
  const router = useRouter();

  const switchLocale = (newLocale: Locale) => {
    // Replace current locale in path
    const newPath = pathname.replace(`/${locale}`, `/${newLocale}`);
    router.push(newPath);
  };

  return (
    <select
      value={locale}
      onChange={(e) => switchLocale(e.target.value as Locale)}
    >
      {locales.map((loc) => (
        <option key={loc} value={loc}>
          {labels[loc]}
        </option>
      ))}
    </select>
  );
}

Static Generation
// app/[locale]/layout.tsx
import { locales } from '@/i18n.config';

export function generateStaticParams() {
  return locales.map((locale) => ({ locale }));
}

Localized Metadata
import { getTranslations } from 'next-intl/server';
import type { Metadata } from 'next';

type Props = {
  params: Promise<{ locale: string }>;
};

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { locale } = await params;
  const t = await getTranslations({ locale, namespace: 'meta' });

  return {
    title: t('title'),
    description: t('description'),
    alternates: {
      canonical: `/${locale}`,
      languages: {
        'pt-PT': '/pt-PT',
        'en': '/en',
        'tr': '/tr',
        'es': '/es',
        'fr': '/fr',
        'de': '/de',
      },
    },
  };
}

Best Practices
Always call setRequestLocale() at the start of Server Components for static rendering
Namespace translations by feature (nav, hero, form, footer)
Keep keys consistent across all locale files
Use interpolation for dynamic values, never concatenate strings
Preserve path when switching locales
Weekly Installs
41
Repository
canatufkansu/cl…e-skills
GitHub Stars
2
First Seen
Feb 12, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass