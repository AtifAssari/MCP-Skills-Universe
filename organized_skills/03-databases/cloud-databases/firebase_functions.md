---
rating: ⭐⭐⭐
title: firebase-functions
url: https://skills.sh/bumgeunsong/daily-writing-friends/firebase-functions
---

# firebase-functions

skills/bumgeunsong/daily-writing-friends/firebase-functions
firebase-functions
Installation
$ npx skills add https://github.com/bumgeunsong/daily-writing-friends --skill firebase-functions
SKILL.md
Firebase Functions Patterns
Directory Structure
functions/
├── src/
│   ├── index.ts              # Function exports
│   ├── admin.ts              # Firebase Admin SDK init
│   ├── backfill/             # Data migration scripts
│   ├── commentSuggestion/    # AI comment features
│   ├── commentings/          # Comment activity tracking
│   ├── notifications/        # Push notification functions
│   ├── postings/             # Post activity tracking
│   ├── replyings/            # Reply activity tracking
│   └── shared/               # Shared utilities

Function Structure
import { onDocumentCreated } from 'firebase-functions/v2/firestore';
import admin from '../admin';
import { Post } from '../types/Post';

export const createPosting = onDocumentCreated(
  'boards/{boardId}/posts/{postId}',
  async (event) => {
    const postData = event.data?.data() as Post;
    const { boardId, postId } = event.params;

    if (!postData) {
      console.error('No post data found.');
      return null;
    }

    try {
      await admin.firestore()
        .collection('users')
        .doc(postData.authorId)
        .collection('postings')
        .add(postingData);
      console.log(`Created posting for user ${postData.authorId}`);
    } catch (error) {
      console.error('Error writing posting:', error);
    }

    return null;
  }
);

Error Handling

Don't throw - let function complete gracefully:

try {
  await admin.firestore().collection('...').add(data);
  console.log(`Successfully created ${resourceType}`);
} catch (error) {
  console.error(`Error creating ${resourceType}:`, error);
  // Don't throw - function should complete
}

return null;

Build & Test
cd functions && npm install   # Install deps
cd functions && npm run build # Compile TypeScript
cd functions && npm test      # Run Jest tests

Weekly Installs
43
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