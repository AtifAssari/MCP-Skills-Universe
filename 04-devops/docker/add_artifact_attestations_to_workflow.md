---
title: add-artifact-attestations-to-workflow
url: https://skills.sh/jim60105/copilot-prompt/add-artifact-attestations-to-workflow
---

# add-artifact-attestations-to-workflow

skills/jim60105/copilot-prompt/add-artifact-attestations-to-workflow
add-artifact-attestations-to-workflow
Installation
$ npx skills add https://github.com/jim60105/copilot-prompt --skill add-artifact-attestations-to-workflow
SKILL.md
Add Artifact Attestations to Workflow

Add SLSA build-provenance attestations to existing GitHub Actions workflows for Docker container images.

Steps

Find existing workflow files in .github/workflows/ that contain docker/build-push-action or similar steps. Note that composite actions may be used — read both the composite action and the calling workflow simultaneously.

Enable OIDC & Attestations permissions In each workflow's top-level permissions: block, grant both the OIDC token and attestations write privileges:

permissions:
  id-token: write
  attestations: write
  contents: read       # (existing)
  packages: write      # (existing)


Log in to container registries Ensure authentication steps exist for each registry you'll attest against. Judge whether there are omissions based on the implemented content, rather than always logging into all registries.

- name: Login to GHCR
  uses: docker/login-action@v3
  with:
    registry: ghcr.io
    username: ${{ github.actor }}
    password: ${{ secrets.GITHUB_TOKEN }}

- name: Login to Docker Hub
  uses: docker/login-action@v3
  with:
    registry: index.docker.io
    username: ${{ secrets.DOCKERHUB_USERNAME }}
    password: ${{ secrets.DOCKERHUB_TOKEN }}

- name: Login to Quay
  uses: docker/login-action@v3
  with:
    registry: quay.io
    username: ${{ secrets.QUAY_USERNAME }}
    password: ${{ secrets.QUAY_TOKEN }}


Build & push image, capturing the digest Use docker/build-push-action@v* with an id to reference its output. Judge tags based on implemented content.

- name: Build and push image
  id: build_push
  uses: docker/build-push-action@v5
  with:
    context: .
    push: true
    tags: |
      ghcr.io/${{ github.repository }}:latest
      index.docker.io/${{ secrets.DOCKERHUB_USERNAME }}/your-repo:latest
      quay.io/${{ github.repository_owner }}/your-repo:latest


Add attestation steps After the build_push step, insert one actions/attest-build-provenance@v3 invocation per registry. The subject-name is the full image name without a tag. The subject-digest comes from the build step's output. Judge which registries to use based on implemented content.

- name: Attest GHCR image
  uses: actions/attest-build-provenance@v3
  with:
    subject-name: ghcr.io/${{ github.repository }}
    subject-digest: ${{ steps.build_push.outputs.digest }}

- name: Attest Docker Hub image
  uses: actions/attest-build-provenance@v3
  with:
    subject-name: index.docker.io/${{ secrets.DOCKERHUB_USERNAME }}/your-repo
    subject-digest: ${{ steps.build_push.outputs.digest }}

- name: Attest Quay image
  uses: actions/attest-build-provenance@v3
  with:
    subject-name: quay.io/${{ github.repository_owner }}/your-repo
    subject-digest: ${{ steps.build_push.outputs.digest }}


Commit changes Write the git commit message in English.

git add .github/workflows/docker_publish.yml # or whatever files you modified
git commit --signoff -m "ci: add build-provenance attestations for container images"


Ask the user to push Tell the user to manually push the changes and verify attestations are created successfully. DO NOT perform a git push.

Weekly Installs
9
Repository
jim60105/copilot-prompt
GitHub Stars
18
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass