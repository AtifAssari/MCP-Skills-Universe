---
title: postgis-dwithin
url: https://skills.sh/mmbmf1/geospatial-skills/postgis-dwithin
---

# postgis-dwithin

skills/mmbmf1/geospatial-skills/postgis-dwithin
postgis-dwithin
Installation
$ npx skills add https://github.com/mmbmf1/geospatial-skills --skill postgis-dwithin
SKILL.md
ST_DWithin (Distance / Proximity Queries)

Use this skill when you need to find features within a given distance of another geometry:

“points within X meters of a line”
proximity searches around a point
replacing expensive buffer + intersects patterns
Core rules
ST_DWithin is faster than ST_Distance < x
Units depend on input type:
geometry → SRID units
geography → meters
Geometries must be in the same SRID
Prefer ST_DWithin over buffering when you only need a boolean test
Canonical patterns
Geometry (projected CRS, SRID units)

Use when your data is stored in a projected SRID (feet/meters).

SELECT *
FROM points p
JOIN lines l
  ON ST_DWithin(p.geom, l.geom, 5);


Distance 5 is in the SRID’s units.

Geography (meters, easiest default)

Use when geometry is stored in EPSG:4326 and you want meters.

SELECT *
FROM points p
JOIN lines l
  ON ST_DWithin(
    p.geom::geography,
    l.geom::geography,
    5
  );


Distance 5 is meters.

Transform once (projected math, better for large jobs)

When using a client/project SRID:

SELECT *
FROM points p
JOIN lines l
  ON ST_DWithin(
    ST_Transform(p.geom, client_srid),
    ST_Transform(l.geom, client_srid),
    5
  );


Transforming both sides is acceptable here because ST_DWithin can still use indexes in many cases, but prefer transforming the smaller side if possible.

Point near line (common validation pattern)
SELECT p.*
FROM points p
JOIN lines l
  ON ST_DWithin(
    p.geom::geography,
    l.geom::geography,
    5
  );


Use this instead of buffering lines unless you need the actual corridor geometry.

Index requirements

Ensure GiST indexes exist:

CREATE INDEX IF NOT EXISTS points_geom_gix ON points USING gist (geom);
CREATE INDEX IF NOT EXISTS lines_geom_gix ON lines USING gist (geom);


ST_DWithin can leverage spatial indexes when used correctly.

Common mistakes
Using ST_Distance(...) < x instead of ST_DWithin
Forgetting geometry vs geography unit differences
Mixing SRIDs without transforming
Buffering geometries just to test proximity
Summary
Prefer ST_DWithin for distance tests
Use geography for meters when in 4326
Use projected SRIDs for heavy planar work
Index geometry columns
Weekly Installs
8
Repository
mmbmf1/geospatial-skills
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass