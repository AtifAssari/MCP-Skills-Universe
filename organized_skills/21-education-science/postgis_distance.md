---
rating: ⭐⭐
title: postgis-distance
url: https://skills.sh/mmbmf1/geospatial-skills/postgis-distance
---

# postgis-distance

skills/mmbmf1/geospatial-skills/postgis-distance
postgis-distance
Installation
$ npx skills add https://github.com/mmbmf1/geospatial-skills --skill postgis-distance
SKILL.md
ST_Distance (Numeric Distance)

Use this skill when you need the numeric distance value between geometries (for reporting, ranking display, metadata).

If you need a boolean “within X distance” filter, prefer ST_DWithin (faster). A common pattern is:

use ST_DWithin to filter candidates
use ST_Distance to compute the returned distance value
Core rules
Units depend on type:
geometry → SRID units (degrees/meters/feet depending on SRID)
geography → meters
Geometries must be in the same SRID for geometry math
Do not compute meaningful distances in EPSG:4326 geometry (degrees) unless you intend degrees
Canonical patterns
Distance in meters (recommended): geography

Works well when data is stored in EPSG:4326 and you want meters.

SELECT
  ST_Distance(a.geom::geography, b.geom::geography) AS distance_m
FROM a
JOIN b ON ...;

Distance in projected SRID units: geometry

Use a projected/client SRID where units are meaningful (feet/meters).

SELECT
  ST_Distance(
    ST_Transform(a.geom, client_srid),
    ST_Transform(b.geom, client_srid)
  ) AS distance_units
FROM a
JOIN b ON ...;

Fast filter + distance output (recommended pattern)

Filter candidates with ST_DWithin, then compute distance.

WITH p AS (
  SELECT ST_SetSRID(ST_MakePoint($1, $2), 4326) AS geom
)
SELECT
  f.*,
  ST_Distance(f.geom::geography, p.geom::geography) AS distance_m
FROM features f, p
WHERE ST_DWithin(f.geom::geography, p.geom::geography, 5000)  -- 5km
ORDER BY f.geom <-> p.geom
LIMIT 50;


This is a common “map / nearby” endpoint pattern:

ST_DWithin constrains work
<-> ranks quickly
ST_Distance provides the numeric value
Common mistakes
Using ST_Distance(geom, geom) on EPSG:4326 geometry and assuming meters
Using ST_Distance(...) < x in WHERE instead of ST_DWithin(...)
Mixing SRIDs without transforming
Computing distances on huge tables without bounding the search
Summary
Use geography for meters
Use projected SRIDs for planar geometry distances
Use ST_DWithin for filtering, ST_Distance for reporting
Weekly Installs
9
Repository
mmbmf1/geospatial-skills
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass