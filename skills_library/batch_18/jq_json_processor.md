---
title: jq-json-processor
url: https://skills.sh/site/skills.volces.com/jq-json-processor
---

# jq-json-processor

skills/skills.volces.com/jq-json-processor
jq-json-processor
$ npx skills add https://skills.volces.com/skills/clawhub/arnarsson
SKILL.md
jq JSON Processor

Process, filter, and transform JSON data with jq.

Quick Examples
Basic filtering
# Extract a field
echo '{"name":"Alice","age":30}' | jq '.name'
# Output: "Alice"

# Multiple fields
echo '{"name":"Alice","age":30}' | jq '{name: .name, age: .age}'

# Array indexing
echo '[1,2,3,4,5]' | jq '.[2]'
# Output: 3

Working with arrays
# Map over array
echo '[{"name":"Alice"},{"name":"Bob"}]' | jq '.[].name'
# Output: "Alice" "Bob"

# Filter array
echo '[1,2,3,4,5]' | jq 'map(select(. > 2))'
# Output: [3,4,5]

# Length
echo '[1,2,3]' | jq 'length'
# Output: 3

Common operations
# Pretty print JSON
cat file.json | jq '.'

# Compact output
cat file.json | jq -c '.'

# Raw output (no quotes)
echo '{"name":"Alice"}' | jq -r '.name'
# Output: Alice

# Sort keys
echo '{"z":1,"a":2}' | jq -S '.'

Advanced filtering
# Select with conditions
jq '[.[] | select(.age > 25)]' people.json

# Group by
jq 'group_by(.category)' items.json

# Reduce
echo '[1,2,3,4,5]' | jq 'reduce .[] as $item (0; . + $item)'
# Output: 15

Working with files
# Read from file
jq '.users[0].name' users.json

# Multiple files
jq -s '.[0] * .[1]' file1.json file2.json

# Modify and save
jq '.version = "2.0"' package.json > package.json.tmp && mv package.json.tmp package.json

Common Use Cases

Extract specific fields from API response:

curl -s https://api.github.com/users/octocat | jq '{name: .name, repos: .public_repos, followers: .followers}'


Convert CSV-like data:

jq -r '.[] | [.name, .email, .age] | @csv' users.json


Debug API responses:

curl -s https://api.example.com/data | jq '.'

Tips
Use -r for raw string output (removes quotes)
Use -c for compact output (single line)
Use -S to sort object keys
Use --arg name value to pass variables
Pipe multiple jq operations: jq '.a' | jq '.b'
Documentation

Full manual: https://jqlang.github.io/jq/manual/ Interactive tutorial: https://jqplay.org/

Weekly Installs
18
Source
skills.volces.c…rnarsson
First Seen
Mar 13, 2026