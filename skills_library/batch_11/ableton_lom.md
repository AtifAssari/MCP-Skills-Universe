---
title: ableton-lom
url: https://skills.sh/mikecfisher/ableton-lom-skill/ableton-lom
---

# ableton-lom

skills/mikecfisher/ableton-lom-skill/ableton-lom
ableton-lom
Installation
$ npx skills add https://github.com/mikecfisher/ableton-lom-skill --skill ableton-lom
SKILL.md
Ableton Live Object Model (LOM) API Reference

This skill provides comprehensive documentation for the Ableton Live Python API used in Remote Scripts. The API is accessed through the _Framework.ControlSurface base class and provides programmatic control over every aspect of a Live Set.

Quick Start
from _Framework.ControlSurface import ControlSurface

class MyScript(ControlSurface):
    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        self._song = self.song()  # Access the Live Set (Song object)
        app = self.application()  # Access the Application object

Core Objects Hierarchy
Application
├── browser (instruments, sounds, drums, audio_effects, midi_effects)
└── Song (live_set)
    ├── tempo, is_playing, loop, metronome
    ├── tracks[] → Track
    │   ├── clip_slots[] → ClipSlot → Clip
    │   ├── devices[] → Device → DeviceParameter
    │   ├── mixer_device → MixerDevice
    │   └── view → Track.View
    ├── return_tracks[] → Track
    ├── master_track → Track
    ├── scenes[] → Scene
    ├── cue_points[] → CuePoint
    ├── groove_pool → GroovePool → Groove
    ├── tuning_system → TuningSystem
    └── view → Song.View

Reference Files by Domain

Load the appropriate reference file based on what you're working with:

Domain	File	Use When
Song & Transport	references/song.md	Working with tempo, playback, time signatures, loops, cue points
Tracks	references/track.md	Creating/modifying tracks, routing, arm/solo/mute, meters
Clips & MIDI	references/clip.md	Creating clips, adding/editing MIDI notes, clip properties, warping
Devices	references/device.md	Loading devices, accessing parameters, device chains
Specialized Devices	references/specialized-devices.md	Simpler, Wavetable, Looper, Compressor, EQ8, Drift, etc.
Rack Devices	references/rack.md	Instrument/Audio/MIDI/Drum Racks, chains, macros, drum pads
Session View	references/session.md	Scenes, clip slots, launching, Session View navigation
Views & UI	references/views.md	Application.View, Song.View, Track.View, Clip.View, Device.View
Browser	references/browser.md	Browsing/loading instruments, effects, samples, presets
Grooves & Tuning	references/grooves-tuning.md	Groove pool, tuning systems
Key Concepts
Property Access Modes
read-only: Can only get the value
read-write: Can get and set the value
observable: Can add listeners with add_<property>_listener(callback)
Threading

All state modifications MUST happen on Ableton's main thread:

def modify_state():
    self._song.tempo = 120.0

self.schedule_message(0, modify_state)  # Schedule for main thread

Canonical Paths

Objects are accessed via paths like live_set tracks 0 devices 1 parameters 2. Use these to understand the object hierarchy.

Common Patterns

Iterate tracks and clips:

for track in self._song.tracks:
    for slot in track.clip_slots:
        if slot.has_clip:
            clip = slot.clip
            # Work with clip


Add a listener:

def on_tempo_changed():
    self.log_message("Tempo: " + str(self._song.tempo))

self._song.add_tempo_listener(on_tempo_changed)


Access device parameters:

device = track.devices[0]
for param in device.parameters:
    self.log_message(param.name + ": " + str(param.value))

Version Compatibility

This documentation covers Live 12.3. Key version notes:

Live 11+: Python 3 required
Live 11.0+: GroovePool, Groove classes added
Live 12.3+: insert_device(), insert_chain(), AB Compare features added
Important Notes
The API is officially undocumented by Ableton - this reference is based on community documentation from Cycling '74's Max for Live LOM reference
Always test Remote Scripts with a backup of your Live Set
Some operations may cause crashes if called from wrong thread
Observable properties can be used to build reactive UIs
Weekly Installs
62
Repository
mikecfisher/abl…om-skill
GitHub Stars
6
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass