---
title: angular-schematics
url: https://skills.sh/oguzhan18/angular-ecosystem-skills/angular-schematics
---

# angular-schematics

skills/oguzhan18/angular-ecosystem-skills/angular-schematics
angular-schematics
Installation
$ npx skills add https://github.com/oguzhan18/angular-ecosystem-skills --skill angular-schematics
SKILL.md
Angular Schematics

Version: Angular 21 (2025) Tags: Schematics, Generators, CLI, Code Generation

References: Schematics Guide • @schematics/angular

Best Practices
Create schematic
npm install -g @angular-devkit/schematics-cli
schematics schematics .:my-schematic

Create rule
import { Rule, SchematicContext, Tree } from '@angular-devkit/schematics';

export function myScheme(options: any): Rule {
  return (tree: Tree, context: SchematicContext) => {
    tree.create(options.path + '/file.ts', 'content');
    return tree;
  };
}

Use templates
import { apply, url, template } from '@angular-devkit/schematics';

export function myScheme(options: any): Rule {
  const templateSource = apply(url('./files'), [
    template({ ...options }),
    move(options.path)
  ]);
  return chain([mergeWith(templateSource)]);
}

Weekly Installs
121
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