---
rating: ⭐⭐⭐
title: fullstack-workflow
url: https://skills.sh/elie222/inbox-zero/fullstack-workflow
---

# fullstack-workflow

skills/elie222/inbox-zero/fullstack-workflow
fullstack-workflow
Installation
$ npx skills add https://github.com/elie222/inbox-zero --skill fullstack-workflow
SKILL.md
Fullstack Workflow

Complete guide for building features from API to UI, combining GET API routes, data fetching, form handling, and server actions.

Overview

When building a new feature, follow this pattern:

GET API Route - For fetching data
Server Action - For mutations (create/update/delete)
Data Fetching - Using SWR on the client
Form Handling - Using React Hook Form with Zod validation
1. GET API Route

For fetching data. Always wrap with withAuth or withEmailAccount:

// apps/web/app/api/user/example/route.ts
import { NextResponse } from "next/server";
import prisma from "@/utils/prisma";
import { withEmailAccount } from "@/utils/middleware";

// Auto-generate response type for client use
export type GetExampleResponse = Awaited<ReturnType<typeof getData>>;

export const GET = withEmailAccount(async (request) => {
  const { emailAccountId } = request.auth;
  
  const result = await getData({ emailAccountId });
  return NextResponse.json(result);
});

// We make this its own function so we can infer the return type for a type-safe response on the client
async function getData({ emailAccountId }: { emailAccountId: string }) {
  const items = await prisma.example.findMany({
    where: { emailAccountId },
  });

  return { items };
}

2. Server Action

For mutations. Use next-safe-action with proper validation.

Action clients (defined in apps/web/utils/actions/safe-action.ts):

Client	Context	Use when
actionClientUser	ctx.userId	Only need authenticated user
actionClient	ctx.emailAccountId, ctx.userId	Need user + email account (most mutations)
adminActionClient	ctx.logger	Admin-only actions (no userId in ctx)

Always use .metadata({ name: "actionName" }) for Sentry instrumentation. Use SafeError for expected errors.

Validation Schema (apps/web/utils/actions/example.validation.ts):

import { z } from "zod";

export const createExampleBody = z.object({
  name: z.string().min(1, "Name is required"),
  email: z.string().email("Invalid email"),
  description: z.string().optional(),
});
export type CreateExampleBody = z.infer<typeof createExampleBody>;

export const updateExampleBody = z.object({
  id: z.string(),
  name: z.string().optional(),
  email: z.string().email().optional(),
  description: z.string().optional(),
});
export type UpdateExampleBody = z.infer<typeof updateExampleBody>;


Server Action (apps/web/utils/actions/example.ts):

"use server";

import { actionClient } from "@/utils/actions/safe-action";
import { createExampleBody, updateExampleBody } from "@/utils/actions/example.validation";
import prisma from "@/utils/prisma";

export const createExampleAction = actionClient
  .metadata({ name: "createExample" })
  .inputSchema(createExampleBody)
  .action(async ({ 
    ctx: { emailAccountId }, 
    parsedInput: { name, email, description } 
  }) => {
    const example = await prisma.example.create({
      data: {
        name,
        email,
        description,
        emailAccountId,
      },
    });
    
    return example;
  });

export const updateExampleAction = actionClient
  .metadata({ name: "updateExample" })
  .inputSchema(updateExampleBody)
  .action(async ({ 
    ctx: { emailAccountId }, 
    parsedInput: { id, name, email, description } 
  }) => {
    const example = await prisma.example.update({
      where: { id, emailAccountId },
      data: { name, email, description },
    });
    
    return example;
  });

3. Data Fetching

Use SWR for client-side data fetching:

import useSWR from "swr";
import { GetExampleResponse } from "@/app/api/user/example/route";

export function useExamples() {
  return useSWR<GetExampleResponse>("/api/user/example");
}

4. Form Handling

Use React Hook Form with useAction from next-safe-action/hooks:

import { useCallback } from "react";
import { useForm, type SubmitHandler } from "react-hook-form";
import { useAction } from "next-safe-action/hooks";
import { zodResolver } from "@hookform/resolvers/zod";
import { Input } from "@/components/Input";
import { Button } from "@/components/ui/button";
import { toastSuccess, toastError } from "@/components/Toast";
import { getActionErrorMessage } from "@/utils/error";
import { createExampleAction } from "@/utils/actions/example";
import { createExampleBody, type CreateExampleBody } from "@/utils/actions/example.validation";

export function ExampleForm({ onSuccess }: { onSuccess?: () => void }) {
  const {
    register,
    handleSubmit,
    formState: { errors },
    reset,
  } = useForm<CreateExampleBody>({
    resolver: zodResolver(createExampleBody),
  });

  const { execute, isExecuting } = useAction(createExampleAction, {
    onSuccess: () => {
      toastSuccess({ description: "Example created!" });
      reset();
      onSuccess?.();
    },
    onError: (error) => {
      toastError({
        description: getActionErrorMessage(error.error),
      });
    },
  });

  return (
    <form className="space-y-4" onSubmit={handleSubmit(execute)}>
      <Input
        type="text"
        name="name"
        label="Name"
        registerProps={register("name")}
        error={errors.name}
      />
      <Input
        type="email"
        name="email"
        label="Email"
        registerProps={register("email")}
        error={errors.email}
      />
      <Input
        type="text"
        name="description"
        label="Description"
        registerProps={register("description")}
        error={errors.description}
      />
      <Button type="submit" loading={isExecuting}>
        Create Example
      </Button>
    </form>
  );
}

5. Complete Data Fetching Component
'use client';

import { useExamples } from "@/hooks/useExamples";
import { Button } from "@/components/ui/button";
import { LoadingContent } from "@/components/LoadingContent";

export function Examples() {
  const { data, isLoading, error } = useExamples();

  return (
    <LoadingContent loading={isLoading} error={error}>
      <div className="grid gap-4">
        {data?.examples.map((example) => (
          <div key={example.id} className="border p-4 rounded">
            <h3 className="font-semibold">{example.name}</h3>
            <p className="text-gray-600">{example.email}</p>
            {example.description && (
              <p className="text-sm text-gray-500">{example.description}</p>
            )}
          </div>
        ))}
      </div>
    </LoadingContent>
  );
}

Key Guidelines
Authentication & Authorization
Use withAuth for user-level operations
Use withEmailAccount for email-account-level operations
Server actions automatically get the right context
Mutations
Use server actions for all mutations (create/update/delete operations)
Do NOT use POST API routes for mutations - use server actions instead
Error Handling
Use useAction hook with onSuccess and onError callbacks
Use getActionErrorMessage(error.error) from @/utils/error to extract user-friendly messages
For prefix + error pattern: getActionErrorMessage(error.error, { prefix: "Failed to save" })
next-safe-action provides centralized error handling with flattened validation errors
No need for try/catch in GET routes when using middleware
Type Safety
Export response types from GET routes
Use Zod schemas for validation on both client and server
Leverage TypeScript inference for better DX
Loading and Error States
Use LoadingContent component to handle loading and error states consistently
Pass loading, error, and children props to LoadingContent
This provides a standardized way to show loading spinners and error messages
Performance
Use SWR for efficient data fetching and caching
Call mutate() after successful mutations to refresh data
File Organization
apps/web/
├── app/api/user/example/route.ts          # GET API route
├── utils/actions/example.validation.ts    # Zod schemas
├── utils/actions/example.ts               # Server actions
├── hooks/useExamples.ts                   # SWR hook
└── components/ExampleForm.tsx              # Form component

Related Rules
GET API Route Guidelines
Data Fetching with SWR
Form Handling
Server Actions
Weekly Installs
21
Repository
elie222/inbox-zero
GitHub Stars
10.6K
First Seen
Mar 10, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass