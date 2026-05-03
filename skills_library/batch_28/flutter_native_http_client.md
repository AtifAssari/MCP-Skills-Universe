---
title: flutter-native-http-client
url: https://skills.sh/rodydavis/skills/flutter-native-http-client
---

# flutter-native-http-client

skills/rodydavis/skills/flutter-native-http-client
flutter-native-http-client
Installation
$ npx skills add https://github.com/rodydavis/skills --skill flutter-native-http-client
SKILL.md
Flutter Native HTTP Client
import 'package:cronet_http/cronet_http.dart';
import 'package:cupertino_http/cupertino_http.dart';
import 'package:device_info_plus/device_info_plus.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart';
import 'package:platform_info/platform_info.dart';

void main() async {
  var clientFactory = Client.new;
  final device = DeviceInfoPlugin();
  if (platform.isAndroid) {
    final engine = CronetEngine.build(
      cacheMode: CacheMode.memory,
      userAgent: (await device.androidInfo).model,
    );
    clientFactory = () => CronetClient.fromCronetEngine(engine);
  } else if (platform.isCupertino) {
    clientFactory = CupertinoClient.defaultSessionConfiguration.call;
  }
  runWithClient(() => runApp(const MyApp()),clientFactory);
}

Weekly Installs
41
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