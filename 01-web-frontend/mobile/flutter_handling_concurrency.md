---
rating: ⭐⭐
title: flutter-handling-concurrency
url: https://skills.sh/flutter/skills/flutter-handling-concurrency
---

# flutter-handling-concurrency

skills/flutter/skills/flutter-handling-concurrency
flutter-handling-concurrency
Installation
$ npx skills add https://github.com/flutter/skills --skill flutter-handling-concurrency
Summary

Offload CPU-intensive tasks to background isolates while keeping Flutter UIs responsive.

Provides three concurrency patterns: async/await for I/O-bound work, Isolate.run() for one-off heavy computations, and Isolate.spawn() with message passing for persistent background workers
Includes a decision matrix to choose between async operations and isolates based on task type (I/O vs. CPU-bound) and execution frequency
Covers three complete workflows with step-by-step task checklists: standard async UI with FutureBuilder, short-lived isolate offloading, and long-lived bidirectional worker communication
Provides three runnable code examples demonstrating FutureBuilder patterns, JSON decoding in isolates, and ReceivePort/SendPort message passing architecture
SKILL.md
Managing Dart Concurrency and Isolates
Contents
Core Concepts
Decision Matrix: Async vs. Isolates
Workflows
Implementing Standard Asynchronous UI
Offloading Short-Lived Heavy Computation
Establishing Long-Lived Worker Isolates
Examples
Core Concepts

Dart utilizes a single-threaded execution model driven by an Event Loop (comparable to the iOS main loop). By default, all Flutter application code runs on the Main Isolate.

Asynchronous Operations (async/await): Use for non-blocking I/O tasks (network requests, file access). The Event Loop continues processing other events while waiting for the Future to complete.
Isolates: Dart's implementation of lightweight threads. Isolates possess their own isolated memory and do not share state. They communicate exclusively via message passing.
Main Isolate: The default thread where UI rendering and event handling occur. Blocking this isolate causes UI freezing (jank).
Worker Isolate: A spawned isolate used to offload CPU-bound tasks (e.g., decoding large JSON blobs) to prevent Main Isolate blockage.
Decision Matrix: Async vs. Isolates

Apply the following conditional logic to determine the correct concurrency approach:

If the task is I/O bound (e.g., HTTP request, database read) -> Use async/await on the Main Isolate.
If the task is CPU-bound but executes quickly (< 16ms) -> Use async/await on the Main Isolate.
If the task is CPU-bound, takes significant time, and runs once (e.g., parsing a massive JSON payload) -> Use Isolate.run().
If the task requires continuous or repeated background processing with multiple messages passed over time -> Use Isolate.spawn() with ReceivePort and SendPort.
Workflows
Implementing Standard Asynchronous UI

Use this workflow to fetch and display non-blocking asynchronous data.

Task Progress:

 Mark the data-fetching function with the async keyword.
 Return a Future<T> from the function.
 Use the await keyword to yield execution until the operation completes.
 Wrap the UI component in a FutureBuilder<T> (or StreamBuilder for streams).
 Handle ConnectionState.waiting, hasError, and hasData states within the builder.
 Run validator -> review UI for loading indicators -> fix missing states.
Offloading Short-Lived Heavy Computation

Use this workflow for one-off, CPU-intensive tasks using Dart 2.19+.

Task Progress:

 Identify the CPU-bound operation blocking the Main Isolate.
 Extract the computation into a standalone callback function.
 Ensure the callback function signature accepts exactly one required, unnamed argument (as per specific architectural constraints).
 Invoke Isolate.run() passing the callback.
 await the result of Isolate.run() in the Main Isolate.
 Assign the returned value to the application state.
Establishing Long-Lived Worker Isolates

Use this workflow for persistent background processes requiring continuous bidirectional communication.

Task Progress:

 Instantiate a ReceivePort on the Main Isolate to listen for messages.
 Spawn the worker isolate using Isolate.spawn(), passing the ReceivePort.sendPort as the initial message.
 In the worker isolate, instantiate its own ReceivePort.
 Send the worker's SendPort back to the Main Isolate via the initial port.
 Store the worker's SendPort in the Main Isolate for future message dispatching.
 Implement listeners on both ReceivePort instances to handle incoming messages.
 Run validator -> review memory leaks -> ensure ports are closed when the isolate is no longer needed.
Examples
Example 1: Asynchronous UI with FutureBuilder
// 1. Define the async operation
Future<String> fetchUserData() async {
  await Future.delayed(const Duration(seconds: 2)); // Simulate network I/O
  return "User Data Loaded";
}

// 2. Consume in the UI
Widget build(BuildContext context) {
  return FutureBuilder<String>(
    future: fetchUserData(),
    builder: (context, snapshot) {
      if (snapshot.connectionState == ConnectionState.waiting) {
        return const CircularProgressIndicator();
      } else if (snapshot.hasError) {
        return Text('Error: ${snapshot.error}');
      } else {
        return Text('Result: ${snapshot.data}');
      }
    },
  );
}

Example 2: Short-Lived Isolate (Isolate.run)
import 'dart:isolate';
import 'dart:convert';

// 1. Define the heavy computation callback
// Note: Adhering to the strict single-argument signature requirement.
List<dynamic> decodeHeavyJson(String jsonString) {
  return jsonDecode(jsonString) as List<dynamic>;
}

// 2. Offload to a worker isolate
Future<List<dynamic>> processDataInBackground(String rawJson) async {
  // Isolate.run spawns the isolate, runs the computation, returns the value, and exits.
  final result = await Isolate.run(() => decodeHeavyJson(rawJson));
  return result;
}

Example 3: Long-Lived Isolate (ReceivePort / SendPort)
import 'dart:isolate';

class WorkerManager {
  late SendPort _workerSendPort;
  final ReceivePort _mainReceivePort = ReceivePort();
  Isolate? _isolate;

  Future<void> initialize() async {
    // 1. Spawn isolate and pass the Main Isolate's SendPort
    _isolate = await Isolate.spawn(_workerEntry, _mainReceivePort.sendPort);

    // 2. Listen for messages from the Worker Isolate
    _mainReceivePort.listen((message) {
      if (message is SendPort) {
        // First message is the Worker's SendPort
        _workerSendPort = message;
        _startCommunication();
      } else {
        // Subsequent messages are data payloads
        print('Main Isolate received: $message');
      }
    });
  }

  void _startCommunication() {
    // Send data to the worker
    _workerSendPort.send("Process this data");
  }

  // 3. Worker Isolate Entry Point
  static void _workerEntry(SendPort mainSendPort) {
    final workerReceivePort = ReceivePort();
    
    // Send the Worker's SendPort back to the Main Isolate
    mainSendPort.send(workerReceivePort.sendPort);

    // Listen for incoming tasks
    workerReceivePort.listen((message) {
      print('Worker Isolate received: $message');
      
      // Perform work and send result back
      final result = "Processed: $message";
      mainSendPort.send(result);
    });
  }

  void dispose() {
    _mainReceivePort.close();
    _isolate?.kill();
  }
}

Weekly Installs
8.5K
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