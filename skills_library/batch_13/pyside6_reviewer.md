---
title: pyside6-reviewer
url: https://skills.sh/akiselev/qt-llm-template/pyside6-reviewer
---

# pyside6-reviewer

skills/akiselev/qt-llm-template/pyside6-reviewer
pyside6-reviewer
Installation
$ npx skills add https://github.com/akiselev/qt-llm-template --skill pyside6-reviewer
SKILL.md
PySide6 Code Reviewer

Expert code review for modern PySide6/Qt 6.8+ applications.

Review Process
Identify Qt version assumptions — Verify code targets Qt 6.8+ (no Qt5 compat)
Check thread safety — All GUI operations on main thread, proper worker patterns
Validate signal/slot usage — Modern connection syntax, proper signatures
Assess Model/View implementation — Role usage, data method patterns, index validity
Review resource management — Parent-child ownership, prevent leaks
Evaluate async patterns — QThread, QtConcurrent, asyncio integration
Check QML integration — Property bindings, type registration, context exposure
Critical Anti-Patterns (Always Flag)
# WRONG: GUI operation from worker thread
class Worker(QThread):
    def run(self):
        self.label.setText("Done")  # CRASH: Cross-thread GUI access

# WRONG: Blocking the event loop
def on_button_click(self):
    time.sleep(5)  # FREEZES UI
    requests.get(url)  # FREEZES UI

# WRONG: Old-style signal connection (Qt4/5 legacy)
self.connect(button, SIGNAL("clicked()"), self.handler)

# WRONG: String-based slot connection
button.clicked.connect("self.handler")  # Should be callable

# WRONG: No parent = memory leak risk
label = QLabel("text")  # Should have parent or be assigned to layout

# WRONG: Deleting QObject while signals pending
obj.deleteLater()  # OK
del obj  # WRONG if signals/slots active

# WRONG: Direct widget manipulation in QThread.run()
class BadWorker(QThread):
    def run(self):
        self.progress_bar.setValue(50)  # Thread violation!

Modern Patterns (Require These)
Signal/Slot Connections
# Qt 6 style - always use this
button.clicked.connect(self.on_click)
button.clicked.connect(lambda: self.handler(arg))

# Typed signals with modern syntax
class Worker(QObject):
    progress = Signal(int)          # Single type
    result = Signal(str, list)      # Multiple types
    error = Signal(Exception)       # Exception passing
    finished = Signal()             # No arguments

Thread-Safe Worker Pattern
class Worker(QObject):
    finished = Signal()
    progress = Signal(int)
    result = Signal(object)
    error = Signal(str)

    @Slot()
    def run(self):
        try:
            for i in range(100):
                # Do work
                self.progress.emit(i)
            self.result.emit(data)
        except Exception as e:
            self.error.emit(str(e))
        finally:
            self.finished.emit()

# Usage
thread = QThread()
worker = Worker()
worker.moveToThread(thread)
thread.started.connect(worker.run)
worker.finished.connect(thread.quit)
worker.finished.connect(worker.deleteLater)
thread.finished.connect(thread.deleteLater)
thread.start()

Async Integration (Qt 6.8+)
import asyncio
from PySide6.QtAsyncio import QAsyncioEventLoopPolicy

# Set up asyncio with Qt event loop
asyncio.set_event_loop_policy(QAsyncioEventLoopPolicy())

class AsyncWidget(QWidget):
    async def fetch_data(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.json()
    
    def start_fetch(self):
        asyncio.ensure_future(self.fetch_data())

Detailed Reference Files
references/signals-slots.md — Signal/slot patterns, connection types, thread-safe emission
references/model-view.md — QAbstractItemModel, roles, proxies, delegates
references/threading.md — QThread, QtConcurrent, async patterns, thread pools
references/widgets.md — Widget lifecycle, layouts, styling, high-DPI
references/qml-integration.md — QML/Python bridge, properties, type registration
references/performance.md — Paint optimization, model efficiency, lazy loading
references/anti-patterns.md — Comprehensive anti-pattern catalog with fixes
Review Checklist (Use for PRs)
Thread Safety
 All widget/GUI calls on main thread only
 Workers use signal/slot for UI updates
 No time.sleep() or blocking calls in main thread
 QThread subclass only overrides run(), not constructor work
 moveToThread() used correctly (object has no parent)
Memory Management
 Widgets have parents OR are added to layouts
 deleteLater() used for QObjects, never del
 Lambda connections don't capture stale references
 Circular signal connections avoided
 Model data returned by value, not reference
Signal/Slot Correctness
 Modern connection syntax (no strings)
 Signal signatures match slot signatures
 @Slot() decorator on all slots
 Qt.QueuedConnection for cross-thread signals
 Signals defined as class attributes
Model/View
 beginInsertRows()/endInsertRows() bracket changes
 dataChanged emitted for updates
 index.isValid() checked before access
 Custom roles use Qt.UserRole + n
 roleNames() override for QML compatibility
Performance
 No widget creation in paint events
 update() not repaint() for redraws
 Large lists use QAbstractItemModel (not QListWidget)
 Lazy loading for expensive data
 blockSignals() during batch updates
Qt 6.8+ Specifics
 Using new enum scoping (Qt.AlignmentFlag.AlignCenter)
 QtAsyncio for async patterns (not third-party)
 QML_ELEMENT macro equivalents for type registration
 Property bindings via QProperty where appropriate
 New QPermission API for platform permissions
Weekly Installs
65
Repository
akiselev/qt-llm-template
GitHub Stars
1
First Seen
Feb 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass