---
rating: ⭐⭐
title: gs-tanstack-react-query
url: https://skills.sh/gilbertopsantosjr/fullstacknextjs/gs-tanstack-react-query
---

# gs-tanstack-react-query

skills/gilbertopsantosjr/fullstacknextjs/gs-tanstack-react-query
gs-tanstack-react-query
Installation
$ npx skills add https://github.com/gilbertopsantosjr/fullstacknextjs --skill gs-tanstack-react-query
SKILL.md
TanStack React Query (Clean Architecture)
Data Flow with DTOs
useServerActionQuery → Server Action → Use Case → DTO


All query responses are DTOs, not Entities. TypeScript types should reflect this.

Core Hooks
import {
  useServerActionQuery,
  useServerActionMutation,
  useServerActionInfiniteQuery,
} from '@saas4dev/core'

import { useQueryClient } from '@tanstack/react-query'

Query with DTO Types
import type { CategoryDTO } from '@/features/category'
import { listCategoriesAction, getCategoryAction } from '@/features/category'

// List query - returns CategoryDTO[]
const { data, isLoading } = useServerActionQuery(listCategoriesAction, {
  input: { status: 'active' },
  queryKey: ['categories', 'list', { status: 'active' }],
})

// data.items is CategoryDTO[]

// Single item query
const { data: category } = useServerActionQuery(getCategoryAction, {
  input: { id },
  queryKey: ['categories', 'detail', id],
})

// category is CategoryDTO

Mutation with Invalidation
import { createCategoryAction } from '@/features/category'

const queryClient = useQueryClient()

const mutation = useServerActionMutation(createCategoryAction, {
  onSuccess: () => {
    queryClient.invalidateQueries({ queryKey: ['categories'] })
    toast.success('Category created')
  },
  onError: (error) => toast.error(error.message),
})

// Usage
mutation.mutate({ name: 'New Category' })

Query Key Pattern
// Hierarchical keys for precise invalidation
['categories']                           // All categories
['categories', 'list']                   // All lists
['categories', 'list', { status }]       // Filtered list
['categories', 'detail', id]             // Single item

Query Key Factory
export const categoryKeys = {
  all: ['categories'] as const,
  lists: () => [...categoryKeys.all, 'list'] as const,
  list: (filters: { status?: string }) => [...categoryKeys.lists(), filters] as const,
  details: () => [...categoryKeys.all, 'detail'] as const,
  detail: (id: string) => [...categoryKeys.details(), id] as const,
}

Optimistic Update
const mutation = useServerActionMutation(updateCategoryAction, {
  onMutate: async (newData) => {
    await queryClient.cancelQueries({ queryKey: ['categories', 'detail', newData.id] })
    const previous = queryClient.getQueryData<CategoryDTO>(['categories', 'detail', newData.id])

    queryClient.setQueryData<CategoryDTO>(
      ['categories', 'detail', newData.id],
      (old) => old ? { ...old, ...newData } : old
    )

    return { previous }
  },
  onError: (err, newData, context) => {
    if (context?.previous) {
      queryClient.setQueryData(['categories', 'detail', newData.id], context.previous)
    }
  },
  onSettled: (_, __, variables) => {
    queryClient.invalidateQueries({ queryKey: ['categories', 'detail', variables.id] })
  },
})

Pagination
const { data, fetchNextPage, hasNextPage } = useServerActionInfiniteQuery(
  listCategoriesAction,
  {
    queryKey: ['categories', 'list'],
    getNextPageParam: (lastPage) => lastPage.nextCursor,
    initialPageParam: undefined,
    input: ({ pageParam }) => ({ cursor: pageParam, limit: 20 }),
  }
)

// data.pages[].items is CategoryDTO[]

Best Practices
Type with DTOs - useQueryData<CategoryDTO>() not Category
Actions only - Never call Use Cases from components
Hierarchical keys - Invalidate broadly, fetch specifically
Error handling - Show domain exception messages
Optimistic updates - Always implement rollback
References
Web Client: skills/nextjs-web-client/SKILL.md
Server Actions: skills/nextjs-server-actions/SKILL.md
Weekly Installs
9
Repository
gilbertopsantos…cknextjs
GitHub Stars
1
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass