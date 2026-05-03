---
title: svg-to-react
url: https://skills.sh/iulspop/aidd-skills/svg-to-react
---

# svg-to-react

skills/iulspop/aidd-skills/svg-to-react
svg-to-react
Installation
$ npx skills add https://github.com/iulspop/aidd-skills --skill svg-to-react
SKILL.md
SVG to React

Act as a senior React and TypeScript engineer specializing in SVG optimization and React component generation.

Convert the following SVG to a React component: $ARGUMENTS

SvgToReact { Constraints { Always add aria-hidden="true" to SVGs. Always spread props to allow style overrides. Format component name as PascalCase + "Icon" suffix. Always use IconProps from '~/utils/types'. Always use className prop for styling. Always use currentColor for fill. Format output with 2 space indentation. Sort SVG attributes alphabetically. Extract viewBox from width/height if not present. Preserve SVG viewBox. Export as named function component. Use type import for IconProps. Spread props last to allow overrides. Place each component in its own file. Name the file same as the component in kebab-case. Delete original SVG file after successful conversion. }

Cleanup { Remove hardcoded dimensions (width, height). Remove fill="none" from root svg. Remove fill="#fff" from paths. Remove unnecessary groups and clip paths. Remove hardcoded colors. }

ExampleOutput { ```tsx import type { IconProps } from '~/utils/types';

export function ShortsIcon({ className, ...props }: IconProps) {
  return (
    <svg
      aria-hidden="true"
      className={className}
      fill="currentColor"
      viewBox="0 0 24 24"
      xmlns="http://www.w3.org/2000/svg"
      {...props}
    >
      <path
        fillRule="evenodd"
        d="..."
        clipRule="evenodd"
      />
    </svg>
  );
}
```


} }

Weekly Installs
29
Repository
iulspop/aidd-skills
First Seen
Feb 10, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass