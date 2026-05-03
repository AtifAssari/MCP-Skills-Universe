---
title: fiftyone-model-evaluation
url: https://skills.sh/voxel51/fiftyone-skills/fiftyone-model-evaluation
---

# fiftyone-model-evaluation

skills/voxel51/fiftyone-skills/fiftyone-model-evaluation
fiftyone-model-evaluation
Installation
$ npx skills add https://github.com/voxel51/fiftyone-skills --skill fiftyone-model-evaluation
SKILL.md
Evaluate Model Predictions in FiftyOne
Key Directives

ALWAYS follow these rules:

1. Check if dataset exists and has required fields
list_datasets()
set_context(dataset_name="my-dataset")
dataset_summary(name="my-dataset")


Verify the dataset has both prediction and ground truth fields of compatible types.

2. Install evaluation plugin if not available
list_plugins()
# If @voxel51/evaluation not listed:
download_plugin(url_or_repo="voxel51/fiftyone-plugins", plugin_names=["@voxel51/evaluation"])
enable_plugin(plugin_name="@voxel51/evaluation")

3. Ask user for evaluation parameters

Always confirm with the user:

Prediction field name
Ground truth field name
Evaluation key (unique identifier for this evaluation)
Evaluation method (coco, open-images, simple, top-k, binary)
Whether to compute mAP (for detection tasks)
4. Launch App for evaluation operators
launch_app(dataset_name="my-dataset")

5. Close app when done
close_app()

Workflow
Step 1: Verify Dataset and Fields
list_datasets()
set_context(dataset_name="my-dataset")
dataset_summary(name="my-dataset")


Review:

Sample count
Available label fields and their types
Identify prediction field (model outputs)
Identify ground truth field (annotations)

Label Types and Compatible Evaluations:

Label Type	Evaluation Method	Supported Methods
Detections	evaluate_detections()	coco, open-images
Polylines	evaluate_detections()	coco, open-images
Keypoints	evaluate_detections()	coco, open-images
TemporalDetections	evaluate_detections()	activitynet
Classification	evaluate_classifications()	simple, top-k, binary
Segmentation	evaluate_segmentations()	simple
Regression	evaluate_regressions()	simple
Step 2: Ensure Evaluation Plugin is Installed
list_plugins()


If @voxel51/evaluation is not in the list:

download_plugin(
    url_or_repo="voxel51/fiftyone-plugins",
    plugin_names=["@voxel51/evaluation"]
)
enable_plugin(plugin_name="@voxel51/evaluation")

Step 3: Launch App
launch_app(dataset_name="my-dataset")

Step 4: Run Evaluation

Ask user for:

Prediction field (pred_field)
Ground truth field (gt_field)
Evaluation key (eval_key) - must be unique identifier
Evaluation method
execute_operator(
    operator_uri="@voxel51/evaluation/evaluate_model",
    params={
        "pred_field": "predictions",
        "gt_field": "ground_truth",
        "eval_key": "eval",
        "method": "coco",
        "iou": 0.5,
        "compute_mAP": true
    }
)

Step 5: View Results

After evaluation, the dataset will have new fields:

{eval_key}_tp - True positive count per sample
{eval_key}_fp - False positive count per sample
{eval_key}_fn - False negative count per sample

View only samples with false positives:

set_view(filters={"eval_fp": {"$gt": 0}})


Use the Model Evaluation Panel in the App to interactively explore:

Summary metrics (mAP, precision, recall)
Confusion matrices
Per-class performance
Scenario analysis
Step 6: View Evaluation Patches (TP/FP/FN)

To examine individual true positives, false positives, and false negatives, guide users to the Python SDK:

import fiftyone as fo

dataset = fo.load_dataset("my-dataset")

# Convert to evaluation patches view
eval_patches = dataset.to_evaluation_patches("eval")

# Count by type
print(eval_patches.count_values("type"))
# Output: {'fn': 246, 'fp': 4131, 'tp': 986}

# View only false positives
fp_view = eval_patches.match(F("type") == "fp")
session = fo.launch_app(view=fp_view)

Step 7: Clean Up
close_app()

Evaluation Types
Detection Evaluation

For Detections, Polylines, Keypoints labels.

COCO-style (default):

execute_operator(
    operator_uri="@voxel51/evaluation/evaluate_model",
    params={
        "pred_field": "predictions",
        "gt_field": "ground_truth",
        "eval_key": "eval_coco",
        "method": "coco",
        "iou": 0.5,
        "classwise": true,
        "compute_mAP": true
    }
)

Parameter	Type	Default	Description
iou	float	0.5	IoU threshold for matching
classwise	bool	true	Only match objects with same class
compute_mAP	bool	false	Compute mAP, mAR, and PR curves
use_masks	bool	false	Use instance masks for IoU (if available)
iscrowd	string	null	Attribute name for crowd annotations
iou_threshs	string	null	Comma-separated IoU thresholds for mAP
max_preds	int	null	Max predictions per sample for mAP

Open Images-style:

execute_operator(
    operator_uri="@voxel51/evaluation/evaluate_model",
    params={
        "pred_field": "predictions",
        "gt_field": "ground_truth",
        "eval_key": "eval_oi",
        "method": "open-images",
        "iou": 0.5
    }
)


Supports additional parameters:

pos_label_field: Classifications specifying which classes should be evaluated
neg_label_field: Classifications specifying which classes should NOT be evaluated

ActivityNet-style (temporal):

For TemporalDetections in video datasets:

execute_operator(
    operator_uri="@voxel51/evaluation/evaluate_model",
    params={
        "pred_field": "predictions",
        "gt_field": "ground_truth",
        "eval_key": "eval_temporal",
        "method": "activitynet",
        "compute_mAP": true
    }
)

Classification Evaluation

For Classification labels.

Simple (default):

execute_operator(
    operator_uri="@voxel51/evaluation/evaluate_model",
    params={
        "pred_field": "predictions",
        "gt_field": "ground_truth",
        "eval_key": "eval_cls",
        "method": "simple"
    }
)


Per-sample field {eval_key} stores boolean indicating if prediction was correct.

Top-k:

Requires predictions with logits field:

execute_operator(
    operator_uri="@voxel51/evaluation/evaluate_model",
    params={
        "pred_field": "predictions",
        "gt_field": "ground_truth",
        "eval_key": "eval_topk",
        "method": "top-k",
        "k": 5
    }
)


Binary:

For binary classifiers:

execute_operator(
    operator_uri="@voxel51/evaluation/evaluate_model",
    params={
        "pred_field": "predictions",
        "gt_field": "ground_truth",
        "eval_key": "eval_binary",
        "method": "binary"
    }
)


Per-sample field {eval_key} stores: "tp", "fp", "tn", or "fn".

Segmentation Evaluation

For Segmentation labels.

execute_operator(
    operator_uri="@voxel51/evaluation/evaluate_model",
    params={
        "pred_field": "predictions",
        "gt_field": "ground_truth",
        "eval_key": "eval_seg",
        "method": "simple",
        "bandwidth": 5  # Optional: evaluate only boundary pixels
    }
)

Parameter	Type	Default	Description
bandwidth	int	null	Pixels along contours to evaluate (null = entire mask)
average	string	"micro"	Averaging strategy: micro, macro, weighted, samples

Per-sample fields:

{eval_key}_accuracy
{eval_key}_precision
{eval_key}_recall
Regression Evaluation

For Regression labels.

execute_operator(
    operator_uri="@voxel51/evaluation/evaluate_model",
    params={
        "pred_field": "predictions",
        "gt_field": "ground_truth",
        "eval_key": "eval_reg",
        "method": "simple",
        "metric": "squared_error"  # or "absolute_error"
    }
)


Per-sample field {eval_key} stores the error value.

Metrics available:

Mean Squared Error (MSE)
Root Mean Squared Error (RMSE)
Mean Absolute Error (MAE)
Median Absolute Error
R² Score
Explained Variance Score
Max Error
Managing Evaluations
List Existing Evaluations
execute_operator(
    operator_uri="@voxel51/evaluation/get_evaluation_info",
    params={
        "eval_key": "eval"
    }
)

Load Evaluation View

Load the exact view on which an evaluation was performed:

execute_operator(
    operator_uri="@voxel51/evaluation/load_evaluation_view",
    params={
        "eval_key": "eval",
        "select_fields": false
    }
)

Rename Evaluation
execute_operator(
    operator_uri="@voxel51/evaluation/rename_evaluation",
    params={
        "eval_key": "eval",
        "new_eval_key": "eval_v2"
    }
)

Delete Evaluation
execute_operator(
    operator_uri="@voxel51/evaluation/delete_evaluation",
    params={
        "eval_key": "eval"
    }
)

Common Use Cases
Use Case 1: Evaluate Object Detection Model
# Verify dataset has detection fields
set_context(dataset_name="my-dataset")
dataset_summary(name="my-dataset")

# Launch app
launch_app(dataset_name="my-dataset")

# Run COCO-style evaluation with mAP
execute_operator(
    operator_uri="@voxel51/evaluation/evaluate_model",
    params={
        "pred_field": "predictions",
        "gt_field": "ground_truth",
        "eval_key": "eval",
        "method": "coco",
        "iou": 0.5,
        "compute_mAP": true
    }
)

# View samples with most false positives
set_view(filters={"eval_fp": {"$gt": 5}})

Use Case 2: Compare Two Detection Models
set_context(dataset_name="my-dataset")
launch_app(dataset_name="my-dataset")

# Evaluate first model
execute_operator(
    operator_uri="@voxel51/evaluation/evaluate_model",
    params={
        "pred_field": "model_a_predictions",
        "gt_field": "ground_truth",
        "eval_key": "eval_model_a",
        "method": "coco",
        "compute_mAP": true
    }
)

# Evaluate second model
execute_operator(
    operator_uri="@voxel51/evaluation/evaluate_model",
    params={
        "pred_field": "model_b_predictions",
        "gt_field": "ground_truth",
        "eval_key": "eval_model_b",
        "method": "coco",
        "compute_mAP": true
    }
)

# Use the Model Evaluation Panel to compare results

Use Case 3: Evaluate Classification Model
set_context(dataset_name="my-classification-dataset")
launch_app(dataset_name="my-classification-dataset")

# Simple classification evaluation
execute_operator(
    operator_uri="@voxel51/evaluation/evaluate_model",
    params={
        "pred_field": "predictions",
        "gt_field": "ground_truth",
        "eval_key": "eval_cls",
        "method": "simple"
    }
)

# View misclassified samples
set_view(filters={"eval_cls": false})

Use Case 4: Evaluate at Different IoU Thresholds
set_context(dataset_name="my-dataset")
launch_app(dataset_name="my-dataset")

# Strict evaluation (IoU 0.75)
execute_operator(
    operator_uri="@voxel51/evaluation/evaluate_model",
    params={
        "pred_field": "predictions",
        "gt_field": "ground_truth",
        "eval_key": "eval_strict",
        "method": "coco",
        "iou": 0.75,
        "compute_mAP": true
    }
)

# Lenient evaluation (IoU 0.25)
execute_operator(
    operator_uri="@voxel51/evaluation/evaluate_model",
    params={
        "pred_field": "predictions",
        "gt_field": "ground_truth",
        "eval_key": "eval_lenient",
        "method": "coco",
        "iou": 0.25,
        "compute_mAP": true
    }
)

Use Case 5: Evaluate Segmentation Model
set_context(dataset_name="my-segmentation-dataset")
launch_app(dataset_name="my-segmentation-dataset")

# Full mask evaluation
execute_operator(
    operator_uri="@voxel51/evaluation/evaluate_model",
    params={
        "pred_field": "predictions",
        "gt_field": "ground_truth",
        "eval_key": "eval_seg",
        "method": "simple"
    }
)

# Boundary-only evaluation (5 pixel bandwidth)
execute_operator(
    operator_uri="@voxel51/evaluation/evaluate_model",
    params={
        "pred_field": "predictions",
        "gt_field": "ground_truth",
        "eval_key": "eval_seg_boundary",
        "method": "simple",
        "bandwidth": 5
    }
)

Python SDK Alternative

For more control over evaluation and access to full results, guide users to the Python SDK:

import fiftyone as fo
import fiftyone.zoo as foz

# Load dataset
dataset = fo.load_dataset("my-dataset")

# Evaluate detections
results = dataset.evaluate_detections(
    "predictions",
    gt_field="ground_truth",
    eval_key="eval",
    method="coco",
    iou=0.5,
    compute_mAP=True,
)

# Print classification report
results.print_report()

# Get mAP value
print(f"mAP: {results.mAP():.3f}")

# Plot confusion matrix (interactive)
plot = results.plot_confusion_matrix()
plot.show()

# Plot precision-recall curves
plot = results.plot_pr_curves(classes=["person", "car", "dog"])
plot.show()

# Convert to evaluation patches to view TP/FP/FN
eval_patches = dataset.to_evaluation_patches("eval")
print(eval_patches.count_values("type"))

# View false positives in the App
from fiftyone import ViewField as F
fp_view = eval_patches.match(F("type") == "fp")
session = fo.launch_app(view=fp_view)


Python SDK evaluation methods:

dataset.evaluate_detections() - Object detection
dataset.evaluate_classifications() - Classification
dataset.evaluate_segmentations() - Semantic segmentation
dataset.evaluate_regressions() - Regression

Results object methods:

results.print_report() - Print classification report
results.print_metrics() - Print aggregate metrics
results.mAP() - Get mAP value (detection only)
results.mAR() - Get mAR value (detection only)
results.plot_confusion_matrix() - Interactive confusion matrix
results.plot_pr_curves() - Precision-recall curves
results.plot_results() - Scatter plot (regression only)
Troubleshooting

Error: "No suitable label fields"

Dataset must have label fields of compatible types
Use dataset_summary() to see available fields and types

Error: "No suitable ground truth fields"

Ground truth field must be same type as prediction field
Cannot compare Detections predictions with Classification ground truth

Error: "Evaluation key already exists"

Each evaluation must have a unique key
Delete existing evaluation or use a different key name

Error: "Plugin not found"

Install the evaluation plugin:
download_plugin(url_or_repo="voxel51/fiftyone-plugins", plugin_names=["@voxel51/evaluation"])
enable_plugin(plugin_name="@voxel51/evaluation")


mAP is not computed

Set compute_mAP: true in params
mAP requires multiple predictions per image to be meaningful

Evaluation is slow

Large datasets take time
Consider evaluating a filtered view first
Use delegated execution for background processing
Best Practices
Use descriptive eval_keys - eval_yolov8_coco, eval_resnet_topk5
Don't overwrite evaluations - Use unique keys for each evaluation run
Compare at same IoU - When comparing models, use consistent IoU thresholds
Check field types first - Ensure prediction and ground truth fields are compatible
Use Model Evaluation Panel - Interactive exploration is easier than scripting
Examine patches - Use to_evaluation_patches() to understand errors
Resources
FiftyOne Evaluation Guide
Detection Evaluation
Classification Evaluation
Segmentation Evaluation
Model Evaluation Panel
Evaluation Plugin
Weekly Installs
12
Repository
voxel51/fiftyone-skills
GitHub Stars
25
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn