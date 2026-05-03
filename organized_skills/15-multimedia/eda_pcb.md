---
rating: ⭐⭐⭐
title: eda-pcb
url: https://skills.sh/l3wi/claude-eda/eda-pcb
---

# eda-pcb

skills/l3wi/claude-eda/eda-pcb
eda-pcb
Installation
$ npx skills add https://github.com/l3wi/claude-eda --skill eda-pcb
SKILL.md
EDA PCB Skill

PCB layout, component placement, and routing.

Auto-Activation Triggers

This skill activates when:

User asks to "layout PCB", "place components", "route traces"
User is working with .kicad_pcb files
User asks about placement, routing, copper pours, vias
Project has schematic but no PCB layout
User mentions DFM, trace width, or clearance
Context Requirements

Requires:

hardware/*.kicad_sch - Completed schematic with netlist
docs/component-selections.md - Component details
docs/design-constraints.json - Board size, layer count, etc.
datasheets/ - For placement/routing recommendations

Produces:

hardware/*.kicad_pcb - KiCad PCB file
docs/pcb-status.md - Layout progress tracking
Workflow
1. Load Context
@docs/design-constraints.json
@docs/component-selections.md
@docs/schematic-status.md
@datasheets/ (for placement guidance)

1.5 Pre-Layout Validation

Before starting layout, verify:

Check	Source	Action if Missing
Schematic ERC clean	schematic-status.md	Complete schematic first
Layer count decided	design-constraints.json	See LAYER-COUNT-DECISION.md
Stackup selected	design-constraints.json	See STACKUP-DECISION.md
Board dimensions	design-constraints.json	Define constraints
Critical interfaces	design-constraints.json	USB, SPI speeds, etc.
Thermal budget	design-constraints.json	Power dissipation known

Extract key constraints:

{
  "board": {
    "layers": 4,
    "thickness": 1.6,
    "dimensions": {"width": 50, "height": 40}
  },
  "dfmTargets": {
    "manufacturer": "JLCPCB",
    "minTraceWidth": 0.15,
    "minClearance": 0.15,
    "impedanceControl": true
  },
  "interfaces": {
    "usb": true,
    "highSpeedSpi": false
  },
  "thermal": {
    "maxPowerDissipation": 2.5
  }
}


Architecture Validation Warnings:

Condition	Warning
USB + 2-layer board	Cannot achieve 90Ω impedance
Buck converter + no ground plane	EMI issues likely
WiFi/BLE + 2-layer	Antenna performance degraded
High-speed SPI (>20MHz) + long traces	Signal integrity risk
No thermal plan + >1W dissipation	Thermal issues likely
2. Initialize PCB
Create PCB file or open existing
Import netlist from schematic
Set board outline per constraints
Configure layer stackup
Set design rules
3. Configure Design Rules

Set rules appropriate for manufacturer:

JLCPCB standard:
- Min trace width: 0.127mm (5mil)
- Min clearance: 0.127mm (5mil)
- Min via drill: 0.3mm
- Min via annular ring: 0.13mm

4. Place Components

Priority order:

Fixed position items - Connectors (edge), mounting holes
MCU/Main IC - Central location
Crystal/oscillator - Within 5mm of MCU
Power components - Near input, thermal considerations
Decoupling capacitors - Adjacent to IC power pins
Sensitive analog - Away from noisy digital
Remaining components - Grouped by function

See reference/PLACEMENT-STRATEGY.md for detailed guidelines.

5. Route Critical Signals First

Priority:

Power delivery (wide traces, pours)
Crystal/oscillator (short, guarded)
USB differential pairs (90Ω impedance)
High-speed signals (length matching)
Sensitive analog (away from digital)
General signals

See reference/ROUTING-RULES.md for trace width and clearance guidelines.

6. Create Copper Pours
GND pour on bottom layer (2-layer)
Or GND on layer 2, power on layer 3 (4-layer)
Thermal relief on pads
Stitch vias for plane continuity
7. Route Remaining Signals
Follow schematic groupings
Minimize vias
Avoid acute angles (use 45°)
Keep trace lengths reasonable
8. DRC Check
Run design rule check
Fix violations
Document intentional exceptions
9. Visual Review
Generate board images
Check silkscreen readability
Verify component orientation marks
Review for manufacturing issues
10. Pre-Manufacturing Review

Validation checklist before ordering:

Category	Check	Reference
DRC	0 errors, 0 warnings	DRC-VIOLATIONS-GUIDE.md
Clearances	Meet manufacturer minimums	DFM-RULES.md
Via sizes	Drill ≥ 0.3mm (JLCPCB std)	DFM-RULES.md
Annular rings	≥ 0.13mm (1oz copper)	DFM-RULES.md
Trace widths	Power traces sized for current	ROUTING-RULES.md
USB traces	90Ω impedance, length matched	HIGH-SPEED-ROUTING.md
Silkscreen	Not on pads, readable	Visual check
Board outline	Closed shape, proper clearance	DFM-RULES.md

Thermal verification:

 Power components have thermal relief
 Thermal vias under QFN/thermal pads
 Heat sink areas connected to copper pour
 No thermal bottlenecks (narrow traces for high current)

Signal integrity verification:

 High-speed signals over solid ground
 Return paths not broken by splits
 Crystal area guarded, no traces crossing
 Antenna keep-out respected (if applicable)
Output Format
pcb-status.md
# PCB Layout Status

Project: [name]
Updated: [date]

## Board Specifications
- Size: X × Y mm
- Layers: N
- Thickness: 1.6mm

## Progress
- [x] Board outline defined
- [x] Mounting holes placed
- [x] Critical components placed
- [x] All components placed
- [ ] Power routing complete
- [ ] Signal routing complete
- [ ] Copper pours added
- [ ] DRC clean

## Layer Usage
| Layer | Usage |
|-------|-------|
| F.Cu | Signals, components |
| B.Cu | GND pour, some signals |

## DRC Status
- Errors: X
- Warnings: Y
- Unrouted nets: Z

## Design Rules
- Trace width: 0.2mm (signals), 0.5mm (power)
- Clearance: 0.2mm
- Via: 0.3mm drill, 0.6mm pad

## Notes
- [Any special considerations]

## Next Steps
- [What remains to be done]

Guidelines
Always check datasheets for recommended layouts
Keep high-current paths short and wide
Maintain ground plane integrity under sensitive signals
Consider thermal management early
Use the DRC frequently during layout
Reference Documents
Document	Purpose
reference/PLACEMENT-STRATEGY.md	Component placement guidelines
reference/ROUTING-RULES.md	Trace width and routing rules
reference/EMI-CONSIDERATIONS.md	EMI/EMC best practices
reference/DFM-RULES.md	Design for manufacturing rules
reference/DRC-VIOLATIONS-GUIDE.md	Common DRC errors and fixes
reference/STACKUP-DECISION.md	Layer stackup selection
reference/HIGH-SPEED-ROUTING.md	USB, SPI, I2C, antenna routing

Upstream documents:

Document	What to Extract
LAYER-COUNT-DECISION.md (eda-architect)	Layer count rationale
THERMAL-BUDGET.md (eda-architect)	Power dissipation limits
DECOUPLING-STRATEGY.md (eda-research)	Cap values and placement
SCHEMATIC-REVIEW-CHECKLIST.md (eda-schematics)	Pre-layout verification
Next Steps

After PCB layout is complete:

Run /eda-check for comprehensive validation
Update design-constraints.json stage to "validation"
Weekly Installs
173
Repository
l3wi/claude-eda
GitHub Stars
12
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass