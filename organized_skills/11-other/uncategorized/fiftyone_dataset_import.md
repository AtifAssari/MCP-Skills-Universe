---
rating: ⭐⭐⭐
title: fiftyone-dataset-import
url: https://skills.sh/voxel51/fiftyone-skills/fiftyone-dataset-import
---

# fiftyone-dataset-import

skills/voxel51/fiftyone-skills/fiftyone-dataset-import
fiftyone-dataset-import
Installation
$ npx skills add https://github.com/voxel51/fiftyone-skills --skill fiftyone-dataset-import
SKILL.md
Universal Dataset Import for FiftyOne
Key Directives

ALWAYS follow these rules:

1. Scan folder FIRST

Before any import, deeply scan the directory to understand its structure:

# Use bash to explore
find /path/to/data -type f | head -50
ls -la /path/to/data

2. Auto-detect everything

Detect media types, label formats, and grouping patterns automatically. Never ask the user to specify format if it can be inferred.

3. Detect multimodal groups

Look for patterns that indicate grouped data:

Scene folders containing multiple media files
Filename patterns with common prefixes (e.g., scene_001_left.jpg, scene_001_right.jpg)
Mixed media types that should be grouped (images + point clouds)
4. Detect and install required packages

Many specialized dataset formats require external Python packages. After detecting the format:

Identify required packages based on the detected format
Check if packages are installed using pip show <package>
Search for installation instructions if needed (use web search or FiftyOne docs)
Ask user for permission before installing any packages
Install required packages (see installation methods below)
Verify installation before proceeding

Common format-to-package mappings:

Dataset Format	Package Name	Install Command
PandaSet	pandaset	pip install "git+https://github.com/scaleapi/pandaset-devkit.git#subdirectory=python"
nuScenes	nuscenes-devkit	pip install nuscenes-devkit
Waymo Open	waymo-open-dataset-tf	See Waymo docs (requires TensorFlow)
Argoverse 2	av2	pip install av2
KITTI 3D	pykitti	pip install pykitti
Lyft L5	l5kit	pip install l5kit
A2D2	a2d2	See Audi A2D2 docs

Additional packages for 3D processing:

Purpose	Package Name	Install Command
Point cloud conversion to PCD	open3d	pip install open3d
Point cloud processing	pyntcloud	pip install pyntcloud
LAS/LAZ point clouds	laspy	pip install laspy

Additional packages for Hugging Face Hub:

Purpose	Package Name	Install Command
HF Hub API	huggingface_hub	pip install huggingface_hub
Parquet file reading	pyarrow	pip install pyarrow
Image processing	Pillow	pip install Pillow

Installation methods (in order of preference):

PyPI - Standard pip install:

pip install <package-name>


GitHub URL - When package is not on PyPI:

# Standard GitHub install
pip install "git+https://github.com/<org>/<repo>.git"

# With subdirectory (for monorepos)
pip install "git+https://github.com/<org>/<repo>.git#subdirectory=python"

# Specific branch or tag
pip install "git+https://github.com/<org>/<repo>.git@v1.0.0"


Clone and install - For complex builds:

git clone https://github.com/<org>/<repo>.git
cd <repo>
pip install .


Dynamic package discovery workflow:

If the format is not in the table above:

Search PyPI for <format-name>, <format-name>-devkit, or <format-name>-sdk
Search GitHub for <format-name> devkit or <format-name> python
Search web for "FiftyOne import " or " python tutorial"
Check the dataset's official website for developer tools/SDK
Present findings to user with installation options

After installation:

Verify the package is installed: pip show <package-name>
Test import in Python: python -c "from <package> import ..."
Search for FiftyOne integration examples or write custom import code
5. Confirm before importing

Present findings to user and explicitly ask for confirmation before creating the dataset. Always end your scan summary with a clear question like:

"Proceed with import?"
"Should I create the dataset with these settings?"

Wait for user response before proceeding. Do not create the dataset until the user confirms.

6. Check for existing datasets and generate names

Before creating a dataset, check if the proposed name already exists:

list_datasets()


If the dataset name exists, ask the user:

Overwrite: Delete existing and create new
Rename: Use a different name (suggest alternatives like dataset-name-v2)
Abort: Cancel the import

If no dataset name was provided by the user, generate a fun unique name using the pattern {ADJECTIVE}_{NOUN}_{VERB}:

squiggly_sky_floats
droopy_horse_slams
smooth_grass_grumbles
nervous_hamburger_yodels

Cross-check against list_datasets() to ensure uniqueness. Always inform the user of the generated name before proceeding.

7. Validate after import

Compare imported sample count with source file count. Report any discrepancies.

8. Report errors minimally to user

Keep error messages simple for the user. Use detailed error info internally to diagnose issues.

Complete Workflow
Step 1: Deep Folder Scan

Scan the target directory to understand its structure:

# Count files by extension
find /path/to/data -type f | sed 's/.*\.//' | sort | uniq -c | sort -rn

# List directory structure (2 levels deep)
find /path/to/data -maxdepth 2 -type d

# Sample some files
ls -la /path/to/data/* | head -20

# IMPORTANT: Scan for ALL annotation/label directories
ls -la /path/to/data/annotations/ 2>/dev/null || ls -la /path/to/data/labels/ 2>/dev/null


Build an inventory of:

Media files by type (images, videos, point clouds, 3D)
Label files by format (JSON, XML, TXT, YAML, PKL)
Directory structure (flat vs nested vs scene-based)
ALL annotation types present (cuboids, segmentation, tracking, etc.)

For 3D/Autonomous Driving datasets, specifically check:

# List all annotation subdirectories
find /path/to/data -type d -name "annotations" -o -name "labels" | xargs -I {} ls -la {}

# Sample an annotation file to understand its structure
python3 -c "import pickle, gzip; print(pickle.load(gzip.open('path/to/annotation.pkl.gz', 'rb'))[:2])"

Step 2: Identify Media Types

Classify files by extension:

Extensions	Media Type	FiftyOne Type
.jpg, .jpeg, .png, .gif, .bmp, .webp, .tiff	Image	image
.mp4, .avi, .mov, .mkv, .webm	Video	video
.pcd, .ply, .las, .laz	Point Cloud	point-cloud
.fo3d, .obj, .gltf, .glb	3D Scene	3d
Step 3: Detect Label Format

Identify label format from file patterns:

Pattern	Format	Dataset Type
annotations.json or instances*.json with COCO structure	COCO	COCO
*.xml files with Pascal VOC structure	VOC	VOC
*.txt per image + classes.txt	YOLOv4	YOLOv4
data.yaml + labels/*.txt	YOLOv5	YOLOv5
*.txt per image (KITTI format)	KITTI	KITTI
Single annotations.xml (CVAT format)	CVAT	CVAT Image
*.json with OpenLABEL structure	OpenLABEL	OpenLABEL Image
Folder-per-class structure	Classification	Image Classification Directory Tree
*.csv with filepath column	CSV	CSV
*.json with GeoJSON structure	GeoJSON	GeoJSON
.dcm DICOM files	DICOM	DICOM
.tiff with geo metadata	GeoTIFF	GeoTIFF

Specialized Autonomous Driving Formats (require external packages):

Directory Pattern	Format	Required Package
camera/, lidar/, annotations/cuboids/ with .pkl.gz	PandaSet	pandaset-devkit
samples/, sweeps/, v1.0-* folders	nuScenes	nuscenes-devkit
segment-* with .tfrecord files	Waymo Open	waymo-open-dataset-tf
argoverse-tracking/ structure	Argoverse	argoverse-api
training/, testing/ with calib/, velodyne/	KITTI 3D	pykitti
scenes/, aerial_map/	Lyft L5	l5kit
Step 4: Detect Required Packages

After identifying the format, check if external packages are needed:

# Check if package is installed (use the actual package name, not repo name)
pip show pandaset

# If not found, the package needs to be installed


If packages are required:

Inform user what packages are needed and why

Search for installation method if not in the common mappings table:

Search PyPI first: pip search <package> or check pypi.org
Search GitHub for the devkit/SDK repository
Check the dataset's official documentation
Search web: " python install"

Ask for permission to install:

This dataset appears to be in PandaSet format, which requires the `pandaset` package.

The package is not on PyPI and must be installed from GitHub:
pip install "git+https://github.com/scaleapi/pandaset-devkit.git#subdirectory=python"

Would you like me to:
- Install the package (recommended)
- Search for alternative import methods
- Abort and let you install manually


Install using the appropriate method:

# PyPI (if available)
pip install <package-name>

# GitHub URL (if not on PyPI)
pip install "git+https://github.com/<org>/<repo>.git#subdirectory=python"

# Clone and install (for complex builds)
git clone https://github.com/<org>/<repo>.git && cd <repo> && pip install .


Verify installation:

pip show <package-name>


Test the import in Python:

python -c "from <package> import <main_class>; print('OK')"


Search for FiftyOne integration code:

Search: "FiftyOne import example"
Search: " to FiftyOne grouped dataset"
Check FiftyOne docs for similar dataset types
If no examples exist, build custom import code using the devkit API
Step 5: Detect Grouping Pattern

Determine if data should be grouped:

Pattern A: Scene Folders (Most Common for Multimodal)

/data/
├── scene_001/
│   ├── left.jpg
│   ├── right.jpg
│   ├── lidar.pcd
│   └── labels.json
├── scene_002/
│   └── ...


Detection: Each subfolder = one group, files inside = slices

Pattern B: Filename Prefix

/data/
├── 001_left.jpg
├── 001_right.jpg
├── 001_lidar.pcd
├── 002_left.jpg
├── 002_right.jpg
├── 002_lidar.pcd


Detection: Common prefix = group ID, suffix = slice name

Pattern C: No Grouping (Flat)

/data/
├── image_001.jpg
├── image_002.jpg
├── image_003.jpg


Detection: Single media type, no clear grouping pattern

Step 6: Present Findings to User

Before importing, present a clear summary that includes ALL detected labels:

Scan Results for /path/to/data:

Media Found:
  - 3,000 images (.jpg, .png)
  - 1,000 point clouds (.pkl.gz → will convert to .pcd)
  - 0 videos

Grouping Detected:
  - Pattern: Scene folders
  - Groups: 1,000 scenes
  - Slices: left (image), right (image), front (image), lidar (point-cloud)

ALL Labels Detected:
  ├── cuboids/           (3D bounding boxes, 1,000 files)
  │   └── Format: pickle, Fields: label, position, dimensions, rotation, track_id
  ├── semseg/            (Semantic segmentation, 1,000 files)
  │   └── Format: pickle, point-wise class labels
  └── instances.json     (2D detections, COCO format)
      └── Classes: 10 (car, pedestrian, cyclist, ...)

Required Packages:
  - ✅ pandaset (installed)
  - ⚠️ open3d (needed for PCD conversion) → pip install open3d

Proposed Configuration:
  - Dataset name: my-dataset
  - Type: Grouped (multimodal)
  - Default slice: front_camera
  - Labels to import:
    - detections_3d (from cuboids/)
    - point_labels (from semseg/)
    - detections (from instances.json)

Proceed with import? (yes/no)


IMPORTANT:

List ALL annotation types found during the scan
Show the format/structure of each label type
Indicate which labels will be imported and how
Wait for user confirmation before proceeding
Step 7: Check for Existing Dataset and Generate Name

Before creating, check if the dataset name already exists:

# Check existing datasets
list_datasets()


If the user didn't provide a name, generate one using the {ADJECTIVE}_{NOUN}_{VERB} pattern (e.g., smooth_grass_grumbles). Cross-check against list_datasets() for uniqueness. Always inform the user of the generated name before proceeding.

If the proposed dataset name exists in the list:

Inform the user: "A dataset named 'my-dataset' already exists with X samples."
Ask for their preference:
Overwrite: Delete existing dataset first
Rename: Suggest alternatives (e.g., my-dataset-v2, my-dataset-20240107)
Abort: Cancel the import

If user chooses to overwrite:

# Delete existing dataset
set_context(dataset_name="my-dataset")
execute_operator(
    operator_uri="@voxel51/utils/delete_dataset",
    params={"name": "my-dataset"}
)

Step 8: Create Dataset
# Create the dataset
execute_operator(
    operator_uri="@voxel51/utils/create_dataset",
    params={
        "name": "my-dataset",
        "persistent": true
    }
)

# Set context
set_context(dataset_name="my-dataset")

Step 9A: Import Simple Dataset (No Groups)

For flat datasets without grouping:

# Import media only
execute_operator(
    operator_uri="@voxel51/io/import_samples",
    params={
        "import_type": "MEDIA_ONLY",
        "style": "DIRECTORY",
        "directory": {"absolute_path": "/path/to/images"}
    }
)

# Import with labels
execute_operator(
    operator_uri="@voxel51/io/import_samples",
    params={
        "import_type": "MEDIA_AND_LABELS",
        "dataset_type": "COCO",
        "data_path": {"absolute_path": "/path/to/images"},
        "labels_path": {"absolute_path": "/path/to/annotations.json"},
        "label_field": "ground_truth"
    }
)

Step 9B: Import Grouped Dataset (Multimodal)

For multimodal data with groups, use Python directly. Guide the user:

import fiftyone as fo

# Create dataset
dataset = fo.Dataset("multimodal-dataset", persistent=True)

# Add group field
dataset.add_group_field("group", default="front")

# Create samples for each group
import os
from pathlib import Path

data_dir = Path("/path/to/data")
samples = []

for scene_dir in sorted(data_dir.iterdir()):
    if not scene_dir.is_dir():
        continue

    # Create a group for this scene
    group = fo.Group()

    # Add each file as a slice
    for file in scene_dir.iterdir():
        if file.suffix in ['.jpg', '.png']:
            # Determine slice name from filename
            slice_name = file.stem  # e.g., "left", "right", "front"
            samples.append(fo.Sample(
                filepath=str(file),
                group=group.element(slice_name)
            ))
        elif file.suffix == '.pcd':
            samples.append(fo.Sample(
                filepath=str(file),
                group=group.element("lidar")
            ))
        elif file.suffix == '.mp4':
            samples.append(fo.Sample(
                filepath=str(file),
                group=group.element("video")
            ))

# Add all samples
dataset.add_samples(samples)
print(f"Added {len(dataset)} samples in {len(dataset.distinct('group.id'))} groups")

Step 9C: Import Specialized Format Dataset (3D/Autonomous Driving)

For datasets requiring external packages (PandaSet, nuScenes, etc.), use the devkit to load data and convert to FiftyOne format.

General approach:

Search FiftyOne documentation or web for the specific import method
Use the devkit to load the raw data
Convert point clouds to PCD format (FiftyOne requires .pcd files)
Create fo.Scene objects for 3D visualization with point clouds
Convert to FiftyOne samples with proper grouping
Import ALL detected labels (cuboids, segmentation, etc.) found during scan
Converting Point Clouds to PCD

Many autonomous driving datasets store LiDAR data in proprietary formats (.pkl.gz, .bin, .npy). Convert to PCD for FiftyOne:

import numpy as np
import open3d as o3d
from pathlib import Path

def convert_to_pcd(points, output_path):
    """
    Convert point cloud array to PCD file.

    Args:
        points: numpy array of shape (N, 3) or (N, 4) with XYZ or XYZI
        output_path: path to save .pcd file
    """
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points[:, :3])

    # If intensity is available, store as colors (grayscale)
    if points.shape[1] >= 4:
        intensity = points[:, 3]
        intensity_normalized = (intensity - intensity.min()) / (intensity.max() - intensity.min() + 1e-8)
        colors = np.stack([intensity_normalized] * 3, axis=1)
        pcd.colors = o3d.utility.Vector3dVector(colors)

    o3d.io.write_point_cloud(str(output_path), pcd)
    return output_path


Note: Install open3d if needed: pip install open3d

Creating fo.Scene for 3D Visualization

For each LiDAR frame, create an fo.Scene that references the PCD file:

import fiftyone as fo

# Create a 3D scene for the point cloud
scene = fo.Scene()

# Add point cloud to the scene
scene.add_point_cloud(
    name="lidar",
    pcd_path="/path/to/frame.pcd",
    flag_for_projection=True  # Enable projection to camera views
)

# Create sample with the scene
sample = fo.Sample(filepath="/path/to/scene.fo3d")  # Or use scene directly
sample["scene"] = scene

Importing ALL Labels Detected During Scan

During the folder scan (Step 1), identify ALL label types present:

# Example: List all annotation directories/files
ls -la /path/to/dataset/annotations/
# Output might show: cuboids/, semseg/, tracking/, instances.json, etc.


Map detected labels to FiftyOne label types:

Annotation Type	FiftyOne Label Type	Field Name
3D Cuboids/Bounding Boxes	fo.Detection with 3D attributes	detections_3d
Semantic Segmentation	fo.Segmentation	segmentation
Instance Segmentation	fo.Detections with masks	instances
Tracking IDs	Add track_id to detections	tracks
Classification	fo.Classification	classification
Keypoints/Pose	fo.Keypoints	keypoints

Example: PandaSet Full Import with Labels

import fiftyone as fo
import numpy as np
import open3d as o3d
from pathlib import Path
import gzip
import pickle

data_path = Path("/path/to/pandaset")
pcd_output_dir = data_path / "pcd_converted"
pcd_output_dir.mkdir(exist_ok=True)

# Create dataset with groups
dataset = fo.Dataset("pandaset", persistent=True)
dataset.add_group_field("group", default="front_camera")

# Get camera names
camera_names = [d.name for d in (data_path / "camera").iterdir() if d.is_dir()]
frame_count = len(list((data_path / "camera" / "front_camera").glob("*.jpg")))

# Check what labels exist
labels_dir = data_path / "annotations"
available_labels = [d.name for d in labels_dir.iterdir() if d.is_dir()]
print(f"Found label types: {available_labels}")  # e.g., ['cuboids', 'semseg']

samples = []
for frame_idx in range(frame_count):
    frame_id = f"{frame_idx:02d}"
    group = fo.Group()

    # === Add camera images ===
    for cam_name in camera_names:
        img_path = data_path / "camera" / cam_name / f"{frame_id}.jpg"
        if img_path.exists():
            sample = fo.Sample(filepath=str(img_path))
            sample["group"] = group.element(cam_name)
            sample["frame_idx"] = frame_idx
            samples.append(sample)

    # === Convert and add LiDAR point cloud ===
    lidar_pkl = data_path / "lidar" / f"{frame_id}.pkl.gz"
    if lidar_pkl.exists():
        # Load pickle
        with gzip.open(lidar_pkl, 'rb') as f:
            lidar_data = pickle.load(f)

        # Extract points (adjust based on actual data structure)
        if isinstance(lidar_data, dict):
            points = lidar_data.get('points', lidar_data.get('data'))
        else:
            points = np.array(lidar_data)

        # Convert to PCD
        pcd_path = pcd_output_dir / f"{frame_id}.pcd"
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(points[:, :3])
        o3d.io.write_point_cloud(str(pcd_path), pcd)

        # Create 3D sample with scene
        lidar_sample = fo.Sample(filepath=str(pcd_path))
        lidar_sample["group"] = group.element("lidar")
        lidar_sample["frame_idx"] = frame_idx

        # === Load 3D cuboid labels if available ===
        # IMPORTANT: Store 3D attributes as flat scalar fields, NOT lists
        # Using lists (e.g., location=[x,y,z]) causes "Symbol.iterator" errors in 3D viewer
        if "cuboids" in available_labels:
            cuboids_pkl = labels_dir / "cuboids" / f"{frame_id}.pkl.gz"
            if cuboids_pkl.exists():
                with gzip.open(cuboids_pkl, 'rb') as f:
                    cuboids_df = pickle.load(f)  # PandaSet uses pandas DataFrame

                detections = []
                for _, row in cuboids_df.iterrows():
                    detection = fo.Detection(
                        label=row.get("label", "object"),
                        bounding_box=[0, 0, 0.01, 0.01],  # minimal 2D placeholder
                    )
                    # Store 3D attributes as FLAT SCALAR fields (not lists!)
                    detection["pos_x"] = float(row.get("position.x", 0))
                    detection["pos_y"] = float(row.get("position.y", 0))
                    detection["pos_z"] = float(row.get("position.z", 0))
                    detection["dim_x"] = float(row.get("dimensions.x", 1))
                    detection["dim_y"] = float(row.get("dimensions.y", 1))
                    detection["dim_z"] = float(row.get("dimensions.z", 1))
                    detection["yaw"] = float(row.get("yaw", 0))
                    detection["track_id"] = str(row.get("uuid", ""))
                    detection["stationary"] = bool(row.get("stationary", False))
                    detections.append(detection)

                lidar_sample["ground_truth"] = fo.Detections(detections=detections)

        # === Load semantic segmentation if available ===
        if "semseg" in available_labels:
            semseg_pkl = labels_dir / "semseg" / f"{frame_id}.pkl.gz"
            if semseg_pkl.exists():
                with gzip.open(semseg_pkl, 'rb') as f:
                    semseg_data = pickle.load(f)
                # Store as custom field (point-wise labels)
                lidar_sample["point_labels"] = semseg_data.tolist() if hasattr(semseg_data, 'tolist') else semseg_data

        samples.append(lidar_sample)

# Add all samples
dataset.add_samples(samples)
dataset.save()

print(f"Imported {len(dataset)} groups with {len(dataset.select_group_slices())} total samples")
print(f"Slices: {dataset.group_slices}")
print(f"Labels imported: {available_labels}")


Dynamic Import Discovery: If no example exists for the format:

Search: "FiftyOne import example"
Search: " devkit python example"
Read the devkit documentation to understand data structure
Explore the annotation files to understand label format:
import pickle, gzip
with gzip.open("annotations/cuboids/00.pkl.gz", "rb") as f:
    data = pickle.load(f)
print(type(data), data[0] if isinstance(data, list) else data)

Build custom import code based on the devkit API and label structure
Step 10: Import Additional Labels (Optional)

If labels weren't imported with the specialized format, add them separately:

# For COCO labels that reference filepaths
execute_operator(
    operator_uri="@voxel51/io/import_samples",
    params={
        "import_type": "LABELS_ONLY",
        "dataset_type": "COCO",
        "labels_path": {"absolute_path": "/path/to/annotations.json"},
        "label_field": "ground_truth"
    }
)

Step 11: Validate Import
# Load and verify
load_dataset(name="my-dataset")

# Check counts match
dataset_summary(name="my-dataset")


Compare:

Imported samples vs source files
Groups created vs expected
Labels imported vs annotation count
Step 12: Launch App and View
launch_app(dataset_name="my-dataset")

# For grouped datasets, view different slices
# In the App, use the slice selector dropdown

Supported Dataset Types
Media Types
Type	Extensions	Description
image	.jpg, .jpeg, .png, .gif, .bmp, .webp, .tiff	Static images
video	.mp4, .avi, .mov, .mkv, .webm	Video files with frames
point-cloud	.pcd, .ply, .las, .laz	3D point cloud data
3d	.fo3d, .obj, .gltf, .glb	3D scenes and meshes
Label Formats
Format	Dataset Type Value	Label Types	File Pattern
COCO	COCO	detections, segmentations, keypoints	*.json
VOC/Pascal	VOC	detections	*.xml per image
KITTI	KITTI	detections	*.txt per image
YOLOv4	YOLOv4	detections	*.txt + classes.txt
YOLOv5	YOLOv5	detections	data.yaml + labels/*.txt
CVAT Image	CVAT Image	classifications, detections, polylines, keypoints	Single *.xml
CVAT Video	CVAT Video	frame labels	XML directory
OpenLABEL Image	OpenLABEL Image	all types	*.json directory
OpenLABEL Video	OpenLABEL Video	all types	*.json directory
TF Object Detection	TF Object Detection	detections	TFRecords
TF Image Classification	TF Image Classification	classification	TFRecords
Image Classification Tree	Image Classification Directory Tree	classification	Folder per class
Video Classification Tree	Video Classification Directory Tree	classification	Folder per class
Image Segmentation	Image Segmentation	segmentation	Mask images
CSV	CSV	custom fields	*.csv
DICOM	DICOM	medical metadata	.dcm files
GeoJSON	GeoJSON	geolocation	*.json
GeoTIFF	GeoTIFF	geolocation	.tiff with geo
FiftyOne Dataset	FiftyOne Dataset	all types	Exported format
Common Use Cases
Use Case 1: Simple Image Dataset with COCO Labels
# Scan directory
# Found: 5000 images, annotations.json (COCO format)

execute_operator(
    operator_uri="@voxel51/utils/create_dataset",
    params={"name": "coco-dataset", "persistent": true}
)

set_context(dataset_name="coco-dataset")

execute_operator(
    operator_uri="@voxel51/io/import_samples",
    params={
        "import_type": "MEDIA_AND_LABELS",
        "dataset_type": "COCO",
        "data_path": {"absolute_path": "/path/to/images"},
        "labels_path": {"absolute_path": "/path/to/annotations.json"},
        "label_field": "ground_truth"
    }
)

launch_app(dataset_name="coco-dataset")

Use Case 2: YOLO Dataset
# Scan directory
# Found: data.yaml, images/, labels/ (YOLOv5 format)

execute_operator(
    operator_uri="@voxel51/utils/create_dataset",
    params={"name": "yolo-dataset", "persistent": true}
)

set_context(dataset_name="yolo-dataset")

execute_operator(
    operator_uri="@voxel51/io/import_samples",
    params={
        "import_type": "MEDIA_AND_LABELS",
        "dataset_type": "YOLOv5",
        "dataset_dir": {"absolute_path": "/path/to/yolo/dataset"},
        "label_field": "ground_truth"
    }
)

launch_app(dataset_name="yolo-dataset")

Use Case 3: Point Cloud Dataset
# Scan directory
# Found: 1000 .pcd files, labels/ with KITTI format

execute_operator(
    operator_uri="@voxel51/utils/create_dataset",
    params={"name": "lidar-dataset", "persistent": true}
)

set_context(dataset_name="lidar-dataset")

# Import point clouds
execute_operator(
    operator_uri="@voxel51/io/import_samples",
    params={
        "import_type": "MEDIA_ONLY",
        "style": "GLOB_PATTERN",
        "glob_patt": {"absolute_path": "/path/to/data/*.pcd"}
    }
)

launch_app(dataset_name="lidar-dataset")

Use Case 4: Autonomous Driving (Multimodal Groups)

This is the most complex case - multiple cameras + LiDAR per scene:

import fiftyone as fo
from pathlib import Path

# Create dataset with group support
dataset = fo.Dataset("driving-dataset", persistent=True)
dataset.add_group_field("group", default="front_camera")

data_dir = Path("/path/to/driving_data")
samples = []

# Process each scene folder
for scene_dir in sorted(data_dir.iterdir()):
    if not scene_dir.is_dir():
        continue

    group = fo.Group()

    # Map files to slices
    slice_mapping = {
        "front": "front_camera",
        "left": "left_camera",
        "right": "right_camera",
        "rear": "rear_camera",
        "lidar": "lidar",
        "radar": "radar"
    }

    for file in scene_dir.iterdir():
        # Determine slice from filename
        for key, slice_name in slice_mapping.items():
            if key in file.stem.lower():
                samples.append(fo.Sample(
                    filepath=str(file),
                    group=group.element(slice_name)
                ))
                break

dataset.add_samples(samples)
dataset.save()

print(f"Created {len(dataset.distinct('group.id'))} groups")
print(f"Slices: {dataset.group_slices}")
print(f"Media types: {dataset.group_media_types}")

# Launch app
session = fo.launch_app(dataset)

Use Case 5: Classification Directory Tree
# Scan directory
# Found: cats/, dogs/, birds/ folders with images inside

execute_operator(
    operator_uri="@voxel51/utils/create_dataset",
    params={"name": "classification-dataset", "persistent": true}
)

set_context(dataset_name="classification-dataset")

execute_operator(
    operator_uri="@voxel51/io/import_samples",
    params={
        "import_type": "MEDIA_AND_LABELS",
        "dataset_type": "Image Classification Directory Tree",
        "dataset_dir": {"absolute_path": "/path/to/classification"},
        "label_field": "ground_truth"
    }
)

launch_app(dataset_name="classification-dataset")

Use Case 6: Mixed Media (Images + Videos)
# Scan directory
# Found: images/, videos/ folders

# Create dataset
execute_operator(
    operator_uri="@voxel51/utils/create_dataset",
    params={"name": "mixed-media", "persistent": true}
)

set_context(dataset_name="mixed-media")

# Import images
execute_operator(
    operator_uri="@voxel51/io/import_samples",
    params={
        "import_type": "MEDIA_ONLY",
        "style": "DIRECTORY",
        "directory": {"absolute_path": "/path/to/images"},
        "tags": ["image"]
    }
)

# Import videos
execute_operator(
    operator_uri="@voxel51/io/import_samples",
    params={
        "import_type": "MEDIA_ONLY",
        "style": "DIRECTORY",
        "directory": {"absolute_path": "/path/to/videos"},
        "tags": ["video"]
    }
)

launch_app(dataset_name="mixed-media")

Working with Groups
Understanding Group Structure

In a grouped dataset:

Each group represents one scene/moment (e.g., one timestamp)
Each slice represents one modality (e.g., left camera, lidar)
All samples in a group share the same group.id
Each sample has a group.name indicating its slice
# Access group information
print(dataset.group_slices)        # ['front_camera', 'left_camera', 'lidar']
print(dataset.group_media_types)   # {'front_camera': 'image', 'lidar': 'point-cloud'}
print(dataset.default_group_slice) # 'front_camera'

# Iterate over groups
for group in dataset.iter_groups():
    print(f"Group has {len(group)} slices")
    for slice_name, sample in group.items():
        print(f"  {slice_name}: {sample.filepath}")

# Get specific slice view
front_images = dataset.select_group_slices("front_camera")
all_point_clouds = dataset.select_group_slices(media_type="point-cloud")

Viewing Groups in the App

After launching the app:

The slice selector dropdown appears in the top bar
Select different slices to view each modality
Samples are synchronized - selecting a sample shows all its group members
Use the grid view to see multiple slices side by side
Importing from Hugging Face Hub

For complete HF Hub import documentation, see HF-HUB-IMPORT.md.

Quick reference:

Dataset Type	Method
FiftyOne-formatted (fiftyone.yml)	load_from_hub("repo_id")
Parquet-based	load_from_hub("repo_id", format="ParquetFilesDataset", filepath="image")
COCO/YOLO/VOC on HF	snapshot_download() → local import
Rate limited (>10K)	Parquet extraction fallback (see HF-HUB-IMPORT.md)

Quick start:

from fiftyone.utils.huggingface import load_from_hub

# FiftyOne-formatted dataset
dataset = load_from_hub("Voxel51/VisDrone2019-DET", persistent=True)

# Generic parquet dataset
dataset = load_from_hub(
    "username/dataset",
    format="ParquetFilesDataset",
    filepath="image",
    classification_fields="label",
    persistent=True,
)

Troubleshooting

Error: "Dataset already exists"

Use a different dataset name
Or delete existing: execute_operator("@voxel51/utils/delete_dataset", {"name": "dataset-name"})

Error: "No samples found"

Verify directory path is correct and accessible
Check file extensions are supported
For nested directories, ensure recursive scanning

Error: "Labels path not found"

Verify labels file/directory exists
Check path is absolute, not relative
Ensure correct format is detected

Error: "Invalid group configuration"

Each group must have at least one sample
Slice names must be consistent across groups
Only one 3d slice allowed per group

Import is slow

For large datasets, use delegated execution
Import in batches if needed
Consider using glob patterns to filter files

Point clouds not rendering

Ensure .pcd files are valid
Check FiftyOne 3D visualization is enabled
Verify point cloud plugin is installed

Groups not detected

Check folder structure matches expected patterns
Verify consistent naming across scenes
May need to specify grouping manually
Best Practices
Always scan first - Understand the data before importing
Confirm with user - Present findings before creating dataset
Use descriptive names - Dataset names and label fields should be meaningful
Validate counts - Ensure imported samples match source files
Handle errors gracefully - Report issues clearly, continue with valid files
Use groups for multimodal - Don't flatten data that should be grouped
Set appropriate default slice - Choose the most commonly viewed modality
Tag imports - Use tags to track import batches or sources
Performance Notes

Import time estimates:

1,000 images: ~10-30 seconds
10,000 images: ~2-5 minutes
100,000 images: ~20-60 minutes
Point clouds: ~2x slower than images
Videos: Depends on frame extraction settings

Memory requirements:

~1KB per sample metadata
Media files are referenced, not loaded into memory
Large datasets may require increased MongoDB limits
Resources
FiftyOne Dataset Import Guide
Grouped Datasets Guide
Point Cloud Support
Supported Dataset Formats
FiftyOne I/O Plugin
FiftyOne Hugging Face Integration
Hugging Face Hub Documentation
Weekly Installs
14
Repository
voxel51/fiftyone-skills
GitHub Stars
25
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn