---
title: capacitor-best-practices
url: https://skills.sh/cap-go/capacitor-skills/capacitor-best-practices
---

# capacitor-best-practices

skills/cap-go/capacitor-skills/capacitor-best-practices
capacitor-best-practices
Installation
$ npx skills add https://github.com/cap-go/capacitor-skills --skill capacitor-best-practices
Summary

Comprehensive guidelines for building production-ready Capacitor applications.

Covers project structure, configuration management, plugin installation patterns, and native project setup for iOS and Android
Emphasizes critical practices: keeping Capacitor packages in sync, checking plugin availability before use, lazy loading plugins, and secure storage for sensitive data
Includes performance optimization strategies such as batching bridge calls, hardware acceleration, and image optimization with quality/size limits
Provides security best practices including certificate pinning, root/jailbreak detection, and proper error handling for all plugin calls
Contains deployment checklist and live update strategies using Capacitor Updater with background download patterns
SKILL.md
Capacitor Best Practices

Comprehensive guidelines for building production-ready Capacitor applications.

When to Use This Skill
Setting up a new Capacitor project
Reviewing Capacitor app architecture
Optimizing app performance
Implementing security measures
Preparing for app store submission
Project Structure
Recommended Directory Layout
my-app/
├── src/                      # Web app source
├── android/                  # Android native project
├── ios/                      # iOS native project
├── capacitor.config.ts       # Capacitor configuration
├── package.json
└── tsconfig.json

Configuration Best Practices

capacitor.config.ts (CORRECT):

import type { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.company.app',
  appName: 'My App',
  webDir: 'dist',
  server: {
    // Only enable for development
    ...(process.env.NODE_ENV === 'development' && {
      url: 'http://localhost:5173',
      cleartext: true,
    }),
  },
  plugins: {
    SplashScreen: {
      launchAutoHide: false,
    },
  },
};

export default config;


capacitor.config.json (AVOID):

{
  "server": {
    "url": "http://localhost:5173",
    "cleartext": true
  }
}


Never commit development server URLs to production

Plugin Usage
CRITICAL: Always Use Latest Capacitor

Keep Capacitor core packages in sync:

npm install @capacitor/core@latest @capacitor/cli@latest
npm install @capacitor/ios@latest @capacitor/android@latest
npx cap sync

Plugin Installation Pattern

CORRECT:

# 1. Install the package
npm install @capgo/capacitor-native-biometric

# 2. Sync native projects
npx cap sync

# 3. For iOS: Install pods (or use SPM)
cd ios/App && pod install && cd ../..


INCORRECT:

# Missing sync step
npm install @capgo/capacitor-native-biometric
# App crashes because native code not linked

Plugin Initialization

CORRECT - Check availability before use:

import { NativeBiometric, BiometryType } from '@capgo/capacitor-native-biometric';

async function authenticate() {
  const { isAvailable, biometryType } = await NativeBiometric.isAvailable();

  if (!isAvailable) {
    // Fallback to password
    return authenticateWithPassword();
  }

  try {
    await NativeBiometric.verifyIdentity({
      reason: 'Authenticate to access your account',
      title: 'Biometric Login',
    });
    return true;
  } catch (error) {
    // User cancelled or biometric failed
    return false;
  }
}


INCORRECT - No availability check:

// Will crash if biometrics not available
await NativeBiometric.verifyIdentity({ reason: 'Login' });

Performance Optimization
CRITICAL: Lazy Load Plugins

CORRECT - Dynamic imports:

// Only load when needed
async function scanDocument() {
  const { DocumentScanner } = await import('@capgo/capacitor-document-scanner');
  return DocumentScanner.scanDocument();
}


INCORRECT - Import everything at startup:

// Increases initial bundle size
import { DocumentScanner } from '@capgo/capacitor-document-scanner';
import { NativeBiometric } from '@capgo/capacitor-native-biometric';
import { Camera } from '@capacitor/camera';
// ... 20 more plugins

HIGH: Optimize WebView Performance

CORRECT - Use hardware acceleration:

<!-- android/app/src/main/AndroidManifest.xml -->
<application
    android:hardwareAccelerated="true"
    android:largeHeap="true">

<!-- ios/App/App/Info.plist -->
<key>UIViewGroupOpacity</key>
<false/>

HIGH: Minimize Bridge Calls

CORRECT - Batch operations:

// Single call with batch data
await Storage.set({
  key: 'userData',
  value: JSON.stringify({ name, email, preferences }),
});


INCORRECT - Multiple bridge calls:

// Each call crosses the JS-native bridge
await Storage.set({ key: 'name', value: name });
await Storage.set({ key: 'email', value: email });
await Storage.set({ key: 'preferences', value: JSON.stringify(preferences) });

MEDIUM: Image Optimization

CORRECT:

import { Camera, CameraResultType } from '@capacitor/camera';

const photo = await Camera.getPhoto({
  quality: 80,           // Not 100
  width: 1024,           // Reasonable max
  resultType: CameraResultType.Uri,  // Not Base64 for large images
  correctOrientation: true,
});


INCORRECT:

const photo = await Camera.getPhoto({
  quality: 100,
  resultType: CameraResultType.Base64,  // Memory intensive
  // No size limits
});

Security Best Practices
CRITICAL: Secure Storage

CORRECT - Use secure storage for sensitive data:

import { NativeBiometric } from '@capgo/capacitor-native-biometric';

// Store credentials securely
await NativeBiometric.setCredentials({
  username: 'user@example.com',
  password: 'secret',
  server: 'api.myapp.com',
});

// Retrieve with biometric verification
const credentials = await NativeBiometric.getCredentials({
  server: 'api.myapp.com',
});


INCORRECT - Plain storage:

import { Preferences } from '@capacitor/preferences';

// NEVER store sensitive data in plain preferences
await Preferences.set({
  key: 'password',
  value: 'secret',  // Stored in plain text!
});

CRITICAL: Certificate Pinning

For production apps handling sensitive data:

// capacitor.config.ts
const config: CapacitorConfig = {
  plugins: {
    CapacitorHttp: {
      enabled: true,
    },
  },
  server: {
    // Disable cleartext in production
    cleartext: false,
  },
};

HIGH: Root/Jailbreak Detection
import { IsRoot } from '@capgo/capacitor-is-root';

async function checkDeviceSecurity() {
  const { isRooted } = await IsRoot.isRooted();

  if (isRooted) {
    // Show warning or restrict functionality
    showSecurityWarning('Device appears to be rooted/jailbroken');
  }
}

HIGH: App Tracking Transparency (iOS)
import { AppTrackingTransparency } from '@capgo/capacitor-app-tracking-transparency';

async function requestTracking() {
  const { status } = await AppTrackingTransparency.requestPermission();

  if (status === 'authorized') {
    // Enable analytics
  }
}

Error Handling
CRITICAL: Always Handle Plugin Errors

CORRECT:

import { Camera, CameraResultType } from '@capacitor/camera';

async function takePhoto() {
  try {
    const image = await Camera.getPhoto({
      quality: 90,
      resultType: CameraResultType.Uri,
    });
    return image;
  } catch (error) {
    if (error.message === 'User cancelled photos app') {
      // User cancelled, not an error
      return null;
    }
    if (error.message.includes('permission')) {
      // Permission denied
      showPermissionDialog();
      return null;
    }
    // Unexpected error
    console.error('Camera error:', error);
    throw error;
  }
}


INCORRECT:

// No error handling
const image = await Camera.getPhoto({ quality: 90 });

Live Updates
Using Capacitor Updater
import { CapacitorUpdater } from '@capgo/capacitor-updater';

// Notify when app is ready
CapacitorUpdater.notifyAppReady();

// Listen for updates
CapacitorUpdater.addListener('updateAvailable', async (update) => {
  // Download in background
  const bundle = await CapacitorUpdater.download({
    url: update.url,
    version: update.version,
  });

  // Apply on next app start
  await CapacitorUpdater.set(bundle);
});

Update Strategy

CORRECT - Background download, apply on restart:

// Download silently
const bundle = await CapacitorUpdater.download({ url, version });

// User continues using app...

// Apply when they close/reopen
await CapacitorUpdater.set(bundle);


INCORRECT - Interrupt user:

// Don't force reload while user is active
const bundle = await CapacitorUpdater.download({ url, version });
await CapacitorUpdater.reload();  // Disrupts user

Native Project Management
iOS: Use Swift Package Manager (SPM)

Modern approach - prefer SPM over CocoaPods:

# Podfile - Remove plugin pods, use SPM instead
target 'App' do
  capacitor_pods
  # Plugin dependencies via SPM in Xcode
end

Android: Gradle Configuration
// android/app/build.gradle
android {
    defaultConfig {
        minSdkVersion 22
        targetSdkVersion 34
    }

    buildTypes {
        release {
            minifyEnabled true
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
        }
    }
}

Testing
Plugin Mocking
// Mock for web testing
jest.mock('@capgo/capacitor-native-biometric', () => ({
  NativeBiometric: {
    isAvailable: jest.fn().mockResolvedValue({
      isAvailable: true,
      biometryType: 'touchId',
    }),
    verifyIdentity: jest.fn().mockResolvedValue({}),
  },
}));

Platform Detection
import { Capacitor } from '@capacitor/core';

if (Capacitor.isNativePlatform()) {
  // Native-specific code
} else {
  // Web fallback
}

// Or check specific platform
if (Capacitor.getPlatform() === 'ios') {
  // iOS-specific code
}

Deployment Checklist
 Remove development server URLs from config
 Enable ProGuard for Android release builds
 Set appropriate iOS deployment target
 Test on real devices, not just simulators
 Verify all permissions are declared
 Test with poor network conditions
 Verify deep links work correctly
 Test app backgrounding/foregrounding
 Verify push notifications work
 Test biometric authentication edge cases
Resources
Capacitor Documentation: https://capacitorjs.com/docs
Capgo Documentation: https://capgo.app/docs
Ionic Framework: https://ionicframework.com/docs
Weekly Installs
614
Repository
cap-go/capacitor-skills
GitHub Stars
31
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass