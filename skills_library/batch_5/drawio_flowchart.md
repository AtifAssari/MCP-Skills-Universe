---
title: drawio-flowchart
url: https://skills.sh/teachingai/full-stack-skills/drawio-flowchart
---

# drawio-flowchart

skills/teachingai/full-stack-skills/drawio-flowchart
drawio-flowchart
Installation
$ npx skills add https://github.com/teachingai/full-stack-skills --skill drawio-flowchart
SKILL.md
When to use this skill

Use this skill whenever the user wants to:

Create flowcharts for business processes or technical workflows
Design swim lane diagrams showing responsibilities across teams or systems
Visualize decision trees with conditional branching
Export process diagrams for documentation or presentations
How to use this skill
Workflow
Start from template - Choose Flowchart template in Draw.io or start blank
Add shapes - Use standard shapes: rounded rectangle (start/end), rectangle (process), diamond (decision)
Connect with arrows - Label decision branches (Yes/No) and flow direction
Apply auto-layout - Use Format > Layout > Vertical/Horizontal Tree for clean alignment
Export - Save as .drawio for editing; export PNG/SVG/PDF for sharing
Quick-Start Example: Order Processing Flowchart (XML)
<mxGraphModel>
  <root>
    <mxCell id="0"/><mxCell id="1" parent="0"/>
    <!-- Start -->
    <mxCell id="2" value="Order Received" style="ellipse;fillColor=#d5e8d4;" vertex="1" parent="1">
      <mxGeometry x="200" y="20" width="120" height="40" as="geometry"/>
    </mxCell>
    <!-- Decision -->
    <mxCell id="3" value="In Stock?" style="rhombus;fillColor=#fff2cc;" vertex="1" parent="1">
      <mxGeometry x="200" y="100" width="120" height="60" as="geometry"/>
    </mxCell>
    <!-- Process -->
    <mxCell id="4" value="Ship Order" style="rounded=0;fillColor=#dae8fc;" vertex="1" parent="1">
      <mxGeometry x="100" y="200" width="120" height="40" as="geometry"/>
    </mxCell>
    <mxCell id="5" value="Backorder" style="rounded=0;fillColor=#f8cecc;" vertex="1" parent="1">
      <mxGeometry x="300" y="200" width="120" height="40" as="geometry"/>
    </mxCell>
    <!-- Arrows -->
    <mxCell id="6" style="" edge="1" source="2" target="3" parent="1"/>
    <mxCell id="7" value="Yes" edge="1" source="3" target="4" parent="1"/>
    <mxCell id="8" value="No" edge="1" source="3" target="5" parent="1"/>
  </root>
</mxGraphModel>

Swim Lane Diagram

For cross-team processes, use Draw.io's swim lane containers:

Insert > Advanced > Pool/Lane
Drag process steps into the appropriate lane
Connect steps across lanes with labeled arrows
Best Practices
Consistent flow direction - Use top-to-bottom or left-to-right consistently
Standard shapes - Rectangles for processes, diamonds for decisions, ovals for start/end
Label decision branches - Always label Yes/No or condition text on decision arrows
One process per diagram - Keep diagrams focused; split complex flows into sub-processes
Include a legend - Add a key explaining shape meanings and color coding
Keywords

draw.io, diagrams.net, flowchart, swim lane, business process, decision tree, workflow diagram, 流程图, 泳道图, process diagram

Weekly Installs
320
Repository
teachingai/full…k-skills
GitHub Stars
349
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass