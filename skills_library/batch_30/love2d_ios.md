---
title: love2d-ios
url: https://skills.sh/chongdashu/love2d-pocket-bomber-game/love2d-ios
---

# love2d-ios

skills/chongdashu/love2d-pocket-bomber-game/love2d-ios
love2d-ios
Installation
$ npx skills add https://github.com/chongdashu/love2d-pocket-bomber-game --skill love2d-ios
SKILL.md
Love2D iOS Development

Build games with Love2D and deploy them to iOS devices—from first prototype to App Store.

Philosophy: Mobile-First Game Development

Love2D was born on desktop, but mobile is where players are. The challenge isn't just "making it run on iOS"—it's rethinking the game for touch.

Before building for iOS, ask:

How will players interact without a keyboard?
What screen sizes and orientations should be supported?
Is the game's pacing appropriate for mobile sessions?
What gestures feel natural for this game's actions?

Core principles:

Touch is not a keyboard substitute: Design touch controls that feel native, not bolted-on. A virtual d-pad is a last resort, not a first choice.

Screen size is a variable, not a constant: Hard-coded coordinates break on different devices. Think in percentages and relative positions.

The build pipeline is fragile: Xcode projects, code signing, and bundle resources have many failure points. Understand the system, don't just copy commands.

Iterate on device early: The simulator lies. Test on real hardware as soon as possible.

Development Workflow
Desktop Development First

Develop and test on desktop before touching iOS:

# macOS: Love2D isn't in PATH by default
/Applications/love.app/Contents/MacOS/love /path/to/game

# Or create an alias in ~/.zshrc
alias love="/Applications/love.app/Contents/MacOS/love"

Project Structure
my-game/
├── conf.lua          # Window size, Love2D version
├── main.lua          # Entry point
├── touch.lua         # Mobile touch controls (optional on desktop)
└── [game modules]    # Player, enemies, etc.

iOS Build Pipeline

See references/ios-setup.md for detailed setup steps.

Quick overview:

Download Love2D iOS source + Apple libraries
Copy libraries to Xcode project
Create game.love (zip of Lua files)
Add game.love to Xcode bundle resources
Configure signing and deploy
Update Workflow

Every code change requires rebuilding:

# From game directory
rm -f game.love
zip -9 -r game.love *.lua [assets/]
cp game.love /path/to/xcode/ios/
# Then build in Xcode (Cmd+R)

Touch Control Patterns

See references/touch-controls.md for implementation details.

Choosing the Right Pattern
Game Type	Recommended Control
Platformer	Virtual joystick + action buttons
Puzzle	Direct touch/drag on game objects
Endless runner	Tap/swipe gestures
Turn-based	Tap to select, tap to confirm
Twin-stick	Dual virtual joysticks
Touch Event Basics
function love.touchpressed(id, x, y, dx, dy, pressure)
    -- id: unique per finger (for multitouch)
    -- x, y: screen coordinates
end

function love.touchmoved(id, x, y, dx, dy, pressure)
    -- Track finger movement
end

function love.touchreleased(id, x, y, dx, dy, pressure)
    -- Clean up touch state
end

Platform Detection
local function isMobile()
    local os = love.system.getOS()
    return os == "iOS" or os == "Android"
end

-- Use this to conditionally show touch controls
if isMobile() then
    touchControls = require("touch")
end

Screen Adaptation
Dynamic Sizing

Never hard-code 800x600. Always query dimensions:

local screenW, screenH

function love.load()
    screenW, screenH = love.graphics.getDimensions()
end

function love.resize(w, h)
    screenW, screenH = w, h
    -- Reposition UI, regenerate layouts
end

Positioning Strategies

Percentage-based:

local buttonX = screenW * 0.85  -- 85% from left
local buttonY = screenH * 0.9   -- 90% from top


Anchor-based:

local margin = 20
local rightEdge = screenW - margin
local bottomEdge = screenH - margin


Aspect-ratio aware:

local targetAspect = 16/9
local currentAspect = screenW / screenH
-- Add letterboxing or adjust game area

Anti-Patterns to Avoid

❌ Hard-coded coordinates

-- BAD: Breaks on different screens
player.x = 400
button.y = 550


Why bad: iPhone SE and iPad Pro have very different dimensions. Better: Use percentages or anchor points relative to screen size.

❌ Ignoring the "No-game screen" Why bad: Your game.love wasn't bundled—the app is working, your game isn't loaded. Better: Verify game.love is in "Copy Bundle Resources" build phase.

❌ Testing only on simulator Why bad: Simulator has different performance, touch behavior, and screen characteristics. Better: Deploy to a real device early and often.

❌ Giant virtual joysticks Why bad: Obscures gameplay, feels clunky. Better: Semi-transparent, appropriately sized (60-80px radius), positioned in thumb-reach zones.

❌ Copying Xcode project changes blindly Why bad: You won't know how to fix it when it breaks differently. Better: Understand the project.pbxproj structure—PBXBuildFile, PBXFileReference, build phases.

❌ Forgetting to rebuild game.love Why bad: You're testing old code and wondering why changes don't work. Better: Script the rebuild process. Make it one command.

Common Issues and Solutions
Deployment Target Errors

Error: IPHONEOS_DEPLOYMENT_TARGET is set to 8.0, but range is 12.0 to X.X

Fix:

find . -name "*.pbxproj" -exec sed -i '' \
  's/IPHONEOS_DEPLOYMENT_TARGET = 8.0/IPHONEOS_DEPLOYMENT_TARGET = 15.0/g' {} \;

"No-game screen" on Device

Cause: game.love not in bundle resources.

Fix: Add game.love to Xcode project:

Right-click ios folder → Add Files
Select game.love
Ensure "Add to targets: love-ios" is checked

If that fails, see references/xcode-project-structure.md for manual pbxproj editing.

Signing Errors

Fix: In Xcode:

Select love-ios target
Signing & Capabilities → Select your Team
Change Bundle Identifier to something unique
Touch Not Responding

Causes:

Not implementing touch callbacks
Touch area too small (minimum 44x44 points recommended)
Touch being consumed by wrong element
Variation Guidance

Touch control layouts should vary based on:

Game genre (platformer vs puzzle vs action)
Screen size (phone vs tablet)
Player handedness (consider offering options)
Game complexity (fewer buttons for simpler games)

Avoid converging on:

Always using virtual joystick (sometimes gestures are better)
Always putting fire button bottom-right (context matters)
Fixed button sizes (adapt to screen)
File Locations Reference
Purpose	Path
Xcode project	love-X.X-ios-source/platform/xcode/love.xcodeproj
iOS libraries	love-X.X-ios-source/platform/xcode/ios/libraries/
game.love destination	love-X.X-ios-source/platform/xcode/ios/game.love
Project config	love.xcodeproj/project.pbxproj
Remember

Love2D makes game development joyful. iOS deployment adds friction, but understanding the pipeline—not just following steps—makes you resilient when things break.

The goal isn't "run on iOS." The goal is "feel great on iOS."

Touch controls that feel native, layouts that adapt gracefully, and a build process you understand—that's the standard.

Claude is capable of building complete, polished mobile games. These guidelines illuminate the path from desktop prototype to iOS deployment.

Weekly Installs
13
Repository
chongdashu/love…ber-game
GitHub Stars
15
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass