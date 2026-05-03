---
rating: ⭐⭐⭐
title: fbp-spec
url: https://skills.sh/constructive-io/constructive-skills/fbp-spec
---

# fbp-spec

skills/constructive-io/constructive-skills/fbp-spec
fbp-spec
Installation
$ npx skills add https://github.com/constructive-io/constructive-skills --skill fbp-spec
SKILL.md

Storage specification and manipulation API for flow-based programming graphs.

Installation
pnpm add @fbp/spec

Overview

@fbp/spec provides a two-layer type system for flow-based programming graphs:

Layer	Purpose
Storage	Minimal canonical format for persistence
Renderer	Extended types with derived data for UI
API	Pure functions for graph manipulation

The storage layer is designed for content-addressable storage (merkle trees) where each graph state can be uniquely hashed.

Design Philosophy
Boundary Nodes as Single Source of Truth

Traditional graph formats store interface definitions in two places (arrays and boundary nodes), causing sync bugs. This spec eliminates the problem by using boundary nodes as the ONLY source of truth.

The inputs/outputs/props arrays are NOT stored in the storage format — they are derived at runtime from boundary nodes and cached in the renderer layer.

Path-Based Identity

Nodes are identified by their path from the root:

/                     # Root scope
/add1                 # Root-level node
/subnet1/add1         # Node inside subnet1
/subnet1/nested/add1  # Deeply nested node

Per-Scope Edges

Edges are stored within the scope they belong to. Root-level edges are in graph.edges, subnet edges are in node.edges.

API Reference

All API functions are pure and immutable — they return new graphs without modifying the original.

Path Utilities
import { parsePath, joinPath, getParentPath, getNodeName, isRootPath } from '@fbp/spec';

parsePath('/foo/bar')     // ['foo', 'bar']
joinPath(['foo', 'bar'])  // '/foo/bar'
getParentPath('/foo/bar') // '/foo'
getNodeName('/foo/bar')   // 'bar'
isRootPath('/')           // true

Node Operations
import { insertNode, removeNode, renameNode, moveNode } from '@fbp/spec';

// Insert a node at root scope
const newGraph = insertNode(graph, '/', { 
  name: 'add1', 
  type: 'math/add' 
});

// Insert into a subnet
const newGraph = insertNode(graph, '/subnet1', { 
  name: 'multiply1', 
  type: 'math/multiply' 
});

// Remove a node and connected edges
const newGraph = removeNode(graph, '/add1');

// Rename a node (updates edge references)
const newGraph = renameNode(graph, '/add1', 'adder');

// Move a node to a different scope
const newGraph = moveNode(graph, '/add1', '/subnet1');

Property Operations
import { setProps, getProps, removeProp } from '@fbp/spec';

const newGraph = setProps(graph, '/add1', [
  { name: 'a', value: 5 },
  { name: 'b', value: 10 }
]);

const props = getProps(graph, '/add1');
// [{ name: 'a', value: 5 }, { name: 'b', value: 10 }]

const newGraph = removeProp(graph, '/add1', 'a');

Edge Operations
import { addEdge, removeEdge } from '@fbp/spec';

const newGraph = addEdge(graph, '/', {
  src: { node: 'input1', port: 'value' },
  dst: { node: 'add1', port: 'a' }
});

const newGraph = removeEdge(graph, '/',
  { node: 'input1', port: 'value' },
  { node: 'add1', port: 'a' }
);

Query Helpers
import { getNode, getNodes, getEdges, findNodes, findBoundaryNodes, hasNode, countNodes } from '@fbp/spec';

const node = getNode(graph, '/subnet1/add1');
const rootNodes = getNodes(graph, '/');
const rootEdges = getEdges(graph, '/');

const addNodes = findNodes(graph, (node) => node.type === 'math/add');
// [{ node: {...}, path: '/add1' }, { node: {...}, path: '/subnet1/add2' }]

const boundary = findBoundaryNodes(graph, '/subnet1');
// { inputs: [...], outputs: [...], props: [...] }

if (hasNode(graph, '/subnet1/add1')) { /* exists */ }

const total = countNodes(graph);

Metadata Operations
import { setMeta, setPosition } from '@fbp/spec';

const newGraph = setMeta(graph, '/add1', { description: 'Adds two numbers' });
const newGraph = setPosition(graph, '/add1', 100, 200);

Example: Simple Math Graph
{
  "nodes": [
    { 
      "name": "input_a", 
      "type": "graphInput", 
      "meta": { "x": 0, "y": 0 },
      "props": [
        { "name": "portName", "value": "a" }, 
        { "name": "dataType", "value": "number" }
      ]
    },
    { 
      "name": "input_b", 
      "type": "graphInput", 
      "meta": { "x": 0, "y": 100 },
      "props": [
        { "name": "portName", "value": "b" }, 
        { "name": "dataType", "value": "number" }
      ]
    },
    { 
      "name": "add1", 
      "type": "math/add", 
      "meta": { "x": 200, "y": 50 }
    },
    { 
      "name": "output_sum", 
      "type": "graphOutput", 
      "meta": { "x": 400, "y": 50 },
      "props": [
        { "name": "portName", "value": "sum" }, 
        { "name": "dataType", "value": "number" }
      ]
    }
  ],
  "edges": [
    { "src": { "node": "input_a", "port": "value" }, "dst": { "node": "add1", "port": "a" } },
    { "src": { "node": "input_b", "port": "value" }, "dst": { "node": "add1", "port": "b" } },
    { "src": { "node": "add1", "port": "sum" }, "dst": { "node": "output_sum", "port": "value" } }
  ]
}

Normative Rules
Boundary Nodes ARE the Interface — No separate inputs/outputs/props arrays in storage
Edges are Per-Scope — Each subnet stores its own edges
Path-Based Identity — Renaming/moving changes identity
Minimal Storage — Only store what's needed to reconstruct the graph
Weekly Installs
13
Repository
constructive-io…e-skills
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass