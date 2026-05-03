---
title: llava
url: https://skills.sh/davila7/claude-code-templates/llava
---

# llava

skills/davila7/claude-code-templates/llava
llava
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill llava
SKILL.md
LLaVA - Large Language and Vision Assistant

Open-source vision-language model for conversational image understanding.

When to use LLaVA

Use when:

Building vision-language chatbots
Visual question answering (VQA)
Image description and captioning
Multi-turn image conversations
Visual instruction following
Document understanding with images

Metrics:

23,000+ GitHub stars
GPT-4V level capabilities (targeted)
Apache 2.0 License
Multiple model sizes (7B-34B params)

Use alternatives instead:

GPT-4V: Highest quality, API-based
CLIP: Simple zero-shot classification
BLIP-2: Better for captioning only
Flamingo: Research, not open-source
Quick start
Installation
# Clone repository
git clone https://github.com/haotian-liu/LLaVA
cd LLaVA

# Install
pip install -e .

Basic usage
from llava.model.builder import load_pretrained_model
from llava.mm_utils import get_model_name_from_path, process_images, tokenizer_image_token
from llava.constants import IMAGE_TOKEN_INDEX, DEFAULT_IMAGE_TOKEN
from llava.conversation import conv_templates
from PIL import Image
import torch

# Load model
model_path = "liuhaotian/llava-v1.5-7b"
tokenizer, model, image_processor, context_len = load_pretrained_model(
    model_path=model_path,
    model_base=None,
    model_name=get_model_name_from_path(model_path)
)

# Load image
image = Image.open("image.jpg")
image_tensor = process_images([image], image_processor, model.config)
image_tensor = image_tensor.to(model.device, dtype=torch.float16)

# Create conversation
conv = conv_templates["llava_v1"].copy()
conv.append_message(conv.roles[0], DEFAULT_IMAGE_TOKEN + "\nWhat is in this image?")
conv.append_message(conv.roles[1], None)
prompt = conv.get_prompt()

# Generate response
input_ids = tokenizer_image_token(prompt, tokenizer, IMAGE_TOKEN_INDEX, return_tensors='pt').unsqueeze(0).to(model.device)

with torch.inference_mode():
    output_ids = model.generate(
        input_ids,
        images=image_tensor,
        do_sample=True,
        temperature=0.2,
        max_new_tokens=512
    )

response = tokenizer.decode(output_ids[0], skip_special_tokens=True).strip()
print(response)

Available models
Model	Parameters	VRAM	Quality
LLaVA-v1.5-7B	7B	~14 GB	Good
LLaVA-v1.5-13B	13B	~28 GB	Better
LLaVA-v1.6-34B	34B	~70 GB	Best
# Load different models
model_7b = "liuhaotian/llava-v1.5-7b"
model_13b = "liuhaotian/llava-v1.5-13b"
model_34b = "liuhaotian/llava-v1.6-34b"

# 4-bit quantization for lower VRAM
load_4bit = True  # Reduces VRAM by ~4×

CLI usage
# Single image query
python -m llava.serve.cli \
    --model-path liuhaotian/llava-v1.5-7b \
    --image-file image.jpg \
    --query "What is in this image?"

# Multi-turn conversation
python -m llava.serve.cli \
    --model-path liuhaotian/llava-v1.5-7b \
    --image-file image.jpg
# Then type questions interactively

Web UI (Gradio)
# Launch Gradio interface
python -m llava.serve.gradio_web_server \
    --model-path liuhaotian/llava-v1.5-7b \
    --load-4bit  # Optional: reduce VRAM

# Access at http://localhost:7860

Multi-turn conversations
# Initialize conversation
conv = conv_templates["llava_v1"].copy()

# Turn 1
conv.append_message(conv.roles[0], DEFAULT_IMAGE_TOKEN + "\nWhat is in this image?")
conv.append_message(conv.roles[1], None)
response1 = generate(conv, model, image)  # "A dog playing in a park"

# Turn 2
conv.messages[-1][1] = response1  # Add previous response
conv.append_message(conv.roles[0], "What breed is the dog?")
conv.append_message(conv.roles[1], None)
response2 = generate(conv, model, image)  # "Golden Retriever"

# Turn 3
conv.messages[-1][1] = response2
conv.append_message(conv.roles[0], "What time of day is it?")
conv.append_message(conv.roles[1], None)
response3 = generate(conv, model, image)

Common tasks
Image captioning
question = "Describe this image in detail."
response = ask(model, image, question)

Visual question answering
question = "How many people are in the image?"
response = ask(model, image, question)

Object detection (textual)
question = "List all the objects you can see in this image."
response = ask(model, image, question)

Scene understanding
question = "What is happening in this scene?"
response = ask(model, image, question)

Document understanding
question = "What is the main topic of this document?"
response = ask(model, document_image, question)

Training custom model
# Stage 1: Feature alignment (558K image-caption pairs)
bash scripts/v1_5/pretrain.sh

# Stage 2: Visual instruction tuning (150K instruction data)
bash scripts/v1_5/finetune.sh

Quantization (reduce VRAM)
# 4-bit quantization
tokenizer, model, image_processor, context_len = load_pretrained_model(
    model_path="liuhaotian/llava-v1.5-13b",
    model_base=None,
    model_name=get_model_name_from_path("liuhaotian/llava-v1.5-13b"),
    load_4bit=True  # Reduces VRAM ~4×
)

# 8-bit quantization
load_8bit=True  # Reduces VRAM ~2×

Best practices
Start with 7B model - Good quality, manageable VRAM
Use 4-bit quantization - Reduces VRAM significantly
GPU required - CPU inference extremely slow
Clear prompts - Specific questions get better answers
Multi-turn conversations - Maintain conversation context
Temperature 0.2-0.7 - Balance creativity/consistency
max_new_tokens 512-1024 - For detailed responses
Batch processing - Process multiple images sequentially
Performance
Model	VRAM (FP16)	VRAM (4-bit)	Speed (tokens/s)
7B	~14 GB	~4 GB	~20
13B	~28 GB	~8 GB	~12
34B	~70 GB	~18 GB	~5

On A100 GPU

Benchmarks

LLaVA achieves competitive scores on:

VQAv2: 78.5%
GQA: 62.0%
MM-Vet: 35.4%
MMBench: 64.3%
Limitations
Hallucinations - May describe things not in image
Spatial reasoning - Struggles with precise locations
Small text - Difficulty reading fine print
Object counting - Imprecise for many objects
VRAM requirements - Need powerful GPU
Inference speed - Slower than CLIP
Integration with frameworks
LangChain
from langchain.llms.base import LLM

class LLaVALLM(LLM):
    def _call(self, prompt, stop=None):
        # Custom LLaVA inference
        return response

llm = LLaVALLM()

Gradio App
import gradio as gr

def chat(image, text, history):
    response = ask_llava(model, image, text)
    return response

demo = gr.ChatInterface(
    chat,
    additional_inputs=[gr.Image(type="pil")],
    title="LLaVA Chat"
)
demo.launch()

Resources
GitHub: https://github.com/haotian-liu/LLaVA ⭐ 23,000+
Paper: https://arxiv.org/abs/2304.08485
Demo: https://llava.hliu.cc
Models: https://huggingface.co/liuhaotian
License: Apache 2.0
Weekly Installs
270
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn