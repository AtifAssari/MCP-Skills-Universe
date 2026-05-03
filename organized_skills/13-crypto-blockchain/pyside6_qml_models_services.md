---
rating: ⭐⭐⭐
title: pyside6-qml-models-services
url: https://skills.sh/ds-codi/project-memory-mcp/pyside6-qml-models-services
---

# pyside6-qml-models-services

skills/ds-codi/project-memory-mcp/pyside6-qml-models-services
pyside6-qml-models-services
Installation
$ npx skills add https://github.com/ds-codi/project-memory-mcp --skill pyside6-qml-models-services
SKILL.md
PySide6 QML Models & Services

The model and service layers form the backend of the MVC architecture. Models define data structures with Qt signal support; services handle all external interactions; the signal registry provides decoupled cross-layer communication.

Model Layer
BaseModel

All domain models inherit from BaseModel to gain Qt signal support and serialization:

"""models/base.py"""
from datetime import datetime
from typing import Any, TypeVar, Type
from PySide6.QtCore import QObject, Signal

T = TypeVar('T', bound='BaseModel')


class BaseModel(QObject):
    """
    Base class for all domain models.
    
    Provides:
    - property_changed(name, value) signal for reactive updates
    - changed() signal for any modification
    - _set_property() helper for consistent change notification
    - to_dict() / from_dict() for serialization
    """

    property_changed = Signal(str, object)  # name, value
    changed = Signal()

    def __init__(self, parent: QObject | None = None) -> None:
        super().__init__(parent)
        self._created_at: datetime = datetime.now()
        self._updated_at: datetime = datetime.now()

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def updated_at(self) -> datetime:
        return self._updated_at

    def _set_property(self, name: str, old_value: Any, new_value: Any) -> bool:
        """Set a property, emit signals if changed. Returns True if changed."""
        if old_value != new_value:
            self._updated_at = datetime.now()
            self.property_changed.emit(name, new_value)
            self.changed.emit()
            return True
        return False

    def to_dict(self) -> dict[str, Any]:
        raise NotImplementedError("Subclasses must implement to_dict()")

    @classmethod
    def from_dict(cls: Type[T], data: dict[str, Any]) -> T:
        raise NotImplementedError("Subclasses must implement from_dict()")

Domain Model Example
"""models/job.py"""
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any, Optional

from PySide6.QtCore import Signal
from my_app.models.base import BaseModel


class JobStatus(Enum):
    ACTIVE = "active"
    COMPLETE = "complete"
    ARCHIVED = "archived"
    ON_HOLD = "on_hold"


@dataclass
class JobFile:
    """Value object for files associated with a job."""
    path: Path
    file_type: str
    file_name: str
    size_bytes: int = 0
    modified_at: datetime = field(default_factory=datetime.now)

    def to_dict(self) -> dict[str, Any]:
        return {
            "path": str(self.path),
            "file_type": self.file_type,
            "file_name": self.file_name,
            "size_bytes": self.size_bytes,
            "modified_at": self.modified_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "JobFile":
        return cls(
            path=Path(data["path"]),
            file_type=data["file_type"],
            file_name=data["file_name"],
            size_bytes=data.get("size_bytes", 0),
            modified_at=datetime.fromisoformat(data.get("modified_at", "")),
        )


class Job(BaseModel):
    """Domain model for a production job."""

    files_updated = Signal()

    def __init__(
        self,
        job_number: str,
        job_name: str = "",
        status: JobStatus = JobStatus.ACTIVE,
        parent=None,
    ) -> None:
        super().__init__(parent)
        self._job_number = job_number
        self._job_name = job_name
        self._status = status
        self._files: list[JobFile] = []

    # --- Properties with change notification ---

    @property
    def job_number(self) -> str:
        return self._job_number

    @property
    def job_name(self) -> str:
        return self._job_name

    @job_name.setter
    def job_name(self, value: str) -> None:
        if self._set_property("job_name", self._job_name, value):
            self._job_name = value

    @property
    def status(self) -> JobStatus:
        return self._status

    @status.setter
    def status(self, value: JobStatus) -> None:
        if self._set_property("status", self._status, value):
            self._status = value

    @property
    def files(self) -> list[JobFile]:
        return list(self._files)

    def add_file(self, file: JobFile) -> None:
        self._files.append(file)
        self.files_updated.emit()
        self.changed.emit()

    # --- Serialization ---

    def to_dict(self) -> dict[str, Any]:
        return {
            "job_number": self._job_number,
            "job_name": self._job_name,
            "status": self._status.value,
            "files": [f.to_dict() for f in self._files],
            "created_at": self._created_at.isoformat(),
            "updated_at": self._updated_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Job":
        job = cls(
            job_number=data["job_number"],
            job_name=data.get("job_name", ""),
            status=JobStatus(data.get("status", "active")),
        )
        for f in data.get("files", []):
            job._files.append(JobFile.from_dict(f))
        return job

Model Design Rules
Rule	Rationale
Always use _set_property() for mutable fields	Ensures signals fire consistently
Use @dataclass for value objects (no signals needed)	Lightweight, immutable data
Use BaseModel for entities tracked by controllers	Reactive updates to UI
Never import services or views in models	Pure data layer
Implement to_dict() / from_dict()	Enables persistence and serialization
Use Enums for constrained values	Type safety, IDE autocomplete
Application State

A singleton that tracks transient UI state (not persisted domain data):

"""models/state.py"""
from PySide6.QtCore import QObject, Signal


class ApplicationState(QObject):
    """
    Singleton for transient application state.
    
    Tracks current UI state such as active selection,
    navigation position, and loading flags.
    """

    active_job_changed = Signal(str)  # job_id or ""
    navigation_changed = Signal(int)  # page index

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init_state()
        return cls._instance

    def _init_state(self):
        super().__init__()
        self._active_job_id: str | None = None
        self._current_page: int = 0

    @property
    def active_job_id(self) -> str | None:
        return self._active_job_id

    @active_job_id.setter
    def active_job_id(self, value: str | None) -> None:
        if self._active_job_id != value:
            self._active_job_id = value
            self.active_job_changed.emit(value or "")

    @property
    def current_page(self) -> int:
        return self._current_page

    @current_page.setter
    def current_page(self, value: int) -> None:
        if self._current_page != value:
            self._current_page = value
            self.navigation_changed.emit(value)

Signal Registry

Central registry of all application-wide signals. Views, controllers, and bridges connect to these:

"""utils/signals.py"""
from PySide6.QtCore import QObject, Signal


class SignalRegistry(QObject):
    """
    Central signal definitions for the application.
    
    All cross-layer communication flows through these signals.
    Organized by domain area.
    """

    # --- Job Signals ---
    job_changed = Signal(str)           # job_id
    job_created = Signal(str)           # job_id
    job_updated = Signal(str, str)      # job_id, field
    job_deleted = Signal(str)           # job_id
    job_files_updated = Signal(str, int)  # job_id, file_count

    # --- Settings Signals ---
    settings_changed = Signal(str, object)  # key, value
    settings_reset = Signal(str)            # category or ""

    # --- Connection Signals ---
    broker_status_changed = Signal(bool)     # connected
    broker_message_received = Signal(str, str)  # topic, payload

    # --- UI Signals ---
    theme_changed = Signal(str)         # "light" or "dark"
    view_focus_requested = Signal(str)  # view_name
    error_occurred = Signal(str, str)   # title, message
    app_closing = Signal()


# Singleton accessor
_registry: SignalRegistry | None = None

def get_signal_registry() -> SignalRegistry:
    global _registry
    if _registry is None:
        _registry = SignalRegistry()
    return _registry

Service Layer
Repository Pattern
"""services/database/jobs_repository.py"""
import sqlite3
import logging
from pathlib import Path
from typing import Optional

from my_app.models.job import Job

logger = logging.getLogger(__name__)


class JobsRepository:
    """
    SQLite-backed repository for job persistence.
    
    Follows the repository pattern — controllers call these methods,
    never raw SQL.
    """

    def __init__(self, db_path: Path) -> None:
        self._db_path = db_path
        self._ensure_schema()

    def _ensure_schema(self) -> None:
        with sqlite3.connect(self._db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS jobs (
                    job_number TEXT PRIMARY KEY,
                    job_name TEXT DEFAULT '',
                    status TEXT DEFAULT 'active',
                    data_json TEXT DEFAULT '{}',
                    created_at TEXT,
                    updated_at TEXT
                )
            """)

    def get_job(self, job_number: str) -> Optional[Job]:
        with sqlite3.connect(self._db_path) as conn:
            conn.row_factory = sqlite3.Row
            row = conn.execute(
                "SELECT * FROM jobs WHERE job_number = ?",
                (job_number,),
            ).fetchone()
        if row:
            return self._row_to_job(row)
        return None

    def save_job(self, job: Job) -> None:
        import json
        data = job.to_dict()
        with sqlite3.connect(self._db_path) as conn:
            conn.execute("""
                INSERT OR REPLACE INTO jobs
                (job_number, job_name, status, data_json, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                data["job_number"],
                data["job_name"],
                data["status"],
                json.dumps(data),
                data["created_at"],
                data["updated_at"],
            ))

    def get_all_jobs(self) -> list[Job]:
        with sqlite3.connect(self._db_path) as conn:
            conn.row_factory = sqlite3.Row
            rows = conn.execute(
                "SELECT * FROM jobs ORDER BY updated_at DESC"
            ).fetchall()
        return [self._row_to_job(r) for r in rows]

    def delete_job(self, job_number: str) -> bool:
        with sqlite3.connect(self._db_path) as conn:
            cursor = conn.execute(
                "DELETE FROM jobs WHERE job_number = ?",
                (job_number,),
            )
        return cursor.rowcount > 0

    def _row_to_job(self, row) -> Job:
        import json
        data = json.loads(row["data_json"])
        return Job.from_dict(data)

Service Pattern

Services wrap external interactions — file I/O, network calls, subprocess execution:

"""services/file_discovery.py"""
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class FileDiscoveryService:
    """Discovers and indexes files in job directories."""

    SUPPORTED_EXTENSIONS = {".dxf", ".pdf", ".top", ".xml", ".nc"}

    def __init__(self, base_path: Path) -> None:
        self._base_path = base_path

    def initialize(self) -> None:
        self._base_path.mkdir(parents=True, exist_ok=True)

    def shutdown(self) -> None:
        pass

    def discover_files(self, job_number: str) -> list[dict]:
        job_dir = self._base_path / job_number
        if not job_dir.exists():
            return []

        results = []
        for path in job_dir.rglob("*"):
            if path.is_file() and path.suffix.lower() in self.SUPPORTED_EXTENSIONS:
                results.append({
                    "path": str(path),
                    "file_type": path.suffix.lstrip(".").lower(),
                    "file_name": path.name,
                    "size_bytes": path.stat().st_size,
                })
        return results

Service Design Rules
Rule	Rationale
Services have initialize() and shutdown() lifecycle methods	Clean startup/teardown
Services never import models, views, or controllers	Pure I/O layer
Services return plain data (dicts, lists, primitives) or model instances	No Qt types leaked
One service per external system	Database, file I/O, broker, API each get their own
Services are injected via constructor, never imported directly by views	Testable, replaceable
Controller Layer

Controllers wire models and services together, emitting signals for the bridge/view layer:

"""controllers/base.py"""
from typing import Any, Protocol
from PySide6.QtCore import QObject
from my_app.utils.signals import SignalRegistry


class IView(Protocol):
    def bind(self, controller: "BaseController") -> None: ...
    def update_display(self, data: dict[str, Any]) -> None: ...


class BaseController(QObject):
    """
    Base class for all controllers.
    
    Provides signal registry access, view registration,
    and lifecycle management.
    """

    def __init__(self, signals: SignalRegistry, parent: QObject | None = None):
        super().__init__(parent)
        self._signals = signals
        self._views: list[IView] = []
        self._initialized = False

    @property
    def signals(self) -> SignalRegistry:
        return self._signals

    def register_view(self, view: IView) -> None:
        if view not in self._views:
            self._views.append(view)
            view.bind(self)

    def notify_views(self, data: dict[str, Any] | None = None) -> None:
        for view in self._views:
            view.update_display(data or {})

    def initialize(self) -> None:
        self._initialized = True

    def cleanup(self) -> None:
        self._views.clear()

Domain Controller Example
"""controllers/job_controller.py"""
import logging
from PySide6.QtCore import QObject

from my_app.controllers.base import BaseController
from my_app.models.job import Job, JobStatus
from my_app.models.state import ApplicationState
from my_app.services.database.jobs_repository import JobsRepository
from my_app.utils.signals import SignalRegistry

logger = logging.getLogger(__name__)


class JobController(BaseController):
    """
    Handles job operations: activate, create, update, search.
    
    Delegates persistence to JobsRepository and
    emits signals via SignalRegistry for UI updates.
    """

    def __init__(
        self,
        signals: SignalRegistry,
        repository: JobsRepository,
        parent: QObject | None = None,
    ) -> None:
        super().__init__(signals, parent)
        self._repository = repository
        self._state = ApplicationState()

    def initialize(self) -> None:
        super().initialize()
        if self._state.active_job_id:
            job = self._repository.get_job(self._state.active_job_id)
            if job is None:
                self._state.active_job_id = None

    def activate_job(self, job_id: str) -> bool:
        job = self._repository.get_job(job_id)
        if job is None:
            logger.warning(f"Job {job_id} not found")
            return False

        self._state.active_job_id = job_id
        self._signals.job_changed.emit(job_id)
        logger.info(f"Activated job {job_id}")
        return True

    def create_job(self, job_number: str) -> bool:
        if self._repository.get_job(job_number):
            logger.warning(f"Job {job_number} already exists")
            return False

        job = Job(job_number=job_number)
        self._repository.save_job(job)
        self._signals.job_created.emit(job_number)
        return True

    def get_job(self, job_id: str) -> Job | None:
        return self._repository.get_job(job_id)

    def get_all_jobs(self) -> list[Job]:
        return self._repository.get_all_jobs()

Controller Design Rules
Rule	Rationale
Controllers receive services via constructor injection	Testable, no hidden dependencies
Controllers emit signals, never manipulate UI	Decoupled from view layer
One controller per domain area	Job, Settings, Script, etc.
Controllers read/write via repositories, not raw DB	Abstraction, testability
Controllers update ApplicationState for UI-relevant state	Centralized state tracking
Testing Approach
"""tests/test_job_controller.py"""
from unittest.mock import MagicMock
from my_app.controllers.job_controller import JobController
from my_app.utils.signals import SignalRegistry
from my_app.models.job import Job


def test_activate_job_emits_signal():
    signals = SignalRegistry()
    repo = MagicMock()
    repo.get_job.return_value = Job(job_number="1234567")

    controller = JobController(signals=signals, repository=repo)
    handler = MagicMock()
    signals.job_changed.connect(handler)

    result = controller.activate_job("1234567")

    assert result is True
    handler.assert_called_once_with("1234567")


def test_activate_nonexistent_job_returns_false():
    signals = SignalRegistry()
    repo = MagicMock()
    repo.get_job.return_value = None

    controller = JobController(signals=signals, repository=repo)
    result = controller.activate_job("9999999")

    assert result is False

References
PySide6 Signals and Slots
PySide6 QAbstractListModel
Repository Pattern
Weekly Installs
34
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