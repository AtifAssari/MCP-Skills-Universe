---
rating: ⭐⭐⭐
title: patent-diagram-generator
url: https://skills.sh/robthepcguy/claude-patent-creator/patent-diagram-generator
---

# patent-diagram-generator

skills/robthepcguy/claude-patent-creator/patent-diagram-generator
patent-diagram-generator
Installation
$ npx skills add https://github.com/robthepcguy/claude-patent-creator --skill patent-diagram-generator
SKILL.md
Patent Diagram Generator Skill

Create patent-style technical diagrams including flowcharts, block diagrams, and system architectures using Graphviz.

When to Use

Invoke this skill when users ask to:

Create flowcharts for method claims
Generate block diagrams for system claims
Draw system architecture diagrams
Create technical illustrations for patents
Add reference numbers to diagrams
Generate patent figures
What This Skill Does

Flowchart Generation:

Method step flowcharts
Decision trees
Process flows with branches
Patent-style step numbering

Block Diagram Creation:

System component diagrams
Hardware architecture diagrams
Software module diagrams
Component interconnections

Custom Diagram Rendering:

Render Graphviz DOT code
Support multiple formats (SVG, PNG, PDF)
Multiple layout engines (dot, neato, fdp, circo, twopi)

Patent-Style Formatting:

Add reference numbers (10, 20, 30, etc.)
Use clear labels and connections
Professional formatting for USPTO filing
Required Dependencies

This skill requires Graphviz to be installed:

Windows:

choco install graphviz


Linux:

sudo apt install graphviz


Mac:

brew install graphviz


Python Package:

pip install graphviz

How to Use

When this skill is invoked:

Load diagram generator:

import sys
sys.path.insert(0, os.path.join(os.environ.get('CLAUDE_PLUGIN_ROOT', '.'), 'python'))
from python.diagram_generator import PatentDiagramGenerator

generator = PatentDiagramGenerator()


Create flowchart from steps:

steps = [
    {"id": "start", "label": "Start", "shape": "ellipse", "next": ["step1"]},
    {"id": "step1", "label": "Initialize System", "shape": "box", "next": ["decision"]},
    {"id": "decision", "label": "Is Valid?", "shape": "diamond", "next": ["step2", "error"]},
    {"id": "step2", "label": "Process Data", "shape": "box", "next": ["end"]},
    {"id": "error", "label": "Handle Error", "shape": "box", "next": ["end"]},
    {"id": "end", "label": "End", "shape": "ellipse", "next": []}
]

diagram_path = generator.create_flowchart(
    steps=steps,
    filename="method_flowchart",
    output_format="svg"
)


Create block diagram:

blocks = [
    {"id": "input", "label": "Input\\nSensor", "type": "input"},
    {"id": "cpu", "label": "Central\\nProcessor", "type": "process"},
    {"id": "memory", "label": "Memory\\nStorage", "type": "storage"},
    {"id": "output", "label": "Output\\nDisplay", "type": "output"}
]

connections = [
    ["input", "cpu", "raw data"],
    ["cpu", "memory", "store"],
    ["memory", "cpu", "retrieve"],
    ["cpu", "output", "processed data"]
]

diagram_path = generator.create_block_diagram(
    blocks=blocks,
    connections=connections,
    filename="system_diagram",
    output_format="svg"
)


Render custom DOT code:

dot_code = """
digraph PatentSystem {
    rankdir=LR;
    node [shape=box, style=rounded];

    Input [label="User Input\\n(10)"];
    Processor [label="Processing Unit\\n(20)"];
    Output [label="Display\\n(30)"];

    Input -> Processor [label="data"];
    Processor -> Output [label="result"];
}
"""

diagram_path = generator.render_dot_diagram(
    dot_code=dot_code,
    filename="custom_diagram",
    output_format="svg",
    engine="dot"
)


Add reference numbers:

# After creating a diagram, add patent-style reference numbers
reference_map = {
    "Input Sensor": 10,
    "Central Processor": 20,
    "Memory Storage": 30,
    "Output Display": 40
}

annotated_path = generator.add_reference_numbers(
    svg_path=diagram_path,
    reference_map=reference_map
)

Diagram Templates

Get common templates:

templates = generator.get_diagram_templates()

# Available templates:
# - simple_flowchart: Basic process flow
# - system_block: System architecture
# - method_steps: Sequential method
# - component_hierarchy: Hierarchical structure

Shape Types
Flowchart Shapes
ellipse: Start/End points
box: Process steps
diamond: Decision points
parallelogram: Input/Output operations
cylinder: Database/Storage
Block Diagram Types
input: Input devices/sensors
output: Output devices/displays
process: Processing units
storage: Memory/storage
decision: Control logic
default: General components
Layout Engines
dot: Hierarchical (top-down/left-right)
neato: Spring model layout
fdp: Force-directed layout
circo: Circular layout
twopi: Radial layout
Output Formats
svg: Scalable Vector Graphics (best for editing)
png: Raster image (good for viewing)
pdf: Portable Document Format (USPTO compatible)
Patent-Style Reference Numbers

Convention:

Main components: 10, 20, 30, 40, ...
Sub-components: 12, 14, 16 (under 10)
Elements: 22, 24, 26 (under 20)

Example labeling:

"Input Sensor (10)"
"  - Detector Element (12)"
"  - Signal Processor (14)"
"Central Unit (20)"
"  - CPU Core (22)"
"  - Cache (24)"

Presentation Format

When creating diagrams:

Describe what will be generated: "Creating a flowchart for the authentication method with 5 steps..."

Generate the diagram: Run Python code to create SVG/PNG/PDF

Show file location: "Diagram created: ${CLAUDE_PLUGIN_ROOT}/python\diagrams\method_flowchart.svg"

List reference numbers (if added):

Reference Numbers:
- Input Module (10)
- Processing Unit (20)
- Output Interface (30)

Common Use Cases

Method Claims → Flowcharts

Show sequential steps
Include decision branches
Number steps (S1, S2, S3...)

System Claims → Block Diagrams

Show components and connections
Use reference numbers
Indicate data flow directions

Architecture Diagrams → Custom DOT

Complex system layouts
Multiple interconnections
Hierarchical structures
Error Handling

If Graphviz is not installed:

Check installation: dot -V
Install for your OS (see above)
Verify Python package: pip show graphviz
Test generation: python scripts/test_diagrams.py
Tools Available
Bash: To run Python diagram generation
Write: To save DOT code or diagrams
Read: To load existing diagrams or templates
Weekly Installs
143
Repository
robthepcguy/cla…-creator
GitHub Stars
97
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass