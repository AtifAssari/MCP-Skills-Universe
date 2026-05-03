---
title: distributing-tauri-for-windows
url: https://skills.sh/dchuk/claude-code-tauri-skills/distributing-tauri-for-windows
---

# distributing-tauri-for-windows

skills/dchuk/claude-code-tauri-skills/distributing-tauri-for-windows
distributing-tauri-for-windows
Installation
$ npx skills add https://github.com/dchuk/claude-code-tauri-skills --skill distributing-tauri-for-windows
SKILL.md
Distributing Tauri Applications for Windows

This skill covers Windows distribution for Tauri v2 applications, including MSI/NSIS installer creation, customization, and Microsoft Store submission.

Installer Formats Overview

Tauri supports two Windows installer formats:

Format	Extension	Build Platform	Notes
WiX MSI	.msi	Windows only	Traditional Windows installer
NSIS	-setup.exe	Cross-platform	Can build on Linux/macOS
Building Installers
Standard Build (Windows)
npm run tauri build
# or
yarn tauri build
# or
pnpm tauri build
# or
cargo tauri build

Target Architectures
# 64-bit (default)
npm run tauri build -- --target x86_64-pc-windows-msvc

# 32-bit
npm run tauri build -- --target i686-pc-windows-msvc

# ARM64 (requires additional VS build tools)
npm run tauri build -- --target aarch64-pc-windows-msvc

Cross-Platform NSIS Build (Linux/macOS)

NSIS installers can be built on non-Windows systems:

Prerequisites (Linux):

# Install NSIS and build tools (Debian/Ubuntu)
sudo apt install nsis lld llvm clang

# Install Windows Rust target
rustup target add x86_64-pc-windows-msvc

# Install cargo-xwin
cargo install --locked cargo-xwin


Prerequisites (macOS):

# Install via Homebrew
brew install nsis llvm

# Add LLVM to PATH
export PATH="/opt/homebrew/opt/llvm/bin:$PATH"

# Install Windows Rust target
rustup target add x86_64-pc-windows-msvc

# Install cargo-xwin
cargo install --locked cargo-xwin


Build command:

npm run tauri build -- --runner cargo-xwin --target x86_64-pc-windows-msvc

WebView2 Installation Modes

Configure how WebView2 runtime is installed on end-user machines:

Mode	Internet Required	Size Impact	Best For
downloadBootstrapper	Yes	0 MB	Default, smallest installer
embedBootstrapper	Yes	~1.8 MB	Better Windows 7 support
offlineInstaller	No	~127 MB	Offline/air-gapped environments
fixedVersion	No	~180 MB	Controlled enterprise deployment
skip	No	0 MB	Not recommended
Configuration
{
  "bundle": {
    "windows": {
      "webviewInstallMode": {
        "type": "embedBootstrapper"  // or: downloadBootstrapper, offlineInstaller, fixedVersion
      }
    }
  }
}


For fixedVersion, add the path: "path": "./WebView2Runtime"

WiX MSI Customization
Custom WiX Template

Replace the default template:

{
  "bundle": {
    "windows": {
      "wix": {
        "template": "./windows/custom-template.wxs"
      }
    }
  }
}

WiX Fragments

Add custom functionality via XML fragments:

1. Create fragment file (src-tauri/windows/fragments/registry.wxs):

<?xml version="1.0" encoding="UTF-8"?>
<Wix xmlns="http://schemas.microsoft.com/wix/2006/wi">
  <Fragment>
    <ComponentGroup Id="MyFragmentRegistryEntries">
      <Component Id="MyRegistryEntry" Directory="INSTALLDIR">
        <RegistryKey Root="HKCU" Key="Software\MyApp">
          <RegistryValue Type="string" Name="InstallPath" Value="[INSTALLDIR]" KeyPath="yes"/>
        </RegistryKey>
      </Component>
    </ComponentGroup>
  </Fragment>
</Wix>


2. Reference in configuration:

{
  "bundle": {
    "windows": {
      "wix": {
        "fragmentPaths": ["./windows/fragments/registry.wxs"],
        "componentRefs": ["MyFragmentRegistryEntries"]
      }
    }
  }
}

Internationalization (WiX)
{
  "bundle": {
    "windows": {
      "wix": {
        "language": ["en-US", "fr-FR", "de-DE"],  // Single: "fr-FR"
        "localePath": "./windows/locales"  // Optional: custom locale files
      }
    }
  }
}

NSIS Installer Customization
Install Modes
Mode	Admin Required	Install Location	Use Case
perUser	No	%LOCALAPPDATA%	Default, no elevation
perMachine	Yes	%PROGRAMFILES%	System-wide install
both	Yes	User choice	Flexible deployment
{
  "bundle": {
    "windows": {
      "nsis": {
        "installMode": "perMachine"
      }
    }
  }
}

Installer Hooks

Extend installation with custom NSIS scripts:

1. Create hooks file (src-tauri/windows/hooks.nsh):

!macro NSIS_HOOK_PREINSTALL
  ; Run before file installation
  DetailPrint "Preparing installation..."
!macroend

!macro NSIS_HOOK_POSTINSTALL
  ; Run after installation completes
  DetailPrint "Configuring application..."
  ; Example: Install VC++ Redistributable
  ReadRegStr $0 HKLM "SOFTWARE\Microsoft\VisualStudio\14.0\VC\Runtimes\x64" "Installed"
  ${If} $0 != "1"
    ExecWait '"$INSTDIR\vc_redist.x64.exe" /quiet /norestart'
  ${EndIf}
!macroend

!macro NSIS_HOOK_PREUNINSTALL
  ; Run before uninstallation
  DetailPrint "Cleaning up..."
!macroend

!macro NSIS_HOOK_POSTUNINSTALL
  ; Run after uninstallation
  DetailPrint "Removal complete"
!macroend


2. Reference in configuration:

{
  "bundle": {
    "windows": {
      "nsis": {
        "installerHooks": "./windows/hooks.nsh"
      }
    }
  }
}

Internationalization (NSIS)

NSIS installers support multiple languages in a single file:

{
  "bundle": {
    "windows": {
      "nsis": {
        "languages": ["English", "French", "German", "Spanish"],
        "displayLanguageSelector": true
      }
    }
  }
}

Minimum WebView2 Version

Require a specific WebView2 version:

{
  "bundle": {
    "windows": {
      "nsis": {
        "minimumWebview2Version": "110.0.1531.0"
      }
    }
  }
}

Complete Configuration Example
{
  "bundle": {
    "active": true,
    "targets": ["msi", "nsis"],
    "icon": ["icons/icon.ico"],
    "windows": {
      "certificateThumbprint": "YOUR_CERTIFICATE_THUMBPRINT",
      "timestampUrl": "http://timestamp.digicert.com",
      "webviewInstallMode": {
        "type": "embedBootstrapper"
      },
      "wix": {
        "language": ["en-US", "de-DE"],
        "fragmentPaths": ["./windows/fragments/registry.wxs"],
        "componentRefs": ["MyRegistryEntries"]
      },
      "nsis": {
        "installMode": "both",
        "installerHooks": "./windows/hooks.nsh",
        "languages": ["English", "German"],
        "displayLanguageSelector": true,
        "minimumWebview2Version": "110.0.1531.0"
      }
    }
  }
}

Special Configurations
Windows 7 Support
{
  "bundle": {
    "windows": {
      "webviewInstallMode": {
        "type": "embedBootstrapper"
      }
    }
  }
}


Enable Windows 7 notification support in Cargo.toml:

[dependencies]
tauri = { version = "2", features = ["windows7-compat"] }

FIPS Compliance

Set environment variable before building:

PowerShell:

$env:TAURI_BUNDLER_WIX_FIPS_COMPLIANT = "true"
npm run tauri build


Command Prompt:

set TAURI_BUNDLER_WIX_FIPS_COMPLIANT=true
npm run tauri build

Microsoft Store Distribution
Requirements
Microsoft account with developer enrollment
Offline installer WebView2 mode (required by Store policy)
Publisher name different from product name
Store-Specific Configuration

Create tauri.microsoftstore.conf.json:

{
  "bundle": {
    "windows": {
      "webviewInstallMode": {
        "type": "offlineInstaller"
      }
    }
  },
  "identifier": "com.yourcompany.yourapp",
  "publisher": "Your Company Name"
}

Generate Store Icons
npm run tauri icon /path/to/app-icon.png


This generates all required icon sizes including Microsoft Store assets.

Build for Store
npm run tauri build -- --config tauri.microsoftstore.conf.json

Submission Process
Build with offline installer configuration
Sign installer with valid code signing certificate
Create app listing in Partner Center (Apps and Games)
Reserve unique app name
Upload installer to distribution service
Link installer URL in Store listing
Submit for certification
Publisher Name Constraint

Your publisher name cannot match your product name. If your bundle identifier is com.myapp.myapp, explicitly set a different publisher:

{
  "identifier": "com.myapp.myapp",
  "publisher": "MyApp Software Inc"
}

Code Signing
Using Certificate Thumbprint
{
  "bundle": {
    "windows": {
      "certificateThumbprint": "YOUR_CERTIFICATE_THUMBPRINT",
      "timestampUrl": "http://timestamp.digicert.com"
    }
  }
}

Environment Variables
# Certificate path
export TAURI_SIGNING_PRIVATE_KEY_PASSWORD="your-password"

# Or via tauri.conf.json

Timestamp Servers

Common timestamp servers:

DigiCert: http://timestamp.digicert.com
Sectigo: http://timestamp.sectigo.com
GlobalSign: http://timestamp.globalsign.com/tsa/r6advanced1
Troubleshooting
MSI Build Fails on Non-Windows

MSI files can only be built on Windows using WiX Toolset. Use NSIS for cross-platform builds.

WebView2 Not Installing
Check webview install mode configuration
Verify internet connectivity for bootstrapper modes
For offline mode, ensure installer size is acceptable
NSIS Cross-Compilation Errors
Verify NSIS is installed and in PATH
Check LLVM/clang installation
Ensure Windows Rust target is installed
Verify cargo-xwin is installed
Certificate Not Found
Verify certificate is installed in Windows certificate store
Check thumbprint matches exactly (no spaces)
Ensure certificate has private key access
Weekly Installs
73
Repository
dchuk/claude-co…i-skills
GitHub Stars
18
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass