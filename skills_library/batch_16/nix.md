---
title: nix
url: https://skills.sh/shakhzodkudratov/nixos-and-flakes-skill/nix
---

# nix

skills/shakhzodkudratov/nixos-and-flakes-skill/nix
nix
Installation
$ npx skills add https://github.com/shakhzodkudratov/nixos-and-flakes-skill --skill nix
SKILL.md
Nix Ecosystem Guide
Core Philosophy
Declarative over Imperative - Describe desired state, not steps to reach it
Reproducibility - Lock files (flake.lock) pin exact versions
Immutability - Nix Store is read-only; same inputs = same outputs
Rollback (NixOS) - Every generation preserved; instant recovery via boot menu
Flake Structure
{
  description = "My Nix configuration";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.11";
    home-manager = {
      url = "github:nix-community/home-manager/release-24.11";
      inputs.nixpkgs.follows = "nixpkgs";  # CRITICAL: avoid duplicate nixpkgs
    };
    # macOS support
    nix-darwin = {
      url = "github:nix-darwin/nix-darwin/nix-darwin-24.11";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = { self, nixpkgs, home-manager, nix-darwin, ... }@inputs: {
    # NixOS configurations
    nixosConfigurations.hostname = nixpkgs.lib.nixosSystem {
      system = "x86_64-linux";
      modules = [ ./configuration.nix ];
    };

    # macOS configurations
    darwinConfigurations.hostname = nix-darwin.lib.darwinSystem {
      system = "aarch64-darwin";  # or x86_64-darwin for Intel
      modules = [ ./darwin.nix ];
    };

    # Development shells
    devShells.x86_64-linux.default = nixpkgs.legacyPackages.x86_64-linux.mkShell {
      packages = [ /* ... */ ];
    };
  };
}

Essential Patterns
Input Management
inputs = {
  nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.11";
  unstable.url = "github:NixOS/nixpkgs/nixos-unstable";

  # Use parent's nixpkgs to avoid downloading multiple versions
  home-manager.inputs.nixpkgs.follows = "nixpkgs";

  # Non-flake input (config files, etc.)
  private-config = {
    url = "git+ssh://git@github.com/user/config.git";
    flake = false;
  };
};

Module System
# Modules have: imports, options, config
{ config, pkgs, lib, ... }: {
  imports = [ ./hardware.nix ./services.nix ];

  options.myOption = lib.mkOption {
    type = lib.types.bool;
    default = false;
  };

  config = lib.mkIf config.myOption {
    # conditional configuration
  };
}

Priority Control
{
  # lib.mkDefault (priority 1000) - base module defaults
  services.nginx.enable = lib.mkDefault true;

  # Direct assignment (priority 100) - normal config
  services.nginx.enable = true;

  # lib.mkForce (priority 50) - override everything
  services.nginx.enable = lib.mkForce false;
}

Package Customization
{
  # Override function arguments
  pkgs.fcitx5-rime.override { rimeDataPkgs = [ ./custom-rime ]; }

  # Override derivation attributes
  pkgs.hello.overrideAttrs (old: { doCheck = false; })

  # Overlays (global modification)
  nixpkgs.overlays = [
    (final: prev: {
      myPackage = prev.myPackage.override { /* ... */ };
    })
  ];
}

Platform-Specific
NixOS
sudo nixos-rebuild switch --flake .#hostname
sudo nixos-rebuild boot --flake .#hostname    # apply on next boot
sudo nixos-rebuild test --flake .#hostname    # test without boot entry

nix-darwin (macOS)
darwin-rebuild switch --flake .#hostname
# TouchID for sudo:
# security.pam.services.sudo_local.touchIdAuth = true;

Home Manager
# As NixOS/Darwin module:
home-manager.useGlobalPkgs = true;
home-manager.useUserPackages = true;
home-manager.users.username = import ./home.nix;

# Standalone:
home-manager switch --flake .#username@hostname

Commands Reference
Task	Command
Rebuild NixOS	sudo nixos-rebuild switch --flake .#hostname
Rebuild Darwin	darwin-rebuild switch --flake .#hostname
Dev shell	nix develop
Temp package	nix shell nixpkgs#package
Run package	nix run nixpkgs#package
Update all	nix flake update
Update one	nix flake update nixpkgs
GC old gens	sudo nix-collect-garbage -d
List gens	nix profile history --profile /nix/var/nix/profiles/system
Debug build	nixos-rebuild switch --show-trace -L -v
REPL	nix repl then :lf . to load flake
Common Gotchas
Untracked files ignored - git add before any flake command (nix build/run/shell/develop, nixos-rebuild, darwin-rebuild)
allowUnfree fails in devShells - Use nixpkgs-unfree overlay or ~/.config/nixpkgs/config.nix
Duplicate input downloads - Use follows to pin dependencies (most common: inputs.nixpkgs.follows)
Python pip fails - Use venv, poetry2nix, or containers
Downloaded binaries fail - Use FHS environment or nix-ld
Merge conflicts in lists - Use lib.mkBefore/lib.mkAfter for ordering
Build from source unexpectedly - Check if overlays invalidate cache
Development Environments
# In flake.nix outputs:
devShells.x86_64-linux.default = pkgs.mkShell {
  packages = with pkgs; [ nodejs python3 rustc ];

  shellHook = ''
    echo "Dev environment ready"
    export MY_VAR="value"
  '';

  # For C libraries
  LD_LIBRARY_PATH = lib.makeLibraryPath [ pkgs.openssl ];
};

direnv Integration
# .envrc
use flake
# or for unfree: use flake --impure

Debugging
# Verbose rebuild
nixos-rebuild switch --show-trace --print-build-logs --verbose

# Interactive REPL
nix repl
:lf .                    # load current flake
:e pkgs.hello           # open in editor
:b pkgs.hello           # build derivation
inputs.<TAB>            # explore inputs

References

For detailed information, see:

references/nix-language.md - Nix language syntax
references/flakes.md - Flake inputs/outputs details
references/home-manager.md - User environment management
references/nix-darwin.md - macOS configuration
references/nixpkgs-advanced.md - Overlays, overrides, callPackage
references/dev-environments.md - Dev shells, direnv, FHS
references/best-practices.md - Modularization, debugging, deployment
references/templates.md - Ready-to-use flake.nix examples
Weekly Installs
11
Repository
shakhzodkudrato…es-skill
GitHub Stars
1
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn