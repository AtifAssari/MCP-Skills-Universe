---
title: chartli
url: https://skills.sh/ahmadawais/chartli/chartli
---

# chartli

skills/ahmadawais/chartli/chartli
chartli
Installation
$ npx skills add https://github.com/ahmadawais/chartli --skill chartli
SKILL.md
chartli Skill

Use this skill when an agent needs to visualize numeric data in the terminal as ASCII/Unicode/SVG charts.

Install
npx skills add ahmadawais/chartli

CLI install/use

Instant use:

npx chartli --help


Global install:

npm i -g chartli

What chartli can do
Render chart types: ascii, spark, bars, columns, heatmap, unicode, braille, svg
Read from file path input
Read from stdin when no file is passed
Control output dimensions with --width and --height
Render SVG with --mode circles|lines
Add x and y axis titles with --x-axis-label and --y-axis-label
Add custom tick/category labels with --x-labels and --series-labels
Show raw values on the plotted data with --data-labels
Promote the first numeric column into x-axis labels with --first-column-x
Command templates

From file:

npx chartli <file> -t <type> [--width N] [--height N] [--mode circles|lines] [--x-axis-label LABEL] [--y-axis-label LABEL] [--x-labels a,b,c] [--series-labels foo,bar] [--data-labels] [--first-column-x]


From stdin:

printf 'x y\n1 10\n2 20\n3 15\n' | npx chartli -t ascii -w 24 -h 8


Labeled two-column chart:

printf 'day value\n1 10\n2 20\n3 15\n' | npx chartli -t ascii -w 24 -h 8 --first-column-x --data-labels


Per-type examples:

npx chartli data.txt -t ascii -w 24 -h 8
npx chartli data.txt -t spark
npx chartli data.txt -t bars -w 28
npx chartli data.txt -t columns -h 8
npx chartli data.txt -t heatmap
npx chartli data.txt -t unicode
npx chartli data.txt -t braille -w 16 -h 6
npx chartli data.txt -t svg -m lines -w 320 -h 120

Input format

Whitespace-separated numeric rows; optional header row is allowed.

day sales costs profit
1 10 8 2
2 14 9 5
3 12 11 3


When --first-column-x is set, the first numeric column becomes the x-axis labels. If a header row exists, chartli uses the first header cell as the x-axis title and the remaining headers as series labels. For common two-column input, the second header cell becomes the y-axis title.

Repository example assets
examples/assets/core-single-series.txt
examples/assets/core-multi-series.txt
examples/assets/image-data.txt
examples/assets/image-columns-variant.txt
Weekly Installs
111
Repository
ahmadawais/chartli
GitHub Stars
657
First Seen
Mar 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn