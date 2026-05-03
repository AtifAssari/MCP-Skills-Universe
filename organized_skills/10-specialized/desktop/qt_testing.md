---
rating: ⭐⭐⭐
title: qt-testing
url: https://skills.sh/talmolab/sleap/qt-testing
---

# qt-testing

skills/talmolab/sleap/qt-testing
qt-testing
Installation
$ npx skills add https://github.com/talmolab/sleap --skill qt-testing
SKILL.md
Qt GUI Testing

Capture screenshots of Qt widgets for visual inspection without displaying windows on screen.

Quick Start
# Capture any widget
from scripts.qt_capture import capture_widget
path = capture_widget(my_widget, "description_here")
# Then read the screenshot with the Read tool

Core Script

Run scripts/qt_capture.py or import capture_widget from it:

# Standalone test
uv run --with PySide6 python .claude/skills/qt-testing/scripts/qt_capture.py

Output Location

All screenshots save to: scratch/.qt-screenshots/

Naming: {YYYY-MM-DD.HH-MM-SS}_{description}.png

Workflow
Create/obtain the widget to test
Call capture_widget(widget, "description")
Read the saved screenshot with the Read tool
Analyze with vision to verify correctness
Interaction Pattern

To interact with widgets (click buttons, etc.):

# Find widget at coordinates (from vision analysis)
target = widget.childAt(x, y)

# Trigger it directly (not mouse events)
if hasattr(target, 'click'):
    target.click()
    QApplication.processEvents()

# Capture result
capture_widget(widget, "after_click")

Example: Test a Dialog
import sys
from PySide6.QtWidgets import QApplication
from sleap.gui.learning.dialog import TrainingEditorDialog

# Add skill scripts to path
sys.path.insert(0, ".claude/skills/qt-testing")
from scripts.qt_capture import capture_widget, init_qt

app = init_qt()
dialog = TrainingEditorDialog()
path = capture_widget(dialog, "training_dialog")
dialog.close()
print(f"Inspect: {path}")

Key Points
Uses Qt.WA_DontShowOnScreen - no window popup
Renders identically to on-screen display (verified)
Call processEvents() after interactions before capture
Use childAt(x, y) to map vision coordinates to widgets
Direct method calls (.click()) work; simulated mouse events don't
Weekly Installs
13
Repository
talmolab/sleap
GitHub Stars
571
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass