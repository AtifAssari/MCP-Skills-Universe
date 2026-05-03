---
rating: ⭐⭐
title: arcgis-knowledge-graphs
url: https://skills.sh/saschabrunnerch/arcgis-maps-sdk-js-ai-context/arcgis-knowledge-graphs
---

# arcgis-knowledge-graphs

skills/saschabrunnerch/arcgis-maps-sdk-js-ai-context/arcgis-knowledge-graphs
arcgis-knowledge-graphs
Installation
$ npx skills add https://github.com/saschabrunnerch/arcgis-maps-sdk-js-ai-context --skill arcgis-knowledge-graphs
SKILL.md
ArcGIS Knowledge Graphs

Use this skill for knowledge graphs, graph queries (openCypher), link chart visualization, and entity-relationship management.

Import Patterns
ESM (npm)
// Knowledge graph service
import * as knowledgeGraphService from "@arcgis/core/rest/knowledgeGraphService.js";

// Layers
import KnowledgeGraphLayer from "@arcgis/core/layers/KnowledgeGraphLayer.js";
import LinkChartLayer from "@arcgis/core/layers/LinkChartLayer.js";

// Views and charts
import WebLinkChart from "@arcgis/core/WebLinkChart.js";
import LinkChartView from "@arcgis/core/views/LinkChartView.js";

// Layout settings
import OrganicLayoutSettings from "@arcgis/core/linkChart/OrganicLayoutSettings.js";
import ChronologicalLayoutSettings from "@arcgis/core/linkChart/ChronologicalLayoutSettings.js";
import LinkChartLayoutSwitcher from "@arcgis/core/linkChart/LinkChartLayoutSwitcher.js";

CDN (dynamic import)
const knowledgeGraphService = await $arcgis.import(
  "@arcgis/core/rest/knowledgeGraphService.js",
);
const KnowledgeGraphLayer = await $arcgis.import(
  "@arcgis/core/layers/KnowledgeGraphLayer.js",
);
const WebLinkChart = await $arcgis.import("@arcgis/core/WebLinkChart.js");
const LinkChartView = await $arcgis.import(
  "@arcgis/core/views/LinkChartView.js",
);

Knowledge Graph Service
Fetch Knowledge Graph
const url =
  "https://your-server/server/rest/services/Hosted/YourKG/KnowledgeGraphServer";
const knowledgeGraph = await knowledgeGraphService.fetchKnowledgeGraph(url);

console.log("Graph name:", knowledgeGraph.name);
console.log("Entity types:", knowledgeGraph.dataModel.entityTypes);
console.log("Relationship types:", knowledgeGraph.dataModel.relationshipTypes);

Service Functions
Function	Description
fetchKnowledgeGraph(url)	Fetch knowledge graph metadata and data model
executeQuery(kg, params)	Execute openCypher query, return all results
executeQueryStreaming(kg, params)	Stream large query results
executeSearch(kg, params)	Full-text search across entities
executeApplyEdits(kg, params)	Add, update, or delete entities and relationships
KnowledgeGraphLayer
Add to Map
const kgLayer = new KnowledgeGraphLayer({
  url: "https://your-server/server/rest/services/Hosted/YourKG/KnowledgeGraphServer",
});

await kgLayer.load();
map.add(kgLayer);

Configure Sublayers
const kgLayer = new KnowledgeGraphLayer({
  url: "...",
  inclusionModeDefinition: {
    generateAllSublayers: false,
    namedTypeDefinitions: new Map([
      ["Person", { useAllData: true }],
      ["Location", { useAllData: true }],
    ]),
  },
});

Querying with openCypher
Basic Query
const result = await knowledgeGraphService.executeQuery(knowledgeGraph, {
  openCypherQuery: "MATCH (n:Person) RETURN n LIMIT 10",
});

console.log("Results:", result.resultRows);

Streaming Query (Large Results)
const queryResults = await knowledgeGraphService.executeQueryStreaming(
  knowledgeGraph,
  {
    openCypherQuery: "MATCH (n:Person)-[r]->(m) RETURN n, r, m",
  },
);

const reader = queryResults.resultRowsStream.getReader();

while (true) {
  const { done, value } = await reader.read();
  if (done) break;

  value.forEach((row) => {
    console.log("Row:", row);
  });
}

Spatial Query with Bind Parameters
import Polygon from "@arcgis/core/geometry/Polygon.js";

const searchArea = new Polygon({
  rings: [
    [
      [-76, 45],
      [-70, 45],
      [-70, 40],
      [-76, 40],
      [-76, 45],
    ],
  ],
});

const queryResults = await knowledgeGraphService.executeQueryStreaming(
  knowledgeGraph,
  {
    openCypherQuery: `
    MATCH path=(a:User)-[]->(b:Observation)
    WHERE esri.graph.ST_Intersects($geometry, b.shape)
    RETURN path
  `,
    bindParameters: {
      geometry: searchArea,
    },
  },
);

Query with Filters
// Filter by property
const result = await knowledgeGraphService.executeQuery(knowledgeGraph, {
  openCypherQuery: `
    MATCH (p:Person)
    WHERE p.age > 30 AND p.name CONTAINS 'John'
    RETURN p
  `,
});

// Query relationships
const result = await knowledgeGraphService.executeQuery(knowledgeGraph, {
  openCypherQuery: `
    MATCH (p:Person)-[r:WORKS_AT]->(c:Company)
    WHERE c.name = 'Esri'
    RETURN p.name, r.startDate, c.name
  `,
});

Common openCypher Patterns
-- Find all entities of a type
MATCH (p:Person) RETURN p

-- Find relationships
MATCH (a)-[r]->(b) RETURN a, r, b

-- Find path with depth
MATCH path = (a:Person)-[:KNOWS*1..3]->(b:Person)
WHERE a.name = 'John'
RETURN path

-- Aggregate
MATCH (p:Person)-[:WORKS_AT]->(c:Company)
RETURN c.name, COUNT(p) as employeeCount

-- Spatial filter
MATCH (loc:Location)
WHERE esri.graph.ST_Intersects($geometry, loc.shape)
RETURN loc

Search Knowledge Graph
const searchResults = await knowledgeGraphService.executeSearch(
  knowledgeGraph,
  {
    searchQuery: "John Smith",
    typeCategoryFilter: "entity", // "entity", "relationship", "both"
    typeNames: ["Person", "Employee"],
    returnSearchContext: true,
  },
);

searchResults.results.forEach((result) => {
  console.log("Found:", result.typeName, result.id);
  console.log("Context:", result.searchContext);
});

Apply Edits
// Add entity
await knowledgeGraphService.executeApplyEdits(knowledgeGraph, {
  entityAdds: [
    {
      typeName: "Person",
      properties: { name: "Jane Doe", age: 28 },
    },
  ],
});

// Update entity
await knowledgeGraphService.executeApplyEdits(knowledgeGraph, {
  entityUpdates: [
    {
      typeName: "Person",
      properties: { globalId: "{existing-global-id}", age: 29 },
    },
  ],
});

// Delete entity
await knowledgeGraphService.executeApplyEdits(knowledgeGraph, {
  entityDeletes: [
    {
      typeName: "Person",
      ids: ["{global-id-to-delete}"],
    },
  ],
});

// Add relationship
await knowledgeGraphService.executeApplyEdits(knowledgeGraph, {
  relationshipAdds: [
    {
      typeName: "WORKS_AT",
      properties: {
        originGlobalId: "{person-global-id}",
        destinationGlobalId: "{company-global-id}",
        startDate: new Date(),
      },
    },
  ],
});

Data Model
const dataModel = knowledgeGraph.dataModel;

dataModel.entityTypes.forEach((entityType) => {
  console.log("Entity:", entityType.name);
  console.log("Properties:", entityType.properties);
});

dataModel.relationshipTypes.forEach((relType) => {
  console.log("Relationship:", relType.name);
  console.log("Origin:", relType.originEntityTypes);
  console.log("Destination:", relType.destinationEntityTypes);
});

Link Chart Visualization
Create Link Chart (Core API)
const linkChartLayer = new LinkChartLayer({
  url: "https://your-server/.../KnowledgeGraphServer",
});

const linkChart = new WebLinkChart({
  layers: [linkChartLayer],
});

const linkChartView = new LinkChartView({
  container: "linkChartDiv",
  map: linkChart,
  highlightOptions: {
    color: [0, 255, 255, 1],
    haloColor: [0, 255, 255, 0.5],
    haloOpacity: 0.8,
  },
});

Link Chart Component
<arcgis-link-chart>
  <arcgis-legend slot="top-right"></arcgis-legend>
  <arcgis-zoom slot="bottom-right"></arcgis-zoom>
</arcgis-link-chart>

<script type="module">
  const linkChartComponent = document.querySelector("arcgis-link-chart");
  await linkChartComponent.componentOnReady();

  const lcView = linkChartComponent.view;
  const linkChart = lcView.map;

  await linkChart.addRecords([
    { id: "entity1", typeName: "Person" },
    { id: "entity2", typeName: "Company" },
  ]);
</script>

Adding and Removing Records
// Add records
await linkChart.addRecords([
  { id: "person-1", typeName: "Person" },
  { id: "company-1", typeName: "Company" },
  { id: "rel-1", typeName: "WORKS_AT" },
]);

// Remove records
await linkChart.removeRecords([{ id: "person-1", typeName: "Person" }]);

Expand Entities
await linkChart.expand({
  ids: ["entity-id"],
  typeName: "Person",
  relationshipTypes: ["KNOWS", "WORKS_AT"],
  direction: "both", // "outgoing", "incoming", "both"
});

Navigate to Entities
linkChartView.goTo([{ id: "person-1", typeName: "Person" }]);

Link Chart Events
linkChartView.on("click", async (event) => {
  const response = await linkChartView.hitTest(event);
  if (response.results.length > 0) {
    const graphic = response.results[0].graphic;
    console.log("Clicked:", graphic.attributes);
  }
});

Update Link Chart from Query Results
async function updateLinkChart(queryResults, linkChart) {
  const reader = queryResults.resultRowsStream.getReader();

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;

    const records = [];
    for (const row of value) {
      for (const record of row[0].path) {
        records.push({
          id: record.id,
          typeName: record.typeName,
        });
      }
    }

    await linkChart.addRecords(records);
  }
}

Layout Settings
Organic Layout
const organicLayout = new OrganicLayoutSettings();
linkChart.layoutSettings = organicLayout;

Chronological Layout
const chronoLayout = new ChronologicalLayoutSettings();
linkChart.layoutSettings = chronoLayout;

Layout Switcher Widget
const layoutSwitcher = new LinkChartLayoutSwitcher({
  view: linkChartView,
});

linkChartView.ui.add(layoutSwitcher, "top-right");

Layout Switcher Component
<arcgis-link-chart>
  <arcgis-link-chart-layout-switcher
    slot="top-right"
  ></arcgis-link-chart-layout-switcher>
</arcgis-link-chart>

WebLinkChart Properties
const webLinkChart = new WebLinkChart({
  portalItem: { id: "LINKCHART_ID" },
  layoutSettings: organicLayout,
});

// Save to portal
await webLinkChart.saveAs({
  title: "My Link Chart",
  snippet: "Visualization of entity relationships",
});

Common Pitfalls

Authentication required: Knowledge graph services typically require authentication — configure credentials or OAuth.

Streaming for large results: Use executeQueryStreaming for queries that may return many results; executeQuery loads everything into memory.

Geometry conversion: Convert geometries to WGS84 before using in spatial queries with esri.graph.ST_Intersects.

Case sensitivity: openCypher property names are case-sensitive — p.Name and p.name are different.

Load before querying: Ensure await kgLayer.load() before accessing sublayers or metadata.

Link chart records: Both entities and relationships must be added as records for links to display.

Reference Samples
knowledgegraph-query — Querying knowledge graphs with openCypher
knowledgegraph-knowledgegraphlayer — Using KnowledgeGraphLayer
knowledgegraph-search — Full-text search
knowledgegraph-applyedits — Editing graph entities
knowledgegraph-datamodelediting — Data model editing
linkchart — Link chart visualization
Related Skills
arcgis-layers — Layer configuration and management
arcgis-interaction — Hit testing and event handling
arcgis-editing — Feature editing patterns
Weekly Installs
36
Repository
saschabrunnerch…-context
GitHub Stars
13
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass