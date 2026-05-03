---
rating: ⭐⭐⭐
title: hyva-render-media-image
url: https://skills.sh/hyva-themes/hyva-ai-tools/hyva-render-media-image
---

# hyva-render-media-image

skills/hyva-themes/hyva-ai-tools/hyva-render-media-image
hyva-render-media-image
Installation
$ npx skills add https://github.com/hyva-themes/hyva-ai-tools --skill hyva-render-media-image
SKILL.md
Hyvä Render Image

Generate responsive <picture> elements for Hyvä Theme templates using the \Hyva\Theme\ViewModel\Media view model.

When to Use
Adding images to Hyvä PHTML templates
Creating responsive images with different sources for mobile/desktop
Implementing hero banners, product images, or CMS content images
Optimizing images for Core Web Vitals (LCP, CLS)
Workflow
1. Gather Image Requirements

The user may provide image data in one of these ways:

Option A: Direct values - Ask the user for:

Image path(s) - Location in pub/media/ (e.g., wysiwyg/hero.jpg, catalog/product/...)
Image dimensions - Width and height in pixels
Responsive requirements - Different images for mobile vs desktop?
Image purpose - Hero/LCP image (eager loading) or below-fold (lazy loading)?
Alt text - Meaningful description for accessibility

Option B: PHP variable - The user provides a variable name (e.g., $imageData, $heroImage). Inform the user of the required array structure documented in references/rendering-images.md under ## Image Configuration Format.

2. Generate the Code

Refer to references/rendering-images.md for the complete API reference, code examples, and all configuration options.

Choose the appropriate pattern:

Scenario	Pattern to Use
Single image, literal values	Single Image Example
Single image from variable	Wrap in array: [$imageData]
Multiple images from variable	Pass directly: $images
Different images for mobile/desktop	Responsive Images with Media Queries
Need to style the <picture> wrapper	Picture Element Attributes

Base template:

<?php
/** @var \Hyva\Theme\ViewModel\Media $mediaViewModel */
$mediaViewModel = $viewModels->require(\Hyva\Theme\ViewModel\Media::class);

echo $mediaViewModel->getResponsivePictureHtml(
    $images,        // Array of image configs (see reference for format)
    $imgAttributes, // Optional: alt, class, loading, fetchpriority
    $pictureAttributes // Optional: class, data-* attributes for <picture>
);

3. Set Loading Strategy
Image Type	Attributes
Hero/LCP (above fold)	'loading' => 'eager', 'fetchpriority' => 'high'
Below fold	'loading' => 'lazy'
Resources
references/rendering-images.md - Complete API reference with method signature, all configuration options, code examples, and best practices
Weekly Installs
305
Repository
hyva-themes/hyv…ai-tools
GitHub Stars
65
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass