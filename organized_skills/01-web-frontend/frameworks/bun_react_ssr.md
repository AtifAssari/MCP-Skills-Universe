---
rating: ⭐⭐⭐
title: bun react ssr
url: https://skills.sh/secondsky/claude-skills/bun-react-ssr
---

# bun react ssr

skills/secondsky/claude-skills/bun-react-ssr
bun-react-ssr
Installation
$ npx skills add https://github.com/secondsky/claude-skills --skill bun-react-ssr
SKILL.md
Bun React SSR

Build custom server-rendered React applications with Bun.

Quick Start
# Initialize project
mkdir my-ssr-app && cd my-ssr-app
bun init

# Install dependencies
bun add react react-dom
bun add -D @types/react @types/react-dom

Basic SSR Setup
Server Entry
// src/server.tsx
import { renderToString } from "react-dom/server";
import App from "./App";

Bun.serve({
  port: 3000,
  async fetch(req) {
    const url = new URL(req.url);

    // Serve static files
    if (url.pathname.startsWith("/static/")) {
      const file = Bun.file(`./public${url.pathname}`);
      if (await file.exists()) {
        return new Response(file);
      }
    }

    // Render React app
    const html = renderToString(<App url={url.pathname} />);

    return new Response(
      `<!DOCTYPE html>
      <html>
        <head>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <title>React SSR</title>
        </head>
        <body>
          <div id="root">${html}</div>
          <script src="/static/client.js"></script>
        </body>
      </html>`,
      {
        headers: { "Content-Type": "text/html" },
      }
    );
  },
});

console.log("Server running on http://localhost:3000");

Client Entry
// src/client.tsx
import { hydrateRoot } from "react-dom/client";
import App from "./App";

hydrateRoot(
  document.getElementById("root")!,
  <App url={window.location.pathname} />
);

React App
// src/App.tsx
interface AppProps {
  url: string;
}

export default function App({ url }: AppProps) {
  return (
    <div>
      <h1>React SSR with Bun</h1>
      <p>Current path: {url}</p>
      <button onClick={() => alert("Hydrated!")}>Click me</button>
    </div>
  );
}

Build Client Bundle
// build.ts
await Bun.build({
  entrypoints: ["./src/client.tsx"],
  outdir: "./public/static",
  target: "browser",
  minify: true,
  splitting: true,
});

# Build client
bun run build.ts

# Start server
bun run src/server.tsx

Streaming SSR
// src/server-streaming.tsx
import { renderToReadableStream } from "react-dom/server";
import App from "./App";

Bun.serve({
  port: 3000,
  async fetch(req) {
    const url = new URL(req.url);

    const stream = await renderToReadableStream(
      <App url={url.pathname} />,
      {
        bootstrapScripts: ["/static/client.js"],
        onError(error) {
          console.error(error);
        },
      }
    );

    // Wait for shell to be ready (Suspense boundaries)
    await stream.allReady;

    return new Response(stream, {
      headers: { "Content-Type": "text/html" },
    });
  },
});

With Suspense
// src/App.tsx
import { Suspense } from "react";

function SlowComponent() {
  // This would be a data fetching component
  return <div>Loaded!</div>;
}

export default function App({ url }: { url: string }) {
  return (
    <html>
      <head>
        <title>Streaming SSR</title>
      </head>
      <body>
        <div id="root">
          <h1>Fast Shell</h1>
          <Suspense fallback={<div>Loading...</div>}>
            <SlowComponent />
          </Suspense>
        </div>
      </body>
    </html>
  );
}

Data Fetching
Server-Side Data
// src/server.tsx
import { renderToString } from "react-dom/server";
import { Database } from "bun:sqlite";
import App from "./App";

const db = new Database("data.sqlite");

Bun.serve({
  async fetch(req) {
    const url = new URL(req.url);

    // Fetch data server-side
    const users = db.query("SELECT * FROM users").all();

    const html = renderToString(
      <App url={url.pathname} initialData={{ users }} />
    );

    return new Response(
      `<!DOCTYPE html>
      <html>
        <head><title>SSR</title></head>
        <body>
          <div id="root">${html}</div>
          <script>
            window.__INITIAL_DATA__ = ${JSON.stringify({ users })};
          </script>
          <script src="/static/client.js"></script>
        </body>
      </html>`,
      { headers: { "Content-Type": "text/html" } }
    );
  },
});

Client Hydration
// src/client.tsx
import { hydrateRoot } from "react-dom/client";
import App from "./App";

const initialData = (window as any).__INITIAL_DATA__;

hydrateRoot(
  document.getElementById("root")!,
  <App url={window.location.pathname} initialData={initialData} />
);

Routing
Simple Router
// src/Router.tsx
import { useState, useEffect } from "react";

interface Route {
  path: string;
  component: React.ComponentType;
}

interface RouterProps {
  routes: Route[];
  initialPath: string;
}

export function Router({ routes, initialPath }: RouterProps) {
  const [path, setPath] = useState(initialPath);

  useEffect(() => {
    const handlePopState = () => setPath(window.location.pathname);
    window.addEventListener("popstate", handlePopState);
    return () => window.removeEventListener("popstate", handlePopState);
  }, []);

  const route = routes.find((r) => r.path === path);
  const Component = route?.component || NotFound;

  return <Component />;
}

export function Link({ href, children }: { href: string; children: React.ReactNode }) {
  const handleClick = (e: React.MouseEvent) => {
    e.preventDefault();
    window.history.pushState({}, "", href);
    window.dispatchEvent(new PopStateEvent("popstate"));
  };

  return <a href={href} onClick={handleClick}>{children}</a>;
}

function NotFound() {
  return <h1>404 - Not Found</h1>;
}

CSS Handling
Inline Styles
const html = renderToString(<App />);

return new Response(
  `<!DOCTYPE html>
  <html>
    <head>
      <style>${await Bun.file("./src/styles.css").text()}</style>
    </head>
    <body>
      <div id="root">${html}</div>
    </body>
  </html>`,
  { headers: { "Content-Type": "text/html" } }
);

External Stylesheet
// Build CSS
await Bun.build({
  entrypoints: ["./src/styles.css"],
  outdir: "./public/static",
});

// Link in HTML
`<link rel="stylesheet" href="/static/styles.css">`

Development Setup
Hot Reload Development
// dev.ts
import { watch } from "fs";

const srcDir = "./src";
let serverProcess: Subprocess | null = null;

async function startServer() {
  serverProcess?.kill();
  serverProcess = Bun.spawn(["bun", "run", "src/server.tsx"], {
    stdout: "inherit",
    stderr: "inherit",
  });
}

// Watch for changes
watch(srcDir, { recursive: true }, async (event, filename) => {
  console.log(`Change detected: ${filename}`);
  await startServer();
});

await startServer();
console.log("Dev server watching...");

Production Build
// build-prod.ts

// Build client
await Bun.build({
  entrypoints: ["./src/client.tsx"],
  outdir: "./dist/public/static",
  target: "browser",
  minify: true,
  splitting: true,
  sourcemap: "external",
});

// Build server
await Bun.build({
  entrypoints: ["./src/server.tsx"],
  outdir: "./dist",
  target: "bun",
  minify: true,
});

console.log("Build complete!");

Common Errors
Error	Cause	Fix
Hydration mismatch	Server/client HTML differs	Check initial state
document is not defined	SSR accessing DOM	Guard with typeof window
Cannot use hooks	Hooks outside component	Check component structure
Flash of unstyled content	CSS not loaded	Inline critical CSS
Performance Tips
Use streaming SSR for faster TTFB
Inline critical CSS above the fold
Code split client bundle
Cache rendered HTML for static pages
Use Suspense for progressive loading
When to Load References

Load references/streaming-patterns.md when:

Complex Suspense boundaries
Selective hydration
Progressive enhancement

Load references/caching.md when:

HTML caching strategies
CDN integration
Edge rendering
Weekly Installs
91
Repository
secondsky/claude-skills
GitHub Stars
129
First Seen
3 days ago
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass