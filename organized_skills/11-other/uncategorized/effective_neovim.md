---
rating: ⭐⭐⭐
title: effective-neovim
url: https://skills.sh/kylesnowschwartz/simpleclaude/effective-neovim
---

# effective-neovim

skills/kylesnowschwartz/simpleclaude/effective-neovim
effective-neovim
Installation
$ npx skills add https://github.com/kylesnowschwartz/simpleclaude --skill effective-neovim
SKILL.md
Effective Neovim

Apply best practices from the Neovim community to write clean, idiomatic Lua plugins.

When to Apply

Use this skill automatically when:

Writing new Neovim plugins in Lua
Reviewing Neovim plugin code
Refactoring existing plugin implementations
Tooling

The Type A Neovim developers use:

Tool	Purpose
StyLua	Formatter (opinionated, like prettier)
selene	Linter (30+ checks)
lua-language-server	Type checking via LuaCATS annotations

Neovim's own .stylua.toml:

column_width = 100
indent_type = "Spaces"
indent_width = 2
quote_style = "AutoPreferSingle"

Key Principles

From nvim-best-practices (parts upstreamed to :h lua-plugin):

No forced setup(): Plugins should work out of the box. Separate configuration from initialization.
<Plug> mappings: Let users define their own keymaps instead of hardcoding bindings.
Subcommands over pollution: Use :Rocks install not :RocksInstall, :RocksPrune, etc.
Defer require(): Don't load everything at startup. Require inside command implementations.
LuaCATS annotations: Use type hints; catch bugs in CI with lua-language-server.
Busted over plenary.nvim: For testing. More powerful, standard in broader Lua community.
SemVer: Version your plugins properly. Publish to luarocks.org.
Health checks: Provide lua/{plugin}/health.lua for :checkhealth.
Style Conventions
Indent: 2 spaces (not tabs)
Quotes: Single quotes preferred
Line width: 100 columns
Naming: snake_case for functions and variables, PascalCase for classes/modules
No semicolons: They're unnecessary in Lua
Trailing commas: In multi-line tables for cleaner diffs
Comments: Explain why, not what
Plugin Structure
plugin-name/
├── lua/
│   └── plugin-name/
│       ├── init.lua      # Entry point, setup function
│       ├── health.lua    # :checkhealth integration
│       └── *.lua         # Module files
├── plugin/
│   └── plugin-name.lua   # Auto-loaded, defines commands/autocommands
├── doc/
│   └── plugin-name.txt   # Vimdoc for :h plugin-name
└── tests/
    └── *_spec.lua        # Busted test files

References

For detailed guidance with code examples, see references/nvim-best-practices.md.

External sources:

nvim-best-practices: https://github.com/nvim-neorocks/nvim-best-practices
Neovim Lua Guide: :h lua-guide
Plugin Development: :h lua-plugin
Roblox Style Guide: https://roblox.github.io/lua-style-guide/ (StyLua's basis)
Weekly Installs
31
Repository
kylesnowschwart…leclaude
GitHub Stars
95
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass