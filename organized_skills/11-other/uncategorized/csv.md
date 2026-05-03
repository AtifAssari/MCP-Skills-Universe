---
rating: ⭐⭐⭐
title: csv
url: https://skills.sh/vercel-labs/bash-tool/csv
---

# csv

skills/vercel-labs/bash-tool/csv
csv
Installation
$ npx skills add https://github.com/vercel-labs/bash-tool --skill csv
SKILL.md
CSV Processing Skill

Process CSV files using standard bash tools (awk, cut, sort, grep).

Available Scripts
analyze.sh

Get statistics and summary of a CSV file.

bash /skills/csv/scripts/analyze.sh data.csv

filter.sh

Filter rows where a column matches a value.

bash /skills/csv/scripts/filter.sh data.csv <column_number> <value>

select.sh

Select specific columns from CSV.

bash /skills/csv/scripts/select.sh data.csv <col1,col2,col3>

sort.sh

Sort CSV by a column.

bash /skills/csv/scripts/sort.sh data.csv <column_number> [--numeric] [--reverse]

Examples
# Show CSV summary
bash /skills/csv/scripts/analyze.sh sales.csv

# Filter where column 3 equals "active"
bash /skills/csv/scripts/filter.sh users.csv 3 active

# Select columns 1, 2, and 4
bash /skills/csv/scripts/select.sh data.csv 1,2,4

# Sort by column 2 numerically in reverse
bash /skills/csv/scripts/sort.sh data.csv 2 --numeric --reverse

Weekly Installs
62
Repository
vercel-labs/bash-tool
GitHub Stars
548
First Seen
Mar 10, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass