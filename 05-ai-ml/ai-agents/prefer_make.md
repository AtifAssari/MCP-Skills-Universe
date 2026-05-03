---
rating: ⭐⭐
title: prefer-make
url: https://skills.sh/lwlee2608/agent-skills/prefer-make
---

# prefer-make

skills/lwlee2608/agent-skills/prefer-make
prefer-make
Installation
$ npx skills add https://github.com/lwlee2608/agent-skills --skill prefer-make
SKILL.md
Build with Make

This project uses a Makefile. Always prefer make targets over running go commands directly.

Rules
Check the Makefile first before running any go build, go test, go run, go vet, go fmt, or golangci-lint command. Look for a corresponding target.
Use the Makefile target instead of the raw go command. For example:
make build instead of go build ./...
make test instead of go test ./...
make lint instead of golangci-lint run
make run instead of go run main.go
make fmt instead of go fmt ./...
Run make help to discover targets. If that fails, read the Makefile directly.
Fall back to raw go commands only if no relevant Makefile target exists for the task.
Verification procedure
Before executing, confirm the target exists by checking make help output or the Makefile.
After execution, verify the command exited with status 0 and produced expected output.
Common mistakes to watch for
Assuming target names without checking. Don't guess that make unit-test exists — read the Makefile. Target names vary across projects.
Adding flags to make targets that already set them. For example, running make test ARGS="-v -race" when the Makefile already passes -race. Check what the target does before adding flags.
Running raw go test ./specific/pkg/... for a subset when the Makefile has a target that accepts a package argument (e.g., make test PKG=./specific/pkg/...).
Weekly Installs
24
Repository
lwlee2608/agent-skills
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass