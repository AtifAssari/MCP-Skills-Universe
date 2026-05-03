---
title: desktop
url: https://skills.sh/lobehub/lobe-chat/desktop
---

# desktop

skills/lobehub/lobe-chat/desktop
desktop
Originally fromlobehub/lobehub
Installation
$ npx skills add https://github.com/lobehub/lobe-chat --skill desktop
SKILL.md
Desktop Development Guide
Architecture Overview

LobeHub desktop is built on Electron with main-renderer architecture:

Main Process (apps/desktop/src/main): App lifecycle, system APIs, window management
Renderer Process: Reuses web code from src/
Preload Scripts (apps/desktop/src/preload): Securely expose main process to renderer
Adding New Desktop Features
1. Create Controller

Location: apps/desktop/src/main/controllers/

import { ControllerModule, IpcMethod } from '@/controllers';

export default class NewFeatureCtr extends ControllerModule {
  static override readonly groupName = 'newFeature';

  @IpcMethod()
  async doSomething(params: SomeParams): Promise<SomeResult> {
    // Implementation
    return { success: true };
  }
}


Register in apps/desktop/src/main/controllers/registry.ts.

2. Define IPC Types

Location: packages/electron-client-ipc/src/types.ts

export interface SomeParams {
  /* ... */
}
export interface SomeResult {
  success: boolean;
  error?: string;
}

3. Create Renderer Service

Location: src/services/electron/

import { ensureElectronIpc } from '@/utils/electron/ipc';

const ipc = ensureElectronIpc();

export const newFeatureService = async (params: SomeParams) => {
  return ipc.newFeature.doSomething(params);
};

4. Implement Store Action

Location: src/store/

5. Add Tests

Location: apps/desktop/src/main/controllers/__tests__/

Detailed Guides

See references/ for specific topics:

Feature implementation: references/feature-implementation.md
Local tools workflow: references/local-tools.md
Menu configuration: references/menu-config.md
Window management: references/window-management.md
Best Practices
Security: Validate inputs, limit exposed APIs
Performance: Use async methods, batch data transfers
UX: Add progress indicators, provide error feedback
Code organization: Follow existing patterns, add documentation
Weekly Installs
461
Repository
lobehub/lobe-chat
GitHub Stars
75.9K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass