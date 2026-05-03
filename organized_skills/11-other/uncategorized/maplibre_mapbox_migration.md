---
rating: ⭐⭐
title: maplibre-mapbox-migration
url: https://skills.sh/maplibre/maplibre-agent-skills/maplibre-mapbox-migration
---

# maplibre-mapbox-migration

skills/maplibre/maplibre-agent-skills/maplibre-mapbox-migration
maplibre-mapbox-migration
Installation
$ npx skills add https://github.com/maplibre/maplibre-agent-skills --skill maplibre-mapbox-migration
SKILL.md
Mapbox to MapLibre Migration

This skill guides you through migrating an application from Mapbox GL JS to MapLibre GL JS. The two libraries share a common ancestry (MapLibre forked from Mapbox GL JS v1.13 in December 2020), so the API is largely the same. The main changes are: swap the package, replace the namespace, remove the Mapbox access token, and choose a new tile source (MapLibre does not use mapbox:// styles).

Primary reference: MapLibre official Mapbox migration guide.

When to Use This Skill
Migrating an existing Mapbox GL JS app to MapLibre
Evaluating MapLibre as an open-source alternative to Mapbox
Understanding API compatibility and what breaks
Choosing tile sources and services after moving off Mapbox
Why Migrate to MapLibre?

Common reasons teams switch from Mapbox to MapLibre:

Open-source license — MapLibre is BSD-3-Clause; no vendor lock-in or proprietary terms
No access token — The library does not require a Mapbox token; tile sources may have their own keys or none (e.g. OpenFreeMap)
Cost — Avoid Mapbox map-load and API pricing; use free or fixed-cost tile and geocoding providers
Self-hosting — Use your own tiles (PMTiles, tileserver-gl, Martin) or any third-party source
Community — MapLibre is maintained by the MapLibre organization and community; style spec and APIs evolve in the open
Community-supported funding — MapLibre is funded by donations from many companies and individuals; there is no single commercial backer, so the project stays aligned with the community
Open vector tile format (MLT) — MapLibre offers MapLibre Tile (MLT), a modern alternative to Mapbox Vector Tiles (MVT) with better compression and support for 3D coordinates and elevation; supported in GL JS and Native, and can be generated with Planetiler

What you give up: Mapbox Studio integration, Mapbox-hosted tiles and styles, Mapbox Search/Directions/Geocoding APIs, official Mapbox support.

Understanding the Fork
Dec 2020: Mapbox GL JS v2.0 switched to a proprietary license. The community forked v1.13 as MapLibre GL JS. MapLibre organization and GL JS repo are the canonical homes.
API: MapLibre GL JS v1.x is largely backward compatible with Mapbox GL JS v1.x. Most map code (methods, events, layers, sources) works with minimal changes.
Releases since the fork: MapLibre has moved ahead with its own version line. v2/v3 brought WebGL2, a modern renderer, and features like hillshade and terrain; v4 introduced Promises in public APIs (replacing many callbacks); v5 added globe view and the Adaptive Composite Map Projection. See releases and CHANGELOG.
Style spec: MapLibre maintains its own MapLibre Style Specification (forked from the Mapbox spec). It is compatible for most styles but has added and diverged in places; check the style spec site when using newer or MapLibre-specific features.
Ecosystem: Besides GL JS, the MapLibre org hosts MapLibre Native (iOS, Android, desktop), Martin (vector tile server from PostGIS/PMTiles/MBTiles), and the MapLibre Tile (MLT) format. Roadmaps and news: maplibre.org/roadmap, maplibre.org/news.
Step-by-Step Migration
1. Install the Package
npm install maplibre-gl

2. Update Imports and CSS
// Before (Mapbox)
import mapboxgl from 'mapbox-gl';
import 'mapbox-gl/dist/mapbox-gl.css';

// After (MapLibre)
import maplibregl from 'maplibre-gl';
import 'maplibre-gl/dist/maplibre-gl.css';


CDN: Replace Mapbox script/link with MapLibre:

Script: https://api.mapbox.com/mapbox-gl-js/v*.*.*/mapbox-gl.js → https://unpkg.com/maplibre-gl@*.*.*/dist/maplibre-gl.js
CSS: same pattern (mapbox-gl.css → maplibre-gl.css).
3. Replace the Namespace

Replace all mapboxgl with maplibregl (and mapbox-gl with maplibre-gl in package names or paths). Examples:

// Before (Mapbox)
const map = new mapboxgl.Map({ ... });
new mapboxgl.Marker().setLngLat([lng, lat]).addTo(map);
map.addControl(new mapboxgl.NavigationControl());

// After (MapLibre)
const map = new maplibregl.Map({ ... });
new maplibregl.Marker().setLngLat([lng, lat]).addTo(map);
map.addControl(new maplibregl.NavigationControl());


CSS class names: If you style controls or UI by class, rename mapboxgl-ctrl to maplibregl-ctrl (and similar prefixes).

4. Remove the Access Token

MapLibre does not use mapboxgl.accessToken. Remove any line that sets it.

Tile and API keys (e.g. for hosted tile services or geocoding) are configured per service, not on the map instance. See maplibre-tile-sources for providers that need a key.

5. Replace the Style URL (Critical)

Mapbox styles (mapbox://styles/...) will not work in MapLibre. You must point the map to a style that uses non-Mapbox tile sources, sprites, and glyphs.

The simplest option is to use a style URL that does not require an API key, like OpenFreeMap. OpenFreeMap is community-funded and free to use with no API key; if your app depends on it in production, consider donating to support the project. Once you have tested and verified your migration works, you can explore the many available options (see awesome-maplibre or MapLibre Tile Sources for further suggestions).

Example:

// Before (Mapbox)
const map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/mapbox/streets-v12',
  center: [-122.42, 37.78],
  zoom: 12
});

// After (MapLibre)
const map = new maplibregl.Map({
  container: 'map',
  style: 'https://tiles.openfreemap.org/styles/liberty', // or your chosen style
  center: [-122.42, 37.78],
  zoom: 12
});


From there, you can install the MapLibre Style Specification & Utilities to validate and debug styles:

npm install @maplibre/maplibre-style-spec


Custom Mapbox styles: If you designed a style in Mapbox Studio, you cannot load it directly in MapLibre. Export the style JSON and replace Mapbox source URLs with URLs for your chosen tile source. Your styles will not render unless and until you adjust all references to the Mapbox tile schema to match the tile schema of your new tile source. In addition to updating source URLs, this means adapting the id, source, and source-layer properties in your style JSON to match the new source and layer names.

Most properties in Mapbox styles are compatible with MapLibre. Check the MapLibre Style Specification for details on supported properties and types. You can use Maputnik, MapLibre's style editor, to visually test and debug your style JSON, and MapLibre Style Spec CLI Tools to check for compatibility and other validation issues.

gl-style-validate style.json

6. Update Plugins (If Used)

Many Mapbox plugins work with MapLibre unchanged, and many have been forked or replaced with MapLibre-native versions. Where a MapLibre-native alternative exists, prefer it for long-term compatibility.

Check the User Interface Plugins, Geocoding & Search Plugins, and Map Rendering Plugins sections of awesome-maplibre to find compatible plugins and alternatives.

7. Replace Mapbox APIs (Search, Directions, etc.)

If your app calls Mapbox Geocoding, Directions, or other REST APIs, replace them with open or third-party services:

Geocoding / search: Nominatim, Photon, Pelias, or MapTiler Geocoding
Directions / routing: OSRM, OpenRouteService, Valhalla

Usage policies and sustainability: These are open or community-funded services with terms that matter in production:

Nominatim — Requires OpenStreetMap attribution; the public instance is for testing and low-volume use only. See the Nominatim usage policy. For production workloads, self-host or use a managed provider (e.g. MapTiler Geocoding).
OSRM demo server (router.project-osrm.org) — Explicitly not for production; no SLA or uptime guarantee. Self-host or use a managed service (e.g. OpenRouteService, MapTiler Directions) for production apps.
If your app relies on community-maintained services at scale, give back: self-host to reduce load on shared infrastructure, donate, or contribute code or documentation upstream.

Update your code to use the new endpoints and response formats; the map layer and interaction code (e.g. adding a route line) stays the same with MapLibre.

8. What Stays the Same

Most of your map code does not change:

Map methods: setCenter, setZoom, fitBounds, flyTo, getBounds, etc.
Events: map.on('load'), map.on('click', layerId, callback), etc.
Markers, popups, controls (Navigation, Geolocate, Fullscreen, Scale)
Sources and layers: addSource, addLayer, setPaintProperty, setFilter
GeoJSON and expressions in the style spec

So after swapping the package, namespace, token, and style (and any plugins/APIs), the rest of your logic can stay as is.

Checklist
 Uninstall mapbox-gl, install maplibre-gl
 Replace imports and CSS (mapbox-gl → maplibre-gl)
 Replace all mapboxgl with maplibregl (and CSS classes mapboxgl- → maplibregl-)
 Remove mapboxgl.accessToken
 Set style to a non-Mapbox URL (hosted or your own style)
 Replace incompatible Mapbox plugins with MapLibre or open alternatives
 Replace Mapbox Geocoding/Directions with Nominatim, OSRM, or other open alternatives
 Test map load, controls, and any API-driven features
Related Skills
maplibre-tile-sources — Choosing and configuring tile sources (OpenFreeMap, MapTiler, PMTiles, self-hosted)
maplibre-pmtiles-patterns — Serverless tiles with PMTiles
Sources Used for This Skill

These sources were used when creating this skill. You may want to involve contributors who maintain or have contributed to them:

MapLibre official migration guide — maplibre.org/maplibre-gl-js/docs/guides/mapbox-migration-guide/ — Primary step-by-step reference (package, namespace, CSS, CDN).
MapLibre GL JS documentation — maplibre.org/maplibre-gl-js/docs/ — API and concepts.
MapLibre GL JS GitHub — github.com/maplibre/maplibre-gl-js — README, releases, and fork history.
mapbox-agent-skills — The mapbox-maplibre-migration skill (Mapbox repo) covers the reverse direction (MapLibre → Mapbox). Topic structure and comparison elements were adapted for this Mapbox → MapLibre skill. Copyright (c) Mapbox, Inc. for adapted portions.
This repo’s skills — maplibre-tile-sources, maplibre-pmtiles-patterns; maplibre-open-search-patterns and maplibre-geospatial-operations not yet in repo — for tile source and service alternatives after migration.
Weekly Installs
90
Repository
maplibre/maplib…t-skills
GitHub Stars
107
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass