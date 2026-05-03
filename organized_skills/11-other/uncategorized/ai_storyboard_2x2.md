---
rating: ⭐⭐⭐
title: ai-storyboard-2x2
url: https://skills.sh/guia-matthieu/clawfu-skills/ai-storyboard-2x2
---

# ai-storyboard-2x2

skills/guia-matthieu/clawfu-skills/ai-storyboard-2x2
ai-storyboard-2x2
Installation
$ npx skills add https://github.com/guia-matthieu/clawfu-skills --skill ai-storyboard-2x2
SKILL.md
AI Storyboard 2x2

Créez des storyboards visuellement cohérents en utilisant la technique des 2x2 Grid Shots de PJ Ace, garantissant éclairage, personnages et décors uniformes entre les plans.

When to Use This Skill
Après avoir finalisé un script vidéo - Transformer le concept en visuels
Besoin de cohérence visuelle - Personnages et éclairage constants entre les plans
Préparer des assets pour animation - Frames prêtes pour Veo, Runway, Kling
Présenter un storyboard client - Visualisation avant production
Planifier des transitions fluides - Séquencer les plans wide → closeup
Methodology Foundation

Source: PJ Ace - AI Video Production Workflow (2025-2026)

Core Principle: "En générant 4 images dans un grid 2x2, le modèle maintient automatiquement la cohérence d'éclairage, de personnage et de lieu entre les shots. Vous obtenez une séquence cinématique au lieu de 4 images disparates."

Why This Matters: Les modèles de génération d'images traitent chaque prompt indépendamment. En demandant un grid 2x2, vous forcez le modèle à créer une scène cohérente sous 4 angles différents, résolvant le problème majeur de l'incohérence visuelle.

What Claude Does vs What You Decide
Claude Does	You Decide
Structures production workflow	Final creative direction
Suggests technical approaches	Equipment and tool choices
Creates templates and checklists	Quality standards
Identifies best practices	Brand/voice decisions
Generates script outlines	Final script approval
What This Skill Does
Génère des prompts 2x2 grid - Structure optimale pour la cohérence
Organise le layout séquentiel - Ordre des plans dans Figma
Guide le cropping et upscaling - Extraire les frames individuelles
Planifie les transitions - Wide → Closeup pour masquer les cuts
Prépare le handoff animation - Frames prêtes pour la génération vidéo
How to Use
Créer un storyboard depuis un script
J'ai ce script structuré: [coller script]. Aide-moi à créer le storyboard avec la technique 2x2 grid.

Générer des prompts pour une scène spécifique
Je dois visualiser cette scène: [description]. Génère-moi le prompt 2x2 grid et explique comment l'utiliser.

Planifier une séquence d'action
J'ai une séquence d'action: [description mouvement]. Crée les 4 frames du grid pour capturer le mouvement.

Instructions
Step 1: Analyser le script et identifier les scènes clés
## Analyse Scène par Scène

**Script source:** [Référence au script]

| Scène | Durée | Type de plan | Éléments clés | Grids nécessaires |
|-------|-------|--------------|---------------|-------------------|
| 1 | 8s | Establishing | Personnage + Décor | 1 grid (4 angles) |
| 2 | 8s | Action | Mouvement | 1-2 grids |
| 3 | 8s | Dialogue | 2 personnages | 1 grid par perso |
| 4 | 8s | Product shot | Produit + Logo | 1 grid |

**Total grids estimés:** [X]


Règles d'estimation:

1 grid = 4 shots d'une même scène
Scène simple = 1 grid
Scène avec mouvement = 2 grids (début/fin)
Scène avec plusieurs personnages = 1 grid par personnage
Step 2: Créer les prompts 2x2 Grid

Le format de prompt clé:

## Prompt Template 2x2 Grid

Create a 2x2 grid shot from [STYLE] film.

Top-left: [SHOT 1 - Usually establishing/wide]
Top-right: [SHOT 2 - Medium shot or different angle]
Bottom-left: [SHOT 3 - Close-up or action]
Bottom-right: [SHOT 4 - Detail or reaction]

Scene description: [CONTEXT GLOBAL]
Lighting: [ÉCLAIRAGE]
Color palette: [COULEURS]
Camera style: [STYLE CAMÉRA]


Exemple concret:

Create a 2x2 grid shot from a premium Nike-style commercial.

Top-left: Wide shot of a modern minimalist office, morning light through large windows, a confident woman in her 30s standing by the desk
Top-right: Medium shot of the same woman, side profile, looking at laptop screen
Bottom-left: Close-up of her hands on keyboard (avoid finger details, focus on gesture)
Bottom-right: Over-the-shoulder shot showing the screen with abstract productivity graphics

Scene: Professional woman starting her productive morning routine
Lighting: Golden hour morning light, soft shadows, rim light from windows
Color palette: Warm neutrals, touches of blue from screen
Camera style: Cinematic, shallow depth of field, 35mm lens look

Step 3: Organiser le layout Figma
## Layout Storyboard

### Structure recommandée

┌─────────────────────────────────────────────────────────────┐
│ SCÈNE 1: [Nom]                                              │
├─────────────┬─────────────┬─────────────┬─────────────┬─────┤
│  Shot 1.1   │  Shot 1.2   │  Shot 1.3   │  Shot 1.4   │ VO  │
│  [Wide]     │  [Medium]   │  [Close]    │  [Detail]   │[txt]│
│  0:00-0:02  │  0:02-0:04  │  0:04-0:06  │  0:06-0:08  │     │
├─────────────┴─────────────┴─────────────┴─────────────┴─────┤
│ SCÈNE 2: [Nom]                                              │
├─────────────┬─────────────┬─────────────┬─────────────┬─────┤
│  Shot 2.1   │  Shot 2.2   │  Shot 2.3   │  Shot 2.4   │ VO  │
│  ...        │  ...        │  ...        │  ...        │[txt]│
└─────────────┴─────────────┴─────────────┴─────────────┴─────┘

### Colonnes
- Frame (image)
- Timing
- Type de plan (W/M/CU/D)
- Notes techniques
- Voiceover


Tips Figma:

Utiliser des frames de 1920x1080 ou 1080x1920 selon format
Nommer les layers: S01-Shot01-Wide
Grouper par scène
Ajouter des annotations pour les transitions
Step 4: Extraire et upscaler les frames
## Workflow d'extraction

### Depuis le 2x2 grid:

1. **Cropper** chaque quadrant individuellement
   - Top-left → Shot_01.png
   - Top-right → Shot_02.png
   - Bottom-left → Shot_03.png
   - Bottom-right → Shot_04.png

2. **Upscaler** chaque frame

   Prompt d'upscale (dans ChatGPT/Ideogram):


Upscale this image to high resolution, maintaining all details. Add subtle film grain for cinematic quality. Enhance sharpness while keeping natural look. Output: 1920x1080 or higher


3. **Vérifier la cohérence**
- Éclairage identique?
- Personnage reconnaissable?
- Palette de couleurs consistante?
- Si non → re-générer le grid

Step 5: Planifier les transitions
## Règles de Transition

### DO: Transitions qui fonctionnent
| Transition | Exemple | Pourquoi ça marche |
|------------|---------|-------------------|
| Wide → Closeup | Establishing → Face | Cache les incohérences de mouvement |
| Closeup → Wide | Detail → Context | Révèle l'environnement |
| Same angle, action continue | Running frame 1 → 2 | Mouvement fluide si même grid |
| Cut on action | Bras levé → Bras en haut | Le mouvement masque le cut |

### DON'T: Transitions problématiques
| Transition | Problème | Solution |
|------------|----------|----------|
| Wide → Wide même scène | Jump cut visible | Insérer un closeup entre |
| 2 personnages face-à-face | Dialogue difficile | Alterner champ/contre-champ |
| Mouvement continu long | Incohérence | Couper en segments de 4-8s |

### Technique de continuité
Pour lier deux clips:
1. Prendre la **dernière frame** du clip A
2. L'utiliser comme **première frame** du clip B (image-to-video)
3. Ou l'upscaler et créer un closeup pour la transition

Step 6: Output final - Storyboard complet
## Storyboard Final: [Titre]

**Projet:** [Nom]
**Durée:** [X] secondes
**Grids générés:** [Y]
**Frames totales:** [Z]

---

### Séquence Complète

| # | Frame | Timing | Type | Prompt utilisé | Transition vers |
|---|-------|--------|------|----------------|-----------------|
| 1 | [thumb] | 0:00-0:02 | Wide | Grid1-TL | Cut to #2 |
| 2 | [thumb] | 0:02-0:04 | Medium | Grid1-TR | Dissolve to #3 |
| 3 | [thumb] | 0:04-0:06 | CU | Grid1-BL | Cut on action to #4 |
| ... | ... | ... | ... | ... | ... |

---

### Assets générés

📁 Storyboard_[Projet]/
├── grids/
│   ├── grid_scene01.png
│   ├── grid_scene02.png
│   └── ...
├── frames/
│   ├── S01_shot01_wide.png
│   ├── S01_shot02_medium.png
│   └── ...
├── upscaled/
│   ├── S01_shot01_wide_4k.png
│   └── ...
└── layout/
    └── storyboard_figma.fig

---

**Prêt pour:** ai-video-prompting (animation)

Examples
Example 1: Séquence produit e-commerce

Context: Storyboard pour une pub de sneakers, style dynamique

Input:

J'ai une scène de 8 secondes: un runner urbain qui court dans la rue au lever du soleil, portant nos nouvelles sneakers. Crée le grid 2x2.

Output:

Grid Prompt: Urban Runner Scene
Create a 2x2 grid shot from a Nike-style athletic commercial.

Top-left: Wide shot of empty urban street at sunrise, golden light,
modern architecture, a male runner (30s, athletic build, black running
outfit) approaching from distance

Top-right: Medium tracking shot of the same runner mid-stride,
side profile, sneakers visible, motion blur on background,
determination on face

Bottom-left: Low angle close-up of the sneakers hitting pavement,
dynamic splash if wet ground, focus on shoe design and movement

Bottom-right: Front-facing medium shot of runner, morning sun
behind creating rim light, confident expression, urban skyline
in soft focus background

Scene: Athletic morning run through city streets
Lighting: Golden hour sunrise, long shadows, warm tones with
cool shadows
Color palette: Orange/gold highlights, blue shadows,
neutral grays of urban environment
Camera style: Cinematic, anamorphic lens flare,
high frame rate feel frozen in stills

Extraction Plan
Position	Nom fichier	Usage	Durée suggérée
Top-left	runner_wide_approach.png	Establishing shot	2s
Top-right	runner_medium_profile.png	Build energy	2s
Bottom-left	sneaker_closeup_action.png	Product focus	2s
Bottom-right	runner_hero_frontface.png	Emotional payoff	2s
Transition Notes
Wide → Medium: Cut naturel, même direction de mouvement
Medium → Closeup sneaker: Cut on footstrike (action)
Closeup → Hero front: Jump emotionnel, acceptable car produit → visage

Why this works: Les 4 shots partagent le même éclairage (sunrise), le même personnage, et racontent une micro-histoire en 4 beats. Le closeup sneaker (bottom-left) est stratégiquement placé pour le focus produit.

Example 2: Séquence narrative avec transformation

Context: Scène "avant/après" pour un produit de productivité

Input:

Je dois montrer une transformation: bureau chaotique → bureau organisé après utilisation de notre app. Crée 2 grids (avant et après).

Output:

Grid 1: "Before" - Chaos
Create a 2x2 grid shot from a comedy-drama office scene.

Top-left: Wide shot of messy home office, papers everywhere,
multiple coffee cups, stressed person (woman, 30s, tired expression)
at cluttered desk, harsh overhead lighting

Top-right: Medium shot of the same woman, head in hands,
laptop showing 47 browser tabs, notification badges everywhere

Bottom-left: Close-up of desk surface chaos - sticky notes overlapping,
tangled cables, cold coffee, crumpled papers

Bottom-right: Over-shoulder shot of laptop screen showing
overwhelming to-do list, calendar with conflicts,
red notification badges

Scene: Overwhelming work-from-home chaos moment
Lighting: Harsh fluorescent overhead, unflattering,
slight greenish tint
Color palette: Desaturated, muddy colors,
visual noise and clutter
Camera style: Handheld feel, slightly tilted,
documentary/mockumentary style

Grid 2: "After" - Harmony
Create a 2x2 grid shot from a premium Apple-style commercial.

Top-left: Wide shot of the same home office, now minimalist and
organized, warm morning light, the same woman (now relaxed,
slight smile) at clean desk with single monitor

Top-right: Medium shot of her confidently working,
good posture, peaceful expression, plant in background

Bottom-left: Close-up of clean desk surface -
single notebook, quality pen, artisan coffee in nice mug,
laptop with clean interface

Bottom-right: Over-shoulder shot of laptop screen showing
clean task management interface (our app),
clear priorities, green checkmarks

Scene: Productive, peaceful work-from-home flow state
Lighting: Warm golden hour light from window,
soft and flattering
Color palette: Warm whites, soft greens,
touches of wood and natural materials
Camera style: Smooth, stable,
premium commercial cinematography

Storyboard Layout
BEFORE SEQUENCE (0:00 - 0:08)
┌─────────────┬─────────────┬─────────────┬─────────────┐
│ G1-Wide     │ G1-Medium   │ G1-CU desk  │ G1-Screen   │
│ Chaos room  │ Stressed    │ Messy       │ Overwhelm   │
│ 0:00-0:02   │ 0:02-0:04   │ 0:04-0:06   │ 0:06-0:08   │
└─────────────┴─────────────┴─────────────┴─────────────┘
           ↓ TRANSITION: Match cut on screen → app interface

AFTER SEQUENCE (0:08 - 0:16)
┌─────────────┬─────────────┬─────────────┬─────────────┐
│ G2-Screen   │ G2-CU desk  │ G2-Medium   │ G2-Wide     │
│ Clean app   │ Organized   │ Confident   │ Zen room    │
│ 0:08-0:10   │ 0:10-0:12   │ 0:12-0:14   │ 0:14-0:16   │
└─────────────┴─────────────┴─────────────┴─────────────┘

Transition Strategy
De	Vers	Technique	Pourquoi
G1-Screen (chaos)	G2-Screen (clean)	Match cut	Même cadrage, transformation visible
G2-Screen	G2-CU desk	Zoom out	Révèle l'environnement transformé
G2-Medium	G2-Wide	Pull back	Payoff émotionnel, satisfaction

Why this works: Les deux grids sont construits en miroir inversé (chaos→ordre). La transition match-cut sur l'écran crée un moment "magie" de transformation. L'ordre des plans After est inversé (screen→wide) pour créer un crescendo de révélation.

Checklists & Templates
Checklist Storyboard 2x2
## Validation Storyboard

### Par Grid
- [ ] 4 shots cohérents (éclairage, couleur, personnage)
- [ ] Variété de plans (wide, medium, CU, detail)
- [ ] Prompt inclut: scène, lighting, palette, camera style
- [ ] Personnage reconnaissable dans tous les shots

### Par Séquence
- [ ] Transitions planifiées (pas de wide→wide)
- [ ] Timing assigné à chaque frame
- [ ] Voiceover aligné avec les visuels
- [ ] Direction de mouvement cohérente

### Assets
- [ ] Grids sauvegardés en haute résolution
- [ ] Frames individuelles croppées
- [ ] Frames upscalées pour animation
- [ ] Layout Figma organisé

### Prêt pour animation
- [ ] Frames nommées clairement (S01_shot01_wide.png)
- [ ] Notes de transition documentées
- [ ] Durées définies
- [ ] Handoff vers ai-video-prompting

Template Prompt 2x2
## 2x2 Grid Prompt

Create a 2x2 grid shot from [GENRE/STYLE] [TYPE: film/commercial/etc].

Top-left: [SHOT TYPE] of [SUBJECT], [ACTION], [KEY DETAILS]

Top-right: [SHOT TYPE] of [SUBJECT], [ANGLE CHANGE], [CONTINUITY ELEMENT]

Bottom-left: [SHOT TYPE] [FOCUS AREA], [DETAIL TO HIGHLIGHT]

Bottom-right: [SHOT TYPE] [EMOTIONAL BEAT], [PAYOFF VISUAL]

Scene: [OVERALL CONTEXT - 1 sentence]
Lighting: [LIGHT SOURCE, QUALITY, DIRECTION]
Color palette: [DOMINANT COLORS, MOOD]
Camera style: [LENS, MOVEMENT STYLE, FILM LOOK]

Types de Plans (Référence)
## Shot Types pour Prompts

| Abbr | Nom | Description | Usage |
|------|-----|-------------|-------|
| EWS | Extreme Wide | Paysage, contexte | Establishing |
| WS | Wide Shot | Personnage entier + environnement | Context |
| MWS | Medium Wide | Personnage genoux-up | Action |
| MS | Medium Shot | Taille-up | Dialogue |
| MCU | Medium Close-up | Poitrine-up | Émotion |
| CU | Close-up | Visage | Intensité |
| ECU | Extreme Close-up | Détail (œil, objet) | Emphasis |
| OTS | Over-the-Shoulder | Par-dessus épaule | Dialogue |
| POV | Point of View | Vue subjective | Immersion |
| Insert | Insert/Cutaway | Détail objet | Information |

Skill Boundaries
What This Skill Does Well
Structuring audio production workflows
Providing technical guidance
Creating quality checklists
Suggesting creative approaches
What This Skill Cannot Do
Replace audio engineering expertise
Make subjective creative decisions
Access or edit audio files directly
Guarantee commercial success
References
PJ Ace. "233M Views in 3 Days: The David Beckham AI Workflow" - Marketing Against the Grain (2026)
MKTG Skills - Étude Écosystème Vidéo IA
Block, Bruce. "The Visual Story" - Visual structure principles
Katz, Steven D. "Film Directing Shot by Shot" - Storyboarding techniques
Related Skills
ai-video-concept - Étape précédente: script structuré
ai-video-prompting - Étape suivante: prompts d'animation
storytelling-storybrand - Structure narrative
Skill Metadata
Mode: cyborg
name: ai-storyboard-2x2
category: video
subcategory: pre-production
version: 1.0
author: MKTG Skills
source_expert: PJ Ace
source_work: AI Video Production Workflow
difficulty: intermediate
estimated_value: $1000-3000 (storyboard development)
tags: [video, ai, storyboard, visual, 2x2-grid, figma, production]
created: 2026-01-25
updated: 2026-01-25

Weekly Installs
98
Repository
guia-matthieu/c…u-skills
GitHub Stars
85
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass