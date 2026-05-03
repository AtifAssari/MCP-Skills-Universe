---
rating: ⭐⭐
title: lumina-image
url: https://skills.sh/liulixiang1988/agent-skills/lumina-image
---

# lumina-image

skills/liulixiang1988/agent-skills/lumina-image
lumina-image
Installation
$ npx skills add https://github.com/liulixiang1988/agent-skills --skill lumina-image
SKILL.md
Lumina Image Build Commands

You build Lumina-specific container images by sourcing and calling pre-built script functions. Do NOT manually replicate the steps in the scripts — just source and call the function directly.

Build Proxy API Image (Windows Only)

When the user asks to build the proxy API image (e.g., "build proxy api image", "build lumina proxy", "build proxy api"):

if (-not $Env:MS_PATH) { $Env:MS_PATH = Get-Location }
. "<skill-path>/scripts/build-proxy.ps1"; lumina_build_proxy_api_image

Build SandboxControlPlane API Image (Windows Only)

When the user asks to build the SandboxControlPlane API image (e.g., "build scp api image", "build sandboxcontrolplane image", "build scp image", "build sandbox control plane api"):

if (-not $Env:MS_PATH) { $Env:MS_PATH = Get-Location }
. "<skill-path>/scripts/build-proxy.ps1"; lumina_build_scp_api_image

Build Sandbox Agent Image

When the user asks to build the sandbox agent image (e.g., "build sandbox agent", "build sandbox agent image", "build sandbox image"):

Windows (PowerShell):

if (-not $Env:MS_PATH) { $Env:MS_PATH = Get-Location }
. "<skill-path>/scripts/build-proxy.ps1"; sandbox_build_agent_image


macOS/Linux (bash/zsh):

if [ -z "${MS_PATH:-}" ]; then export MS_PATH="$(pwd)"; fi
. "<skill-path>/scripts/build-sandbox-agent.sh"; sandbox_build_agent_image

Replace Kubernetes Deployment Image

When the user asks to replace or update an existing Lumina deployment image in Kubernetes after building an image (for example, replacing the SandboxControlPlane deployment image in AKS), do not change the deployment immediately.

You must first ask the user to confirm the target values for all of the following:

Kube context: Ask the user which kubectx / Kubernetes context to use.
Namespace: Ask the user which namespace to use.
Deployment: Ask the user which deployment to update.
Image: Confirm the exact target image tag that will be applied.

After collecting those values, explicitly ask the user whether to replace the existing deployment image. Only perform the kubectl set image / rollout step after the user confirms.

Recommended execution flow:

Ask the user to choose the kube context.
Ask the user to choose the namespace.
Ask the user to choose the deployment.
Show the exact image that will be used.
Ask for confirmation to replace the existing deployment image.
Only after confirmation, update the deployment image and verify rollout status.

Recommended question template:

I can replace the existing deployment image, but I need you to confirm the target first.

Please choose:
1. kube context
2. namespace
3. deployment

Then I will show the exact image tag and ask for final confirmation before applying the change.


Recommended confirmation template:

I am about to replace the image for deployment <deployment> in namespace <namespace> on context <kube-context>.

Target image:
<image>

Do you want me to replace the existing deployment image now?


Recommended execution commands after confirmation:

kubectl --context <kube-context> -n <namespace> get deployment <deployment> -o json
kubectl --context <kube-context> -n <namespace> set image deployment/<deployment> <container-name>=<image>
kubectl --context <kube-context> -n <namespace> rollout status deployment/<deployment> --timeout=10m
kubectl --context <kube-context> -n <namespace> get pods -l app=<deployment> -o wide


Notes:

Read the deployment first to identify the correct container name before running kubectl set image.
Do not assume the container name is the same as the deployment name.
After rollout, verify that the new pod is running and that the deployment template now points to the requested image.

If the deployment has multiple containers:

List all container names and their current images before making any change.
Show the list to the user and ask which container should be updated.
Do not update multiple containers unless the user explicitly asks for that.
Repeat the final confirmation step with the selected container name included.

Recommended multi-container inspection command:

kubectl --context <kube-context> -n <namespace> get deployment <deployment> -o jsonpath="{range .spec.template.spec.containers[*]}{.name}{'|'}{.image}{'\n'}{end}"


Recommended multi-container question template:

This deployment has multiple containers. Please choose which container to update:

<container-name-1> | <current-image-1>
<container-name-2> | <current-image-2>
<container-name-3> | <current-image-3>


Recommended multi-container confirmation template:

I am about to replace the image for container <container-name> in deployment <deployment> within namespace <namespace> on context <kube-context>.

Current image:
<current-image>

Target image:
<target-image>

Do you want me to replace this container image now?

Prerequisites
MS_PATH: Must point to the CopilotLumina root directory. If not set, the commands above auto-detect it from the current working directory.
ACR Login: If a docker push fails with an authentication error, run az acr login -n luminaacrdev and retry.
<skill-path>: Replace with the actual path to the skill directory containing the scripts folder.
Kubernetes updates: Before replacing a deployment image, ask the user to choose the kube context, namespace, and deployment, then ask for explicit confirmation before applying the change.
Behavior
lumina_build_proxy_api_image remains Windows/PowerShell only.
lumina_build_scp_api_image is Windows/PowerShell only.
sandbox_build_agent_image now supports both Windows (PowerShell) and macOS/Linux (bash/zsh).
All commands build the image, push to ACR, and print the image tag.
For Kubernetes deployment image replacement, the skill must gather the kube context, namespace, and deployment from the user via questions, and must not replace an existing deployment image without explicit user confirmation.
Weekly Installs
12
Repository
liulixiang1988/…t-skills
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass