---
title: xrift-world
url: https://skills.sh/webxr-jp/xrift-skills/xrift-world
---

# xrift-world

skills/webxr-jp/xrift-skills/xrift-world
xrift-world
Installation
$ npx skills add https://github.com/webxr-jp/xrift-skills --skill xrift-world
SKILL.md
XRift World Development Guide

A guide for creating and modifying WebXR worlds for the XRift platform.

References
API Reference - Full specification of all hooks, components, and constants in @xrift/world-components
Code Templates - Implementation patterns for GLB models, textures, Skybox, interactions, and more
Type Definitions - Type definitions for User, PlayerMovement, VRTrackingData, TeleportDestination, WorldInfo, InstanceInfo, ConfirmOptions, Tag, VideoState, LogEntry, PhysicsConfig, CameraConfig, VoiceVolumeOverrideContextValue
Critical Rules (Must Follow)
Always use baseUrl from useXRift() when loading assets
Place asset files in the public/ directory
baseUrl includes a trailing /, so join with ${baseUrl}path (${baseUrl}/path is WRONG)
// Correct
const { baseUrl } = useXRift()
const model = useGLTF(`${baseUrl}robot.glb`)

// Wrong
const model = useGLTF('/robot.glb')           // Absolute path - NG
const model = useGLTF(`${baseUrl}/robot.glb`) // Extra / - NG

Project Overview
Purpose: WebXR worlds for the XRift platform
Tech Stack: React Three Fiber + Rapier physics engine + Module Federation
How It Works: Uploaded to CDN, dynamically loaded by the frontend
Project Structure
xrift-world-template/
├── public/              # Asset files (place directly, no subdirectories needed)
│   ├── model.glb
│   ├── texture.jpg
│   └── skybox.jpg
├── src/
│   ├── components/      # 3D components
│   ├── World.tsx        # Main world component
│   ├── dev.tsx          # Development entry point
│   ├── index.tsx        # Production export
│   └── constants.ts     # Constants
├── .triplex/            # Triplex (3D editor) config
├── xrift.json           # XRift CLI config
├── vite.config.ts       # Build config (Module Federation)
└── package.json

xrift.json Configuration
physics (Physics Settings)
Field	Type	Default	Description
gravity	number	9.81	Gravity strength (positive value; Earth=9.81, Moon=1.62, Jupiter=24.79)
allowInfiniteJump	boolean	true	Whether to allow infinite jumping
{
  "physics": {
    "gravity": 9.81,
    "allowInfiniteJump": true
  }
}


Examples:

Obstacle course world: "allowInfiniteJump": false to add fall risk
Low gravity world: "gravity": 1.62 (Moon gravity) for floaty movement
High gravity world: "gravity": 24.79 (Jupiter gravity) for heavy movement
camera (Camera Settings)
Field	Type	Description
near	number	Near clip distance (hides objects closer than this distance)
far	number	Far clip distance (hides objects farther than this distance)
{
  "camera": {
    "near": 0.1,
    "far": 1000
  }
}


Examples:

Vast world: "far": 5000 to render distant objects
Precise world: "near": 0.01 for higher near-range rendering precision
outputBufferType (Output Buffer Type)

Specifies the output buffer type for WebGLRenderer. Affects post-processing and HDR rendering precision.

Value	Description
UnsignedByteType	8-bit integer (default, standard rendering)
HalfFloatType	16-bit float (HDR and post-processing)
FloatType	32-bit float (highest precision, higher GPU cost)
{
  "outputBufferType": "HalfFloatType"
}

permissions (Permission Settings)

Declares permissions required by the world. Declared permissions are shown to users as an approval screen when entering an instance.

Field	Type	Description
allowedDomains	string[]	External domains the world communicates with
allowedCodeRules	string[]	Code security rules to relax
{
  "permissions": {
    "allowedDomains": ["api.example.com", "cdn.example.com"],
    "allowedCodeRules": ["no-storage-access", "no-network-without-permission"]
  }
}

allowedCodeRules

Rules defined by @xrift/code-security analyzer. By default, unsafe operations are blocked but can be relaxed when required.

Category	Rule	Description
Dynamic Code	no-eval	Allows eval()
Dynamic Code	no-new-function	Allows Function constructor
Dynamic Code	no-string-timeout	Allows setTimeout/setInterval with string args
Dynamic Code	no-javascript-blob	Allows JavaScript Blob creation
Obfuscation	no-obfuscation	Allows obfuscated code patterns
Network	no-network-without-permission	Allows fetch, WebSocket, etc.
Network	no-unauthorized-domain	Allows connections outside allowedDomains
Network	no-rtc-connection	Allows WebRTC peer connections
Network	no-external-import	Allows external JS module imports
Storage	no-storage-access	Allows localStorage/sessionStorage
Storage	no-cookie-access	Allows cookie read/write
Storage	no-indexeddb-access	Allows IndexedDB access
Storage	no-storage-event	Allows storage event listening
DOM	no-dangerous-dom	Allows innerHTML and script injection
Browser API	no-navigator-access	Allows geolocation, camera, mic, clipboard
Global	no-sensitive-api-override	Allows overriding fetch, etc.
Global	no-global-override	Allows overriding window, document
Global	no-prototype-pollution	Allows prototype modification
Command Reference
# Development
npm run dev        # Start dev server (http://localhost:5173)
npm run build      # Production build
npm run typecheck  # Type checking

# XRift CLI
xrift login        # Authenticate
xrift create world # Create new world project
xrift upload       # Upload (auto-detect from xrift.json)
xrift whoami       # Check logged-in user
xrift logout       # Log out

Development Environment

Run npm run dev to start the dev server. You can navigate and test the world in first-person view.

Action	Key
Look around	Click to lock mouse, then move mouse
Move	W / A / S / D
Ascend / Descend	E or Space / Q
Interact	Aim crosshair and click
Release mouse lock	ESC

Interactable component click behavior can also be tested in the dev environment (the center Raycaster detects the LAYERS.INTERACTABLE layer).

dev.tsx Structure

src/dev.tsx is the development-only entry point. It is not included in the production build.

Note: XRiftProvider is not needed in production (the frontend wraps it automatically).

Dependencies
Required (peerDependencies)
react / react-dom ^19.0.0
three ^0.182.0
@react-three/fiber ^9.3.0
@react-three/drei ^10.7.3
@react-three/rapier ^2.1.0
XRift-specific
@xrift/world-components - XRift hooks and components
Module Federation Shared パッケージ

ホスト（xrift.net）と shared で共有されるパッケージ。ワールドの vite.config.ts で shared に宣言すれば、ワールドチャンクにバンドルされずホストから提供される。

パッケージ	バージョン要件
react	^19.0.0
react-dom	^19.0.0
react-dom/client	-
react/jsx-runtime	^19.0.0
three	^0.176.0
three/addons/loaders/GLTFLoader.js	-
three/addons/loaders/DRACOLoader.js	-
three/addons/loaders/KTX2Loader.js	-
@react-three/fiber	^9.0.0
@react-three/rapier	^2.0.0
@react-three/drei	^10.0.0
@react-three/uikit	^1.0.0
@pmndrs/uikit	^1.0.0
@xrift/world-components	^0.1.0
three/addons の注意
three/addons バレルを shared にすると Lottie 由来の eval がバンドルに含まれるため、サブパス単位で shared にしている
ワールド側でも three/addons/loaders/DRACOLoader.js のようにサブパスで import & shared 宣言する
// vite.config.ts — shared の設定例（xrift-world-template 準拠）
federation({
  name: 'xrift_world_template',
  filename: 'remoteEntry.js',
  exposes: {
    './World': './src/index.tsx',
  },
  shared: {
    react: { singleton: true, requiredVersion: '^19.0.0' },
    'react-dom': { singleton: true, requiredVersion: '^19.0.0' },
    'react-dom/client': { singleton: true },
    'react/jsx-runtime': { singleton: true },
    three: { singleton: true, requiredVersion: '^0.176.0' },
    // three/addons はバレルではなくサブパス単位で宣言する
    'three/addons/loaders/DRACOLoader.js': { singleton: true },
    '@react-three/fiber': { singleton: true, requiredVersion: '^9.3.0' },
    '@react-three/rapier': { singleton: true, requiredVersion: '^2.1.0' },
    '@react-three/drei': { singleton: true, requiredVersion: '^10.7.3' },
    '@xrift/world-components': { singleton: true, requiredVersion: '^0.1.0' },
  },
}),

Troubleshooting
"useXRift must be used within XRiftProvider"

Cause: Not wrapped with XRiftProvider

Solution:

Check that src/dev.tsx uses XRiftProvider
When using Triplex: check .triplex/provider.tsx
Assets fail to load

Cause: Not using baseUrl, or incorrect path concatenation

Solution:

// Correct
const { baseUrl } = useXRift()
const model = useGLTF(`${baseUrl}robot.glb`)

// Wrong
const model = useGLTF('/robot.glb')
const model = useGLTF(`${baseUrl}/robot.glb`)

Physics not working

Cause: Not wrapped with Physics component, or missing RigidBody

Solution:

<Physics>
  <RigidBody type="fixed">  {/* or "dynamic" */}
    <mesh>...</mesh>
  </RigidBody>
</Physics>

Links
XRift Documentation
XRift CLI (GitHub)
React Three Fiber
Rapier Physics
Triplex (Visual Editor)
Example Implementations
GLB model: src/components/Duck/index.tsx
Skybox: src/components/Skybox/index.tsx
Animation: src/components/RotatingObject/index.tsx
Interaction: src/components/InteractableButton/index.tsx
User tracking: src/components/RemoteUserHUDs/index.tsx
Teleport: src/components/TeleportPortal/index.tsx
Main world: src/World.tsx
Weekly Installs
27
Repository
webxr-jp/xrift-skills
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn