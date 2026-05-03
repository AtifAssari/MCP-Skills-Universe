---
rating: ⭐⭐⭐
title: react-flow
url: https://skills.sh/existential-birds/beagle/react-flow
---

# react-flow

skills/existential-birds/beagle/react-flow
react-flow
Installation
$ npx skills add https://github.com/existential-birds/beagle --skill react-flow
Summary

Interactive node-based graph visualization and workflow editor for React applications.

Provides built-in node types (default, input, output, group) and edge types (bezier, straight, step, smoothstep) with full customization via custom components
Includes Handle components for connection points, NodeProps and EdgeProps for typed custom nodes and edges, and EdgeLabelRenderer for interactive labels
Offers programmatic control through useReactFlow hook for viewport management (fitView, zoom, pan), node/edge manipulation, and coordinate transformation
Supports comprehensive event handling for node/edge interactions, connections, selection changes, and viewport updates with connection validation
SKILL.md
React Flow

React Flow (@xyflow/react) is a library for building node-based graphs, workflow editors, and interactive diagrams. It provides a highly customizable framework for creating visual programming interfaces, process flows, and network visualizations.

Quick Start
Installation
pnpm add @xyflow/react

Basic Setup
import { ReactFlow, Node, Edge, Background, Controls, MiniMap } from '@xyflow/react';
import '@xyflow/react/dist/style.css';

const initialNodes: Node[] = [
  {
    id: '1',
    type: 'input',
    data: { label: 'Input Node' },
    position: { x: 250, y: 5 },
  },
  {
    id: '2',
    data: { label: 'Default Node' },
    position: { x: 100, y: 100 },
  },
  {
    id: '3',
    type: 'output',
    data: { label: 'Output Node' },
    position: { x: 400, y: 100 },
  },
];

const initialEdges: Edge[] = [
  { id: 'e1-2', source: '1', target: '2', animated: true },
  { id: 'e2-3', source: '2', target: '3' },
];

function Flow() {
  return (
    <div style={{ width: '100vw', height: '100vh' }}>
      <ReactFlow nodes={initialNodes} edges={initialEdges}>
        <Background />
        <Controls />
        <MiniMap />
      </ReactFlow>
    </div>
  );
}

export default Flow;

Core Concepts
Nodes

Nodes are the building blocks of the graph. Each node has:

id: Unique identifier
type: Node type (built-in or custom)
position: { x, y } coordinates
data: Custom data object
import { Node } from '@xyflow/react';

const node: Node = {
  id: 'node-1',
  type: 'default',
  position: { x: 100, y: 100 },
  data: { label: 'Node Label' },
  style: { background: '#D6D5E6' },
  className: 'custom-node',
};


Built-in node types:

default: Standard node
input: No target handles
output: No source handles
group: Container for other nodes
Edges

Edges connect nodes. Each edge requires:

id: Unique identifier
source: Source node ID
target: Target node ID
import { Edge } from '@xyflow/react';

const edge: Edge = {
  id: 'e1-2',
  source: '1',
  target: '2',
  type: 'smoothstep',
  animated: true,
  label: 'Edge Label',
  style: { stroke: '#fff', strokeWidth: 2 },
};


Built-in edge types:

default: Bezier curve
straight: Straight line
step: Orthogonal with sharp corners
smoothstep: Orthogonal with rounded corners
Handles

Handles are connection points on nodes. Use Position enum for placement:

import { Handle, Position } from '@xyflow/react';

<Handle type="target" position={Position.Top} />
<Handle type="source" position={Position.Bottom} />


Available positions: Position.Top, Position.Right, Position.Bottom, Position.Left

State Management
Controlled Flow

Use state hooks for full control:

import { useNodesState, useEdgesState, addEdge, OnConnect } from '@xyflow/react';
import { useCallback } from 'react';

function ControlledFlow() {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);

  const onConnect: OnConnect = useCallback(
    (connection) => setEdges((eds) => addEdge(connection, eds)),
    [setEdges]
  );

  return (
    <ReactFlow
      nodes={nodes}
      edges={edges}
      onNodesChange={onNodesChange}
      onEdgesChange={onEdgesChange}
      onConnect={onConnect}
    />
  );
}

useReactFlow Hook

Access the React Flow instance for programmatic control:

import { useReactFlow } from '@xyflow/react';

function FlowControls() {
  const {
    getNodes,
    getEdges,
    setNodes,
    setEdges,
    addNodes,
    addEdges,
    deleteElements,
    fitView,
    zoomIn,
    zoomOut,
    getNode,
    getEdge,
    updateNode,
    updateEdge,
  } = useReactFlow();

  return (
    <button onClick={() => fitView()}>Fit View</button>
  );
}

Custom Nodes

Define custom nodes using NodeProps<T> with typed data:

import { NodeProps, Node, Handle, Position } from '@xyflow/react';

export type CustomNode = Node<{ label: string; status: 'active' | 'inactive' }, 'custom'>;

function CustomNodeComponent({ data, selected }: NodeProps<CustomNode>) {
  return (
    <div className={`px-4 py-2 ${selected ? 'ring-2' : ''}`}>
      <Handle type="target" position={Position.Top} />
      <div className="font-bold">{data.label}</div>
      <Handle type="source" position={Position.Bottom} />
    </div>
  );
}


Register with nodeTypes:

const nodeTypes: NodeTypes = { custom: CustomNodeComponent };
<ReactFlow nodeTypes={nodeTypes} />

Key Patterns
Multiple Handles: Use id prop and style for positioning
Dynamic Handles: Call useUpdateNodeInternals([nodeId]) after adding/removing handles
Interactive Elements: Add className="nodrag" to prevent dragging on inputs/buttons

See Custom Nodes Reference for detailed patterns including styling, aviation map pins, and dynamic handles.

Custom Edges

Define custom edges using EdgeProps<T> and path utilities:

import { BaseEdge, EdgeProps, getBezierPath } from '@xyflow/react';

export type CustomEdge = Edge<{ status: 'normal' | 'error' }, 'custom'>;

function CustomEdgeComponent(props: EdgeProps<CustomEdge>) {
  const [edgePath] = getBezierPath(props);

  return (
    <BaseEdge
      id={props.id}
      path={edgePath}
      style={{ stroke: props.data?.status === 'error' ? '#ef4444' : '#64748b' }}
    />
  );
}

Path Utilities
getBezierPath() - Smooth curves
getStraightPath() - Straight lines
getSmoothStepPath() - Orthogonal with rounded corners
getSmoothStepPath({ borderRadius: 0 }) - Orthogonal with sharp corners (step edge)

All return [path, labelX, labelY, offsetX, offsetY].

Interactive Labels

Use EdgeLabelRenderer for HTML-based labels with pointer events:

import { EdgeLabelRenderer, BaseEdge, getBezierPath } from '@xyflow/react';

function ButtonEdge(props: EdgeProps) {
  const [edgePath, labelX, labelY] = getBezierPath(props);
  return (
    <>
      <BaseEdge id={props.id} path={edgePath} />
      <EdgeLabelRenderer>
        <div
          style={{
            position: 'absolute',
            transform: `translate(-50%, -50%) translate(${labelX}px, ${labelY}px)`,
            pointerEvents: 'all',
          }}
          className="nodrag nopan"
        >
          <button onClick={() => console.log('Delete')}>×</button>
        </div>
      </EdgeLabelRenderer>
    </>
  );
}


See Custom Edges Reference for animated edges, time labels, and SVG text patterns.

Viewport Control

Use useReactFlow() hook for programmatic viewport control:

import { useReactFlow } from '@xyflow/react';

function ViewportControls() {
  const { fitView, zoomIn, zoomOut, setCenter, screenToFlowPosition } = useReactFlow();

  // Fit all nodes in view
  const handleFitView = () => fitView({ padding: 0.2, duration: 400 });

  // Zoom controls
  const handleZoomIn = () => zoomIn({ duration: 300 });
  const handleZoomOut = () => zoomOut({ duration: 300 });

  // Center on specific coordinates
  const handleCenter = () => setCenter(250, 250, { zoom: 1.5, duration: 500 });

  // Convert screen coordinates to flow coordinates
  const addNodeAtClick = (event: React.MouseEvent) => {
    const position = screenToFlowPosition({ x: event.clientX, y: event.clientY });
    // Use position to add node
  };

  return null;
}


See Viewport Reference for save/restore state, controlled viewport, and coordinate transformations.

Events

React Flow provides comprehensive event handling:

Node Events
import { NodeMouseHandler, OnNodeDrag } from '@xyflow/react';

const onNodeClick: NodeMouseHandler = (event, node) => {
  console.log('Node clicked:', node.id);
};

const onNodeDrag: OnNodeDrag = (event, node, nodes) => {
  console.log('Dragging:', node.id);
};

<ReactFlow
  onNodeClick={onNodeClick}
  onNodeDrag={onNodeDrag}
  onNodeDragStop={onNodeClick}
/>

Edge and Connection Events
import { EdgeMouseHandler, OnConnect } from '@xyflow/react';

const onEdgeClick: EdgeMouseHandler = (event, edge) => console.log('Edge:', edge.id);
const onConnect: OnConnect = (connection) => console.log('Connected:', connection);

<ReactFlow onEdgeClick={onEdgeClick} onConnect={onConnect} />

Selection and Viewport Events
import { useOnSelectionChange, useOnViewportChange } from '@xyflow/react';

useOnSelectionChange({
  onChange: ({ nodes, edges }) => console.log('Selected:', nodes.length, edges.length),
});

useOnViewportChange({
  onChange: (viewport) => console.log('Viewport:', viewport.zoom),
});


See Events Reference for complete event catalog including validation, deletion, and error handling.

Common Patterns
Preventing Drag/Pan
<input className="nodrag" />
<button className="nodrag nopan">Click me</button>

Connection Validation
const isValidConnection = (connection: Connection) => {
  return connection.source !== connection.target; // Prevent self-connections
};

<ReactFlow isValidConnection={isValidConnection} />

Adding Nodes on Click
const { screenToFlowPosition, setNodes } = useReactFlow();

const onPaneClick = (event: React.MouseEvent) => {
  const position = screenToFlowPosition({ x: event.clientX, y: event.clientY });
  setNodes(nodes => [...nodes, { id: `node-${Date.now()}`, position, data: { label: 'New' } }]);
};

Updating Node Data
const { updateNodeData } = useReactFlow();
updateNodeData('node-1', { label: 'Updated' });
updateNodeData('node-1', (node) => ({ ...node.data, count: node.data.count + 1 }));

Provider Pattern

Wrap the app with ReactFlowProvider when using useReactFlow() outside the flow:

import { ReactFlow, ReactFlowProvider, useReactFlow } from '@xyflow/react';

function Controls() {
  const { fitView } = useReactFlow(); // Must be inside provider
  return <button onClick={() => fitView()}>Fit View</button>;
}

function App() {
  return (
    <ReactFlowProvider>
      <Controls />
      <ReactFlow nodes={nodes} edges={edges} />
    </ReactFlowProvider>
  );
}

Reference Files

For detailed implementation patterns, see:

Custom Nodes - NodeProps typing, Handle component, dynamic handles, styling patterns
Custom Edges - EdgeProps typing, path utilities, EdgeLabelRenderer, animated edges
Viewport - useReactFlow methods, fitView options, coordinate conversion
Events - Node/edge/connection events, selection handling, viewport changes
Weekly Installs
708
Repository
existential-birds/beagle
GitHub Stars
56
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass