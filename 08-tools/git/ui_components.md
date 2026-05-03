---
title: ui-components
url: https://skills.sh/elie222/inbox-zero/ui-components
---

# ui-components

skills/elie222/inbox-zero/ui-components
ui-components
Installation
$ npx skills add https://github.com/elie222/inbox-zero --skill ui-components
SKILL.md
UI Components and Styling
UI Framework
Use Shadcn UI and Tailwind for components and styling
Implement responsive design with Tailwind CSS using a mobile-first approach
Use next/image package for images
Install new Shadcn components
pnpm dlx shadcn@latest add COMPONENT


Example:

pnpm dlx shadcn@latest add progress

Data Fetching with SWR

For API get requests to server use the swr package:

const searchParams = useSearchParams();
const page = searchParams.get("page") || "1";
const { data, isLoading, error } = useSWR<PlanHistoryResponse>(
  `/api/user/planned/history?page=${page}`
);

Loading Components

Use the LoadingContent component to handle loading states:

<Card>
  <LoadingContent loading={isLoading} error={error}>
    {data && <MyComponent data={data} />}
  </LoadingContent>
</Card>

Form Components
Text Inputs
<Input
  type="email"
  name="email"
  label="Email"
  registerProps={register("email", { required: true })}
  error={errors.email}
/>

Text Area
<Input
  type="text"
  autosizeTextarea
  rows={3}
  name="message"
  placeholder="Paste in email content"
  registerProps={register("message", { required: true })}
  error={errors.message}
/>

Weekly Installs
75
Repository
elie222/inbox-zero
GitHub Stars
10.6K
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass