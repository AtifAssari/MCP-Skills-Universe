---
title: marimo-batch
url: https://skills.sh/marimo-team/skills/marimo-batch
---

# marimo-batch

skills/marimo-team/skills/marimo-batch
marimo-batch
Installation
$ npx skills add https://github.com/marimo-team/skills --skill marimo-batch
Summary

Prepare marimo notebooks for scheduled batch execution with CLI parameters and optional experiment tracking.

Converts UI-based parameters into Pydantic models that support both interactive forms and command-line argument parsing
Enables dual-mode execution: iterate with the UI, then run batch jobs via CLI with arguments like --sample-size 4096 --learning-rate 0.005
Optionally integrates Weights and Biases for experiment logging and parameter tracking
Includes EnvConfig for managing environment variables and API keys with optional validators
Preserves notebook column layouts and structure during modifications
SKILL.md

Pydantic is a great way to declare a source of truth for a batch job, especially for ML. You can declare something like:

from pydantic import BaseModel, Field

class ModelParams(BaseModel):
    sample_size: int = Field(
        default=1024 * 4, description="Number of training samples per epoch."
    )
    learning_rate: float = Field(default=0.01, description="Learning rate for the optimizer.")


You can fill these model params with two methods too, you can imagine a form in the UI.

el = mo.md("""
{sample_size} 
{learning_rate}
""").batch(
    sample_size=mo.ui.slider(1024, 1024 * 10, value=1024 * 4, step=1024, label="Sample size"),
    learning_rate=mo.ui.slider(0.001, 0.1, value=0.01, step=0.001, label="Learning rate"),
).form()
el


But you can also use the CLI from marimo.

if mo.app_meta().mode == "script":
    if "help" in mo.cli_args() or len(cli_args) == 0:
        print("Usage: uv run git_archaeology.py --repo <url> [--samples <n>]")
        print()
        for name, field in ModelParams.model_fields.items():
            default = f" (default: {field.default})" if field.default is not None else " (required)"
            print(f"  --{name:12s} {field.description}{default}")
        exit()
    model_params = ModelParams(
        **{k.replace("-", "_"): v for k, v in mo.cli_args().items()
    })
else: 
    model_params = ModelParams(**el.value)


The user can now run this from the command line via:

uv run notebook.py --sample-size 4096 --learning-rate 0.005


This is the best of both worlds, you can use the UI to test and iterate, and then use the CLI to run the batch job. Another benefit is that you can run the notebook with settings to make it run quickly to see if there are any bugs in the notebook.

The user wants to be able to run a notebook using this pattern, so make sure you ask the user which parameters they want to make configurable via the CLI and the proceed to make the changes to the notebook. Make sure you verify the changes with the user before making them.

Weights and Biases

It is possible that the user is interested in adding support for weights and biases. Make sure you confirm if this is the case yes/no. If that is the case, make sure these ModelParams are logged. You also want to make sure that the wandb_project and wandb_run_name are part of the ModelParams is the user wants to go down this route.

If the user is keen to start a training job for ML, make sure you use this starting point. Make sure you keep the columns intact in this notebook!

Environment Variables

You may need to read environment variables for the job. Use python-dotenv to read a .env file if it exists, but also add an EnvConfig so users may add keys manually in a ui.

from wigglystuff import EnvConfig

# With validators
config = EnvConfig({
    "OPENAI_API_KEY": lambda k: openai.Client(api_key=k).models.list(),
    "WANDB_API_KEY": lambda k: wandb.login(key=k, verify=True)
})

# Block until valid, useful in cell that needs the key
config.require_valid()

# Access values
config["OPENAI_API_KEY"]
config.get("OPENAI_API_KEY", "some default")


Make sure you add this EnvConfig at the top of the notebook.

Columns

It can be common for larger marimo notebooks to use the columns feature to make it easy to navigate. If that is the case, you must keep these columns intact!

@app.cell(column=0, hide_code=True)
def _(mo):
    mo.md(r"""demo""")

Compute platform

When the job is ready to get some serious compute, it is important that we keep good practices in mind. Consider batch sizes for the data set and make sure that there are plenty of logs so the user can spot if issues arise.

Grid search

When the user wants to run a hyperparameter sweep, point them to this grid launcher. It works with the notebook in references/starting-point.py out of the box: it samples random combinations from a search space that matches the notebook's ModelParams fields and launches each one as a separate job.

By default the script does a dry run (uv run grid.py) so the user can inspect the combinations before spending compute. Pass --launch to actually submit jobs. The --count and --seed flags control how many combinations to sample and the RNG seed.

The reference uses Hugging Face Jobs as the compute provider, but this is just one option. The user can swap it out for Modal, RunPod, or any other provider that can run a uv script.

Weekly Installs
1.4K
Repository
marimo-team/skills
GitHub Stars
127
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass