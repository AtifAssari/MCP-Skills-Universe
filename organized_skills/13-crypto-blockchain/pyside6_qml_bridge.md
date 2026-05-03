---
rating: ⭐⭐⭐
title: pyside6-qml-bridge
url: https://skills.sh/ds-codi/project-memory-mcp/pyside6-qml-bridge
---

# pyside6-qml-bridge

skills/ds-codi/project-memory-mcp/pyside6-qml-bridge
pyside6-qml-bridge
Installation
$ npx skills add https://github.com/ds-codi/project-memory-mcp --skill pyside6-qml-bridge
SKILL.md
PySide6 QML Bridge Layer

The bridge layer is the critical interface between Python business logic and QML views. Bridge classes are QObject subclasses that expose properties, signals, and slots to QML via Qt's meta-object system.

Bridge Architecture
┌──────────────────────────────────────────────┐
│                QML View                      │
│  Text { text: jobBridge.jobNumber }          │
│  Button { onClicked: jobBridge.activateJob() }│
└───────────────┬──────────────────────────────┘
                │  Property bindings, signal connections
┌───────────────▼──────────────────────────────┐
│           Bridge (QObject)                   │
│  @Property, @Slot, Signal                    │
│  Delegates to Controller                     │
└───────────────┬──────────────────────────────┘
                │
┌───────────────▼──────────────────────────────┐
│           Controller                         │
│  Business logic, model updates               │
└──────────────────────────────────────────────┘

Bridge Class Pattern
"""views/bridge.py — QObject bridge classes exposed to QML."""
from PySide6.QtCore import QObject, Property, Signal, Slot, QStringListModel
from PySide6.QtQml import QmlElement

from my_app.controllers.job_controller import JobController
from my_app.utils.signals import SignalRegistry


class JobBridge(QObject):
    """
    Bridge between QML views and the JobController.
    
    Exposes job data as Qt properties with NOTIFY signals
    and controller actions as invokable slots.
    """
    
    # --- NOTIFY Signals (one per property group) ---
    job_number_changed = Signal()
    job_name_changed = Signal()
    is_busy_changed = Signal()
    jobs_list_changed = Signal()
    error_changed = Signal()

    def __init__(
        self,
        controller: JobController,
        signals: SignalRegistry,
        parent: QObject | None = None,
    ) -> None:
        super().__init__(parent)
        self._controller = controller
        self._signals = signals
        
        # Internal state (backing fields for properties)
        self._job_number: str = ""
        self._job_name: str = ""
        self._is_busy: bool = False
        self._jobs_list: list[str] = []
        self._error_message: str = ""
        
        # Connect to application signals
        self._signals.job_changed.connect(self._on_job_changed)

    # -----------------------------------------------------------------
    # Qt Properties (exposed to QML via Property decorator)
    # -----------------------------------------------------------------

    @Property(str, notify=job_number_changed)
    def jobNumber(self) -> str:
        return self._job_number

    @Property(str, notify=job_name_changed)
    def jobName(self) -> str:
        return self._job_name

    @Property(bool, notify=is_busy_changed)
    def isBusy(self) -> bool:
        return self._is_busy

    @Property(list, notify=jobs_list_changed)
    def jobsList(self) -> list:
        return self._jobs_list

    @Property(str, notify=error_changed)
    def errorMessage(self) -> str:
        return self._error_message

    # -----------------------------------------------------------------
    # Slots (callable from QML)
    # -----------------------------------------------------------------

    @Slot(str)
    def activateJob(self, job_id: str) -> None:
        """Activate a job — delegates to controller."""
        self._set_busy(True)
        success = self._controller.activate_job(job_id)
        if not success:
            self._set_error("Failed to activate job")
        self._set_busy(False)

    @Slot(str, result=bool)
    def createJob(self, job_number: str) -> bool:
        """Create a new job — returns success."""
        return self._controller.create_job(job_number)

    @Slot()
    def refreshJobs(self) -> None:
        """Reload the jobs list from repository."""
        jobs = self._controller.get_all_jobs()
        self._jobs_list = [j.job_number for j in jobs]
        self.jobs_list_changed.emit()

    @Slot(str)
    def openJobFolder(self, job_id: str) -> None:
        """Open job folder in file explorer."""
        self._controller.open_job_folder(job_id)

    # -----------------------------------------------------------------
    # Internal signal handlers
    # -----------------------------------------------------------------

    def _on_job_changed(self, job_id: str) -> None:
        """Handle global job_changed signal."""
        job = self._controller.get_job(job_id)
        if job:
            self._job_number = job.job_number
            self._job_name = job.job_name or ""
            self.job_number_changed.emit()
            self.job_name_changed.emit()

    # -----------------------------------------------------------------
    # Private helpers
    # -----------------------------------------------------------------

    def _set_busy(self, busy: bool) -> None:
        if self._is_busy != busy:
            self._is_busy = busy
            self.is_busy_changed.emit()

    def _set_error(self, message: str) -> None:
        self._error_message = message
        self.error_changed.emit()

Registering Bridges with QML
Option A: Context Properties (recommended for singletons)
# In app.py — _register_qml_types()
def _register_qml_types(self) -> None:
    ctx = self._engine.rootContext()

    self._job_bridge = JobBridge(
        controller=self._controllers["job"],
        signals=self._signals,
    )
    ctx.setContextProperty("jobBridge", self._job_bridge)

    self._settings_bridge = SettingsBridge(
        controller=self._controllers["settings"],
        signals=self._signals,
    )
    ctx.setContextProperty("settingsBridge", self._settings_bridge)


Usage in QML:

Text { text: jobBridge.jobNumber }
Button { onClicked: jobBridge.activateJob("1234567") }

Option B: QML Type Registration (for instantiable types)
from PySide6.QtQml import qmlRegisterType

# Register before engine.load()
qmlRegisterType(JobBridge, "MyApp", 1, 0, "JobBridge")


Usage in QML:

import MyApp 1.0

JobBridge {
    id: jobBridge
    // properties auto-bound
}

Option C: QmlElement Decorator (PySide6 6.5+)
from PySide6.QtQml import QmlElement

QML_IMPORT_NAME = "MyApp"
QML_IMPORT_MAJOR_VERSION = 1
QML_IMPORT_MINOR_VERSION = 0

@QmlElement
class JobBridge(QObject):
    ...

Property Type Mapping
Python Type	Qt/QML Type	Property Decorator	Notes
str	string	Property(str, ...)	Most common
int	int	Property(int, ...)	
float	real / double	Property(float, ...)	
bool	bool	Property(bool, ...)	
list	var (JS array)	Property(list, ...)	Copies to JS array
dict	var (JS object)	Property('QVariant', ...)	Use QVariant type hint
QUrl	url	Property(QUrl, ...)	For file/resource paths
QColor	color	Property(QColor, ...)	
QStringList	list<string>	Property('QStringList', ...)	Preferred for string lists
QVariantList	var	Property('QVariantList', ...)	For mixed-type lists
QVariantMap	var	Property('QVariantMap', ...)	For key-value objects
Exposing List Models to QML

For table/list views, use QAbstractListModel:

from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex

class JobListModel(QAbstractListModel):
    """Exposes a list of jobs for QML ListView/Repeater."""

    # Custom roles
    JobNumberRole = Qt.UserRole + 1
    JobNameRole = Qt.UserRole + 2
    StatusRole = Qt.UserRole + 3

    def __init__(self, parent=None):
        super().__init__(parent)
        self._jobs: list[dict] = []

    def roleNames(self):
        return {
            self.JobNumberRole: b"jobNumber",
            self.JobNameRole: b"jobName",
            self.StatusRole: b"status",
        }

    def rowCount(self, parent=QModelIndex()):
        return len(self._jobs)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or index.row() >= len(self._jobs):
            return None
        job = self._jobs[index.row()]
        if role == self.JobNumberRole:
            return job.get("job_number", "")
        if role == self.JobNameRole:
            return job.get("job_name", "")
        if role == self.StatusRole:
            return job.get("status", "")
        return None

    def update_jobs(self, jobs: list[dict]) -> None:
        """Replace the jobs list and notify QML."""
        self.beginResetModel()
        self._jobs = jobs
        self.endResetModel()


Register as context property:

ctx.setContextProperty("jobListModel", self._job_list_model)


Use in QML:

ListView {
    model: jobListModel
    delegate: Row {
        Text { text: jobNumber }
        Text { text: jobName }
        Text { text: status }
    }
}

Naming Conventions
Context	Convention	Example
Python class names	PascalCase	JobBridge
Python backing fields	_snake_case	self._job_number
Qt Property names	camelCase	jobNumber
Signal names	snake_case (Python)	job_number_changed
Slot names	camelCase (QML-facing)	activateJob
QML context property	camelCase	jobBridge
Common Anti-Patterns
Never embed business logic in the bridge
# ❌ WRONG — bridge doing controller work
@Slot(str)
def activateJob(self, job_id: str) -> None:
    job = self._repository.get_job(job_id)  # NO direct DB access
    self._ini_service.write(job)            # NO service calls
    self._broker.publish("job.activated")   # NO broker calls

# ✅ CORRECT — bridge delegates to controller
@Slot(str)
def activateJob(self, job_id: str) -> None:
    self._controller.activate_job(job_id)

Never manipulate QML from Python
# ❌ WRONG — reaching into QML from Python
root = self._engine.rootObjects()[0]
label = root.findChild(QObject, "statusLabel")
label.setProperty("text", "Active")

# ✅ CORRECT — update a property, QML binding does the rest
self._status_text = "Active"
self.status_text_changed.emit()

Always emit NOTIFY signals
# ❌ WRONG — property changes without notification
self._job_number = "1234567"

# ✅ CORRECT — emit so QML bindings update
self._job_number = "1234567"
self.job_number_changed.emit()

Thread Safety

For long-running operations, use QThread or Python threads with signal marshalling:

from PySide6.QtCore import QThread, Signal

class WorkerThread(QThread):
    finished = Signal(object)  # result
    error = Signal(str)        # error message

    def __init__(self, task_fn, parent=None):
        super().__init__(parent)
        self._task_fn = task_fn

    def run(self):
        try:
            result = self._task_fn()
            self.finished.emit(result)
        except Exception as e:
            self.error.emit(str(e))

# In bridge:
@Slot()
def loadJobsAsync(self) -> None:
    self._set_busy(True)
    worker = WorkerThread(self._controller.get_all_jobs, self)
    worker.finished.connect(self._on_jobs_loaded)
    worker.error.connect(self._on_load_error)
    worker.start()

def _on_jobs_loaded(self, jobs) -> None:
    self._jobs_list = [j.job_number for j in jobs]
    self.jobs_list_changed.emit()
    self._set_busy(False)

References
PySide6 QML Integration Tutorial
PySide6 Property System
QAbstractListModel in PySide6
Weekly Installs
32
Repository
ds-codi/project…mory-mcp
GitHub Stars
4
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass