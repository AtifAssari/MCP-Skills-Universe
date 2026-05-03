---
title: graphql-design
url: https://skills.sh/rohitg00/awesome-claude-code-toolkit/graphql-design
---

# graphql-design

skills/rohitg00/awesome-claude-code-toolkit/graphql-design
graphql-design
Installation
$ npx skills add https://github.com/rohitg00/awesome-claude-code-toolkit --skill graphql-design
SKILL.md
GraphQL Design
Schema Design
type Query {
  user(id: ID!): User
  users(filter: UserFilter, first: Int = 20, after: String): UserConnection!
}

type Mutation {
  createUser(input: CreateUserInput!): CreateUserPayload!
  updateUser(id: ID!, input: UpdateUserInput!): UpdateUserPayload!
}

type Subscription {
  orderStatusChanged(orderId: ID!): Order!
}

type User {
  id: ID!
  email: String!
  name: String!
  orders(first: Int = 10, after: String): OrderConnection!
  createdAt: DateTime!
}

input CreateUserInput {
  email: String!
  name: String!
}

type CreateUserPayload {
  user: User
  errors: [UserError!]!
}

type UserError {
  field: String!
  message: String!
}

type UserConnection {
  edges: [UserEdge!]!
  pageInfo: PageInfo!
  totalCount: Int!
}

type UserEdge {
  node: User!
  cursor: String!
}

type PageInfo {
  hasNextPage: Boolean!
  endCursor: String
}


Use Relay-style connections for pagination. Return payload types from mutations with both result and errors.

Resolvers
const resolvers: Resolvers = {
  Query: {
    user: async (_, { id }, ctx) => {
      return ctx.dataloaders.user.load(id);
    },
    users: async (_, { filter, first, after }, ctx) => {
      const cursor = after ? decodeCursor(after) : undefined;
      const users = await ctx.db.user.findMany({
        where: buildFilter(filter),
        take: first + 1,
        cursor: cursor ? { id: cursor } : undefined,
        orderBy: { createdAt: "desc" },
      });

      const hasNextPage = users.length > first;
      const edges = users.slice(0, first).map(user => ({
        node: user,
        cursor: encodeCursor(user.id),
      }));

      return {
        edges,
        pageInfo: {
          hasNextPage,
          endCursor: edges[edges.length - 1]?.cursor ?? null,
        },
      };
    },
  },

  Mutation: {
    createUser: async (_, { input }, ctx) => {
      const existing = await ctx.db.user.findUnique({ where: { email: input.email } });
      if (existing) {
        return { user: null, errors: [{ field: "email", message: "Already taken" }] };
      }
      const user = await ctx.db.user.create({ data: input });
      return { user, errors: [] };
    },
  },

  User: {
    orders: async (parent, { first, after }, ctx) => {
      return ctx.dataloaders.userOrders.load({ userId: parent.id, first, after });
    },
  },
};

DataLoader for N+1 Prevention
import DataLoader from "dataloader";

function createLoaders(db: Database) {
  return {
    user: new DataLoader<string, User>(async (ids) => {
      const users = await db.user.findMany({ where: { id: { in: [...ids] } } });
      const userMap = new Map(users.map(u => [u.id, u]));
      return ids.map(id => userMap.get(id) ?? new Error(`User ${id} not found`));
    }),

    userOrders: new DataLoader<{ userId: string }, Order[]>(async (keys) => {
      const userIds = keys.map(k => k.userId);
      const orders = await db.order.findMany({
        where: { userId: { in: userIds } },
        orderBy: { createdAt: "desc" },
      });
      const grouped = new Map<string, Order[]>();
      orders.forEach(o => {
        const list = grouped.get(o.userId) ?? [];
        list.push(o);
        grouped.set(o.userId, list);
      });
      return keys.map(k => grouped.get(k.userId) ?? []);
    }),
  };
}


Create new DataLoader instances per request to avoid stale cache across users.

Subscriptions
const pubsub = new PubSub();

const resolvers = {
  Subscription: {
    orderStatusChanged: {
      subscribe: (_, { orderId }) => {
        return pubsub.asyncIterableIterator(`ORDER_STATUS_${orderId}`);
      },
    },
  },
  Mutation: {
    updateOrderStatus: async (_, { id, status }, ctx) => {
      const order = await ctx.db.order.update({ where: { id }, data: { status } });
      await pubsub.publish(`ORDER_STATUS_${id}`, { orderStatusChanged: order });
      return { order, errors: [] };
    },
  },
};

Anti-Patterns
Exposing database schema directly as GraphQL schema
Resolving nested fields without DataLoader (causes N+1 queries)
Using offset-based pagination instead of cursor-based for large datasets
Throwing raw errors from resolvers instead of returning typed error payloads
Creating a single monolithic schema file instead of modular type definitions
Allowing unbounded queries without depth or complexity limits
Checklist
 Relay-style cursor pagination for all list fields
 DataLoader used for all batched entity lookups
 Mutations return payload types with both result and error fields
 Input types used for mutation arguments
 Query depth and complexity limits configured
 DataLoader instances created per-request in context
 Schema split into domain-specific modules
 Subscriptions use filtered topics to avoid broadcasting to all clients
Weekly Installs
43
Repository
rohitg00/awesom…-toolkit
GitHub Stars
1.5K
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass