---
title: arcgis-coordinates-projection
url: https://skills.sh/saschabrunnerch/arcgis-maps-sdk-js-ai-context/arcgis-coordinates-projection
---

# arcgis-coordinates-projection

skills/saschabrunnerch/arcgis-maps-sdk-js-ai-context/arcgis-coordinates-projection
arcgis-coordinates-projection
Installation
$ npx skills add https://github.com/saschabrunnerch/arcgis-maps-sdk-js-ai-context --skill arcgis-coordinates-projection
SKILL.md
ArcGIS Coordinates and Projection

Use this skill for coordinate conversion, projection transformations, spatial reference handling, and displaying coordinates in various formats.

Important: The projection module (deprecated since 4.32) and geodesicUtils (deprecated since 4.33) were removed in v5.0. Use projectOperator and geodetic geometry operators instead.

Import Patterns
Direct ESM Imports
import projectOperator from "@arcgis/core/geometry/operators/projectOperator.js";
import SpatialReference from "@arcgis/core/geometry/SpatialReference.js";
import coordinateFormatter from "@arcgis/core/geometry/coordinateFormatter.js";
import webMercatorUtils from "@arcgis/core/geometry/support/webMercatorUtils.js";

Dynamic Imports (CDN)
const projectOperator = await $arcgis.import(
  "@arcgis/core/geometry/operators/projectOperator.js",
);
const coordinateFormatter = await $arcgis.import(
  "@arcgis/core/geometry/coordinateFormatter.js",
);
const [SpatialReference, webMercatorUtils] = await $arcgis.import([
  "@arcgis/core/geometry/SpatialReference.js",
  "@arcgis/core/geometry/support/webMercatorUtils.js",
]);

Coordinate Conversion Component
Basic Setup
<arcgis-map basemap="topo-vector" center="-117.049, 34.485" zoom="12">
  <arcgis-zoom slot="top-left"></arcgis-zoom>
  <arcgis-coordinate-conversion
    slot="bottom-left"
  ></arcgis-coordinate-conversion>
</arcgis-map>

Coordinate Conversion Widget (Core API)
import CoordinateConversion from "@arcgis/core/widgets/CoordinateConversion.js";

const ccWidget = new CoordinateConversion({ view });
view.ui.add(ccWidget, "bottom-left");

Custom Coordinate Formats
import CoordinateConversion from "@arcgis/core/widgets/CoordinateConversion.js";
import Format from "@arcgis/core/widgets/CoordinateConversion/support/Format.js";

const customFormat = new Format({
  name: "Custom XY",
  conversionInfo: {
    spatialReference: { wkid: 4326 },
    reverseConvert: (string) => {
      const parts = string.split(",");
      return [parseFloat(parts[0]), parseFloat(parts[1])];
    },
  },
  coordinateSegments: [
    { alias: "Lon", description: "Longitude", searchPattern: "X" },
    { alias: "Lat", description: "Latitude", searchPattern: "Y" },
  ],
  defaultPattern: "X°, Y°",
});

const ccWidget = new CoordinateConversion({
  view,
  formats: [customFormat],
});

Spatial Reference
Common Spatial References
Name	WKID	Type
WGS 84	4326	Geographic
Web Mercator	102100 or 3857	Projected
UTM Zone 11N	32611	Projected
State Plane (example)	2230	Projected
Create Spatial Reference
import SpatialReference from "@arcgis/core/geometry/SpatialReference.js";

// By WKID
const wgs84 = new SpatialReference({ wkid: 4326 });
const webMercator = new SpatialReference({ wkid: 102100 });

// By WKT (for custom projections)
const customSR = new SpatialReference({
  wkt: 'PROJCS["NAD_1983_StatePlane_California_VI_FIPS_0406_Feet"...',
});

// Shorthand (autocast)
const sr = { wkid: 4326 };

SpatialReference Properties
const sr = new SpatialReference({ wkid: 4326 });

console.log(sr.isGeographic); // true for lat/lon systems
console.log(sr.isWebMercator); // true for WKID 3857/102100
console.log(sr.isWGS84); // true for WKID 4326
console.log(sr.wkid); // 4326

Client-Side Projection (projectOperator)

The recommended way to project geometries client-side.

Project Geometry
import projectOperator from "@arcgis/core/geometry/operators/projectOperator.js";

await projectOperator.load();

const projected = projectOperator.execute(geometry, { wkid: 4326 });

Project with Geographic Transformation
import projectOperator from "@arcgis/core/geometry/operators/projectOperator.js";

await projectOperator.load();

const projected = projectOperator.execute(
  geometry,
  { wkid: 4326 },
  {
    geographicTransformation: {
      steps: [{ wkid: 108190 }], // NAD_1983_To_WGS_1984_5
    },
  },
);

Shape-Preserving Projection

For projecting geometries while preserving geodesic shape (great circle arcs):

import shapePreservingProjectOperator from "@arcgis/core/geometry/operators/shapePreservingProjectOperator.js";

await shapePreservingProjectOperator.load();

const projected = shapePreservingProjectOperator.execute(geometry, {
  wkid: 3857,
});

Geographic Transformation Utilities
import geographicTransformationUtils from "@arcgis/core/geometry/operators/support/geographicTransformationUtils.js";

// Get available transformations between two spatial references
const transformations = geographicTransformationUtils.getTransformations(
  { wkid: 4269 }, // NAD83
  { wkid: 4326 }, // WGS84
);

transformations.forEach((t) => {
  console.log(t.wkid, t.wkt);
});

Server-Side Projection (Geometry Service)

For complex projections or when the client-side engine is insufficient:

import * as geometryService from "@arcgis/core/rest/geometryService.js";
import ProjectParameters from "@arcgis/core/rest/support/ProjectParameters.js";

const gsUrl =
  "https://utility.arcgisonline.com/ArcGIS/rest/services/Geometry/GeometryServer";

const params = new ProjectParameters({
  geometries: [geometry],
  outSpatialReference: { wkid: 4326 },
});

const results = await geometryService.project(gsUrl, params);
const projected = results[0];

Coordinate Conversion Utilities
Web Mercator to/from Geographic
import webMercatorUtils from "@arcgis/core/geometry/support/webMercatorUtils.js";

const geoPoint = webMercatorUtils.webMercatorToGeographic(webMercatorPoint);
const wmPoint = webMercatorUtils.geographicToWebMercator(geoPoint);
const canProject = webMercatorUtils.canProject(fromSR, toSR);

Coordinate Formatter

Convert coordinates to/from DMS, UTM, MGRS, USNG strings.

import coordinateFormatter from "@arcgis/core/geometry/coordinateFormatter.js";

await coordinateFormatter.load();

// To Degrees Minutes Seconds
const dms = coordinateFormatter.toLatitudeLongitude(point, "dms", 3);
// Output: "34°29'06.000\"N 117°02'56.400\"W"

// To MGRS
const mgrs = coordinateFormatter.toMgrs(point, "automatic", 5, false);
// Output: "11SNU1234567890"

// To UTM
const utm = coordinateFormatter.toUtm(point, "north-south-indicators", true);
// Output: "11S 500000 3800000"

// To USNG
const usng = coordinateFormatter.toUsng(point, 5, false);

// From string to point
const pointFromDMS = coordinateFormatter.fromLatitudeLongitude(
  "34°29'06\"N 117°02'56\"W",
);
const pointFromMGRS = coordinateFormatter.fromMgrs("11SNU1234567890");
const pointFromUTM = coordinateFormatter.fromUtm("11S 500000 3800000");
const pointFromUSNG = coordinateFormatter.fromUsng("11SNU1234567890");

coordinateFormatter Methods
Method	Description
toLatitudeLongitude(point, format, decimals)	Format: "dd", "dm", "dms"
toMgrs(point, mode, precision, spaces)	Military Grid Reference System
toUtm(point, mode, spaces)	Universal Transverse Mercator
toUsng(point, precision, spaces)	US National Grid
fromLatitudeLongitude(string)	Parse DMS/DD string to Point
fromMgrs(string)	Parse MGRS to Point
fromUtm(string)	Parse UTM to Point
fromUsng(string)	Parse USNG to Point
Display Coordinates
Show Mouse Coordinates
view.on("pointer-move", (event) => {
  const mapPoint = view.toMap({ x: event.x, y: event.y });
  if (mapPoint) {
    document.getElementById("coords").textContent =
      `Lat: ${mapPoint.latitude.toFixed(6)}, Lon: ${mapPoint.longitude.toFixed(6)}`;
  }
});

Multi-Format Coordinate Display
import coordinateFormatter from "@arcgis/core/geometry/coordinateFormatter.js";

await coordinateFormatter.load();

view.on("pointer-move", (event) => {
  const point = view.toMap({ x: event.x, y: event.y });
  if (point) {
    document.getElementById("latlon").textContent =
      `${point.latitude.toFixed(6)}, ${point.longitude.toFixed(6)}`;
    document.getElementById("utm").textContent = coordinateFormatter.toUtm(
      point,
      "north-south-indicators",
      true,
    );
    document.getElementById("mgrs").textContent = coordinateFormatter.toMgrs(
      point,
      "automatic",
      5,
      true,
    );
  }
});

Geodetic Geometry Operations

For geodesic calculations (distance, area, length on Earth's surface):

import geodeticDistanceOperator from "@arcgis/core/geometry/operators/geodeticDistanceOperator.js";
import geodeticAreaOperator from "@arcgis/core/geometry/operators/geodeticAreaOperator.js";
import geodeticLengthOperator from "@arcgis/core/geometry/operators/geodeticLengthOperator.js";

// Geodesic distance between two points
const distance = geodeticDistanceOperator.execute(point1, point2, {
  unit: "kilometers",
});

// Geodesic area of a polygon
const area = geodeticAreaOperator.execute(polygon, {
  unit: "square-kilometers",
});

// Geodesic length of a polyline
const length = geodeticLengthOperator.execute(polyline, { unit: "kilometers" });


For full operator documentation, see arcgis-geometry-operations.

Migration from Removed Modules
Removed Module (pre-5.0)	Replacement (5.0)
projection.project(geom, sr)	projectOperator.execute(geom, sr)
projection.load()	projectOperator.load()
geodesicUtils.geodesicDistance(p1, p2, unit)	geodeticDistanceOperator.execute(p1, p2, { unit })
geodesicUtils.geodesicArea(geom, unit)	geodeticAreaOperator.execute(geom, { unit })
geodesicUtils.geodesicLength(geom, unit)	geodeticLengthOperator.execute(geom, { unit })
Common Pitfalls

Forgetting to load the projection engine: projectOperator.load() and coordinateFormatter.load() must be called before use:

// Anti-pattern: using before load
const projected = projectOperator.execute(geom, { wkid: 4326 }); // Error

// Correct: load first
await projectOperator.load();
const projected = projectOperator.execute(geom, { wkid: 4326 });


Coordinate order: Geographic coordinates are (longitude, latitude) in the SDK, not (latitude, longitude). Point properties use x = longitude, y = latitude.

WKID vs WKT: Use WKID when a well-known ID exists. Use WKT only for custom coordinate systems not in the WKID registry.

Datum transformations: When projecting between different datums (e.g., NAD83 to WGS84), provide a geographic transformation for accuracy. Without it, results may be off by meters.

Client vs server: Use client-side projection (projectOperator) for speed. Use server-side (geometryService.project()) only for complex transformations the client engine cannot handle.

Using removed modules: The projection and geodesicUtils modules were removed in 5.0. Use projectOperator and geodetic operators instead.

Reference Samples
coordinate-conversion - Converting between coordinate formats
coordinate-conversion-custom - Custom coordinate formats
widgets-coordinateconversion - CoordinateConversion widget usage
widgets-coordinateconversion-custom - Custom coordinate widget formats
client-projection - Client-side projection of geometries
layers-csv-projection - CSV layer with projection
Related Skills
See arcgis-geometry-operations for geometry creation and spatial operators.
See arcgis-rest-services for server-side geometry service (project, buffer, etc.).
See arcgis-core-maps for map and view spatial reference configuration.
Weekly Installs
29
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