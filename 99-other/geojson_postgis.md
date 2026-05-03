---
title: geojson-postgis
url: https://skills.sh/mmbmf1/geospatial-skills/geojson-postgis
---

# geojson-postgis

skills/mmbmf1/geospatial-skills/geojson-postgis
geojson-postgis
Installation
$ npx skills add https://github.com/mmbmf1/geospatial-skills --skill geojson-postgis
SKILL.md
PostGIS Geometry Rows → GeoJSON FeatureCollection

Use this skill when your data already has a PostGIS geometry column (typically geom) and you need to serve it to a web map as GeoJSON.

This is the canonical pattern:

output WGS84 (EPSG:4326) for clients
return a FeatureCollection
keep properties as “all columns minus geom” (or explicitly selected fields)
When to use
You have a table with geom (geometry) and other columns
You are building or updating an API endpoint that returns map layers
You want consistent GeoJSON structure and coordinate system
Core rules
Serve geometry in EPSG:4326 for web clients
GeoJSON output should be a FeatureCollection
Properties should not include raw geom (remove it or select explicitly)
Canonical SQL pattern (FeatureCollection)
SELECT jsonb_build_object(
  'type', 'FeatureCollection',
  'features', COALESCE(jsonb_agg(
    jsonb_build_object(
      'type', 'Feature',
      'geometry', ST_AsGeoJSON(ST_Transform(t.geom, 4326))::jsonb,
      'properties', (to_jsonb(t) - 'geom')
    )
  ), '[]'::jsonb)
) AS geojson
FROM my_table t
WHERE t.geom IS NOT NULL;

Notes
COALESCE(..., '[]') ensures empty results return "features": [] (not null)
ST_Transform(..., 4326) ensures map-safe coordinates
to_jsonb(t) - 'geom' keeps properties clean
Selecting only certain properties (recommended for payload size)

If a table has many columns, explicitly build properties:

SELECT jsonb_build_object(
  'type', 'FeatureCollection',
  'features', COALESCE(jsonb_agg(
    jsonb_build_object(
      'type', 'Feature',
      'geometry', ST_AsGeoJSON(ST_Transform(t.geom, 4326))::jsonb,
      'properties', jsonb_build_object(
        'id', t.id,
        'name', t.name,
        'status', t.status
      )
    )
  ), '[]'::jsonb)
) AS geojson
FROM my_table t
WHERE t.geom IS NOT NULL;

Returning one feature by id

Use this pattern for a single geometry row:

SELECT jsonb_build_object(
  'type', 'Feature',
  'geometry', ST_AsGeoJSON(ST_Transform(t.geom, 4326))::jsonb,
  'properties', (to_jsonb(t) - 'geom')
) AS feature
FROM my_table t
WHERE t.id = $1
  AND t.geom IS NOT NULL;

Guardrails for map endpoints
Always require filtering (bbox, ids, or a sensible limit) for large tables
Consider enforcing a maximum feature count
Prefer explicit properties for large payloads
If you frequently serve this layer, consider simplifying geometry upstream (separate skill)
Common mistakes
Serving geometry in a projected SRID (client renders nonsense)
Returning raw geom in properties
Forgetting COALESCE and returning "features": null
Returning too many features (browser crash / huge payload)
Weekly Installs
19
Repository
mmbmf1/geospatial-skills
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass