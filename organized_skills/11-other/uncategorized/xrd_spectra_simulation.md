---
rating: ⭐⭐
title: xrd-spectra-simulation
url: https://skills.sh/internscience/chemclaw/xrd-spectra-simulation
---

# xrd-spectra-simulation

skills/internscience/chemclaw/xrd-spectra-simulation
xrd-spectra-simulation
Installation
$ npx skills add https://github.com/internscience/chemclaw --skill xrd-spectra-simulation
SKILL.md
XRD Spectrum Simulation Skill
When to use this

Use this skill when the user provides a .cif structure file and wants:

Simulated XRD pattern (Cu Kα by default)
Publication-ready PNG plot
Inputs
.cif file path (user provides crystal structure)
Outputs
/tmp/chemclaw/xrd_spectrum.png — XRD pattern plot
New environment (from zero)
conda create -n spec python=3.12 -y
conda activate spec
cd xrd-spectra-simulation
pip install -r requirements.txt

python xrd_spectra_simulation.py example/1100157.cif

仓库内附范例 example/1100157.cif 可直接测试。
How to use
cd xrd-spectra-simulation
python xrd_spectra_simulation.py example/1100157.cif
python xrd_spectra_simulation.py path/to/structure.cif --output /tmp/chemclaw/my_xrd.png

Optional
cd xrd-spectra-simulation
python xrd_spectra_simulation.py structure.cif --wavelength MoKa

Dependencies (requirements.txt)
pymatgen
matplotlib
Notes
Uses pymatgen XRDCalculator
Default: Cu Kα radiation
Available: CuKa, MoKa, CrKa, FeKa, CoKa, AgKa, etc.
Weekly Installs
9
Repository
internscience/chemclaw
GitHub Stars
44
First Seen
Mar 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass