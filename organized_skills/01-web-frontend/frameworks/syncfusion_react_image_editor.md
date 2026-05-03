---
rating: ⭐⭐
title: syncfusion-react-image-editor
url: https://skills.sh/syncfusion/react-ui-components-skills/syncfusion-react-image-editor
---

# syncfusion-react-image-editor

skills/syncfusion/react-ui-components-skills/syncfusion-react-image-editor
syncfusion-react-image-editor
Installation
$ npx skills add https://github.com/syncfusion/react-ui-components-skills --skill syncfusion-react-image-editor
SKILL.md
Implementing Syncfusion React Image Editor

The Syncfusion React Image Editor is a comprehensive, feature-rich component for editing images directly in your React applications. It provides an intuitive interface with powerful tools for transformations, annotations, effects, and more.

Component Overview

The Image Editor combines a canvas-based editing environment with a comprehensive toolbar and contextual tools. It supports:

Multiple Input Sources: Files, URLs, base64, blobs, file managers, treeviews
Rich Annotation Support: Text (with styling), shapes, freehand drawings, watermarks
Professional Effects: Filters and fine-tuning controls
Advanced Operations: Z-order management, redaction, frame decoration
Accessibility First: Full keyboard navigation, WCAG compliance, RTL support, 120+ localization keys
Flexible Integration: Standalone or within dialogs, with customizable toolbars
Documentation and Navigation Guide
🔹 API Reference

📄 Read: references/api.md

Complete API documentation with all properties, methods, and events
Properties overview (core, toolbar, settings)
Methods for image operations, transformations, annotations
Events for lifecycle, interactions, effects, and toolbars
Enums and type definitions (ArrowheadType, FrameType, RedactType, etc.)
Complete working examples with verified method signatures
Getting Started

📄 Read: references/getting-started.md

Installation with Vite and create-react-app
CSS imports and theme setup
Basic component initialization
Setting width, height, and initial rendering
Opening and Saving Images

📄 Read: references/opening-saving-images.md

Open from file paths, URLs, base64 strings, blobs
Open from file uploader, file manager, and treeview
Save/export as PNG, JPEG, SVG, WEBP
Image dimensions and aspect ratio control
File opened, saving, and lifecycle events
Selection and Cropping

📄 Read: references/selection-cropping.md

Insert custom, square, and circle selections
Crop with aspect ratios (2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 5:7, 7:5, 9:16, 16:9)
Crop method and selection events
Maintain original image size during cropping
Lock selection area during resizing
Transform: Rotate, Flip, and Straighten

📄 Read: references/transform-rotate-flip.md

Rotate clockwise/counter-clockwise by degrees
Flip horizontally and vertically
Straighten images with fine degree adjustments (-45° to +45°)
Transform annotations along with image
Rotating and flipping events
Zoom and Pan Operations

📄 Read: references/zooming-panning.md

Zoom in/out with configurable min/max factors
Pan when zoomed or during cropping
Zoom triggers (toolbar, pinch, mouse wheel, keyboard)
Zooming and panning events
Zoom point calculations
Text Annotations

📄 Read: references/text-annotations.md

Add text with position, content, and font settings
Text styling (bold, italic, underline, strikethrough)
Font families, sizes, and colors
Multiline text with newline characters
Delete text annotations
Customize font color via shapeChanging event
Freehand Drawing

📄 Read: references/freehand-drawing.md

Enable/disable freehand drawing mode
Customize stroke width and color
Delete freehand annotations
Adjust stroke during drawing via shapeChanging event
Shape Annotations

📄 Read: references/shape-annotations.md

Draw rectangles, ellipses, lines, arrows, and paths
Customize shapes with stroke color, stroke width, and fill color
Rotate shapes with degree parameter
Delete shape annotations
Customize default stroke colors
Shape changing and customization events
Image Annotations

📄 Read: references/image-annotations.md

Add images or icons as annotations
Control position, size, rotation, and opacity
Aspect ratio preservation
Watermarks and decorative elements
Filters

📄 Read: references/filters.md

Apply predefined filters (Chrome, Cold, Warm, Grayscale, Sepia, Invert)
Image filtering event
Reset filter to original
Fine-Tuning

📄 Read: references/finetune.md

Adjust brightness, contrast, saturation
Control hue, exposure, blur, opacity
Finetune value changing events
Real-time adjustments with sliders
Undo and Redo

📄 Read: references/undo-redo.md

Undo/redo operations with 16-step history
Keyboard shortcuts (Ctrl+Z, Ctrl+Y)
History management and limits
Toolbar Customization

📄 Read: references/toolbar-customization.md

Built-in toolbar items (20+ default tools)
Add, remove, enable, disable toolbar items
Custom toolbar items with event handlers
Contextual toolbar for annotations
Toolbar templates for complete customization
Toolbar created and item clicked events
Quick Access Toolbar

📄 Read: references/quick-access-toolbar.md

Quick access toolbar for annotations
Show/hide quick access toolbar
Add custom items to quick access toolbar
Quick access toolbar open event
Resize Image

📄 Read: references/resize-image.md

Resize with or without aspect ratio
Width and height parameters
Resizing event with before/after dimensions
Frame Decoration

📄 Read: references/frame-decoration.md

Apply frames (Mat, Bevel, Line, Inset, Hook)
Customize frame color, size, and line style
Frame changing event
Z-Order Layering

📄 Read: references/z-order-layering.md

Bring forward/send backward annotations
Bring to front/send to back
Manage annotation layer order
Redact Sensitive Information

📄 Read: references/redact-sensitive-info.md

Blur sensitive areas
Pixelate sensitive information
Redact CRUD operations (select, update, delete, get)
Privacy and compliance
Accessibility and Localization

📄 Read: references/accessibility-localization.md

WCAG 2.2, Section 508 compliance
Screen reader support
Keyboard shortcuts (Ctrl+Z, Ctrl+S, Ctrl+O, Delete, Enter, Escape)
RTL language support
Localization with 120+ locale keys
Image Restrictions and Validation

📄 Read: references/image-restrictions-validation.md

Allowed file extensions (.jpg, .png, .svg, .webp, .bmp)
Min and max file size restrictions
File validation and error alerts
Clear Image

📄 Read: references/clear-image.md

Clear editor state
Dialog reuse patterns
Remove previously loaded images
Fit to Width and Height

📄 Read: references/fit-width-height.md

Fit image to editor container width
Fit image to editor container height
Zoom calculations for perfect fit
Render in Dialog

📄 Read: references/render-in-dialog.md

Render Image Editor within Dialog component
Content template integration
Dialog show/hide patterns
Reset Image

📄 Read: references/reset-image.md

Reset all modifications to original state
Restore unmodified version
Clear annotations and effects
Quick Start Example
import { ImageEditorComponent } from '@syncfusion/ej2-react-image-editor';
import React from 'react';

function App() {
  let imgObj: ImageEditorComponent;

  function imageEditorCreated(): void {
    imgObj.open('https://ej2.syncfusion.com/react/documentation/image-editor/images/bridge.jpeg');
  }

  return (
    <div>
      <ImageEditorComponent
        ref={(img) => { imgObj = img }}
        width="550px"
        height="350px"
        created={imageEditorCreated}
      />
    </div>
  );
}

export default App;

Common Patterns
Pattern 1: Open + Edit + Save Workflow
Open image via open() method
Apply transformations, annotations, or effects
Use export() to save as PNG/JPEG/SVG/WEBP
Optionally convert to base64 or blob for backend storage
Pattern 2: Responsive Toolbar
Define custom toolbar items in toolbar property
Handle clicks via toolbarItemClicked event
Execute methods like rotate(), zoom(), drawText() based on clicked item
Update contextual toolbar via toolbarUpdating event
Pattern 3: Annotation Workflow
Enable annotation mode (freehand, text, shape)
Customize via shapeChanging event (color, stroke, font)
Delete via deleteShape() with shape ID
Manage layers via z-order methods
Pattern 4: Dialog Integration
Render Image Editor in Dialog's content template
Load image when dialog opens via fileOpened event
Call clearImage() before closing dialog
Retrieve edited image data via export() or getImageData()
Pattern 5: Filter + Finetune Pipeline
Apply filter via applyImageFilter()
Fine-tune via finetuneImage() (brightness, contrast, etc.)
Listen to imageFiltering and finetuneValueChanging events
Combine effects for professional results
Key Properties
Property	Type	Purpose
width	string	Editor canvas width (e.g., "550px", "100%")
height	string	Editor canvas height (e.g., "350px", "100%")
toolbar	array	Customize toolbar items and visibility
fontFamily	object	Add custom font families
uploadSettings	object	Configure file restrictions (extensions, size)
zoomSettings	object	Set min/max zoom factors
showQuickAccessToolbar	boolean	Show/hide quick access toolbar
locale	string	Set localization (e.g., 'de-DE')
Key Events
Event	Trigger	Use Case
created	Component initialized	Load image on startup
fileOpened	Image loaded	Add watermarks, apply defaults
beforeSave	Before export	Validate, add metadata
cropping	During crop	Prevent scaling, lock dimensions
zooming	During zoom	Validate zoom level
rotating	During rotate	Track rotation angle
shapeChanging	Annotation modified	Customize stroke, font
toolbarUpdating	Toolbar rendered	Add/remove contextual items
Supported File Formats

Open: PNG, JPEG, JPG, SVG, WEBP, BMP (local, URL, base64, blob) Save/Export: PNG, JPEG, SVG, WEBP

Next Steps
Start with getting-started.md for setup
Explore opening-saving-images.md to understand data flow
Check specific features in their dedicated reference files
Use accessibility-localization.md for multi-language support
Weekly Installs
81
Repository
syncfusion/reac…s-skills
GitHub Stars
1
First Seen
Mar 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass