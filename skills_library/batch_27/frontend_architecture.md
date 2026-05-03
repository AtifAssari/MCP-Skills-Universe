---
title: frontend architecture
url: https://skills.sh/exceptionless/exceptionless/frontend-architecture
---

# frontend architecture

skills/exceptionless/exceptionless/frontend-architecture
frontend-architecture
Installation
$ npx skills add https://github.com/exceptionless/exceptionless --skill frontend-architecture
SKILL.md
Frontend Architecture

Located in src/Exceptionless.Web/ClientApp. The Svelte SPA is the primary client.

Directory Structure
src/
├── lib/
│   ├── features/           # Feature slices (vertical organization)
│   │   ├── auth/
│   │   │   ├── api.svelte.ts
│   │   │   ├── models/
│   │   │   ├── schemas.ts
│   │   │   └── components/
│   │   ├── organizations/
│   │   ├── projects/
│   │   ├── events/
│   │   └── shared/         # Cross-feature shared code
│   ├── components/         # App-wide shared components
│   │   └── ui/             # shadcn-svelte components
│   ├── generated/          # API-generated types
│   └── utils/              # Utility functions
├── routes/
│   ├── (app)/              # Authenticated app routes
│   ├── (auth)/             # Authentication routes
│   └── (public)/           # Public routes
└── app.html

Route Groups

Organize routes by authentication/layout requirements:

routes/
├── (app)/                  # Requires authentication
│   ├── +layout.svelte      # App layout with nav
│   ├── organizations/
│   └── projects/
├── (auth)/                 # Login/signup flows
│   ├── +layout.svelte      # Minimal auth layout
│   ├── login/
│   └── signup/
└── (public)/               # Public pages
    ├── +layout.svelte      # Marketing layout
    └── pricing/

Feature Slices

Organize by feature, aligned with API controllers:

features/organizations/
├── api.svelte.ts           # TanStack Query hooks
├── models/
│   └── index.ts            # Re-exports from generated
├── schemas.ts              # Zod validation schemas
├── options.ts              # Dropdown options, enums
└── components/
    ├── organization-card.svelte
    ├── organization-form.svelte
    └── dialogs/
        └── create-organization-dialog.svelte

API Client Pattern

Centralize API calls per feature:

// features/organizations/api.svelte.ts
import {
    createQuery,
    createMutation,
    useQueryClient,
} from "@tanstack/svelte-query";
import { useFetchClient } from "@exceptionless/fetchclient";
import type { Organization, CreateOrganizationRequest } from "./models";

export function getOrganizationsQuery() {
    const client = useFetchClient();

    return createQuery(() => ({
        queryKey: ["organizations"],
        queryFn: async () => {
            const response =
                await client.getJSON<Organization[]>("/organizations");
            if (!response.ok) throw response.problem;
            return response.data!;
        },
    }));
}

export function postOrganizationMutation() {
    const client = useFetchClient();
    const queryClient = useQueryClient();

    return createMutation(() => ({
        mutationFn: async (data: CreateOrganizationRequest) => {
            const response = await client.postJSON<Organization>(
                "/organizations",
                data,
            );
            if (!response.ok) throw response.problem;
            return response.data!;
        },
        onSuccess: () => {
            queryClient.invalidateQueries({ queryKey: ["organizations"] });
        },
    }));
}

Model Re-exports

Re-export generated models through feature model folders:

// features/organizations/models/index.ts
export type {
    Organization,
    CreateOrganizationRequest,
    UpdateOrganizationRequest,
} from "$lib/generated";

// Add feature-specific types
export interface OrganizationWithStats extends Organization {
    eventCount: number;
    projectCount: number;
}

Barrel Exports

Use index.ts for clean imports:

// features/organizations/index.ts
export { getOrganizationsQuery, postOrganizationMutation } from "./api.svelte";
export type { Organization, CreateOrganizationRequest } from "./models";
export { organizationSchema } from "./schemas";

Shared Components

Place truly shared components in appropriate locations:

lib/
├── features/shared/        # Shared between features
│   ├── components/
│   │   ├── formatters/     # Boolean, date, number, bytes, duration, currency, percentage, time-ago formatters
│   │   ├── loading/
│   │   └── error/
│   └── utils/
└── components/             # App-wide components
    ├── ui/                 # shadcn-svelte
    ├── layout/
    └── dialogs/            # Global dialogs

Formatter Components (MUST use — never write custom formatting functions)

The formatters/ directory contains Svelte components for displaying formatted values. Always use these instead of writing custom formatting functions like formatDateTime() or formatBytes().

Component	Use For
<DateTime>	Date and time display
<TimeAgo>	Relative time ("3 hours ago")
<Duration>	Time durations
<Bytes>	File sizes, memory
<Number>	Numeric values with locale formatting
<Boolean>	True/false display
<Currency>	Money amounts
<Percentage>	Percentage values
<DateMath>	Elasticsearch date math expressions
<!-- CORRECT: use the formatter component -->
<DateTime value={event.date} />
<TimeAgo value={event.date} />
<Bytes value={event.size} />

<!-- WRONG: never do this -->
{formatDateTime(event.date)}
{new Date(event.date).toLocaleString()}


Consistency rule: If a formatter component exists for a data type, you MUST use it. Creating a custom formatting function when a component already exists is a code review BLOCKER.

Generated Types

When API contracts change:

npm run generate-models


Prefer regeneration over hand-writing DTOs. Generated types live in $lib/generated.

Import Aliases
// Configured in svelte.config.js
import { Button } from "$comp/ui/button"; // $lib/components
import { User } from "$features/users/models"; // $lib/features
import { formatDate } from "$shared/formatters"; // $lib/features/shared

Consistency Rule

Before creating anything new, search the codebase for existing patterns. Consistency is the most important quality of a codebase:

Find the closest existing implementation of what you're building
Match its patterns exactly — file structure, naming, imports, component composition
Reuse shared utilities and components from $lib/features/shared/ and $comp/
If an existing utility almost does what you need, extend it — don't create a parallel one

Pattern divergence is a code review BLOCKER, not a nit.

Composite Component Pattern

Study existing components before creating new ones:

Dialogs: See /components/dialogs/
Dropdowns: Use options.ts with DropdownItem<EnumType>[]
Forms: Follow TanStack Form patterns in svelte-forms skill
Weekly Installs
11
Repository
exceptionless/e…tionless
GitHub Stars
2.5K
First Seen
Mar 15, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass