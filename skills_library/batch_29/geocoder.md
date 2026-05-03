---
title: geocoder
url: https://skills.sh/dkyazzentwatwa/chatgpt-skills/geocoder
---

# geocoder

skills/dkyazzentwatwa/chatgpt-skills/geocoder
geocoder
Installation
$ npx skills add https://github.com/dkyazzentwatwa/chatgpt-skills --skill geocoder
SKILL.md
Geocoder

Convert between addresses and geographic coordinates.

Features
Geocoding: Address to coordinates
Reverse Geocoding: Coordinates to address
Batch Processing: Process CSV files
Multiple Providers: Nominatim (free), Google, Bing
Address Components: Structured address parsing
Caching: Built-in result caching
Quick Start
from geocoder import Geocoder

geo = Geocoder()

# Address to coordinates
result = geo.geocode("1600 Amphitheatre Parkway, Mountain View, CA")
print(f"Coordinates: {result['lat']}, {result['lon']}")

# Coordinates to address
result = geo.reverse(37.4224, -122.0840)
print(f"Address: {result['address']}")

CLI Usage
# Geocode address
python geocoder.py --geocode "Empire State Building, New York"

# Reverse geocode
python geocoder.py --reverse "40.7484,-73.9857"

# Batch geocode CSV
python geocoder.py --input addresses.csv --column address --output geocoded.csv

# Batch reverse geocode
python geocoder.py --input coords.csv --lat lat --lon lon --reverse-batch --output addresses.csv

API Reference
Geocoder Class
class Geocoder:
    def __init__(self, provider: str = "nominatim", api_key: str = None)

    # Single operations
    def geocode(self, address: str) -> dict
    def reverse(self, lat: float, lon: float) -> dict

    # Batch operations
    def batch_geocode(self, addresses: list, delay: float = 1.0) -> list
    def batch_reverse(self, coordinates: list, delay: float = 1.0) -> list

    # File operations
    def geocode_csv(self, input: str, column: str, output: str) -> str
    def reverse_csv(self, input: str, lat: str, lon: str, output: str) -> str

Providers
Nominatim (Default)
Free, no API key required
Rate limited (1 request/second)
Uses OpenStreetMap data
Google Maps
geo = Geocoder(provider="google", api_key="YOUR_KEY")

Bing Maps
geo = Geocoder(provider="bing", api_key="YOUR_KEY")

Geocoding Result
{
    "address": "1600 Amphitheatre Parkway, Mountain View, CA",
    "lat": 37.4224764,
    "lon": -122.0842499,
    "components": {
        "house_number": "1600",
        "road": "Amphitheatre Parkway",
        "city": "Mountain View",
        "state": "California",
        "postcode": "94043",
        "country": "United States"
    },
    "raw": {...}  # Provider-specific data
}

Reverse Geocoding Result
{
    "lat": 40.7484,
    "lon": -73.9857,
    "address": "20 W 34th St, New York, NY 10001, USA",
    "components": {
        "house_number": "20",
        "road": "West 34th Street",
        "city": "New York",
        "state": "New York",
        "postcode": "10001",
        "country": "United States"
    }
}

Example Workflows
Geocode Customer Addresses
geo = Geocoder()
result = geo.geocode_csv(
    input="customers.csv",
    column="shipping_address",
    output="customers_geocoded.csv"
)
print(f"Geocoded {result['success']} of {result['total']} addresses")

Validate Addresses
geo = Geocoder()
address = "123 Main St, Anytown"

result = geo.geocode(address)
if result:
    print(f"Valid: {result['address']}")
    print(f"Standardized: {result['components']}")
else:
    print("Address not found")

Add Addresses to Coordinates
geo = Geocoder()

locations = [
    (40.7128, -74.0060),
    (34.0522, -118.2437),
    (41.8781, -87.6298)
]

for lat, lon in locations:
    result = geo.reverse(lat, lon)
    print(f"({lat}, {lon}): {result['address']}")

Rate Limiting

Nominatim requires 1 second between requests. The batch functions handle this automatically.

# Automatic delay in batch operations
results = geo.batch_geocode(addresses, delay=1.0)

# For paid providers, can reduce delay
geo = Geocoder(provider="google", api_key="KEY")
results = geo.batch_geocode(addresses, delay=0.1)

Error Handling
result = geo.geocode("Invalid Address XYZ123")
if result is None:
    print("Address not found")
elif result.get('error'):
    print(f"Error: {result['error']}")
else:
    print(f"Found: {result['address']}")

Dependencies
geopy>=2.4.0
pandas>=2.0.0
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
SnykWarn