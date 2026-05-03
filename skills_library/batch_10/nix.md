---
title: nix
url: https://skills.sh/i9wa4/dotfiles/nix
---

# nix

skills/i9wa4/dotfiles/nix
nix
Installation
$ npx skills add https://github.com/i9wa4/dotfiles --skill nix
SKILL.md
Nix Skill
1. nurl

IMPORTANT: nurl generates Nix fetcher calls from repository URLs

nix run 'nixpkgs#nurl' -- https://github.com/rvben/rumdl v0.0.206


IMPORTANT: Output can be used directly in fetchFromGitHub

fetchFromGitHub {
  owner = "rvben";
  repo = "rumdl";
  rev = "v0.0.206";
  hash = "sha256-XXX...";
}


IMPORTANT: For cargoHash/vendorHash, use build error method (nurl does not support these)

Weekly Installs
64
Repository
i9wa4/dotfiles
GitHub Stars
9
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn