---
rating: ⭐⭐
title: geojson-points
url: https://skills.sh/mmbmf1/geospatial-skills/geojson-points
---

# geojson-points

skills/mmbmf1/geospatial-skills/geojson-points
geojson-points
Installation
$ npx skills add https://github.com/mmbmf1/geospatial-skills --skill geojson-points
SKILL.md
Points → GeoJSON (PostGIS)

Use this skill when you have tabular data (rows or JSON) that include latitude/longitude fields and you need a GeoJSON FeatureCollection for map display.

This skill documents the canonical raw SQL pattern for building GeoJSON from point data in PostGIS.

When to use
You have rows like { id, lat, lng, ... }
You want GeoJSON directly from Postgres
You want predictable geometry and property handling
Input assumptions
Latitude and longitude are stored as numeric or castable to numeric
Longitude comes first in point construction
Geometry is output in WGS84 (EPSG:4326)
Canonical SQL pattern
From JSON input

Use when your API passes rows as a JSON array.

WITH data_rows AS (
  SELECT jsonb_array_elements($1::jsonb) AS row_data
)
SELECT jsonb_build_object(
  'type', 'FeatureCollection',
  'features', jsonb_agg(
    jsonb_build_object(
      'type', 'Feature',
      'geometry', ST_AsGeoJSON(
        ST_Point(
          (row_data->>'lng')::float,
          (row_data->>'lat')::float
        )
      )::jsonb,
      'properties', row_data - 'lat' - 'lng'
    )
  )
)
FROM data_rows;

From a table

Use when latitude/longitude are stored in columns.

SELECT jsonb_build_object(
  'type', 'FeatureCollection',
  'features', jsonb_agg(
    jsonb_build_object(
      'type', 'Feature',
      'geometry', ST_AsGeoJSON(
        ST_Point(lng, lat)
      )::jsonb,
      'properties', to_jsonb(t) - 'lat' - 'lng'
    )
  )
)
FROM my_table t;

Coordinate rules (critical)
GeoJSON coordinates are [longitude, latitude]
Latitude range: -90..90
Longitude range: -180..180

Most incorrect maps come from swapped coordinates.

Output shape
type: "FeatureCollection"
features: array of GeoJSON Feature objects
Each feature has:
geometry.type = "Point"
geometry.coordinates = [lng, lat]
properties = remaining fields
Implementation notes
Use ST_Point(lng, lat) (not ST_MakePoint(lat, lng))
ST_AsGeoJSON(... )::jsonb avoids string parsing downstream
Removing coord fields keeps properties clean and map-safe
Guardrails
Filter rows with missing or invalid coordinates before conversion
Enforce feature limits for browser safety
Explicitly select properties if payload size matters
Weekly Installs
16
Repository
mmbmf1/geospatial-skills
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass