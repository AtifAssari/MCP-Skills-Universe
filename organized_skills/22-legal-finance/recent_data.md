---
rating: ⭐⭐
title: recent-data
url: https://skills.sh/lobehub/lobehub/recent-data
---

# recent-data

skills/lobehub/lobehub/recent-data
recent-data
Installation
$ npx skills add https://github.com/lobehub/lobehub --skill recent-data
Summary

Session store integration for tracking recently accessed topics, resources, and pages.

Three initialization hooks (useInitRecentTopic, useInitRecentResource, useInitRecentPage) load recent data into session store at app startup
Read recent data via selectors (recentSelectors.recentTopics, etc.) or hook return values; selectors are recommended for multi-component access
Built-in features include auto login detection, data caching, SWR-based auto-refresh on focus, and full TypeScript typing
RecentTopic includes agent metadata (avatar, background color, title) and updatedAt timestamp; RecentResources and RecentPages follow similar patterns
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
547
Repository
lobehub/lobehub
GitHub Stars
75.9K
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass