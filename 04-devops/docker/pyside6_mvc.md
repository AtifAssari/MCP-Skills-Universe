---
title: pyside6-mvc
url: https://skills.sh/ds-codi/project-memory-mcp/pyside6-mvc
---

# pyside6-mvc

skills/ds-codi/project-memory-mcp/pyside6-mvc
pyside6-mvc
Installation
$ npx skills add https://github.com/ds-codi/project-memory-mcp --skill pyside6-mvc
SKILL.md
PySide6 MVC Architecture Instructions

Guidelines for building Python desktop applications using PySide6 with strict MVC architecture where all UI is defined by .ui files.

Architecture Overview
┌─────────────────────────────────────────┐
│           View Layer (.ui files)        │
│  Load from Qt Designer, capture input   │
└──────────────────┬──────────────────────┘
                   │ Signals
┌──────────────────▼──────────────────────┐
│           Controller Layer              │
│  Coordinate models & services           │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│           Model Layer                   │
│  Data structures, validation            │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│           Services Layer                │
│  Database, files, network, broker       │
└─────────────────────────────────────────┘

Project Structure
my_app/
├── app.py                    # Bootstrap & DI container
├── __main__.py               # Entry point
├── controllers/
│   ├── base.py               # BaseController
│   └── *_controller.py       # Domain controllers
├── models/
│   ├── base.py               # BaseModel with signals
│   └── *.py                  # Domain models
├── views/
│   ├── base.py               # BaseView
│   └── *.py                  # View classes
├── services/
│   └── *.py                  # External interactions
├── resources/
│   └── ui/                   # .ui files (Qt Designer)
└── utils/
    └── signals.py            # Central signal registry

Core Principles
Component	Responsibility	Does NOT
Model	Data, validation, serialization	Touch UI, call services
View	Load .ui files, capture input	Contain business logic
Controller	Coordinate models & services	Manipulate UI directly
Base Model Pattern
from PySide6.QtCore import QObject, Signal
from datetime import datetime
from typing import Any

class BaseModel(QObject):
    property_changed = Signal(str, object)  # name, value
    changed = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._updated_at = datetime.now()
    
    def _set_property(self, name: str, old: Any, new: Any) -> bool:
        if old != new:
            self._updated_at = datetime.now()
            self.property_changed.emit(name, new)
            self.changed.emit()
            return True
        return False
    
    def to_dict(self) -> dict:
        raise NotImplementedError
    
    @classmethod
    def from_dict(cls, data: dict):
        raise NotImplementedError

Base View Pattern
from pathlib import Path
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import QFile, Signal
from PySide6.QtUiTools import QUiLoader

class BaseView(QWidget):
    error_occurred = Signal(str, str)  # title, message
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._controller = None
        self._init_ui()
        self._connect_signals()
    
    def _load_ui(self, ui_filename: str) -> QWidget:
        ui_path = Path(__file__).parent.parent / "resources" / "ui" / ui_filename
        loader = QUiLoader()
        ui_file = QFile(str(ui_path))
        
        if ui_file.open(QFile.ReadOnly):
            ui = loader.load(ui_file, self)
            ui_file.close()
            
            layout = QVBoxLayout(self)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.addWidget(ui)
            return ui
        raise FileNotFoundError(f"Cannot open: {ui_path}")
    
    def _init_ui(self):
        pass  # Override: load .ui file
    
    def _connect_signals(self):
        pass  # Override: connect handlers
    
    def set_controller(self, controller):
        self._controller = controller
    
    def refresh(self):
        pass  # Override: update from model

Base Controller Pattern
from PySide6.QtCore import QObject

class BaseController(QObject):
    def __init__(self, signals, parent=None):
        super().__init__(parent)
        self._signals = signals
        self._views = []
    
    def register_view(self, view):
        if view not in self._views:
            self._views.append(view)
            view.set_controller(self)
    
    def notify_views(self):
        for view in self._views:
            view.refresh()
    
    def initialize(self):
        pass  # Override: setup logic
    
    def cleanup(self):
        self._views.clear()

Central Signal Registry
from PySide6.QtCore import QObject, Signal

class SignalRegistry(QObject):
    # Domain signals
    job_changed = Signal(str)         # job_id
    job_created = Signal(str)         # job_id
    settings_changed = Signal(str, object)  # key, value
    
    # Connection signals
    broker_connected = Signal(bool)   # connected
    
    # UI signals
    error_occurred = Signal(str, str)  # title, message
    app_closing = Signal()

# Singleton
_registry = None

def get_signal_registry():
    global _registry
    if _registry is None:
        _registry = SignalRegistry()
    return _registry

Application Bootstrap (DI Container)
import sys
from PySide6.QtWidgets import QApplication
from my_app.utils.signals import get_signal_registry

class MyApplication:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        self._qt_app = None
        self._services = {}
        self._controllers = {}
        self._signals = get_signal_registry()
    
    def _register_services(self):
        self._services["db"] = DatabaseService()
    
    def _register_controllers(self):
        self._controllers["job"] = JobController(
            signals=self._signals,
            db=self._services["db"],
        )
        for c in self._controllers.values():
            c.initialize()
    
    def run(self) -> int:
        self._qt_app = QApplication(sys.argv)
        self._register_services()
        self._register_controllers()
        
        window = MainWindow(self._signals, self._controllers)
        window.show()
        return self._qt_app.exec()

Widget Naming Conventions (.ui files)
Widget Type	Pattern	Example
Label	*_label	job_number_label
Button	*_btn	save_btn
Line Edit	*_input	customer_input
List	*_list	jobs_list
Table	*_table	pieces_table
Combo	*_combo	status_combo
Signal Flow
User Action (View)
       ↓
    View emits signal
       ↓
    Controller handles action
       ↓
    Service performs operation
       ↓
    SignalRegistry.emit()
       ↓
    Views call refresh()

Best Practices
1. Never Create UI Programmatically

❌ Wrong:

layout = QVBoxLayout()
btn = QPushButton("Click")
layout.addWidget(btn)


✅ Correct:

self._ui = self._load_ui("my_widget.ui")
self._btn = self._ui.findChild(QPushButton, "action_btn")

2. Controllers Never Touch UI

❌ Wrong:

def activate_job(self):
    self._view.label.setText(job.name)  # NO!


✅ Correct:

def activate_job(self):
    self._signals.job_changed.emit(job_id)  # Views subscribe

3. Views Subscribe to Signals
def _connect_signals(self):
    self._signals.job_changed.connect(self._on_job_changed)

def _on_job_changed(self, job_id):
    self.refresh()

4. Provide Fallback UI
def _init_ui(self):
    try:
        self._ui = self._load_ui("widget.ui")
    except FileNotFoundError:
        self._create_fallback_ui()

5. Use Services for External Operations

Controllers delegate to services:

Database queries → Repository services
File operations → File service
Network calls → API service
IPC → Broker client
Common Imports
# Qt
from PySide6.QtWidgets import QWidget, QMainWindow
from PySide6.QtCore import Signal, Slot, QFile
from PySide6.QtUiTools import QUiLoader

# Project
from my_app.utils.signals import get_signal_registry
from my_app.controllers.base import BaseController
from my_app.views.base import BaseView
from my_app.models.base import BaseModel

References
Qt Designer Manual
PySide6 Documentation
Weekly Installs
95
Repository
ds-codi/project…mory-mcp
GitHub Stars
4
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass