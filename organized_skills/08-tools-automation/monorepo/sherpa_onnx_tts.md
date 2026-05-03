---
rating: ⭐⭐
title: sherpa-onnx-tts
url: https://skills.sh/steipete/clawdis/sherpa-onnx-tts
---

# sherpa-onnx-tts

skills/steipete/clawdis/sherpa-onnx-tts
sherpa-onnx-tts
Installation
$ npx skills add https://github.com/steipete/clawdis --skill sherpa-onnx-tts
SKILL.md
sherpa-onnx-tts

Local TTS using the sherpa-onnx offline CLI.

Install
Download the runtime for your OS (extracts into $OPENCLAW_STATE_DIR/tools/sherpa-onnx-tts/runtime, default ~/.openclaw/tools/sherpa-onnx-tts/runtime)
Download a voice model (extracts into $OPENCLAW_STATE_DIR/tools/sherpa-onnx-tts/models, default ~/.openclaw/tools/sherpa-onnx-tts/models)

Resolve the active state directory first:

STATE_DIR="${OPENCLAW_STATE_DIR:-$HOME/.openclaw}"


Then write those resolved paths into the active OpenClaw config file ($OPENCLAW_CONFIG_PATH, default ~/.openclaw/openclaw.json):

{
  skills: {
    entries: {
      "sherpa-onnx-tts": {
        env: {
          SHERPA_ONNX_RUNTIME_DIR: "/path/to/your/state-dir/tools/sherpa-onnx-tts/runtime",
          SHERPA_ONNX_MODEL_DIR: "/path/to/your/state-dir/tools/sherpa-onnx-tts/models/vits-piper-en_US-lessac-high",
        },
      },
    },
  },
}


The wrapper lives in this skill folder. Run it directly, or add the wrapper to PATH:

export PATH="{baseDir}/bin:$PATH"

Usage
{baseDir}/bin/sherpa-onnx-tts -o ./tts.wav "Hello from local TTS."


Notes:

Pick a different model from the sherpa-onnx tts-models release if you want another voice.
If the model dir has multiple .onnx files, set SHERPA_ONNX_MODEL_FILE or pass --model-file.
You can also pass --tokens-file or --data-dir to override the defaults.
Windows: run node {baseDir}\\bin\\sherpa-onnx-tts -o tts.wav "Hello from local TTS."
Weekly Installs
1.0K
Repository
steipete/clawdis
GitHub Stars
367.2K
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass