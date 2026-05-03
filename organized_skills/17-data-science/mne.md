---
rating: ⭐⭐⭐
title: mne
url: https://skills.sh/tondevrel/scientific-agent-skills/mne
---

# mne

skills/tondevrel/scientific-agent-skills/mne
mne
Installation
$ npx skills add https://github.com/tondevrel/scientific-agent-skills --skill mne
SKILL.md
MNE - Neurophysiology Analysis

MNE provides sophisticated tools for filtering brain signals, epoching data, and performing source localization (mapping signals back to brain anatomy).

When to Use
Processing EEG/MEG recordings from clinical or research studies.
Analyzing event-related potentials (ERPs).
Source localization (finding where in the brain signals originate).
Connectivity analysis between brain regions.
Preprocessing neurophysiological data for machine learning.
Core Principles
Raw → Epochs → Evoked

The standard pipeline: continuous raw data → segmented epochs → averaged evoked responses.

Sensor Space vs. Source Space

Sensor space: signals at electrodes. Source space: signals reconstructed at brain locations.

Frequency Analysis

Brain signals are analyzed in frequency bands (delta, theta, alpha, beta, gamma).

Quick Reference
Standard Imports
import mne
import numpy as np

Basic Patterns
# 1. Load data
raw = mne.io.read_raw_fif("sample_audvis_raw.fif")
# Or: raw = mne.io.read_raw_edf("eeg.edf")

# 2. Filter and cleaning
raw.filter(l_freq=1, h_freq=40)  # Bandpass filter
raw.notch_filter(freqs=[50, 100]) # Remove power line noise

# 3. Find events and create Epochs
events = mne.find_events(raw)
epochs = mne.Epochs(raw, events, event_id={'stimulus': 1}, tmin=-0.2, tmax=0.5)
epochs.average().plot() # Plot Evoked potential

# 4. Frequency analysis
epochs.compute_psd().plot()

Critical Rules
✅ DO
Filter before epoching - Apply filters to continuous data, not epochs.
Check data quality - Use raw.plot() to visually inspect for artifacts.
Set montage - Assign electrode positions for proper visualization.
Reject bad epochs - Remove epochs with artifacts before averaging.
❌ DON'T
Don't filter too aggressively - Over-filtering removes signal along with noise.
Don't ignore reference - EEG signals are relative. Know your reference electrode.
Don't mix sampling rates - Ensure all channels have the same sampling rate.
Advanced Patterns
Source Localization
# Compute forward solution and inverse
fwd = mne.make_forward_solution(raw.info, trans, src, bem)
inv = mne.minimum_norm.make_inverse_operator(raw.info, fwd, cov)
stc = mne.minimum_norm.apply_inverse(evoked, inv)
stc.plot()

Connectivity Analysis
from mne.connectivity import spectral_connectivity

# Compute connectivity between channels
con, freqs, times, n_epochs, n_tapers = spectral_connectivity(
    epochs, method='coh', mode='multitaper')


MNE is the gold standard for neurophysiological data analysis, enabling researchers to extract meaningful insights from the complex signals of the human brain.

Weekly Installs
20
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