---
title: reflex-dev
url: https://skills.sh/silvainfm/claude-skills/reflex-dev
---

# reflex-dev

skills/silvainfm/claude-skills/reflex-dev
reflex-dev
Installation
$ npx skills add https://github.com/silvainfm/claude-skills --skill reflex-dev
SKILL.md
Reflex Development
Overview

Reflex is a full-stack Python framework for building web applications without writing JavaScript. Apps compile to a React frontend and FastAPI backend, with state management and event handlers running entirely in Python.

Architecture:

Frontend: Compiled to React (JavaScript) for UI rendering
Backend: FastAPI server running Python event handlers
Communication: WebSockets for real-time state updates
State: Server-side Python state synchronized to frontend
Core Concepts
State Management

State is a Python class that holds all mutable data and event handlers. All state variables must be JSON-serializable.

import reflex as rx

class AppState(rx.State):
    # State variables (any JSON-serializable type)
    count: int = 0
    items: list[str] = []
    user_name: str = ""

    # Event handlers - the ONLY way to modify state
    def increment(self):
        self.count += 1

    def add_item(self, item: str):
        self.items.append(item)

    # Computed vars (derived state)
    @rx.var
    def item_count(self) -> int:
        return len(self.items)


Key Rules:

State vars MUST be JSON-serializable (int, str, list, dict, bool, float)
Only event handlers can modify state
Use @rx.var decorator for computed/derived values
State is per-user session (isolated between users)
Components

Components are UI building blocks. Reflex provides 60+ built-in components.

import reflex as rx

def header() -> rx.Component:
    return rx.heading("My App", size="lg")

def counter_component(state: AppState) -> rx.Component:
    return rx.vstack(
        rx.text(f"Count: {state.count}"),
        rx.button("Increment", on_click=state.increment),
        spacing="4"
    )


Common Components:

Layout: rx.vstack, rx.hstack, rx.box, rx.container
Text: rx.heading, rx.text, rx.code
Input: rx.input, rx.text_area, rx.select, rx.checkbox
Interactive: rx.button, rx.link, rx.icon_button
Data: rx.table, rx.data_table, rx.list
Charts: rx.recharts.line_chart, rx.recharts.bar_chart, etc.
Event Handlers

Event handlers respond to user interactions and are the ONLY way to modify state.

class FormState(rx.State):
    form_data: dict[str, str] = {}

    # Simple event handler
    def handle_submit(self):
        print(f"Submitted: {self.form_data}")

    # Event handler with argument
    def update_field(self, field: str, value: str):
        self.form_data[field] = value

    # Async event handler (for API calls, DB queries)
    async def fetch_data(self):
        # Can use any Python library
        import httpx
        async with httpx.AsyncClient() as client:
            response = await client.get("https://api.example.com/data")
            self.data = response.json()


Event Triggers (connect components to handlers):

on_click: Button clicks
on_change: Input field changes
on_submit: Form submissions
on_mount: Component first renders
on_blur, on_focus: Input focus events
Project Structure

Standard Reflex app structure:

my_app/
├── my_app/
│   ├── __init__.py         # Empty
│   └── my_app.py           # Main app file (State + pages)
├── assets/                 # Static files (images, fonts, etc.)
├── .web/                   # Auto-generated frontend (don't edit)
├── rxconfig.py             # Reflex configuration
└── requirements.txt        # Python dependencies

Main App File Pattern
import reflex as rx

# 1. Define State
class State(rx.State):
    count: int = 0

    def increment(self):
        self.count += 1

# 2. Define Pages
def index() -> rx.Component:
    return rx.container(
        rx.heading("Welcome"),
        rx.button("Click", on_click=State.increment),
        rx.text(f"Count: {State.count}")
    )

def about() -> rx.Component:
    return rx.container(
        rx.heading("About"),
        rx.link("Home", href="/")
    )

# 3. Create App and Add Routes
app = rx.App()
app.add_page(index, route="/")
app.add_page(about, route="/about")

Common Patterns
Form Handling
class FormState(rx.State):
    name: str = ""
    email: str = ""

    def handle_submit(self, form_data: dict):
        self.name = form_data.get("name", "")
        self.email = form_data.get("email", "")

def form_page():
    return rx.form(
        rx.vstack(
            rx.input(name="name", placeholder="Name"),
            rx.input(name="email", placeholder="Email"),
            rx.button("Submit", type="submit"),
        ),
        on_submit=FormState.handle_submit,
    )

Data Tables
class DataState(rx.State):
    data: list[dict] = [
        {"id": 1, "name": "Alice", "age": 25},
        {"id": 2, "name": "Bob", "age": 30},
    ]

def data_table_page():
    return rx.data_table(
        data=DataState.data,
        columns=["id", "name", "age"],
        sort=True,
        search=True,
        pagination=True,
    )

File Upload
class UploadState(rx.State):
    async def handle_upload(self, files: list[rx.UploadFile]):
        for file in files:
            upload_data = await file.read()
            # Process file data
            outfile = f"./uploads/{file.filename}"
            with open(outfile, "wb") as f:
                f.write(upload_data)

def upload_page():
    return rx.vstack(
        rx.upload(
            rx.button("Select Files"),
            id="upload1",
        ),
        rx.button(
            "Upload",
            on_click=UploadState.handle_upload(rx.upload_files(upload_id="upload1"))
        ),
    )

Database Integration (with DuckDB)
import duckdb
import polars as pl

class DBState(rx.State):
    records: list[dict] = []

    async def load_data(self):
        # Use existing database connection
        conn = duckdb.connect("data/mydb.duckdb")
        df = conn.execute("SELECT * FROM mytable").pl()
        self.records = df.to_dicts()
        conn.close()

    async def insert_record(self, data: dict):
        conn = duckdb.connect("data/mydb.duckdb")
        conn.execute(
            "INSERT INTO mytable (name, value) VALUES (?, ?)",
            [data["name"], data["value"]]
        )
        conn.close()
        await self.load_data()  # Refresh

Styling & Layout
Inline Styling
rx.box(
    rx.text("Styled text"),
    bg="#1a5f9e",
    color="white",
    padding="4",
    border_radius="md",
)

Responsive Layout
rx.container(
    rx.responsive_grid(
        rx.box("Item 1", bg="blue"),
        rx.box("Item 2", bg="green"),
        rx.box("Item 3", bg="red"),
        columns=[1, 2, 3],  # 1 col mobile, 2 tablet, 3 desktop
        spacing="4",
    ),
    max_width="1200px",
)

Common Style Props
Layout: width, height, padding, margin, display
Colors: bg (background), color (text)
Typography: font_size, font_weight, text_align
Borders: border, border_radius, border_color
Spacing: spacing (for stacks), gap
Routing
Multiple Pages
app = rx.App()

# Route with parameters
@rx.page(route="/user/[id]")
def user_page() -> rx.Component:
    return rx.text(f"User ID: {State.router.page.params.get('id')}")

# Simple routes
app.add_page(index, route="/")
app.add_page(about, route="/about")

Navigation
# Links
rx.link("Go to About", href="/about")

# Programmatic navigation
def go_home(self):
    return rx.redirect("/")

Development Workflow
Initialize New App
pip install reflex
reflex init

Run Development Server
reflex run


App runs on http://localhost:3000 with auto-reload.

Common Commands
reflex run          # Start dev server
reflex export       # Build production bundle
reflex db init      # Initialize database (if using Reflex DB)
reflex db migrate   # Run migrations

Best Practices

State Organization: Split large states into substates

class AuthState(rx.State):
    user: str = ""

class DataState(rx.State):
    items: list = []


Component Reusability: Create reusable component functions

def card(title: str, content: str) -> rx.Component:
    return rx.box(
        rx.heading(title, size="md"),
        rx.text(content),
        padding="4",
        border="1px solid #ddd",
    )


Event Handler Performance: Use async for I/O operations

async def fetch_data(self):
    # Async I/O won't block other users
    self.data = await some_api_call()


Type Hints: Always type-hint state vars and event handlers

count: int = 0
items: list[str] = []

def update_count(self, value: int) -> None:
    self.count = value

References
Documentation
Official Docs: https://reflex.dev/docs/getting-started/introduction/
Component Library: https://reflex.dev/docs/library
Tutorials: https://reflex.dev/docs/getting-started/tutorial/
Example Apps

See examples/ directory for complete working examples:

Simple counter app
Data table with CRUD operations
Form with validation
File upload and processing
Common Patterns Reference

See references/patterns.md for detailed examples of:

Authentication flows
Real-time updates
Complex form validation
Multi-step workflows
Data visualization with charts
Weekly Installs
88
Repository
silvainfm/claude-skills
GitHub Stars
2
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn