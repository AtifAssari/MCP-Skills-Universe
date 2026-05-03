---
title: pydicom
url: https://skills.sh/tondevrel/scientific-agent-skills/pydicom
---

# pydicom

skills/tondevrel/scientific-agent-skills/pydicom
pydicom
Installation
$ npx skills add https://github.com/tondevrel/scientific-agent-skills --skill pydicom
SKILL.md
Pydicom - Medical Imaging Standards

DICOM is more than an image; it's a rich data structure containing patient info, spatial orientation, and pixel data. Pydicom provides access to all these tags.

When to Use
Processing medical imaging data (CT, MRI, X-ray, ultrasound).
Extracting patient metadata and clinical information from DICOM files.
Building AI models for radiology that require both image and metadata.
Converting DICOM to other formats for analysis.
Quality assurance and compliance checking in medical imaging workflows.
Core Principles
Datasets as Dicts

Access tags by name (e.g., ds.PatientName) or ID (ds[0x0010, 0x0010]).

Pixel Data

Raw pixel data is stored in PixelData, but should be accessed via pixel_array for NumPy integration.

VR (Value Representation)

Strict typing for dates, ages, and decimals ensures data integrity.

Quick Reference
Standard Imports
import pydicom
from pydicom.data import get_testdata_files
import matplotlib.pyplot as plt
import numpy as np

Basic Patterns
# 1. Read file
ds = pydicom.dcmread("scan.dcm")

# 2. Access Metadata
print(f"Patient: {ds.PatientName}, ID: {ds.PatientID}")
print(f"Modality: {ds.Modality}") # CT, MR, DX
print(f"Study Date: {ds.StudyDate}")
print(f"Slice Thickness: {ds.SliceThickness}")

# 3. Access Image
plt.imshow(ds.pixel_array, cmap="gray")
plt.title(f"{ds.Modality} - {ds.PatientName}")

Critical Rules
✅ DO
Use pixel_array property - Always access pixel data via ds.pixel_array rather than ds.PixelData for proper NumPy integration.
Check for missing tags - Use hasattr(ds, 'TagName') before accessing optional tags.
Respect patient privacy - DICOM files contain PHI (Protected Health Information). Always anonymize before sharing.
Handle different photometric interpretations - Some images may be inverted or use different color spaces.
❌ DON'T
Don't modify DICOM files in place - Always create a copy when modifying to preserve original data.
Don't ignore VR types - DICOM has strict data types. Converting incorrectly can corrupt data.
Don't assume all DICOM files have images - Some contain only metadata (structured reports).
Advanced Patterns
Working with DICOM Series
import pydicom
from pathlib import Path

# Load a series of DICOM files
dicom_dir = Path("dicom_series")
files = sorted(dicom_dir.glob("*.dcm"))

# Load and stack slices
slices = [pydicom.dcmread(f) for f in files]
volume = np.stack([s.pixel_array for s in slices])

Anonymization
# Remove patient identifiers
ds.PatientName = "ANONYMOUS"
ds.PatientID = "000000"
ds.PatientBirthDate = ""
ds.PatientSex = ""


Pydicom is the foundation of medical imaging in Python, enabling researchers and clinicians to work with the rich, standardized DICOM format that powers modern radiology.

Weekly Installs
16
Repository
tondevrel/scien…t-skills
GitHub Stars
9
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass