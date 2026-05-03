---
title: flutter-terminal-cheat-sheet
url: https://skills.sh/rodydavis/skills/flutter-terminal-cheat-sheet
---

# flutter-terminal-cheat-sheet

skills/rodydavis/skills/flutter-terminal-cheat-sheet
flutter-terminal-cheat-sheet
Installation
$ npx skills add https://github.com/rodydavis/skills --skill flutter-terminal-cheat-sheet
SKILL.md
Flutter Terminal Cheat Sheet
Run Flutter web with SKIA
flutter run -d web --release --dart-define=FLUTTER_WEB_USE_SKIA=true

Run Flutter web with Canvas Kit
flutter run -d chrome --release --dart-define=FLUTTER_WEB_USE_EXPERIMENTAL_CANVAS_TEXT=true

Build your Flutter web app to Github Pages to the docs folder
flutter build web && rm -rf ./docs && mkdir ./docs && cp -a ./build/web/. ./docs/

Clean rebuild CocoaPods
cd ios && pod deintegrate && pod cache clean —all && pod install && cd ..


Sometimes with firebase you need to run: pod update Firebase

Create Dart package with Example
flutter create -t plugin . && flutter create -i swift -a kotlin --androidx example

Watch Build Files
flutter packages pub run build_runner watch  -—delete-conflicting-outputs

Generate Build Files
flutter packages pub run build_runner build  -—delete-conflicting-outputs

Build Bug Report
flutter run —bug-report

Flutter generate test coverage
flutter test --coverage && genhtml -o coverage coverage/lcov.info

Rebuild Flutter Cache
flutter pub pub cache repair

Clean every flutter project
find . -name "pubspec.yaml" -exec $SHELL -c '
    echo "Done. Cleaning all projects."
    for i in "$@" ; do
        DIR=$(dirname "${i}")
        echo "Cleaning ${DIR}..."
        (cd "$DIR" && flutter clean >/dev/null 2>&1)
    done
    echo "DONE!"
' {} +

Conditional Export/Import
export 'unsupported.dart'
    if (dart.library.html) 'web.dart'
    if (dart.library.io) 'mobile.dart';

Kill Dart Running
killall -9 dart

Flutter scripts 

Add all the scripts to your pubspec.yaml with flutter_scripts.

Weekly Installs
48
Repository
rodydavis/skills
GitHub Stars
40
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass