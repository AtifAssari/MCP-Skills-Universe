---
title: recent-data
url: https://skills.sh/lobehub/lobe-chat/recent-data
---

# recent-data

skills/lobehub/lobe-chat/recent-data
recent-data
Originally fromlobehub/lobehub
Installation
$ npx skills add https://github.com/lobehub/lobe-chat --skill recent-data
SKILL.md
Recent Data Usage Guide

Recent data (recentTopics, recentResources, recentPages) is stored in session store.

Initialization

In app top-level (e.g., RecentHydration.tsx):

import { useInitRecentTopic } from '@/hooks/useInitRecentTopic';
import { useInitRecentResource } from '@/hooks/useInitRecentResource';
import { useInitRecentPage } from '@/hooks/useInitRecentPage';

const App = () => {
  useInitRecentTopic();
  useInitRecentResource();
  useInitRecentPage();
  return <YourComponents />;
};

Usage
Method 1: Read from Store (Recommended)
import { useSessionStore } from '@/store/session';
import { recentSelectors } from '@/store/session/selectors';

const Component = () => {
  const recentTopics = useSessionStore(recentSelectors.recentTopics);
  const isInit = useSessionStore(recentSelectors.isRecentTopicsInit);

  if (!isInit) return <div>Loading...</div>;

  return (
    <div>
      {recentTopics.map((topic) => (
        <div key={topic.id}>{topic.title}</div>
      ))}
    </div>
  );
};

Method 2: Use Hook Return (Single component)
const { data: recentTopics, isLoading } = useInitRecentTopic();

Available Selectors
Recent Topics
const recentTopics = useSessionStore(recentSelectors.recentTopics);
// Type: RecentTopic[]

const isInit = useSessionStore(recentSelectors.isRecentTopicsInit);
// Type: boolean


RecentTopic type:

interface RecentTopic {
  agent: {
    avatar: string | null;
    backgroundColor: string | null;
    id: string;
    title: string | null;
  } | null;
  id: string;
  title: string | null;
  updatedAt: Date;
}

Recent Resources
const recentResources = useSessionStore(recentSelectors.recentResources);
// Type: FileListItem[]

const isInit = useSessionStore(recentSelectors.isRecentResourcesInit);

Recent Pages
const recentPages = useSessionStore(recentSelectors.recentPages);
const isInit = useSessionStore(recentSelectors.isRecentPagesInit);

Features
Auto login detection: Only loads when user is logged in
Data caching: Stored in store, no repeated loading
Auto refresh: SWR refreshes on focus (5-minute interval)
Type safe: Full TypeScript types
Best Practices
Initialize all recent data at app top-level
Use selectors to read from store
For multi-component use, prefer Method 1
Use selectors for render optimization
Weekly Installs
319
Repository
lobehub/lobe-chat
GitHub Stars
75.9K
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass