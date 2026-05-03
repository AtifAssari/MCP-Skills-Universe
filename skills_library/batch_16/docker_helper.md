---
title: docker-helper
url: https://skills.sh/1mangesh1/dev-skills-collection/docker-helper
---

# docker-helper

skills/1mangesh1/dev-skills-collection/docker-helper
docker-helper
Installation
$ npx skills add https://github.com/1mangesh1/dev-skills-collection --skill docker-helper
SKILL.md
Docker Helper
Dockerfile Best Practices
Layer Caching and .dockerignore

Order instructions from least to most frequently changing. Copy dependency manifests before source code.

FROM node:20-alpine
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --omit=dev
COPY . .
CMD ["node", "server.js"]


Always include a .dockerignore to reduce build context and prevent secret leaks:

node_modules
.git
.env
*.log
dist
__pycache__
.venv

Health Checks
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD wget -qO- http://localhost:3000/health || exit 1

Image Management
docker build -t myapp:latest .
docker build -t myapp:v1.2 -f Dockerfile.prod --build-arg NODE_ENV=production .
docker build --no-cache -t myapp:latest .

docker tag myapp:latest registry.example.com/myapp:v1.2
docker push registry.example.com/myapp:v1.2
docker pull registry.example.com/myapp:v1.2

docker images
docker images --filter "dangling=true"
docker image ls --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}"
docker history myapp:latest

docker rmi myapp:latest
docker image prune -a

Container Lifecycle
# Run (create + start)
docker run -d --name myapp -p 8080:80 nginx
docker run -it --rm ubuntu bash
docker run -d --restart unless-stopped myapp

# Start / stop / restart
docker start myapp
docker stop myapp
docker restart myapp

# Remove
docker rm myapp
docker rm -f myapp

# List
docker ps                  # Running
docker ps -a               # All

# Logs
docker logs myapp
docker logs -f --tail 200 myapp
docker logs --since 10m myapp

# Execute inside a running container
docker exec -it myapp bash
docker exec -it myapp sh   # Alpine
docker exec myapp cat /etc/os-release

Networking
docker network ls
docker network create mynet

# Containers on the same custom network resolve each other by name
docker run -d --name api --network mynet myapi:latest
docker run -d --name db --network mynet postgres:16
# From api, reach db at hostname "db": postgresql://user:pass@db:5432/mydb

docker network connect mynet myapp
docker network disconnect mynet myapp
docker network inspect mynet

# Port mapping
docker run -d -p 8080:80 nginx               # Host 8080 -> container 80
docker run -d -p 127.0.0.1:8080:80 nginx     # Bind to localhost only
docker run -d -P nginx                        # All exposed -> random host ports

# Host networking (Linux only, container shares host network stack)
docker run -d --network host nginx

Volumes and Bind Mounts
# Named volume
docker volume create mydata
docker run -d -v mydata:/var/lib/data myapp

# Bind mount
docker run -d -v $(pwd)/src:/app/src myapp
docker run -d -v $(pwd)/config.yaml:/app/config.yaml:ro myapp

# tmpfs (in-memory, never written to disk)
docker run -d --tmpfs /tmp:rw,size=64m myapp

docker volume ls
docker volume inspect mydata
docker volume rm mydata

# Copy files
docker cp myapp:/app/data.json ./
docker cp ./config.yaml myapp:/app/

Environment Variables and Secrets
docker run -e DATABASE_URL=postgres://user:pass@db:5432/app myapp
docker run --env-file .env myapp


BuildKit secrets (never stored in image layers):

docker build --secret id=npmrc,src=$HOME/.npmrc -t myapp .

# syntax=docker/dockerfile:1
RUN --mount=type=secret,id=npmrc,target=/root/.npmrc npm ci

Multi-Stage Build Patterns
Go (scratch)
FROM golang:1.22-alpine AS builder
WORKDIR /src
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o /app .

FROM scratch
COPY --from=builder /app /app
ENTRYPOINT ["/app"]

Python
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN python -m venv /opt/venv && /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

FROM python:3.12-slim
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
WORKDIR /app
COPY . .
USER nobody
CMD ["python", "main.py"]

Node.js
FROM node:20-alpine AS builder
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build && npm prune --omit=dev

FROM node:20-alpine
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/dist ./dist
COPY package.json ./
RUN addgroup -g 1001 appgroup && adduser -S -u 1001 -G appgroup appuser
USER appuser
EXPOSE 3000
CMD ["node", "dist/server.js"]

Java
FROM eclipse-temurin:21-jdk AS builder
WORKDIR /app
COPY build.gradle settings.gradle gradlew ./
COPY gradle ./gradle
RUN ./gradlew dependencies --no-daemon
COPY src ./src
RUN ./gradlew bootJar --no-daemon

FROM eclipse-temurin:21-jre
COPY --from=builder /app/build/libs/*.jar app.jar
USER 1000
EXPOSE 8080
CMD ["java", "-jar", "app.jar"]

Debugging Containers
docker inspect myapp
docker inspect --format '{{.State.Status}}' myapp
docker inspect --format '{{.State.ExitCode}}' myapp
docker inspect --format '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' myapp

docker stats                     # Live resource usage
docker stats myapp --no-stream   # Single snapshot
docker top myapp                 # Processes inside container
docker diff myapp                # Filesystem changes since start
docker events --filter container=myapp

# Debug sidecar with network tools
docker run -it --rm --pid=container:myapp --network=container:myapp nicolaka/netshoot

Docker Buildx (Multi-Platform)
docker buildx create --name multibuilder --use
docker buildx build --platform linux/amd64,linux/arm64 -t myapp:latest --push .
docker buildx build --platform linux/amd64 -t myapp:latest --load .
docker buildx ls
docker buildx rm multibuilder

Image Optimization
Base Image	Size	Shell	Use Case
ubuntu:22.04	~77 MB	Yes	General purpose
debian:bookworm-slim	~52 MB	Yes	Smaller general purpose
alpine:3.19	~7 MB	Yes	Small images with shell
gcr.io/distroless/base	~20 MB	No	Minimal attack surface
scratch	0 MB	No	Static binaries (Go, Rust)
Combine RUN statements: RUN apt-get update && apt-get install -y pkg && rm -rf /var/lib/apt/lists/*
Remove caches in the same layer they are created.
Use docker history and dive to find large layers.
Security
# Non-root user
RUN addgroup -g 1001 appgroup && adduser -S -u 1001 -G appgroup appuser
USER appuser

# Read-only filesystem
docker run --read-only --tmpfs /tmp myapp

# Drop capabilities
docker run --cap-drop ALL --cap-add NET_BIND_SERVICE myapp

# Prevent privilege escalation
docker run --security-opt no-new-privileges myapp

# Limit resources
docker run --memory 512m --cpus 1.0 myapp


Never use COPY or ENV for secrets. Use BuildKit secret mounts or runtime env vars.

Scanning with Trivy
trivy image myapp:latest
trivy image --severity HIGH,CRITICAL --exit-code 1 myapp:latest
trivy config Dockerfile

Cleanup Commands
docker container prune              # Remove stopped containers
docker image prune -a               # Remove all unused images
docker volume prune                 # Remove unused volumes (data loss risk)
docker network prune                # Remove unused networks
docker system prune -a --volumes    # Remove everything unused
docker system df                    # Check disk usage

Troubleshooting
Container Exits Immediately
docker logs myapp
docker inspect --format '{{.State.ExitCode}}' myapp
# Exit 0:   process completed (not a daemon, or CMD missing)
# Exit 1:   application error
# Exit 137: OOM killed or SIGKILL
# Exit 126: command not executable
# Exit 127: command not found (check CMD/ENTRYPOINT path)

Port Conflicts
lsof -i :8080                       # Find what uses the port
docker run -d -p 9090:80 nginx      # Use a different host port

Permission Issues
COPY --chown=appuser:appgroup . /app

docker run -u $(id -u):$(id -g) -v $(pwd):/app myapp

Container Cannot Resolve Other Containers

Default bridge does not support DNS. Use a user-defined network:

docker network create mynet
docker run -d --name api --network mynet myapi
docker run -d --name db --network mynet postgres:16

Build Context Too Large

Add paths to .dockerignore, or specify a smaller context directory:

docker build -t myapp -f Dockerfile ./src

Weekly Installs
8
Repository
1mangesh1/dev-s…llection
GitHub Stars
3
First Seen
Feb 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass