---
rating: ⭐⭐
title: flutter-accessibility-audit
url: https://skills.sh/flutter/skills/flutter-accessibility-audit
---

# flutter-accessibility-audit

skills/flutter/skills/flutter-accessibility-audit
flutter-accessibility-audit
Installation
$ npx skills add https://github.com/flutter/skills --skill flutter-accessibility-audit
SKILL.md
Implementing Flutter Accessibility
Contents
Managing Semantics
Auditing Accessibility
Debugging the Semantics Tree
Examples
Managing Semantics

Rely on Flutter's standard widgets (e.g., TabBar, MenuAnchor) for automatic semantic role assignment whenever possible. When building custom components or overriding default behaviors, explicitly define the UI element's purpose using the Semantics widget.

Wrap custom UI components in a Semantics widget.
Assign the appropriate SemanticsRole enum value to the role property to define the element's purpose (e.g., button, list, heading).
If building for Flutter Web, note that Flutter translates these roles into corresponding ARIA roles in the HTML DOM.
Enable web accessibility explicitly. It is disabled by default for performance. Either instruct users to press the invisible aria-label="Enable accessibility" button, or force it programmatically in your main() function.
Auditing Accessibility

Implement the following workflows to verify that your application meets accessibility standards.

Task Progress: Platform-Specific Scanning

Copy this checklist to track your manual auditing progress across target platforms:

 If testing on Android:
Install the Accessibility Scanner from Google Play.
Enable it via Settings > Accessibility > Accessibility Scanner > On.
Tap the Accessibility Scanner checkmark icon over your running app to initiate the scan.
 If testing on iOS:
Open the ios folder in Xcode and run the app on a Simulator.
Navigate to Xcode > Open Developer Tools > Accessibility Inspector.
Select Inspection > Enable Point to Inspect and click UI elements to verify attributes.
Select Audit > Run Audit to generate an issue report.
 If testing on Web:
Open Chrome DevTools.
Inspect the HTML tree under the semantics host node.
Navigate to the Elements tab and open the Accessibility sub-tab to inspect exported ARIA data.
Visualize semantic nodes by running the app with: flutter run -d chrome --profile --dart-define=FLUTTER_WEB_DEBUG_SHOW_SEMANTICS=true.
Task Progress: Automated Testing

Integrate Flutter's Accessibility Guideline API into your widget tests to catch contrast, target size, and labeling issues automatically.

 Create a dedicated test file (e.g., test/a11y_test.dart).
 Initialize the semantics handle using tester.ensureSemantics().
 Assert against androidTapTargetGuideline (48x48px minimum).
 Assert against iOSTapTargetGuideline (44x44px minimum).
 Assert against labeledTapTargetGuideline.
 Assert against textContrastGuideline (3:1 minimum for large text).
 Dispose of the semantics handle at the end of the test.
Debugging the Semantics Tree

When semantic nodes are incorrectly placed or missing, execute the following feedback loop to identify and resolve the discrepancies.

Run validator: Trigger a dump of the Semantics tree to the console.
Enable accessibility via a system tool or SemanticsDebugger.
Invoke debugDumpSemanticsTree() (e.g., bind it to a GestureDetector's onTap callback for easy triggering during debugging).
Review errors: Analyze the console output to locate missing labels, incorrect roles, or improperly nested semantic nodes.
Fix: Wrap the offending widgets in Semantics or MergeSemantics widgets, apply the correct SemanticsRole, and repeat step 1 until the tree accurately reflects the visual UI.
Examples
Programmatically Enabling Web Accessibility

Force the Semantics tree to build immediately on Flutter Web.

import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter/semantics.dart';

void main() {
  runApp(const MyApp());
  if (kIsWeb) {
    SemanticsBinding.instance.ensureSemantics();
  }
}

Explicitly Defining Semantic Roles

Assign explicit list and list-item roles to a custom layout.

import 'package:flutter/material.dart';
import 'package:flutter/semantics.dart';

class MyCustomListWidget extends StatelessWidget {
  const MyCustomListWidget({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Semantics(
      role: SemanticsRole.list,
      explicitChildNodes: true,
      child: Column(
        children: <Widget>[
          Semantics(
            role: SemanticsRole.listItem,
            child: const Padding(
              padding: EdgeInsets.all(8.0),
              child: Text('Content of the first custom list item.'),
            ),
          ),
          Semantics(
            role: SemanticsRole.listItem,
            child: const Padding(
              padding: EdgeInsets.all(8.0),
              child: Text('Content of the second custom list item.'),
            ),
          ),
        ],
      ),
    );
  }
}

Automated Accessibility Testing

Implement the Accessibility Guideline API in a widget test.

import 'package:flutter_test/flutter_test.dart';
import 'package:your_accessible_app/main.dart';

void main() {
  testWidgets('Follows a11y guidelines', (tester) async {
    final SemanticsHandle handle = tester.ensureSemantics();
    await tester.pumpWidget(const AccessibleApp());

    // Check tap target sizes
    await expectLater(tester, meetsGuideline(androidTapTargetGuideline));
    await expectLater(tester, meetsGuideline(iOSTapTargetGuideline));

    // Check labels and contrast
    await expectLater(tester, meetsGuideline(labeledTapTargetGuideline));
    await expectLater(tester, meetsGuideline(textContrastGuideline));
    
    handle.dispose();
  });
}

Weekly Installs
1.5K
Repository
flutter/skills
GitHub Stars
1.3K
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass