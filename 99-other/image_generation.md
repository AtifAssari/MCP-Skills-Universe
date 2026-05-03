---
title: image-generation
url: https://skills.sh/answerzhao/agent-skills/image-generation
---

# image-generation

skills/answerzhao/agent-skills/image-generation
image-generation
Installation
$ npx skills add https://github.com/answerzhao/agent-skills --skill image-generation
SKILL.md
Image Generation Skill

This skill guides the implementation of image generation functionality using the z-ai-web-dev-sdk package and CLI tool, enabling creation of high-quality images from text descriptions.

Skills Path

Skill Location: {project_path}/skills/image-generation

this skill is located at above path in your project.

Reference Scripts: Example test scripts are available in the {Skill Location}/scripts/ directory for quick testing and reference. See {Skill Location}/scripts/image-generation.ts for a working example.

Overview

Image Generation allows you to build applications that create visual content from text prompts using AI models, enabling creative workflows, design automation, and visual content production.

IMPORTANT: z-ai-web-dev-sdk MUST be used in backend code only. Never use it in client-side code.

Prerequisites

The z-ai-web-dev-sdk package is already installed. Import it as shown in the examples below.

Basic Image Generation
Simple Image Creation
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

async function generateImage(prompt, outputPath) {
  const zai = await ZAI.create();

  const response = await zai.images.generations.create({
    prompt: prompt,
    size: '1024x1024'
  });

  const imageBase64 = response.data[0].base64;
  
  // Save image
  const buffer = Buffer.from(imageBase64, 'base64');
  fs.writeFileSync(outputPath, buffer);
  
  console.log(`Image saved to ${outputPath}`);
  return outputPath;
}

// Usage
await generateImage(
  'A cute cat playing in the garden',
  './cat_image.png'
);

Multiple Image Sizes
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

// Supported sizes
const SUPPORTED_SIZES = [
  '1024x1024',  // Square
  '768x1344',   // Portrait
  '864x1152',   // Portrait
  '1344x768',   // Landscape
  '1152x864',   // Landscape
  '1440x720',   // Wide landscape
  '720x1440'    // Tall portrait
];

async function generateImageWithSize(prompt, size, outputPath) {
  if (!SUPPORTED_SIZES.includes(size)) {
    throw new Error(`Unsupported size: ${size}. Use one of: ${SUPPORTED_SIZES.join(', ')}`);
  }

  const zai = await ZAI.create();

  const response = await zai.images.generations.create({
    prompt: prompt,
    size: size
  });

  const imageBase64 = response.data[0].base64;
  const buffer = Buffer.from(imageBase64, 'base64');
  fs.writeFileSync(outputPath, buffer);

  return {
    path: outputPath,
    size: size,
    fileSize: buffer.length
  };
}

// Usage - Different sizes
await generateImageWithSize(
  'A beautiful landscape',
  '1344x768',
  './landscape.png'
);

await generateImageWithSize(
  'A portrait of a person',
  '768x1344',
  './portrait.png'
);

CLI Tool Usage

The z-ai CLI tool provides a convenient way to generate images directly from the command line.

Basic CLI Usage
# Generate image with full options
z-ai image --prompt "A beautiful landscape" --output "./image.png"

# Short form
z-ai image -p "A cute cat" -o "./cat.png"

# Specify size
z-ai image -p "A sunset" -o "./sunset.png" -s 1344x768

# Portrait orientation
z-ai image -p "A portrait" -o "./portrait.png" -s 768x1344

CLI Use Cases
# Website hero image
z-ai image -p "Modern tech office with diverse team collaborating" -o "./hero.png" -s 1440x720

# Product image
z-ai image -p "Sleek smartphone on minimalist desk, professional product photography" -o "./product.png" -s 1024x1024

# Blog post illustration
z-ai image -p "Abstract visualization of data flowing through networks" -o "./blog_header.png" -s 1344x768

# Social media content
z-ai image -p "Vibrant illustration of community connection" -o "./social.png" -s 1024x1024

# Website favicon/logo
z-ai image -p "Simple geometric logo with blue gradient, minimal design" -o "./logo.png" -s 1024x1024

# Background pattern
z-ai image -p "Subtle geometric pattern, pastel colors, website background" -o "./bg_pattern.png" -s 1440x720

Advanced Use Cases
Batch Image Generation
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
import path from 'path';

async function generateImageBatch(prompts, outputDir, size = '1024x1024') {
  const zai = await ZAI.create();

  // Ensure output directory exists
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }

  const results = [];

  for (let i = 0; i < prompts.length; i++) {
    try {
      const prompt = prompts[i];
      const filename = `image_${i + 1}.png`;
      const outputPath = path.join(outputDir, filename);

      const response = await zai.images.generations.create({
        prompt: prompt,
        size: size
      });

      const imageBase64 = response.data[0].base64;
      const buffer = Buffer.from(imageBase64, 'base64');
      fs.writeFileSync(outputPath, buffer);

      results.push({
        success: true,
        prompt: prompt,
        path: outputPath,
        size: buffer.length
      });

      console.log(`✓ Generated: ${filename}`);
    } catch (error) {
      results.push({
        success: false,
        prompt: prompts[i],
        error: error.message
      });

      console.error(`✗ Failed: ${prompts[i]} - ${error.message}`);
    }
  }

  return results;
}

// Usage
const prompts = [
  'A serene mountain landscape at sunset',
  'A futuristic city with flying cars',
  'An underwater coral reef teeming with life'
];

const results = await generateImageBatch(prompts, './generated-images');
console.log(`Generated ${results.filter(r => r.success).length} images`);

Image Generation Service
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
import path from 'path';
import crypto from 'crypto';

class ImageGenerationService {
  constructor(outputDir = './generated-images') {
    this.outputDir = outputDir;
    this.zai = null;
    this.cache = new Map();
  }

  async initialize() {
    this.zai = await ZAI.create();
    
    if (!fs.existsSync(this.outputDir)) {
      fs.mkdirSync(this.outputDir, { recursive: true });
    }
  }

  generateCacheKey(prompt, size) {
    return crypto
      .createHash('md5')
      .update(`${prompt}-${size}`)
      .digest('hex');
  }

  async generate(prompt, options = {}) {
    const {
      size = '1024x1024',
      useCache = true,
      filename = null
    } = options;

    // Check cache
    const cacheKey = this.generateCacheKey(prompt, size);
    
    if (useCache && this.cache.has(cacheKey)) {
      const cachedPath = this.cache.get(cacheKey);
      if (fs.existsSync(cachedPath)) {
        return {
          path: cachedPath,
          cached: true,
          prompt: prompt,
          size: size
        };
      }
    }

    // Generate new image
    const response = await this.zai.images.generations.create({
      prompt: prompt,
      size: size
    });

    const imageBase64 = response.data[0].base64;
    const buffer = Buffer.from(imageBase64, 'base64');

    // Determine output path
    const outputFilename = filename || `${cacheKey}.png`;
    const outputPath = path.join(this.outputDir, outputFilename);

    fs.writeFileSync(outputPath, buffer);

    // Cache result
    if (useCache) {
      this.cache.set(cacheKey, outputPath);
    }

    return {
      path: outputPath,
      cached: false,
      prompt: prompt,
      size: size,
      fileSize: buffer.length
    };
  }

  clearCache() {
    this.cache.clear();
  }

  getCacheSize() {
    return this.cache.size;
  }
}

// Usage
const service = new ImageGenerationService();
await service.initialize();

const result = await service.generate(
  'A modern office space',
  { size: '1440x720' }
);

console.log('Generated:', result.path);

Website Asset Generator
# Using CLI for quick website asset generation
z-ai image -p "Modern tech hero banner, blue gradient" -o "./assets/hero.png" -s 1440x720
z-ai image -p "Team collaboration illustration" -o "./assets/team.png" -s 1344x768
z-ai image -p "Simple geometric logo" -o "./assets/logo.png" -s 1024x1024

Best Practices
1. Effective Prompt Engineering
function buildEffectivePrompt(subject, style, details = []) {
  const components = [
    subject,
    style,
    ...details,
    'high quality',
    'detailed'
  ];

  return components.filter(Boolean).join(', ');
}

// Usage
const prompt = buildEffectivePrompt(
  'mountain landscape',
  'oil painting style',
  ['sunset lighting', 'dramatic clouds', 'reflection in lake']
);

// Result: "mountain landscape, oil painting style, sunset lighting, dramatic clouds, reflection in lake, high quality, detailed"

2. Size Selection Helper
function selectOptimalSize(purpose) {
  const sizeMap = {
    'hero-banner': '1440x720',
    'blog-header': '1344x768',
    'social-square': '1024x1024',
    'portrait': '768x1344',
    'product': '1024x1024',
    'landscape': '1344x768',
    'mobile-banner': '720x1440',
    'thumbnail': '1024x1024'
  };

  return sizeMap[purpose] || '1024x1024';
}

// Usage
const size = selectOptimalSize('hero-banner');
await generateImage('website hero image', size, './hero.png');

3. Error Handling
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

async function safeGenerateImage(prompt, size, outputPath, retries = 3) {
  let lastError;

  for (let attempt = 1; attempt <= retries; attempt++) {
    try {
      const zai = await ZAI.create();

      const response = await zai.images.generations.create({
        prompt: prompt,
        size: size
      });

      if (!response.data || !response.data[0] || !response.data[0].base64) {
        throw new Error('Invalid response from image generation API');
      }

      const imageBase64 = response.data[0].base64;
      const buffer = Buffer.from(imageBase64, 'base64');
      fs.writeFileSync(outputPath, buffer);

      return {
        success: true,
        path: outputPath,
        attempts: attempt
      };
    } catch (error) {
      lastError = error;
      console.error(`Attempt ${attempt} failed:`, error.message);

      if (attempt < retries) {
        // Wait before retry (exponential backoff)
        await new Promise(resolve => setTimeout(resolve, 1000 * attempt));
      }
    }
  }

  return {
    success: false,
    error: lastError.message,
    attempts: retries
  };
}

Common Use Cases
Website Design: Generate hero images, backgrounds, and visual assets
Marketing Materials: Create social media graphics and promotional images
Product Visualization: Generate product mockups and variations
Content Creation: Produce blog post illustrations and thumbnails
Brand Assets: Create logos, icons, and brand imagery
UI/UX Design: Generate interface elements and illustrations
Game Development: Create concept art and game assets
E-commerce: Generate product images and lifestyle shots
Integration Examples
Express.js API Endpoint
import express from 'express';
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
import path from 'path';

const app = express();
app.use(express.json());
app.use('/images', express.static('generated-images'));

let zaiInstance;
const outputDir = './generated-images';

async function initZAI() {
  zaiInstance = await ZAI.create();
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }
}

app.post('/api/generate-image', async (req, res) => {
  try {
    const { prompt, size = '1024x1024' } = req.body;

    if (!prompt) {
      return res.status(400).json({ error: 'Prompt is required' });
    }

    const response = await zaiInstance.images.generations.create({
      prompt: prompt,
      size: size
    });

    const imageBase64 = response.data[0].base64;
    const buffer = Buffer.from(imageBase64, 'base64');
    
    const filename = `img_${Date.now()}.png`;
    const filepath = path.join(outputDir, filename);
    fs.writeFileSync(filepath, buffer);

    res.json({
      success: true,
      imageUrl: `/images/${filename}`,
      prompt: prompt,
      size: size
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
});

initZAI().then(() => {
  app.listen(3000, () => {
    console.log('Image generation API running on port 3000');
  });
});

CLI Integration in Scripts
Shell Script Example
#!/bin/bash

# Generate website assets using CLI
echo "Generating website assets..."

z-ai image -p "Modern tech hero banner, blue gradient" -o "./assets/hero.png" -s 1440x720
z-ai image -p "Team collaboration illustration" -o "./assets/team.png" -s 1344x768
z-ai image -p "Simple geometric logo" -o "./assets/logo.png" -s 1024x1024

echo "Assets generated successfully!"

Troubleshooting

Issue: "SDK must be used in backend"

Solution: Ensure z-ai-web-dev-sdk is only used in server-side code

Issue: Invalid size parameter

Solution: Use only supported sizes: 1024x1024, 768x1344, 864x1152, 1344x768, 1152x864, 1440x720, 720x1440

Issue: Generated image doesn't match prompt

Solution: Make prompts more specific and descriptive. Include style, details, and quality terms

Issue: CLI command not found

Solution: Ensure z-ai CLI is properly installed and in PATH

Issue: Image file is corrupted

Solution: Verify base64 decoding and file writing are correct
Prompt Engineering Tips
Good Prompts
✓ "Professional product photography of wireless headphones, white background, studio lighting, high quality"
✓ "Mountain landscape at golden hour, oil painting style, dramatic clouds, detailed"
✓ "Modern minimalist logo for tech company, blue and white, geometric shapes"
Poor Prompts
✗ "headphones"
✗ "picture of mountains"
✗ "logo"
Prompt Components
Subject: What you want to see
Style: Art style, photography style, etc.
Details: Specific elements, colors, mood
Quality: "high quality", "detailed", "professional"
Supported Image Sizes
1024x1024 - Square
768x1344 - Portrait
864x1152 - Portrait
1344x768 - Landscape
1152x864 - Landscape
1440x720 - Wide landscape
720x1440 - Tall portrait
Remember
Always use z-ai-web-dev-sdk in backend code only
The SDK is already installed - import as shown
CLI tool is available for quick image generation
Supported sizes are specific - use the provided list
Base64 images need to be decoded before saving
Consider caching for repeated prompts
Implement retry logic for production applications
Use descriptive prompts for better results
Weekly Installs
29
Repository
answerzhao/agent-skills
GitHub Stars
26
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass