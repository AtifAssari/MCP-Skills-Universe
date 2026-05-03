---
title: filter-sphere
url: https://skills.sh/lawvs/fn-sphere/filter-sphere
---

# filter-sphere

skills/lawvs/fn-sphere/filter-sphere
filter-sphere
Installation
$ npx skills add https://github.com/lawvs/fn-sphere --skill filter-sphere
SKILL.md
Filter Sphere - Schema-driven Filtering

Build advanced filtering interfaces powered by Zod schemas.

Quick Start
# React filter UI
pnpm add @fn-sphere/filter zod

Core Concepts
Basic Setup
import {
  FilterSphereProvider,
  FilterBuilder,
  useFilterSphere,
} from "@fn-sphere/filter";
import { z } from "zod";

// 1. Define your data schema with Zod
const schema = z.object({
  name: z.string().describe("Name"),
  age: z.number().describe("Age"),
});

export function FilterBuilder() {
  // 2. use the `useFilterSphere` hook to get the context and predicate
  const { filterRule, predicate, context } = useFilterSphere({
    schema,
    onRuleChange: ({ filterRule }) => {
      console.log("Filter rule changed:", filterRule);
    },
  });

  const data = [
    /* ... */
  ];

  // 4. use the `predicate` to filter the data
  const filteredData = data.filter(predicate);

  return (
    // 3. display the `FilterBuilder` inside the `FilterSphereProvider`
    <FilterSphereProvider context={context}>
      <FilterBuilder />
    </FilterSphereProvider>
  );
}

Project Structure (Recommended)
filter-sphere/
  index.tsx      # Main component wiring everything together
  schema.ts      # Zod schema, default rules, custom functions
  theme.tsx      # Theme via createFilterTheme
  locale.ts      # (Optional) i18n with getLocaleText

Core References
Topic	Reference
Introduction	Introduction
Getting Started	Getting Started
Best Practices	Best Practices
Work with AI	Work with AI
Customizing Filters	Customizing Filters
Customizing Theme	Customizing Theme
Customizing Data Input	Data Input
Persistence	Persistence
Preset Filters	Preset Filters
Example	Example
Resources
Repository: https://github.com/lawvs/fn-sphere
Documentation: https://www.waterwater.moe/fn-sphere/
Weekly Installs
11
Repository
lawvs/fn-sphere
GitHub Stars
32
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass