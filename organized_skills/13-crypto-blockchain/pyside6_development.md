---
rating: ⭐⭐⭐
title: pyside6-development
url: https://skills.sh/caliphsdev/water-balance-application/pyside6-development
---

# pyside6-development

skills/caliphsdev/water-balance-application/pyside6-development
pyside6-development
Installation
$ npx skills add https://github.com/caliphsdev/water-balance-application --skill pyside6-development
SKILL.md
PySide6 Development Guide

This skill provides structured reference to the comprehensive PySide6 documentation (730 pages) for building professional desktop GUI applications. When developing PySide6 features, reference the appropriate chapter from the PDF at Docs/pyside6/create-gui-applications-pyside6.pdf.

Quick Reference: Table of Contents
1. Introduction (Pages 2-6)
A brief history of GUI development
About Qt and PySide6
Qt and PySide6 relationship
2. Basic PySide6 Features (Pages 7-166)

Reference for: Core concepts, first applications, fundamental building blocks

2.1 My First Application (Pages 8-17)
Creating your App
What's the event loop?
Widgets and Windows
QMainWindow
Sizing windows and widgets
2.2 Signals & Slots (Pages 18-27)
QPushButton Signals
Connecting signals to slots
Signal/slot patterns
2.3 Widgets (Pages 28-55)
QLabel (p.30): Text and image display
QCheckBox (p.38): Boolean input
QComboBox (p.40): Dropdown selection
QListWidget (p.44): Item lists
QLineEdit (p.47): Single-line text input
QSpinBox/QDoubleSpinBox (p.49): Numeric input
QSlider (p.51): Range slider
QDial (p.53): Circular dial control
QWidget (p.55): Base widget class
2.4 Layouts (Pages 56-85)
Placeholder widget (p.57)
QVBoxLayout (p.59): Vertical arrangement
QHBoxLayout (p.62): Horizontal arrangement
Nesting layouts (p.64): Complex compositions
QGridLayout (p.68): Grid-based arrangement
QStackedLayout (p.70): Stacked widgets (like pages)
QFormLayout (p.77): Two-column form layout
2.5 Actions, Toolbars & Menus (Pages 86-106)
Toolbars (p.86): Action buttons
Menus (p.97): Application menus
2.6 Dialogs (Pages 107-149)
QMessageBox (p.116): Message dialogs
Standard dialogs (p.119): Built-in dialog types
Single value dialogs (p.122): Input dialogs
File dialogs (p.134): Open/save file selection
2.7 Windows (Pages 150-159)
Creating new windows
Closing windows
Persistent windows
Showing & hiding windows
Connecting signals between windows
2.8 Events (Pages 160-166)
Mouse events
Context menus
Event hierarchy
3. Qt Designer (Pages 168-199)

Reference for: Visual UI design, .ui files, resource management

3.1 Installing Qt Designer (Pages 169-174)
Command line launcher
Platform-specific installation
3.2 Getting Started with Qt Designer (Pages 175-191)
Creating .ui files
Laying out Main Window
Using UI files from Python
Loading .ui files in Python
Converting .ui to Python
Building your application
Adding application logic
3.3 The Qt Resource System (Pages 192-199)
The QRC file
Using QRC files
Resources in Qt Designer
Using resources with compiled UI files
4. Theming (Pages 200-265)

Reference for: Application styling, dark mode, icons, QSS

4.1 Styles (Pages 201-202)
Fusion style
4.2 Palettes (Pages 203-211)
Dark Mode implementation
4.3 Icons (Pages 212-217)
Qt Standard Icons
Icon files
Free Desktop Specification Icons
4.4 Qt Style Sheets (QSS) (Pages 218-265)
Style editor (p.218)
Styling properties (p.223)
Targeting (p.239): Selecting specific widgets
Inheritance (p.247)
Pseudo-selectors (p.249): :hover, :pressed, etc.
Styling Widget Sub-controls (p.254)
Editing Stylesheets in Qt Designer (p.263)
5. Model View Controller (Pages 266-357)

Reference for: MVC architecture, data models, table views, SQL integration

5.1-5.2 Introduction to MVC (Pages 266-292)
Architecture overview
Implementation patterns
Creating the Model
Where's the Controller?
Project Architecture notes
5.3 Qt's Model View Architecture (Pages 293-294)
The Model View concept
5.4 A Simple Model View - Todo List (Pages 295-310)
The UI
The Model
Basic implementation
Hooking up actions
Using DecorationRole
Persistent data store
5.5 Tabular Data with numpy & pandas (Pages 311-331)
QTableView introduction (p.311)
Nested list as 2D data store (p.313)
Writing custom QAbstractTableModel (p.315)
Formatting numbers and dates (p.317)
Styles & Colors with Roles (p.319)
Alternative Python data structures (p.327)
5.6 Querying SQL Databases with Qt Models (Pages 332-357)
Connecting to database (p.333)
QSqlTableModel (p.334)
QSqlRelationalTableModel (p.343)
QSqlRelationalDelegate (p.345)
QSqlQueryModel (p.346)
QDataWidgetMapper (p.352)
QSqlDatabase authentication (p.357)
6. Custom Widgets (Pages 358-422)

Reference for: Custom drawing, QPainter, creating new widget types

6.1 Bitmap Graphics in Qt (Pages 359-386)
QPainter (p.359): Core drawing class
Drawing primitives (p.362): Lines, shapes, text
Fun with QPainter (p.376): Creative examples
6.2 Creating Custom Widgets (Pages 387-414)
Getting started
paintEvent (p.389)
Positioning
Updating the display
Drawing the bar
Customizing the Bar
6.3 Using Custom Widgets in Qt Designer (Pages 415-422)
Background
Writing Promotable Custom Widgets
7. Concurrent Execution (Pages 423-522)

Reference for: Threading, async operations, background tasks, QThread, QRunnable

7.1 Introduction to Threads & Processes (Pages 425-430)
The wrong approach (blocking UI)
Threads and Processes overview
7.2 Using the Thread Pool (Pages 431-440)
QRunnable (p.431)
QThreadPool.start() (p.433)
Extending QRunnable (p.435)
Thread IO (p.436)
7.3 QRunnable Examples (Pages 441-497)
Progress watcher (p.442)
Calculator (p.452)
Stopping a running QRunnable (p.457)
Pausing a runner (p.460)
Communicator (p.464)
Generic runner (p.470)
Running external processes (p.478)
The Manager (p.488)
7.4 Long-running Threads (Pages 498-513)
Using QThread (p.498)
7.5 Running External Commands & Processes (Pages 514-522)
8. Plotting (Pages 523-558)

Reference for: Charts, graphs, data visualization

8.1 Plotting with PyQtGraph (Pages 524-542)
Getting started
Creating a PyQtGraph widget
Styling plots
Plot Titles
Axis Labels
Legends
Background Grid
Plotting multiple lines
Clearing the plot
Updating the plot
8.2 Plotting with Matplotlib (Pages 544-558)
Installing Matplotlib
Simple examples
Plot controls
Updating plots
Embedding plots from Pandas
9. Further PySide6 Features (Pages 559-603)

Reference for: Advanced topics, timers, signals, system tray, enums

9.1 Timers (Pages 560-564)
Interval timers (p.560)
Single shot timers (p.562)
Postponing via event queue (p.563)
9.2 Extending Signals (Pages 565-574)
Custom Signals (p.565)
Modifying Signal Data (p.567)
9.3 Working with Relative Paths (Pages 575-579)
Relative paths
Using a Paths class
9.4 System Tray & macOS Menus (Pages 580-588)
Adding system tray icon
9.5 Enums & the Qt Namespace (Pages 589-597)
It's all just numbers
Binary & Hexadecimal
Bitwise OR combination
Checking compound flags
Bitwise AND checks
9.6 Working with Command-line Arguments (Pages 598-601)
9.7 Pythonic PySide6 (Pages 602-603)
10. Packaging & Distribution (Pages 605-652)

Reference for: Building executables, installers, deployment

10.1 Packaging with PyInstaller (Pages 606-628)
Requirements
Getting Started
Building the basic app
The .spec file
Tweaking the build
Data files and Resources
10.2 Creating a Windows Installer with InstallForge (Pages 629-639)
General, Setup, Dialogs, System, Build sections
Running the installer
10.3 Creating a macOS Disk Image Installer (Pages 640-642)
create-dmg
10.4 Creating a Linux Package with fpm (Pages 643-652)
Installing fpm
Structuring your package
Building your package
Scripting the build
11. Example Applications (Pages 653-688)

Reference for: Complete application examples

11.1 Mozzarella Ashbadger - Web Browser (Pages 653-668)
Browser widget
Paths
Navigation
File operations
Printing
Help
Tabbed Browsing
11.2 Moonsweeper - Minesweeper Game (Pages 669-688)
Icons & Colors
Playing Field
Position Tiles
Mechanics
Endgames
Status
Menus
Appendix A (Pages 689-716)

Reference for: Installation, C++ translation, PyQt6 differences

A.1 Installing PySide6 (Pages 690-694)
Windows, macOS, Linux installation
Working with Virtual Environments
A.2 Translating C++ Examples to Python (Pages 695-704)
Imports
main() function
C++ types
Signals
Syntax
A.3 PyQt6 and PySide6 Differences (Pages 705-714)
Background
Licensing
Namespaces & Enums
UI files
exec() vs exec_()
Slots and Signals
QMouseEvent
Features in PySide6 only
Supporting both in libraries
Usage Guidelines
When to Use This Skill

Reference this skill when:

Creating new widgets: See Chapter 2.3 (Widgets) and Chapter 6 (Custom Widgets)
Building layouts: See Chapter 2.4 (Layouts)
Implementing signals/slots: See Chapter 2.2 and Chapter 9.2
Creating dialogs: See Chapter 2.6 (Dialogs)
Theming/styling: See Chapter 4 (Theming) especially QSS
Data tables/models: See Chapter 5 (Model View Controller)
Threading/async: See Chapter 7 (Concurrent Execution)
Plotting/charts: See Chapter 8 (Plotting)
Packaging apps: See Chapter 10 (Packaging & Distribution)
Reading the PDF

To read specific content from the PDF, use pdfplumber:

import pdfplumber

with pdfplumber.open('Docs/pyside6/create-gui-applications-pyside6.pdf') as pdf:
    # Read specific page (0-indexed, so page 100 in PDF is index 99)
    page = pdf.pages[99]  # Page 100
    text = page.extract_text()
    print(text)

Key PySide6 Patterns from This Book
Signal/Slot Connection
from PySide6.QtWidgets import QPushButton
button = QPushButton("Click me")
button.clicked.connect(self.on_button_clicked)

Custom Widget with paintEvent
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter

class CustomWidget(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        # Drawing code here
        painter.end()

QThread for Background Tasks
from PySide6.QtCore import QThread, Signal

class Worker(QThread):
    finished = Signal(object)
    
    def run(self):
        result = self.do_work()
        self.finished.emit(result)

QSS Styling
widget.setStyleSheet("""
    QWidget {
        background-color: #2d2d2d;
        color: white;
        font-size: 14px;
    }
    QPushButton:hover {
        background-color: #3d3d3d;
    }
""")

PDF Location

Full Documentation: Docs/pyside6/create-gui-applications-pyside6.pdf
Total Pages: 730
Version: 6.1 (2025-09-10)
Author: Martin Fitzpatrick

When you need detailed examples or explanations on any PySide6 topic, read the appropriate pages from this PDF using the pdf skill tools.

Weekly Installs
10
Repository
caliphsdev/wate…lication
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass