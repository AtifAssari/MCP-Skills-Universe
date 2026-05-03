---
title: h100-sglang-diffusion
url: https://skills.sh/bbuf/sglang-auto-driven-skills/h100-sglang-diffusion
---

# h100-sglang-diffusion

skills/bbuf/sglang-auto-driven-skills/h100-sglang-diffusion
h100-sglang-diffusion
Installation
$ npx skills add https://github.com/bbuf/sglang-auto-driven-skills --skill h100-sglang-diffusion
SKILL.md
H100 — SGLang Diffusion
Overview

Use this skill to do SGLang diffusion development on the H100 box through h100_sglang. The default container is sglang_bbuf and the repo lives at /data/bbuf/repos/sglang.

Prefer this skill when:

Validating diffusion Triton / CUDA JIT kernels
Running diffusion model smoke tests (DiffGenerator, flux, etc.)
Comparing eager vs torch.compile diffusion performance
Verifying python[diffusion] editable install changes

This environment is already prepared:

sglang_bbuf is running on lmsysorg/sglang:dev
the repo is cloned at /data/bbuf/repos/sglang
editable installs for python[all] and python[diffusion] are already done
/data/.cache is mounted to /root/.cache
Infiniband paths are mounted for RDMA-aware workflows: /sys/class/infiniband, /dev/infiniband, and /usr/sbin/show_gids
Quick Start
Check the host, container, and GPU state.
ssh h100_sglang 'hostname && whoami'
ssh h100_sglang 'docker ps --format "table {{.Names}}\t{{.Status}}" | sed -n "1,20p"'
ssh h100_sglang 'nvidia-smi --query-gpu=index,name,utilization.gpu,memory.used,memory.total --format=csv,noheader,nounits'

Enter the container and confirm HF token visibility.
ssh h100_sglang 'docker exec -it sglang_bbuf /bin/zsh'
cd /data/bbuf/repos/sglang
echo ${HF_TOKEN:+set}


If HF_TOKEN is missing, export it before any Hub-backed diffusion run:

export HF_TOKEN=<your-hf-token>
export HUGGINGFACE_HUB_TOKEN="$HF_TOKEN"


For non-interactive docker exec ... bash -lc "<cmd>" runs, export both variables inline instead of relying on shell startup:

ssh h100_sglang 'docker exec sglang_bbuf env HF_TOKEN=<your-hf-token> HUGGINGFACE_HUB_TOKEN=<your-hf-token> zsh -lc "..."'

Pick a free GPU.

Use a GPU with 0 utilization and only a few MiB allocated. Always set CUDA_VISIBLE_DEVICES=<gpu_id> for diffusion validation commands.

If the container is not running, start it.
ssh h100_sglang 'docker start sglang_bbuf'

Safe Remote Workflow
Inspect the repo state before editing.
ssh h100_sglang 'docker exec sglang_bbuf zsh -lc "cd /data/bbuf/repos/sglang && git branch --show-current && git status --short"'

Fast-forward to latest clean main before creating a validation worktree.
ssh h100_sglang 'docker exec sglang_bbuf zsh -lc "cd /data/bbuf/repos/sglang && git fetch origin && git checkout main && git pull --ff-only origin main"'


Never write directly into /data/bbuf/repos/sglang when it is dirty.

Use one of these isolation strategies.

Create a detached worktree for remote-only experiments:

ssh h100_sglang 'docker exec sglang_bbuf zsh -lc "cd /data/bbuf/repos/sglang && git worktree add --detach /tmp/sglang_validate_h100 HEAD"'


Stream the local working tree into the container (validates exactly what is local right now):

COPYFILE_DISABLE=1 tar --exclude=.git -cf - . | \
ssh h100_sglang 'docker exec -i sglang_bbuf sh -lc "rm -rf /tmp/sglang_local_validate && mkdir -p /tmp/sglang_local_validate && tar -xf - -C /tmp/sglang_local_validate"'
ssh h100_sglang 'docker exec sglang_bbuf zsh -lc "find /tmp/sglang_local_validate -name '\''._*'\'' -delete"'


For patch-oriented validation:

fast-forward remote main
create a detached worktree from that commit
stream or git apply only the focused local diff into the worktree

This keeps /data/bbuf/repos/sglang clean while still validating the exact local delta.

Diffusion Validation Workflow
1. Syntax / Import Check

Always start here before running any GPU kernel or model test.

ssh h100_sglang 'docker exec sglang_bbuf zsh -lc "cd /tmp/sglang_local_validate && python -m compileall python/sglang/jit_kernel/diffusion/triton python/sglang/multimodal_gen/runtime/layers"'


For broader coverage:

ssh h100_sglang 'docker exec sglang_bbuf zsh -lc "cd /tmp/sglang_local_validate && python -m compileall python/sglang"'

2. JIT Kernel Smoke

Run a targeted smoke script covering the changed primitives before any model-level test.

Cover at least these when relevant:

rms_norm_fn
RMSNorm under torch.compile
norm_infer
apply_rotary_embedding

Pipe the smoke script through docker exec -i:

ssh h100_sglang 'docker exec -i sglang_bbuf env CUDA_VISIBLE_DEVICES=0 PYTHONPATH=python python' < /path/to/local_smoke.py

3. Fused Modulation Regression

Run this after any change to jit_kernel/diffusion/triton:

ssh h100_sglang 'docker exec sglang_bbuf env CUDA_VISIBLE_DEVICES=0 PYTHONPATH=python zsh -lc "cd /tmp/sglang_local_validate && pytest -q python/sglang/jit_kernel/tests/diffusion/test_qwen_image_modulation.py -q"'

4. General Diffusion Tests
ssh h100_sglang 'docker exec sglang_bbuf env CUDA_VISIBLE_DEVICES=0 PYTHONPATH=python zsh -lc "cd /tmp/sglang_local_validate && pytest -q path/to/diffusion_test.py -q"'

5. Model-Level Smoke (DiffGenerator)

Only after steps 1–4 pass.

Use a real .py file with if __name__ == "__main__": guard — multiprocessing.spawn will fail if the entry point is stdin or unguarded top-level code.

# stream the script file to the container
scp /path/to/local_smoke_model.py h100_sglang:/tmp/smoke_model.py
ssh h100_sglang 'docker exec sglang_bbuf env CUDA_VISIBLE_DEVICES=0 HF_TOKEN=<your-hf-token> HUGGINGFACE_HUB_TOKEN=<your-hf-token> PYTHONPATH=/tmp/sglang_local_validate/python zsh -lc "python /tmp/smoke_model.py"'


Treat checkpoint, dependency, and environment failures separately from code regressions.

6. Server-Level Smoke

Only attempt after model-level smoke passes.

ssh h100_sglang 'docker exec sglang_bbuf env CUDA_VISIBLE_DEVICES=0 PYTHONPATH=python zsh -lc "cd /tmp/sglang_local_validate && python -m sglang.launch_server --model-path <model> --port 30000 &"'

Torch Compile Attribution

When a benchmark compares eager vs torch.compile, do not stop at the speedup number. Capture matching eager and compile perf dumps or profile dirs. Compare structured perf dumps with the in-repo comparator:

ssh h100_sglang 'docker exec sglang_bbuf zsh -lc "cd /tmp/sglang_local_validate && python python/sglang/multimodal_gen/benchmarks/compare_perf.py eager.json compile.json"'


For trace-level attribution, use llm-torch-profiler-analysis on the matching profile dirs and explain whether the gain came from fewer launches, fewer copies, or fused kernels replacing eager ATen ops.

Cleanup
ssh h100_sglang 'docker exec sglang_bbuf rm -rf /tmp/sglang_local_validate /tmp/sglang_validate_h100 /tmp/smoke_model.py'

Weekly Installs
23
Repository
bbuf/sglang-aut…n-skills
GitHub Stars
189
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail