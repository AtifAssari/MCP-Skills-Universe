---
title: draggable-dom-with-lit
url: https://skills.sh/rodydavis/skills/draggable-dom-with-lit
---

# draggable-dom-with-lit

skills/rodydavis/skills/draggable-dom-with-lit
draggable-dom-with-lit
Installation
$ npx skills add https://github.com/rodydavis/skills --skill draggable-dom-with-lit
SKILL.md
Draggable DOM with Lit

In this article I will go over how to set up a Lit web component and use it to create a interactive dom with CSS transforms and slots.

TLDR The final source here and an online demo.

Prerequisites 
Vscode
Node >= 16
Typescript
Getting Started 

We can start off by navigating in terminal to the location of the project and run the following:

npm init @vitejs/app --template lit-ts


Then enter a project name lit-draggable-dom and now open the project in vscode and install the dependencies:

cd lit-draggable-dom
npm i lit
npm i -D @types/node
code .


Update the vite.config.ts with the following:

import { defineConfig } from "vite";
import { resolve } from "path";

export default defineConfig({
  base: "/lit-draggable-dom/",
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, "index.html"),
      },
    },
  },
});

Template 

Open up the index.html and update it with the following:

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/src/favicon.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Lit Draggable DOM</title>
    <style>
      body {
        margin: 0;
        padding: 0;
        width: 100%;
        height: 100vh;
      }
    </style>
    <script type="module" src="/src/draggable-dom.ts"></script>
  </head>
  <body>
    <draggable-dom>
      <img
        src="https://lit.dev/images/logo.svg"
        alt="Lit Logo"
        width="500"
        height="333"
        style="--dx: 59.4909px; --dy: 32.8429px"
      />
      <svg width="400" height="110" style="--dx: 230.057px; --dy: 33.6257px">
        <rect
          width="400"
          height="100"
          style="fill: rgb(0, 0, 255); stroke-width: 3; stroke: rgb(0, 0, 0)"
        />
      </svg>
      <svg height="100" width="100">
        <circle
          cx="50"
          cy="50"
          r="40"
          stroke="black"
          stroke-width="3"
          fill="red"
        />
      </svg>
    </draggable-dom>
  </body>
</html>


We are setting up the lit-element to have a few slots which can be any valid HTML or SVG Elements.

It is optional to set the css custom properties --dx and --dy as this is just the initial positions on the canvas.

Web Component 

Before we update our component we need to rename my-element.ts to draggable-dom.ts

Open up draggable-dom.ts and update it with the following:

import { html, css, LitElement } from "lit";
import { customElement, query } from "lit/decorators.js";

type DragType = "none" | "canvas" | "element";
type SupportedNode = HTMLElement | SVGElement;

@customElement("draggable-dom")
export class CSSCanvas extends LitElement {
  @query("main") root!: HTMLElement;
  @query("#children") container!: HTMLElement;
  @query("canvas") canvas!: HTMLCanvasElement;
  dragType: DragType = "none";
  offset: Offset = { x: 0, y: 0 };
  pointerMap: Map<number, PointerData> = new Map();

  static styles = css`
    :host {
      --offset-x: 0;
      --offset-y: 0;
      --grid-background-color: white;
      --grid-color: black;
      --grid-size: 40px;
      --grid-dot-size: 1px;
    }
    main {
      overflow: hidden;
    }
    canvas {
      background-size: var(--grid-size) var(--grid-size);
      background-image: radial-gradient(
        circle,
        var(--grid-color) var(--grid-dot-size),
        var(--grid-background-color) var(--grid-dot-size)
      );
      background-position: var(--offset-x) var(--offset-y);
      z-index: 0;
    }
    .full-size {
      width: 100%;
      height: 100%;
      position: fixed;
    }
    .child {
      --dx: 0px;
      --dy: 0px;
      position: fixed;
      flex-shrink: 1;
      z-index: var(--layer, 0);
      transform: translate(var(--dx), var(--dy));
    }
    @media (prefers-color-scheme: dark) {
      main {
        --grid-background-color: black;
        --grid-color: grey;
      }
    }
  `;

  render() {
    return html`
      <main class="full-size">
        <canvas class="full-size"></canvas>
        <div id="children" class="full-size"></div>
      </main>
    `;
  }
}

interface Offset {
  x: number;
  y: number;
}

interface PointerData {
  id: number;
  startPos: Offset;
  currentPos: Offset;
}


Here we are just setting up some boilerplate to render a main element with a canvas element as a background and the div element to contain the canvas elements.

We are also making sure to clip and only render what is visible.

The Offset and PointerData interfaces will be used for storing the location of each pointer interacting with the screen.

When the user has dark mode enabled for the system it will change the colors of the canvas grid.

Now let's add the slot children to the canvas by adding the following to the class:

async firstUpdated() {
    const items = Array.from(this.childNodes);
    let i = 0;
    for (const node of items) {
        if (node instanceof SVGElement || node instanceof HTMLElement) {
            const child = node as SupportedNode;
            child.classList.add("child");
            child.style.setProperty("--layer", `${i}`);
            this.container.append(child);
            child.addEventListener("pointerdown", (e: any) => {
                // Pointer Down for Child
            });
            child.addEventListener("pointermove", (e: any) => {
                // Pointer Move for Child
            });
            i++;
        }
    }
    this.requestUpdate();
    this.root.addEventListener("pointerdown", (e: any) => {
        // Pointer Down for Canvas
    });
    this.root.addEventListener("pointermove", (e: any) => {
        // Pointer Move for Canvas
    });
    this.root.addEventListener("pointerup", (e: any) => {
        // Pointer Up for Canvas
    });
}


The order of the slots defines what renders on top of each other. For each item in the slot it sets--layer and z-index to the current index.

Currently nothing is happening when we interact with the elements but things should be rendering.

Now let's add the event handlers for the pointer events by appending the following to the class:

handleDown(event: PointerEvent, type: DragType) {
    if (this.dragType === "none") {
        event.preventDefault();
        this.dragType = type;
        (event.target as Element).setPointerCapture(event.pointerId);
        this.pointerMap.set(event.pointerId, {
            id: event.pointerId,
            startPos: { x: event.clientX, y: event.clientY },
            currentPos: { x: event.clientX, y: event.clientY },
        });
    }
}

handleMove(
    event: PointerEvent,
    type: DragType,
    onMove: (delta: Offset) => void
) {
    if (this.dragType === type) {
        event.preventDefault();
        const saved = this.pointerMap.get(event.pointerId)!;
        const current = { ...saved.currentPos };
        saved.currentPos = { x: event.clientX, y: event.clientY };
        const delta = {
            x: saved.currentPos.x - current.x,
            y: saved.currentPos.y - current.y,
        };
        onMove(delta);
    }
}

handleUp(event: PointerEvent) {
    this.dragType = "none";
    (event.target as Element).releasePointerCapture(event.pointerId);
}


For each event we want to check if the current event canvas or element so if we start moving an element it doesn't move the canvas and vice versa.

When we have a pointer interact with the screen we will add it to the pointer map (since it can be multi touch) and start tracking the offset.

The delta is calculated to move the elements but a global offset is used for the canvas background.

We are setting the pointer capture events so if the mouse is not perfectly on the item it won't lose tracking.

Now let's add methods for moving the canvas and elements by appending the following to the class:

moveCanvas(delta: Offset) {
    this.offset.x += delta.x;
    this.offset.y += delta.y;
    this.root.style.setProperty("--offset-x", `${this.offset.x}px`);
    this.root.style.setProperty("--offset-y", `${this.offset.y}px`);
}

moveElement(child: SupportedNode, delta: Offset) {
    const getNumber = (key: "--dx" | "--dy", fallback: number) => {
      const saved = child.style.getPropertyValue(key);
      if (saved.length > 0) {
        return parseFloat(saved.replace("px", ""));
      }
      return fallback;
    };
    const dx = getNumber("--dx", 0) + delta.x;
    const dy = getNumber("--dy", 0) + delta.y;
    child.style.transform = `translate(${dx}px, ${dy}px)`;
    child.style.setProperty("--dx", `${dx}px`);
    child.style.setProperty("--dy", `${dy}px`);
}


For the canvas it will set a global offset for the CSS background-position and update the saved offset.

For the element we want to transform by the delta so the animation is smooth thanks to hardware acceleration. After the transform it will store the offset as CSS custom properties.

Now let's add the event handlers to the canvas and elements by adjusting the following:

async firstUpdated() {
    const items = Array.from(this.childNodes);
    let i = 0;
    for (const node of items) {
      if (node instanceof SVGElement || node instanceof HTMLElement) {
        const child = node as SupportedNode;
        child.classList.add("child");
        child.style.setProperty("--layer", `${i}`);
        this.container.append(child);
        child.addEventListener("pointerdown", (e: any) => {
          this.handleDown(e, "element");
        });
        child.addEventListener("pointermove", (e: any) => {
          this.handleMove(e, "element", (delta) => {
            this.moveElement(child, delta);
          });
        });
        i++;
      }
    }
    this.requestUpdate();
    this.root.addEventListener("pointerdown", (e: any) => {
      this.handleDown(e, "canvas");
    });
    this.root.addEventListener("pointermove", (e: any) => {
      this.handleMove(e, "canvas", (delta) => {
        this.moveCanvas(delta);
        for (const node of Array.from(this.container.children)) {
          if (node instanceof SVGElement || node instanceof HTMLElement) {
            this.moveElement(node, delta);
          }
        }
      });
    });
    this.root.addEventListener("pointerup", (e: any) => {
      this.handleUp(e);
    });
}


Everything should work as expected now and the final code should look like the following:

import { html, css, LitElement } from "lit";
import { customElement, query } from "lit/decorators.js";

type DragType = "none" | "canvas" | "element";
type SupportedNode = HTMLElement | SVGElement;

@customElement("draggable-dom")
export class DraggableDOM extends LitElement {
  @query("main") root!: HTMLElement;
  @query("#children") container!: HTMLElement;
  @query("canvas") canvas!: HTMLCanvasElement;
  dragType: DragType = "none";
  offset: Offset = { x: 0, y: 0 };
  pointerMap: Map<number, PointerData> = new Map();

  static styles = css`
    :host {
      --offset-x: 0;
      --offset-y: 0;
      --grid-background-color: white;
      --grid-color: black;
      --grid-size: 40px;
      --grid-dot-size: 1px;
    }
    main {
      overflow: hidden;
    }
    canvas {
      background-size: var(--grid-size) var(--grid-size);
      background-image: radial-gradient(
        circle,
        var(--grid-color) var(--grid-dot-size),
        var(--grid-background-color) var(--grid-dot-size)
      );
      background-position: var(--offset-x) var(--offset-y);
      z-index: 0;
    }
    .full-size {
      width: 100%;
      height: 100%;
      position: fixed;
    }
    .child {
      --dx: 0px;
      --dy: 0px;
      position: fixed;
      flex-shrink: 1;
      z-index: var(--layer, 0);
      transform: translate(var(--dx), var(--dy));
    }
    @media (prefers-color-scheme: dark) {
      main {
        --grid-background-color: black;
        --grid-color: grey;
      }
    }
  `;

  render() {
    console.log("render");
    return html`
      <main class="full-size">
        <canvas class="full-size"></canvas>
        <div id="children" class="full-size"></div>
      </main>
    `;
  }

  handleDown(event: PointerEvent, type: DragType) {
    if (this.dragType === "none") {
      event.preventDefault();
      this.dragType = type;
      (event.target as Element).setPointerCapture(event.pointerId);
      this.pointerMap.set(event.pointerId, {
        id: event.pointerId,
        startPos: { x: event.clientX, y: event.clientY },
        currentPos: { x: event.clientX, y: event.clientY },
      });
    }
  }

  handleMove(
    event: PointerEvent,
    type: DragType,
    onMove: (delta: Offset) => void
  ) {
    if (this.dragType === type) {
      event.preventDefault();
      const saved = this.pointerMap.get(event.pointerId)!;
      const current = { ...saved.currentPos };
      saved.currentPos = { x: event.clientX, y: event.clientY };
      const delta = {
        x: saved.currentPos.x - current.x,
        y: saved.currentPos.y - current.y,
      };
      onMove(delta);
    }
  }

  handleUp(event: PointerEvent) {
    this.dragType = "none";
    (event.target as Element).releasePointerCapture(event.pointerId);
  }

  moveCanvas(delta: Offset) {
    this.offset.x += delta.x;
    this.offset.y += delta.y;
    this.root.style.setProperty("--offset-x", `${this.offset.x}px`);
    this.root.style.setProperty("--offset-y", `${this.offset.y}px`);
  }

  moveElement(child: SupportedNode, delta: Offset) {
    const getNumber = (key: "--dx" | "--dy", fallback: number) => {
      const saved = child.style.getPropertyValue(key);
      if (saved.length > 0) {
        return parseFloat(saved.replace("px", ""));
      }
      return fallback;
    };
    const dx = getNumber("--dx", 0) + delta.x;
    const dy = getNumber("--dy", 0) + delta.y;
    child.style.transform = `translate(${dx}px, ${dy}px)`;
    child.style.setProperty("--dx", `${dx}px`);
    child.style.setProperty("--dy", `${dy}px`);
  }

  async firstUpdated() {
    const items = Array.from(this.childNodes);
    let i = 0;
    for (const node of items) {
      if (node instanceof SVGElement || node instanceof HTMLElement) {
        const child = node as SupportedNode;
        child.classList.add("child");
        child.style.setProperty("--layer", `${i}`);
        this.container.append(child);
        child.addEventListener("pointerdown", (e: any) => {
          this.handleDown(e, "element");
        });
        child.addEventListener("pointermove", (e: any) => {
          this.handleMove(e, "element", (delta) => {
            this.moveElement(child, delta);
          });
        });
        child.setAttribute("draggable", "false");
        i++;
      }
    }
    this.requestUpdate();
    this.root.addEventListener("pointerdown", (e: any) => {
      this.handleDown(e, "canvas");
    });
    this.root.addEventListener("pointermove", (e: any) => {
      this.handleMove(e, "canvas", (delta) => {
        this.moveCanvas(delta);
        for (const node of Array.from(this.container.children)) {
          if (node instanceof SVGElement || node instanceof HTMLElement) {
            this.moveElement(node, delta);
          }
        }
      });
    });
    this.root.addEventListener("touchstart", function (e) {
      e.preventDefault();
    });
    this.root.addEventListener("pointerup", (e: any) => {
      this.handleUp(e);
    });
  }
}

interface Offset {
  x: number;
  y: number;
}

interface PointerData {
  id: number;
  startPos: Offset;
  currentPos: Offset;
}

Conclusion 

If you want to learn more about building with Lit you can read the docs here. There is also an example on the Lit playground here.

The source for this example can be found here.

Weekly Installs
38
Repository
rodydavis/skills
GitHub Stars
40
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass