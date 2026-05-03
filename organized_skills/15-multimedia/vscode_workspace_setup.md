---
rating: ⭐⭐⭐
title: vscode-workspace-setup
url: https://skills.sh/patricio0312rev/skills/vscode-workspace-setup
---

# vscode-workspace-setup

skills/patricio0312rev/skills/vscode-workspace-setup
vscode-workspace-setup
Installation
$ npx skills add https://github.com/patricio0312rev/skills --skill vscode-workspace-setup
SKILL.md
VS Code Workspace Setup

Configure VS Code for optimal team productivity and consistency.

Core Workflow
Create workspace settings: .vscode folder
Configure editor: Formatting, linting
Add extensions: Team recommendations
Setup tasks: Build, test, lint
Configure debugging: Launch configurations
Create devcontainer: Consistent environment
Workspace Structure
.vscode/
├── settings.json        # Workspace settings
├── extensions.json      # Recommended extensions
├── tasks.json          # Build tasks
├── launch.json         # Debug configurations
└── snippets/           # Custom snippets
    └── typescript.json

Workspace Settings
// .vscode/settings.json
{
  // Editor settings
  "editor.formatOnSave": true,
  "editor.formatOnPaste": false,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": "explicit",
    "source.organizeImports": "never"
  },
  "editor.tabSize": 2,
  "editor.insertSpaces": true,
  "editor.detectIndentation": false,
  "editor.rulers": [100],
  "editor.wordWrap": "off",
  "editor.minimap.enabled": false,
  "editor.bracketPairColorization.enabled": true,
  "editor.guides.bracketPairs": "active",
  "editor.inlineSuggest.enabled": true,
  "editor.quickSuggestions": {
    "strings": true
  },

  // Files
  "files.trimTrailingWhitespace": true,
  "files.insertFinalNewline": true,
  "files.trimFinalNewlines": true,
  "files.exclude": {
    "**/node_modules": true,
    "**/.git": true,
    "**/.DS_Store": true,
    "**/dist": true,
    "**/.next": true,
    "**/coverage": true
  },
  "files.watcherExclude": {
    "**/node_modules/**": true,
    "**/.git/objects/**": true,
    "**/dist/**": true,
    "**/.next/**": true
  },
  "files.associations": {
    "*.css": "tailwindcss"
  },

  // Search
  "search.exclude": {
    "**/node_modules": true,
    "**/dist": true,
    "**/.next": true,
    "**/coverage": true,
    "pnpm-lock.yaml": true,
    "package-lock.json": true
  },

  // TypeScript
  "typescript.preferences.importModuleSpecifier": "relative",
  "typescript.preferences.quoteStyle": "single",
  "typescript.suggest.autoImports": true,
  "typescript.updateImportsOnFileMove.enabled": "always",
  "typescript.inlayHints.parameterNames.enabled": "literals",
  "typescript.inlayHints.functionLikeReturnTypes.enabled": true,
  "typescript.tsdk": "node_modules/typescript/lib",

  // JavaScript
  "javascript.preferences.importModuleSpecifier": "relative",
  "javascript.preferences.quoteStyle": "single",
  "javascript.updateImportsOnFileMove.enabled": "always",

  // ESLint
  "eslint.validate": [
    "javascript",
    "javascriptreact",
    "typescript",
    "typescriptreact"
  ],
  "eslint.workingDirectories": [{ "mode": "auto" }],
  "eslint.codeActionsOnSave.mode": "problems",

  // Prettier
  "[typescript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[typescriptreact]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[javascript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[json]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[jsonc]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[markdown]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "editor.wordWrap": "on"
  },
  "[css]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[html]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },

  // Tailwind CSS
  "tailwindCSS.experimental.classRegex": [
    ["clsx\\(([^)]*)\\)", "(?:'|\"|`)([^']*)(?:'|\"|`)"],
    ["cn\\(([^)]*)\\)", "(?:'|\"|`)([^']*)(?:'|\"|`)"],
    ["cva\\(([^)]*)\\)", "[\"'`]([^\"'`]*).*?[\"'`]"]
  ],
  "tailwindCSS.includeLanguages": {
    "typescript": "javascript",
    "typescriptreact": "javascript"
  },

  // Git
  "git.autofetch": true,
  "git.confirmSync": false,
  "git.enableSmartCommit": true,
  "git.inputValidation": true,

  // Terminal
  "terminal.integrated.defaultProfile.osx": "zsh",
  "terminal.integrated.fontSize": 13,
  "terminal.integrated.scrollback": 10000,

  // Explorer
  "explorer.compactFolders": false,
  "explorer.fileNesting.enabled": true,
  "explorer.fileNesting.patterns": {
    "package.json": "package-lock.json, yarn.lock, pnpm-lock.yaml, .npmrc",
    "tsconfig.json": "tsconfig.*.json",
    ".eslintrc*": ".eslintignore, .prettierrc*, .prettierignore",
    "*.ts": "${capture}.test.ts, ${capture}.spec.ts",
    "*.tsx": "${capture}.test.tsx, ${capture}.spec.tsx"
  },

  // Debug
  "debug.javascript.autoAttachFilter": "smart",

  // Testing
  "testing.automaticallyOpenPeekView": "never"
}

Recommended Extensions
// .vscode/extensions.json
{
  "recommendations": [
    // Essential
    "dbaeumer.vscode-eslint",
    "esbenp.prettier-vscode",
    "bradlc.vscode-tailwindcss",

    // TypeScript
    "ms-vscode.vscode-typescript-next",
    "yoavbls.pretty-ts-errors",

    // React
    "dsznajder.es7-react-js-snippets",
    "burkeholland.simple-react-snippets",

    // Git
    "eamodio.gitlens",
    "mhutchie.git-graph",

    // Testing
    "vitest.explorer",
    "orta.vscode-jest",

    // Utilities
    "streetsidesoftware.code-spell-checker",
    "christian-kohler.path-intellisense",
    "christian-kohler.npm-intellisense",
    "mikestead.dotenv",
    "EditorConfig.EditorConfig",

    // AI
    "github.copilot",
    "github.copilot-chat",

    // Debugging
    "ms-vscode.js-debug-nightly",

    // Docker
    "ms-azuretools.vscode-docker",
    "ms-vscode-remote.remote-containers"
  ],
  "unwantedRecommendations": [
    "hookyqr.beautify"
  ]
}

Build Tasks
// .vscode/tasks.json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "dev",
      "type": "npm",
      "script": "dev",
      "problemMatcher": [],
      "isBackground": true,
      "presentation": {
        "reveal": "always",
        "panel": "dedicated"
      },
      "group": {
        "kind": "build",
        "isDefault": true
      }
    },
    {
      "label": "build",
      "type": "npm",
      "script": "build",
      "problemMatcher": ["$tsc"],
      "presentation": {
        "reveal": "always"
      },
      "group": "build"
    },
    {
      "label": "test",
      "type": "npm",
      "script": "test",
      "problemMatcher": [],
      "presentation": {
        "reveal": "always"
      },
      "group": "test"
    },
    {
      "label": "test:watch",
      "type": "npm",
      "script": "test:watch",
      "problemMatcher": [],
      "isBackground": true,
      "presentation": {
        "reveal": "always",
        "panel": "dedicated"
      },
      "group": "test"
    },
    {
      "label": "lint",
      "type": "npm",
      "script": "lint",
      "problemMatcher": ["$eslint-stylish"],
      "presentation": {
        "reveal": "never"
      }
    },
    {
      "label": "lint:fix",
      "type": "npm",
      "script": "lint:fix",
      "problemMatcher": ["$eslint-stylish"],
      "presentation": {
        "reveal": "never"
      }
    },
    {
      "label": "typecheck",
      "type": "npm",
      "script": "typecheck",
      "problemMatcher": ["$tsc-watch"],
      "presentation": {
        "reveal": "silent"
      }
    },
    {
      "label": "typecheck:watch",
      "type": "shell",
      "command": "npx tsc --noEmit --watch",
      "problemMatcher": ["$tsc-watch"],
      "isBackground": true,
      "presentation": {
        "reveal": "always",
        "panel": "dedicated"
      }
    }
  ]
}

Debug Configurations
// .vscode/launch.json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Next.js: Debug Server",
      "type": "node-terminal",
      "request": "launch",
      "command": "npm run dev",
      "serverReadyAction": {
        "pattern": "- Local:.+(https?://.+)",
        "uriFormat": "%s",
        "action": "debugWithChrome"
      }
    },
    {
      "name": "Next.js: Debug Full Stack",
      "type": "node-terminal",
      "request": "launch",
      "command": "npm run dev",
      "serverReadyAction": {
        "pattern": "- Local:.+(https?://.+)",
        "uriFormat": "%s",
        "action": "debugWithChrome"
      }
    },
    {
      "name": "Chrome: Debug Client",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:3000",
      "webRoot": "${workspaceFolder}",
      "sourceMaps": true,
      "sourceMapPathOverrides": {
        "webpack://_N_E/*": "${webRoot}/*"
      }
    },
    {
      "name": "Vite: Debug",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:5173",
      "webRoot": "${workspaceFolder}/src",
      "sourceMaps": true
    },
    {
      "name": "Jest: Current File",
      "type": "node",
      "request": "launch",
      "program": "${workspaceFolder}/node_modules/.bin/jest",
      "args": [
        "${relativeFile}",
        "--config",
        "jest.config.js",
        "--runInBand"
      ],
      "console": "integratedTerminal",
      "internalConsoleOptions": "neverOpen"
    },
    {
      "name": "Vitest: Current File",
      "type": "node",
      "request": "launch",
      "program": "${workspaceFolder}/node_modules/.bin/vitest",
      "args": ["run", "${relativeFile}"],
      "console": "integratedTerminal",
      "internalConsoleOptions": "neverOpen"
    },
    {
      "name": "Node: Attach",
      "type": "node",
      "request": "attach",
      "port": 9229,
      "restart": true
    },
    {
      "name": "Node: Current File",
      "type": "node",
      "request": "launch",
      "program": "${file}",
      "runtimeArgs": ["-r", "ts-node/register"],
      "console": "integratedTerminal"
    }
  ],
  "compounds": [
    {
      "name": "Full Stack Debug",
      "configurations": ["Next.js: Debug Server", "Chrome: Debug Client"]
    }
  ]
}

Custom Snippets
// .vscode/snippets/typescript.json
{
  "React Functional Component": {
    "prefix": "rfc",
    "body": [
      "interface ${1:Component}Props {",
      "  $2",
      "}",
      "",
      "export function ${1:Component}({ $3 }: ${1:Component}Props) {",
      "  return (",
      "    <div>",
      "      $0",
      "    </div>",
      "  );",
      "}"
    ],
    "description": "React Functional Component with TypeScript"
  },
  "React useState": {
    "prefix": "us",
    "body": [
      "const [${1:state}, set${1/(.*)/${1:/capitalize}/}] = useState<${2:type}>($3);"
    ],
    "description": "React useState hook"
  },
  "React useEffect": {
    "prefix": "ue",
    "body": [
      "useEffect(() => {",
      "  $1",
      "  return () => {",
      "    $2",
      "  };",
      "}, [$3]);"
    ],
    "description": "React useEffect hook"
  },
  "Console Log": {
    "prefix": "cl",
    "body": ["console.log('${1:label}:', $2);"],
    "description": "Console log with label"
  },
  "Async Function": {
    "prefix": "af",
    "body": [
      "async function ${1:name}(${2:params}): Promise<${3:void}> {",
      "  $0",
      "}"
    ],
    "description": "Async function"
  },
  "Try Catch": {
    "prefix": "tc",
    "body": [
      "try {",
      "  $1",
      "} catch (error) {",
      "  if (error instanceof Error) {",
      "    console.error(error.message);",
      "  }",
      "  throw error;",
      "}"
    ],
    "description": "Try catch with proper error handling"
  },
  "Zod Schema": {
    "prefix": "zod",
    "body": [
      "const ${1:Schema} = z.object({",
      "  ${2:field}: z.${3:string}(),",
      "});",
      "",
      "type ${1:Schema} = z.infer<typeof ${1:Schema}>;"
    ],
    "description": "Zod schema with type inference"
  }
}

Dev Container
// .devcontainer/devcontainer.json
{
  "name": "Node.js Development",
  "image": "mcr.microsoft.com/devcontainers/typescript-node:20",

  // Features to install
  "features": {
    "ghcr.io/devcontainers/features/github-cli:1": {},
    "ghcr.io/devcontainers/features/docker-in-docker:2": {}
  },

  // Forward ports
  "forwardPorts": [3000, 5173],

  // Environment variables
  "containerEnv": {
    "NODE_ENV": "development"
  },

  // Run commands after container is created
  "postCreateCommand": "npm install",

  // VS Code settings for container
  "customizations": {
    "vscode": {
      "settings": {
        "terminal.integrated.defaultProfile.linux": "zsh"
      },
      "extensions": [
        "dbaeumer.vscode-eslint",
        "esbenp.prettier-vscode",
        "bradlc.vscode-tailwindcss",
        "github.copilot"
      ]
    }
  },

  // Mount volumes
  "mounts": [
    "source=${localWorkspaceFolder}/.git,target=/workspaces/${localWorkspaceFolderBasename}/.git,type=bind"
  ],

  // User configuration
  "remoteUser": "node"
}

EditorConfig
# .editorconfig
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true
indent_style = space
indent_size = 2

[*.md]
trim_trailing_whitespace = false

[*.{yml,yaml}]
indent_size = 2

[Makefile]
indent_style = tab

Best Practices
Commit settings: Version control .vscode
Use workspace settings: Not user settings
Recommend extensions: extensions.json
Configure tasks: Common operations
Setup debugging: Launch configurations
Add snippets: Team conventions
Use devcontainers: Consistent environments
File nesting: Clean explorer
Output Checklist

Every VS Code workspace should include:

 Workspace settings.json
 Recommended extensions.json
 Build tasks.json
 Debug launch.json
 Custom snippets
 EditorConfig
 Format on save enabled
 ESLint integration
 Prettier as default formatter
 DevContainer configuration (optional)
Weekly Installs
126
Repository
patricio0312rev/skills
GitHub Stars
35
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass