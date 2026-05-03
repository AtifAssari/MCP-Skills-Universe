---
title: flutter-adding-home-screen-widgets
url: https://skills.sh/flutter/skills/flutter-adding-home-screen-widgets
---

# flutter-adding-home-screen-widgets

skills/flutter/skills/flutter-adding-home-screen-widgets
flutter-adding-home-screen-widgets
Installation
$ npx skills add https://github.com/flutter/skills --skill flutter-adding-home-screen-widgets
Summary

Add home screen widgets to Flutter apps for Android and iOS with native UI and shared data synchronization.

Flutter communicates with native widgets via shared local storage (UserDefaults on iOS, SharedPreferences on Android) using the home_widget package; data flows from Flutter writes to native widget reads on OS trigger.
iOS implementation uses Xcode, SwiftUI, and Widget Extension targets with App Groups capability; Android uses Android Studio with AppWidgetProvider, XML layouts, and RemoteViews.
Supports rendering complex Flutter widgets as images for display in native widgets, and custom font registration on iOS.
Includes step-by-step checklists for Flutter integration, iOS SwiftUI setup, and Android Kotlin setup with code examples for data updates and widget providers.
SKILL.md
Implementing Flutter Home Screen Widgets
Contents
Architecture & Data Flow
Flutter Integration Workflow
iOS Implementation Workflow
Android Implementation Workflow
Advanced Techniques
Examples
Architecture & Data Flow

Home Screen Widgets require native UI implementation (SwiftUI for iOS, XML/Kotlin for Android). The Flutter app communicates with these native widgets via shared local storage (UserDefaults on iOS, SharedPreferences on Android) using the home_widget package.

Data Write: Flutter app writes key-value pairs or renders images to a shared container.
Trigger: Flutter app signals the native OS to update the widget.
Data Read: Native widget wakes up, reads the key-value pairs or images from the shared container, and updates its UI.
Flutter Integration Workflow

Use this checklist to implement the Dart side of the Home Screen Widget integration.

 Step 1: Initialize the App Group. Call HomeWidget.setAppGroupId('<YOUR_APP_GROUP>') in initState() or app startup.
 Step 2: Save Data. Use HomeWidget.saveWidgetData<T>('key', value) to write data to shared storage.
 Step 3: Trigger Update. Call HomeWidget.updateWidget(iOSName: 'YourIOSWidget', androidName: 'YourAndroidWidget') to notify the OS.
 Step 4: Validate. Run Flutter build -> review console for missing plugin registrations -> fix.
iOS Implementation Workflow

If targeting iOS, implement the widget using Xcode and SwiftUI.

 Step 1: Create Target. Open ios/Runner.xcworkspace in Xcode. Add a new Widget Extension target. Disable "Include Live Activity" and "Include Configuration Intent" unless explicitly required.
 Step 2: Configure App Groups. Add the App Groups capability to both the Runner target and the Widget Extension target. Ensure the App Group ID matches the one used in Dart.
 Step 3: Define TimelineEntry. Create a struct conforming to TimelineEntry to hold the data passed from shared storage.
 Step 4: Implement TimelineProvider.
In getSnapshot and getTimeline, instantiate UserDefaults(suiteName: "<YOUR_APP_GROUP>").
Extract values using userDefaults?.string(forKey: "your_key").
Return the populated TimelineEntry.
 Step 5: Build UI. Implement the SwiftUI View to display the data from the TimelineEntry.
 Step 6: Validate. Run Xcode build for the Widget Extension -> review provisioning/App Group errors -> fix.
Android Implementation Workflow

If targeting Android, implement the widget using Android Studio and XML/Kotlin.

 Step 1: Create App Widget. Open the android folder in Android Studio. Right-click the app directory -> New -> Widget -> App Widget.
 Step 2: Define Layout. Edit res/layout/<widget_name>.xml to define the UI using standard Android XML layouts (e.g., RelativeLayout, TextView, ImageView).
 Step 3: Implement AppWidgetProvider.
Open the generated Kotlin class extending AppWidgetProvider.
In the onUpdate method, retrieve shared data using HomeWidgetPlugin.getData(context).
Extract values using widgetData.getString("your_key", null).
Update the UI using RemoteViews and setTextViewText or setImageViewBitmap.
Call appWidgetManager.updateAppWidget(appWidgetId, views).
 Step 4: Validate. Run Android build -> review Manifest registration errors -> fix.
Advanced Techniques
Rendering Flutter Widgets as Images

If the UI is too complex to recreate natively (e.g., custom charts), render the Flutter widget to an image and display the image in the native widget.

Wrap the target Flutter widget with a GlobalKey.
Call HomeWidget.renderFlutterWidget(), passing the widget, a filename, and the key.
iOS: Read the file path from UserDefaults and render using UIImage(contentsOfFile:) inside a SwiftUI Image.
Android: Read the file path from SharedPreferences, decode using BitmapFactory.decodeFile(), and render using setImageViewBitmap().
Using Custom Flutter Fonts (iOS Only)

If utilizing custom fonts defined in Flutter on iOS Home Screen Widgets:

Extract the Flutter asset bundle path in Swift.
Register the font using CTFontManagerRegisterFontsForURL.
Apply the font in SwiftUI using Font.custom().
Examples
Example: Flutter Data Update
import 'package:home_widget/home_widget.dart';

const String appGroupId = 'group.com.example.app';
const String iOSWidgetName = 'NewsWidgets';
const String androidWidgetName = 'NewsWidget';

Future<void> updateWidgetData(String title, String description) async {
  await HomeWidget.setAppGroupId(appGroupId);
  await HomeWidget.saveWidgetData<String>('headline_title', title);
  await HomeWidget.saveWidgetData<String>('headline_description', description);
  await HomeWidget.updateWidget(
    iOSName: iOSWidgetName,
    androidName: androidWidgetName,
  );
}

Example: iOS SwiftUI Provider & View
import WidgetKit
import SwiftUI

struct NewsArticleEntry: TimelineEntry {
    let date: Date
    let title: String
    let description: String
}

struct Provider: TimelineProvider {
    func placeholder(in context: Context) -> NewsArticleEntry {
        NewsArticleEntry(date: Date(), title: "Loading...", description: "Loading...")
    }

    func getSnapshot(in context: Context, completion: @escaping (NewsArticleEntry) -> ()) {
        let userDefaults = UserDefaults(suiteName: "group.com.example.app")
        let title = userDefaults?.string(forKey: "headline_title") ?? "No Title"
        let description = userDefaults?.string(forKey: "headline_description") ?? "No Description"
        
        let entry = NewsArticleEntry(date: Date(), title: title, description: description)
        completion(entry)
    }

    func getTimeline(in context: Context, completion: @escaping (Timeline<Entry>) -> ()) {
        getSnapshot(in: context) { (entry) in
            let timeline = Timeline(entries: [entry], policy: .atEnd)
            completion(timeline)
        }
    }
}

struct NewsWidgetsEntryView : View {
    var entry: Provider.Entry

    var body: some View {
        VStack(alignment: .leading) {
            Text(entry.title).font(.headline)
            Text(entry.description).font(.subheadline)
        }
    }
}

Example: Android Kotlin Provider
package com.example.app.widgets

import android.appwidget.AppWidgetManager
import android.appwidget.AppWidgetProvider
import android.content.Context
import android.widget.RemoteViews
import es.antonborri.home_widget.HomeWidgetPlugin
import com.example.app.R

class NewsWidget : AppWidgetProvider() {
    override fun onUpdate(
        context: Context,
        appWidgetManager: AppWidgetManager,
        appWidgetIds: IntArray,
    ) {
        for (appWidgetId in appWidgetIds) {
            val widgetData = HomeWidgetPlugin.getData(context)
            val views = RemoteViews(context.packageName, R.layout.news_widget).apply {
                val title = widgetData.getString("headline_title", "No Title")
                setTextViewText(R.id.headline_title, title)

                val description = widgetData.getString("headline_description", "No Description")
                setTextViewText(R.id.headline_description, description)
            }
            appWidgetManager.updateAppWidget(appWidgetId, views)
        }
    }
}

// Add this to your SwiftUI View struct
var bundle: URL {
    let bundle = Bundle.main
    if bundle.bundleURL.pathExtension == "appex" {
        var url = bundle.bundleURL.deletingLastPathComponent().deletingLastPathComponent()
        url.append(component: "Frameworks/App.framework/flutter_assets")
        return url
    }
    return bundle.bundleURL
}

init(entry: Provider.Entry) {
    self.entry = entry
    CTFontManagerRegisterFontsForURL(
        bundle.appending(path: "/fonts/YourCustomFont.ttf") as CFURL, 
        CTFontManagerScope.process, 
        nil
    )
}

Weekly Installs
8.3K
Repository
flutter/skills
GitHub Stars
1.3K
First Seen
Mar 13, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass