---
rating: ⭐⭐⭐
title: graphicode-init
url: https://skills.sh/sien75/graphicode-skills/graphicode-init
---

# graphicode-init

skills/sien75/graphicode-skills/graphicode-init
graphicode-init
Installation
$ npx skills add https://github.com/sien75/graphicode-skills --skill graphicode-init
SKILL.md

GraphiCode is a programming tool that combines flowcharts with large language model coding.

This init skill is responsible for initializing a GraphiCode-managed project by collecting project information, creating graphig.md, and setting up the required directory structure.

Steps
0. Check if graphig.md already exists
cat ./graphig.md


If graphig.md already exists, inform the user that the project is already initialized and exit immediately.

1. Collect project information from the user

Ask the user for the following fields (all at once):

appName — the application name
language — the programming language
devEnv — the development environment
runtimeEnv — the runtime environment
2. Gather more info

Read ./references/config-example.md from this skill's directory to get the typical language & devEnv & runtimeEnv options for the chosen runtime and their corresponding values.

If the user's provided language, devEnv, or runtimeEnv does not match any entry in the reference file, prompt the user to revise their input before proceeding.

First show the typical value in config-example, and ask user if want to change some value.

After user confirmed, do the next step.

3. Create graphig.md

Create graphig.md in the project root, combining the user's input from step 1 and the values looked up from the language reference file:

cat << 'EOF' > ./graphig.md
# <appName>

xx config:

* xxx
* xxx
* xxx

xx config:

* xxx
* xxx
* xxx

EOF

4. Create directory structure

For each directory in flowDirs/algorithmDirs/stateDirs in graphig.md:

Create the directory (including parent directories if needed).
Create an empty dir config file inside it:
# for each flowDir
mkdir -p <flowDir> && echo '# flow' > <flowDir>/flow.graphig.md
# for each algorithmDir
mkdir -p <algorithmDir> && echo '# algorithm' > <algorithmDir>/algorithm.graphig.md
# for each stateDir
mkdir -p <stateDir> && echo '# state' > <stateDir>/state.graphig.md

5. Copy utility files

Copy the language-specific utility files from this skill's assets directory to the project's :

mkdir -p ./graphicode-utils
cp <this-skill-dir>/assets/<language>/* <utilsDir>


Replace <language> and <utilsDir> with the value of corresponding value in graphig.md.

6. Confirm to the user

After all files and directories are created, print a summary of what was created and confirm the initialization is complete.

Others

Remember to respond in the language the user uses.

Write file content (descriptions, READMEs, comments) in the writingLanguage configured in graphig.md.

Weekly Installs
30
Repository
sien75/graphicode-skills
First Seen
Feb 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass