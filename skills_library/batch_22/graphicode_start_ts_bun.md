---
title: graphicode-start-ts-bun
url: https://skills.sh/sien75/graphicode-skills/graphicode-start-ts-bun
---

# graphicode-start-ts-bun

skills/sien75/graphicode-skills/graphicode-start-ts-bun
graphicode-start-ts-bun
Installation
$ npx skills add https://github.com/sien75/graphicode-skills --skill graphicode-start-ts-bun
SKILL.md

GraphiCode is a programming tool that combines flowcharts with large language model coding.

You are the starter of TypeScript Bun runtime develop environment in GraphiCode. Your responsibility is to start a TypeScript Bun develop environment project.

Steps
1. Get entry file location, state dirs and flow dirs
cat ./graphig.md


The entry file location is in the entryDir field, state dirs are in the stateDirs field, and flow dirs are in the flowDirs field.

2. Write the launcher.ts file

Regardless of whether it already exists, you must refer to the template ./references/launcher.md and create/update <entryDir>/launcher.ts based on the current state and flow setup.

First, list all folder names under each state and flow directory:

ls -d <stateDir1>/*/

ls -d <flowDir1>/*/


Each folder name is the ID. Use it directly for the import:

import stateId1 from '<stateDir1>/stateId1';

import flowId1 from '<flowDir1>/flowId1';


Importing all state and flow files is what causes them to be instantiated.

Then, read the state.graphig.md file under each state directory. Any state whose description is marked with [START] must be enabled at startup:

stateId1.enable(); // assuming stateId1's description contains the [START] marker

Weekly Installs
10
Repository
sien75/graphicode-skills
First Seen
Feb 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass