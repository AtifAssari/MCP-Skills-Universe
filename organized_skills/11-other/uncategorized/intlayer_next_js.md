---
rating: ⭐⭐
title: intlayer-next-js
url: https://skills.sh/aymericzip/intlayer-skills/intlayer-next-js
---

# intlayer-next-js

skills/aymericzip/intlayer-skills/intlayer-next-js
intlayer-next-js
Installation
$ npx skills add https://github.com/aymericzip/intlayer-skills --skill intlayer-next-js
SKILL.md
Intlayer Next.js Usage
Core Philosophy

Intlayer promotes Component-Level Content Declaration. Instead of a massive global translation file, content is declared in *.content.ts files adjacent to the Next.js components that use them.

Workflow

To create a translated component, you need two files:

Declaration: A content file (e.g., myComponent.content.ts) defining the dictionary.
Implementation: A Next.js component (Server or Client) using the useIntlayer hook.
1. Declare Content

Create a content file using t() for translations. File: src/components/MyComponent/myComponent.content.ts

import { t, type Dictionary } from "intlayer";

const content = {
  // The 'key' must be unique and matches what you pass to useIntlayer()
  key: "my-component",
  content: {
    text: t({
      en: "Welcome",
      fr: "Bienvenue",
      es: "Hola",
    }),
  },
} satisfies Dictionary;

export default content;

Setup
Next.js
Next.js 14
Next.js 15
No Locale Path
Page Router
Server Components

To use Intlayer in Server Components, use IntlayerServerProvider to provide the locale and useIntlayer from next-intlayer/server.

import { IntlayerServerProvider, useIntlayer } from "next-intlayer/server";

const MyServerComponent = () => {
  const content = useIntlayer("my-component");
  return (
    <div>
      <h1>{content.text}</h1>
    </div>
  );
};

const Page = async ({ params }) => {
  const { locale } = await params;
  return (
    <IntlayerServerProvider locale={locale}>
      <MyServerComponent />
    </IntlayerServerProvider>
  );
};

export default Page;

Client Components

For Client Components, add the "use client" directive and use useIntlayer from next-intlayer. Ensure the component is wrapped in an IntlayerClientProvider.

"use client";

import { useIntlayer } from "next-intlayer";

export const MyClientComponent = () => {
  const content = useIntlayer("my-component");

  return (
    <div>
      <h1>{content.text}</h1>
    </div>
  );
};


Next.js package Documentation

References
Website
Doc
Environments
Next.js
Next.js 14
Next.js 15
Next.js No Locale Path
Next.js with Page Router
Packages
Intlayer Exports
Next Intlayer Exports
Next Intlayer Middleware
Next Intlayer T
Next Intlayer useDictionary
Next Intlayer useIntlayer
Next Intlayer useLocale
Weekly Installs
13
Repository
aymericzip/intl…r-skills
GitHub Stars
4
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass