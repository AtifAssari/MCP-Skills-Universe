---
rating: ⭐⭐
title: mobile-offline-support
url: https://skills.sh/aj-geddes/useful-ai-prompts/mobile-offline-support
---

# mobile-offline-support

skills/aj-geddes/useful-ai-prompts/mobile-offline-support
mobile-offline-support
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill mobile-offline-support
SKILL.md
Mobile Offline Support
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Design offline-first mobile applications that provide seamless user experience regardless of connectivity.

When to Use
Building apps that work without internet connection
Implementing seamless sync when connectivity returns
Handling data conflicts between device and server
Reducing server load with intelligent caching
Improving app responsiveness with local storage
Quick Start

Minimal working example:

import AsyncStorage from '@react-native-async-storage/async-storage';
import NetInfo from '@react-native-community/netinfo';

class StorageManager {
  static async saveItems(items) {
    try {
      await AsyncStorage.setItem(
        'items_cache',
        JSON.stringify({ data: items, timestamp: Date.now() })
      );
    } catch (error) {
      console.error('Failed to save items:', error);
    }
  }

  static async getItems() {
    try {
      const data = await AsyncStorage.getItem('items_cache');
      return data ? JSON.parse(data) : null;
    } catch (error) {
      console.error('Failed to retrieve items:', error);
      return null;
    }
  }

// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
React Native Offline Storage	React Native Offline Storage
iOS Core Data Implementation	iOS Core Data Implementation
Android Room Database	Android Room Database
Best Practices
✅ DO
Implement robust local storage
Use automatic sync when online
Provide visual feedback for offline status
Queue actions for later sync
Handle conflicts gracefully
Cache frequently accessed data
Implement proper error recovery
Test offline scenarios thoroughly
Use compression for large data
Monitor storage usage
❌ DON'T
Assume constant connectivity
Sync large files frequently
Ignore storage limitations
Force unnecessary syncing
Lose data on offline mode
Store sensitive data unencrypted
Accumulate infinite queue items
Ignore sync failures silently
Sync in tight loops
Deploy without offline testing
Weekly Installs
321
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass