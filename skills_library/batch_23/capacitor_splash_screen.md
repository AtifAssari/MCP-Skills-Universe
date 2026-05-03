---
title: capacitor-splash-screen
url: https://skills.sh/cap-go/capgo-skills/capacitor-splash-screen
---

# capacitor-splash-screen

skills/cap-go/capgo-skills/capacitor-splash-screen
capacitor-splash-screen
Installation
$ npx skills add https://github.com/cap-go/capgo-skills --skill capacitor-splash-screen
SKILL.md
Splash Screen in Capacitor

Configure and customize splash screens for iOS and Android.

When to Use This Skill
User wants to customize splash screen
User needs splash screen assets
User wants animated splash
User has splash screen issues
Quick Start
Install Plugin
npm install @capacitor/splash-screen
npx cap sync

Basic Configuration
// capacitor.config.ts
import type { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  plugins: {
    SplashScreen: {
      launchShowDuration: 2000,
      launchAutoHide: true,
      backgroundColor: '#ffffff',
      androidSplashResourceName: 'splash',
      androidScaleType: 'CENTER_CROP',
      showSpinner: false,
      splashFullScreen: true,
      splashImmersive: true,
    },
  },
};

Programmatic Control
import { SplashScreen } from '@capacitor/splash-screen';

// Hide after app is ready
async function initApp() {
  // Initialize your app
  await loadUserData();
  await setupServices();

  // Hide splash screen
  await SplashScreen.hide();
}

// Show splash (useful for app refresh)
await SplashScreen.show({
  autoHide: false,
});

// Hide with animation
await SplashScreen.hide({
  fadeOutDuration: 500,
});

Generate Assets
Using Capacitor Assets
npm install -D @capacitor/assets

# Place source images in resources/
# resources/splash.png (2732x2732 recommended)
# resources/splash-dark.png (optional)

npx capacitor-assets generate

iOS Sizes
Size	Usage
2732x2732	iPad Pro 12.9"
2048x2732	iPad Pro portrait
2732x2048	iPad Pro landscape
1668x2388	iPad Pro 11"
1536x2048	iPad
1242x2688	iPhone XS Max
828x1792	iPhone XR
1125x2436	iPhone X/XS
1242x2208	iPhone Plus
750x1334	iPhone 8
640x1136	iPhone SE
Android Sizes
Density	Size
mdpi	320x480
hdpi	480x800
xhdpi	720x1280
xxhdpi	960x1600
xxxhdpi	1280x1920
iOS Storyboard
<!-- ios/App/App/Base.lproj/LaunchScreen.storyboard -->
<?xml version="1.0" encoding="UTF-8"?>
<document type="com.apple.InterfaceBuilder3.CocoaTouch.Storyboard.XIB" version="3.0">
    <scenes>
        <scene sceneID="1">
            <objects>
                <viewController id="2" sceneMemberID="viewController">
                    <view key="view" contentMode="scaleToFill" id="3">
                        <rect key="frame" x="0" y="0" width="414" height="896"/>
                        <color key="backgroundColor" systemColor="systemBackgroundColor"/>
                        <subviews>
                            <imageView
                                contentMode="scaleAspectFit"
                                image="splash"
                                translatesAutoresizingMaskIntoConstraints="NO"
                                id="4">
                            </imageView>
                        </subviews>
                        <constraints>
                            <constraint firstItem="4" firstAttribute="centerX" secondItem="3" secondAttribute="centerX" id="5"/>
                            <constraint firstItem="4" firstAttribute="centerY" secondItem="3" secondAttribute="centerY" id="6"/>
                        </constraints>
                    </view>
                </viewController>
            </objects>
        </scene>
    </scenes>
</document>

Android Configuration
XML Splash Screen (Android 11+)
<!-- android/app/src/main/res/values/styles.xml -->
<resources>
    <style name="AppTheme.NoActionBarLaunch" parent="Theme.SplashScreen">
        <item name="windowSplashScreenBackground">@color/splash_background</item>
        <item name="windowSplashScreenAnimatedIcon">@drawable/splash</item>
        <item name="windowSplashScreenAnimationDuration">1000</item>
        <item name="postSplashScreenTheme">@style/AppTheme.NoActionBar</item>
    </style>
</resources>

Colors
<!-- android/app/src/main/res/values/colors.xml -->
<resources>
    <color name="splash_background">#FFFFFF</color>
</resources>

<!-- android/app/src/main/res/values-night/colors.xml -->
<resources>
    <color name="splash_background">#121212</color>
</resources>

Dark Mode Support
// capacitor.config.ts
plugins: {
  SplashScreen: {
    launchAutoHide: false, // Control manually
    backgroundColor: '#ffffff',
    // iOS will use LaunchScreen.storyboard variations
    // Android uses values-night/colors.xml
  },
},

// Detect dark mode and configure
import { SplashScreen } from '@capacitor/splash-screen';

const isDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

// Show appropriate themed content
await SplashScreen.hide({
  fadeOutDuration: 300,
});

Animated Splash
Lottie Animation
import { SplashScreen } from '@capacitor/splash-screen';

async function showAnimatedSplash() {
  // Keep native splash while loading
  await SplashScreen.show({ autoHide: false });

  // Load Lottie animation in web
  const lottie = await import('lottie-web');

  // Show web-based animated splash
  document.getElementById('splash-animation').style.display = 'block';

  const animation = lottie.loadAnimation({
    container: document.getElementById('splash-animation'),
    path: '/animations/splash.json',
    loop: false,
  });

  animation.addEventListener('complete', async () => {
    // Hide native splash
    await SplashScreen.hide({ fadeOutDuration: 0 });
    // Hide web splash
    document.getElementById('splash-animation').style.display = 'none';
  });
}

Best Practices
Keep it fast - Under 2 seconds total
Match branding - Use consistent colors/logo
Support dark mode - Provide dark variants
Don't block - Load essentials only
Progressive reveal - Fade out smoothly
Troubleshooting
Issue	Solution
White flash	Match splash background to app
Stretching	Use correct asset sizes
Not hiding	Call hide() manually
Dark mode wrong	Add values-night resources
Resources
Capacitor Splash Screen: https://capacitorjs.com/docs/apis/splash-screen
Capacitor Assets: https://github.com/ionic-team/capacitor-assets
Android Splash Screens: https://developer.android.com/develop/ui/views/launch/splash-screen
Weekly Installs
246
Repository
cap-go/capgo-skills
GitHub Stars
31
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass