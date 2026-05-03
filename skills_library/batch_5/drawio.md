---
title: drawio
url: https://skills.sh/markdown-viewer/skills/drawio
---

# drawio

skills/markdown-viewer/skills/drawio
drawio
Installation
$ npx skills add https://github.com/markdown-viewer/skills --skill drawio
SKILL.md
drawio Diagram Generator

Quick Start: Create <mxfile> with <diagram> → Define <mxGraphModel> with grid settings → Add <root> with cells → Use <mxCell> for shapes and edges → Set geometry with <mxGeometry> → Wrap in ```drawio fence.

Critical Rules
Structure Rules
S1: Check Stencil Names 🚨 NEVER guess stencil names. Check stencils/README.md for EXACT names. Wrong: mxgraph.cisco.router → Correct: mxgraph.cisco.routers.router
S2: Stencils Require fillColor Many stencils have no default color. Always add fillColor/strokeColor. Exception: edge/link stencils are connectors, not devices.
S3: Root Cells Required Must include <mxCell id="0"/> and <mxCell id="1" parent="0"/> or diagram won't render.
S4: Labels Below Stencils Use verticalLabelPosition=bottom;verticalAlign=top;labelPosition=center;align=center; for device labels.
S5: mxCell Must Be Siblings ALL mxCell elements must be siblings under <root> — NEVER nest mxCell inside another mxCell.
S6: Container Transparency For container shapes, use fillColor=none; to make background transparent and prevent covering child elements.

Preset Color Palette: Blue(#dae8fc,#6c8ebf) Green(#d5e8d4,#82b366) Orange(#ffe6cc,#d79b00) Red(#f8cecc,#b85450) Purple(#e1d5e7,#9673a6) Yellow(#fff2cc,#d6b656) Gray(#f5f5f5,#666666)

Layout Rules
L1: Starting Margin Begin positioning from x=40, y=40.
L2: Element Spacing Keep 40-60px gaps between connected shapes; 150-200px for routing channels.
L3: Compact Layouts Use vertical stacking or grid layouts. Avoid spreading elements too far apart.
Edge Routing Rules — CRITICAL for Clean Diagrams
E1: No Shared Paths Multiple edges between same nodes must use DIFFERENT exit/entry positions (exitY=0.3 and exitY=0.7, NOT both 0.5).
E2: Bidirectional Use Opposite Sides A→B: exitX=1, entryX=0. B→A: exitX=0, entryX=1.
E3: Explicit Exit/Entry Points Every edge should specify: exitX, exitY, entryX, entryY in style.
E4: Route Around Obstacles If any shape is between source and target, use waypoints. Add 20-30px clearance. NEVER let edges cross over shapes.
E5: Plan Layout First Organize shapes into columns/rows. Trace each edge mentally: "What shapes are between source and target?"
E6: Multiple Waypoints Use 2-3 waypoints for L-shaped or U-shaped paths. Each direction change needs a waypoint.
E7: Natural Connection Points NEVER use corners (entryX=1,entryY=1). Top-to-bottom: exitY=1, entryY=0. Left-to-right: exitX=1, entryX=0.
E8: Diagonal Routing Principle When connecting distant nodes diagonally, route along the PERIMETER (outside edge) of the diagram, NOT through the middle where other shapes exist.
Pre-Generation Checklist
Do any edges cross over non-source/target shapes? → Add waypoints
Do any two edges share the same path? → Adjust exit/entry points
Are any connections at corners? → Use edge centers instead
Could rearranging shapes reduce crossings? → Revise layout
Multi-Phase Generation Workflow

Complex diagrams should be generated in ordered phases. Output each phase as a separate chunk to keep XML manageable and reduce errors.

P1: Plan Identify diagram type: topology (has edges) or spatial (layout-only, e.g. floor plans). Choose canvas size, select stencil library from stencils/README.md. Plan element positions first, then derive zone boundaries from the element layout — you can't size a zone without knowing what's inside it.
P2: Zones (XML output order) Although zones are planned after elements (P1), they must be written first in XML — drawio renders by document order, so earlier cells sit behind later ones. Solid fill: rounded=1;fillColor=#BAC8D3;strokeColor=none;opacity=60. Dashed border: rounded=1;dashed=1;dashPattern=8 8;fillColor=none;strokeColor=#0BA5C4. Use separate text cells for zone labels. Bus bars (if needed): shape=line;strokeColor=#23445D.
P3: Elements Position shapes on grid (multiples of 10/20). Keep 40-60px spacing within groups, 150-200px routing channels between groups. Consistent device style per stencil family (e.g. Cisco: fillColor=#036897;strokeColor=#ffffff;strokeWidth=2).
P4: Connections Skip for spatial diagrams (floor plans, wireframes) — they use proximity, not edges. For topology diagrams, add edges last. Network links: endArrow=none;endFill=0. Data flow: endArrow=classic. Dashed for logical/VPN: dashed=1. Trace each edge mentally to avoid crossing shapes.
P5: Labels Add floating text, legends, dimension lines. For spatial diagrams labels carry more semantic weight. Verify every element has a value or adjacent label cell.
P6: Chunking When a diagram exceeds ~30 elements, split XML output: Chunk 1 = header + zones + first element group, Chunk 2 = remaining elements, Chunk 3 = all edges + closing tags.
Common Shapes
Basic Shapes
<mxfile><diagram name="Basic Shapes" id="basic-shapes"><mxGraphModel dx="800" dy="600" grid="1" gridSize="10"><root><mxCell id="0"/><mxCell id="1" parent="0"/>
  <mxCell id="rect" value="Box" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1"><mxGeometry x="20" y="20" width="100" height="50" as="geometry"/></mxCell>
  <mxCell id="rounded" value="Rounded" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1"><mxGeometry x="140" y="20" width="100" height="50" as="geometry"/></mxCell>
  <mxCell id="circle" value="Circle" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1"><mxGeometry x="260" y="10" width="70" height="70" as="geometry"/></mxCell>
  <mxCell id="diamond" value="Decision" style="rhombus;whiteSpace=wrap;html=1;" vertex="1" parent="1"><mxGeometry x="350" y="10" width="70" height="70" as="geometry"/></mxCell>
  <mxCell id="db" value="Database" style="shape=cylinder;whiteSpace=wrap;html=1;" vertex="1" parent="1"><mxGeometry x="440" y="5" width="60" height="80" as="geometry"/></mxCell>
  <mxCell id="cloud" value="Cloud" style="ellipse;shape=cloud;whiteSpace=wrap;html=1;" vertex="1" parent="1"><mxGeometry x="520" y="10" width="100" height="70" as="geometry"/></mxCell>
</root></mxGraphModel></diagram></mxfile>

Container/Swimlane
<mxfile><diagram name="Container Example" id="container-ex"><mxGraphModel dx="800" dy="600" grid="1" gridSize="10"><root><mxCell id="0"/><mxCell id="1" parent="0"/>
  <mxCell id="container" value="Container" style="swimlane;whiteSpace=wrap;html=1;" vertex="1" parent="1"><mxGeometry x="40" y="40" width="200" height="150" as="geometry"/>
  </mxCell>
  <mxCell id="zone" value="Zone Name" style="whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=none;verticalAlign=top;fontSize=14;" vertex="1" parent="1"><mxGeometry x="280" y="40" width="200" height="150" as="geometry"/>
  </mxCell>
</root></mxGraphModel></diagram></mxfile>

Swimlane with Child Elements (Relative Positioning)
<mxfile><diagram name="Swimlane" id="swimlane-ex"><mxGraphModel dx="800" dy="600" grid="1" gridSize="10"><root><mxCell id="0"/><mxCell id="1" parent="0"/>
  <mxCell id="lane1" value="Frontend" style="swimlane;" vertex="1" parent="1"><mxGeometry x="40" y="40" width="200" height="200" as="geometry"/></mxCell>
  <mxCell id="step1" value="Step 1" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="lane1"><mxGeometry x="20" y="60" width="160" height="40" as="geometry"/></mxCell>
  <mxCell id="lane2" value="Backend" style="swimlane;" vertex="1" parent="1"><mxGeometry x="280" y="40" width="200" height="200" as="geometry"/></mxCell>
  <mxCell id="step2" value="Step 2" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="lane2"><mxGeometry x="20" y="60" width="160" height="40" as="geometry"/></mxCell>
  <mxCell id="edge1" style="edgeStyle=orthogonalEdgeStyle;endArrow=classic;html=1;" edge="1" parent="1" source="step1" target="step2"><mxGeometry relative="1" as="geometry"/></mxCell>
</root></mxGraphModel></diagram></mxfile>


Note: Child elements (step1, step2) use parent="lane1" / parent="lane2" with coordinates RELATIVE to the swimlane. Edges always use parent="1" (main canvas).

Stencil Libraries

drawio provides 8900+ pre-built stencils across 48 categories for professional diagrams. Full stencil reference: See stencils/README.md.

Category	Examples	Use Case
Cloud	aws4, azure, gcp2, alibaba_cloud, ibm_cloud	Cloud architecture diagrams
Network	cisco, cisco19, cisco_safe, networks, networks2	Network topology
Virtualization	citrix, citrix2, veeam, vvd, kubernetes	Infrastructure diagrams
Software	bpmn, flowchart, sitemap, mockup	Process & UI design
Hardware	rack, cabinets, electrical	Data center & electrical
Office	office, atlassian, salesforce	Business diagrams
<mxfile><diagram name="Stencil Example" id="stencil-ex"><mxGraphModel dx="800" dy="600" grid="1" gridSize="10"><root><mxCell id="0"/><mxCell id="1" parent="0"/>
<mxCell id="router" value="" style="shape=mxgraph.cisco.routers.router;html=1;fillColor=#036897;strokeColor=#ffffff;strokeWidth=2;" vertex="1" parent="1"><mxGeometry x="100" y="100" width="78" height="53" as="geometry"/></mxCell>
</root></mxGraphModel></diagram></mxfile>

Common Style Reference
Arrow Types: Inheritance(endArrow=block;endFill=0) Implementation(endArrow=block;endFill=0;dashed=1) Association(endArrow=open;endFill=1) Dependency(endArrow=open;dashed=1) Aggregation(startArrow=diamondThin;startFill=0) Composition(startArrow=diamondThin;startFill=1)
Visibility Symbols: +(public) #(protected) -(private) ~(package) /(derived)
State Colors: Pending(#dae8fc,#6c8ebf) Success(#d5e8d4,#82b366) Error(#f8cecc,#b85450) Warning(#fff2cc,#d6b656) Complete(#e1d5e7,#9673a6)
Shape Styles: rounded(0,1) fillColor(hex) strokeColor(hex) strokeWidth(num) dashed(0,1) opacity(0-100) fontColor(hex) fontSize(num) fontStyle(0=normal,1=bold,2=italic,3=both) align(left,center,right) verticalAlign(top,middle,bottom)
Edge Styles: edgeStyle(orthogonalEdgeStyle,entityRelationEdgeStyle,elbowEdgeStyle) curved(0,1) endArrow/startArrow(classic,block,open,oval,diamond,none) endFill/startFill(0=hollow,1=filled)
Edge Examples
Basic Edge
<mxfile><diagram name="Edge Examples" id="edge-examples"><mxGraphModel dx="800" dy="600" grid="1" gridSize="10"><root><mxCell id="0"/><mxCell id="1" parent="0"/>
  <mxCell id="a1" value="A" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1"><mxGeometry x="20" y="20" width="60" height="30" as="geometry"/></mxCell>
  <mxCell id="b1" value="B" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1"><mxGeometry x="140" y="20" width="60" height="30" as="geometry"/></mxCell>
  <mxCell style="endArrow=classic;html=1;" edge="1" parent="1" source="a1" target="b1"><mxGeometry relative="1" as="geometry"/></mxCell>
  <mxCell id="a2" value="C" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1"><mxGeometry x="20" y="80" width="60" height="30" as="geometry"/></mxCell>
  <mxCell id="b2" value="D" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1"><mxGeometry x="140" y="80" width="60" height="30" as="geometry"/></mxCell>
  <mxCell style="edgeStyle=orthogonalEdgeStyle;endArrow=classic;dashed=1;html=1;" edge="1" parent="1" source="a2" target="b2"><mxGeometry relative="1" as="geometry"/></mxCell>
</root></mxGraphModel></diagram></mxfile>

Two Edges Between Same Nodes (No Overlap)
<mxfile><diagram name="Bidirectional" id="bidir"><mxGraphModel dx="800" dy="600" grid="1" gridSize="10"><root><mxCell id="0"/><mxCell id="1" parent="0"/>
  <mxCell id="nodeA" value="A" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1"><mxGeometry x="40" y="60" width="80" height="40" as="geometry"/></mxCell>
  <mxCell id="nodeB" value="B" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1"><mxGeometry x="200" y="60" width="80" height="40" as="geometry"/></mxCell>
  <mxCell id="e1" value="Request" style="edgeStyle=orthogonalEdgeStyle;exitX=1;exitY=0.3;entryX=0;entryY=0.3;endArrow=classic;html=1;" edge="1" parent="1" source="nodeA" target="nodeB"><mxGeometry relative="1" as="geometry"/></mxCell>
  <mxCell id="e2" value="Response" style="edgeStyle=orthogonalEdgeStyle;exitX=0;exitY=0.7;entryX=1;entryY=0.7;endArrow=classic;html=1;" edge="1" parent="1" source="nodeB" target="nodeA"><mxGeometry relative="1" as="geometry"/></mxCell>
</root></mxGraphModel></diagram></mxfile>

Edge with Waypoints (Routing Around Obstacle)
<mxfile><diagram name="Waypoints" id="waypoints"><mxGraphModel dx="800" dy="600" grid="1" gridSize="10"><root><mxCell id="0"/><mxCell id="1" parent="0"/>
  <mxCell id="src" value="Source" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1"><mxGeometry x="40" y="40" width="80" height="40" as="geometry"/></mxCell>
  <mxCell id="obstacle" value="Obstacle" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5;strokeColor=#666666;" vertex="1" parent="1"><mxGeometry x="160" y="100" width="80" height="40" as="geometry"/></mxCell>
  <mxCell id="tgt" value="Target" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1"><mxGeometry x="280" y="160" width="80" height="40" as="geometry"/></mxCell>
  <mxCell id="edge1" style="edgeStyle=orthogonalEdgeStyle;exitX=1;exitY=0.5;entryX=0.5;entryY=0;endArrow=classic;html=1;" edge="1" parent="1" source="src" target="tgt">
    <mxGeometry relative="1" as="geometry">
      <Array as="points">
        <mxPoint x="320" y="60"/>
      </Array>
    </mxGeometry>
  </mxCell>
</root></mxGraphModel></diagram></mxfile>

Diagonal Routing (Perimeter Pattern)

When connecting distant nodes diagonally with obstacles in between, route along the OUTSIDE perimeter:

<mxfile><diagram name="Perimeter" id="perimeter"><mxGraphModel dx="800" dy="600" grid="1" gridSize="10"><root><mxCell id="0"/><mxCell id="1" parent="0"/>
  <mxCell id="main" value="Main" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1"><mxGeometry x="200" y="40" width="80" height="40" as="geometry"/></mxCell>
  <mxCell id="develop" value="Develop" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1"><mxGeometry x="200" y="120" width="80" height="40" as="geometry"/></mxCell>
  <mxCell id="hotfix" value="Hotfix" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1"><mxGeometry x="350" y="200" width="80" height="40" as="geometry"/></mxCell>
  <mxCell id="hotfix_to_main" style="edgeStyle=orthogonalEdgeStyle;exitX=0.5;exitY=0;entryX=1;entryY=0.5;endArrow=classic;html=1;" edge="1" parent="1" source="hotfix" target="main">
    <mxGeometry relative="1" as="geometry">
      <Array as="points">
        <mxPoint x="390" y="60"/>
      </Array>
    </mxGeometry>
  </mxCell>
</root></mxGraphModel></diagram></mxfile>


Key: Route goes RIGHT (x=390) then UP, avoiding the Develop node in the middle.

Complete Example: Simple Architecture
<mxfile><diagram name="Architecture" id="arch-1"><mxGraphModel dx="800" dy="600" grid="1" gridSize="10"><root><mxCell id="0"/><mxCell id="1" parent="0"/>
  <mxCell id="client" value="Client" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1"><mxGeometry x="40" y="100" width="100" height="50" as="geometry"/></mxCell>
  <mxCell id="server" value="Server" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1"><mxGeometry x="240" y="100" width="100" height="50" as="geometry"/></mxCell>
  <mxCell id="db" value="Database" style="shape=cylinder;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;" vertex="1" parent="1"><mxGeometry x="440" y="85" width="80" height="80" as="geometry"/></mxCell>
  <mxCell style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=classic;" edge="1" parent="1" source="client" target="server"><mxGeometry relative="1" as="geometry"/></mxCell>
  <mxCell style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=classic;" edge="1" parent="1" source="server" target="db"><mxGeometry relative="1" as="geometry"/></mxCell>
</root></mxGraphModel></diagram</mxfile>

Common Pitfalls
Issue	Solution
Shape not visible	Verify vertex="1" and parent="1" attributes
Edge not connecting	Ensure source and target match cell IDs
Styles not applying	Check semicolon separators in style string
Text not showing	Add html=1;whiteSpace=wrap; to style
Edges crossing shapes	Use waypoints to route around obstacles
Multiple edges overlapping	Use different exitY/entryY values (0.3 and 0.7)
Corner connections look ugly	Use edge centers instead (exitX=1,exitY=0.5)
Diagram too spread out	Keep within x: 0-800, y: 0-600 viewport
XML comments break editing	NEVER include <!-- ... --> in generated XML
Tips for AI Generation
Plan layout first: Sketch positions mentally before writing XML — identify potential edge crossings
Use grid alignment: Position shapes at multiples of 10 or 20
Unique IDs: Use descriptive IDs like client, server, db instead of random strings
Consistent spacing: Keep 40-60px gaps between connected shapes; 150-200px for routing channels
Layer backgrounds first: Define zone/container cells before shapes inside them
Color zones: Use light background colors with strokeColor=none for region highlighting
Verify edges mentally: Before generating, trace each edge and ask "Does this cross any shape?"
Escape special characters: Use &lt; for <, &gt; for >, &amp; for &, &quot; for "
Resources
drawio Documentation
mxGraph API Reference
Weekly Installs
277
Repository
markdown-viewer/skills
GitHub Stars
2.4K
First Seen
Jan 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass