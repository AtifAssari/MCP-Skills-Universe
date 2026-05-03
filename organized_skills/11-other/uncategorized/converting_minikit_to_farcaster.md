---
rating: ⭐⭐
title: converting-minikit-to-farcaster
url: https://skills.sh/base/skills/converting-minikit-to-farcaster
---

# converting-minikit-to-farcaster

skills/base/skills/converting-minikit-to-farcaster
converting-minikit-to-farcaster
Installation
$ npx skills add https://github.com/base/skills --skill converting-minikit-to-farcaster
SKILL.md
MiniKit to Farcaster SDK
Breaking Changes (SDK v0.2.0+)
sdk.context is a Promise — must await
sdk.isInMiniApp() accepts no parameters
sdk.actions.setPrimaryButton() has no onClick callback

Check version: npm list @farcaster/miniapp-sdk

Quick Reference
MiniKit	Farcaster SDK	Notes
useMiniKit().setFrameReady()	await sdk.actions.ready()	
useMiniKit().context	await sdk.context	Async
useMiniKit().isSDKLoaded	await sdk.isInMiniApp()	No params
useClose()	await sdk.actions.close()	
useOpenUrl(url)	await sdk.actions.openUrl(url)	
useViewProfile(fid)	await sdk.actions.viewProfile({ fid })	
useViewCast(hash)	await sdk.actions.viewCast({ hash })	
useComposeCast()	await sdk.actions.composeCast({ text, embeds })	
useAddFrame()	await sdk.actions.addMiniApp()	
usePrimaryButton(opts, cb)	await sdk.actions.setPrimaryButton(opts)	No callback
useAuthenticate()	sdk.quickAuth.getToken()	See AUTH.md
Context Access Pattern
// WRONG
const fid = sdk.context?.user?.fid;

// CORRECT
const context = await sdk.context;
const fid = context?.user?.fid;


In React components, use state:

const [context, setContext] = useState(null);

useEffect(() => {
  const load = async () => {
    const ctx = await sdk.context;
    setContext(ctx);
  };
  load();
}, []);

Conversion Workflow
Verify Node.js >= 22.11.0
Update dependencies — see DEPENDENCIES.md
Replace imports: @coinbase/onchainkit/minikit → @farcaster/miniapp-sdk
Convert hooks using reference above
Add FrameProvider — see PROVIDER.md
Update manifest: frame → miniapp — see MANIFEST.md
Common Errors

"Property 'user' does not exist on type 'Promise'" → Await sdk.context before accessing properties

"Expected 0 arguments, but got 1" → Remove parameters from sdk.isInMiniApp()

Context is null in components → Ensure FrameProvider is in your provider chain

References
MAPPING.md — Complete hook-by-hook conversion reference
EXAMPLES.md — Before/after code examples
PROVIDER.md — Provider setup with FrameProvider
PITFALLS.md — Common errors and solutions
DEPENDENCIES.md — Package updates
AUTH.md — Quick Auth migration
MANIFEST.md — farcaster.json changes
Weekly Installs
196
Repository
base/skills
GitHub Stars
66
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass