---
rating: ⭐⭐⭐
title: fiftyone-dataset-inference
url: https://skills.sh/voxel51/fiftyone-skills/fiftyone-dataset-inference
---

# fiftyone-dataset-inference

skills/voxel51/fiftyone-skills/fiftyone-dataset-inference
fiftyone-dataset-inference
Installation
$ npx skills add https://github.com/voxel51/fiftyone-skills --skill fiftyone-dataset-inference
SKILL.md
Run Model Inference on FiftyOne Datasets
Key Directives

ALWAYS follow these rules:

1. Check if dataset exists first
list_datasets()


If the dataset doesn't exist, use the fiftyone-dataset-import skill to load it first.

2. Set context before operations
set_context(dataset_name="my-dataset")

3. Launch App for inference

The App must be running to execute inference operators:

launch_app(dataset_name="my-dataset")

4. Ask user for field names

Always confirm with the user:

Which model to use
Label field name for predictions (e.g., predictions, detections, embeddings)
5. Close app when done
close_app()

Workflow
Step 1: Verify Dataset Exists
list_datasets()


If the dataset is not in the list:

Ask the user for the data location
Use the fiftyone-dataset-import skill to import the data first
Return to this workflow after import completes
Step 2: Load Dataset and Review
set_context(dataset_name="my-dataset")
dataset_summary(name="my-dataset")


Review:

Sample count
Media type
Existing label fields
Step 3: Launch App
launch_app(dataset_name="my-dataset")

Step 4: Discover and Apply Model

Ask the user about the task, model, or type of data they're using (detection, classification, segmentation, embeddings, or a specific model name); note users may give a 'tool name' (see Path B). Then determine the path:

Path A — Zoo model (most common)

ALWAYS first fetch the live model list — never assume what's available:

get_operator_schema(operator_uri="@voxel51/zoo/apply_zoo_model")


Pick the right model from the schema's model enum, then apply:

execute_operator(
    operator_uri="@voxel51/zoo/apply_zoo_model",
    params={
        "tab": "BUILTIN",
        "model": "<model-name-from-schema>",
        "label_field": "predictions"
    }
)


Path B — Plugin operator

If the user mentions a specific tool (e.g. CLIP similarity, SAM, a third-party model), check installed operators first:

list_operators(builtin_only=False)


Find the matching operator, inspect its schema, then execute it:

get_operator_schema(operator_uri="@org/plugin/operator")
execute_operator(operator_uri="@org/plugin/operator", params={...})


Path C — Remote / externally registered model

Check registered remote sources first:

import fiftyone.zoo as foz
foz.list_zoo_model_sources()


If the model comes from a registered remote source (GitHub repo registered via foz.register_zoo_model_source()):

execute_operator(
    operator_uri="@voxel51/zoo/apply_zoo_model",
    params={
        "tab": "REMOTE",
        "source": "<github-repo-url>",
        "label_field": "predictions"
    }
)

Step 5: View Results
set_view(exists=["predictions"])

Step 6: Clean Up
close_app()

Model Discovery

ALWAYS fetch the live model list — never rely on a hardcoded list.

get_operator_schema(operator_uri="@voxel51/zoo/apply_zoo_model")


The schema returns the full set of available models at runtime. Use the model names from there directly.

For plugin-provided models or operators:

list_operators(builtin_only=False)


If a model fails with a dependency error, the response includes install_command. Offer to run it for the user.

Common Use Cases
Use Case 1: Run Object Detection
# Verify dataset exists
list_datasets()

# Set context and launch
set_context(dataset_name="my-dataset")
launch_app(dataset_name="my-dataset")

# Apply detection model
execute_operator(
    operator_uri="@voxel51/zoo/apply_zoo_model",
    params={
        "tab": "BUILTIN",
        "model": "faster-rcnn-resnet50-fpn-coco-torch",
        "label_field": "predictions"
    }
)

# View results
set_view(exists=["predictions"])

Use Case 2: Run Classification
set_context(dataset_name="my-dataset")
launch_app(dataset_name="my-dataset")

execute_operator(
    operator_uri="@voxel51/zoo/apply_zoo_model",
    params={
        "tab": "BUILTIN",
        "model": "resnet50-imagenet-torch",
        "label_field": "classification"
    }
)

set_view(exists=["classification"])

Use Case 3: Generate Embeddings
set_context(dataset_name="my-dataset")
launch_app(dataset_name="my-dataset")

execute_operator(
    operator_uri="@voxel51/zoo/apply_zoo_model",
    params={
        "tab": "BUILTIN",
        "model": "clip-vit-base32-torch",
        "label_field": "clip_embeddings"
    }
)

Use Case 4: Compare Ground Truth with Predictions

If dataset has existing labels:

set_context(dataset_name="my-dataset")
dataset_summary(name="my-dataset")  # Check existing fields

launch_app(dataset_name="my-dataset")

# Run inference with different field name
execute_operator(
    operator_uri="@voxel51/zoo/apply_zoo_model",
    params={
        "tab": "BUILTIN",
        "model": "yolov8m-coco-torch",
        "label_field": "predictions"  # Different from ground_truth
    }
)

# View both fields to compare
set_view(exists=["ground_truth", "predictions"])

Use Case 5: Run Multiple Models
set_context(dataset_name="my-dataset")
launch_app(dataset_name="my-dataset")

# Run detection
execute_operator(
    operator_uri="@voxel51/zoo/apply_zoo_model",
    params={
        "tab": "BUILTIN",
        "model": "yolov8n-coco-torch",
        "label_field": "detections"
    }
)

# Run classification
execute_operator(
    operator_uri="@voxel51/zoo/apply_zoo_model",
    params={
        "tab": "BUILTIN",
        "model": "resnet50-imagenet-torch",
        "label_field": "classification"
    }
)

# Run embeddings
execute_operator(
    operator_uri="@voxel51/zoo/apply_zoo_model",
    params={
        "tab": "BUILTIN",
        "model": "clip-vit-base32-torch",
        "label_field": "embeddings"
    }
)

Troubleshooting

Error: "Dataset not found"

Use list_datasets() to see available datasets
Use the fiftyone-dataset-import skill to import data first

Error: "Model not found"

Run get_operator_schema(operator_uri="@voxel51/zoo/apply_zoo_model") to get the current live model list and pick the correct name

Error: "Missing dependency" (e.g., ultralytics, segment-anything)

The MCP server detects missing dependencies
Response includes missing_package and install_command
Install the required package: pip install <package>
Restart MCP server after installing

Inference is slow

Use smaller model variant (e.g., yolov8n instead of yolov8x)
Use delegated execution for large datasets
Consider filtering to a view first

Out of memory

Reduce batch size
Use smaller model variant
Process dataset in chunks using views
Best Practices
Use descriptive field names - predictions, yolo_detections, clip_embeddings
Don't overwrite ground truth - Use different field names for predictions
Start with fast models - Use nano/small variants first, upgrade if needed
Check existing fields - Use dataset_summary() before running inference
Filter first for testing - Test on a small view before processing full dataset
Resources
FiftyOne Model Zoo
Applying Models Guide
Zoo Models API
Weekly Installs
12
Repository
voxel51/fiftyone-skills
GitHub Stars
25
First Seen
Feb 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass