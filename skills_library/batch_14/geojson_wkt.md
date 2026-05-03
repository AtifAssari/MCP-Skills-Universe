---
title: geojson-wkt
url: https://skills.sh/mmbmf1/geospatial-skills/geojson-wkt
---

# geojson-wkt

skills/mmbmf1/geospatial-skills/geojson-wkt
geojson-wkt
Installation
$ npx skills add https://github.com/mmbmf1/geospatial-skills --skill geojson-wkt
SKILL.md
WKT → GeoJSON (PostGIS)

Use this skill when your data includes geometries as WKT strings (e.g., "POINT(-87.6 41.8)", "LINESTRING(...)", "POLYGON(...)") and you want a GeoJSON FeatureCollection for map display.

This skill documents the canonical raw SQL pattern for building GeoJSON from WKT using PostGIS.

When to use
You receive an array of objects like { id, wkt, ... }
You want GeoJSON directly from Postgres
You want consistent property shaping and GeoJSON output
Input assumptions
WKT is valid (or you’ll get PostGIS parse errors)
The WKT may or may not include an SRID (this pattern assumes no SRID unless you add it)
Output should be web-map friendly (commonly EPSG:4326)
Canonical SQL pattern
From JSON input (WKT field)

Use when your API passes rows as a JSON array, and one field contains WKT.

WITH data_rows AS (
  SELECT jsonb_array_elements($1::jsonb) AS row_data
)
SELECT jsonb_build_object(
  'type', 'FeatureCollection',
  'features', jsonb_agg(
    jsonb_build_object(
      'type', 'Feature',
      'geometry', ST_AsGeoJSON(
        ST_GeomFromText(row_data->>'wkt')
      )::jsonb,
      'properties', row_data - 'wkt'
    )
  )
)
FROM data_rows;

From a table (WKT column)

Use when WKT is stored in a column.

SELECT jsonb_build_object(
  'type', 'FeatureCollection',
  'features', jsonb_agg(
    jsonb_build_object(
      'type', 'Feature',
      'geometry', ST_AsGeoJSON(
        ST_GeomFromText(t.wkt)
      )::jsonb,
      'properties', to_jsonb(t) - 'wkt'
    )
  )
)
FROM my_table t;

Handling SRID (recommended)

If your WKT is intended to be EPSG:4326, set it explicitly:

ST_SetSRID(ST_GeomFromText(row_data->>'wkt'), 4326)


If you need to transform to 4326 for web clients:

ST_AsGeoJSON(ST_Transform(
  ST_SetSRID(ST_GeomFromText(row_data->>'wkt'), <source_srid>),
  4326
))::jsonb

Example input
[
  { "id": 1, "name": "A", "wkt": "POINT(-87.6298 41.8781)", "status": "active" },
  { "id": 2, "name": "B", "wkt": "POINT(-95.3698 29.7604)", "status": "inactive" }
]

Example output (shape)
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-87.6298, 41.8781]
      },
      "properties": {
        "id": 1,
        "name": "A",
        "status": "active"
      }
    }
  ]
}

Implementation notes
Parse WKT with ST_GeomFromText(...)
Serialize with ST_AsGeoJSON(...)::jsonb
Properties are computed by removing the WKT field:
row_data - '<wkt_field>'
Guardrails
Validate/clean WKT upstream when possible (invalid WKT will error)
Enforce feature limits for browser safety
Prefer explicit SRID assignment (ST_SetSRID) when SRID is known
Weekly Installs
13
Repository
mmbmf1/geospatial-skills
First Seen
Feb 9, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass