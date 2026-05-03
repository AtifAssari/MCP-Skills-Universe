---
rating: ⭐⭐⭐
title: pokemon-data-fetcher
url: https://skills.sh/kehwar/experiments/pokemon-data-fetcher
---

# pokemon-data-fetcher

skills/kehwar/experiments/pokemon-data-fetcher
pokemon-data-fetcher
Installation
$ npx skills add https://github.com/kehwar/experiments --skill pokemon-data-fetcher
SKILL.md
Pokemon Data Fetcher
Overview

This skill provides a Python script to fetch Pokemon data from the PokeAPI and organize it into JSON files. The script retrieves all Pokemon names, sorts them by generation, and saves the results in a structured format.

Quick Start

Fetch all Pokemon data organized by generation:

cd pokemon-data-fetcher/scripts
python3 fetch_pokemon.py


This will create JSON files in the current directory containing Pokemon data organized by generation.

Features
1. Fetch All Pokemon

The script fetches all Pokemon from the PokeAPI and organizes them by their generation:

Generation I (Kanto region)
Generation II (Johto region)
Generation III (Hoenn region)
Generation IV (Sinnoh region)
Generation V (Unova region)
Generation VI (Kalos region)
Generation VII (Alola region)
Generation VIII (Galar region)
Generation IX (Paldea region)
2. Sort by Generation

Pokemon are automatically sorted alphabetically within each generation for easy reference.

3. JSON Output

Results are saved in JSON format for easy parsing and integration with other tools:

pokemon_by_generation.json - All Pokemon organized by generation
Clean, readable JSON formatting
Installation
Ensure Python 3.6+ is installed
No external dependencies required - uses Python standard library only

The script uses built-in modules: urllib, json, sys, time

Usage
Basic Usage

Navigate to the scripts directory and run:

cd pokemon-data-fetcher/scripts
python3 fetch_pokemon.py

Script Output

The script will:

Connect to PokeAPI
Fetch all Pokemon species
Organize them by generation
Sort alphabetically within each generation
Save to pokemon_by_generation.json
Output Format
{
  "generation-i": [
    "bulbasaur",
    "charmander",
    "squirtle",
    ...
  ],
  "generation-ii": [
    "chikorita",
    "cyndaquil",
    "totodile",
    ...
  ],
  ...
}

Examples
Example 1: Fetch Pokemon Data
cd pokemon-data-fetcher/scripts
python3 fetch_pokemon.py


Output:

Fetching Pokemon data from PokeAPI...
Fetched 1025 Pokemon species
Organizing by generation...
Results saved to pokemon_by_generation.json

Example 2: Use the Data
import json

# Load the generated data
with open('pokemon_by_generation.json', 'r') as f:
    data = json.load(f)

# Get all Generation I Pokemon
gen1_pokemon = data['generation-i']
print(f"Generation I has {len(gen1_pokemon)} Pokemon")
print(f"First Pokemon: {gen1_pokemon[0]}")

Script Details
fetch_pokemon.py

The main script that handles all Pokemon data fetching:

Functions:

fetch_all_pokemon() - Retrieves all Pokemon species from the API
organize_by_generation() - Groups Pokemon by their generation
save_to_json() - Writes results to a JSON file

API Endpoints Used:

https://pokeapi.co/api/v2/pokemon-species/?limit=10000 - Get all Pokemon species
https://pokeapi.co/api/v2/generation/{id} - Get generation details
Troubleshooting
Issue: Connection Error

Symptoms: Script fails with connection error

Solution: Check your internet connection and verify PokeAPI is accessible:

curl https://pokeapi.co/api/v2/pokemon-species/1


Prevention: The script includes retry logic for temporary network issues

Issue: Missing Dependencies

Symptoms: Script runs successfully without additional installation

Note: This script uses only Python standard library modules (urllib.request, json, sys, time), so no external dependencies need to be installed.

Issue: Permission Denied

Symptoms: Cannot write output file

Solution: Ensure you have write permissions in the current directory:

chmod +w .

Best Practices
Run the script periodically to get updated Pokemon data
Store the JSON output in version control to track changes
Use the data as a reference for Pokemon-related applications
Consider caching the results to avoid repeated API calls
API Information

This skill uses the PokeAPI, a free and open Pokemon API that provides comprehensive Pokemon data.

API Features:

No authentication required
Rate limiting: Fair use policy (no strict limits for reasonable use)
Data includes: Pokemon species, abilities, types, moves, and more
Well-documented and actively maintained

API Limits:

Please be respectful of the free service
Implement caching when making frequent requests
The script is designed to minimize API calls
Reference
PokeAPI Documentation: https://pokeapi.co/docs/v2
PokeAPI GitHub: https://github.com/PokeAPI/pokeapi
Pokemon Generations: https://bulbapedia.bulbagarden.net/wiki/Generation
See Also
For detailed Pokemon data analysis, extend the script with additional API endpoints
Consider using the data for Pokemon team builders, Pokedex apps, or educational tools
Weekly Installs
32
Repository
kehwar/experiments
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass