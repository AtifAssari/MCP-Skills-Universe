---
rating: ⭐⭐⭐
title: eslint-prettier-config
url: https://skills.sh/patricio0312rev/skills/eslint-prettier-config
---

# eslint-prettier-config

skills/patricio0312rev/skills/eslint-prettier-config
eslint-prettier-config
Installation
$ npx skills add https://github.com/patricio0312rev/skills --skill eslint-prettier-config
Summary

ESLint and Prettier configuration for TypeScript, React, and modern JavaScript projects.

Supports both ESLint v9 flat config and legacy .eslintrc format, with TypeScript, React, React Hooks, and import ordering rules built in
Includes Prettier integration with conflict resolution, VS Code settings, and pre-commit validation via Husky and lint-staged
Provides framework-specific configurations for Next.js and Node.js/API projects, plus examples of custom ESLint rules
Covers full workflow setup: dependency installation, linting and formatting scripts, Git hooks, and commitlint for conventional commits
SKILL.md
ESLint & Prettier Configuration

Setup consistent code quality and formatting with ESLint and Prettier.

Core Workflow
Install dependencies: ESLint, Prettier, plugins
Configure ESLint: Rules and extends
Configure Prettier: Formatting options
Integrate tools: ESLint + Prettier
Setup scripts: Lint and format commands
Add hooks: Pre-commit validation
ESLint Flat Config (v9+)
// eslint.config.mjs
import js from '@eslint/js';
import typescript from '@typescript-eslint/eslint-plugin';
import tsParser from '@typescript-eslint/parser';
import react from 'eslint-plugin-react';
import reactHooks from 'eslint-plugin-react-hooks';
import reactRefresh from 'eslint-plugin-react-refresh';
import importPlugin from 'eslint-plugin-import';
import prettier from 'eslint-config-prettier';

export default [
  // Ignore patterns
  {
    ignores: [
      '**/node_modules/**',
      '**/dist/**',
      '**/build/**',
      '**/.next/**',
      '**/coverage/**',
      '**/*.config.js',
      '**/*.config.mjs',
    ],
  },

  // Base JavaScript config
  js.configs.recommended,

  // TypeScript files
  {
    files: ['**/*.ts', '**/*.tsx'],
    languageOptions: {
      parser: tsParser,
      parserOptions: {
        ecmaVersion: 'latest',
        sourceType: 'module',
        ecmaFeatures: {
          jsx: true,
        },
        project: './tsconfig.json',
      },
    },
    plugins: {
      '@typescript-eslint': typescript,
      'import': importPlugin,
    },
    rules: {
      // TypeScript rules
      ...typescript.configs.recommended.rules,
      '@typescript-eslint/no-unused-vars': ['error', {
        argsIgnorePattern: '^_',
        varsIgnorePattern: '^_',
      }],
      '@typescript-eslint/no-explicit-any': 'warn',
      '@typescript-eslint/explicit-function-return-type': 'off',
      '@typescript-eslint/explicit-module-boundary-types': 'off',
      '@typescript-eslint/no-non-null-assertion': 'warn',
      '@typescript-eslint/consistent-type-imports': ['error', {
        prefer: 'type-imports',
        fixStyle: 'inline-type-imports',
      }],

      // Import rules
      'import/order': ['error', {
        groups: [
          'builtin',
          'external',
          'internal',
          ['parent', 'sibling'],
          'index',
          'type',
        ],
        'newlines-between': 'always',
        alphabetize: { order: 'asc', caseInsensitive: true },
      }],
      'import/no-duplicates': 'error',
    },
  },

  // React files
  {
    files: ['**/*.tsx', '**/*.jsx'],
    plugins: {
      'react': react,
      'react-hooks': reactHooks,
      'react-refresh': reactRefresh,
    },
    settings: {
      react: {
        version: 'detect',
      },
    },
    rules: {
      ...react.configs.recommended.rules,
      ...reactHooks.configs.recommended.rules,
      'react/react-in-jsx-scope': 'off',
      'react/prop-types': 'off',
      'react/jsx-uses-react': 'off',
      'react/jsx-no-target-blank': 'error',
      'react/self-closing-comp': 'error',
      'react/jsx-curly-brace-presence': ['error', {
        props: 'never',
        children: 'never',
      }],
      'react-hooks/rules-of-hooks': 'error',
      'react-hooks/exhaustive-deps': 'warn',
      'react-refresh/only-export-components': ['warn', {
        allowConstantExport: true,
      }],
    },
  },

  // Test files
  {
    files: ['**/*.test.ts', '**/*.test.tsx', '**/*.spec.ts', '**/*.spec.tsx'],
    rules: {
      '@typescript-eslint/no-explicit-any': 'off',
      '@typescript-eslint/no-non-null-assertion': 'off',
    },
  },

  // Disable rules that conflict with Prettier
  prettier,
];

ESLint Legacy Config (.eslintrc)
// .eslintrc.json
{
  "root": true,
  "env": {
    "browser": true,
    "es2022": true,
    "node": true
  },
  "extends": [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:@typescript-eslint/recommended-type-checked",
    "plugin:react/recommended",
    "plugin:react-hooks/recommended",
    "plugin:import/recommended",
    "plugin:import/typescript",
    "plugin:jsx-a11y/recommended",
    "prettier"
  ],
  "parser": "@typescript-eslint/parser",
  "parserOptions": {
    "ecmaVersion": "latest",
    "sourceType": "module",
    "ecmaFeatures": {
      "jsx": true
    },
    "project": ["./tsconfig.json"]
  },
  "plugins": [
    "@typescript-eslint",
    "react",
    "react-hooks",
    "import",
    "jsx-a11y"
  ],
  "settings": {
    "react": {
      "version": "detect"
    },
    "import/resolver": {
      "typescript": {
        "alwaysTryTypes": true
      }
    }
  },
  "rules": {
    // TypeScript
    "@typescript-eslint/no-unused-vars": ["error", {
      "argsIgnorePattern": "^_",
      "varsIgnorePattern": "^_"
    }],
    "@typescript-eslint/consistent-type-imports": ["error", {
      "prefer": "type-imports",
      "fixStyle": "inline-type-imports"
    }],
    "@typescript-eslint/no-explicit-any": "warn",
    "@typescript-eslint/no-floating-promises": "error",
    "@typescript-eslint/await-thenable": "error",

    // React
    "react/react-in-jsx-scope": "off",
    "react/prop-types": "off",
    "react/self-closing-comp": "error",

    // Imports
    "import/order": ["error", {
      "groups": ["builtin", "external", "internal", "parent", "sibling", "index", "type"],
      "newlines-between": "always",
      "alphabetize": { "order": "asc" }
    }],
    "import/no-duplicates": "error",
    "import/no-unresolved": "error",

    // General
    "no-console": ["warn", { "allow": ["warn", "error"] }],
    "prefer-const": "error",
    "no-var": "error"
  },
  "overrides": [
    {
      "files": ["*.test.ts", "*.test.tsx", "*.spec.ts", "*.spec.tsx"],
      "rules": {
        "@typescript-eslint/no-explicit-any": "off",
        "@typescript-eslint/no-floating-promises": "off"
      }
    }
  ],
  "ignorePatterns": [
    "node_modules",
    "dist",
    "build",
    ".next",
    "coverage"
  ]
}

Prettier Configuration
// .prettierrc
{
  "semi": true,
  "singleQuote": true,
  "trailingComma": "es5",
  "tabWidth": 2,
  "useTabs": false,
  "printWidth": 100,
  "bracketSpacing": true,
  "bracketSameLine": false,
  "arrowParens": "always",
  "endOfLine": "lf",
  "quoteProps": "as-needed",
  "jsxSingleQuote": false,
  "proseWrap": "preserve",
  "htmlWhitespaceSensitivity": "css",
  "embeddedLanguageFormatting": "auto"
}

// .prettierignore
node_modules
dist
build
.next
coverage
*.min.js
*.min.css
pnpm-lock.yaml
package-lock.json
yarn.lock

Package Dependencies
// package.json (partial)
{
  "scripts": {
    "lint": "eslint . --ext .ts,.tsx --max-warnings 0",
    "lint:fix": "eslint . --ext .ts,.tsx --fix",
    "format": "prettier --write \"**/*.{ts,tsx,json,md,css}\"",
    "format:check": "prettier --check \"**/*.{ts,tsx,json,md,css}\"",
    "typecheck": "tsc --noEmit",
    "check": "npm run typecheck && npm run lint && npm run format:check"
  },
  "devDependencies": {
    "@eslint/js": "^9.0.0",
    "@typescript-eslint/eslint-plugin": "^7.0.0",
    "@typescript-eslint/parser": "^7.0.0",
    "eslint": "^9.0.0",
    "eslint-config-prettier": "^9.1.0",
    "eslint-import-resolver-typescript": "^3.6.0",
    "eslint-plugin-import": "^2.29.0",
    "eslint-plugin-jsx-a11y": "^6.8.0",
    "eslint-plugin-react": "^7.33.0",
    "eslint-plugin-react-hooks": "^4.6.0",
    "eslint-plugin-react-refresh": "^0.4.0",
    "prettier": "^3.2.0",
    "typescript": "^5.3.0"
  }
}

Git Hooks with Husky
# Install Husky
npm install -D husky lint-staged
npx husky init

// package.json
{
  "lint-staged": {
    "*.{ts,tsx}": [
      "eslint --fix --max-warnings 0",
      "prettier --write"
    ],
    "*.{json,md,css,scss}": [
      "prettier --write"
    ]
  }
}

# .husky/pre-commit
npx lint-staged

# .husky/commit-msg
npx commitlint --edit $1

Commitlint Configuration
// commitlint.config.js
module.exports = {
  extends: ['@commitlint/config-conventional'],
  rules: {
    'type-enum': [
      2,
      'always',
      [
        'feat',     // New feature
        'fix',      // Bug fix
        'docs',     // Documentation
        'style',    // Formatting
        'refactor', // Code restructuring
        'perf',     // Performance
        'test',     // Tests
        'build',    // Build system
        'ci',       // CI configuration
        'chore',    // Maintenance
        'revert',   // Revert changes
      ],
    ],
    'subject-case': [2, 'always', 'lower-case'],
    'subject-max-length': [2, 'always', 72],
    'body-max-line-length': [2, 'always', 100],
  },
};

VS Code Integration
// .vscode/settings.json
{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": "explicit",
    "source.organizeImports": "never"
  },
  "[typescript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[typescriptreact]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[json]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "eslint.validate": [
    "javascript",
    "javascriptreact",
    "typescript",
    "typescriptreact"
  ],
  "typescript.preferences.importModuleSpecifier": "relative",
  "typescript.suggest.autoImports": true
}

// .vscode/extensions.json
{
  "recommendations": [
    "dbaeumer.vscode-eslint",
    "esbenp.prettier-vscode",
    "bradlc.vscode-tailwindcss",
    "streetsidesoftware.code-spell-checker"
  ]
}

Next.js Specific
// .eslintrc.js (Next.js)
module.exports = {
  extends: [
    'next/core-web-vitals',
    'plugin:@typescript-eslint/recommended',
    'prettier',
  ],
  parser: '@typescript-eslint/parser',
  plugins: ['@typescript-eslint'],
  rules: {
    '@typescript-eslint/no-unused-vars': ['error', { argsIgnorePattern: '^_' }],
    '@typescript-eslint/consistent-type-imports': 'error',
    'import/order': ['error', {
      groups: ['builtin', 'external', 'internal', 'parent', 'sibling', 'index'],
      'newlines-between': 'always',
    }],
  },
};

Node.js/API Specific
// eslint.config.mjs (Node.js API)
import js from '@eslint/js';
import typescript from '@typescript-eslint/eslint-plugin';
import tsParser from '@typescript-eslint/parser';
import nodePlugin from 'eslint-plugin-n';
import prettier from 'eslint-config-prettier';

export default [
  js.configs.recommended,
  {
    files: ['**/*.ts'],
    languageOptions: {
      parser: tsParser,
      parserOptions: {
        project: './tsconfig.json',
      },
    },
    plugins: {
      '@typescript-eslint': typescript,
      'n': nodePlugin,
    },
    rules: {
      ...typescript.configs.recommended.rules,
      'n/no-process-exit': 'error',
      'n/no-unsupported-features/es-syntax': 'off',
      '@typescript-eslint/no-floating-promises': 'error',
      '@typescript-eslint/require-await': 'error',
    },
  },
  prettier,
];

Custom Rules Examples
// Custom ESLint rule example (eslint-plugin-custom/no-direct-env.js)
module.exports = {
  meta: {
    type: 'problem',
    docs: {
      description: 'Disallow direct process.env access',
    },
    messages: {
      noDirectEnv: 'Use config module instead of direct process.env access',
    },
  },
  create(context) {
    return {
      MemberExpression(node) {
        if (
          node.object.type === 'MemberExpression' &&
          node.object.object.name === 'process' &&
          node.object.property.name === 'env'
        ) {
          context.report({
            node,
            messageId: 'noDirectEnv',
          });
        }
      },
    };
  },
};

Best Practices
Extend carefully: Order matters in extends
Use type-checking: Enable type-aware rules
Consistent imports: Enforce import ordering
Prettier last: Always extend prettier last
Auto-fix on save: Configure VS Code
Pre-commit hooks: Validate before commit
CI validation: Run lint in CI pipeline
Progressive adoption: Start with warnings
Output Checklist

Every ESLint/Prettier setup should include:

 ESLint configuration (flat or legacy)
 TypeScript-ESLint integration
 React/React Hooks rules
 Import ordering rules
 Prettier configuration
 ESLint-Prettier integration
 VS Code settings
 Husky pre-commit hooks
 lint-staged configuration
 CI lint validation
 Ignore patterns
 npm scripts for lint/format
Weekly Installs
513
Repository
patricio0312rev/skills
GitHub Stars
35
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass