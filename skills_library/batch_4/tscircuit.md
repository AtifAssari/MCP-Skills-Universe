---
title: tscircuit
url: https://skills.sh/tscircuit/skill/tscircuit
---

# tscircuit

skills/tscircuit/skill/tscircuit
tscircuit
Installation
$ npx skills add https://github.com/tscircuit/skill --skill tscircuit
SKILL.md
tscircuit

You are helping the user design electronics using tscircuit (React/TypeScript) and the tsci CLI.

When this Skill is active:

Prefer tscircuit’s documented primitives and CLI behavior. If something is unclear, confirm by:
Reading local files in the repo (e.g., tscircuit.config.json, index.circuit.tsx, package.json)
Running tsci --help or the specific subcommand’s --help
Avoid “inventing” JSX props or CLI flags.
Default workflow
Clarify requirements (if not already given)
Board form factor / size constraints
Power sources and voltage rails
I/O: connectors, headers, mounting holes, mechanical constraints
Target manufacturer constraints (trace/space, assembly, supplier)
Choose a starting point
If the repo is not a tscircuit project, recommend:
Install CLI, then tsci init to bootstrap a project.
If a form-factor template is appropriate (Arduino Shield, Raspberry Pi HAT, etc.), prefer @tscircuit/common templates.
Find and install components
Use tsci search "<query>" to discover footprints and tscircuit registry packages.
For USB-C receptacles/connectors, prefer builtin syntax with <connector standard="usb_c" /> instead of importing from JLCPCB.
Use one of:
tsci add <author/pkg> for registry packages (installs @tsci/* packages)
tsci import <query> when you need to import a component from JLCPCB or the registry.
Write/modify TSX circuit code
Keep circuits as a default-exported function that returns JSX.
Use layout props intentionally:
PCB: pcbX, pcbY, pcbRotation, layer
Schematic: schX, schY, schRotation, schOrientation
Use <trace /> for connectivity; prefer net connections (net.GND, net.VCC, etc.) for power/ground.
Build and iterate
Run tsci check netlist before tsci check schematic-placement, tsci check placement, and tsci build to catch connectivity issues early.
Use tsci check schematic-placement to validate schematic-side placement before checking PCB placement.
Do not finalize unless both tsci check schematic-placement and tsci check placement pass with no actionable placement violations; if violations exist, fix layout and rerun until clean.
Use tsci check trace-length to check for long straight line distances (before routing) or long routes (after routing)
Run tsci build --pcb-png [file] to inspect placement before checking routing.
Run tsci check routing-difficulty after placement to identify potential areas of congestion.
Run tsci build to compile and validate the circuit.
DRC (Design Rule Check) errors can often be ignored during development—focus on getting the circuit correct first.
If routing struggles, reduce density, use <group /> for sub-layouts, or change autorouter settings.
Use tsci dev only when you need interactive visual feedback (not typical for AI-driven iteration).
Validate and export
Run tsci check netlist before tsci check schematic-placement, tsci check placement, and tsci build when preparing to share/publish.
Run tsci build (and optionally tsci snapshot) before sharing/publishing.
Use tsci export for SVG/netlist/DSN/3D/library outputs.
For manufacturing, obtain fabrication outputs (Gerbers/BOM/PnP) from the export UI after tsci dev.
Safety and non-goals
Treat electrical safety, regulatory compliance, and manufacturability as user-owned responsibilities.
Do not publish (tsci push) or place orders unless the user explicitly requests it.
Local references bundled with this Skill
CLI primer: CLI.md
Syntax primer: SYNTAX.md
Workflow patterns: WORKFLOW.md
Pre-export checklist: CHECKLIST.md
Ready-to-copy templates: templates/
Helper scripts: scripts/
Builtin Elements
<analogsimulation />
<battery />
<board />
<cadassembly />
<cadmodel />
<capacitor />
<chip />
<connector />
<constraint />
<copperpour />
<coppertext />
<courtyardcircle />
<courtyardoutline />
<courtyardpill />
<courtyardrect />
<crystal />
<currentsource />
<cutout />
<diode />
<fabricationnotedimension />
<fabricationnotepath />
<fabricationnoterect />
<fabricationnotetext />
<fiducial />
<footprint />
<fuse />
<group />
<hole />
<inductor />
<jumper />
<led />
<mosfet />
<mountedboard />
<net />
<netalias />
<netlabel />
<opamp />
<panel />
<pcbkeepout />
<pcbnotedimension />
<pcbnoteline />
<pcbnotepath />
<pcbnoterect />
<pcbnotetext />
<pcbtrace />
<pinheader />
<pinout />
<platedhole />
<port />
<potentiometer />
<pushbutton />
<resistor />
<resonator />
<schematicarc />
<schematicbox />
<schematiccell />
<schematiccircle />
<schematicline />
<schematicpath />
<schematicrect />
<schematicrow />
<schematictable />
<schematictext />
<silkscreencircle />
<silkscreenline />
<silkscreenpath />
<silkscreenrect />
<silkscreentext />
<smtpad />
<solderjumper />
<subcircuit />
<subpanel />
<switch />
<symbol />
<testpoint />
<trace />
<tracehint />
<transistor />
<via />
<voltageprobe />
<voltagesource />
Weekly Installs
409
Repository
tscircuit/skill
GitHub Stars
3
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn