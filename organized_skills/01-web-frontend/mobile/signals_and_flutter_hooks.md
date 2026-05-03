---
rating: ⭐⭐
title: signals-and-flutter-hooks
url: https://skills.sh/rodydavis/skills/signals-and-flutter-hooks
---

# signals-and-flutter-hooks

skills/rodydavis/skills/signals-and-flutter-hooks
signals-and-flutter-hooks
Installation
$ npx skills add https://github.com/rodydavis/skills --skill signals-and-flutter-hooks
SKILL.md
Signals and Flutter Hooks

When working with data in Flutter, on of the first things you are exposed to is setState.

setState
import 'package:flutter/material.dart';

void main() {
  runApp(const MaterialApp(debugShowCheckedModeBanner: false, home: Counter()));
}

class Counter extends StatefulWidget {
  const Counter({super.key});

  @override
  State<Counter> createState() => _CounterState();
}

class _CounterState extends State<Counter> {
  int count = 0;

  void increment() {
    if (mounted) {
      setState(() {
        count++;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Counter')),
      body: Center(child: Text('Count: $count')),
      floatingActionButton: FloatingActionButton(
        onPressed: increment,
        child: const Icon(Icons.add),
      ),
    );
  }
}


This simply marks the widget as dirty every time you call setState but requires you (as the developer) to be mindful and explict about when those updates happen. If you forget to call setState when mutating data the widget tree can become stale.

ValueNotifier

We can impove this by using ValueNotifier instead of storing the value directly. This gives us the ability to read and write a value in a container and use helper widgets like ValueListenableBuilder to update sub parts of the widget tree on value changes.

import 'package:flutter/material.dart';

void main() {
  runApp(const MaterialApp(debugShowCheckedModeBanner: false, home: Counter()));
}

class Counter extends StatefulWidget {
  const Counter({super.key});

  @override
  State<Counter> createState() => _CounterState();
}

class _CounterState extends State<Counter> {
  final count = ValueNotifier(0);

  void increment() {
    count.value++;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Counter')),
      body: Center(child: ValueListenableBuilder(
        valueListenable: count,
        builder: (context, value, child) {
          return Text('Count: $value');
        }
      )),
      floatingActionButton: FloatingActionButton(
        onPressed: increment,
        child: const Icon(Icons.add),
      ),
    );
  }
}

FlutterSignal

Using the signals package we can upgrade ValueNotifier to a signal backed implmentation which uses a reactive graph based on a push / pull architecture.

import 'package:flutter/material.dart';
import 'package:signals/signals_flutter.dart';

void main() {
  runApp(const MaterialApp(debugShowCheckedModeBanner: false, home: Counter()));
}

class Counter extends StatefulWidget {
  const Counter({super.key});

  @override
  State<Counter> createState() => _CounterState();
}

class _CounterState extends State<Counter> {
  final count = signal(0);

  void increment() {
    count.value++;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Counter')),
      body: Center(
        child: ValueListenableBuilder(
          valueListenable: count,
          builder: (context, value, child) {
            return Text('Count: $value');
          },
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: increment,
        child: const Icon(Icons.add),
      ),
    );
  }
}


Signals created after 6.0.0 also implement ValueNotifier so you can easily migrate them without changing any other code.

Instead of ValueListenableBuilder we can use the Watch widget or .watch(context) extension.

import 'package:flutter/material.dart';
import 'package:signals/signals_flutter.dart';

void main() {
  runApp(const MaterialApp(debugShowCheckedModeBanner: false, home: Counter()));
}

class Counter extends StatefulWidget {
  const Counter({super.key});

  @override
  State<Counter> createState() => _CounterState();
}

class _CounterState extends State<Counter> {
  final count = signal(0);

  void increment() {
    count.value++;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Counter')),
      body: Center(
        child: Text('Count: ${count.watch(context)}'),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: increment,
        child: const Icon(Icons.add),
      ),
    );
  }
}

flutter_hooks

Using Flutter Hooks we can reduce boilerplate of StatefulWidget by switching to a HookWidget. With useState we can define the state directly in the build method and easily share them across widgets.

import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';

void main() {
  runApp(const MaterialApp(debugShowCheckedModeBanner: false, home: Counter()));
}

class Counter extends HookWidget {
  const Counter({super.key});

  @override
  Widget build(BuildContext context) {
    final count = useState(0);
    return Scaffold(
      appBar: AppBar(title: const Text('Counter')),
      body: Center(child: Text('Count: ${count.value}')),
      floatingActionButton: FloatingActionButton(
        onPressed: () => count.value++,
        child: const Icon(Icons.add),
      ),
    );
  }
}


useState returns a ValueNotifier that automatically rebuilds the widget on changes

signals_hooks

Using a new package signals_hooks we can now define signals in HookWidgets and have the benifits of a reactive graph with shareable lifecycles between widgets.

import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import 'package:signals_hooks/signals_hooks.dart';

void main() {
  runApp(const MaterialApp(debugShowCheckedModeBanner: false, home: Counter()));
}

class Counter extends HookWidget {
  const Counter({super.key});

  @override
  Widget build(BuildContext context) {
    final count = useSignal(0);
    final countStr = useComputed(() => count.value.toString());
    useSignalEffect(() {
      print('count: $count');
    });
    return Scaffold(
      appBar: AppBar(title: const Text('Counter')),
      body: Center(child: Text('Count: $countStr')),
      floatingActionButton: FloatingActionButton(
        onPressed: () => count.value++,
        child: const Icon(Icons.add),
      ),
    );
  }
}

Weekly Installs
43
Repository
rodydavis/skills
GitHub Stars
40
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass