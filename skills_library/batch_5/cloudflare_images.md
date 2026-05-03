---
title: cloudflare-images
url: https://skills.sh/jezweb/claude-skills/cloudflare-images
---

# cloudflare-images

skills/jezweb/claude-skills/cloudflare-images
cloudflare-images
Installation
$ npx skills add https://github.com/jezweb/claude-skills --skill cloudflare-images
Summary

Store, transform, and deliver images at scale with Cloudflare Images API and URL-based transformations.

Upload images via API, direct creator URLs, or external sources; serve via imagedelivery.net with optional signed URLs for private access
Transform any image on-the-fly using /cdn-cgi/image/ parameters (resize, crop, quality, format auto-detection) or Workers cf.image object
Create up to 100 named variants for common transformations; use flexible variants for dynamic parameters (incompatible with signed URLs)
AI face detection (gravity=face with zoom control) for smart cropping; preserve image provenance with Content Credentials (C2PA standard)
Prevent 16 documented issues including CORS failures, direct upload timeouts, metadata stripping, AVIF resolution limits, and cache behavior quirks
SKILL.md
Cloudflare Images

Status: Production Ready ✅ Last Updated: 2026-01-21 Dependencies: Cloudflare account with Images enabled Latest Versions: Cloudflare Images API v2, @cloudflare/workers-types@4.20260108.0

Recent Updates (2025):

February 2025: Content Credentials support (C2PA standard) - preserve image provenance chains, automatic cryptographic signing of transformations
August 2025: AI Face Cropping GA (gravity=face with zoom control, GPU-based RetinaFace, 99.4% precision)
May 2025: Media Transformations origin restrictions (default: same-domain only, configurable via dashboard)
Upcoming: Background removal, generative upscale (planned features)

Deprecation Notice: Mirage deprecated September 15, 2025. Migrate to Cloudflare Images for storage/transformations or use native <img loading="lazy"> for lazy loading.

Overview

Two features: Images API (upload/store with variants) and Image Transformations (resize any image via URL or Workers).

Quick Start

1. Enable: Dashboard → Images → Get Account ID + API token (Cloudflare Images: Edit permission)

2. Upload:

curl -X POST https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/images/v1 \
  -H 'Authorization: Bearer <API_TOKEN>' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@./image.jpg'


3. Serve: https://imagedelivery.net/<ACCOUNT_HASH>/<IMAGE_ID>/public

4. Transform (optional): Dashboard → Images → Transformations → Enable for zone

<img src="/cdn-cgi/image/width=800,quality=85/uploads/photo.jpg" />

Upload Methods

1. File Upload: POST to /images/v1 with file (multipart/form-data), optional id, requireSignedURLs, metadata

2. Upload via URL: POST with url=https://example.com/image.jpg (supports HTTP basic auth)

3. Direct Creator Upload (one-time URLs, no API key exposure):

Backend: POST to /images/v2/direct_upload → returns uploadURL Frontend: POST file to uploadURL with FormData

CRITICAL CORS FIX:

✅ Use multipart/form-data (let browser set header)
✅ Name field file (NOT image)
✅ Call /direct_upload from backend only
❌ Don't set Content-Type: application/json
❌ Don't call /direct_upload from browser
Image Transformations

URL: /cdn-cgi/image/<OPTIONS>/<SOURCE>

Sizing: width=800,height=600,fit=cover
Quality: quality=85 (1-100)
Format: format=auto (WebP/AVIF auto-detection)
Cropping: gravity=auto (smart crop), gravity=face (AI face detection, Aug 2025 GA), gravity=center, zoom=0.5 (0-1 range, face crop tightness)
Effects: blur=10,sharpen=3,brightness=1.2
Fit: scale-down, contain, cover, crop, pad

Workers: Use cf.image object in fetch

fetch(imageURL, {
  cf: {
    image: { width: 800, quality: 85, format: 'auto', gravity: 'face', zoom: 0.8 }
  }
});

Variants

Named Variants (up to 100): Predefined transformations (e.g., avatar, thumbnail)

Create: POST to /images/v1/variants with id, options
Use: imagedelivery.net/<HASH>/<ID>/avatar
Works with signed URLs

Flexible Variants: Dynamic params in URL (w=400,sharpen=3)

Enable: PATCH /images/v1/config with {"flexible_variants": true}
❌ Cannot use with signed URLs (use named variants instead)
Signed URLs

Generate HMAC-SHA256 tokens for private images (URL format: ?exp=<TIMESTAMP>&sig=<HMAC>).

Algorithm: HMAC-SHA256(signingKey, imageId + variant + expiry) → hex signature

See: templates/signed-urls-generation.ts for Workers implementation

Critical Rules
Always Do

✅ Use multipart/form-data for Direct Creator Upload ✅ Name the file field file (not image or other names) ✅ Call /direct_upload API from backend only (NOT browser) ✅ Use HTTPS URLs for transformations (HTTP not supported) ✅ URL-encode special characters in image paths ✅ Enable transformations on zone before using /cdn-cgi/image/ ✅ Use named variants for private images (signed URLs) ✅ Check Cf-Resized header for transformation errors ✅ Set format=auto for automatic WebP/AVIF conversion ✅ Use fit=scale-down to prevent unwanted enlargement

Never Do

❌ Use application/json Content-Type for file uploads ❌ Call /direct_upload from browser (CORS will fail) ❌ Use flexible variants with requireSignedURLs=true ❌ Resize SVG files (they're inherently scalable) ❌ Use HTTP URLs for transformations (HTTPS only) ❌ Put spaces or unescaped Unicode in URLs ❌ Transform the same image multiple times in Workers (causes 9403 loop) ❌ Exceed 100 megapixels image size ❌ Use /cdn-cgi/image/ endpoint in Workers (use cf.image instead) ❌ Forget to enable transformations on zone before use

Known Issues Prevention

This skill prevents 16 documented issues.

Issue #1: Direct Creator Upload CORS Error

Error: Access to XMLHttpRequest blocked by CORS policy: Request header field content-type is not allowed

Source: Cloudflare Community #345739, #368114

Why It Happens: Server CORS settings only allow multipart/form-data for Content-Type header

Prevention:

// ✅ CORRECT
const formData = new FormData();
formData.append('file', fileInput.files[0]);
await fetch(uploadURL, {
  method: 'POST',
  body: formData // Browser sets multipart/form-data automatically
});

// ❌ WRONG
await fetch(uploadURL, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' }, // CORS error
  body: JSON.stringify({ file: base64Image })
});

Issue #2: Error 5408 - Upload Timeout

Error: Error 5408 after ~15 seconds of upload

Source: Cloudflare Community #571336

Why It Happens: Cloudflare has 30-second request timeout; slow uploads or large files exceed limit

Prevention:

Compress images before upload (client-side with Canvas API)
Use reasonable file size limits (e.g., max 10MB)
Show upload progress to user
Handle timeout errors gracefully
const MAX_FILE_SIZE = 10 * 1024 * 1024; // 10MB

if (file.size > MAX_FILE_SIZE) {
  alert('File too large. Please select an image under 10MB.');
  return;
}

Issue #3: Error 400 - Invalid File Parameter

Error: 400 Bad Request with unhelpful error message

Source: Cloudflare Community #487629

Why It Happens: File field must be named file (not image, photo, etc.)

Prevention:

// ✅ CORRECT
formData.append('file', imageFile);

// ❌ WRONG
formData.append('image', imageFile); // 400 error
formData.append('photo', imageFile); // 400 error

Issue #4: CORS Preflight Failures

Error: Preflight OPTIONS request blocked

Source: Cloudflare Community #306805

Why It Happens: Calling /direct_upload API directly from browser (should be backend-only)

Prevention:

ARCHITECTURE:
Browser → Backend API → POST /direct_upload → Returns uploadURL → Browser uploads to uploadURL


Never expose API token to browser. Generate upload URL on backend, return to frontend.

Issue #5: Error 9401 - Invalid Arguments

Error: Cf-Resized: err=9401 - Required cf.image options missing or invalid

Source: Cloudflare Images Docs - Troubleshooting

Why It Happens: Missing required transformation parameters or invalid values

Prevention:

// ✅ CORRECT
fetch(imageURL, {
  cf: {
    image: {
      width: 800,
      quality: 85,
      format: 'auto'
    }
  }
});

// ❌ WRONG
fetch(imageURL, {
  cf: {
    image: {
      width: 'large', // Must be number
      quality: 150 // Max 100
    }
  }
});

Issue #6: Error 9402 - Image Too Large

Error: Cf-Resized: err=9402 - Image too large or connection interrupted

Source: Cloudflare Images Docs - Troubleshooting

Why It Happens: Image exceeds maximum area (100 megapixels) or download fails

Prevention:

Validate image dimensions before transforming
Use reasonable source images (max 10000x10000px)
Handle network errors gracefully
Issue #7: Error 9403 - Request Loop

Error: Cf-Resized: err=9403 - Worker fetching its own URL or already-resized image

Source: Cloudflare Images Docs - Troubleshooting

Why It Happens: Transformation applied to already-transformed image, or Worker fetches itself

Prevention:

// ✅ CORRECT
if (url.pathname.startsWith('/images/')) {
  const originalPath = url.pathname.replace('/images/', '');
  const originURL = `https://storage.example.com/${originalPath}`;
  return fetch(originURL, { cf: { image: { width: 800 } } });
}

// ❌ WRONG
if (url.pathname.startsWith('/images/')) {
  // Fetches worker's own URL, causes loop
  return fetch(request, { cf: { image: { width: 800 } } });
}

Issue #8: Error 9406/9419 - Invalid URL Format

Error: Cf-Resized: err=9406 or err=9419 - Non-HTTPS URL or URL has spaces/unescaped Unicode

Source: Cloudflare Images Docs - Troubleshooting

Why It Happens: Image URL uses HTTP (not HTTPS) or contains invalid characters

Prevention:

// ✅ CORRECT
const imageURL = "https://example.com/images/photo%20name.jpg";

// ❌ WRONG
const imageURL = "http://example.com/images/photo.jpg"; // HTTP not allowed
const imageURL = "https://example.com/images/photo name.jpg"; // Space not encoded


Always use encodeURIComponent() for URL paths:

const filename = "photo name.jpg";
const imageURL = `https://example.com/images/${encodeURIComponent(filename)}`;

Issue #9: Error 9412 - Non-Image Response

Error: Cf-Resized: err=9412 - Origin returned HTML instead of image

Source: Cloudflare Images Docs - Troubleshooting

Why It Happens: Origin server returns 404 page or error page (HTML) instead of image

Prevention:

// Verify URL before transforming
const originResponse = await fetch(imageURL, { method: 'HEAD' });
const contentType = originResponse.headers.get('content-type');

if (!contentType?.startsWith('image/')) {
  return new Response('Not an image', { status: 400 });
}

return fetch(imageURL, { cf: { image: { width: 800 } } });

Issue #10: Error 9413 - Max Image Area Exceeded

Error: Cf-Resized: err=9413 - Image exceeds 100 megapixels

Source: Cloudflare Images Docs - Troubleshooting

Why It Happens: Source image dimensions exceed 100 megapixels (e.g., 10000x10000px)

Prevention:

Validate image dimensions before upload
Pre-process oversized images
Reject images above threshold
const MAX_MEGAPIXELS = 100;

if (width * height > MAX_MEGAPIXELS * 1_000_000) {
  return new Response('Image too large', { status: 413 });
}

Issue #11: Flexible Variants + Signed URLs Incompatibility

Error: Flexible variants don't work with private images

Source: Cloudflare Images Docs - Enable flexible variants

Why It Happens: Flexible variants cannot be used with requireSignedURLs=true

Prevention:

// ✅ CORRECT - Use named variants for private images
await uploadImage({
  file: imageFile,
  requireSignedURLs: true // Use named variants: /public, /avatar, etc.
});

// ❌ WRONG - Flexible variants don't support signed URLs
// Cannot use: /w=400,sharpen=3 with requireSignedURLs=true

Issue #12: SVG Resizing Limitation

Error: SVG files don't resize via transformations

Source: Cloudflare Images Docs - SVG files

Why It Happens: SVG is inherently scalable (vector format), resizing not applicable

Prevention:

// SVGs can be served but not resized
// Use any variant name as placeholder
// https://imagedelivery.net/<HASH>/<SVG_ID>/public

// SVG will be served at original size regardless of variant settings

Issue #13: EXIF Metadata Stripped by Format

Error: GPS data, camera settings removed from uploaded images

Source: Cloudflare Images Docs - Transform via URL

Why It Happens: Default behavior strips all metadata except copyright. CRITICAL: WebP and PNG output formats ALWAYS discard metadata regardless of settings - only JPEG supports metadata preservation.

Prevention:

// ✅ CORRECT - JPEG preserves metadata
fetch(imageURL, {
  cf: {
    image: {
      width: 800,
      format: 'jpeg', // or 'auto' (may become jpeg)
      metadata: 'keep' // Preserves most EXIF including GPS
    }
  }
});

// ❌ WRONG - WebP/PNG ignore metadata setting
fetch(imageURL, {
  cf: {
    image: {
      format: 'webp',
      metadata: 'keep' // NO EFFECT - always stripped for WebP/PNG
    }
  }
});


Metadata Options (JPEG only):

none: Strip all metadata
copyright: Keep only copyright tag (default for JPEG)
keep: Preserve most EXIF metadata including GPS

Format Support:

✅ JPEG: All metadata options work
❌ WebP: Always strips metadata (acts as none)
❌ PNG: Always strips metadata (acts as none)
Issue #14: AVIF Resolution Limit Ambiguity

Error: Large AVIF transformations fail or degrade to lower resolution

Source: Cloudflare Docs + Community Report

Why It Happens: Official docs state 1,600px hard limit for format=avif, but community reports indicate practical limit of 1200px for longest side as of late 2024. Note: Discrepancy between official docs (1600px) and reported behavior (1200px) needs verification.

Prevention:

// ✅ RECOMMENDED - Use format=auto instead of explicit avif
fetch(imageURL, {
  cf: {
    image: {
      width: 2000,
      format: 'auto' // Cloudflare chooses best format
    }
  }
});

// ⚠️ MAY FAIL - Explicit AVIF with large dimensions
fetch(imageURL, {
  cf: {
    image: {
      width: 2000,
      format: 'avif' // May fail if >1200px
    }
  }
});

// ✅ WORKAROUND - Use WebP for larger images
if (width > 1200) {
  format = 'webp'; // WebP supports larger dimensions
} else {
  format = 'avif'; // AVIF for smaller images
}

Issue #15: Image Cache by Device Type (Community-reported)

Error: Desktop and mobile see different cached versions, unexpected cache misses

Source: Cloudflare Community

Why It Happens: Images are cached by device type unexpectedly with no configuration option to disable this behavior in cache rules. Multiple users confirm this behavior as of Dec 2024.

Prevention:

Understand that purging cache requires purging for each device type
Use manual cache purging per device type via Cloudflare dashboard
Account for device-specific caching in cache invalidation strategies

Solution/Workaround: Manual cache purging per device type via Cloudflare dashboard when needed.

Issue #16: PNG Not Cached by Default

Error: PNG images not caching despite other image formats working

Source: Cloudflare Community

Why It Happens: Default file extensions cached by Cloudflare do NOT include .png. Default cached extensions: .jpg, .jpeg, .gif, .webp, .bmp, .ico, .svg, .tif, .tiff (PNG is missing).

Prevention: Create explicit cache rule for PNG files:

Dashboard → Caching → Cache Rules
Add rule: URI Path ends with .png → Cache Everything
Using Bundled Resources
Templates (templates/)

Copy-paste ready code for common patterns:

wrangler-images-binding.jsonc - Wrangler configuration (no binding needed)
upload-api-basic.ts - Upload file to Images API
upload-via-url.ts - Ingest image from external URL
direct-creator-upload-backend.ts - Generate one-time upload URLs
direct-creator-upload-frontend.html - User upload form
transform-via-url.ts - URL transformation examples
transform-via-workers.ts - Workers transformation patterns
variants-management.ts - Create/list/delete variants
signed-urls-generation.ts - HMAC-SHA256 signed URL generation
responsive-images-srcset.html - Responsive image patterns
batch-upload.ts - Batch API for high-volume uploads

Usage:

cp templates/upload-api-basic.ts src/upload.ts
# Edit with your account ID and API token

References (references/)

In-depth documentation Claude can load as needed:

api-reference.md - Complete API endpoints (upload, list, delete, variants)
transformation-options.md - All transform params with examples
variants-guide.md - Named vs flexible variants, when to use each
signed-urls-guide.md - HMAC-SHA256 implementation details
direct-upload-complete-workflow.md - Full architecture and flow
responsive-images-patterns.md - srcset, sizes, art direction
format-optimization.md - WebP/AVIF auto-conversion strategies
top-errors.md - All 13+ errors with detailed troubleshooting

When to load:

Deep-dive into specific feature
Troubleshooting complex issues
Understanding API details
Implementing advanced patterns
Scripts (scripts/)

check-versions.sh - Verify API endpoints are current

Advanced Topics

Custom Domains: Serve from your domain via /cdn-cgi/imagedelivery/<HASH>/<ID>/<VARIANT> (requires domain on Cloudflare, proxied). Use Transform Rules for custom paths.

Batch API: High-volume uploads via batch.imagedelivery.net with batch tokens (Dashboard → Images → Batch API)

Webhooks: Notifications for Direct Creator Upload (Dashboard → Notifications → Webhooks). Payload includes imageId, status, metadata.

Content Credentials (C2PA): Cloudflare Images preserves and signs image provenance chains. When transforming images with Content Credentials, Cloudflare automatically appends transformations to the manifest and cryptographically signs them using DigiCert certificates. Enable via Dashboard → Images → Transformations → Preserve Content Credentials. Note: Only works if source images already contain C2PA metadata (certain cameras, DALL-E, compatible editing software). Verify at contentcredentials.org/verify.

Browser Cache TTL: Default Browser Cache TTL is 2 days (172,800 seconds). Customizable from 1 hour to 1 year (account-level or per-variant). Important: Private images (signed URLs) do NOT respect TTL settings. Can cause issues when re-uploading images with same Custom ID - users may see old version for up to 2 days. Solution: Use unique image IDs (append timestamp/hash) or manually purge cache after re-upload.

Product Merge Migration (Nov 2023): Cloudflare merged Image Resizing into Images product with new pricing: $0.50 per 1,000 unique transformations monthly (billing once per 30 days per unique transformation). Migration Gotchas: Old Image Resizing bills based on uncached requests (unpredictable costs due to variable cache behavior). New billing is per "unique transformation" (image ID + params combination), not request count. Same transformation requested 1,000 times/month = billed once. Existing customers can continue using legacy version or migrate voluntarily.

R2 Integration for Cost Optimization: Cloudflare Images is built on R2 + Image Resizing. For cost savings, store original images in R2 and use Image Transformations on-demand:

Upload images to R2 bucket
Serve via custom domain with /cdn-cgi/image/ transformations
No variants stored (transformations are ephemeral/cached)

Cost Comparison:

R2: 10GB storage + unlimited bandwidth (free tier)
Cloudflare Images: $5/month (100k images) + $1 per 100k transformations
R2 + Transformations: R2 storage + $0.50 per 1k unique transformations

Use Case: If you don't need named variants, batch uploads, or Direct Creator Upload features, R2 is more cost-effective.

Example Workers Pattern with R2:

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const imageKey = url.pathname.replace('/images/', '');
    const originURL = `https://r2-bucket.example.com/${imageKey}`;

    return fetch(originURL, {
      cf: {
        image: {
          width: 800,
          quality: 85,
          format: 'auto'
        }
      }
    });
  }
};


Reference: Cloudflare Reference Architecture

Troubleshooting
Problem: Images not transforming

Symptoms: /cdn-cgi/image/... returns original image or 404

Solutions:

Enable transformations on zone: Dashboard → Images → Transformations → Enable for zone
Verify zone is proxied through Cloudflare (orange cloud)
Check source image is publicly accessible
Wait 5-10 minutes for settings to propagate
Problem: Direct upload returns CORS error

Symptoms: Access-Control-Allow-Origin error in browser console

Solutions:

Use multipart/form-data encoding (let browser set Content-Type)
Don't call /direct_upload from browser; call from backend
Name file field file (not image)
Remove manual Content-Type header
Problem: Worker transformations return 9403 loop error

Symptoms: Cf-Resized: err=9403 in response headers

Solutions:

Don't fetch Worker's own URL (use external origin)
Don't transform already-resized images
Check URL routing logic to avoid loops
Problem: Signed URLs not working

Symptoms: 403 Forbidden when accessing signed URL

Solutions:

Verify image uploaded with requireSignedURLs=true
Check signature generation (HMAC-SHA256)
Ensure expiry timestamp is in future
Verify signing key matches dashboard (Images → Keys)
Cannot use flexible variants with signed URLs (use named variants)
Problem: Images uploaded but not appearing

Symptoms: Upload returns 200 OK but image not in dashboard

Solutions:

Check for draft: true in response (Direct Creator Upload)
Wait for upload to complete (check via GET /images/v1/{id})
Verify account ID matches
Check for upload errors in webhooks
Problem: Re-uploaded image still shows old version

Symptoms: Even users who never visited page see old image after re-upload

Solutions:

Use unique image IDs for each upload: const imageId = \${baseId}-${Date.now()}`;`
Set shorter Cache-Control headers (e.g., max-age=86400 for 1 day instead of 30 days)
Manual purge via dashboard after re-upload with same ID
Understand default Browser Cache TTL is 2 days - users may see cached version

Root Cause: Cloudflare respects origin Cache-Control headers. If origin sets long max-age (e.g., 30 days), images remain cached even after re-upload with same ID.

Problem: PNG images not caching

Symptoms: PNG images bypass cache while other formats (JPEG, WebP) cache correctly

Solutions:

Create explicit cache rule: Dashboard → Caching → Cache Rules
Add rule: URI Path ends with .png → Cache Everything
Default cached extensions don't include .png (only .jpg, .jpeg, .gif, .webp, .bmp, .ico, .svg, .tif, .tiff)
Official Documentation
Cloudflare Images: https://developers.cloudflare.com/images/
Get Started: https://developers.cloudflare.com/images/get-started/
Upload Images: https://developers.cloudflare.com/images/upload-images/
Direct Creator Upload: https://developers.cloudflare.com/images/upload-images/direct-creator-upload/
Transform Images: https://developers.cloudflare.com/images/transform-images/
Transform via URL: https://developers.cloudflare.com/images/transform-images/transform-via-url/
Transform via Workers: https://developers.cloudflare.com/images/transform-images/transform-via-workers/
Create Variants: https://developers.cloudflare.com/images/manage-images/create-variants/
Serve Private Images: https://developers.cloudflare.com/images/manage-images/serve-images/serve-private-images/
Troubleshooting: https://developers.cloudflare.com/images/reference/troubleshooting/
API Reference: https://developers.cloudflare.com/api/resources/images/
Package Versions

Last Verified: 2026-01-21 API Version: v2 (direct uploads), v1 (standard uploads) Optional: @cloudflare/workers-types@4.20260108.0

Skill Version: 2.1.0 | Changes: Added 3 new issues (AVIF limits, cache by device, PNG caching), enhanced metadata issue with format details, added Content Credentials, Browser Cache TTL, Product Merge notes, R2 integration pattern, Mirage deprecation notice, and cache troubleshooting guidance. Error count: 13 → 16.

Weekly Installs
334
Repository
jezweb/claude-skills
GitHub Stars
759
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail