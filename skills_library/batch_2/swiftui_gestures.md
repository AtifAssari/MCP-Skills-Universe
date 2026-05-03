---
title: swiftui-gestures
url: https://skills.sh/dpearson2699/swift-ios-skills/swiftui-gestures
---

# swiftui-gestures

skills/dpearson2699/swift-ios-skills/swiftui-gestures
swiftui-gestures
Installation
$ npx skills add https://github.com/dpearson2699/swift-ios-skills --skill swiftui-gestures
SKILL.md
SwiftUI Gestures (iOS 26+)

Review, write, and fix SwiftUI gesture interactions. Apply modern gesture APIs with correct composition, state management, and conflict resolution using Swift 6.3 patterns.

Contents
Gesture Overview
TapGesture
LongPressGesture
DragGesture
MagnifyGesture (iOS 17+)
RotateGesture (iOS 17+)
Gesture Composition
@GestureState
Adding Gestures to Views
Custom Gesture Protocol
Common Mistakes
Review Checklist
References
Gesture Overview
Gesture	Type	Value	Since
TapGesture	Discrete	Void	iOS 13
LongPressGesture	Discrete	Bool	iOS 13
DragGesture	Continuous	DragGesture.Value	iOS 13
MagnifyGesture	Continuous	MagnifyGesture.Value	iOS 17
RotateGesture	Continuous	RotateGesture.Value	iOS 17
SpatialTapGesture	Discrete	SpatialTapGesture.Value	iOS 16

Discrete gestures fire once (.onEnded). Continuous gestures stream updates (.onChanged, .onEnded, .updating).

TapGesture

Recognizes one or more taps. Use the count parameter for multi-tap.

// Single, double, and triple tap
TapGesture()            .onEnded { tapped.toggle() }
TapGesture(count: 2)    .onEnded { handleDoubleTap() }
TapGesture(count: 3)    .onEnded { handleTripleTap() }

// Shorthand modifier
Text("Tap me").onTapGesture(count: 2) { handleDoubleTap() }

LongPressGesture

Succeeds after the user holds for minimumDuration. Fails if finger moves beyond maximumDistance.

// Basic long press (0.5s default)
LongPressGesture()
    .onEnded { _ in showMenu = true }

// Custom duration and distance tolerance
LongPressGesture(minimumDuration: 1.0, maximumDistance: 10)
    .onEnded { _ in triggerHaptic() }


With visual feedback via @GestureState + .updating():

@GestureState private var isPressing = false

Circle()
    .fill(isPressing ? .red : .blue)
    .scaleEffect(isPressing ? 1.2 : 1.0)
    .gesture(
        LongPressGesture(minimumDuration: 0.8)
            .updating($isPressing) { current, state, _ in state = current }
            .onEnded { _ in completedLongPress = true }
    )


Shorthand: .onLongPressGesture(minimumDuration:perform:onPressingChanged:).

DragGesture

Tracks finger movement. Value provides startLocation, location, translation, velocity, and predictedEndTranslation.

@State private var offset = CGSize.zero

RoundedRectangle(cornerRadius: 16)
    .fill(.blue)
    .frame(width: 100, height: 100)
    .offset(offset)
    .gesture(
        DragGesture()
            .onChanged { value in offset = value.translation }
            .onEnded { _ in withAnimation(.spring) { offset = .zero } }
    )


Configure minimum distance and coordinate space:

DragGesture(minimumDistance: 20, coordinateSpace: .global)

MagnifyGesture (iOS 17+)

Replaces the deprecated MagnificationGesture. Tracks pinch-to-zoom scale.

@GestureState private var magnifyBy = 1.0

Image("photo")
    .resizable().scaledToFit()
    .scaleEffect(magnifyBy)
    .gesture(
        MagnifyGesture()
            .updating($magnifyBy) { value, state, _ in
                state = value.magnification
            }
    )


With persisted scale:

@State private var currentScale = 1.0
@GestureState private var gestureScale = 1.0

Image("photo")
    .scaleEffect(currentScale * gestureScale)
    .gesture(
        MagnifyGesture(minimumScaleDelta: 0.01)
            .updating($gestureScale) { value, state, _ in state = value.magnification }
            .onEnded { value in
                currentScale = min(max(currentScale * value.magnification, 0.5), 5.0)
            }
    )

RotateGesture (iOS 17+)

RotateGesture is the newer alternative to RotationGesture. Tracks two-finger rotation angle.

@State private var angle = Angle.zero

Rectangle()
    .fill(.blue).frame(width: 200, height: 200)
    .rotationEffect(angle)
    .gesture(
        RotateGesture(minimumAngleDelta: .degrees(1))
            .onChanged { value in angle = value.rotation }
    )


With persisted rotation:

@State private var currentAngle = Angle.zero
@GestureState private var gestureAngle = Angle.zero

Rectangle()
    .rotationEffect(currentAngle + gestureAngle)
    .gesture(
        RotateGesture()
            .updating($gestureAngle) { value, state, _ in state = value.rotation }
            .onEnded { value in currentAngle += value.rotation }
    )

Gesture Composition
.simultaneously(with:) — both gestures recognized at the same time
let magnify = MagnifyGesture()
    .onChanged { value in scale = value.magnification }

let rotate = RotateGesture()
    .onChanged { value in angle = value.rotation }

Image("photo")
    .scaleEffect(scale)
    .rotationEffect(angle)
    .gesture(magnify.simultaneously(with: rotate))


The value is SimultaneousGesture.Value with .first and .second optionals.

.sequenced(before:) — first must succeed before second begins
let longPressBeforeDrag = LongPressGesture(minimumDuration: 0.5)
    .sequenced(before: DragGesture())
    .onEnded { value in
        guard case .second(true, let drag?) = value else { return }
        finalOffset.width += drag.translation.width
        finalOffset.height += drag.translation.height
    }

.exclusively(before:) — only one succeeds (first has priority)
let doubleTapOrLongPress = TapGesture(count: 2)
    .map { ExclusiveResult.doubleTap }
    .exclusively(before:
        LongPressGesture()
            .map { _ in ExclusiveResult.longPress }
    )
    .onEnded { result in
        switch result {
        case .first(let val): handleDoubleTap()
        case .second(let val): handleLongPress()
        }
    }

@GestureState

@GestureState is a property wrapper that automatically resets to its initial value when the gesture ends. Use for transient feedback; use @State for values that persist.

@GestureState private var dragOffset = CGSize.zero  // resets to .zero
@State private var position = CGSize.zero            // persists

Circle()
    .offset(
        x: position.width + dragOffset.width,
        y: position.height + dragOffset.height
    )
    .gesture(
        DragGesture()
            .updating($dragOffset) { value, state, _ in
                state = value.translation
            }
            .onEnded { value in
                position.width += value.translation.width
                position.height += value.translation.height
            }
    )


Custom reset with animation: @GestureState(resetTransaction: Transaction(animation: .spring))

Adding Gestures to Views

Three modifiers control gesture priority in the view hierarchy:

Modifier	Behavior
.gesture()	Default priority. Child gestures win over parent.
.highPriorityGesture()	Parent gesture takes precedence over child.
.simultaneousGesture()	Both parent and child gestures fire.
// Problem: parent tap swallows child tap
VStack {
    Button("Child") { handleChild() }  // never fires
}
.gesture(TapGesture().onEnded { handleParent() })

// Fix 1: Use simultaneousGesture on parent
VStack {
    Button("Child") { handleChild() }
}
.simultaneousGesture(TapGesture().onEnded { handleParent() })

// Fix 2: Give parent explicit priority
VStack {
    Text("Child")
        .gesture(TapGesture().onEnded { handleChild() })
}
.highPriorityGesture(TapGesture().onEnded { handleParent() })

GestureMask

Control which gestures participate when using .gesture(_:including:):

.gesture(drag, including: .gesture)   // only this gesture, not subviews
.gesture(drag, including: .subviews)  // only subview gestures
.gesture(drag, including: .all)       // default: this + subviews

Custom Gesture Protocol

Create reusable gestures by conforming to Gesture:

struct SwipeGesture: Gesture {
    enum Direction { case left, right, up, down }
    let minimumDistance: CGFloat
    let onSwipe: (Direction) -> Void

    init(minimumDistance: CGFloat = 50, onSwipe: @escaping (Direction) -> Void) {
        self.minimumDistance = minimumDistance
        self.onSwipe = onSwipe
    }

    var body: some Gesture {
        DragGesture(minimumDistance: minimumDistance)
            .onEnded { value in
                let h = value.translation.width, v = value.translation.height
                if abs(h) > abs(v) {
                    onSwipe(h > 0 ? .right : .left)
                } else {
                    onSwipe(v > 0 ? .down : .up)
                }
            }
    }
}

// Usage
Rectangle().gesture(SwipeGesture { print("Swiped \($0)") })


Wrap in a View extension for ergonomic API:

extension View {
    func onSwipe(perform action: @escaping (SwipeGesture.Direction) -> Void) -> some View {
        gesture(SwipeGesture(onSwipe: action))
    }
}

Common Mistakes
1. Conflicting parent/child gestures
// DON'T: Parent .gesture() conflicts with child tap
VStack {
    Button("Action") { doSomething() }
}
.gesture(TapGesture().onEnded { parentAction() })

// DO: Use .simultaneousGesture() or .highPriorityGesture()
VStack {
    Button("Action") { doSomething() }
}
.simultaneousGesture(TapGesture().onEnded { parentAction() })

2. Using @State instead of @GestureState for transient state
// DON'T: @State doesn't auto-reset — view stays offset after gesture ends
@State private var dragOffset = CGSize.zero

DragGesture()
    .onChanged { value in dragOffset = value.translation }
    .onEnded { _ in dragOffset = .zero }  // manual reset required

// DO: @GestureState auto-resets when gesture ends
@GestureState private var dragOffset = CGSize.zero

DragGesture()
    .updating($dragOffset) { value, state, _ in
        state = value.translation
    }

3. Not using .updating() for intermediate feedback
// DON'T: No visual feedback during long press
LongPressGesture(minimumDuration: 2.0)
    .onEnded { _ in showResult = true }

// DO: Provide feedback while pressing
@GestureState private var isPressing = false

LongPressGesture(minimumDuration: 2.0)
    .updating($isPressing) { current, state, _ in
        state = current
    }
    .onEnded { _ in showResult = true }

4. Using deprecated gesture types on iOS 17+
// DON'T: Deprecated since iOS 17
MagnificationGesture()   // deprecated — use MagnifyGesture()

// DO: Use newer gesture types
MagnifyGesture()         // iOS 17+
RotateGesture()          // iOS 17+ (newer alternative to RotationGesture)

5. Heavy computation in onChanged
// DON'T: Expensive work called every frame (~60-120 Hz)
DragGesture()
    .onChanged { value in
        let result = performExpensiveHitTest(at: value.location)
        let filtered = applyComplexFilter(result)
        updateModel(filtered)
    }

// DO: Throttle or defer expensive work
DragGesture()
    .onChanged { value in
        dragPosition = value.location  // lightweight state update only
    }
    .onEnded { value in
        performExpensiveHitTest(at: value.location)  // once at end
    }

6. Using onTapGesture for actions that should be a Button
// DON'T: onTapGesture has no accessibility traits, VoiceOver role,
// Voice Control targeting, Switch Control scanning, or keyboard activation
Text("Delete")
    .onTapGesture { deleteItem() }

// DO: Button provides all of these automatically
Button("Delete", role: .destructive) { deleteItem() }

// DO: For custom visuals, use ButtonStyle instead of onTapGesture
Button { toggleExpanded() } label: {
    CardView()
}
.buttonStyle(.plain)


Reserve onTapGesture for multi-tap (count: 2+), tap-location-dependent behavior, or adding tap recognition to non-interactive content that already has appropriate accessibility traits.

Review Checklist
 Correct gesture type: MagnifyGesture/RotateGesture (not deprecated Magnification/Rotation variants)
 @GestureState used for transient values that should reset; @State for persisted values
 .updating() provides intermediate visual feedback during continuous gestures
 Parent/child conflicts resolved with .highPriorityGesture() or .simultaneousGesture()
 onChanged closures are lightweight — no heavy computation every frame
 Composed gestures use correct combinator: simultaneously, sequenced, or exclusively
 Persisted scale/rotation clamped to reasonable bounds in onEnded
 Custom Gesture conformances use var body: some Gesture (not View)
 Gesture-driven animations use .spring or similar for natural deceleration
 GestureMask considered when mixing gestures across view hierarchy levels
 onTapGesture only used where count > 1, tap location, or coordinate space matters — plain single-tap actions use Button instead
References
See references/gesture-patterns.md for drag-to-reorder, pinch-to-zoom, combined rotate+scale, velocity calculations, and SwiftUI/UIKit gesture interop.
Gesture protocol
TapGesture
LongPressGesture
DragGesture
MagnifyGesture
RotateGesture
GestureState
Composing SwiftUI gestures
Adding interactivity with gestures
Weekly Installs
1.2K
Repository
dpearson2699/sw…s-skills
GitHub Stars
512
First Seen
Mar 8, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass