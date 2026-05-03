---
rating: ⭐⭐
title: intlayer-react
url: https://skills.sh/aymericzip/intlayer/intlayer-react
---

# intlayer-react

skills/aymericzip/intlayer/intlayer-react
intlayer-react
Installation
$ npx skills add https://github.com/aymericzip/intlayer --skill intlayer-react
SKILL.md
Intlayer React Usage
Core Philosophy

Intlayer promotes Component-Level Content Declaration. Instead of a massive global translation file, content is declared in *.content.ts files adjacent to the React components that use them.

Workflow

To create a translated component, you need two files:

Declaration: A content file (e.g., myComponent.content.ts) defining the dictionary.
Implementation: A React component (e.g., MyComponent.tsx) using the useIntlayer hook.
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
      // ... All other locales set in intlayer config file
    }),
  },
} satisfies Dictionary;

export default content;

Intlayer React Usage
Setup
Vite and React
Create React App
React Router v7
React Router v7 (fs routes)
Tanstack Start
React Native and Expo
Lynx and React
useIntlayer Hook
import { useIntlayer } from "react-intlayer";
const MyComponent = () => {
  const content = useIntlayer("my-dictionary-key");
  return (
    <div>
      <h1>
        {/* Return react node */}
        {content.text}
      </h1>
      {/* Return string (.value) */}
      <img src={content.text.value} alt={content.text.value} />
    </div>
  );
};

References
Website
Doc
Environments
Vite and React
Create React App
Vite and React (React Router v7)
Vite and React (React Router v7 FS Routes)
Packages
Intlayer Exports
React Intlayer Provider
React Intlayer MarkdownRenderer
React Intlayer Exports
React Intlayer T
React Intlayer useDictionary
React Intlayer useI18n
React Intlayer useIntlayer
React Intlayer useLocale
Weekly Installs
37
Repository
aymericzip/intlayer
GitHub Stars
692
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass