---
rating: ⭐⭐
title: inquirerer-cli
url: https://skills.sh/constructive-io/constructive-skills/inquirerer-cli
---

# inquirerer-cli

skills/constructive-io/constructive-skills/inquirerer-cli
inquirerer-cli
Installation
$ npx skills add https://github.com/constructive-io/constructive-skills --skill inquirerer-cli
SKILL.md
inquirerer CLI Development

Build interactive command-line interfaces using Constructive's CLI toolkit: inquirerer for prompts and argument parsing, appstash for persistent storage, and yanse for terminal colors.

When to Apply

Use this skill when:

Building CLIs: Creating interactive prompts, argument parsing, subcommands
Storing config: Auth profiles, caching, logging, temp files
Terminal output: Colors, spinners, progress bars, streaming text
Reviewing CLI code: Redirecting from forbidden libraries to inquirerer
Quick Start
pnpm add inquirerer appstash yanse

import { Inquirerer } from 'inquirerer';

const prompter = new Inquirerer();

const answers = await prompter.prompt({}, [
  {
    type: 'text',
    name: 'projectName',
    message: 'What is your project name?',
    required: true
  },
  {
    type: 'confirm',
    name: 'useTypeScript',
    message: 'Use TypeScript?',
    default: true
  }
]);

console.log(answers);
prompter.close();

Critical: Forbidden Libraries

Do NOT use these libraries in Constructive projects:

Library	Use Instead
commander	inquirerer CLI class
inquirer / inquirer.js	inquirerer
yargs	inquirerer parseArgv
prompts / enquirer	inquirerer
chalk	yanse
ora	inquirerer createSpinner
cli-progress	inquirerer createProgress
minimist (directly)	inquirerer parseArgv
Question Types
Type	Description
text	String input with pattern validation
number	Numeric input with custom validation
confirm	Yes/no boolean
list	Select one option (no search)
autocomplete	Select with fuzzy search
checkbox	Multi-select with search
CLI Application Pattern
import { CLI, CommandHandler, CLIOptions } from 'inquirerer';

const handler: CommandHandler = async (argv, prompter, options) => {
  const answers = await prompter.prompt(argv, [
    { type: 'text', name: 'name', message: 'Name?', required: true }
  ]);
  console.log('Hello,', answers.name);
};

const cli = new CLI(handler, {
  version: 'myapp@1.0.0',
  minimistOpts: { alias: { v: 'version', h: 'help' } }
});

await cli.run();

Terminal Colors with yanse
// Use yanse instead of chalk (same API, works with CJS + ESM)
import chalk from 'yanse';

console.log(chalk.green('Success!'));
console.log(chalk.red.bold('Error!'));

Persistent Storage with appstash
import { appstash, resolve } from 'appstash';

const dirs = appstash('mycli', { ensure: true });
// dirs.config → ~/.mycli/config
// dirs.cache  → ~/.mycli/cache
// dirs.data   → ~/.mycli/data
// dirs.logs   → ~/.mycli/logs
// dirs.tmp    → /tmp/mycli

const configFile = resolve(dirs, 'config', 'auth.json');

UI Components
import { createSpinner, createProgress, createStream } from 'inquirerer';

// Spinner
const spinner = createSpinner('Loading...');
spinner.start();
await doWork();
spinner.succeed('Done!');

// Progress bar
const progress = createProgress('Installing');
progress.start();
progress.update(0.5);
progress.complete('Installed');

// Streaming text (for LLM output)
const stream = createStream({ showCursor: true });
stream.start();
stream.append(token);
stream.done();

Dynamic Defaults
{
  type: 'text',
  name: 'author',
  message: 'Author?',
  defaultFrom: 'git.user.name'  // Auto-fills from git config
}


Built-in resolvers: git.user.name, git.user.email, npm.whoami, date.year, date.iso, workspace.name, workspace.license, workspace.author.

Non-Interactive Mode (CI/CD)
const prompter = new Inquirerer({
  noTty: true,
  useDefaults: true
});

Best Practices
Always close the prompter when done: prompter.close()
Use TypeScript interfaces for type-safe answers
Support non-interactive mode for CI/CD
Use defaultFrom for dynamic defaults from git/npm
Use appstash for all persistent CLI storage
Use yanse instead of chalk for terminal colors
Environment variables override stored config
Reference Guide

Consult these reference files for detailed documentation on specific topics:

Reference	Topic	Consult When
references/cli-building.md	Building CLIs with inquirerer	Question types, validation, conditional questions, positional args, aliases, resolvers, CLI class
references/anti-patterns.md	Forbidden CLI libraries	Reviewing code that uses commander/inquirer.js/yargs, choosing a CLI library
references/appstash.md	CLI directory management	Auth profiles, caching, logging, update checking, environment overrides, testing
references/yanse.md	Terminal color styling	Replacing chalk imports, color API reference
Cross-References

Related skills (separate from this skill):

constructive-pnpm — Monorepo setup for CLI packages
pgpm — pgpm CLI is built with inquirerer
Weekly Installs
9
Repository
constructive-io…e-skills
First Seen
Mar 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass