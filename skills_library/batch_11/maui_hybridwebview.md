---
title: maui-hybridwebview
url: https://skills.sh/davidortinau/maui-skills/maui-hybridwebview
---

# maui-hybridwebview

skills/davidortinau/maui-skills/maui-hybridwebview
maui-hybridwebview
Installation
$ npx skills add https://github.com/davidortinau/maui-skills --skill maui-hybridwebview
SKILL.md
HybridWebView in .NET MAUI

HybridWebView hosts HTML/JS/CSS content inside a .NET MAUI app with bidirectional C#↔JS communication. It is not a general browser control — it is designed for local web content shipped with the app.

Common gotchas
Issue	Fix
Blank white screen	Web assets missing from Resources/Raw/wwwroot or DefaultFile not set
JS interop silently fails	Missing <script src="_hwv/HybridWebView.js"></script> in HTML
InvokeJavaScriptAsync returns null	Return type missing [JsonSerializable] attribute in JsonSerializerContext
JS → C# calls do nothing	SetInvokeJavaScriptTarget not called before JS invokes C# methods
Serialization crash with trimming	Not using source-generated JsonSerializerContext
⚠️ Bridge script is mandatory

The HTML page must include the bridge script before any app scripts:

<!-- ✅ Correct order -->
<script src="_hwv/HybridWebView.js"></script>
<script src="scripts/app.js"></script>

<!-- ❌ Wrong — app.js loads before bridge, interop calls fail silently -->
<script src="scripts/app.js"></script>
<script src="_hwv/HybridWebView.js"></script>

JSON serialization — every type must be registered

Every parameter type and return type used in InvokeJavaScriptAsync must have a [JsonSerializable] entry:

// ✅ Correct — all interop types registered
[JsonSerializable(typeof(int))]
[JsonSerializable(typeof(string))]
[JsonSerializable(typeof(Person))]
internal partial class MyJsonContext : JsonSerializerContext { }

// ❌ Wrong — adding a new type to interop without registering it
// This causes silent null returns or runtime exceptions


Rule: When you add a new type to the interop surface, you must add a [JsonSerializable(typeof(T))] attribute to the context. Forgetting this is the #1 cause of mysterious interop failures.

SetInvokeJavaScriptTarget — timing matters
// ✅ Set target BEFORE the web page loads and JS calls C#
myHybridWebView.SetInvokeJavaScriptTarget(new MyJsBridge());

// ❌ Setting it after JS already tried to call — calls are lost


⚠️ Call SetInvokeJavaScriptTarget during page construction or OnAppearing, not lazily.

Exception handling (.NET 9+)

JS exceptions thrown during InvokeJavaScriptAsync are forwarded to .NET. Always wrap interop calls:

// ✅ Catches JS errors
try
{
    var result = await myHybridWebView.InvokeJavaScriptAsync<string>(
        "riskyFunction", MyJsonContext.Default.String);
}
catch (Exception ex)
{
    Debug.WriteLine($"JS error: {ex.Message}");
}

// ❌ Unhandled JS exception crashes the interop pipeline
var result = await myHybridWebView.InvokeJavaScriptAsync<string>(
    "riskyFunction", MyJsonContext.Default.String);

Trimming / NativeAOT pitfalls

Trimming is disabled by default in MAUI projects. If you enable it:

⚠️ You must use source-generated JsonSerializerContext (not reflection-based serialization)
⚠️ Set JsonSerializerIsReflectionEnabledByDefault to false
Using JsonSerializerContext as shown above is recommended regardless of trimming settings
<PropertyGroup>
  <PublishTrimmed>true</PublishTrimmed>
  <JsonSerializerIsReflectionEnabledByDefault>false</JsonSerializerIsReflectionEnabledByDefault>
</PropertyGroup>

Decision framework — typed interop vs raw messages
Need	Use
Structured data exchange with type safety	InvokeJavaScriptAsync / InvokeDotNet with JsonSerializerContext
Simple string payloads, fire-and-forget	SendRawMessage / RawMessageReceived
Calling C# from JS with return values	InvokeDotNet (target must be set first)
Multiple JS functions to call	Typed interop — one InvokeJavaScriptAsync per function
Quick checklist
 Web content is under Resources/Raw/wwwroot
 index.html includes <script src="_hwv/HybridWebView.js"></script> before app scripts
 DefaultFile is set (or defaults to index.html)
 Every interop type has a [JsonSerializable] entry in a JsonSerializerContext
 SetInvokeJavaScriptTarget is called before JS invokes C# methods
 InvokeJavaScriptAsync calls are wrapped in try/catch (.NET 9+)
 If trimming enabled: source-generated JSON serialization configured
Weekly Installs
15
Repository
davidortinau/maui-skills
GitHub Stars
130
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass