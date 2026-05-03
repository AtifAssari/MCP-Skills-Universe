---
title: quarto-authoring
url: https://skills.sh/posit-dev/skills/quarto-authoring
---

# quarto-authoring

skills/posit-dev/skills/quarto-authoring
quarto-authoring
Installation
$ npx skills add https://github.com/posit-dev/skills --skill quarto-authoring
SKILL.md
Quarto Authoring

This skill is based on Quarto CLI v1.9.36 (2026-03-24).

When to Use What

Task: Write a new Quarto document Use: Follow "QMD Essentials" below, then see specific reference files

Task: Add cross-references Use: references/cross-references.md

Task: Configure code cells Use: references/code-cells.md

Task: Add figures with captions Use: references/figures.md

Task: Create tables Use: references/tables.md

Task: Add citations and bibliography Use: references/citations.md

Task: Add callout blocks Use: references/callouts.md

Task: Add diagrams (Mermaid, Graphviz) Use: references/diagrams.md

Task: Control page layout Use: references/layout.md

Task: Use shortcodes Use: references/shortcodes.md

Task: Add conditional content Use: references/conditional-content.md

Task: Use divs and spans Use: references/divs-and-spans.md

Task: Configure YAML front matter Use: references/yaml-front-matter.md

Task: Find and use extensions Use: references/extensions.md

Task: Apply markdown linting rules Use: references/markdown-linting.md

Task: Choose or configure a compute engine (knitr, jupyter, julia) Use: references/engines.md

Migration (only when converting an existing project)

Do NOT read these references when writing new Quarto documents. Only read the one matching the source format when the user explicitly asks to convert or migrate an existing project.

R Markdown (.Rmd) to Quarto: references/conversion-rmarkdown.md
bookdown project: references/conversion-bookdown.md
xaringan slides: references/conversion-xaringan.md
distill article: references/conversion-distill.md
blogdown site: references/conversion-blogdown.md
Jupyter notebook (.ipynb) to/from Quarto: references/conversion-jupyter.md
QMD Essentials
Basic Document Structure
---
title: "Document Title"
author: "Author Name"
date: today
format: html
---

Content goes here.


A Quarto document consists of two main parts:

YAML Front Matter: Metadata and configuration at the top, enclosed by ---.
Markdown Content: Main body using standard markdown syntax.
Divs and Spans

Divs use fenced syntax with three colons:

::: {.class-name}
Content inside the div.
:::


Spans use bracketed syntax:

This is [important text]{.highlight}.


Details: references/divs-and-spans.md

Code Cell Options Syntax

A code cell starts with triple backticks and a language identifier between curly braces. Code cells are code blocks that can be executed to produce output.

Quarto uses the language's comment symbol + | for cell options. Options use dashes, not dots (e.g., fig-cap not fig.cap).

R, Python, Julia: #|
Mermaid: %%|
Graphviz/DOT: //|
```{language}
#| label: fig-example
#| echo: false
#| fig-cap: "A scatter plot example."

# code that produces a figure
```


Set document-level defaults in YAML front matter:

execute:
  echo: false
  warning: false


Caching — critical engine difference: Only suggest #| cache: true for R code cells (knitr engine). Never suggest it for other language cells — it does not work and will be silently ignored. The only correct approach is execute: cache: true in the top-level YAML front matter when using engines other than knitr. Python/Jupyter requires jupyter-cache (pip install jupyter-cache):

execute:
  cache: true


Details: references/code-cells.md

Cross-References

Labels must start with a type prefix. Reference with @:

Figure: fig- prefix, e.g., #| label: fig-plot → @fig-plot
Table: tbl- prefix, e.g., #| label: tbl-data → @tbl-data
Section: sec- prefix, e.g., {#sec-intro} → @sec-intro
Equation: eq- prefix, e.g., {#eq-model} → @eq-model
```{language}
#| label: fig-plot
#| fig-cap: "A caption for the plot."

# code that produces a figure
```

See @fig-plot for the results.


Details: references/cross-references.md

Callout Blocks

Five types: note, warning, important, tip, caution.

::: {.callout-note}
This is a note callout.
:::

::: {.callout-warning}

## Custom Title

This is a warning with a custom title.

:::


Details: references/callouts.md

Figures
![Caption text](image.png){#fig-name fig-alt="Alt text"}


Subfigures:

::: {#fig-group layout-ncol=2}
![Sub caption 1](image1.png){#fig-sub1}

![Sub caption 2](image2.png){#fig-sub2}

Main caption for the group.
:::


Details: references/figures.md

Tables
::: {#tbl-example}

| Column 1 | Column 2 |
| -------- | -------- |
| Data 1   | Data 2   |

Table caption.
:::


Details: references/tables.md

Citations
According to @smith2020, the results show...
Multiple citations [@smith2020; @jones2021].


Configure in YAML:

bibliography: references.bib
csl: apa.csl


Details: references/citations.md

Common Workflows
Creating an HTML Document
title: "My Report"
author: "Your Name"
date: today
format:
  html:
    toc: true
    code-fold: true
    theme: cosmo

Creating a PDF Document
title: "My Report"
format:
  pdf:
    documentclass: article
    papersize: a4

Creating a RevealJS Presentation
---
title: "My Presentation"
format: revealjs
---

## First Slide

Content here.

## Second Slide

More content.

Setting Up a Quarto Project

Create _quarto.yml in the project root:

project:
  type: website

website:
  title: "My Site"
  navbar:
    left:
      - href: index.qmd
        text: Home
      - href: about.qmd
        text: About

format:
  html:
    theme: cosmo

Resources
Quarto Documentation
Quarto Guide
Quarto Extensions
Community Extensions List
Weekly Installs
360
Repository
posit-dev/skills
GitHub Stars
331
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass