---
rating: ⭐⭐⭐
title: flussonic-media-server
url: https://skills.sh/a1500llc/flussonic-skill/flussonic-media-server
---

# flussonic-media-server

skills/a1500llc/flussonic-skill/flussonic-media-server
flussonic-media-server
Installation
$ npx skills add https://github.com/a1500llc/flussonic-skill --skill flussonic-media-server
SKILL.md
Flussonic Media Server Skill

Provide expert guidance on Flussonic Media Server — a professional software for video streaming, recording, and delivery. Help users configure, troubleshoot, and optimize their Flussonic deployments.

Architecture Overview

Flussonic Media Server is an all-in-one streaming server that handles:

Ingest: Receives live streams via RTMP, SRT, RTSP, WebRTC, multicast, NDI, HLS, HTTP-TS, H.323
Processing: Transcoding (software + hardware GPU), mixing, mosaic, logo overlay, silence detection
Recording: DVR with configurable retention, multiple storage backends, cloud DVR, RAID, nPVR
Delivery: HLS, LL-HLS, DASH, WebRTC, MSE, SRT, MPEG-TS multicast, MSS, thumbnails
Protection: Token auth, DRM (Widevine, PlayReady, FairPlay), GeoIP, session limits, secure links
Scaling: Clustering, load balancing, restreaming between servers, CDN peering
Monitoring: Retroview for input monitoring, stream health dashboards, alerting, Prometheus/Grafana integration
Key Configuration Model

Flussonic uses a text config file (/etc/flussonic/flussonic.conf) or the web UI. Configuration objects:

stream — A named live/VOD stream with input sources, processing, and output settings
template — Reusable configuration applied to streams matching a pattern
dvr — Named global DVR storage config (must be defined before streams reference it)
cluster — Server clustering configuration for redundancy and scaling

Basic config pattern (DVR requires a global dvr block, then streams reference it with @name):

# Global DVR config (define storage location)
dvr storage1 {
  root /mnt/storage;
}

stream channel1 {
  input udp://239.0.0.1:1234;
  input tshttp://backup-server/channel1/mpegts backup;
  transcoder vb=4000k size=1920x1080 ab=128k;
  dvr @storage1 7d;
  push rtmp://cdn.example.com/live/channel1;
}

API Overview

Flussonic exposes two APIs:

Control API (/streamer/api/v3/) — Manage configuration: streams, DVR, templates, sessions, events. Uses Basic auth (edit_auth/view_auth credentials).
Streaming API — Media delivery endpoints: HLS (/stream/index.m3u8), DASH (/stream/index.mpd), WebRTC, thumbnails, etc.

Important API patterns:

Stream creation/update uses PUT (upsert): PUT /streamer/api/v3/streams/{name}
JSON body uses "inputs": [{"url": "..."}] (array of objects), NOT "input": "string"
Monitoring: /streamer/api/v3/monitoring/liveness and /streamer/api/v3/monitoring/readiness
Stats: /streamer/api/v3/config/stats
When to Read Reference Files

This skill has detailed reference guides. Read them based on the user's question:

User asks about...	Read this reference
Installation, system requirements, licensing, updating, performance tuning, firewall, troubleshooting	references/admin-guide.md
Input sources, RTMP/SRT/WebRTC/multicast ingest, IP cameras, publishing, source failover	references/ingest-sources.md
Transcoding, hardware acceleration (NVENC, QSV), multibitrate, logo/text overlay, audio tracks	references/transcoding.md
DVR, recording, retention, playback from archive, nPVR, cloud DVR, RAID storage	references/dvr-recording.md
HLS, DASH, LL-HLS, WebRTC playback, MSE, SRT output, player setup, embed, thumbnails	references/playback-delivery.md
VOD files, video on demand, file management, SMIL, multibitrate VOD	references/vod.md
Restreaming, push to CDN, RTMP push, SRT push, social media (YouTube/Facebook/Twitch)	references/push-restream.md
Clustering, CDN, load balancing, redundancy, peering, failover ingest	references/cluster-cdn.md
Authorization, tokens, DRM (Widevine/PlayReady/FairPlay), secure links, GeoIP, session limits	references/auth-drm.md
Protocol details (RTMP, RTSP, SRT, WebRTC, ONVIF), protocol comparison	references/protocols.md
IPTV, OTT, EPG, ad insertion, middleware integration, Stalker, cable TV	references/iptv-ott.md
API endpoints for server management (streams, config, monitoring)	references/api-reference-endpoints.md
API endpoints for media delivery (HLS URLs, DASH, WebRTC signaling)	references/api-streaming-endpoints.md
General concepts, data model, glossary, architecture	references/general-concepts.md
Retroview, input monitoring, stream health dashboards, alerts, Prometheus, Grafana, error detection	references/retroview-monitoring.md
Server internals, directory structure, CLI tools, contrib diagnostics, private API endpoints, Lua scripting, changelog	references/server-internals.md

Read only the relevant reference(s) — don't load all files at once. For complex questions, read 2-3 related references.

Common Workflows
Live Ingest → Transcode → DVR → Restream to CDN

This is the most common workflow. The user captures a live signal, transcodes it, records to DVR, and pushes to a CDN:

stream live_channel {
  input udp://239.0.0.1:1234;

  # Transcode to multibitrate (multiple vb= on one line = multiple video tracks)
  transcoder vb=4000k size=1920x1080 vb=2000k size=1280x720 vb=800k size=640x360 ab=128k;

  # Record with 7 days retention (references global dvr block)
  dvr @storage1 7d;

  # Enable output protocols
  protocols dash hls;

  # Push to CDN
  push rtmp://cdn.example.com/live/channel;
}

Source Failover

Configure multiple sources with automatic failover (priority by order, first = primary):

stream resilient_channel {
  input srt://primary-encoder:9000 streamid="#!::m=request,r=resilient_channel";
  input rtmp://backup-encoder/live/stream;
  input fake://fake;  # Test pattern if all sources fail
}

Hardware Transcoding (NVIDIA)
stream gpu_channel {
  input rtsp://camera:554/stream;
  transcoder hw=nvenc deviceid=0 vb=5000k size=1920x1080 deinterlace=true deinterlace_rate=frame vb=2500k size=1280x720 vb=1000k size=640x360 ab=128k;
}


Note: Intel QSV was deprecated in v25.09 and removed from the transcoder. Use NVIDIA NVENC for hardware acceleration.

Cluster Setup
# All peers share the same cluster_key
# On all servers:
cluster_key mySecretKey;
peer server1.example.com;
peer server2.example.com;

# Stream with cluster_ingest (auto-distributes capture across peers)
stream channel1 {
  input rtsp://camera:554/stream;
  cluster_ingest;
}

# Or pull from another peer:
stream channel1 {
  input m4f://origin-server/channel1;
}

Input Monitoring with Retroview

Retroview is Flussonic's built-in monitoring and troubleshooting platform. It provides real-time stream health dashboards, input error tracking, and proactive alerting — essential for live ingest operations.

Key monitoring capabilities:

Input errors: lost packets, TS continuity counter errors, scrambled packets, broken payloads, HTTP errors
Server metrics: CPU, scheduler utilization, memory, disk I/O, GPU usage, network bandwidth
Alerts: Configurable thresholds for stream failures, mass input loss, transcoding overload, DVR storage
Integration: Prometheus metrics export, Grafana dashboards, webhooks (Slack, Telegram, PagerDuty)

For monitoring a live ingest + transcode + CDN restream workflow, the critical metrics to watch are:

Input error rate (lost_packets, ts_cc errors) — detect source degradation early
Scheduler utilization — ensure transcoding isn't overloading the CPU
DVR disk usage — prevent recording failures from full storage
Output push status — detect CDN delivery failures

Read references/retroview-monitoring.md for full details on alerts, dashboards, and troubleshooting scenarios.

DRM Protection (CPIX)

Flussonic uses the CPIX standard for multi-DRM. Config uses a single drm cpix directive with a keyserver:

stream protected_channel {
  input udp://239.0.0.1:1234;
  drm cpix keyserver=http://drm-server/api/drm/cpix?client=myapp&clientToken=SECRET resource_id=protected_channel;
  protocols dash hls;
}


This enables Widevine, PlayReady, and FairPlay simultaneously through the CPIX keyserver.

SRT Ingest & Output

SRT Publish (receive incoming SRT streams):

# Global shared SRT publish port
srt_publish {
  port 9998;
  passphrase 0123456789;
}

stream my_srt_stream {
  input publish://;
}


Per-stream SRT play (output):

stream my_stream {
  input udp://239.0.0.1:1234;
  srt_play {
    port 9300;
  }
}


SRT caller (pull from remote SRT source):

stream srt_pull {
  input srt://remote-server:8888 streamid="#!::m=request,r=stream_name";
}

Response Guidelines

When helping users:

Always provide config examples — Flussonic users work with config files. Show the exact syntax they need.
Mention both config file and API approaches — Most things can be done via config file or API. Mention both when relevant.
Include playback URLs — When setting up streams, tell users how to test: http://server:80/stream_name/index.m3u8 for HLS.
Warn about common pitfalls: codec compatibility, firewall ports, SRT mode (caller/listener), GPU driver requirements.
Reference official docs — Point users to https://flussonic.com/doc/ for the specific topic when appropriate.
Consider the user's scale — Ask if they haven't said: how many streams? what bitrate? what hardware? This matters for performance tuning.
Never directly modify system files — Show config examples for the user to apply themselves. Do not write to /etc/flussonic/flussonic.conf or other system paths, run service commands, or change firewall rules directly. Present the config/commands and let the user execute them on their server. Use the API (PUT /streamer/api/v3/streams/{name}) when the user wants to make changes programmatically.
Important Ports
Port	Protocol	Usage
80	HTTP	Web UI, API, HLS/DASH
443	HTTPS	Secure web UI and streaming
1935	TCP	RTMP ingest/publish
554	TCP	RTSP
8080	TCP	API (alternative)
9000+	UDP	SRT (configurable)
Custom	UDP	Multicast ingest
Quick Troubleshooting
Input quality issues: Use Retroview input monitoring to check lost_packets, ts_cc errors. See references/retroview-monitoring.md.
Stream not starting: Check source URL, firewall, codec support. Use input_monitor in config.
High CPU: Enable hardware transcoding (NVENC), reduce resolution/bitrate, check if transcoding is needed. Note: Intel QSV was removed in v25.09.
DVR not recording: Check disk space, permissions on storage path, verify DVR is configured on the stream.
Playback stuttering: Check bitrate vs. available bandwidth, consider ABR profiles, check server CPU load.
API 401: Verify Basic auth credentials match edit_auth/view_auth in flussonic.conf. API base path is /streamer/api/v3/.
SRT connection fails: Check firewall UDP ports, verify passphrase (10-79 chars), check streamid format for caller mode.
API "authorization_failed": The v3 API requires edit_auth credentials. Use -u user:pass with curl.
Weekly Installs
9
Repository
a1500llc/flussonic-skill
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn