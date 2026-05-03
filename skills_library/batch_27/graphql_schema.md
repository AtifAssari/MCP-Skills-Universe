---
title: graphql-schema
url: https://skills.sh/chriswiles/claude-code-showcase/graphql-schema
---

# graphql-schema

skills/chriswiles/claude-code-showcase/graphql-schema
graphql-schema
Installation
$ npx skills add https://github.com/chriswiles/claude-code-showcase --skill graphql-schema
SKILL.md
GraphQL Schema Patterns
Core Rules
NEVER inline gql literals - Create .gql files
ALWAYS run codegen after creating/modifying .gql files
ALWAYS add onError handler to mutations
Use generated hooks - Never write raw Apollo hooks
File Structure
src/
├── components/
│   └── ItemList/
│       ├── ItemList.tsx
│       ├── GetItems.gql           # Query definition
│       └── GetItems.generated.ts  # Auto-generated (don't edit)
└── graphql/
    └── mutations/
        └── CreateItem.gql         # Shared mutations

Creating a Query
Step 1: Create .gql file
# src/components/ItemList/GetItems.gql
query GetItems($limit: Int, $offset: Int) {
  items(limit: $limit, offset: $offset) {
    id
    name
    description
    createdAt
  }
}

Step 2: Run codegen
npm run gql:typegen

Step 3: Import and use generated hook
import { useGetItemsQuery } from './GetItems.generated';

const ItemList = () => {
  const { data, loading, error, refetch } = useGetItemsQuery({
    variables: { limit: 20, offset: 0 },
  });

  if (error) return <ErrorState error={error} onRetry={refetch} />;
  if (loading && !data) return <LoadingSkeleton />;
  if (!data?.items.length) return <EmptyState />;

  return <List items={data.items} />;
};

Creating a Mutation
Step 1: Create .gql file
# src/graphql/mutations/CreateItem.gql
mutation CreateItem($input: CreateItemInput!) {
  createItem(input: $input) {
    id
    name
    description
  }
}

Step 2: Run codegen
npm run gql:typegen

Step 3: Use with REQUIRED error handling
import { useCreateItemMutation } from 'graphql/mutations/CreateItem.generated';

const CreateItemForm = () => {
  const [createItem, { loading }] = useCreateItemMutation({
    // Success handling
    onCompleted: (data) => {
      toast.success({ title: 'Item created' });
      navigation.goBack();
    },
    // ERROR HANDLING IS REQUIRED
    onError: (error) => {
      console.error('createItem failed:', error);
      toast.error({ title: 'Failed to create item' });
    },
    // Cache update
    update: (cache, { data }) => {
      if (data?.createItem) {
        cache.modify({
          fields: {
            items: (existing = []) => [...existing, data.createItem],
          },
        });
      }
    },
  });

  return (
    <Button
      onPress={() => createItem({ variables: { input: formValues } })}
      isDisabled={!isValid || loading}
      isLoading={loading}
    >
      Create
    </Button>
  );
};

Mutation UI Requirements

CRITICAL: Every mutation trigger must:

Be disabled during mutation - Prevent double-clicks
Show loading state - Visual feedback
Have onError handler - User knows it failed
Show success feedback - User knows it worked
// CORRECT - Complete mutation pattern
const [submit, { loading }] = useSubmitMutation({
  onError: (error) => {
    console.error('submit failed:', error);
    toast.error({ title: 'Save failed' });
  },
  onCompleted: () => {
    toast.success({ title: 'Saved' });
  },
});

<Button
  onPress={handleSubmit}
  isDisabled={!isValid || loading}
  isLoading={loading}
>
  Submit
</Button>

Query Options
Fetch Policies
Policy	Use When
cache-first	Data rarely changes
cache-and-network	Want fast + fresh (default)
network-only	Always need latest
no-cache	Never cache (rare)
Common Options
useGetItemsQuery({
  variables: { id: itemId },

  // Fetch strategy
  fetchPolicy: 'cache-and-network',

  // Re-render on network status changes
  notifyOnNetworkStatusChange: true,

  // Skip if condition not met
  skip: !itemId,

  // Poll for updates
  pollInterval: 30000,
});

Optimistic Updates

For instant UI feedback:

const [toggleFavorite] = useToggleFavoriteMutation({
  optimisticResponse: {
    toggleFavorite: {
      __typename: 'Item',
      id: itemId,
      isFavorite: !currentState,
    },
  },
  onError: (error) => {
    // Rollback happens automatically
    console.error('toggleFavorite failed:', error);
    toast.error({ title: 'Failed to update' });
  },
});

When NOT to Use Optimistic Updates
Operations that can fail validation
Operations with server-generated values
Destructive operations (delete)
Operations affecting other users
Fragments

For reusable field selections:

# src/graphql/fragments/ItemFields.gql
fragment ItemFields on Item {
  id
  name
  description
  createdAt
  updatedAt
}


Use in queries:

query GetItems {
  items {
    ...ItemFields
  }
}

Anti-Patterns
// WRONG - Inline gql
const GET_ITEMS = gql`
  query GetItems { items { id } }
`;

// CORRECT - Use .gql file + generated hook
import { useGetItemsQuery } from './GetItems.generated';


// WRONG - No error handler
const [mutate] = useMutation(MUTATION);

// CORRECT - Always handle errors
const [mutate] = useMutation(MUTATION, {
  onError: (error) => {
    console.error('mutation failed:', error);
    toast.error({ title: 'Operation failed' });
  },
});


// WRONG - Button not disabled during mutation
<Button onPress={submit}>Submit</Button>

// CORRECT - Disabled and loading
<Button onPress={submit} isDisabled={loading} isLoading={loading}>
  Submit
</Button>

Codegen Commands
# Generate types from .gql files
npm run gql:typegen

# Download schema + generate types
npm run sync-types

Integration with Other Skills
react-ui-patterns: Loading/error/empty states for queries
testing-patterns: Mock generated hooks in tests
formik-patterns: Mutation submission patterns
Weekly Installs
35
Repository
chriswiles/clau…showcase
GitHub Stars
5.9K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass