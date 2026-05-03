---
title: tanstack query v5
url: https://skills.sh/slanycukr/riot-api-project/tanstack-query-v5
---

# tanstack query v5

skills/slanycukr/riot-api-project/TanStack Query v5
TanStack Query v5
Installation
$ npx skills add https://github.com/slanycukr/riot-api-project --skill 'TanStack Query v5'
SKILL.md
TanStack Query v5
Quick start
npm install @tanstack/react-query
# or
yarn add @tanstack/react-query
# or
pnpm add @tanstack/react-query

// providers.tsx
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";

const queryClient = new QueryClient();

export function Providers({ children }: { children: React.ReactNode }) {
  return (
    <QueryClientProvider client={queryClient}>{children}</QueryClientProvider>
  );
}

// Basic usage
import { useQuery } from "@tanstack/react-query";

function Users() {
  const { data, isLoading, error } = useQuery({
    queryKey: ["users"],
    queryFn: () => fetch("/api/users").then((res) => res.json()),
  });

  if (isLoading) return "Loading...";
  if (error) return "An error occurred";

  return <div>{JSON.stringify(data)}</div>;
}

Common patterns
Data fetching with loading states
function UserProfile({ userId }: { userId: string }) {
  const {
    data: user,
    isLoading,
    error,
  } = useQuery({
    queryKey: ["user", userId],
    queryFn: () => fetchUser(userId),
    enabled: !!userId,
  });

  if (isLoading) return <Skeleton />;
  if (error) return <ErrorMessage error={error} />;
  if (!user) return null;

  return <UserCard user={user} />;
}

Mutations with optimistic updates
function LikeButton({ postId }: { postId: string }) {
  const queryClient = useQueryClient();

  const mutation = useMutation({
    mutationFn: () => toggleLike(postId),
    onMutate: async () => {
      await queryClient.cancelQueries({ queryKey: ["posts"] });
      const previousPosts = queryClient.getQueryData(["posts"]);
      queryClient.setQueryData(["posts"], (old: any[]) =>
        old?.map((post) =>
          post.id === postId ? { ...post, likes: post.likes + 1 } : post,
        ),
      );
      return { previousPosts };
    },
    onError: (err, _, context) => {
      queryClient.setQueryData(["posts"], context?.previousPosts);
    },
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ["posts"] });
    },
  });

  return (
    <button onClick={() => mutation.mutate()}>
      ❤️ {mutation.isPending ? "..." : "Like"}
    </button>
  );
}

Pagination
function PaginatedPosts() {
  const [page, setPage] = useState(1);

  const { data, isLoading, isPlaceholderData } = useQuery({
    queryKey: ["posts", page],
    queryFn: () => fetchPosts(page),
    placeholderData: keepPreviousData,
  });

  return (
    <div>
      {data?.posts.map((post) => (
        <Post key={post.id} post={post} />
      ))}
      <button
        onClick={() => setPage((p) => p - 1)}
        disabled={page === 1 || isLoading}
      >
        Previous
      </button>
      <button
        onClick={() => setPage((p) => p + 1)}
        disabled={!data?.hasNextPage || isLoading}
      >
        Next
      </button>
    </div>
  );
}

Infinite scroll
function InfinitePosts() {
  const { data, fetchNextPage, hasNextPage, isFetchingNextPage } =
    useInfiniteQuery({
      queryKey: ["posts"],
      queryFn: ({ pageParam = 0 }) => fetchPosts(pageParam),
      getNextPageParam: (lastPage, allPages) => lastPage.nextCursor,
    });

  return (
    <div>
      {data?.pages.map((page) =>
        page.posts.map((post) => <Post key={post.id} post={post} />),
      )}
      <button
        onClick={() => fetchNextPage()}
        disabled={!hasNextPage || isFetchingNextPage}
      >
        {isFetchingNextPage ? "Loading more..." : "Load more"}
      </button>
    </div>
  );
}

Dependent queries
function UserProfile({ userId }: { userId: string }) {
  const { data: user } = useQuery({
    queryKey: ["user", userId],
    queryFn: () => fetchUser(userId),
  });

  const { data: posts } = useQuery({
    queryKey: ["posts", userId],
    queryFn: () => fetchUserPosts(userId),
    enabled: !!user?.id,
  });

  return (
    <div>
      <h1>{user?.name}</h1>
      {posts?.map((post) => (
        <Post key={post.id} post={post} />
      ))}
    </div>
  );
}

Requirements
Installation
# Core package
npm install @tanstack/react-query

# DevTools (recommended for development)
npm install @tanstack/react-query-devtools

Browser support
Supports all modern browsers
IE11+ with appropriate polyfills
React version compatibility
React 16.8+ (hooks required)
React 18+ preferred for concurrent features
TypeScript support
Built-in TypeScript definitions
Full type inference for queries and mutations
Weekly Installs
–
Repository
slanycukr/riot-…-project
GitHub Stars
2
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass