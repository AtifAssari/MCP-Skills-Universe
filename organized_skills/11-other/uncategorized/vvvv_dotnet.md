---
rating: ⭐⭐⭐
title: vvvv-dotnet
url: https://skills.sh/tebjan/vvvv-skills/vvvv-dotnet
---

# vvvv-dotnet

skills/tebjan/vvvv-skills/vvvv-dotnet
vvvv-dotnet
Installation
$ npx skills add https://github.com/tebjan/vvvv-skills --skill vvvv-dotnet
SKILL.md
.NET Integration in vvvv gamma
.csproj Configuration for vvvv Plugins

Minimal .csproj for a vvvv gamma C# plugin:

<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <OutputPath Condition="'$(Configuration)'=='Release'">..\..\lib\net8.0\</OutputPath>
    <AppendTargetFrameworkToOutputPath>false</AppendTargetFrameworkToOutputPath>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="VL.Core" Version="2025.7.*" />
    <PackageReference Include="VL.Stride" Version="2025.7.*" />
  </ItemGroup>
</Project>


Key settings:

Target framework: net8.0 (required for vvvv gamma 6+)
Output path: Point to lib/net8.0/ relative to your .vl document
AppendTargetFrameworkToOutputPath: Set to false so DLLs go directly to the output folder
How vvvv Uses C# Code

There are two workflows for integrating C# with a .vl document:

Source project reference (live reload): The .vl document references a .csproj. vvvv compiles .cs source files itself via Roslyn into in-memory assemblies — no dotnet build needed. On every .cs file save, vvvv detects the change and recompiles automatically. The output path in .csproj is not involved during live development; it is used for NuGet packaging and deployment.

Binary reference (no live reload): The .vl document references a pre-compiled DLL or NuGet package. To apply C# changes, rebuild externally (dotnet build) and restart vvvv. This is the standard workflow for larger projects and stable libraries.

Shaders (.sdsl files) always live-reload regardless of workflow.

For AI agents: regardless of workflow, run dotnet build to verify your code compiles — you cannot see vvvv's compiler output. For source project references, vvvv picks up changes on file save automatically (no restart needed). For binary references, dotnet build is required and the user must restart vvvv.

Required Global Usings
global using VL.Core;
global using VL.Core.Import;
global using VL.Lib.Collections;

Required Assembly Attribute

For vvvv to discover your ProcessNodes and static methods:

[assembly: ImportAsIs]


Without this, your nodes will not appear in the vvvv node browser.

NuGet Package Sources

Add these to your NuGet.config for vvvv packages:

<configuration>
  <packageSources>
    <add key="nuget.org" value="https://api.nuget.org/v3/index.json" />
    <add key="vvvv" value="https://teamcity.vvvv.org/guestAuth/app/nuget/v1/FeedService.svc/" />
  </packageSources>
</configuration>

NuGet Packaging

To distribute your plugin as a NuGet package:

nuget pack MyPlugin/deployment/MyPlugin.nuspec


The .nuspec should reference your .vl document, compiled DLLs, shader files, and help patches.

Common VL Packages
Package	Purpose
VL.Core	Core types, ProcessNode attribute, Spread
VL.Stride	3D rendering, shader integration
VL.Stride.Runtime	Stride engine runtime
VL.Core.Import	ImportAsIs attribute
VL.Lib.Collections	Spread, SpreadBuilder
VL.Skia	2D rendering (Skia graphics engine)
VL.Fuse	GPU visual programming (shader graph)
VL.IO.OSC	Open Sound Control protocol
VL.IO.MQTT	MQTT messaging
VL.IO.Redis	Redis key-value store
VL.OpenCV	Computer vision (OpenCV bindings)
VL.MediaPipe	MediaPipe ML pipelines (hand, face, pose)
VL.Audio	Audio synthesis and I/O (NAudio-based)
VL.Devices.AzureKinect	Azure Kinect / Orbbec depth cameras

For a full catalog, see vvvv.org/packs.

Vector Types & SIMD Strategy
Internal hot paths: Use System.Numerics.Vector3/Vector4/Quaternion (SIMD via AVX/SSE)
External API (Update method params): Use Stride.Core.Mathematics types (required by VL)
Zero-cost conversion between them:
using System.Runtime.CompilerServices;

// Stride → System.Numerics (zero-cost reinterpret)
ref var numericsVec = ref Unsafe.As<Stride.Core.Mathematics.Vector3, System.Numerics.Vector3>(ref strideVec);

// System.Numerics → Stride (zero-cost reinterpret)
ref var strideVec = ref Unsafe.As<System.Numerics.Vector3, Stride.Core.Mathematics.Vector3>(ref numericsVec);


These types have identical memory layouts, making Unsafe.As a zero-cost operation.

IDisposable and Resource Management

Any node holding native/unmanaged resources must implement IDisposable:

[ProcessNode]
public class NativeWrapper : IDisposable
{
    private IntPtr _handle;

    public NativeWrapper()
    {
        _handle = NativeLib.Create();
    }

    public void Update(out int result)
    {
        result = NativeLib.Process(_handle);
    }

    public void Dispose()
    {
        if (_handle != IntPtr.Zero)
        {
            NativeLib.Destroy(_handle);
            _handle = IntPtr.Zero;
        }
    }
}


vvvv calls Dispose() when the node is removed or the document closes.

Async Patterns in vvvv

Since Update() runs on the main thread at 60 FPS, long-running operations must be async:

[ProcessNode]
public class AsyncLoader
{
    private Task<string>? _loadTask;
    private string _cachedResult = "";

    public void Update(
        out string result,
        out bool isLoading,
        string url = "",
        bool trigger = false)
    {
        if (trigger && (_loadTask == null || _loadTask.IsCompleted))
        {
            _loadTask = Task.Run(() => LoadFromUrl(url));
        }

        isLoading = _loadTask != null && !_loadTask.IsCompleted;

        if (_loadTask?.IsCompletedSuccessfully == true)
            _cachedResult = _loadTask.Result;

        result = _cachedResult;
    }
}

Blittable Structs for GPU/Network

For data that crosses GPU or network boundaries, use blittable structs:

[StructLayout(LayoutKind.Sequential)]
public struct AnimationBlendState
{
    public int ClipIndex1;      // 4 bytes
    public float ClipTime1;     // 4 bytes
    public int ClipIndex2;      // 4 bytes
    public float ClipTime2;     // 4 bytes
    public float BlendWeight;   // 4 bytes
}


Rules: no reference type fields, no bool (use int), explicit layout. Enables Span<T> access and zero-copy serialization via MemoryMarshal.

Referencing vvvv-Loaded DLLs

When referencing DLLs already loaded by vvvv (e.g., VL.Fuse), use <Private>false</Private> to prevent copying:

<Reference Include="Fuse">
    <HintPath>..\..\path\to\Fuse.dll</HintPath>
    <Private>false</Private>
</Reference>

Build Commands

Build a vvvv plugin project:

dotnet build src/MyPlugin.csproj -c Release


Build an entire solution:

dotnet build src/MyPlugin.sln -c Release

C++/CLI Interop

For wrapping native C/C++ libraries:

msbuild MyCLIWrapper/MyCLIWrapper.vcxproj /p:Configuration=Release /p:Platform=x64


C++/CLI projects require Visual Studio (not dotnet CLI) for building.

Common Package Version Ranges

When referencing vvvv packages, use wildcard versions to stay compatible:

<PackageReference Include="VL.Core" Version="2025.7.*" />


This ensures your plugin works with any patch release of the target vvvv version.

Directory.Build.props

For multi-project solutions, centralize settings:

<Project>
  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <ManagePackageVersionsCentrally>true</ManagePackageVersionsCentrally>
  </PropertyGroup>
</Project>

COM Interop Pitfalls (DX11/DX12)

When working with COM objects (Direct3D, DXGI):

ComPtr<T> is a struct with no finalizer — if it goes out of scope without Dispose(), the COM ref leaks
Always return ComPtrs to pools or explicitly Dispose them
IDXGISwapChain::ResizeBuffers fails if any command list on the queue is in recording state

For forwarding .NET libraries into VL (wrapping without new types, pin modifications, event wrapping), see forwarding.md.

Threading Considerations
Update() is always called on the VL main thread
Use SynchronizationContext to post back to the VL thread from background tasks:
private SynchronizationContext _vlSyncContext;

public MyNode()
{
    _vlSyncContext = SynchronizationContext.Current!;
}

// From background thread:
_vlSyncContext.Post(_ => { /* runs on VL thread */ }, null);

Weekly Installs
46
Repository
tebjan/vvvv-skills
GitHub Stars
23
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass