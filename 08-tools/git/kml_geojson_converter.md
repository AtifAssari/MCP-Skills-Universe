---
title: kml-geojson-converter
url: https://skills.sh/dkyazzentwatwa/chatgpt-skills/kml-geojson-converter
---

# kml-geojson-converter

skills/dkyazzentwatwa/chatgpt-skills/kml-geojson-converter
kml-geojson-converter
Installation
$ npx skills add https://github.com/dkyazzentwatwa/chatgpt-skills --skill kml-geojson-converter
SKILL.md
KML/GeoJSON Converter

Convert geographic data between KML, GeoJSON, and other geo formats for mapping and GIS applications.

Purpose

Geo format conversion for:

Google Maps / Earth integration
Web mapping applications (Leaflet, Mapbox)
GIS data interchange
Spatial data processing
GPS track conversion
Features
Bidirectional Conversion: KML ↔ GeoJSON
Feature Preservation: Maintain properties, styles, descriptions
Batch Processing: Convert multiple files
Coordinate Systems: WGS84, UTM support
Validation: Verify output format validity
Simplification: Reduce polygon complexity
Quick Start
from kml_geojson_converter import GeoConverter

# KML to GeoJSON
converter = GeoConverter()
converter.load_kml('input.kml')
converter.save_geojson('output.geojson')

# GeoJSON to KML
converter.load_geojson('input.geojson')
converter.save_kml('output.kml')

CLI Usage
# Convert KML to GeoJSON
python kml_geojson_converter.py input.kml --to geojson --output output.geojson

# Convert GeoJSON to KML
python kml_geojson_converter.py input.geojson --to kml --output output.kml

Weekly Installs
65
Repository
dkyazzentwatwa/…t-skills
GitHub Stars
53
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass