---
rating: ⭐⭐⭐
title: api-layer
url: https://skills.sh/bumgeunsong/daily-writing-friends/api-layer
---

# api-layer

skills/bumgeunsong/daily-writing-friends/api-layer
api-layer
Installation
$ npx skills add https://github.com/bumgeunsong/daily-writing-friends --skill api-layer
SKILL.md
API Layer Patterns
File Location

All API functions go in [feature]/api/:

src/
├── post/
│   └── api/
│       ├── post.ts        # CRUD operations
│       └── postQueries.ts # React Query hooks

Function Structure
import { collection, addDoc, query, where, getDocs } from 'firebase/firestore';
import { db } from '@/firebase';
import type { Post } from '../model/Post';

export async function createPost(
  boardId: string,
  postData: Omit<Post, 'id' | 'createdAt'>,
): Promise<Post> {
  const postsRef = collection(db, 'boards', boardId, 'posts');
  const docRef = await addDoc(postsRef, {
    ...postData,
    createdAt: new Date(),
  });
  return { ...postData, id: docRef.id, createdAt: new Date() };
}

Firestore Best Practices
Batch Writes for Related Operations
import { writeBatch, doc } from 'firebase/firestore';

const batch = writeBatch(db);
batch.set(doc(db, 'posts', postId), postData);
batch.update(doc(db, 'users', userId), { postCount: increment(1) });
await batch.commit();

Collection Paths
users/{userId}
users/{userId}/postings/{postingId}
users/{userId}/commentings/{commentingId}
boards/{boardId}/posts/{postId}
boards/{boardId}/posts/{postId}/comments/{commentId}
boards/{boardId}/posts/{postId}/comments/{commentId}/replies/{replyId}

Optimistic Updates with React Query
const mutation = useMutation({
  mutationFn: createPost,
  onMutate: async (newPost) => {
    await queryClient.cancelQueries({ queryKey: ['posts'] });
    const previous = queryClient.getQueryData(['posts']);
    queryClient.setQueryData(['posts'], (old) => [...old, newPost]);
    return { previous };
  },
  onError: (err, newPost, context) => {
    queryClient.setQueryData(['posts'], context.previous);
  },
  onSettled: () => {
    queryClient.invalidateQueries({ queryKey: ['posts'] });
  },
});

Quick Reference
Pattern	When
addDoc	Create with auto-ID
setDoc	Create/overwrite with known ID
updateDoc	Partial update
writeBatch	Multiple related writes
Listeners	Real-time features
Weekly Installs
28
Repository
bumgeunsong/dai…-friends
GitHub Stars
9
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass