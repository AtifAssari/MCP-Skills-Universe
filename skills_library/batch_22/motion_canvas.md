---
title: motion-canvas
url: https://skills.sh/videozero/skills/motion-canvas
---

# motion-canvas

skills/videozero/skills/motion-canvas
motion-canvas
Installation
$ npx skills add https://github.com/videozero/skills --skill motion-canvas
SKILL.md
Motion Canvas
Base Scene Template
import {makeScene2D} from '@motion-canvas/2d';

export default makeScene2D(function* (view) {

});

Generator Functions & Animation Flow
function* defines a generator function
yield pauses until next frame
yield* delegates to another generator (composition)
export default makeScene2D(function* (view) {
  const circle = createRef<Circle>();
  view.add(<Circle ref={circle} width={100} height={100} fill={'red'} />);

  yield* circle().position.x(300, 1);
  yield* circle().position.x(-300, 1);
});


Reusable animation pattern:

function* flicker(circle: Circle, duration: number): ThreadGenerator {
  const colors = ['#e13238', '#e6a700', '#99C47A'];
  for (const color of colors) {
    circle.fill(color);
    yield* waitFor(duration);
  }
}
yield* flicker(myCircle(), 0.5);

Signals System
import {createSignal} from '@motion-canvas/core';

const radius = createSignal(3);

radius();            // Get → 3
radius(5);           // Set → 5
yield* radius(4, 2); // Tween to 4 over 2 seconds


Computed signals:

const area = createSignal(() => Math.PI * radius() * radius());


Signals in JSX:

<Circle width={() => radius() * 2} height={() => radius() * 2} />
yield* radius(200, 1); // Circle updates automatically


Vector signals:

const position = Vector2.createSignal(Vector2.up);
yield* position(Vector2.zero, 1);


Reset to default:

import {DEFAULT} from '@motion-canvas/core';
signal(DEFAULT);             // Instant reset
yield* signal(DEFAULT, 2);   // Tween to default

References (Refs)

createRef (single node):

const circle = createRef<Circle>();
<Circle ref={circle} width={100} height={100} fill={'red'} />
yield* circle().scale(2, 0.3);


makeRef (arrays):

const circles: Circle[] = [];
{range(10).map(index => (
  <Circle ref={makeRef(circles, index)} x={index * 50} width={40} height={40} />
))}
yield* all(...circles.map(c => c.scale(1.5, 0.5)));


createRefMap (keyed):

const labels = createRefMap<Txt>();
<Txt ref={labels.a} text="Label A" />
<Txt ref={labels.b} text="Label B" />
yield* labels.a().text('Updated A', 0.3);

Scene Hierarchy
view.add(<Circle />);               // Add to view
container().add(<Circle />);         // Add to node
container().insert(<Circle />, 0);   // Insert at index
circle().remove();                   // Remove
container().removeChildren();        // Remove all children
circle().reparent(newParent());      // Move to new parent


Z-order: moveUp(), moveDown(), moveToTop(), moveToBottom(), moveTo(2)

Querying:

import {is} from '@motion-canvas/2d';
const textNodes = view.findAll(is(Txt));
const firstCircle = view.findFirst(is(Circle));

Save / Restore State
yield* circle().save();
yield* all(circle().position.x(300, 1), circle().scale(2, 1));
yield* circle().restore(1); // Animate back to saved state

Time Events & Waiting
import {waitFor, waitUntil, useDuration} from '@motion-canvas/core';

yield* waitFor(2);                    // Wait 2 seconds
yield* waitUntil('voice-line-2');     // Wait for named event
const dur = useDuration('segment');   // Get event duration

Utilities

Random: useRandom(42) → .nextInt(10, 100), .nextFloat(0, 1) Logging: useLogger() → .debug(), .info(), .warn(), .error(); also debug('msg') Hooks: useScene() → .getSize(); useTime() Range: range(5) → [0,1,2,3,4]; range(2,5) → [2,3,4] Threads:

// Spawn a background thread (do NOT yield — spawn starts it automatically)
const task = spawn(function* () {
  yield* loop(Infinity, function* () {
    yield* circle().rotation(360, 2);
    circle().rotation(0);
  });
});

// Cancel a running thread
cancel(task);

// Wait for a thread to finish
yield* join(task);

Shape Components

Circle:

<Circle width={200} height={200} fill={'#e13238'} stroke={'#fff'} lineWidth={4}
  startAngle={0} endAngle={270} closed={false} />


Rect:

<Rect width={300} height={200} fill={'#68ABDF'} radius={10} smoothCorners cornerSharpness={0.6} />


Line:

<Line points={[[0,0],[100,100],[200,50]]} stroke={'#fff'} lineWidth={4}
  lineDash={[20,10]} lineCap={'round'} lineJoin={'round'} startArrow endArrow arrowSize={12} />


Polygon:

<Polygon sides={6} size={200} fill={'#99C47A'} />


Grid:

import {Grid} from '@motion-canvas/2d';

<Grid width={'100%'} height={'100%'} stroke={'#333'} lineWidth={1} spacing={80} start={0} end={1} />


Animate with start/end (0-1) for drawing/erasing effects.

Path (SVG path data):

import {Path} from '@motion-canvas/2d';

<Path data={'M 0 -100 L 29 -40 L 95 -31 Z'} stroke={'#e6a700'} lineWidth={3} />


Supports morphing: yield* path().data(newPathData, 1);

Filters
import {blur, brightness, grayscale, sepia, contrast, saturate, hue, invert} from '@motion-canvas/2d';

<Rect filters={[blur(5), brightness(1.5)]} />
yield* rect().filters([blur(0), grayscale(1)], 1); // Animated


See Filters for full details.

Gradients
import {Gradient} from '@motion-canvas/2d';

const grad = new Gradient({
  type: 'linear',
  from: [-100, 0], to: [100, 0],
  stops: [{offset: 0, color: '#e13238'}, {offset: 1, color: '#68ABDF'}],
});
<Rect fill={grad} />


See Gradients for radial and conic types.

Path Components

Ray: <Ray from={[0,0]} to={[300,200]} endArrow /> — animate with start(1,1) / end(0,1) CubicBezier: <CubicBezier p0={..} p1={..} p2={..} p3={..} /> QuadBezier: <QuadBezier p0={..} p1={..} p2={..} /> Spline: <Spline points={[..]} /> — smooth curves Knot: new Knot([x,y], sharpness) — adjust curve sharpness within Spline

Text Rendering

See Txt for full details.

<Txt text={'Hello World'} fontSize={64} fontFamily={'Inter'} fill={'#ffffff'} wrap={true} />

Custom Components
export class Switch extends Node {
  @initial(false) @signal()
  public declare readonly initialState: SimpleSignal<boolean, this>;

  public constructor(props?: SwitchProps) {
    super({...props});
  }

  public *toggle(duration: number) { /* animation logic */ }
}


Decorators (import from @motion-canvas/2d): @signal(), @initial(value), @colorSignal(), @vector2Signal()

import {Node, NodeProps, initial, signal} from '@motion-canvas/2d';

Scene Transitions
import {slideTransition, fadeTransition, Direction} from '@motion-canvas/core';
yield* slideTransition(Direction.Left);


All transitions (from @motion-canvas/core):

slideTransition(Direction.Left) — slide in from direction
fadeTransition(duration?) — cross-fade
zoomInTransition(area, duration?) — zoom into a BBox area
zoomOutTransition(area, duration?) — zoom out from a BBox area
waitTransition(duration?) — wait without visual transition

Directions: Top, Bottom, Left, Right, TopLeft, TopRight, BottomLeft, BottomRight

Custom:

import {useTransition} from '@motion-canvas/core';
const transition = useTransition(ctx => { /* current */ }, ctx => { /* previous */ });
yield* transition(1);

Advanced Patterns

Conditional: if (cond()) yield* a(); else yield* b(); Reactive: <Circle fill={() => val() > 150 ? 'red' : 'blue'} /> State machines: while/switch pattern with enum states

References
Setup — Project creation, installation, troubleshooting
Flow Control — all, any, chain, delay, sequence, loop
Tweening — Property tweens, easing, interpolation
Springs — Physics-based spring animations
Transforms — Coordinates, positioning, matrix operations
Presentation Mode — Slide-based playback
Txt — Text rendering, dynamic text, multi-line
Layout — Flexbox, cardinal directions, offset
LaTeX — Mathematical equations
Media — Images, icons, video
SVG — Animatable SVG component
Icons — Iconify icon usage and catalog
Camera — Pan, zoom, follow
Filters — blur, brightness, contrast, grayscale, sepia, hue, saturate, invert
Gradients — Linear, radial, conic gradient fills
Effects — createEffect, createDeferredEffect
Rendering — Rendering settings and output configuration
Sounds — Programmable sound playback (@alpha)
Weekly Installs
35
Repository
videozero/skills
GitHub Stars
45
First Seen
Mar 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass